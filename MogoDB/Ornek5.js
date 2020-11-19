// Equality ==
// db.Products.find({"ProductID" : 77}) => ürün id değeri 77 olan kaydı getirir.

// CategoryID değeri 8 olan ürünleri listeleyiniz.

db.Products.find({ "CategoryID": 8 }).pretty()


// less than <
// Fiyatı 50$'dan az olan ürünlerin listelenmesi

db.Products.find({ "UnitPrice": { $lt: 50 } }).pretty()


// ürünlerin sıralanması
// Ascending +1 A'dan Z'ye 0'dan 9'a şeklinde sıralama yapar (Fakirden Zengine)
// Descending -1 Z'den A'ya 9'dan 0'a şeklinde sıralama yapar (Zenginden Fakire)

db.Products.find().pretty().sort({ "UnitPrice": 1 })   // ascending 
db.Products.find().pretty().sort({ "UnitPrice": -1 })  // descendig


// less than equal  <= 
// Fiyatı 50$ eşit veya küçük olan ürünlerin, küçükten büyüğe sıralanması
db.Products.find({
    "UnitPrice": { $lte: 50 }

}).pretty().sort({
    "UnitPrice": 1
})


// grather than  >

// fiyatı 100$ büyük olan ürünleri listeleyiniz.


db.Products.find(
    {
        "UnitPrice": { $gt: 100 }
    }
).pretty().sort({
    "UnitPrice": 1
})


// Grather than equals  >=
db.Products.find({ "UnitPrice": { $gte: 60 } }).pretty().sort({ "ProductName": -1 })

// And ve Or Kullanımı

// and kullanımı :
// Fiyatı 30$ büyük, stok adedi 100'den küçük olan ürünlerin listelenmesi 
db.Products.find({
    $and:
        [
            {
                "UnitPrice": { $gte: 30 }
            }
            ,
            {
                "UnitsInStock": { $lte: 100 }

            }
        ]
})

db.Products.find({})

db.Products.find({ $and: [] })
db.Products.find({ $and: [{}, {}] })
db.Products.find({ $and: [{ "UnitPrice": { $gte: 30 } }, {}] })
db.Products.find({ $and: [{ "UnitPrice": { $gte: 30 } }, { "UnitsInStock": { $lte: 100 } }] }).sort({ "UnitPrice": 1 })


// select * from Products where UnitPrice >= 30 and UnitsInStock <= 100 orderby UnitPrice desc

