a = [1, 5, 9 ,2 ,8, 6, 3, 7, 4]

for i in range(len(a)):
    j = i-1
    key = a[i]
    while a[j]>key and j>=0:
        a[j+1] = a[j]
        j = j-1
    a[j+1] = key


print(a)