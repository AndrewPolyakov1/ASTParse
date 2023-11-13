import os.path
import re
import my_ast
import ast

# '''
# Make sure to put 
#     #F
# as a comment at the end of lines that contain a function call that don't also contain an assignment (=).
# '''

# python_file = 'ex_class.py'

# basic_conversion_rules = {
#     "for": "FOR",
#     "=": "TO", 
#     "if": "IF", 
#     "==": "EQUALS", 
#     "while": "WHILE", 
#     "until": "UNTIL",
#     "import": "IMPORT",
#     "class": "DEFINE CLASS", 
#     "def": "DEFINE FUNCTION", 
#     "else:": "ELSE:",
#     "elif": "ELSEIF", 
#     "except:": "EXCEPT:", 
#     "try:": "TRY:", 
#     "pass": "PASS", 
#     "in": "IN"}

# prefix_conversion_rules = {
#     "=": "SET ", 
#     "#F": "CALL "}

# advanced_conversion_rules = {
#     "print": "OUTPUT", 
#     "return": "RETURN", 
#     "input": "INPUT"}

# class__conversion_rules = {
#     "class" : "DEFINE CLASS",
#     "__init__" : "INITIALIZE",
#     "def" : "DEFINE METHOD"
# }

code = """
class Person:
   def __init__(self, name, age):
       self.name = name
       self.age = age

   def introduce(self):
       print("My name is {self.name} and I am {self.age} years old.")

def ask_for_name_and_age():
   name = input("Enter your name: ")
   age = input("Enter your age: ")
   return name, age

def main():
   name, age = ask_for_name_and_age()
   person = Person(name, age)
   person.introduce()

def summ(a, b):
    if a >= b:
        return a + b

if __name__ == "__main__":
   main()"""

tree = my_ast.parse(code)

print(my_ast.dump(tree))

unparsed_code = my_ast.unparse(tree)

print(unparsed_code)