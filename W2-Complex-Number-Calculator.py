# ---------------------------------------------------------------
# Complex number calculator
# Author: Roxanne Prajapati
# Description:
#      This program lets users chose a math operation from the menu
#      to perform on two complex numbers.
# ---------------------------------------------------------------
import math

class ComplexNumberCalculator:

    def __init__(self):
        self.first_complex_number = None
        self.second_complex_number = None
        self.choice = None
        self.real_number = None
        self.i_number = None

    def display_menu(self):
        print("\nChoose operation:")
        print("1. Addition (z1 + z2)")
        print("2. Subtraction (z1 - z2)")
        print("3. Multiplication (z1 × z2)")
        print("4. Division (z1 ÷ z2)")
        print("5. Get Modulus/Magnitude (|z|)")
        print("6. EXIT")

    def get_user_input(self):
        self.choice = int(input("Enter number (1-6): "))
        # if 6.EXIT is selected
        if self.choice == 6:
            return False

        # if 5.Modulus/Magnitude is selected
        if self.choice == 5:
            real_number = input("Enter a real number: ").strip()
            imaginary_number = input("Enter imaginary number: ").strip()

            # Reject inputs like "5i", "5j", "3+4j", etc.
            if not real_number.replace(".", "", 1).replace("-", "", 1).isdigit():
                raise ValueError("Real number part must be a numeric value.")

            if not imaginary_number.replace(".", "", 1).replace("-", "", 1).isdigit():
                raise ValueError("Imaginary number part must be a numeric value (no 'i' or 'j').")

            self.real_number = float(real_number)
            self.i_number = float(imaginary_number)
            return True

        #if other operation is selected
        try:
            self.first_complex_number = complex(input("Enter first complex number (example: 3+4j): ").strip().replace(' ',''))
        except ValueError:
            raise ValueError("Invalid first complex number format.")

        try:
            self.second_complex_number = complex(input("Enter second complex number (example: 10+j): ").strip().replace(' ',''))
        except ValueError:
            raise ValueError("Invalid second complex number format.")

        return True

    def perform_operation(self):
        match self.choice:
            case 1:
                print("The sum of complex number is: ", self.first_complex_number + self.second_complex_number)
            case 2:
                print("The difference of complex number is: ", self.first_complex_number - self.second_complex_number)
            case 3:
                print("The product of complex number is: ", self.first_complex_number * self.second_complex_number)
            case 4:
                print("The quotient of complex number is: ", self.first_complex_number / self.second_complex_number)
            case 5:
                #magnitude =sqrt(x**2 + y**2)
                magnitude = math.sqrt(self.real_number**2 + self.i_number**2)
                print("The magnitude of the complex number is: ", magnitude)
            case _:
                raise ValueError("Invalid choice")


# Run the program only when executed directly
if __name__ == "__main__":
    complex_number_calculator = ComplexNumberCalculator()
    while True:
        try:
            complex_number_calculator.display_menu()
            user_input = complex_number_calculator.get_user_input()

            #if user selected 6.EXIT
            if(user_input == False):
                break

            complex_number_calculator.perform_operation()

            # Ask user if they want another operation, if no exit the loop
            again = input("Do you perform another operation and display the menu? (Y/N): ").strip().upper()

            if again != "Y":
                print("\nThank you for using this Complex Number Calculator.!")
                break
        except ValueError as err:
            print("Invalid input:", err)
            print("Please try again.\n")

