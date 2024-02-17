weight = int(input('Введите вес в фунтах: '))
height = int(input('Введите рост в дюймах: '))
bmi = 703*(weight/(height**2))

print(round(bmi, 2))
