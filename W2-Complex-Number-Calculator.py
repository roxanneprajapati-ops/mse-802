# ---------------------------------------------------------------
# Complex number calculator
# Author: Roxanne Prajapati
# Description:
#      This program lets users choose mathematical operations
#      to perform on complex numbers.
# ---------------------------------------------------------------
import math

class ComplexNumberCalculator:

    def __init__(self):
        # Store complex numbers and reusable numeric inputs
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
        print("6. Get Phase Difference")
        print("7. Get Complex Number from magnitude and phase")
        print("8. EXIT")

    def validate_complex_input(self):
        """Validate two complex numbers."""
        try:
            self.first_complex_number = complex(
                input("Enter first complex number (example: 3+4j): ").strip().replace(' ', ''))
        except ValueError:
            raise ValueError("Invalid first complex number format.")

        try:
            self.second_complex_number = complex(
                input("Enter second complex number (example: 10+j): ").strip().replace(' ', ''))
        except ValueError:
            raise ValueError("Invalid second complex number format.")

        return True

    def validate_modulus_input(self):
        """Validate real and imaginary numeric input for magnitude/modulus."""
        real_number = input("Enter a real number: ").strip()
        imaginary_number = input("Enter imaginary number: ").strip()

        # Check if both are pure numeric (no j, i, symbols)
        if not real_number.replace(".", "", 1).replace("-", "", 1).isdigit():
            raise ValueError("Real number part must be a numeric value.")

        if not imaginary_number.replace(".", "", 1).replace("-", "", 1).isdigit():
            raise ValueError("Imaginary number part must be a numeric value (no 'i' or 'j').")

        self.real_number = float(real_number)
        self.i_number = float(imaginary_number)
        return True

    def validate_phase_magnitude_input(self):
        """Validate magnitude and phase angle input."""
        magnitude = input("Enter magnitude: ").strip()
        phase_deg = input("Enter phase angle in degrees: ").strip()

        if not magnitude.replace(".", "", 1).replace("-", "", 1).isdigit():
            raise ValueError("Magnitude must be numeric.")

        if not phase_deg.replace(".", "", 1).replace("-", "", 1).isdigit():
            raise ValueError("Phase angle must be numeric.")

        self.real_number = float(magnitude)
        self.i_number = float(phase_deg)
        return True

    def get_user_input(self):
        """Gets the menu choice and call to correct input validator."""
        choice = input("Enter number (1-8): ")

        #validate choice
        if not choice.isdigit():
            raise ValueError("Menu choice must be a number.")

        self.choice = int(choice)

        if not 1 <= self.choice <= 8:
            raise ValueError("Menu choice must be between 1 and 8.")

        match self.choice:
            case 8:
                # EXIT
                return False  # EXIT
            case 5:
                # Magnitude inputs
                return self.validate_modulus_input()
            case 6:
                # Phase difference needs 2 complex numbers
                return self.validate_complex_input()
            case 7:
                # Polar inputs (magnitude + phase)
                return self.validate_phase_magnitude_input()
            case _:
                # For add, subtract, multiple and division (operations 1-4)
                return self.validate_complex_input()

    def phase_operation(self):
        """Computes the phase difference of two complex numbers."""
        first_complex_number = self.first_complex_number
        second_complex_number = self.second_complex_number

        #phase = tan^-1(b/a) or atan2(b,a)
        phase1 = math.atan2(first_complex_number.imag, first_complex_number.real)
        phase2 = math.atan2(second_complex_number.imag, second_complex_number.real)

        print("First phase:", phase1, "radians")
        print("Second phase:", phase2, "radians")
        print("Phase difference (first phase - second phase):", phase2 - phase1, "radians")

    def perform_operation(self):
        """Perform selected complex number operation."""
        match self.choice:
            case 1: #Addition
                print("The sum of complex number is: ", self.first_complex_number + self.second_complex_number)
            case 2: #Subtraction
                print("The difference of complex number is: ", self.first_complex_number - self.second_complex_number)
            case 3: #Multiplication
                print("The product of complex number is: ", self.first_complex_number * self.second_complex_number)
            case 4: #Division
                try:
                    print("The quotient of complex number is: ", self.first_complex_number / self.second_complex_number)
                except ZeroDivisionError:
                    raise ValueError("Error: Cannot divide by zero complex number.")
            case 5: #magnitude =sqrt(x^2 + y^2)
                magnitude = math.sqrt(self.real_number**2 + self.i_number**2)
                print("The magnitude of the complex number is: ", magnitude)
            case 6: # Phase difference
                self.phase_operation()
            case 7:
                magnitude = self.real_number
                angle_deg = self.i_number
                angle_rad = math.radians(angle_deg)

                complex_value = magnitude * (math.cos(angle_rad) + 1j * math.sin(angle_rad))

                print("Complex number from magnitude and phase:", complex_value)
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
            if user_input == False:
                break

            complex_number_calculator.perform_operation()

            # Ask user if they want another operation, if no exit the loop
            again = input("Do you perform another operation and display the menu? (Y/N): ").strip().upper()

            if again != "Y":
                print("\nThank you for using this Complex Number Calculator.!")
                break
        except ValueError as err:
            print("\nInvalid input:", err)
            print("Please try again.\n")

