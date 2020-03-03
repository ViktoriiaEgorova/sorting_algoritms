a = [1, 5, 9 ,2 ,8, 6, 3, 7, 4]

gap = len(a)
swapped = True

while gap>1 or swapped:
    gap = max(1, int(gap/1.2473))
    swapped = False
    for i in range(len(a)-gap):
        j = i+gap
        if a[i]>a[j]:
            a[i], a[j] = a[j], a[i]
            swapped = True

print(a)
