def diffPairs(li):
   c=li.copy()
   new = []
   for i in range(len(li)-1):
       for j in range(i+1, len(li)):
           d = abs(li[i]-li[j])
           if d not in li and d not in new:
               new.append(d)
               
   li.extend(new)
   return li
li = [3,6,9,12,2]
diffPairs(li)
# [1,2,3] -> [1,2,3]
def medium(li,k):
   while(True):
      li3 = differencePairs(li)
      if li3[0] == li3[1]:
         break
      if len(li3[0]) >= k:
         return sorted(li3[0],reverse=True)[k-1]
      return -1
# Function to identify differences of all
# pairs of numbers and add those differences
# to the same list.
# It returns the updated list and original list

def differencePairs(li):
   cli = li[:]
   newelements = []
   for i in range(len(li)-1):
      for j in range(i+1, len(li)):
         d = abs(li[i]-li[j])
         if d not in li and d not in newelements:
            newelements.append(d)
            li.extend(newelements)
            return [cli, li]
li = [1,9,8,7,6,2]
differencePairs(li)

# [1,2,3] -> [1,2,3]

def medium(li,k):
   while(True):
       li3 = differencePairs(li)
       if li3[0] == li3[1]:
           break
   if len(li3[0]) >= k:
       return sorted(li3[0],reverse=True)[k-1]
   return -1

# Function to identify differences of all
# pairs of numbers and add those differences
# to the same list.
# It returns the updated list and original list

def differencePairs(li):
   cli = li[:]
   newelements = []
   
   for i in range(len(li)-1):
       for j in range(i+1, len(li)):
           d = abs(li[i]-li[j])
           if d not in li and d not in newelements:
               newelements.append(d)
   li.extend(newelements)
   return [cli, li]
li = [1,9,8,7,6,2]
differencePairs(li)
