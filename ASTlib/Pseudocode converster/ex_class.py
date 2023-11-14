class Person:
   def __init__(self, name, age):
       self.name = name
       self.age = age

   def introduce(self):
       print(f"My name is {self.name} and I am {self.age} years old.")

def ask_for_name_and_age():
   name = input("Enter your name: ")
   age = input("Enter your age: ")
   return name, age

def main():
   name, age = ask_for_name_and_age()
   person = Person(name, age)
   person.introduce()

def wh(a):
   while a > 1:
      print(a)
      a -= 1

if __name__ == "__main__":
   main()