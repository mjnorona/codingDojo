var mongoose = require('mongoose');
// create the schema
var MongooseSchema = new mongoose.Schema({
    name: String,
    description: String,
})
// register the schema as a model
var Mongoose = mongoose.model('Mongoose', MongooseSchema);