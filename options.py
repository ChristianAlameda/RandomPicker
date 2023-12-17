import csv
import random
import winsound
import pyttsx3
import time
from PIL import Image
from playsound import playsound
from pygame import mixer
import os
from entry import Entry
import playsound
import threading

class Options:
    
    def __init__(self):
        self.original = []
        self.current = []
        self.used = []
        self.quotes_list = []
        self.pick = ''
    
    #getting data from original.csv and using lines
    def create_inventory(self, original):
        with open(original,"r") as csvfile:
            csvreader = csv.reader(csvfile)
            for line in csvreader:
                self.original.append(line)
    
    #making it for removed to get into old
    def create_inventory1(self,old):
        with open(old, "r") as csvfile:
            csvreader = csv.reader(csvfile)
            for line in csvreader:
                self.used.append(line)
    
    # reading in data from "quotes.csv" in order to use them
    def create_inventory2(self,quotes):
        with open(quotes, "r") as csvfile:
            csvreader = csv.reader(csvfile)
            for line in csvreader:
                entry = Entry()
                entry.set_quotes(line[0]) 
                entry.set_author(line[1])
                entry.set_location(line[2]) 
                self.quotes_list.append(entry)
                
    def print_list(self):
        """_summary_: 4 options
            1: exit
            2: print finished essay prompts
            3: print unfinished essay prompts
            4: puppy bombardment
        """
        # if user wants to print the list of all the availiable essay prompts 
        # or print the essay prompts he has already done he can press
        # 1 for essay prompt and 2 for finished essay prompts 3 for dog attack
        
        print("Please enter [0] for exiting Program\nPlease enter [1] for unfinished essay prompts\nPlease enter [2] for finished essay prompts\nPlease enter [3] for a puppy bonbardment")
        answer = int(input("Enter Here: "))

        if answer == 0: exit()
        if answer == 1:
            for i in self.original:
                print(i)
        if answer == 2:
            for i in self.used:
                print(i)
        if answer == 3:
            ''' Quotes '''
            ''' We have to have quotes'''
            
            # calling get_quotes, get_author, and get_location from our entry
            # initalizing them for use
            # they are lists of strings
            
            for i in self.quotes_list:
                
                quote = i.get_quotes()
                author = i.get_author()
                location = i.get_location()
            
                #We need a tripple for loop so that quotes, authors, and locations are all matched up
                
                # initializing the number of charachters in a quote
                
                # if it is greater than 30 I want to add a newline after 30 charachters
                # divide the quote into segments of 30 or less charachters when coming to the end
                self.original_num = []
                self.original30 = []
                self.line = []
                for char in quote:
                    self.original_num.append(char)
                    
                for i in range(0, len(quote), 60):
                    print(quote[i:i+60])
                #time.sleep(3)
                print('\t\t' +' - ' +author + '  - ' +location)

            print("Enter a number for what you want\n[0] - exit, if your wise\n[1] - continue, if you are not")
            choice2 = int(input("Enter Here: "))
            if choice2 == 0:
                exit()
            if choice2 == 1:
                parent_dir = r"puppyFolder"
                mp3_file = 'moonlight.mp3'
                image_files = [os.path.join(parent_dir, file) for file in os.listdir(parent_dir) if file.lower().endswith(('.png', '.jpg', '.jpeg', '.gif'))]

                music_thread = threading.Thread(target=self.play_music, args=(mp3_file,))
                images_thread = threading.Thread(target=self.display_images, args=(image_files,))

                music_thread.start()
                images_thread.start()

                music_thread.join()
                images_thread.join()
                
        else:
            print('You have entered a wrong number, please try again')
            self.print_list()  
    
    def play_music(self, mp3_file):
        playsound.playsound(mp3_file)

    def display_images(self, image_files):
        for image_file in image_files:
            Image.open(image_file).show()
            
    def choice(self, original, old, notUsed):
        """_summary_: Give the user 
            option 1: to print_which will give 3 options to show old or unused topics or to have a puppy show
            option 2: make the choice for a topic
            option 3: user made a mistake

        Args:
            orignal (csv file): orignal topics
            old (csv file): old topics that have been selected already
            transfer (csv file): a transfer file between original to old, meant to not tarnish orignal
        """
        choice = int(input("Enter a number for what you want\n[0] - exit\n[1] - printed List\n[2] - Choice Selector\nEnter Here:"))
        
        if choice == 0:
            exit()
        elif choice == 1:
            self.print_list()
        elif choice == 2:
            self.spectacular(original, old, notUsed)
        else:
            print('You have chosen a wrong choice selection; Correct selections: [0,1,2]')
            self.choice(original,old,notUsed)
                    
    # picks a random item in our list
    def pick_random(self):
        """_summary_: grabs a random item from the csv that has not been used yet

        Returns:
            str: just the unused item that was selected
        """
        
        pick = random.choice(self.original) 
        return pick
                
    def spectacular(self, original, old, notUsed):
        """_summary_: 3 parts to this function: 
            1: make a choice from random and present the user what choice has been made
            2: from the choice we want to remove the selected choice from orginal list
            3: we add the item chosen to old.csv and and we recreate notUsed.csv to update it

        Args:
            orignal (csv): original csv with the 100 items
            old (csv): used items 
            notUsed (csv): transfer csv file
        """
        '''
        1
        ===================================================================
        '''
        # first part will  do the picking
        self.pick = self.pick_random()
        
        self.beep1()
        time.sleep(3) # in seconds
        
        print("Your choice for today is: ",self.pick,", Woooooooooooooooooo")
        
        engine = pyttsx3.init()
        engine.say("Your choice for today is: ")
        engine.say(self.pick)
        engine.say("Woooooooooooooooooo")
        engine.runAndWait()
        
        self.beep2()
        '''
        2
        ===================================================================
        '''
        
        # second part will do the removing of the picked item
        # and redoing the original.csv as to remove that item from it
        # only able to hold it for when the program is running
        
        self.current.append(self.pick)
        
        for i in self.original:
            if i in self.used:# changed to used
                self.original.remove(i)
                
            elif i == self.pick:
                self.original.remove(self.pick)
                
        '''
        3
        =======================================================================
        '''
        # third part with be adding the removed prompt into a new place
        # to live
        
        current = self.current
        
        # appending current items in list to the function in order to 
        # keep track of which essays have been finished
        
        with open(old,"a") as file: 
            for i in current:
                for j in i:
                    file.write(j + '\n')
        
        # we want to recreate the file
        # as to not have it in our new list
        
        with open(original, 'r') as inp, open(notUsed, 'w') as out:
            writer = csv.writer(out)
            for row in csv.reader(inp):
                if row not in self.used: #changed to used
                    writer.writerow(row)

    def beep1(self):
        
        # gets to 1000
        
        x = 500
        i = 0
        
        while i < 5: 
            
            # x will change, y will remain constant
            
            winsound.Beep(x,20) 

            x = x + 100
            i = i + 1
        
        
    def beep2(self):
        
        # starts at 1000 goes to 500
        
        y = 1000 
        j = 0
        while j < 5: 
            
            # x will change, y will remain constant
            
            winsound.Beep(y,20) 

            y = y - 100
            j=j+1