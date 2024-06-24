#This is a program called Collatz Sequence.

def collatz(number):
  """
  This function calculates and prints the next number in the Collatz sequence.

  Args:
      number: The current number in the sequence.
  """
  if number % 2 == 0:
    print(number // 2)
    return number // 2
  else:
    print(3 * number + 1)
    return 3 * number + 1

# Get user input and handle potential errors
while True:
  try:
    number = int(input("Enter a positive integer: "))
    if number <= 0:
      raise ValueError("Please enter a positive integer.")
    break  # Exit the loop if valid input is received
  except ValueError:
    print("Invalid input. Please enter a positive integer.")

# Call the collatz function with the valid integer
collatz(number)