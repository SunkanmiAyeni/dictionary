Sdata={"Steven":["maths","english","science"],"Gavi":["maths","english","science"],"Pedri":["maths","english","science"],"Steven":["maths","english","science"]}
result={}
for key,value in Sdata.items():
    if value not in result.values():
        result[key]=value
print("The unique elements of the dictionary are",result)