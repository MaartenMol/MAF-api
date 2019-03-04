//In a Mongo shell use ie: load("CouponCustomer/demoData.js")

db.createCollection("coupons", {"autoIndexId": "1", }),
db.createCollection("customers", {"autoIndexId": "1", }),

db.coupons.insertMany([
    { "id": "VrjnaCnxtcF", "status": "1", "value": "1", "customer_id": "5c6c1d49a990cde0ca31a23e" },
    { "id": "H2Bn26LmKs9", "status": "1", "value": "1", "customer_id": "5c6c1d49a990cde0ca31a23e" },
    { "id": "vTfw6ZNaQbv", "status": "0", "value": "1"},
    { "id": "YCDMkPKMsuz", "status": "0", "value": "1"},
    { "id": "sxZuV67d9d9", "status": "0", "value": "1"},
    { "id": "8QFftxtUnQV", "status": "0", "value": "1"},
    { "id": "j42EfJCAGYh", "status": "0", "value": "1"},
    { "id": "PZ4RJEjvezt", "status": "0", "value": "1"},
    { "id": "sny7cnDvcyA", "status": "0", "value": "1"},
    { "id": "ffTSdR22tE4", "status": "0", "value": "1"},
]),

db.customers.insertMany([
    { "_id": "5c6c1d49a990cde0ca31a23e", "firstname": "Jane", "lastname": "Doe", "email": "jane.doe@test.com"},
    { "firstname": "Pleb", "lastname": "Noob", "email": "pleb.noob@test.com" },
])