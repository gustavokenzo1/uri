beans = input().split(' ')

for i in range(4):
    if beans[i] == '1':
        print(int(i)+1)
    elif beans[i] == '0':
        continue
