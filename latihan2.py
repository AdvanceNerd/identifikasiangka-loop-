while True:
    try:
        num = int(input("Masukkan Bilangan: "))

        if (10 <= num <= 15) or (20 <= num <= 25) or (35 <= num <= 40):

            print("Benar...")

            break
        else:
            print("Salah!")
    except ValueError:
        print("Masukkan bilangan bulat yang valid.")
