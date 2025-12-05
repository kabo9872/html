from abc import ABC, abstractmethod

class animal(ABC):
    
    def move(self):
        pass

class human(animal):
    
    def move(self):
        print("I can walk and run")


class snake(animal):
    print("I can crawl")



class dog(animal):
    print("I can bark")



R = human()
R.move

K = snake()
K.move

R = dog()
R.move