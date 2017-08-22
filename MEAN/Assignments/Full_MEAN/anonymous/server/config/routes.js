var mongoose = require('mongoose')
var Note = mongoose.model('Note')
var notes = require('../controllers/notes.js')
module.exports = function(app){
    app.get('/', function(req,res){
        res.render('index')
        
    })

    app.post('/notes', function(req, res){
        console.log("GO HERE LINE 11", req.body)
        notes.create(req,res)
    })

    app.get('/notes', function(req,res){
        notes.show(req,res)
    })

    app.get('/delete', function(req,res){
        notes.deleteAll(req,res)
    })
    app.all("*", (req,res,next) => {
        res.sendFile(path.resolve("../public/dist/index.html"))
    });
}