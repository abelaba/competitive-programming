x = input().split(" ")
n = eval(x[0])
m = eval(x[1])
a = eval(x[2])

z = int(n / a)
y = int(m / a)

if(n % a != 0):
    z += 1
if(m % a != 0):
    y += 1

print(y * z)
