var mongoose = require('mongoose');
var Schema = mongoose.Schema
var CommentSchema = new mongoose.Schema({
    name: {type: String, required: true, minlength: 4},
    _message: {type: Schema.Types.ObjectId, ref: 'Message'},
    content: {type: String, required: true},
}, {timestamps: true})

var Comment = mongoose.model('Comment', CommentSchema)