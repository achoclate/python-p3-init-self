#!/usr/bin/env python3

# Define the Person class
class Person:
    def __init__(self, name):
        self.name = name

# Example 
if __name__ == "__main__":
    # Creating a person with a name
    person1 = Person(name="Alice")
    print(f"Person Name: {person1.name}")

    # Creating another person with a different name
    person2 = Person(name="Bob")
    print(f"Person Name: {person2.name}")

