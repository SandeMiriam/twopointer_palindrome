# 

a="I am Akirachix"
b=a.split()
start=0
end=len(b)-1
while start<end:
    b[start],b[end]=b[end],b[start]
    start +=1
    end -=1
    str=" "

m=(str.join(b))
if(m==a):
 print("a is a palindrome")
else:
 print("a is not a palindrome")
    
