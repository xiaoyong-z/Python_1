print("Please think of a number between 0 and 100!")
low = 0
high = 100
while True:
    ans = (low + high) // 2
    print("Is your secret number " + str(ans) + "?")
    result = input("Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly. ")
    if result != 'c' and result != 'h' and result != 'l':
        print("Sorry, I did not understand your input.")
        continue
    if result == 'c':
        print("Game over. Your secret number was: " + str(ans))
        break
    elif result == 'h':
        high = ans
    elif result == 'l':
        low = ans