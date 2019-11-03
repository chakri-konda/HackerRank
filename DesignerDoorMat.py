N, M = map(int, input().split())
p = '.|.'
f = '-'
h = (N//2)
#upper
for i in range(0,h):
    print((p*((2*i)+1)).center(M,f))
#welcome
print('WELCOME'.center(M,f))
#lower
for i in range(0,h):
    print((p*((2*(h-i-1))+1)).center(M,f))
