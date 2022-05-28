# create a class
class person():
    def __init__(self,name,gender,age,origin,phone):
        self.name=name
        self.gender=gender
        self.age=age
        self.origin=origin
        self.phone=phone

    def info_func(self):
        print(f'This is {self.name}, {self.gender}, is {self.age} years old.')

        if self.gender == 'male':
            print(f'He is from {self.origin}, and his phone number is {self.phone}.')
        else:
            print(f'She is from {self.origin}, and her phone number is {self.phone}.')

    
person1=person('Susan', 'female', 23, 'Canada', 77788999)
person2=person('Jack', 'male', 21, 'USA', 22188966)
