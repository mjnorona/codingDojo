var mongoose = require('mongoose');
var Mongoose = mongoose.model('Mongoose');
module.exports = {
  showAll: function(req, res) {
    Mongoose.find({}, function(err,mongooses){
            if (err) {
                console.log()
                console.log("something went wrong in /")
            } else {
                console.log(mongooses)
                res.render('index', {mongooses: mongooses})
            }
        })
  },

  showMongoose: function(req, res){
    Mongoose.find({_id: req.params.id}, function(err, mongooses){
            
            if (err){
                console.log('something went wrong in /mongooses/:id')
            } else {
                console.log(mongooses)
                res.render('displayMongoose', {mongoose: mongooses[0]})
            }
        })
  },

  create: function(req, res) {
    var mongoose = new Mongoose({name: req.body.name, description: req.body.description})
        mongoose.save(function(err){
            if (err){
                console.log('something went wrong in /mongooses')
            } else {
                console.log('successfully added mongoose')
                res.redirect('/')
            }
        })
  },

  edit: function(req, res) {
      Mongoose.find({_id: req.params.id}, function(err, mongooses){
            if (err){
                console.log("something wrong in /mongooses/:id")
            } else {
                mongooses[0].name = req.body.name
                mongooses[0].description = req.body.description
                mongooses[0].save(function(err){
                    if (err) {
                        console.log('save went wrong')
                    } else {
                        console.log("dope")
                    }
                })
                console.log(mongooses[0].name)
                res.redirect('/')
            }
            
        })
  },

  destroy: function(req, res) {
      Mongoose.remove({_id: req.params.id}, function(err){
            if (err) {
                console.log("something went wrong with deletion")
            } else {
                console.log("deletion was successful")
                res.redirect('/')
            }
        })
  }
}