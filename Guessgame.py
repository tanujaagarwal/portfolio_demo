import random
words = ('apple', 'angel', 'beach', 'blaze', 'brave', 'brick', 'brief', 'bring', 'broad', 'broke','brush', 'buddy', 'build', 'bunch', 'burst', 'cable', 'carry', 'catch', 'cause', 'chain','chair', 'charm', 'chase', 'chest', 'chief', 'child', 'chill', 'choir', 'chose', 'claim', 'class', 'clean', 'clear', 'climb', 'clock', 'close', 'cloud', 'coach', 'coast', 'color', 'count', 'craft', 'crash', 'crazy','cream', 'crime', 'cross', 'crowd', 'crown', 'curve','cycle', 'dance', 'dealt', 'death', 'debut', 'delay', 'depth', 'devil', 'diary', 'dirty', 'dream', 'drift', 'drink', 'drive', 'eager', 'early', 'earth', 'elbow', 'elder', 'elect', 'empty', 'enemy', 'entry', 'equal', 'equip', 'essay', 'event', 'every', 'exact', 'exist','extra', 'faith', 'false', 'fault', 'favor', 'feast', 'fever', 'field', 'fifth', 'final','first', 'flame', 'flash', 'fleet', 'floor', 'focus', 'force', 'forth', 'forum', 'found','frame', 'fresh', 'front', 'fruit', 'funny', 'ghost', 'giant', 'given', 'globe', 'glory', 'grace', 'grade', 'grand', 'grant', 'grass', 'great', 'green', 'greet', 'group', 'guard','guest', 'guide', 'habit', 'happy', 'harsh', 'heart', 'heavy', 'honey', 'honor', 'horse','hotel', 'house', 'human', 'hurry', 'ideal', 'image', 'index', 'inner', 'input', 'issue','joint', 'judge', 'juice', 'knife', 'knock', 'label', 'large', 'laser', 'later', 'laugh','layer', 'learn', 'leave', 'level', 'light', 'limit', 'local', 'loyal', 'lucky', 'lunch','magic', 'major', 'maker', 'march', 'match', 'mayor', 'media', 'metal', 'might', 'minor','model', 'money', 'month', 'moral', 'motor', 'mount', 'mouse', 'music', 'naked', 'nasty','never', 'noble', 'noise', 'north', 'novel', 'nurse', 'occur', 'ocean', 'offer', 'often','older', 'other', 'outer', 'owner', 'panel', 'panic', 'party', 'peace', 'phase', 'phone','photo', 'piano', 'piece', 'pilot', 'pitch', 'place', 'plain', 'plane', 'plant', 'plate','point', 'pound', 'power', 'press', 'price', 'pride', 'prime', 'print', 'prior', 'prize','proof', 'proud', 'prove', 'queen', 'quick', 'quiet', 'radio', 'raise', 'reach', 'react','ready', 'refer', 'relax', 'reply', 'rival', 'river', 'roast', 'robot', 'rough', 'round','route', 'royal', 'ruler', 'rural', 'scale', 'scene', 'scope', 'score', 'sense', 'serve','seven', 'shall', 'shape', 'share', 'sharp', 'sheep', 'sheet', 'shelf', 'shift', 'shine','shirt', 'shock', 'shoot', 'short', 'shout', 'sight', 'silly', 'since', 'skill', 'sleep','slice', 'slide', 'small', 'smart', 'smile', 'smoke', 'solid', 'solve', 'sorry', 'sound','south', 'space', 'spare', 'speak', 'speed', 'spell', 'spend', 'spice', 'spite', 'split','sport', 'staff', 'stage', 'stake', 'stand', 'stare', 'start', 'state', 'steal', 'steel','stick', 'still', 'stock', 'stone', 'store', 'storm', 'story', 'strip', 'stuck', 'study','stuff', 'style', 'sugar', 'super', 'sweet', 'swing', 'sword', 'table', 'taste', 'teach','teeth', 'tempt', 'thank', 'their', 'theme', 'there', 'these', 'thick', 'thing', 'think','third', 'those', 'three', 'throw', 'tight', 'times', 'tired', 'title', 'today', 'topic','total', 'touch', 'tower', 'track', 'trade', 'trail', 'train', 'trend', 'trial', 'tribe','trick', 'trust', 'truth', 'twist', 'uncle', 'union', 'unite', 'urban', 'urged', 'usual','valid', 'value', 'video', 'visit', 'vital', 'voice', 'waste', 'watch', 'water', 'weigh','weird', 'whale', 'wheat', 'wheel', 'where', 'which', 'while', 'white', 'whole', 'whose','wider', 'worry', 'world', 'worth', 'would', 'wound', 'write', 'wrong', 'young', 'youth','yummy', 'zebra', 'zonal')
def isword(user_word, wordly_word):
    message = {0: "Marvellous", 1: "Excellent", 2: "Very good", 3: "Nice", 4: "Good", 5: "OK"}
    colors = []  # List to store color codes for each letter

    for i in range(len(user_word)):
        if user_word[i] == wordly_word[i]:
            colors.append("green")  # Green for correct position
        elif user_word[i] in wordly_word:
            colors.append("yellow")  # Yellow for letter present elsewhere
        else:
            colors.append("black")  # Black for letter not present

    # Print the user's guess with colors
    for i, letter in enumerate(user_word):
        print(letter,colors[i], end="")

    # Check if the word is guessed correctly
    if user_word == wordly_word:
        print("\n", message[0])  # "Marvellous" for correct guess
        return True
    else:
        return False


def play_wordle():
    random_word = random.choice(words)
    print(random_word)  # Don't reveal the word for actual gameplay
    print("Let's Play Wordle!")

    guesses_left = 6
    while guesses_left > 0:
        user_word = input("\nEnter word (5 letters): ")

        if len(user_word) != 5 or not user_word.isalpha():
            print("Please enter a valid 5-letter word.")
            continue

        if isword(user_word, random_word):
            break

        guesses_left -= 1
        print(f"\nYou have {guesses_left} guesses left.")

    if guesses_left == 0:
        print("\nEnd of Game. The correct word was:", random_word)


play_wordle()
