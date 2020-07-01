import json
from difflib import get_close_matches
from difflib import SequenceMatcher

data = json.load(open("dictionary.json"))

def find_the_word(word):
   word = word.lower()   
   if word in data:
      return data[word]
   elif len(get_close_matches(word,data.keys())) > 0:
       answer = input("Did you mean %s instead answer YES or NO:" % get_close_matches(word, data.keys())[0])
       if answer == "YES":
         return data[get_close_matches(word, data.keys())[0]]
       elif answer=="NO":
         return "This word does not exist"
       else:
         return "We don't understand what you mean"         
   else:
        print ("This word does not exist please check it again")


word = input("please give a word:")
output = (find_the_word(word))

if type(output)==list:
   for i in output:
      print (i)
      