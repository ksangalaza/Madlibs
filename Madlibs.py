import words
import csv
import random
import pymongo
from pymongo import MongoClient
import pprint
import logging








#MAIN CODE
def pick_theme():

#CONNECTING TO MONGODB  
    client = MongoClient()
    db_Madlibs = client.Madlibs
    madlibs_data = db_Madlibs.madlibs_data


    loop = 1
    while (loop < 2):
        while True:

#USER GIVEN OPTION TO CHOOSE A THEME OR DELETE THE ARCHIVES            
            print("Welcome to an interactive MADLIBS!")
            your_name = input("Please tell us your name: ")
            print("Please choose a theme: ")
            print("\t 1) Thank you Speech")
            print("\t 2) Study Solution")
            print("\t 3) Behind the Scenes of a Movie")
            print("\t 4) A Christmas Carol")
            print("\t 5) DELETE ARCHIVES")
            theme = input(">>>")
            
        
        
#ERROR IF USER DOES NOT SELECT AN OPTION FROM THE LIST
            if not theme == '1' and not theme == '2' and not theme == '3' and not theme == '4' and not theme == '5':
                raise ValueError('Theme is not on the list')
            else:
                break
            
        while True:
            
#USER GIVEN THE OPTION TO CHOOSE A GAME MODE 
            print("\t 1) Let the Computer Generate Words")
            print("\t 2) Choose My Own Words")
            print("\t 3) SERIOUSLY DELETE ARCHIVES")
            mode = input(">>>")


            if not mode == '1' and not mode == '2' and not mode == '3':
                raise ValueError('Please choose one of the modes 1, 2, or 3: ')
            else:
                break
#DELETE ALL OF THE ARCHIVES
        if theme == '5' and mode == '3':
                madlibs_data.delete_many({})
                break

#INPUTS FOR A STUDY SOLUTION AND USER INPUT VALUES
        elif theme == '2' and mode == '2':
            Noun = input('Enter a noun: ')
            ProperNoun = input('Enter a proper noun: ')
            Verb = input('Enter a verb: ')
            Adjective = input('Enter an adjective: ')
            Adverb = input('Enter an Adverb: ')
            ml2 = words.Study(Noun, ProperNoun, Verb, Adjective, Adverb)

            (ml2.write_into_archives())
            print(ml2.studystory())
            
           
#INPUTS FOR A BEHIND THE SCENES AND USER INPUTS
        elif theme == '3' and mode == '2':
            Noun = input('Enter a noun: ')
            Propernoun = input('Enter a proper noun:')
            Verb = input('Enter a verb: ')
            Adjective = input('Enter an adjective: ')
            Adverb = input('Enter an Adverb: ')
            ml3 = words.Movie(Noun, Propernoun, Verb, Adjective, Adverb)
            print(ml3.moviestory())
#CONNECT MY CLASS TO WRITE INTO ARCHIVES
            (ml3.write_into_archives())

#INPUTS FOR A CHRISTMAS CAROL AND USER INPUTS
        elif theme == '4' and mode == '2':
            Noun = input('Enter a noun: ')
            ProperNoun = input('Enter a proper noun: ')
            Verb = input('Enter a verb: ')
            Adjective = input('Enter an adjective: ')
            Adverb = input('Enter an Adverb: ')
            ml4 = words.Christmas(Noun, ProperNoun, Verb, Adjective, Adverb)
            print(ml4.christmasstory())
#CONNECT MY CLASS TO WRITE INTO ARCHIVES            
            (ml4.write_into_archives())

#INPUTS FOR THANK YOU SPEECH AND USER INPUTS
        elif theme == '1' and mode == '2':
            ProperNoun = input('Enter a proper noun: ')
            Noun = input('Enter a noun: ')
            Verb = input('Enter a verb: ')
            Adjective = input('Enter an adjective: ')
            Adverb = input('Enter an Adverb: ')
            ml = words.ThankYou(Noun, ProperNoun, Verb, Adjective, Adverb)
            print(ml.thankyoustory())
#CONNECT MY CLASS TO WRITE INTO ARCHIVES
            (ml.write_into_archives())

#INPUTS FOR STUDY SOLUTION AND COMPUTER GENERATED INPUTS
        elif mode == '1' and theme == '2':
#READING FROM A CSV FILE
            with open("Madlibs_Random.csv", 'r') as computer:
                generator = csv.reader(computer)
                header = next(generator)
                col0 = []
                col1 = []
                col2 = []
                col3 = [] 
                col4 = []
                for row in generator:
                    Noun, ProperNoun, Verb, Adjective, Adverb = row
                    col0.append(Noun)
                    col1.append(ProperNoun)
                    col2.append(Verb)
                    col3.append(Adjective)
                    col4.append(Adverb)
#RANDOM SHUFFLE THE COLUMNS
            random.shuffle(col0)
            random.shuffle(col1)
            random.shuffle(col2)
            random.shuffle(col3)
            random.shuffle(col4)
            ml2 = words.Study(col0[0], col1[1], col2[2], col3[3], col4[4])
                
            print(ml2.studystory())
#CONNECT MY CLASS TO WRITE INTO ARCHIVES
            (ml2.write_into_archives())

                    
#INPUTS FOR BEHIND THE SCENES AND COMPUTER GENERATED INPUTS       
        elif mode == '1' and theme == '3':
#READING FROM A CSV FILE           
            with open("Madlibs_Random.csv", 'r') as computer:
                generator = csv.reader(computer)
                header = next(generator)
                col0 = []
                col1 = []
                col2 = []
                col3 = [] 
                col4 = []
                for row in generator:
                    Noun, ProperNoun, Verb, Adjective, Adverb = row
                    col0.append(ProperNoun)
                    col1.append(Noun)
                    col2.append(Verb)
                    col3.append(Adjective)
                    col4.append(Adverb)
#RANDOM SHUFFLE THE COLUMNS
            random.shuffle(col0)
            random.shuffle(col2)
            random.shuffle(col3)
            random.shuffle(col4)
            ml3 = words.Movie(col1[0],col0[1], col2[2], col3[3], col4[4])
            print(ml3.moviestory())
#CONNECT MY CLASS TO WRITE INTO ARCHIVES
            (ml3.write_into_archives())
                    

#INPUTS FOR CHRISTMAS CAROL AND COMPUTER GENERATED INPUTS
        elif mode == '1' and theme == '4':
#READING FROM A CSV FILE
            with open("Madlibs_Random.csv", 'r') as computer:
                generator = csv.reader(computer)
                header = next(generator)
                col0 = []
                col1 = []
                col2 = []
                col3 = [] 
                col4 = []
                for row in generator:
                    Noun, ProperNoun, Verb, Adjective, Adverb = row
                    col0.append(ProperNoun)
                    col1.append(Noun)
                    col2.append(Verb)
                    col3.append(Adjective)
                    col4.append(Adverb)
#RANDOM SHUFFLE THE COLUMNS
            random.shuffle(col0)
            random.shuffle(col1)
            random.shuffle(col2)
            random.shuffle(col3)
            random.shuffle(col4)
            ml4 = words.Christmas(col1[0], col0[1], col2[2], col3[3], col4[4])
            print(ml4.christmasstory())
#CONNECT MY CLASS TO WRITE INTO ARCHIVES
            (ml4.write_into_archives())

#INPUTS FOR THANK YOU SPEECH AND COMPUTER GENERATED INPUTS
        elif mode == '1' and theme == '1':
#READING FROM A CSV FILE
            with open("Madlibs_Random.csv", 'r') as computer:
                generator = csv.reader(computer)
                header = next(generator)
                col0 = []
                col1 = []
                col2 = []
                col3 = [] 
                col4 = []
                for row in generator:
                    Noun, ProperNoun, Verb, Adjective, Adverb = row
                    col0.append(ProperNoun)
                    col1.append(Noun)
                    col2.append(Verb)
                    col3.append(Adjective)
                    col4.append(Adverb)
#RANDOM SHUFFLE THE COLUMNS
            random.shuffle(col0)
            random.shuffle(col1)
            random.shuffle(col2)
            random.shuffle(col3)
            random.shuffle(col4)
            ml = words.ThankYou(col1[0], col0[1], col2[2], col3[3], col4[4])
            
            print(ml.thankyoustory())
#CONNECT MY CLASS TO WRITE INTO ARCHIVES
            (ml.write_into_archives())
                

               
pick_theme()



