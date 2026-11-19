import json
dic={
    "name":"Amal",
    "age":19,
    "Male":True
}
with open('first.json','w') as file:
    json.dump(dic,file)
with open('first.json','r') as f:
    tp=json.load(f)
print(tp)