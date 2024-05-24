"""
Use a while loop to recite the digits of pi
"""
from tkinter import messagebox, simpledialog, Tk



if __name__ == '__main__':
    window = Tk()
    window.withdraw()
    # TODO) Place the first 20 digits of pi into a variable as a string
    #  3.1415926535897932384

    # TODO) Print out the first 3 digits of pi. For example,
    #  pi_str[0]   # first digit
    #  pi_str[1]   # second digit
    pi_str = '31415926535897932384'
    print(pi_str[0])
    print(pi_str[2])
    print(pi_str[3])

    # TODO) Use a while loop to keep asking for the next digit of pi
    answer = simpledialog.askinteger(None, prompt = "What is the next letter of pi?")
    score = 3
    while score < len(pi_str):
        answer
    if answer == pi_str[score]:
        score += 1
    else:
        exit()


        # TODO) If they are correct, print "correct".
        #  If they are not, print "incorrect" and break out of the while loop



    # TODO) Print out how many digits of pi the user was able to recite
    #  in a row
