# add entry or lookup Entry
# provide task name, number of minutes spent, additional notes
# write to a csv file  
# find by date, time spend, exact search, by pattern 
import csv
import os.path
from ctypes.test.test_array_in_pointer import Value
MENU_OPTIONS = ('(A)dd Entry', '(S)earch Entries', '(Q)uit')
MENU_CHOICES = ('A', 'S', 'Q')
VALIDATOR = ('Y', 'N') 
entry_counter = 0



class Entry:
    def __init__(self, name, task_name, time, note):
        self.name = name
        self.task_name = task_name
        self.time = time
        self.note = note
        

def add_entry():
    print('Entry logger:')
    while True:
        try:
            name = input('Workers name: ')
            validator = input("Is '{}' correct? (Y, N): ".format(name))
            validator.upper()
            if validator not in VALIDATOR:
                raise ValueError
            
            if validator == 'N':
                raise ValueError
            
        except (ValueError, TypeError):
            print('What is the Correct Workers name?')
            
        else:
            break
        
    while True:
        try:
            task_name = input('Task name: ')
            validator = input("Is '{}' correct? (Y, N): ".format(task_name))
            validator.upper()
            if validator not in VALIDATOR:
                raise ValueError
            
            if validator == 'N':
                raise ValueError
            
        
        except (ValueError, TypeError):
            print('what is the True task name?')
        
        else:
            break
        
    while True:
        try:
            str_time = input('How long was spent on such task (minutes)?: ')
            time = int(str_time)
            validator = input("Is '{}' minutes correct? (Y, N): ".format(time))
            validator.upper()
            if validator not in VALIDATOR:
                raise ValueError
            
            if validator == 'N':
                raise ValueError
            
            
        except (ValueError, TypeError):
            print('what was the correct time spent?')
        
        else:
            break
        
    while True:
        try:
            note_check = input('is there an additional note you would like to add? (Y,N): ')
            note_check.upper()
            if note_check not in VALIDATOR:
                raise ValueError
            
            if note_check == 'Y':
                note = input('Note Adder: ')
                validator = input("Is '{}' correct? (Y, N): ".format(note))
                validator.upper()
                if validator not in VALIDATOR:
                    raise ValueError
            
                if validator == 'N':
                    raise ValueError
               
            if note_check == 'N':
                note = 'None'
            
        except (ValueError, TypeError):
            print('what is the note you would like to add?')
        else:
            break
    
    new_note = Entry(name, task_name, time, note)
    
    with open("Work_log.csv", "a") as csvfile:
        fieldnames = ['Name', 'Task Name', 'Time Spent', 'Note']
        notewriter = csv.DictWriter(csvfile, fieldnames=fieldnames)
        notewriter.writerow({
            'Name': new_note.name,
            'Task Name': new_note.task_name,
            'Time Spent': new_note.time,
            'Note': new_note.note,
            
            })
        

def search_entries():
    pass


def task(User):
    pass
    
def menu():
    print('What would you like to do?')
    for option in MENU_OPTIONS:
        print('> {}'.format(option))
    while True:
        try:
            choice = input('What would you like to do?: ')
            choice.upper()
            
            if choice not in MENU_CHOICES:
                raise ValueError
            
            if choice == 'A':
                add_entry()
            
            if choice == 'S':
                search_entries()
            
            if choice == 'Q':
                quit()
        
        except (ValueError, TypeError):
            print('please select a valid menu option')
            
        else:
            break
 

if  __name__=='__main__':
    if os.path.isfile("Work_log.csv") != True:
        with open("Work_log.csv", "a") as csvfile:
            fieldnames = ['Name', 'Task Name', 'Time Spent', 'Note']
            notewriter = csv.DictWriter(csvfile, fieldnames=fieldnames)
            notewriter.writeheader()
            
    print('Welcome to my Worklog')
    menu()
    
    