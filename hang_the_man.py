import random
from guessing import guess_list

word=random.choice(guess_list).lower()
word_letter = len(word)
game_over=False
tries=6

print(f'The Word you guessed is {word}')

result=[]
for _ in range(word_letter):
    result+='_'

while not game_over:
    user_guessing=input("Guess a letter: ")
    
    if user_guessing in result:
        print(f'The letter you have guessed is {user_guessing}')

    for pos in range(word_letter):
        letter=word[pos]
        if letter == user_guessing:
            result[pos]=letter

    if user_guessing not in word:
        print(f'You guessed {user_guessing}, This letter is not in the word, you lose a try')
        tries-=1
        if tries==0:
            game_over=True
            print('Game Over, You lose the game, try again later')

    print(f"{''.join(result)}")

    if '_' not in result:
        game_over=True
        print('You are a winner, Congratulations')

    from lives import pics
    print(pics[6-tries])
