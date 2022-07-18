try:
    a = input("Введите первое число:")
    b = input("Введите второе число:")
    result = int(a)/int(b)

except ZeroDivisionError:
    a = input("Введите первое число заново:")
    b = input("Введите второе число заново:")
except ValueError:
    print("erorhuerror")