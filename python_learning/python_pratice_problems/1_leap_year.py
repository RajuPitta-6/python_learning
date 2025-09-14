def is_prime(year):
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                print(f"{year} is a leap year. ")
            else:
                print(f"{year} is not a leap year. ")
        else:
            print(f"{year} is a leap year. ")
    else:
        print(f"{year} is not a leap year. ")


is_prime(2025)
is_prime(2024)
is_prime(2000)
is_prime(1900)
is_prime(1800)