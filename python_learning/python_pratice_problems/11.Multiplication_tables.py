def table(n, start, stop):
    for j in range(start, stop+1):
        print(f"{n} X {j} == {n * j}")

num = list(map(int, input("Enter which table you wante ,range(start/stop) respectively in order\nEg: 2,1,20\nTable :").split(',')))
table(num[0], num[1], num[2])


# Example output 1:
'''

Enter which table you wante ,range(start/stop) respectively in order
Eg: 2,1,20
Table :2,1,20
2 X 1 == 2
2 X 2 == 4
2 X 3 == 6
2 X 4 == 8
2 X 5 == 10
2 X 6 == 12
2 X 7 == 14
2 X 8 == 16
2 X 9 == 18
2 X 10 == 20
2 X 11 == 22
2 X 12 == 24
2 X 13 == 26
2 X 14 == 28
2 X 15 == 30
2 X 16 == 32
2 X 17 == 34
2 X 18 == 36
2 X 19 == 38
2 X 20 == 40'''

# Example output 2:
'''
Enter which table you wante ,range(start/stop) respectively in order
Eg: 2,1,20
Table :19,1,10
19 X 1 == 19
19 X 2 == 38
19 X 3 == 57
19 X 4 == 76
19 X 5 == 95
19 X 6 == 114
19 X 7 == 133
19 X 8 == 152
19 X 9 == 171
19 X 10 == 190
'''
