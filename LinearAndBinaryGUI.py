import random
import tkinter as tk
from tkinter import *



# GUI setup
gui = tk.Tk()

#set window size

gui.geometry("400x400")

# Lables for text boxes
tk.Label(gui, text="Size of Array?: ").grid(row=0)
tk.Label(gui, text="Number to search for?: ").grid(row=1)


# Creating text boxes

array_size = tk.Entry(gui, width=100)
number_search = tk.Entry(gui, width=100)

# Placing text boxes im GUI
array_size.grid(row=0, column=1)
number_search.grid(row=1, column=1)

#Clear button
def clear_text():
   array_size.delete(0, END)
   number_search.delete(0, END)

def randomArray(array_size):
    array_size = []
    for x in range (len(array_size)):
        array_size.append(random.randrange(0, array_size))
              
    return array_size



def linear_search_button(array_size, number_search):
    for x in range(len(array_size.get())):
        if randomArray.array_size[x] == number_search:
            return(f'Found {number_search}')

    return ("Not found")

label=tk.Label(gui, text="Random Array:").grid(row=5)


# def Binary_search_button():
tk.Button(gui, 
          text='Linear Search',height= 1, width=10, command=lambda: randomArray(array_size)).grid(row=3, column=0, 
          sticky=tk.W, pady=4)
tk.Button(gui, 
          text='Clear', command=clear_text).grid(row=4, column=0, sticky=tk.W, pady=4)
tk.Button(gui, 
          text='Quit', command=quit).grid(row=4, column=1, sticky=tk.W, pady=4)


tk.mainloop()

