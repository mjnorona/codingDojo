var express = require("express");

var app = express();
app.use(express.static(__dirname + "/static"));
app.set('views', __dirname + '/views'); 
// Now lets set the view engine itself so that express knows that we are using ejs as opposed to another templating engine like jade
app.set('view engine', 'ejs');

var bodyParser = require('body-parser');
// use it!
app.use(bodyParser.urlencoded({extended: true}));

var session = require('express-session');
// original code:
var app = express();
// more new code:
app.use(session({secret: 'codingdojorocks'}));

app.get('/', function (req, res){
  res.render('index', {title: "my Express project"});
});

app.post('/users', function (req, res){
    console.log("POST DATA \n\n", req.body)
    //code to add user to db goes here!
    // redirect the user back to the root route.  
    requ.session.name = req.body.name
    console.log(req.session.name)
    res.redirect('/')
});

app.get("/users/:id", function (req, res){
    console.log("The user id requested is:", req.params.id);
    // just to illustrate that req.params is usable here:
    res.send("You requested the user with id: " + req.params.id);
    // code to get user from db goes here, etc...
});

app.listen(8000, function() {
  console.log("listening on port 8000");
})