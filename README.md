# Hard Coder Challenge

10 days script writing challenge in Python.

# Day 1 - Palindromes

Script should check if console input console input is a palindrome and look for all anagrams. 
Modules used:
  - re - filtering non-letters from input
  - requests - scrapping HTML code from online scrabble engine
  - BeautifulSoup - checking for anagrams in HTML code

# Day 2 - Weather and name day

Simple calendar card, returning weather, date-time and name day info:
Modules used:
  - pytz - for timezone info
  - requests - conneting to weather API, scrapping HTML code from name day info site
  - BeautifulSoup - checking for names in HTML code
  
 # Day 3 - Email sender
 
Script for sending emails for every person in base (excel chart). After logging on gmail account in terminal, emails will be automaticly sent to all persons in database. Email contains of short message and image, named with person name and surname.
Modules used:
  - smtplib, email, ssl - email sending
  - pandas - handling .xlsx file
  - getpass - password input

# Day 4 - BMI app

Script for calculating BMI based on API and creating plan of activities for a week, based on calculated BMI.
Modules used: requests - conneting to weather API
  -  requests - conneting to BMI API
  -  random - creating random activieties list

# Day 5 - Image resizer
Script halves every picture in /img folder by half and saves them into /smaller folder. Script calculates how much memory is saved and prints it both in % and bytes.
Modules used:
  - os - iterating througth files
  - pillow - image operations
  - io - calculating memory difference

# Day 6 - Films library

Script connecting with IMDB API, gathering info about films basing on IMDB searching engine.
Modules used:
  - requests - conntecting to IMDB API


# Day 7 - Password generator

Script for generating strong passwords, each containg one lower letter, upper letter, digit and special symbol. After generation, password gets copied to clipboard.
Modules used:
  - random - generating password
  - string - ready to use char arrays (eg. string.lowercase)
  - pyperclip - auto-copying string

# Day 8 - Library

Script connecting with online library API, retriving informations about books. Script is connected with local SQLite3 database, storing informations about which books are borrowed, and who borrowed them.
Modules used:
  - requests - connecting with library API
  - sqlalchemy - connecting script with database
