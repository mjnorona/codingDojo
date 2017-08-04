// require express
var express = require("express");
// path module -- try to figure out where and why we use this
var path = require("path");
// create the express app
var app = express();
var bodyParser = require('body-parser');

var session = require('express-session')
app.use(session({secret: 'codingdojorocks'}));
// use it!
app.use(bodyParser.urlencoded({ extended: true }));
// static content
app.use(express.static(path.join(__dirname, "./static")));
// setting up ejs and our views folder
app.set('views', path.join(__dirname, './views'));
app.set('view engine', 'ejs');
// root route to render the index.ejs view



app.get('/', function(req, res) {
    if ('count' in req.session) {
        req.session.count++
        
    } else {
        req.session.count = 1
    }
    console.log(req.session.count)
    res.render("index", {count: req.session.count});
})
// post route for adding a user

// tell the express app to listen on port 8000
app.listen(8000, function() {
    console.log("listening on port 8000");
});