# for commit

class Person:
    def __init__(self, name):
        self.name = name

    def talk(self):
        print(f"Hi I am {self.name} what should I say? ")
        message = input(" ")
        print(f"{self.name} said " + message)


justin = Person("Justin")
justin.talk()
print("Thanks for talking with me goodbye. ")
