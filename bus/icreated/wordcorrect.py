import enchant
import sys
import os
from django.core.files import File
class speelcorrect:
    
    @staticmethod
    def correct(word_to_check):
       
        f= open('./bus/icreated/towname.txt','r')
       
        input_movie_name = word_to_check
        movies_dict = enchant.PyPWL("./bus/icreated/towname.txt")

        word_exists = movies_dict.check(input_movie_name)
        print("word exists: ", word_exists)
        suggestions=0
        if not word_exists:
            suggestions = movies_dict.suggest(input_movie_name)
            print ("input:", input_movie_name)
            print("suggestions:", suggestions[0])
            
            return suggestions[0]






    
