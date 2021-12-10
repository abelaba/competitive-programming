x = input().split(" ")
n = eval(x[0]) * eval(x[1])
if(n % 2 != 0):
    print(int((n-1)/2))
else:
    print(int(n/2))
