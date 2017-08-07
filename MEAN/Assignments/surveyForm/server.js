var express = require('express');
var bodyParser = require('body-parser');
var path = require('path');
var app = express();
var session = require('express-session');


app.use(bodyParser.urlencoded({extended: true}))
app.use(express.static(path.join(__dirname, './static')))
app.use(session({secret: "mylittlesecret"}));

app.set('views', path.join(__dirname, './views'))
app.set('view engine', 'ejs');

app.get('/', function(req, res) {
    res.render("index")
})

app.get('/results', function(req,res) {
    console.log(req.session.fields)
    res.render("results", {fields: req.session.fields})
})

app.post('/result', function(req, res) {
    
    req.session.fields = req.body
    res.redirect('/results')
})

app.listen(8000, function() {
    console.log("listening on port 8000")
})