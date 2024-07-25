from higher_lower_anime_dict import anime_list
import random

a = random.choice(anime_list)
b = random.choice(anime_list)




def comparing_anime(a, b):
    """Function that takes as a variable year of broadcasting given anime series and compares it with other
    anime to return correct answer, which is older anime series."""
    anime_year_a = a["year"]
    anime_year_b = b["year"]
    correct_a = anime_year_a < anime_year_b
    correct_b = anime_year_a > anime_year_b

    return [correct_a, correct_b]

def correct_or_not(comparing):
    """Function that takes returned values from comparing_anime function and checks wether user's answer
    is correct or not."""
    print(f"Compare A: {a["title"]}, {a["genre"]}.")
    print(f"Against B: {b["title"]}, {b["genre"]}.")
    player_answer = input("Which anime is older?\n").lower()
    if comparing[0] == True and player_answer == 'a':
        return 'correct a'
    elif comparing[1] == True and player_answer == 'b':
        return 'correct b'
    
    return 'wrong'
    
def repeating(comparing, answering):
    """Function that keeps replacing the correct answer with the wrong one and generates a new random one."""
    global a, b
    if answering == 'correct a':
        a = b
        b = random.choice(anime_list)
        while a == b:
            b = random.choice(anime_list)
    elif answering == 'correct b':
        b = random.choice(anime_list)
        while a == b:
            b = random.choice(anime_list)
    return a, b

    

score = 0

while True:
    comparing = comparing_anime(a, b)
    answering = correct_or_not(comparing)
    if answering == 'correct a' or answering == 'correct b':
        a, b = repeating(comparing, answering)
    else:
        print("You lose")
        break





    










