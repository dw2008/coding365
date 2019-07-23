import random
# spam = 1
# assert spam == spam < 10, "This thang has to be less than 10 boi"
# eggs = 'yeet'
# bacon = 'YeEt'
# assert eggs == eggs.lower() != bacon.lower(), "Dude eggs and bacon aren't the same"
# assert eggs.upper == bacon.lower, "Yay this might work"
guess = raw_input('Guess please: ')
while guess.lower() not in ('heads', 'tails') :
    print('Guess the coin toss! Enter heads or tails:')
    guess = raw_input('Guess again please: ')
toss = random.randint(0, 1)
if toss == 0 :
    toss = 'tails'
elif toss == 1 :
    toss = 'heads'
if toss == guess.lower :
    print('Correct')
else :
    print('hA HA wrong')
    guessb = raw_input('Now you can probably get it ')
    if toss == guessb.lower() :
        print('Good job you get a participation prize')
    else :
        print('Either you are doing this on purpose or your blind or forgetful')
        