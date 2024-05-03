from tkinter import messagebox, simpledialog, Tk




if __name__ == '__main__':
    window = Tk()
    window.withdraw()
    # TODO)
    #  1. Use a boolean variable to indicate if it is the weekend.
    #     Display a different message to the user depending on whether it is
    #     the weekend or not.
    is_weekend = False
    day_of_week = simpledialog.askstring(title=None, prompt="What day is it?")
    if day_of_week == 'Saturday' or day_of_week == 'Sunday':
        is_weekend = True

    if is_weekend:
        messagebox.showinfo(title="ok", message="Go enjoy the weekend!")
    else:
        messagebox.showinfo(title="ok", message="Sadly you still have school")


    #  2. Use a boolean variable to indicate if a student passed an exam.
    #     Display a different message to the user depending on whether they
    #     passed or not.
    passed_exam = False
    score = simpledialog.askstring(title=None, prompt="What score did you get?")
    if score > '70 percent':
        passed_exam = True

    if passed_exam:
        messagebox.showinfo(title=None, message="Congrats, you passed! :)")
    else:
        messagebox.showinfo(title=None, message="You did not pass unfortunatly")

    #  3. Use a boolean variable to indicate if a game is over. When the game
    #     is over, tell the user.
    game_finished = False
    number = simpledialog.askstring(title=None, prompt="What is 2 + 2?")
    if number == '4':
     game_finished = False
    else:
        exit()
    if not game_finished:
        messagebox.showinfo(title=None, message="Congrats! Continue forward")

    chicken = simpledialog.askstring(title=None, prompt="What is 5+5?")
    if chicken == '10':
        game_finished = False
    else:
        exit()
    if not game_finished:
        messagebox.showinfo(title=None, message="Congrats! Continue forward")






    #  4. Use two boolean variables, one to indicate if a shape should be red,
    #     the other to indicate if the shape is to be square. When both
    #     variables are true, use a turtle to draw a red square.
