#Write a program that creates an object of the class and promps the user to enter info on the pet.
class Pet:
    # The __init__ method initializes the attributes.
    def __init__(self, name, animal_type, age):
        self.__name = name
        self.__animal_type = animal_type
        self.__age = age

    # The set_name method sets the pet's name.
    def set_name(self, name):
        self.__name = name

    # The set_animal_type method sets the pet's type.
    def set_animal_type(self, animal_type):
        self.__animal_type = animal_type

    # The set_age method sets the pet's age.
    def set_age(self, age):
        self.__age = age

    # The get_name method returns the pet's name.
    def get_name(self):
        return self.__name 

    # The get_animal_type method returns the pet's type.
    def get_animal_type(self):
        return self.__animal_type

    # The get_age method returns the pet's age.
    def get_age(self):
        return self.__age


# Get the pet's name, type, and age.
name = input("What is your pet's name? ")
animal_type = input("What type of animal is that? ")
age = input("How old is your pet? ")

# Create an instance of the Pet class.
my_pet = Pet(name, animal_type, age)

# Print the pet's information.
print("Here is the information you entered: ")
print("Pet name:", my_pet.get_name())
print("Animal type:", my_pet.get_animal_type())
print("Age:", my_pet.get_age())



#Design a program that creates a car object then calls the accelarte method five times. after each call to accelerate get the current speed of car and display it. 
#Do the same for the break method
class Car:
    # The __init__ method initializes the car's year model, make, and sets speed to 0.
    def __init__(self, year_model, make):
        self.__year_model = year_model
        self.__make = make
        self.__speed = 0  # Initial speed is 0

    # The accelerate method increases the speed by 5 each time it is called.
    def accelerate(self):
        self.__speed += 5

    # The brake method decreases the speed by 5 each time it is called.
    def brake(self):
        self.__speed -= 5

    # The get_speed method returns the current speed of the car.
    def get_speed(self):
        return self.__speed


# Create a Car object with year model and make as arguments
my_car = Car(2024, "Toyota")

# Accelerate the car 5 times and display the speed after each acceleration
print("Accelerating the car:")
for _ in range(5):
    my_car.accelerate()
    print(f"Speed: {my_car.get_speed()} mph")

# Brake the car 5 times and display the speed after each brake
print("\nBraking the car:")
for _ in range(5):
    my_car.brake()
    print(f"Speed: {my_car.get_speed()} mph")



#Design a class that holds the following personal datat:name, address,age,and phone number.
#Write appropriate accessor and mutator methods. also write a program tha create three instances of the class. Each instnace with fake info
class PersonalData:
    # Constructor to initialize the attributes
    def __init__(self, name, address, age, phone_number):
        self.__name = name
        self.__address = address
        self.__age = age
        self.__phone_number = phone_number

    # Accessor (getter) methods
    def get_name(self):
        return self.__name

    def get_address(self):
        return self.__address

    def get_age(self):
        return self.__age

    def get_phone_number(self):
        return self.__phone_number

    # Mutator (setter) methods
    def set_name(self, name):
        self.__name = name

    def set_address(self, address):
        self.__address = address

    def set_age(self, age):
        self.__age = age

    def set_phone_number(self, phone_number):
        self.__phone_number = phone_number

    # Method to display all personal data
    def display_personal_data(self):
        print(f"Name: {self.__name}")
        print(f"Address: {self.__address}")
        print(f"Age: {self.__age}")
        print(f"Phone Number: {self.__phone_number}")
        print("-" * 30)


# Create three instances of PersonalData with fictional information
person1 = PersonalData("Alice Johnson", "123 Maple St, Wonderland", 29, "555-1234")
person2 = PersonalData("Bob Smith", "456 Oak Ave, Dreamland", 35, "555-5678")
person3 = PersonalData("Charlie Brown", "789 Pine Rd, Neverland", 40, "555-9876")

# Display the personal data for all three people
print("Person 1's Information:")
person1.display_personal_data()

print("Person 2's Information:")
person2.display_personal_data()

print("Person 3's Information:")
person3.display_personal_data()


#