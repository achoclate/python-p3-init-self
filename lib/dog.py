#!/usr/bin/env python3


class Dog:
    def __init__(self, name, breed="Mutt"):
        self.name = name
        self.breed = breed

# Example 
if __name__ == "__main__":
    # Creating a dog with both name and breed
    dog1 = Dog(name="Buddy", breed="Golden Retriever")
    print(f"Dog1 Name: {dog1.name}, Breed: {dog1.breed}")

    # Creating a dog with only name, breed should default to "Mutt"
    dog2 = Dog(name="Max")
    print(f"Dog2 Name: {dog2.name}, Breed: {dog2.breed}")

    