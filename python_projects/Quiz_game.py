import os
import random as rnd

score = 0
n_question = 0
done = []
keys = []

general_qa = {
    "What is the capital of France?": "paris",
    "What is the largest planet in the solar system?": "jupiter",
    "Who wrote 'Romeo and Juliet'?": "William shakespeare",
    "What is the chemical symbol for water?": "H2O",
    "How many continents are there on Earth?": "7",
    "What is the smallest prime number?": "2",
    "Who painted the Mona Lisa?": "leonardo da vinci",
    "What is the square root of 64?": "8",
    "What is the main ingredient in bread?": "flour",
    "What is the speed of light?": "299,792,458 meters per second",
    "Who discovered gravity?": "isaac newton",
    "What is the largest ocean on Earth?": "pacific Ocean",
    "What is the freezing point of water in Celsius?": "0 degrees",
    "What is the longest river in the world?": "nile River",
    "What is the currency of Japan?": "yen",
    "What is the largest mammal on Earth?": "blue Whale",
    "What is the boiling point of water in Celsius?": "100 degrees",
    "Who is known as the father of computers?": "charles babbage",
    "What is the hardest natural substance on Earth?": "diamond",
    "What is the name of the galaxy we live in?": "milky way"
}

for key in general_qa.keys():
    keys.append(key)


def clear():
    os.system('cls' if os.name == 'nt' else 'clear')


def question():
    qua = rnd.choice(keys)
    if qua not in done:
        done.append(qua)
        return qua


is_running = True
while is_running:
    qua = question()
    print(qua)
    answer = input('Please enter your answer: ')
    if answer == general_qa[qua]:
        print("It's right!")
    else:
        print("Wrong answer")

    choice = input('Next question? Y for yes and N for no').lower()
    is_running = False if choice == 'n' else True