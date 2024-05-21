import math

def pollard_strassen_factorization(n):
    """
    Function to calculate the pollard strassen factorization ogitf .

    :argument:
    :param n:  The number to calculate the pollard.
    :type n: int

    :returns:
    :int или str: The pollard strassen factorization .
    """

    if n % 2 == 0:
        return 2  # Четные числа имеют тривиальный делитель 2

    x = 2
    y = 2
    d = 1

    def f(x):
        return (x * x + 1) % n

    while d == 1:
        x = f(x)
        y = f(f(y))
        abs_diff = abs(x - y)
        d = math.gcd(abs_diff, n)
        print(f"Текущие значения: x={x}, y={y}, abs(x-y)={abs_diff}, gcd(abs(x-y), {n})={d}")  # Подробный вывод шагов

    if d == n:
        return "Не найден делитель"
    else:
        return d

# Пример использования
n = 209
result = pollard_strassen_factorization(n)
print(f"Делитель числа {n} равен {result}")
