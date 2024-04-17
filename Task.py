print("Первое задание")
num1 = int(input("Введите первое число: "))
num2 = int(input("Ввндите второе число: "))

if num1 > num2:
    print(f"{num1} больше {num2}")
    
else:
    print(f"{num2} больше {num1}")


print("\nВторое задание")
l = []
num1 = int(input("Введите Первое число: "))
l.append(num1)
num2 = int(input("Введите второе число: "))
l.append(num2)
num3 = int(input("Введите третье число: "))
l.append(num3)

l.sort()
print(f"Самое большое число {l[2]}")
