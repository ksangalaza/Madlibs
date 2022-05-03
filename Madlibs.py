import words
import csv
import random
import pymongo
from pymongo import MongoClient
import pprint
import logging

# logging.basicConfig(filename= 'Madlibs.log', encoding='utf-8', level=logging.DEBUG, format='%(asctime)s %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p::')








def pick_theme():
  
    client = MongoClient()
    db_Madlibs = client.Madlibs
    madlibs_data = db_Madlibs.madlibs_data


    loop = 1
    while (loop < 2):
        while True:
            
            print("Welcome to an interactive MADLIBS!")
            your_name = input("Please tell us your name: ")
            print("Please choose a theme: ")
            print("\t 1) Thank you Speech")
            print("\t 2) Study Solution")
            print("\t 3) Behind the Scenes of a Movie")
            print("\t 4) A Christmas Carol")
            theme = input(">>>")
            
            # logging.debug("User inputted theme ", theme)

            if not theme == '1' and not theme == '2' and not theme == '3' and not theme == '4':
                raise ValueError('Theme is not on the list')
            else:
                break

        while True:

            print("\t 1) Let the Computer Generate Words")
            print("\t 2) Choose My Own Words")
            mode = input(">>>")

            # logging.debug("User inputted mode ", mode)

            if not mode == '1' and not mode == '2':
                raise ValueError('Please choose one of the modes 1 or 2: ')
            else:
                break

        if theme == '2' and mode == '2':
            Noun = input('Enter a noun: ')
            ProperNoun = input('Enter a proper noun: ')
            Verb = input('Enter a verb: ')
            Adjective = input('Enter an adjective: ')
            Adverb = input('Enter an Adverb: ')
            ml2 = words.Study(Noun, ProperNoun, Verb, Adjective, Adverb)

            (ml2.write_into_archives())
            print(ml2.studystory())
            
           

        elif theme == '3' and mode == '2':
            Noun = input('Enter a noun: ')
            Propernoun = input('Enter a proper noun:')
            Verb = input('Enter a verb: ')
            Adjective = input('Enter an adjective: ')
            Adverb = input('Enter an Adverb: ')
            ml3 = words.Movie(Noun, Propernoun, Verb, Adjective, Adverb)
            print(ml3.moviestory())
            (ml3.write_into_archives())
            # logging.info("Successfuly added objects to database.")

        elif theme == '4' and mode == '2':
            Noun = input('Enter a noun: ')
            ProperNoun = input('Enter a proper noun: ')
            Verb = input('Enter a verb: ')
            Adjective = input('Enter an adjective: ')
            Adverb = input('Enter an Adverb: ')
            ml4 = words.Christmas(Noun, ProperNoun, Verb, Adjective, Adverb)
            print(ml4.christmasstory())
            (ml4.write_into_archives())
            # logging.info("Successfuly added objects to database.")

        elif theme == '1' and mode == '2':
            ProperNoun = input('Enter a proper noun: ')
            Noun = input('Enter a noun: ')
            Verb = input('Enter a verb: ')
            Adjective = input('Enter an adjective: ')
            Adverb = input('Enter an Adverb: ')
            ml = words.ThankYou(Noun, ProperNoun, Verb, Adjective, Adverb)
            print(ml.thankyoustory())
            (ml.write_into_archives())
            # logging.info("Successfuly added objects to database.")

        elif mode == '1' and theme == '2':
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
            random.shuffle(col0)
            random.shuffle(col1)
            random.shuffle(col2)
            random.shuffle(col3)
            random.shuffle(col4)
            ml2 = words.Study(col0[0], col1[1], col2[2], col3[3], col4[4])
                
            print(ml2.studystory())
            (ml2.write_into_archives())
            # logging.info("Successfuly added objects to database.")

                    
        
        elif mode == '1' and theme == '3':
            
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
            random.shuffle(col0)
            random.shuffle(col2)
            random.shuffle(col3)
            random.shuffle(col4)
            ml3 = words.Movie(col1[0],col0[1], col2[2], col3[3], col4[4])
            print(ml3.moviestory())
            (ml3.write_into_archives())
            # logging.info("Successfuly added objects to database.")
                    

        elif mode == '1' and theme == '4':
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
            random.shuffle(col0)
            random.shuffle(col1)
            random.shuffle(col2)
            random.shuffle(col3)
            random.shuffle(col4)
            ml4 = words.Christmas(col1[0], col0[1], col2[2], col3[3], col4[4])
            print(ml4.christmasstory())
            (ml4.write_into_archives())
            # logging.info("Successfuly added objects to database.")

        elif mode == '1' and theme == '1':
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
            random.shuffle(col0)
            random.shuffle(col1)
            random.shuffle(col2)
            random.shuffle(col3)
            random.shuffle(col4)
            ml = words.ThankYou(col1[0], col0[1], col2[2], col3[3], col4[4])
            
            print(ml.thankyoustory())
            (ml.write_into_archives())
            # logging.info("Successfuly added objects to database.")
                

               
pick_theme()



