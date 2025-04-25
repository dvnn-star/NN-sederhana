#konsep LIFO LAST in first out

arr = [1, 2, 3, 4, 5]
stack = []
for i in range(len(arr)):
    stack.append(arr[i])

reversedlist = []
while len(stack) >0:
    reversedlist.append(stack.pop())
    

print(reversedlist)