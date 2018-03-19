print("Please give me two numbers, I'll plus them.")
print("Print 'q' to quit.")

while True:
    first_number = input("\nFirst number: ")
    if first_number == 'q':
        break
    seconde_number = input("\nSecond number: ")
    try:
        result = int(first_number) + int(seconde_number)
        print(result)
    except ValueError:
        print("Sorry, you need to give me numbers!")
