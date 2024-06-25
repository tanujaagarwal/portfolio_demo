import random

def generate_number():
  """Generates a random 4-digit number (excluding leading zeros)."""
  while True:
    num = random.randrange(1000, 10000)
    if num // 1000 != 0:  # Ensure no leading zero
      return num

def get_guess():
  """Prompts the user for a valid 4-digit guess and returns it as an integer."""
  while True:
    try:
      guess = int(input("Guess the 4-digit number: "))
      if guess < 1000 or guess >= 10000:
        raise ValueError
      return guess
    except ValueError:
      print("Invalid input. Please enter a 4-digit number.")

def check_guess(guess, number):
  """
  Checks the guess against the number and returns a tuple containing:
  - Number of bulls (correct digits in the correct place)
  - Number of cows (correct digits in the wrong place)
  """
  bulls = 0
  cows = 0
  guess_str = str(guess)
  number_str = str(number)

  for i in range(4):
    if guess_str[i] == number_str[i]:
      bulls += 1
    elif guess_str[i] in number_str:
      cows += 1

  return bulls, cows

def main():
  """Runs the guessing game."""
  number = generate_number()
  guesses = 0

  while True:
    guess = get_guess()
    guesses += 1

    bulls, cows = check_guess(guess, number)

    if bulls == 4:
      print(f"Congratulations! You guessed the number in {guesses} tries!")
      break
    else:
      feedback = f"{bulls} bull(s) and {cows} cow(s)"
      print(feedback if cows > 0 else "None of the digits are correct.")

if __name__ == "__main__":
  main()

