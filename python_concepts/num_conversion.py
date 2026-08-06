# Number System Conversion (based on a C project example from GeeksForGeeks)
def decimal_to_binary(decimal: int) -> str:
    return bin(decimal)[2:]  # strip "0b"

def binary_to_decimal(binary: str) -> int:
    return int(binary, 2)

def decimal_to_octal(decimal: int) -> str:
    return oct(decimal)[2:]  # strip "0o"

def octal_to_decimal(octal: str) -> int:
    return int(octal, 8)

def decimal_to_hexadecimal(decimal: int) -> str:
    return hex(decimal)[2:].upper()

def hexadecimal_to_decimal(hex_str: str) -> int:
    return int(hex_str, 16) 


# Main 
while True:
    print("Menu:"
        "\n1. Decimal to Binary"
        "\n2. Binary to Decimal"
        "\n3. Decimal to Octal"
        "\n4. Octal to Decimal"
        "\n5. Decimal to Hexadecimal"
        "\n6. Hexadecimal to Decimal"
        "\n7. Exit")

    choice = input("Enter your choice: ")

    if choice == '7':
        print("Goodbye!")
        break

    if choice == '1':
        decimal = int(input("Enter a decimal number: "))
        print("Decimal to Binary: ", decimal_to_binary(decimal))

    elif choice == '2':
        binary = input("Enter a binary number: ")
        print("Binary to Decimal: ", binary_to_decimal(binary))


    elif choice == "3":
        decimal = int(input("Enter a decimal number: "))
        print("Decimal to Octal:", decimal_to_octal(decimal))

    elif choice == "4":
        octal = input("Enter an octal number: ")
        print("Octal to Decimal:", octal_to_decimal(octal))

    elif choice == "5":
        decimal = int(input("Enter a decimal number: "))
        print("Decimal to Hexadecimal:", decimal_to_hexadecimal(decimal))

    elif choice == "6":
        hex_str = input("Enter a hexadecimal number: ")
        print("Hexadecimal to Decimal:", hexadecimal_to_decimal(hex_str))

    else:
        print("Invalid Option. Please choose one of the 7 options.")