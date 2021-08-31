#循环遍历所有的key
dict={"k1":"v1","k2":"v2","k3":"v3"}
for k in dict.keys():
    print(k)

dict={"k1":"v1","k2":"v2","k3":"v3"}
for k in dict:
    print(k)


#循环遍历所有的value
dict={"k1":"v1","k2":"v2","k3":"v3"}
print(dict["k1"])
print(dict["k2"])
print(dict["k3"])

dict={"k1":"v1","k2":"v2","k3":"v3"}
for w in dict:
   print (dict[w])

 #请在字典中增加一个键值对,"k4":"v4"
dict={"k1":"v1","k2":"v2","k3":"v3"}
dict["k4"]="v4"
print(dict)