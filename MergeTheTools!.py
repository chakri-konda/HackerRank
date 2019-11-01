from collections import OrderedDict 
def rmdup(str):
    return "".join(OrderedDict.fromkeys(str))

def merge_the_tools(string, k):
    s = int(len(string)/k)
    t = []
    i = 0
    for _ in range(s):
        t.append(string[i:i+k])
        i = i+k
    u = []
    for a in t:
        u.append(rmdup(a))
    for a in u:
        print(a)


if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)
