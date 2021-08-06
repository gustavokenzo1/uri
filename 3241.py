tests = int(input())

for i in range(tests):
    conta = input().split('+')

    if conta[0] == 'P=NP':
        print('skipped')

    else:
        conta1 = int(conta[0])
        conta2 = int(conta[1])
        total = conta1 + conta2
        print(total)
