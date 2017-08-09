var mongoose = require('mongoose');
var Mongoose = mongoose.model('Mongoose')
var mongooses = require('../controllers/mongooses.js');
module.exports = function(app){
    app.get('/', function(req,res){
         mongooses.showAll(req, res)
        
    })

    app.get('/mongooses/new', function(req,res){
        res.render('newMongoose')
    })

    app.get('/mongooses/:id', function(req,res){
        console.log("The mongoose id: ", req.params.id)
        mongooses.showMongoose(req,res)
    })

    app.get('/mongooses/new', function(req,res){
        console.log('going here')
        res.render('newMongoose')
    })

    app.post('/mongooses', function(req,res){
        console.log("post data: ", req.body)
        mongooses.create(req,res)
        
    })

    app.get('/mongooses/edit/:id', function(req,res){
        console.log("id: ", req.params.id)
        res.render('editMongoose', {id: req.params.id})
    })

    app.post('/mongooses/:id', function(req,res){
        console.log('id: ', req.params.id)
        console.log('name: ', req.body.name)
        console.log('description: ', req.body.description)
        mongooses.edit(req,res)
        
    })

    app.post('/mongooses/destroy/:id', function(req,res){
        console.log('id: ', req.params.id)
        mongooses.destroy(req,res)
    })
}
