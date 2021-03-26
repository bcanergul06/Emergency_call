#!/usr/bin/python3
# -*- coding: utf-8 -*-
from lib.mixlib import menu_maker, menu_space

# Importing the Tkinter
import tkinter as tk
import tkinter.ttk as ttk
from tkinter import simpledialog, messagebox

# Added Transaction Receiver
def emergency_call_main_tx(tx):
    print("Data of the TX: "+str(tx.data))

# Added Menus
def emergency_call_main_cli(): 
    print(
        menu_maker(menu_number="earthquake",menu_text="Earthquake Call") + \
        menu_maker(menu_number="ambulance",menu_text="Ambulance Call") + \
        menu_space())

# Added command for menus 
def emergency_call_main_cli_command(choices_input): 

    if choices_input == "earthquake":
       print("Earthquake call is triggered.") # Warning for CLI
    elif choices_input == "ambulance":
       print("Ambulance call is triggered.") # Warning for CLI
        
# Added Button
def emergency_call_main_gui(main_gui,column,row):

    main_gui.earthquake_button = ttk.Button(main_gui.frame) # Button defination
    main_gui.earthquake_button.configure(text='Earthquake Call') # Button text configuration
    main_gui.earthquake_button.grid(column=str(column), padx='25', pady='20', row=str(row), sticky='n') # Button place defination with grid system
    import_arguments_earthquake_button = f"from apps.Emergency_call.emergency_call_main import earthquake_button_command" # An import defination for command of this button
    func_name_earthquake_button = "earthquake_button_command"  # An defination for command of this button
    main_gui.earthquake_button.configure(command= lambda: main_gui.apps_func(import_arguments_earthquake_button, func_name_earthquake_button)) # Setting the command button

    column += 1 # With this the next button will slide to the rigth from earthquake button

    main_gui.ambulance_button = ttk.Button(main_gui.frame) # Button defination
    main_gui.ambulance_button.configure(text='Ambulance Call') # Button text configuration
    main_gui.ambulance_button.grid(column=str(column), padx='25', pady='20', row=str(row), sticky='n') # Button place defination with grid system
    import_arguments_ambulance_button = f"from apps.Emergency_call.emergency_call_main import ambulance_button_command" # An import defination for command of this button
    func_name_ambulance_button = "ambulance_button_command"  # An defination for command of this button
    main_gui.ambulance_button.configure(command= lambda: main_gui.apps_func(import_arguments_ambulance_button, func_name_ambulance_button)) # Setting the command button

# Added command for earthquake button
def earthquake_button_command(main_gui):
    messagebox.showinfo('Earthquake Button', "Earthquake call is triggered.") # Warning for GUI
    print("Earthquake call is triggered.") # Warning for CLI

# Added command for ambulance button
def ambulance_button_command(main_gui):
    messagebox.showinfo('Ambulance Button', "Ambulance call is triggered.") # Warning for GUI
    print("Ambulance call is triggered.") # Warning for CLI
