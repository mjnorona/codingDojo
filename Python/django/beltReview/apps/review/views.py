
from django.contrib import messages
from django.shortcuts import render, redirect
from .models import User, Author, Book, Review

# Create your views here.
def index(request):
    list = User.objects.all()
    for i in list:
        print i.email
    return render(request, 'review/index.html')


def register(request):

    if request.method == "POST":
        values = User.objects.register(request.POST['first'], request.POST['last'], request.POST['email'], request.POST['password'], request.POST['confirm'])
        successful = True

        if values[0]:
            if not values[1]:
                messages.error(request, 'First Name can only contain letters and must have at least 2 characters')
                successful = False
            if not values[2]:
                messages.error(request, 'Last Name can only contain letters and must have at least 2 characters')
                successful = False
            if not values[3]:
                messages.error(request, 'Email is not valid')
                successful = False
            if not values[4]:
                messages.error(request, 'Password must be at least 8 characters')
                successful = False
            if not values[5]:
                messages.error(request, 'Passwords do not match')
                successful = False

            if successful:
                user = User.objects.create(first_name=request.POST['first'], last_name=request.POST['last'],
                                        email=request.POST['email'], password=request.POST['password'])
                request.session['id'] = user.id
                print user.id
                return redirect('/books')
            else:
                return redirect('/')
        else:
            messages.error(request, 'User with email already exists')
            return redirect('/')


def login(request):
    if request.method == "POST":
        login = User.objects.login(request.POST['email'], request.POST['password'])
        print login
        if login[0]:
            request.session['id'] = login[1]
            return redirect('/books')
        else:
            messages.error(request, 'Email or password is incorrect')
            return redirect('/')

def books(request):
    try:
        # Review.objects.all().delete()
        # Book.objects.all().delete()
        # Author.objects.all().delete()
        user = User.objects.get(id = request.session['id'])
        books = Book.objects.all()
        reviews = Review.objects.all().order_by('-created_at')
        content = {
            'name' : user.first_name,
            'reviews': reviews,
            'books': books, 
            'id': request.session['id']
        }
        
        return render(request, 'review/books.html', content)
    except KeyError:
        return redirect('/')

def book_add(request):
    authors = Author.objects.all()
    content = { 'authors': authors}
    return render(request, 'review/books_add.html', content)

def review_delete(request, id):
    query = Review.objects.filter(id = id)
    print query[0].book.title
    count = Review.objects.filter(book = Book.objects.filter(title = query[0].book.title)).count()
    if count == 1:
        Book.objects.filter(id__in = query.values('book_id')).delete()
    Review.objects.filter(id = id).delete()
    return redirect('/books')

def book_submit(request):
    if request.method == "POST":
        author = ""
        book = ""
        try:
            #choosing between existing author or making new one
            if not len(request.POST['authorEnter']) == 0:
                author = Author.objects.create(name = request.POST['authorEnter'])
                print "New Author " + author.name
            else: 
                author = Author.objects.get(id = request.POST['author'])
                print "Existing Author " + author.name
        except:
            author = Author.objects.get(name = request.POST['author'])
            print "Existing Author " + author.name
        #if the book exists don't make a new one, otherwise make new book
        if not len(Book.objects.filter(title = request.POST['title'])) == 0:
            book = Book.objects.get(title = request.POST['title'])
            print book.title
        else:
            book = Book.objects.create(title = request.POST['title'], author = author)

        review = Review.objects.create(content = request.POST['review'], rating = request.POST['rating'], book = book, user = User.objects.get(id = request.session['id']))
        print review.content, book.author.name
    return redirect('book_reviews', id = book.id)

def book_reviews(request, id):
    book = Book.objects.get(id = id)
    reviews = Review.objects.filter(book = Book.objects.get(id = book.id))
    print book.title
    content = {
        "title": book.title,
        'author': book.author.name,
        'reviews': reviews,
        'user' : request.session['id']
    }
    return render(request, 'review/book_reviews.html', content)

def user_reviews(request, id):
    user = User.objects.get(id = id)
    review_count = Review.objects.filter(user = user).count()
    query = Review.objects.filter(user = id)
    books = Book.objects.filter(id__in = query.values('book_id'))
    content = {
        'user': user,
        'count': review_count,
        'books': books
    }
    
    return render(request, 'review/user_reviews.html', content)

def logout(request):
    request.session.pop('id', None)
    return redirect('/')