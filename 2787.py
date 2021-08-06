lines = int(input())
collumns = int(input())

if lines % 2 != 0 and collumns % 2 != 0:
    print(1)
if lines % 2 != 0 and collumns % 2 == 0:
    print(0)
if lines % 2 == 0 and collumns % 2 != 0:
    print(0)
if lines % 2 == 0 and collumns % 2 == 0:
    print(1)
