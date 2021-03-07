def invert_array(a: list, n: int):
    """
    Переворачивание массива A длинной N от 0 элемента до N-1
    """
    for x in range(n // 2):
        a[x], a[n - 1 - x] = a[n - 1 - x], a[x]


def test_invert_array():
    A1 = [1, 2, 10]
    print(A1)
    A2 = A1
    print(invert_array(A2, 3))
    print(A2)
    if A2 == [10, 2, 1]:
        print("test1 - ok")
    else:
        print("test1 failed!")


# test_invert_array()

# еще пример обращения со ссылками и создание новых объектов
a = [1, 2, 3, 4, 5]
for x in a:
    x += 1
print(a)

