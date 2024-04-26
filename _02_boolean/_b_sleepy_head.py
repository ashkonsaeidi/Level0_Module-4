from tkinter import messagebox




if __name__ == '__main__':
    # TODO)
    #  1. Use a boolean variable to indicate if it is the weekend.
    #     Display a different message to the user depending on whether it is
    #     the weekend or not.
    is_weekend = False
    day_of_week = 'Friday'
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

    if passed_exam:
        messagebox.showinfo(title="ok", message="Congrats, you passed!")


    #  3. Use a boolean variable to indicate if a game is over. When the game
    #     is over, tell the user.
    #  4. Use two boolean variables, one to indicate if a shape should be red,
    #     the other to indicate if the shape is to be square. When both
    #     variables are true, use a turtle to draw a red square.
