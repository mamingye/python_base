secret_number=9
guess_count=0
guess_limit=3
while guess_count < guess_limit:
    guess_input=int(input('Guess:'))
    guess_count+=1
    if  guess_input == secret_number:
        print("You Win!")
        break
else:
        print("you failed")