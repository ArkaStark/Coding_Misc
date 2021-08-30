const MongoClient = require('mongodb').MongoClient;

MongoClient.connect('mongodb://localhost:27017/devfeb'),(err,client) => {
    if (err) throw err
    
    var db = client.db('devfeb');

    // INSERTION
    db.collection('items').insertOne({
        name: '',
        price: ''
    });
}