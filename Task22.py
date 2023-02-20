n = int(input("Введите количество элементов первого множества n : "))
set1 = set()
for i in range(n):
    if i < n:
        set1.add(input(f"Введите элемент {i + 1}: "))

m = int(input("Введите количество элементов второго множества m : "))
set2 = set()
for i in range(m):
    if i < m:
        set2.add(input(f"Введите элемент {i + 1}: "))
set3 = set1 | set2
print("Отсортированные в порядке возрастания:", *sorted(set3))

