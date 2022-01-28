travel_log=[
    {
        "country":"France",
        "visits":12,
        "cities":["Paris","Lille","Dijon"]
    },
    {
        "country":"Germany",
        "visits":5,
        "cities":["Berlin","Hamburg","Stuttgart"]
    },
]
def add_new_country(name,times,places):
    travel_log.append({"country":name,"visits":times,"cities":places})

add_new_country("Russia",2,["Moscow","Saint Petersburg"])
print(travel_log)
