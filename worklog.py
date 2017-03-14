# add entry or lookup Entry
# provide task name, number of minutes spent, additional notes
# write to a csv file  
# find by date, time spend, exact search, by pattern 
import csv
import os.path
import datetime
import re

MENU_OPTIONS = ('(A)dd Entry', '(S)earch Entries', '(Q)uit')
MENU_CHOICES = ('A', 'S', 'Q')
VALIDATOR = ('Y', 'N') 
entry_counter = 0
SEARCH_OPTIONS = ('by (D)ate', 'by (T)ime Spent', 'by (E)xact Search', 'by (P)attern')
SEARCH_CHOICES = ('D', 'T', 'E', 'P')

class Entry:
    def __init__(self, name, task_name, time, note, date):
        self.name = name
        self.task_name = task_name
        self.time = time
        self.note = note
        self.date = date

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
        
    while True:
        try:
            date_check = input('Was this work done Today? (Y/N)?:')
            date_check.upper()
            if date_check not in VALIDATOR:
                raise ValueError
            
        except (TypeError, ValueError):
            print('please select a valid date')
        
        else:
            break
    
    if date_check == 'Y':
        date = datetime.datetime.today().strftime("%Y/%m/%d")
                
    if date_check == 'N':
        while True:
            try:
                year = int(input('What year was this work performed?: '))
                year_check = input("is '{}' correct?: (Y/N): ".format(year))
                if year_check not in VALIDATOR:
                    raise ValueError
            except (ValueError, TypeError):
                print('please type in the correct year')
                
            else:
                break
            
        while True:
            try:
                month = int(input('What month was this work performed? (as number): '))
                month_check = input("is '{}' the correct month?: (Y/N) ".format(month))
                if month_check not in VALIDATOR:
                    raise ValueError
            except (ValueError, TypeError):
                print('please input the correct Month')
                
            else:
                break
        
        while True:
            try:
                day = int(input('What day was this work performed? (as number): '))
                day_check = input("is '{}' the correct day?: (Y/N) ".format(day))
                if day_check not in VALIDATOR:
                    raise ValueError
            except (ValueError, TypeError):
                print('please input the correct Day')
                
            else:
                break
                    
        str_date= '{}-{}-{}'.format(year, month, day)
        my_date = datetime.date(*[int(i) for i in str_date.split('-')])
        date = my_date.strftime('%Y/%m/%d')
    
    new_note = Entry(name, task_name, time, note, date)
    
    with open("Work_log.csv", "a") as csvfile:
        fieldnames = ['Name', 'Task Name', 'Time Spent', 'Note', 'Date']
        notewriter = csv.DictWriter(csvfile, fieldnames=fieldnames)
        notewriter.writerow({
            'Name': new_note.name,
            'Task Name': new_note.task_name,
            'Time Spent': new_note.time,
            'Note': new_note.note,
            'Date': new_note.date,
            
            })
        
    print('Note added succesfully!')
    menu()

def search_entries():
    print('How would you like to search?')
    for option in SEARCH_OPTIONS:
        print('> {}'.format(option))
    while True:
        try:
            choice = input('Please select search type: ')
            choice.upper()
            if choice not in SEARCH_CHOICES:
                raise ValueError
        except (ValueError, TypeError):
            print('please select a valid option')
            
        else:
            break
             
    if choice == 'D':
        while True:
            try:
                print('What date are you searching for?')
                date = input('type in as YYYY/MM/DD: ')
                date_list = date.split('/')
                year= int(date_list[0])
                month = int(date_list[1])
                day = int(date_list[2])
                date_check = datetime.datetime(year=year, month=month, day=day)
                
            
            except (ValueError, TypeError):
                print('Please select a valid date in form YYYY/MM/DD')
                
            else:
                break
        
        with open('Work_log.csv', 'r') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                if row['Date'] == date:
                    print(row)
                
    if choice == 'T':
        while True:
            try:
                print('How long was the time spent on the log your looking for?')
                time = int(input('Type a time in minutes: '))
                
            except (TypeError, ValueError):
                print('please select a valid time in minutes')
            
            else:
                break
            
        with open('Work_log.csv', 'r') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                if row['Time Spent'] == time:
                    print(row)
                    
    if choice == 'E':
        while True:
            try:
                print('Type in a search string')
                search = input('what would you like to search?')
                validator = input('is {} what you would like to search for? (Y/N): '.format(search))
                if validator not in VALIDATOR:
                    raise ValueError
                
            except ValueError:
                print('What would you like to search for?')
            
            else:
                break
            
        with open('Work_log.csv', 'r') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                if search in row:
                    print(row)
                    
    if choice == 'P':
        file = open('Work_log.csv')
        data = file.read()
        file.close()
        
        while True:
            try:
                print('Please input a regular expression to search for')
                reg_ex = input('What is the patter your looking for?: ')   
                with open('Work_log.csv', 'r') as csvfile:
                    reader = csv.DictReader(csvfile)
                    for row in reader:
                        search = re.findall(reg_ex, data)
                        if search:
                            print(row)
                       
                
            except(ValueError, re.error):
                print('please input a valid Regular Expression')
            
            else:
                break
       
       
                        
    menu()


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
            fieldnames = ['Name', 'Task Name', 'Time Spent', 'Note', 'Date']
            notewriter = csv.DictWriter(csvfile, fieldnames=fieldnames)
            notewriter.writeheader()
            
    print('Welcome to my Worklog')
    menu()
    
    