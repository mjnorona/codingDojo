var mongoose = require('mongoose');
var Message = mongoose.model('Message')
var messages = require('../controllers/messages.js')
var comments = require('../controllers/comments.js')
module.exports = function(app){
    app.get('/', function(req, res){
        messages.show(req,res)
    })

    app.post('/newMessage', function(req,res){
        messages.create(req,res)
    })

    app.post('/newComment/:id', function(req,res){
        // console.log("comment id: ", req.params.id)
        // console.log('post data', req.body)
        comments.create(req,res)
    })
}