var mongoose = require('mongoose')
var Note = mongoose.model('Note')

module.exports = {
    show: function(req, res){
        Note.find({}, function(err, notes){
            res.json(notes)
        })
    },

    create: function(req,res){
        console.log(req.body.data)
        var note = new Note({content: req.body.data});
        note.save(function(err){
            if (err){
                console.log('something went wrong');
            } else {
                res.redirect('/notes')
            }
        })
    },

    deleteAll: function(req,res){
        
    }
}