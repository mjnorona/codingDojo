var mongoose = require('mongoose')
var Message = mongoose.model('Message');
module.exports = {
    show: function(req, res){
        Message.find({}, function(err, messages){
            if (err){
                console.log('something went wrong with /')
            } else {
                var list = []
                Message.find().populate('comments').exec(function(err, texts){
                    if(err){
                        console.log('could not get comments')
                    } else {
                        console.log('successfully got comments')
                        console.log(texts)
                        res.render('index', {messages: texts})
                    }
                })
                
                
            }
        })
    },
    create: function(req, res){
        console.log("post data!!", req.body)
        var message = new Message({name: req.body.name, content: req.body.content})
        message.save(function(err){
            if (err){
                console.log("something went wrong with /newMessage", err)
                
            } else {
                console.log("successfully added message")
                res.redirect('/')
            }
        })
    }
}