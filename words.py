import random
import pymongo
from pymongo import MongoClient

class Words:
    isInEnglish = True

client = MongoClient()
db_Madlibs = client.Madlibs
madlibs_data = db_Madlibs.madlibs_data


def write_into_archives(noun, propernoun, verb, adjective, adverb):
    
    madlibs_data.insert_one(
        {
        "Noun": noun,
        "Proper Noun": propernoun,
        "Verb": verb,
        "Adjective": adjective,
        "Adverb": adverb
     })
    return "Successfully added to database"
    

def __init__(self, noun, propernoun, verb, adjective, adverb ):
    self.noun = noun
    self.propernoun = propernoun
    self.verb = verb
    self.adjective = adjective
    self.adverb = adverb


class Study(Words):
    def __init__(self, noun, propernoun, verb, adjective, adverb ):
        self.noun = noun
        self.propernoun = propernoun
        self.verb = verb
        self.adjective = adjective
        self.adverb = adverb
    def studystory(self):
        return "Hi there " + self.propernoun +". You're probably reading this because you cant seem to find the best study method. Here at StudyPLUS we " + self.verb + "to cure conditions such as procrastination, sophopbia, laziness, etc. The list goes on! Our inpatient " + self.adjective + " rehab will turn you from a ZERO to a " + self.adjective + " HERO. For the low price of 2999.99, we will " + self.adverb + " get you back to tip top " + self.noun + ". Don't hesitate! " + self.adverb + " call us now!"
        
    def write_into_archives(self):
    
        madlibs_data.insert_one(
            {
            "Noun": self.noun,
            "Proper Noun": self.propernoun,
            "Verb": self.verb,
            "Adjective": self.adjective,
            "Adverb": self.adverb
        })
        return "Successfully added to database"

class Movie(Words):
    def __init__(self, noun, propernoun, verb, adjective, adverb ):
        self.noun = noun
        self.propernoun = propernoun
        self.verb = verb
        self.adjective = adjective
        self.adverb = adverb
    def moviestory(self):
        return "Back in the early 90's I was working on the set of a movie called " + self.noun + ". This was before animations did all of our " + self.adjective + " scenes. We had to " + self.verb + " for 12 hours a day! One day I went to " + self.verb + " and I " + self.adverb + " slipped on a random marble someone had left on set. I was so " + self.adjective + " and so after the movie was done, I was done with the acting world."
    
    def write_into_archives(self):
    
        madlibs_data.insert_one(
            {
            "Noun": self.noun,
            "Proper Noun": self.propernoun,
            "Verb": self.verb,
            "Adjective": self.adjective,
            "Adverb": self.adverb
        })
        return "Successfully added to database"

class ThankYou(Words):
    def __init__(self, noun, propernoun, verb, adjective, adverb ):
        self.noun = noun
        self.propernoun = propernoun
        self.verb = verb
        self.adjective = adjective
        self.adverb = adverb
    def thankyoustory(self):
        return "Wow! I can't believe I am here today. I am so honored to have had the opportunity to " + self.verb + " my experiences with you all. First I would like to thank " + self.propernoun + " for all of the sleepless nights spent reciting my presentation. My " + self.noun + " is my number one supporter, so I couldnt accept this honor without recognizing my " + self.noun + ". Lastly, I " + self.adverb + " appreciate this recognition. This was a " + self.adjective + " journey."

    def write_into_archives(self):
    
        madlibs_data.insert_one(
            {
            "Noun": self.noun,
            "Proper Noun": self.propernoun,
            "Verb": self.verb,
            "Adjective": self.adjective,
            "Adverb": self.adverb
        })
        return "Successfully added to database"

class Christmas(Words):
    def __init__(self, noun, propernoun, verb, adjective, adverb ):
        self.noun = noun
        self.propernoun = propernoun
        self.verb = verb
        self.adjective = adjective
        self.adverb = adverb
    def christmasstory(self):
        return "Dashing through the " + self.noun + " in a " + self.adjective + " open sleigh. O'er the fields we go, " + self.adverb + " all the way. Bells on bobtails " + self.verb + ", making spirits bright. What fun it is to ride and sing, a sleighing " + self.propernoun + " tonight, oh! Jingle " + self.noun + " Jingle " + self.noun + " Jingle all the way. Oh what fun it is to ride, in a " + self.adjective +  " open sleigh!" 
    
    def write_into_archives(self):
    
        madlibs_data.insert_one(
            {
            "Noun": self.noun,
            "Proper Noun": self.propernoun,
            "Verb": self.verb,
            "Adjective": self.adjective,
            "Adverb": self.adverb
        })
        return "Successfully added to database"