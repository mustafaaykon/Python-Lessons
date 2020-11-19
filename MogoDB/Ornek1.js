/*
1) show dbs           : server içerisinde yer alan database'leri görüntüler
2) use <database adı> : çalışmak istediğiniz database'in adını vermeniz yeterlididr.Not : küçük büyük harf duyarlılığı vardır.
3) show collections   : database içerisinde yer alan koleksiyonlar(table)'ı gösterir

*/


// use kisiler    => kisiler database'ini seçili hale getirdik.

// 1) use TelefonRehberi   => TelefonRehberi adında bir db oluşturduk
/* 2)

        db.Kisiler.insert({
            "firstname" : "murat",
            "lastname" : "vuranok",
            "mail" : "murat.vuranok@bilgeadam.com",
            "phone" : "+905323520997",
            "phones" : [
                {
                    "name" : "is",
                    "phone" :"+905323520997"
                },
                {
                    "name" : "ev",
                    "phone" :"+905323520997"
                },
                {
                    "name" : "okul",
                    "phone" :"+905323520997"
                }
            ]
        })

*/

// 3) db.Kisiler.find()
// 4) db.Kisiler.find().pretty()


[
    {
        "firstname": "murat",
        "lastname": "vuranok",
        "mail": "murat.vuranok@bilgeadam.com",
        "phone": "+905323520997",
        "phones": [
            {
                "name": "is",
                "phone": "+905323520997"
            },
            {
                "name": "ev",
                "phone": "+905323520997"
            },
            {
                "name": "okul",
                "phone": "+905323520997"
            }
        ]
    }
]