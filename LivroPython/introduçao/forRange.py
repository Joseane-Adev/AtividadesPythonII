for i in range(10):
    if  i == 2:
        print('i é o 2, pulando...')
        continue

    if i == 8:
        print('i é o 8, seu else não executará')
        break

    for j in range (1,3):
        print(i, j)
else:
    print('For completo!')