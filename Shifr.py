
for a in range (3, 21):
    result = f'{a} - '
    for i in range (1, a):
        for j in range (i+1, a):
            if a % (i + j) == 0:
                result += str(i) + str(j)
    print(result)

