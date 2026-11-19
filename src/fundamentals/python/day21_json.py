import json
dic={
    "name":"Amal",
    "age":19,
    "Male":True
}
tp=json.dumps(dic)
t=json.loads(tp)
print(t)