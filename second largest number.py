x=input("Enter any string: ")
longest =""
max_length=0
n=0
while n<len(x):
    m=n+1
    while m<=len(x):
        sub=""
        rev=""
        i=n
        while i<m:
            sub+=x[i]
            i+=1
        i=m-1
        while i>=n:
            rev+=x[i]
            i_=1
        if sub==rev and len(sub)>max_len:
            longest=sub
            max_len=len(sub)
        m+=1
    n=+1
    print("longest palindromestringin the given string",longest)  



