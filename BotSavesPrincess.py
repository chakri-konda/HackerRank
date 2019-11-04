def displayPathtoPrincess(n,grid):
    s = [list(x) for x in grid]
    for i in range(n):
        for j in range(n):
            if s[i][j] == 'p':
                a, b = i, j
                break
    c, d = n//2, n//2
    while (a != c) and (b != d):
        if a > c:
            c += 1
            print("DOWN")
        elif a < c:
            c -= 1
            print("UP")
        if b < d:
            d -= 1
            print("LEFT")
        elif b > d:
            d += 1
            print("RIGHT")

m = int(input())
grid = [] 
for i in range(0, m): 
    grid.append(input().strip())

displayPathtoPrincess(m,grid)
