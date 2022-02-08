from tkinter import *

score = 0
tries = 0


def flag_game(function, function2):
    questions = function2()

    def game():
        def game_over():
            def retry():
                global tries, score
                tries = 0
                score = 0
                root1.destroy()
                flag_game()

            def back():
                global tries, score
                tries = 0
                score = 0
                root1.destroy()
                function()

            root1 = Tk()
            root1.attributes('-fullscreen', True)
            canvas1 = Canvas(root1, width=1536, height=1025)
            background_image1 = PhotoImage(file="backgrounds/game_background.png")
            canvas1.create_image(768, 512.5, image=background_image1)
            canvas1.place(x=0, y=0)
            canvas1.create_text(768, 200, text="Game Over", font=("MamaKilo Decorative", 200))
            canvas1.create_text(768, 400, text=f"Your Score is {score}/{tries}", font=("MamaKilo Decorative", 50))
            retry_button_image = PhotoImage(file="control_buttons/retry_button.png")
            return_button_image = PhotoImage(file="control_buttons/return_button.png")
            menu_button = Button(root1, image=return_button_image, command=back, highlightthickness=0)
            retry_button = Button(root1, image=retry_button_image, command=retry, highlightthickness=0)
            menu_button.place(x=210, y=600)
            retry_button.place(x=868, y=600)
            root1.mainloop()

        def gameplay(i):
            def command_1():
                global score, tries
                tries += 1
                if questions[i]["option_1"].flag == questions[i]["flag"]:
                    score += 1
                canvas.itemconfig(scoreboard, text=f"{score}/{tries}")
                gameplay(i+1)

            def command_2():
                global score, tries
                tries += 1
                if questions[i]["option_2"].flag == questions[i]["flag"]:
                    score += 1
                canvas.itemconfig(scoreboard, text=f"{score}/{tries}")
                gameplay(i+1)

            def command_3():
                global score, tries
                tries += 1
                if questions[i]["option_3"].flag == questions[i]["flag"]:
                    score += 1
                canvas.itemconfig(scoreboard, text=f"{score}/{tries}")
                gameplay(i+1)

            def command_4():
                global score, tries
                tries += 1
                if questions[i]["option_4"].flag == questions[i]["flag"]:
                    score += 1
                canvas.itemconfig(scoreboard, text=f"{score}/{tries}")
                gameplay(i+1)

            global flag_image, option_1_image, option_2_image, option_3_image, option_4_image
            flag_image = PhotoImage(file=questions[i]["flag"])
            option_1_image = PhotoImage(file=questions[i]["option_1"].name)
            option_2_image = PhotoImage(file=questions[i]["option_2"].name)
            option_3_image = PhotoImage(file=questions[i]["option_3"].name)
            option_4_image = PhotoImage(file=questions[i]["option_4"].name)
            button1 = Button(root, image=option_1_image, command=command_1, highlightthickness=0)
            button2 = Button(root, image=option_2_image, command=command_2, highlightthickness=0)
            button3 = Button(root, image=option_3_image, command=command_3, highlightthickness=0)
            button4 = Button(root, image=option_4_image, command=command_4, highlightthickness=0)
            button1.place(x=1000, y=200)
            button2.place(x=1000, y=350)
            button3.place(x=1000, y=500)
            button4.place(x=1000, y=650)
            canvas.create_image(500, 530, image=flag_image)

        def game_countdown(number):
            if number >= 10:
                canvas.itemconfig(time_tracker, text=f"0:{number}")
            else:
                canvas.itemconfig(time_tracker, text=f"0:0{number}")
            if number > 0:
                root.after(1000, game_countdown, number-1)
            else:
                root.destroy()
                game_over()

        canvas.itemconfig(bgi, image=img)
        game_countdown(59)
        gameplay(0)

    def countdown_to_start(number):
        if number > 1:
            canvas.itemconfig(to_start, text=str(number-1))
        else:
            canvas.itemconfig(to_start, text="Start")
        if number > 0:
            root.after(1000, countdown_to_start, number-1)
        else:
            canvas.itemconfig(to_start, text="")
            game()

    root = Tk()
    root.attributes('-fullscreen', True)
    canvas = Canvas(root, width=1536, height=1025)
    background_image = PhotoImage(file="backgrounds/game_background.png")
    bgi = canvas.create_image(768, 512.5, image=background_image)
    img = PhotoImage(file="backgrounds/in_game_background.png")
    canvas.place(x=0, y=0)
    to_start = canvas.create_text(768, 400, text=4, font=("MamaKilo Decorative", 400))
    canvas.create_text(150, 50, text="Score:", font=("MamaKilo Decorative", 50))
    scoreboard = canvas.create_text(350, 50, text="0/0", font=("MamaKilo Decorative", 50))
    canvas.create_text(1000, 50, text="Time:", font=("MamaKilo Decorative", 50))
    time_tracker = canvas.create_text(1150, 50, text="1:00", font=("MamaKilo Decorative", 50))
    countdown_to_start(4)
    root.mainloop()


