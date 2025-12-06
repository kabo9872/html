class cat:

    def __init__(self,name,age):
        self.name = name
        self.age = age


    def info(self):
        print(f"I am a cat.My name is {self.name}. I am {self.age} years old.")

    
    def make_sound(self):
        print("meow")



class dog:

    def __init__(self,name,age):
        self.name = name
        self.age = age

    
    def info(self):
        print(f"I am a dog. My name is {self.name}. I am {self.age} years old.")

    
    def make_sound(self):
        print("bark")


catone = cat("misky",3)
dogone = dog("spike",3.2)


for animal in(catone,dogone):
    animal.make_sound()
    animal.info()