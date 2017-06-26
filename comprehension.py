import random  # import random module

guessesTaken = 0  # assign 0 to guessesTaken variable

print('Hello! What is your name?')  # output the string
myName = input()  # assign myName to user input

number = random.randint(1, 20)  # assign number to a random number between 1 and 20
print('Well, ' + myName + ', I am thinking of a number between 1 and 20.')  # output string and the user input

while guessesTaken < 6:  # create a loop until 6
    print('Take a guess.')  # output the string
    guess = input()  # assign guess to user input
    guess = int(guess)  # convert user input to integer

    guessesTaken += 1  # increase the loop variable by 1

    if guess < number:  # create "if" control flow to decide if the user input is less than the random number
        print('Your guess is too low.')  # if so, output the string

    if guess > number:  # check another parameter if the user input is greater thean the random number
        print('Your guess is too high.')  # output the string

    if guess == number:  # check the equality of the user input and the random number
        break  # in this case, end the loop

if guess == number:  # check the equality of the user input and the random number
    guessesTaken = str(guessesTaken)  # convert the guessesTaken variable to string
    print('Good job, ' + myName + '! You guessed my number in ' + guessesTaken + ' guesses!')  # output the string with
    #  the user input myName and the variable guessesTaken

if guess != number:  # if user input does not equals to random number
    number = str(number)  # convert random number to string
    print('Nope. The number I was thinking of was ' + number)  # output the string with the random number
