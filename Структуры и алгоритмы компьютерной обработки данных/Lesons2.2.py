
def fact_r(n):
    if n <= 1 or n > 100:
        return 1
    return n * fact_r(n-1)

n = 5
fact = 1

for i in range(1, n+1, 1):
    fact *= i
print(f"Факториал {n} равен: {fact}")


# числа фибаначи
fib1 = fib2 = 1
print(fib1, fib2, end =' ')
n = 5
for i in range(2, n):
    summa = fib2 + fib1
    fib1 = fib2
    fib2 = summa
    print(summa, end=' ')

