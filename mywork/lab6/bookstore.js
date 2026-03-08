// Step 1: use bookstore database
use bookstore

// Step 2: insert Jane Austen
db.authors.insertOne({...})

// Step 3: update Jane Austen's birthday
db.authors.updateOne({...})

// Step 4: insert 4 more authors
db.authors.insertMany([...])

// Step 5: total count
db.authors.countDocuments({})

// Step 6: British authors, sorted by name
db.authors.find({ "nationality": "British" }).sort({ "name": 1 }).pretty()
