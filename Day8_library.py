import requests
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
import os
import sys

basedir = os.path.abspath(os.path.dirname(__file__))
engine = create_engine('sqlite:///'  + os.path.join(basedir, 'books.db'))
Base = declarative_base()
Session = sessionmaker(bind=engine)
session = Session()


class Books(Base):
    __tablename__ = 'books'
    id = Column(Integer, primary_key=True)
    book_id = Column(Integer)
    name = Column(String)
    user_name = Column(String)
    
    def __repr__(self):
        return "<Books({}, {})>".format(self.book_id, self.name)
    
    
def check_for_books():
    author = input('Author name (Name Surname): ')
    author = author.split(" ")
    try:
        url = 'http://data.bn.org.pl/api/bibs.json?author={}%20{}'.format(author[0], author[1])
        response = requests.get(url)
        lib = response.json()
        for i in range(len(lib["bibs"])):
            print("Id: {}".format(lib["bibs"][i]['id']))
            print("Title: {}".format(lib["bibs"][i]['title']))
            print("Year: {}".format(lib["bibs"][i]['publicationYear']))
            print("Author: {} ".format(lib["bibs"][i]['author']))
            print("")
    except Exception as ex:
        print(ex)

        
def borrow(user_name):
    id = int(input("Enter book id: "))
    try:
        url = 'http://data.bn.org.pl/api/bibs.json?id={}'.format(id)
        response = requests.get(url)
        title = response.json()["bibs"][0]["title"]
        if session.query(Books).filter_by(book_id=id).first() == None:
            book = Books(book_id = id, name = title, user_name=user_name)
            session.add(book)
            session.commit()
        else:  
            print("Book already borrowed!")
    except Exception as ex:
        print(ex)

        
def return_book(user_name):
    id = int(input("Enter book id: "))
    if session.query(Books).filter_by(book_id=id, user_name=user_name).first() != None:
        book = Books(book_id = id)
        session.query(Books).filter(Books.book_id == id).\
            delete(synchronize_session="fetch")
        session.commit()
    else:  
        print("Book in not borrowed by you!")
        
            
def your_books(user_name):
    for i in session.query(Books).filter_by(user_name=user_name).all():
        print("{}, {}".format(i.book_id, i.name))
            
            
def main():
    user_name = input("Your username: ")
    while True:
        print("1 - Check for books from author\n2 - Borrow a book\n3 - Return a book\n4 - Check borrowed books\n5 - Quit")
        while True:    
            try:
                choice = int(input("Choose an option: "))
                break
            except:
                pass
        os.system('CLS')
        if choice == 1:
            check_for_books()
        elif choice == 2:
            borrow(user_name)
        elif choice == 3:
            return_book(user_name)
        elif choice == 4:
            your_books(user_name)
        elif choice == 5:  
            print("Thanks for using!")     
            break
        else:
            pass
    
main()
