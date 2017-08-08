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

mongoose.connect('mongodb://localhost/quotes');

var QuoteSchema = new mongoose.Schema({
    name: String,
    quote: String,
    date: {type: Date, default: Date.now},
}, {timestamps: true})
mongoose.model('Quote', QuoteSchema)
var Quote = mongoose.model('Quote')
mongoose.Promise = global.Promise

app.get('/', function(req,res) {
    // Quote.remove({}, function(err){
    //     if (err) {
    //         console.log("error")
    //     } else {
    //         console.log("success")
    //     }
    // })
    res.render('index')
})

app.post('/quotes', function(req, res) {
    console.log("post data: ", req.body)
    var quote = new Quote({name: req.body.name, quote: req.body.quote})
    quote.save(function(err) {
        if (err) {
            console.log("something went wrong")
            res.redirect('/')
        } else {
            console.log("successfully submitted quote!")
            res.redirect('/quotes')
        }
    })
    
})

app.get('/quotes', function(req,res) {
    console.log("here we are!")
    Quote.find({}, function(err, quotes){
        if (err){
            console.log("something went wrong")
        } else {
            res.render('quotes', {quotes: quotes})
        }
    })
    
})

app.listen(8000, function() {
    console.log("listening on port 8000")
})