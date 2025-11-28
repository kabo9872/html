class student:
    grade = 9
    name = "kabo"

    def introduction(self):
        print("Hi i am a student ")

    def details(self):
        print("My name is" , self.name)
        print("I study in Grade", self.grade)

ob = student()
ob.introduction()
ob.details()