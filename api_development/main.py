data ={
    "name": "Johny Deep",
    "age": 30,
    "address":{
        "street": "123 street",
        "city": "Prishtina"
    },
    "contact": [
        {
            "type": "email"
        },
        {
            "type": "phone"
        }
    ]
}

print(data["contact"][0]["type"])