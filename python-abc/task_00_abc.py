#!/usr/bin/python3
"""Define an abstract class"""


from abc import ABC, abstractmethod


class Animal(ABC):
    """Abstract class"""
    @abstractmethod
    def sound(self):
        """Sound method"""
        pass


    class Dog(Animal):
        """Dog class.
        
        Args:
            Animals (class): Abstract class.
            """
        
        def sound(self):
            """Sound method for the dog
            
            Returns:
                str: Bark
            """
            return "Bark"
        
    
    class Cat(Animal):
        """Cat class.
        
        Args:
            Animals (class): Abstract class.
        """

        def sound(self):
            """Sound method for the cat.
            Returns:
                str: Meow
            """
            return "Meow"
