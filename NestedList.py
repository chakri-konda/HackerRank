if __name__ == '__main__':
    students = []
    for _ in range(int(input())):
        name = input()
        score = float(input())
        students.append([name, score])
    students.sort()
    sml = sorted( {x[1] for x in students} )[1]  #finding second smallest element
    for i in students:
        if(i[1] == sml):
            print(i[0])
