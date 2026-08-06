# this was a forum activity on the UVM (made originally in C++ and here is its recreated in python with a few adjustements)

while True:
    text = input("Write some text: ")

    upper_or_lower = int(input("Convert to uppercase or lowercase? " 
                                "\n1. UPPERCASE" 
                                "\n2. lowercase" 
                                "\nPick an Option (1/2): "))

    if upper_or_lower == 1:
        print(text.upper())
        
    elif upper_or_lower == 2:
        print(text.lower())

    else:
        print("This generator only has two options (1,2)")

    # Option for writing again
    write_again = input("Want to write again? ")
    if write_again != 'y':
        print("Goodbye!")
        break
    else:
        continue