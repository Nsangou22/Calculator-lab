from src import utils


def main():
    while True:
        print("\n--- Calculator ---")
        print("1. Add\n2. Subtract\n3. Multiply\n4. Divide")
        choice = input("Choose operation (1–4): ")

        try:
            a = float(input("Enter first number: "))
            b = float(input("Enter second number: "))
        except ValueError:
            print("❌ Invalid input.")
            continue

        try:
            if choice == "1":
                print("Result:", utils.add(a, b))
            elif choice == "2":
                print("Result:", utils.subtract(a, b))
            elif choice == "3":
                print("Result:", utils.multiply(a, b))
            elif choice == "4":
                print("Result:", utils.divide(a, b))
            else:
                print("❌ Invalid choice.")
        except ZeroDivisionError as e:
            print(e)

        again = input("Another calculation? (y/n): ")
        if again.lower() != "y":
            break


if __name__ == "__main__":
    main()
