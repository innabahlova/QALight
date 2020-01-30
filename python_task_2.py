import random

А = random.randint(0, 10)
Б = random.randint(0, 10)
В = random.randint(0, 10)

if А > Б:
    print("Позитивный текст")
elif А < Б:
    print("Негативный текст")
elif А == Б:
    print(В, "Теперь эта!")
    if А + Б < В:
        print("Позитивный текст")
    elif А + Б > В:
        print("Негативный текст")
    elif А + Б == В:
        print("Страдания")