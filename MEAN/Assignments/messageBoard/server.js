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
mongoose.connect('mongodb://localhost/mongooses')

//schemas
var Schema = mongoose.Schema
var MessageSchema = new mongoose.Schema({
    name: {type: String, required: true, minlength: 4},
    content: {type: String, required: true},
    comments: [{type: Schema.Types.ObjectId, ref: 'Comment'}]
}, { timestamps: true})

var CommentSchema = new mongoose.Schema({
    name: {type: String, required: true, minlength: 4},
    _message: {type: Schema.Types.ObjectId, ref: 'Message'},
    content: {type: String, required: true},
}, {timestamps: true})

mongoose.model('Message', MessageSchema)
mongoose.model('Comment', CommentSchema)

var Message = mongoose.model('Message')
var Comment = mongoose.model('Comment')

app.get('/', function(req, res){
    res.render('index')
})

app.post('/newMessage', function(req,res){
    console.log("post data", req.body)
    var message = new Message({name: req.body.name, content: req.body.content})
    message.save(function(err){
        if (err){
            console.log("something went wrong with /newMessage")
            
        } else {
            console.log("successfully added message")
            res.redirect('/')
        }
    })
    
})

app.listen(8000, function(){
    console.log("listening at port 8000")
})