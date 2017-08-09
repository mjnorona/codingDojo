var mongoose = require('mongoose');
var Schema = mongoose.Schema
var MessageSchema = new mongoose.Schema({
    name: {type: String, required: true, minlength: 4},
    content: {type: String, required: true},
    comments: [{type: Schema.Types.ObjectId, ref: 'Comment'}]
}, { timestamps: true})

var Message = mongoose.model('Message', MessageSchema)