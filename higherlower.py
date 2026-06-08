from random import choice
print("welcome to HIGHER LOWER Game !")

logo = """
    __  ___       __             
   / / / (_)___ _/ /_  ___  _____
  / /_/ / / __ `/ __ \/ _ \/ ___/
 / __  / / /_/ / / / /  __/ /    
/_/ ///_/\__, /_/ /_/\___/_/     
   / /  /____/_      _____  _____
  / /   / __ \ | /| / / _ \/ ___/
 / /___/ /_/ / |/ |/ /  __/ /    
/_____/\____/|__/|__/\___/_/     
"""


vs = """
 _    __    
| |  / /____
| | / / ___/
| |/ (__  ) 
|___/____(_)
"""
score = 0
game_data = [
    {
    "name": "Instagram",
    "follower_count": 346,
    "description" : "Social media platform",
    "country" : "United States"
    },
    {
    "name": "Cristiano Ronaldo",
    "follower_count": 215,
    "description" : "Footballer",
    "country" : "Portugal"
    },
    {
    "name": "Ariana Grande",
    "follower_count": 183,
    "description" : "Musician and actress",
    "country" : "United States"
    },
    {
    "name": "Dwayne Johnson",
    "follower_count": 181,
    "description" : "Actor and professional wrestler",
    "country" : "United States"
    },
    {
    "name": "Selena Gomez",
    "follower_count": 174,
    "description" : "Musician and actress",
    "country" : "United States"
    },
    {
    "name": "Kylie Jenner",
    "follower_count": 172,
    "description" : "Reality TV personality and businesswoman",
    "country" : "United States"
    },
    {
    "name": "Kim Kardashian",
    "follower_count": 167,
    "description" : "Reality TV personality and businesswoman",
    "country" : "United States"
    },
    {
    "name": "Lionel Messi",
    "follower_count": 149,
    "description" : "Footballer",
    "country" : "Argentina"
    },
    {
    "name": "Beyoncé",
    "follower_count": 141,
    "description" : "Musician and actress",
    "country" : "United States"
    },
    {
    "name": "Neymar",
    "follower_count": 138,
    "description" : "Footballer",
    "country" : "Brazil"
    },
    {
        "name": "National Geographic",
        "follower_count": 135,
        "description" : "Magazine",
        "country" : "United States"
    },
    {
        "name": "Virat Kohli",
        "follower_count": 157,
        "description" : "Cricketer",
        "country" : "India"
    },
    {
        "name": "Justin Bieber",
        "follower_count": 133,
        "description" : "Musician",
        "country" : "Canada"
    },
    {
        "name": "Taylor Swift",
        "follower_count": 131,
        "description" : "Musician",
        "country" : "United States"
    },
    {
        "name" : "Priyanka Chopra Jonas",
        "follower_count": 543,
        "description" : "Actress and singer",
        "country" : "India"
    },
    {
        "name" : "Deepika Padukone",
        "follower_count": 321,
        "description" : "Actress",
        "country" : "India"
    },
    {
        "name" : "Shah Rukh Khan",
        "follower_count": 290,
        "description" : "Actor",
        "country" : "India"
    },
    {
        "name" : "Salman Khan",
        "follower_count": 280,
        "description" : "Actor",
        "country" : "India"
    }
]
def check_answer( component_a, component_b):
    if component_a['follower_count'] > component_b['follower_count']:
        return 'a'
    else:
        return 'b'

def get_to_play():

    game_should_continue = True
    while game_should_continue:
        print(logo)
    
        component_a = choice(game_data)
        component_b = choice(game_data)
        if component_a == component_b:
            component_b = choice(game_data)
        print(f"Compare A : {component_a['name']},{component_a['description']} from {component_a['country']}")
        print(vs)
        print(f"Against B : {component_b['name']},{component_b['description']} from {component_b['country']}")
        user_input = input("Who has more followers ? Type 'A' or 'B' : ").lower()
        correct_answer = check_answer(component_a, component_b)
        if user_input == correct_answer:
            global score
            score += 1
            print(f"You are right ! your score is {score}")
        else:
            print(f"Sorry, you are wrong ! The final score is : {score}")
            game_should_continue = False

        
        
get_to_play()
