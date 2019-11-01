a = []
def evaluate(command):
    if(command[0:6] == 'insert'):
        [i, e] = [int(x) for x in command[7:].split(' ',2)]
        a.insert(i, e)
    elif(command[0:5] == 'print'):
        print(a)
    elif(command[0:6] == 'remove'):
        e = int(command[7:])
        a.remove(e)
    elif(command[0:6] == 'append'):
        e = int(command[7:])
        a.append(e)
    elif(command[0:4] == 'sort'):
        a.sort()
    elif(command[0:3] == 'pop'):
        a.pop()
    elif(command[0:7] == 'reverse'):
        a.reverse()
    return

if __name__ == '__main__':
    N = int(input())
    for _ in range(N):
        command = input()
        evaluate(command)
