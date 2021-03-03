class student:
    
    def __init__(self,name,age):
        self.name = name
        self.age = age

    def introduce(self):
        print(f'''
        Hello My name is {self.name}!!
        I am {self.age} years old
        How are you?
        ''')

    def GetIntroduction(self):
        return f'''
        Hello My name is {self.name}!!
        I am {self.age} years old
        How are you?
        '''


