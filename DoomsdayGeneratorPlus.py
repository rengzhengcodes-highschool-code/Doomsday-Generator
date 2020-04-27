import random
from tkinter import Tk, simpledialog, messagebox
from datetime import date
import sys


def time():
    current_year = date.today().year
    return str(current_year + random.randint(1, 20))


def line_break_remover(file):
    hold = []
    for line in open(file):
        line = line.rstrip('\n')
        hold += [line]
    return hold
objects = ['Asteroid', 'Lizards', 'Giraffes', 'Birds', 'Squirrels', 'The NSA', 'Bill Nye', 'Nukes', 'Apple', 'Amazon', 'Google', 'A 1000 degree knife', 'Uncle Iroh', 'Jack Sparrow', 'Chickens', 'KFC', 'Pizza Hut', 'Potatoes', 'Banana', 'Tomato', 'Watermelon', 'Goats', 'Mr. Grossman', 'A carriage ride', 'Nicholas Cage', 'The 11th floor pool', 'Roosters', 'Toaster', 'Cthulu', 'Cars (the movie)', 'Shrek', 'Mushrooms', 'Weeds (I have been told to specify the pest not the drug)', 'Coca Cola', 'Pepsi', 'Fanta', 'Red solo cups', 'Sprite', 'Mints', 'A button that says "do not press"', 'Jason Borne', 'The live action Avatar remake', 'John Cena', 'A goat', 'Garfield', 'The corpse of Nichola Tesla', 'Fredrich Wilhelm II', 'Otto von Bismarck', 'Queen Victoria', 'Betty White', 'Queen Elizabeth II', 'Nyan cat', 'Humans', 'Aliens', 'A UFO', 'The bougeoisie', 'Texas', 'Florida man', 'Peanuts', 'Charlie Brown', 'The Onion', 'Rick Astley']
plural_verbs = ['obliterate', 'demolish', 'wreck', 'disintegrate', 'destroy', 'anhillate', 'take over', 'annex', 'invade', 'steal', 'abscond', 'incinerate', 'bury', 'dab on', 'dominate', 'shred', 'captivate', 'mind control', 'capture', 'end', 'slice', 'kill', 'stop', 'sabotage', 'stymie', 'ruin', 'wreck', 'smash', 'shatter', 'crash', 'blemish', 'impair', 'injure', 'scar', 'deface', 'crush', 'hydraulic press', 'eliminate', 'eradicate', 'liquidate', 'extinguise', 'massacre', 'butcher', 'exterminate', 'decimate', 'take out', 'vanquish', 'overwhelm', 'clobber', 'pulverize', 'amalgamate', 'coup', 'purchase']
singular_verbs = ['obliterates', 'demolishes', 'wrecks', 'disintegrates', 'destroys', 'anhillates', 'annexs', 'invades', 'steals', 'absconds', 'incinerates', 'burys', 'dominates', 'shreds', 'captivates', 'mind controls', 'captures', 'ends', 'slices', 'kills', 'stops', 'sabotages', 'stymies', 'ruins', 'wrecks', 'smashes', 'shatters', 'crashes', 'blemishes', 'impairs', 'injures', 'scars', 'defaces', 'crushes', 'hydraulic presss', 'eliminates', 'eradicates', 'liquidates', 'extinguises', 'massacres', 'butchers', 'exterminates', 'decimates', 'vanquishes', 'overwhelms', 'clobbers', 'pulverizes', 'amalgamates', 'coups', 'purchases']
causes_of_destruction = ['by hugging it.', 'with the moon.', 'by the power of friendship.', 'with a 1000 degree knife.', 'with floridaman.', 'by using a tractor beam.', 'by putting it into the bath with a toaster.', 'by being just too darn cuddly.', 'with the power of environmental destruction.', 'using grenades.', 'using weaponized Oedipus Rex.', 'by FTL warp ramming.', 'with nukes.', 'by eating all the Taco Bell.', 'by causing a tsunami of Zoom calls.', 'by cancelling all Amazon Prime accounts.', 'with the destruction of the Netflix databanks.', 'using Steve Buscemi.', 'using a potato that looks like Channing Tatum.', 'with the British.', 'using the rage of New Yorkers as pineapple is put on pizza.', "with Reng's inability to cook.", 'with a jetski.', 'by causing a collective fart.', 'by asserting dominance in with a T-pose.', 'by giving 5 year olds their every wish.', 'by fulfilling every sarcastic comment about a deadly cause.', 'by giving Stuyvesant students numerical grades.', 'using a gigantic teakettle.', 'by giving the earth a long carriage ride. ;)', "using Ebtesham's basketball.", 'using a name sign.', 'with all the socks ever lost.', 'with shorturl.at/pRWY8.', 'with a gigantic tardigrade.', "by saying 'this sentence is false.'", 'using the activities of the Hudson staircase.']
display = Tk()
display.withdraw()
def doomsday_generator():
    destructor = objects[random.randint(0, len(objects) - 1)]
    if destructor[-1] == 's':
        plural = True
    else:
        plural = False
    if plural:
        verb = plural_verbs[random.randint(0, len(plural_verbs) - 1)]
    else:
        verb = singular_verbs[random.randint(0, len(singular_verbs) - 1)]
    cause_of_destruction = causes_of_destruction[random.randint(0, len(causes_of_destruction) - 1)]
    messagebox.showinfo('prediction','Here is your prediction: \n\n' + destructor + ' ' + verb + ' the world in ' + time() + ' ' + cause_of_destruction)
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
    
