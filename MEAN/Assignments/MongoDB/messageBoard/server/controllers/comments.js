var mongoose = require('mongoose')
var Message = mongoose.model('Message');
var Comment = mongoose.model('Comment');
module.exports = {
    
    create: function(req,res){
        console.log('post data', req.body)
        Message.findOne({_id: req.params.id}, function(err,message){
            var comment = new Comment(req.body)
            comment._message = message.id
            comment.save(function(err){
                message.comments.push(comment);
                message.save(function(err){
                    if (err){
                        console.log('error adding comment')
                    } else {
                        console.log('successfully added comment')
                        res.redirect('/')
                    }
                })
            })
        })
        
    }
}