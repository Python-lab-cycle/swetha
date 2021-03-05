list=[10,20,456,30,40,789]
result=[]
for i in list:
    if i>100:
        result.append('over')
    else:
        result.append(i)
print(result)
