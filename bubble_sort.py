a = [1, 5, 9 ,2 ,8, 6, 3, 7, 4]

for i in range(len(a)-1):
    for j in range(len(a)-i-1):
        if a[j]>a[j+1]:
            a[j], a[j+1] = a[j+1], a[j]

print(a)