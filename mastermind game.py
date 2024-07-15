'''MASTERMIND GAME:
------------------
The players play the game against each other;let's assume player1 and player2,
player1 plays first by setting a multi-digit number.
player2 now tries his first attempt at guessing the number.
If player 2 succeedes in his first attempt(despite odds which ar highly unlikely) he wins the game and is crowned mastermind! if not,then player1 hints by revealing which digits or numbers player 2 got correct.
The game continues till player 2 eventually is able to guess the number entirely.
Now,player 2 gets to set the number and player 1 plays the part of guessing the number.
If player 1 is able to guess the number within a lesser number of tries than player2 took,then player1 wins the game and is crowned mastermind player1 wins the game and is crowned mastermind
If not,then player2 wins the game.'''
import random

# the .randrange() function generates
# a random number within the specified range.
num = random.randrange(1000, 10000)

n = int(input("Guess the 4 digit number:"))

# condition to test equality of the
# guess made. Program terminates if true.
if(n == num):
	print("Great! You guessed the number in just 1 try! You're a Mastermind!")
else:
	# ctr variable initialized. It will keep count of
	# the number of tries the Player takes to guess the number.
	ctr = 0

	# while loop repeats as long as the Player
	# fails to guess the number correctly.
	while(n != num):
		# variable increments every time the loop
		# is executed, giving an idea of how many
		# guesses were made.
		ctr += 1

		count = 0

		# explicit type conversion of an integer to
		# a string in order to ease extraction of digits
		n = str(n)

		# explicit type conversion of a string to an integer
		num = str(num)

		# correct[] list stores digits which are correct
		correct = []

		# for loop runs 4 times since the number has 4 digits.
		for i in range(0, 4):
			# checking for equality of digits
			if(n[i] == num[i]):
				# number of digits guessed correctly increments
				count += 1
				# hence, the digit is stored in correct[].
				correct.append(n[i])
			else:
				continue

		# when not all the digits are guessed correctly.
		if (count < 4) and (count != 0):
			print("Not quite the number. But you did get ",
				count, " digit(s) correct!")
			print("Also these numbers in your input were correct.")

			for k in correct:
				print(k, end=' ')

			print('\n')
			print('\n')
			n = int(input("Enter your next choice of numbers: "))

		# when none of the digits are guessed correctly.
		elif(count == 0):
			print("None of the numbers in your input match.")
			n = int(input("Enter your next choice of numbers: "))

	if n == num:
		print("You've become a Mastermind!")
		print("It took you only", ctr, "tries.")
