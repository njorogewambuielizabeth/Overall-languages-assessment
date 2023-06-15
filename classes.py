# 1. **Ancestral Stories:** In many African cultures, the art of storytelling is passed
# down from generation to generation. Imagine you're creating an application that
# records these oral stories and translates them into different languages. The
# stories vary by length, moral lessons, and the age group they are intended for.
# Think about how you would model `Story`, `StoryTeller`, and `Translator`
# objects, and how inheritance might come into play if there are different types of
# stories or storytellers.

# create a parent class for the ancestral stories where other classes can inherit
# from ie story,storyteller and translater
# 
class Ancestral_stories:
    def __init__(self, title,moral_lessons , length, age_group):
        self.title = title
        self.moral_lessons = moral_lessons
        self.length = length
        self.age_group = age_group 
        
    def story(self):
        self.moral_lessons 
        
class Story:
    def __init__(self, name):
        self.name = name  
                       
class Story_teller:
    def __init__(self, name,story_title):
        self.name = name  
        self.story_title=story_title
        
    def tell_story(self):
        print(f"{self.name} is telling a story:")
        print(Story_teller.tell_story(self))
        
class Translator:
     def __init__(self, name,language):
        self.name = name  
        self.language=language
        
story = Story("Mzee Kobe") 
ancestral_story = Ancestral_stories("The cunning fox", "Helping others is important.", "Short", "Children")
storyteller = Story_teller("John", "The dark forest")
translator = Translator("Maria", "Spanish")


                   
# 2. **African Cuisine:** You're creating a recipe app specifically for African cuisine.
# The app needs to handle recipes from different African countries, each with its
# unique ingredients, preparation time, cooking method, and nutritional
# information. Consider creating a `Recipe` class, and think about how you might
# create subclasses for different types of recipes (e.g., `MoroccanRecipe`,
# `EthiopianRecipe`, `NigerianRecipe`), each with their own unique properties and
# methods.

# class recipe 
# 
  
class Recipe:
    def __init__(self, name, country, ingredients, preparation_time, cooking_method):
        self.name = name
        self.country = country
        self.ingredients = ingredients
        self.preparation_time = preparation_time
        self.cooking_method = cooking_method
        

    def display_recipe(self):
        print(f"Recipe: {self.name}")
        print(f"Country: {self.country}")
        print("Ingredients:") 
        
        
class MoroccanRecipe(Recipe):
    def __init__(self, name, ingredients, preparation_time, cooking_method, serving_suggestion):
        Recipe.__init__(self, name, "Morocco", ingredients, preparation_time, cooking_method)
        self.serving_suggestion = serving_suggestion

    def display_recipe(self):
        Recipe.display_recipe(self)
        print(f"Serving Suggestion: {self.serving_suggestion}") 
        
class EthiopianRecipe(Recipe):
    def __init__(self, name, ingredients, preparation_time, cooking_method, spice_level):
        Recipe.__init__(self, name, "Ethiopia", ingredients, preparation_time, cooking_method)
        self.spice_level = spice_level

    def display_recipe(self):
        Recipe.display_recipe(self)
        print(f"Spice Level: {self.spice_level}") 
        
class NigerianRecipe(Recipe):
    def __init__(self, name, ingredients, preparation_time, cooking_method, nutritional_information):
        Recipe.__init__(self, name, "Nigeria", ingredients, preparation_time, cooking_method)
        self.nutritional_information = nutritional_information

    def display_recipe(self):
        Recipe.display_recipe(self)
        print("Nutritional Information:")
     
#      5. Create a class called Product with attributes for name, price, and quantity.
# Implement a method to calculate the total value of the product (price * quantity).
# Create multiple objects of the Product class and calculate their total values.
                  
      
class Product:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

    def calculate_total_value(self):
        return self.price * self.quantity


product1 = Product("Apple", 30, 10)
product2 = Product("Banana", 10, 8)
product3 = Product("Orange", 20, 12)

total_value1 = product1.calculate_total_value()
total_value2 = product2.calculate_total_value()
total_value3 = product3.calculate_total_value()

print(f"Total value of {product1.name}s: Ksh {total_value1}")
print(f"Total value of {product2.name}s: Ksh {total_value2}")
print(f"Total value of {product3.name}s: Ksh {total_value3}")

total_value_all = total_value1 + total_value2 + total_value3
print(f"Total value of all products: Ksh {total_value_all}")


# 6. Implement a class called Student with attributes for name, age, and grades (a
# list of integers). Include methods to calculate the average grade, display the
# student information, and determine if the student has passed (average grade >=
# 60). Create objects for the Student class and demonstrate the usage of these
# methods.
#  class student, get the sum grades then to get average divide by the total no of grades
# if averagegrade >=60 the student has passed
class Student:
    def __init__(self, name, age, grades):
        self.name = name
        self.age = age
        self.grades = grades

    def calculate_average_grade(self):   
        total_grades = sum(self.grades)
        average_grade = total_grades / len(self.grades)
        return average_grade

    def display_student_info(self):
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Grades: {self.grades}")

    def has_passed(self):
        average_grade = self.calculate_average_grade()
        return average_grade >= 60

# instances for the student 
student1 = Student("Elizabeth", 21, [80, 75, 90, 95])
student1.display_student_info()
average_grade1 = student1.calculate_average_grade()
print(f"Average Grade: {average_grade1}")
print(f"Passed: {student1.has_passed()}")

print()

# 8. Create a LibraryCatalog class that handles the cataloging and management of
# books in a library. Implement methods to add new books, search for books by
# title or author, keep track of available copies, and display book details.
# class  LibraryCatalog has management and handling of books so we need
# class book which will have the data about each book ie;title,author and copies 
# easy access to class  LibraryCatalog ie we can add book,search
class Book:
    def __init__(self, title, author, total_copies):
        self.title = title
        self.author = author
        self.total_copies = total_copies
        self.available_copies = total_copies

    def display_details(self):
        print("Title:", self.title)
        print("Author:", self.author)
        print("Total Copies:", self.total_copies)
        print("Available Copies:", self.available_copies)


class LibraryCatalog:
    def __init__(self):
        self.books = []

    def add_book(self, title, author, total_copies):
        book = Book(title, author, total_copies)
        self.books.append(book)

    def search_by_title(self, title):
        found_books = []
        for book in self.books:
            if book.title.lower() == title.lower():
                found_books.append(book)
        return found_books

    def search_by_author(self, author):
        found_books = []
        for book in self.books:
            if book.author.lower() == author.lower():
                found_books.append(book)
        return found_books

    def display_book_details(self, title):
        found_books = self.search_by_title(title)
        if found_books:
            for book in found_books:
                book.display_book_details()
        else:
            print("Book not found in the library.")

library = LibraryCatalog()
library.add_book("Born A Crime", "Trevor Noah", 13)


         