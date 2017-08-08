 // Require the Express Module
var express = require('express');
// Create an Express App
var app = express();
// Require body-parser (to receive post data from clients)
var bodyParser = require('body-parser');
// Integrate body-parser with our App
app.use(bodyParser.urlencoded({ extended: true }));
// Require path
var path = require('path');
// Setting our Static Folder Directory
app.use(express.static(path.join(__dirname, './static')));
// Setting our Views Folder Directory
app.set('views', path.join(__dirname, './views'));
// Setting our View Engine set to EJS
app.set('view engine', 'ejs');

var mongoose = require('mongoose');

mongoose.connect('mongodb://localhost/mongooses');
var MongooseSchema = new mongoose.Schema({
    name: String,
    description: String,
})
mongoose.model('Mongoose', MongooseSchema)
var Mongoose = mongoose.model('Mongoose')
mongoose.Promise = global.Promise;

app.get('/', function(req,res){
    Mongoose.find({}, function(err,mongooses){
        if (err) {
            console.log()
            console.log("something went wrong in /")
        } else {
            console.log(mongooses)
            res.render('index', {mongooses: mongooses})
        }
    })
    
})

app.get('/mongooses/new', function(req,res){
    console.log('going here')
    res.render('newMongoose')
})

app.get('/mongooses/:id', function(req,res){
    console.log("The mongoose id: ", req.params.id)
    
    Mongoose.find({_id: req.params.id}, function(err, mongooses){
        
        if (err){
            console.log('something went wrong in /mongooses/:id')
        } else {
            console.log(mongooses)
            res.render('displayMongoose', {mongoose: mongooses[0]})
        }
    })
    
})

app.get('/mongooses/new', function(req,res){
    console.log('going here')
    res.render('newMongoose')
})

app.post('/mongooses', function(req,res){
    console.log("post data: ", req.body)
    var mongoose = new Mongoose({name: req.body.name, description: req.body.description})
    mongoose.save(function(err){
        if (err){
            console.log('something went wrong in /mongooses')
        } else {
            console.log('successfully added mongoose')
            res.redirect('/')
        }
    })
    
})

app.get('/mongooses/edit/:id', function(req,res){
    console.log("id: ", req.params.id)
    res.render('editMongoose', {id: req.params.id})
})

app.post('/mongooses/:id', function(req,res){
    console.log('id: ', req.params.id)
    console.log('name: ', req.body.name)
    console.log('description: ', req.body.description)
    Mongoose.find({_id: req.params.id}, function(err, mongooses){
        if (err){
            console.log("something wrong in /mongooses/:id")
        } else {
            mongooses[0].name = req.body.name
            mongooses[0].description = req.body.description
            mongooses[0].save(function(err){
                if (err) {
                    console.log('save went wrong')
                } else {
                    console.log("dope")
                }
            })
            console.log(mongooses[0].name)
            res.redirect('/')
        }
        
    })
    
})

app.post('/mongooses/destroy/:id', function(req,res){
    console.log('id: ', req.params.id)
    Mongoose.remove({_id: req.params.id}, function(err){
        if (err) {
            console.log("something went wrong with deletion")
        } else {
            console.log("deletion was successful")
            res.redirect('/')
        }
    })
})
app.listen(8000, function(){
    console.log("listening on port 8000")
})