'''
编写一个函数，传入一个列表，并统计每个数字出现的次数。返回字典数据：{21:3,56:9,10:3}
'''
r=[56,21,56,10,56,10,56,21,56,10,56,21,56,56,56]
r_dict={}
for b in r:
    if b not in r_dict:
        r_dict[b]=1
    else:
        r_dict[b]+=1
print(r_dict)


k=[56,21,56,10,56,10,56,21,56,10,56,21,56,56,56]
from collections import Counter  #从Collections集合模块中引入集合类Counter
print (Counter(k))               #Counter(a)可以打印出数组a中每个元素出现的次数


#求数组种出现次数最多的元素
d=[56,21,56,10,56,10,56,21,56,10,56,21,56,56,56]
from  collections import Counter
print (Counter(d).most_common(1))  #参数1：表示输出几个出现次数最多的元素

d=[56,21,56,10,56,10,56,21,56,10,56,21,56,56,56]
from  collections import Counter
print (Counter(d).most_common(2))