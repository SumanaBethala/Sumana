def string(s):
   sum=0
   for i in s:
       sum=sum+(ord(i)-96)
       print(i)
       print(sum)
   
s=input()
string(s)
