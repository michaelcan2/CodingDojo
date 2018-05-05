'''
class Human():
    
    def __init__(self,name,gender):

        self.name= name
        self.gender= gender
    
    def speak_name(self):
        print "My name is {}".format(self.name)

will = Human ('William', 'Male')

print will.name
print will.gender

will.speak_name()
'''
'''
class Human():
    
    def __init__(self,name,gender):

        self.name= name
        self.gender= gender
    
    def speak_name(self):
        print "My name is {}".format(self.name)
    
    def speak(self,text):
        print text

will = Human ('William', 'Male')

print will.name
print will.gender

will.speak("I love python programming")
'''

'''
class Human():
    
    def __init__(self,name,gender):

        self.name= name
        self.gender= gender
    
    def speak_name(self):
        print "My name is {}".format(self.name)
    
    def speak(self,text):
        print text

    def perform_math_task(self,math_operation,)

will = Human ('William', 'Male')

print will.name
print will.gender

will.speak("I love python programming")
'''

class bike(object):
    def __init__(self,price,max_speed):
        self.price=price 
        self.max_speed=max_speed
        self.miles=0
        
    def displayinfo(self):
        # print self.price
        # print self.max_speed
        print "hello, {}?! that makes me want to run {}, and I used {} amount of miles.".format(self.price,self.max_speed,self.miles)
        return self
    
    def ride(self):
        print "Riding"
        self.miles += 10 
        print "I have just finished Riding {} miles.".format(self.miles)
        return self

    def reverse(self):
       print "Reversing"
       self.miles -=5
       print "Everything is going down {}".format(self.miles) 
       return self

redBike=bike("$50","40mph")
greenBike=bike("$70","7mph")
blueBike=bike("100","14mph")

redBike.displayinfo().ride().displayinfo().ride()