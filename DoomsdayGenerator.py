import random
from tkinter import Tk, simpledialog, messagebox
from datetime import date
import sys


def time():
    current_year = date.today().year
    return (current_year + random.randint(1, 20))


def line_break_remover(file):
    hold = []
    for line in open(file):
        line = line.rstrip('\n')
        hold += [line]
    return hold
objects = line_break_remover('objects.txt')
plural_verbs = line_break_remover('verbs.txt')
singular_verbs = []
for verb in plural_verbs: #converts plural verbs to singular verbs
    if '#' in verb:
        multipart = True
    else:
        multipart = False
    if multipart:
        index = verb.find('#')
        ending = verb[index - 2:index]
        if ending == 'sh' or ending == 'x':
            verb = verb.replace('#', 'es')
        else:
            verb = verb.replace('#', 's')
    else:
        ending = verb[-2:]
        if ending == 'sh' or ending == 'x':
            verb = verb + 'es'
        else:
            verb = verb + 's'
        singular_verbs += [verb]
for i in range(len(plural_verbs)): #removes verb indication marker for singularization
    plural_verbs[i] = plural_verbs[i].replace('#', '')
causes_of_destruction = line_break_remover('cause of destruction.txt')

display = Tk()
display.withdraw()
def doomsday_generator():
    destructor = objects[random.randint(0, len(objects))]
    if destructor[-1] == 's':
        plural = True
    else:
        plural = False
    if plural:
        verb = plural_verbs[random.randint(0, len(plural_verbs) - 1)]
    else:
        verb = singular_verbs[random.randint(0, len(singular_verbs) - 1)]
    cause_of_destruction = causes_of_destruction[random.randint(0, len(causes_of_destruction) - 1)]
    messagebox.showinfo('prediction','Here is your prediction: \n\n' + destructor + ' ' + verb + ' the world ' + cause_of_destruction)
def prompter():
    result = messagebox.askyesno('Generate Doomsday', 'Do you wish to generate a doomsday prediction?')
    while result:
        if result:
            doomsday_generator()
            result = messagebox.askyesno('Generate Doomsday', 'Do you wish to generate a doomsday prediction?')
        else:
            sys.exit()
prompter()
display.mainloop()
    
