var mongoose = require('mongoose')

var NoteSchema = new mongoose.Schema({
    content: String,
}, {timestamps: true})

var Note = mongoose.model('Note', NoteSchema)