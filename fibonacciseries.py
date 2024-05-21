n = 100
a = 0
b = 1

print(a, end = " ")

count = 1  

while count < n: 
    print(b, end = " ")
    a, b = b, a + b  
    count += 1
print()
