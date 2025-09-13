import random

son = random.randint(1, 100)
urinishlar = 0

while True:
    guess = int(input("1 dan 100 gacha son kiriting: "))
    urinishlar += 1

    if guess == son:
        print(f"🎉 To‘g‘ri topdingiz! Son: {son}")
        print(f"Urinishlar soni: {urinishlar}")
        break
    elif guess < son:
        print("🔼 Katta son o‘ylang")
    else:
        print("🔽 Kichik son o‘ylang")
