# This is from a college activity (in there that code was done in c++ as its instructions commanded)
class Patient:
    def __init__(self, p_id, name, paternal_surname, maternal_surname, birth_date, gender, phone, email, address):
        self.p_id = p_id
        self.name = name
        self.paternal_surname = paternal_surname
        self.maternal_surname = maternal_surname
        self.birth_date = birth_date
        self.gender = gender
        self.phone = phone
        self.email = email
        self.address = address
        
    def display(self):
        print(f"ID: {self.p_id}")
        print(f"Name: {self.name}")
        print(f"Paternal Surname: {self.paternal_surname}")
        print(f"Materal Surname: {self.maternal_surname}")
        print(f"Birth Date: {self.birth_date}")
        print(f"Gender: {self.gender}")
        print(f"Phone: {self.phone}")
        print(f"Email: {self.email}")
        print(f"Address: {self.address}")
        print("-" * 40)

max_patients = 100
patients = []

def main_menu():
    print("*** Main Menu ***")
    print("1. Register Patient")
    print("2. Delete Patient")
    print("3. Modify Patient")
    print("4. Search Patient")
    print("5. Show All Patients")
    print("6. Exit")

# Option 1
def register_patient():
    if len(patients) >= max_patients: 
        print("Patient limit reached")
        return
    
    print("***Add patients***")
    p_id = int(input("Enter patient ID: ")) 
    if any(p.p_id == p_id for p in patients):
        print(f"Patient with ID {p_id} already exists.")
        return
    
    name = input("Enter name: ")
    paternal_surname= input("Enter paternal surname: ")
    maternal_surname= input("Enter maternal surname: ")
    birth_date = input("Enter birth date (MM/DD/YYYY): ")
    gender = input("Enter gender (Male/Female): ")
    phone = input("Enter phone number: ")
    email = input("Enter email: ")
    address = input("Enter address: ")

    new_patient = Patient(p_id, name, paternal_surname, maternal_surname, birth_date, gender, phone, email, address)
    patients.append(new_patient)
    print("Patient successfully registered")

# Option 2
def delete_patient():
    print("*** Delete patients ***")
    p_id = int(input("Enter patient ID to delete: "))
    for i, p in enumerate(patients):
        if p.p_id == p_id:
            confirm = input("Confirm deletion (Y/N): ".lower())
            if confirm == 'y':
                patients.pop(i)
                print("Patient ID has been removed.")
            else:
                print("Deletion cancelled.")
            return
    print("Patient not found.")

# Option 3
def modify_patient():
    print("*** Modify patient***")
    p_id = int(input("Enter patient ID to modify: "))
    for p in patients:
        if p.p_id == p_id:
            print("Current patient data: ")
            p.display()

            confirm = input("Want to modify this patient's data? (Y/N:)".lower())
            if confirm != 'y':
                print("Modification cancelled.")
                return
            
            def update_field(field_name, current_value):
                print(f"{field_name} (current: {current_value})")
                new_value = input("Enter new value or press Enter to keep current: ")
                return new_value if new_value.strip() else current_value 
            
            p.name = update_field("Name: ", p.name)
            p.paternal_surname = update_field("Paternal surname: ", p.paternal_surname)
            p.maternal_surname = update_field("Maternal surname: ", p.maternal_surname)
            p.birth_date = update_field("Birth date (MM/DD/YYYY): ", p.birth_date)
            p.gender = update_field("Gender (Male/Female): ", p.gender)
            p.phone = update_field("Phone number: ", p.phone)
            p.email = update_field("Email: ", p.email)
            p.address = update_field("Address: ", p.address)
            print("Patient data updated.")
            return
    print("Patient not found.")

# Option 4
def search_patient():
    print("***Search patient***")
    print("Search by:\n1. Patient ID\n2. Name")
    option = int(input("Choose an option: "))
    
    if option == 1:
        p_id = int(input("Enter patient ID: "))
        for p in patients:
            if p.p_id == p_id:
                print("Patient ID: ")
                p.display()
                return
        print("Patient name not found.")
    if option == 2:
        name = input("Enter patient's name: ")
        for p in patients:
            if p.name.lower() == name.lower():
                print("Patient name: ")
                p.display()
                return
        print("Patient name not found.")
    else:
        print("Invalid option.")

# Option 5
def show_all_patients():
    print("*** List of patients ***")
    if not patients:
        print("No patients registrered.") 
        return
    for i, p in enumerate(patients, start=1):
        print(f"Patient {i}:")
        p.display()

# Menu usage 
def run():
    while True:
        main_menu()
        choice = int(input("Select an option: "))
        if choice == 1:
            register_patient()
        elif choice == 2:
            delete_patient()
        elif choice == 3:
            modify_patient()
        elif choice == 4:
            search_patient()
        elif choice == 5:
            show_all_patients()
        elif choice == 6:
            print("Existing system... ")
            break
        else:
            print("Invalid option.")

run()
 