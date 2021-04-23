a1 = int(input())
b1 = int(input())
c1 = int(input())


def sum_of_length(a, b, c):
    return 4 * (a + b + c)


def surface_area(a, b, c):
    return 2 * (a * b + b * c + a * c)


def volume(a, b, c):
    return a * b * c


print(sum_of_length(a1, b1, c1))
print(surface_area(a1, b1, c1))
print(volume(a1, b1, c1))
