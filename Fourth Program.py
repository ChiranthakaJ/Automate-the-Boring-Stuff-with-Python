#This is a program called Collatz Sequence. This is the simplest version of it.
def collatz(number):
  """
  This function calculates the next number in the Collatz sequence for a given number.

  Args:
      number: The current number in the sequence.

  Returns:
      The next number in the Collatz sequence.
  """
  if number % 2 == 0:
    return number // 2
  else:
    return 3 * number + 1

# Example usage
next_number = collatz(11)
print(next_number)  # Output: 34