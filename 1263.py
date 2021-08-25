while True:
    try:
        frase = input().lower().split()
        total = 0
        flag = False

        for i, j in enumerate(frase):
            frase[i] = j[0]

            if frase[i] == frase[i - 1] and flag == False:
                flag = True
                total += 1
            elif frase[i] != frase[i - 1]:
                flag = False

        print(total)
    except EOFError: # EOF = End of file
        break
