line=input("enter the line:");
counts={}
word={}
sentence=line.split()
for word in sentence:
    if word in counts:
        counts[words]+=1
    else:
            counts[word]=1
            for k,v in counts.items():
             print(k,v)
