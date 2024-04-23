# Davis Arita and Yazan Khawaldeh
# CS 131 Pizza Project
# 11.17.2022

import tkinter
from tkinter import *


def click():  # the main function that access the info submitted by the customer and turns it into an order.
    TAX = 0.0875

    output.insert(END, "Your order is: ")  # prints a starting header
    selected = radio_var.get()  # retrieves the crust choice from the radio buttons
    pizza_size = size_input.get(1.0, "end-1c")  # retrieves the text imputed by the customer for size of pizza
    price = 0.0  # creates a base variable to store the price of the pizza

    if pizza_size.lower() == "small":  # compares the text in pizza_size and updates the price of the pizza accordingly
        price = 10.99
        size = "\nSmall Pizza"
    elif pizza_size.lower() == "medium":
        price = 12.99
        size = "\nMedium Pizza"
    else:
        price = 14.99
        size = "\nLarge Pizza"
    output.insert(END, size)

    crust = "\nCrust: "
    if selected == 1:  # compares the value of the pizza crust selection and updates the crust variable with the
        crust += "Thin-Crust"  # customers selection
        print(crust)
    elif selected == 2:
        crust += "Deep-dish"
        print(crust)
    else:
        crust += "Hand Tossed"
        print(crust)

    toppingsStr = "\nToppings: cheese"
    checkbutton1.get()
    checkbutton2.get()
    checkbutton3.get()
    checkbutton4.get()
    if checkbutton1.get():
        price += 1.25
        toppingsStr += ", pepperoni"
    if checkbutton2.get():
        price += 1.25
        toppingsStr += ", sausage"
    if checkbutton3.get():
        price += 1.25
        toppingsStr += ", mushrooms"
    if checkbutton4.get():
        price += 1.25
        toppingsStr += ", onions"

    output.insert(END, toppingsStr)

    output.insert(END, crust)  # prints the customer's crust selection to the order window.
    price *= TAX
    output.insert(END, "\nYour final cost is: $%.2f" % price)

    #output.insert(END, "%.2f" % price)  # prints the final price to the order window


prize = 0

root = Tk()  # instantiates the window under the name root.

root.geometry('1250x750')  # determines the overall size of the window

root.configure(background="black")  # makes the overall background of the main window black

photo1 = PhotoImage(file="pizza2.gif")  # stores the photo in the photo1 variable.  If you want to change the photo
# you'll need to add the photo to the folder where this file is located and
# change the name that is in quotes to the name of the photo you have chosen.

mylabel = Label(root, image=photo1, bg="black", anchor=CENTER)  # creates a label displaying the picture of the pizza sizes

mylabel.pack()

mylabel2 = Label(root, text="Enter your pizza size", bg="black", fg="white",
                 font="arial 14 bold", anchor=CENTER)  # creates a label prompting customer to type in the size of pizza they want
mylabel2.pack()

radio_var = IntVar()  # variable to hold the crust choice

Radiobutton(root, text="Thin-Crust", variable=radio_var, value=1).pack(side=RIGHT)  # thin-crust
Radiobutton(root, text="Thick-Crust", variable=radio_var, value=2).pack(side=RIGHT)  # thick crust
Radiobutton(root, text="Hand Tossed", variable=radio_var, value=3).pack(side=RIGHT)  # hand tossed

# checkboxes for toppings $1.25 each
checkbutton1 = IntVar()
checkbutton2 = IntVar()
checkbutton3 = IntVar()
checkbutton4 = IntVar()

pepperoni = Checkbutton(root, text="Pepperoni",
                        variable=checkbutton1,
                        onvalue=1,
                        offvalue=0,
                        height=2,
                        width=8)
sausage = Checkbutton(root, text="Sausage",
                      variable=checkbutton2,
                      onvalue=1,
                      offvalue=0,
                      height=2,
                      width=8)
mushroom = Checkbutton(root, text="Mushrooms",
                       variable=checkbutton3,
                       onvalue=1,
                       offvalue=0,
                       height=2,
                       width=8)
onion = Checkbutton(root, text="Onion",
                    variable=checkbutton4,
                    onvalue=1,
                    offvalue=0,
                    height=2,
                    width=8)
pepperoni.pack(side=LEFT)
sausage.pack(side=LEFT)
mushroom.pack(side=LEFT)
onion.pack(side=LEFT)

size_input = tkinter.Text(root, height=2,
                          width=10)  # creates the text box for customer to type in the size of the pizza
size_input.pack()

submit = Button(root, text="submit your order", command=click, anchor=CENTER)  # submit your order button.  Runs the click function.
submit.pack()

output = Text(root, height=15, width=75)  # creates the window to display the customer's order once they click submit
output.pack()

mainloop()

# Yazan, I haven't figured out how to center the order window, text entry, and submit button under the picture.
# Right now they are off center.
# We need to create a set of check boxes for the topping selection.  Created the boxes and labels (? think) near the
# code for the radio buttons and instead of (side=RIGHT) try (side=LEFT)?
# then we need to code the input up at the top in the click() function.
