name = input("Введите имя: ")
print(f"Привет, {name}, приятного пользования моей программой")

while True:
    try:
        age = int(input("Введите свой возраст: "))
        break  
    except ValueError:
        print("Ошибка! Введите возраст только цифрами.")

print(f"Отлично, вам {age} лет.")
