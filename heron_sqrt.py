# Квадратный корень по алгоритму Герона в виде функции
def heron_sqrt(target):
    x = 1
    while True:
        oldx = x
        x = (x + target / x) / 2
        if oldx == x:
            break
    return x


number = 2021
result = heron_sqrt(number)
print("x =", result)
print("x^2 =", result * result)
