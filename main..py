
t=int(input())

while t>0:
    t-=1

    list1 = []
    list2 = []

    for i in range(10):
        list1 = [None] * 10
        list1 = list(map(str, input().split()[0]))
        list2.append(list1)
    count = 0
    for i in range(len(list2)):
        for j in range(len(list2[i])):
            if list2[i][j] == 'X':
                if i == 0 or i == 9 or j == 0 or j == 9:
                    count += 1


                elif (i == 1 and (j == 1 or j == 2 or j == 3 or j == 4 or j == 5 or j == 6 or j == 7 or j == 8)) or (
                        i == 8 and (j == 1 or j == 2 or j == 3 or j == 4 or j == 5 or j == 6 or j == 7 or j == 8)) or (
                        j == 1 and i != 0 and i != 9) or (j == 8 and i != 0 and i != 9):
                    count += 2

                elif (i == 2 and (j == 2 or j == 3 or j == 4 or j == 5 or j == 6 or j == 7)) or (
                        i == 7 and (j == 2 or j == 3 or j == 4 or j == 5 or j == 6 or j == 7)) or (
                        j == 2 and i != 0 and i != 9 and i != 1 and i != 8) or (
                        j == 7 and i != 0 and i != 9 and i != 1 and i != 8):
                    count += 3

                elif (i == 3 and (j == 3 or j == 4 or j == 5 or j == 6)) or (
                        i == 6 and (j == 3 or j == 4 or j == 5 or j == 6)) or (
                        j == 3 and i != 0 and i != 9 and i != 1 and i != 2 and i != 7 and i != 8) or (
                        j == 6 and i != 0 and i != 9 and i != 2 and i != 7 and i != 1 and i != 8):
                    count += 4

                else:
                    count += 5

    print(count)