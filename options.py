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




class Options:
    
    def __init__(self):
        self.list = []
        self.current = []
        self.used = []
        self.quotes_list = []
        self.pick = ''
        
    def print_list(self):
        
        # if user wants to print the list of all the availiable essay prompts 
        # or print the essay prompts he has already done he can press
        # 1 for essay prompt and 2 for finished essay prompts 3 for dog attack
        
        print("Please enter [0] for exiting Program\nPlease enter [1] for unfinished essay prompts\nPlease enter [2] for finished essay prompts\nPlease enter [3] for a puppy bonbardment")
        print("__________________________________________________________________________________________________________________________")
        print("__________________________________________________________________________________________________________________________")
        
        answer = int(input(": "))
        #just for now answer will be 3 to quickly error check
        
        if answer == 0:
            exit()
        if answer == 1:
            
            for i in self.list:
                print(i)
        if answer == 2:
            
            for i in    self.used:
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
                self.list_num = []
                self.list30 = []
                self.line = []
                for char in quote:
                    self.list_num.append(char)
                #print(self.list_num)
                
                
                #3 lines instead of 82 lines
                
                for i in range(0, len(quote), 60):
                    print(quote[i:i+60])
                #time.sleep(3)
                print('\t\t' +' - ' +author + '  - ' +location)

            print("Enter a number for what you want\n[0] - exit, if your wise\n[1] - continue, if you are not")
            choice2 = int(input("Enter Here: "))
            if choice2 == 0:
                exit()
            if choice2 == 1:
                #C:\\Users\\Christian Alameda\\Documents\\funWithCode\\vs code\\PickingRandomTopic\\
               # mixer.init()
                #mixer.music.load(r"moonlight.mp3")
                #mixer.music.play()
                
                while(playsound.playsound('moonlight.mp3')):     
                
                    #"C:\Users\Christian Alameda\Documents\funWithCode\vs code\PickingRandomTopic\puppyFolder\puppy2.png"
                    #playsound('moonlight.mp3', False)# false will simply not play the audio
                    #winsound.PlaySound("moonlight", winsound.SND_ASYNC | winsound.SND_ALIAS )
                    
                    #C:\\Users\\Christian Alameda\\Documents\\funWithCode\\vs code\\PickingRandomTopic\\
                    parent_dir = (r"puppyFolder")
                    for subdir, dirs, files in os.walk(parent_dir):
                        for file in files:
                            
                            # show needs an "Image.open(file)" in front of it
                            
                            Image.open("puppyFolder\\"+file).show() # file in this contxt is a string
                
        else:
            print('You have entered a wrong number, please try again')
            self.print_list()  
            
    def choice(self, q, old, q1):
        choice = int(input("Enter a number for what you want\n[0] - exit\n[1] - printed List\n[2] - Choice Selector\nEnter Here:"))
        
        if choice == 0:
            exit()
        elif choice == 1:
            self.print_list()
        elif choice == 2:
            self.spectacular(q, old, q1)
        else:
            print('You have chosen a wrong choice selection; Correct selections: [0,1,2]')
            self.choice(q,old,q1)
                
              
            
              
    def pick_random(self):
        
        # picks a random item in our list
        
        pick = random.choice(self.list) 
        return pick
    
    #getting data from q and using lines
    
    def create_inventory(self, q):
        with open("q.csv","r") as csvfile:
            csvreader = csv.reader(csvfile)
            for line in csvreader:
                self.list.append(line)
    
    #making it for removed to get into old
    
    def create_inventory1(self,old):
        with open("old.csv", "r") as csvfile:
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
                
    

    
    
    
    
                

    
                
                
    def spectacular(self, q, old, q1):
        
        # first part will  do the picking
        
        self.pick = self.pick_random()
        
        self.beep1()
        
        #in seconds
        
        time.sleep(3)
        
        
        print("Your choice for today is: ",self.pick,", Woooooooooooooooooo")
        
        engine = pyttsx3.init()
        engine.say("Your choice for today is: ")
        engine.say(self.pick)
        engine.say("Woooooooooooooooooo")
        engine.runAndWait()
        
        
        self.beep2()
        '''
        ===================================================================
        '''
        
        #second part will do the removing of the picked item
        # and redoing the q.csv as to remove that item from it
        # only able to hold it for when the program is running
        
        self.current.append(self.pick)
        
        for i in self.list:
            if i in self.used:# changed to used
                self.list.remove(i)
                
            elif i == self.pick:
                self.list.remove(self.pick)
                
        '''
        =======================================================================
        '''
        #third part with be adding the removed prompt into a new place
        #to live
        
        current = self.current
        
        # appending current items in list to the function in order to 
        # keep track of which essays have been finished
        
        with open(old,"a") as fd: 
            for i in current:
                for j in i:
                    fd.write(j + '\n')
        
        # we want to recreate the file
        # as to not have it in our new list
        
        with open(q, 'r') as inp, open(q1, 'w') as out:
            writer = csv.writer(out)
            for row in csv.reader(inp):
                if row not in self.used: #changed to used
                    writer.writerow(row)
            
        '''
        =======================================================================
        '''

        
        
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