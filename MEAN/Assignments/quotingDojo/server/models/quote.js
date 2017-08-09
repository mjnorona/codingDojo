// require mongoose
var mongoose = require('mongoose');
// create the schema
var QuoteSchema = new mongoose.Schema({
    name: String,
    quote: String,
    date: {type: Date, default: Date.now},
}, {timestamps: true})
// register the schema as a model
var Quote = mongoose.model('Quote', QuoteSchema);