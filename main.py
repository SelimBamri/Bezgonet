from tkinter import *
import json
from Country import Country
import random
from flags_game import flag_game
from maps_game import map_game
from capitals_game import capital_game


country_list = []
with open("data.json", "r") as file:
    data = json.load(file)
    for country_data in data["countries"]:
        country = Country(country_data["name"], country_data["capital"], country_data["flag"], country_data["map"])
        country_list.append(country)


def generate_question():
    answers = random.sample(country_list, 4)
    flag = answers[0].flag
    map = answers[0].map
    name = answers[0].name
    capital = answers[0].capital
    random.shuffle(answers)
    answers_dict = {
        "name": name,
        "flag": flag,
        "capital": capital,
        "map": map,
        "option_1": answers[0],
        "option_2": answers[1],
        "option_3": answers[2],
        "option_4": answers[3]
    }
    return answers_dict


def generate_questions():
    questions_list = []
    for _ in range(300):
        questions_list.append(generate_question())
    return questions_list


def main_menu():
    def quit_game():
        screen.destroy()

    def final_flag_game():
        screen.destroy()
        flag_game(main_menu, generate_questions)

    def final_map_game():
        screen.destroy()
        map_game(main_menu, generate_questions)

    def final_capital_game():
        screen.destroy()
        capital_game(main_menu, generate_questions)

    screen = Tk()
    screen.attributes('-fullscreen', True)
    bg = PhotoImage(file="backgrounds/background.png")
    label1 = Label(screen, image=bg)
    label1.place(x=0, y=0)

    flags_button_image = PhotoImage(file="control_buttons/flags_button.png")
    flag_button = Button(image=flags_button_image, highlightthickness=0, command=final_flag_game)
    flag_button.place(x=200, y=300)

    maps_button_image = PhotoImage(file="control_buttons/maps_button.png")
    map_button = Button(image=maps_button_image, highlightthickness=0, command=final_map_game)
    map_button.place(x=200, y=500)

    capitals_button_image = PhotoImage(file="control_buttons/capitals_button.png")
    capital_button = Button(image=capitals_button_image, highlightthickness=0, command=final_capital_game)
    capital_button.place(x=200, y=700)

    quit_button_image = PhotoImage(file="control_buttons/quit_button.png")
    flag_button = Button(image=quit_button_image, highlightthickness=0, command=quit_game)
    flag_button.place(x=900, y=700)
    screen.mainloop()


main_menu()
