import time
import re
import requests
from bs4 import BeautifulSoup

string = input("Your string: ")
print(string.lower())
regex = re.compile('[^a-zA-ZąćęłńóśźżĄĘŁŃÓŚŹŻ]')
string = regex.sub('', string)
if(string.lower() == string[::-1].lower()):
    print ("Input is a palindrome.")
else:
    print ("Input is not a palindrome.")
    
webpage = requests.get('https://poocoo.pl/scrabble-slowa-z-liter/{}'.format(string)).text
soup = BeautifulSoup(webpage, "html.parser")
mydiv = soup.find("div", {"class": "scrabble-result"})
if mydiv:
    print("\nList of anagrams and words created by deleting letters: ")
    for hit in mydiv.findAll(attrs={'rel' : 'nofollow'}):
        print(regex.sub('', hit.text))
else:
    print("\nInput don't have any anagrams.")