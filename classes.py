# define a class

class Point:
    def __init__(self,x,y):
        self.x = x
        self.y = y

    def move(self):
         print("Move")
    
    def draw(self):
        print("draw")


point = Point(10,20)
point.x=11
print(point.x)

"""
    
point1 = Point()
point1.x = 10
point1.y = 20

print(point1.x)
point1.draw()

point2 = Point()
point2.x = 200
print(point2.x) # invalid if point2.x is not defined

"""

class Person:
    def __init__(self, name="John Arrington"):
        self.name = name

    def talk(self):
        print(f"Hello there!, I am {self.name}")


Person1 = Person()
Person1.talk()
Person2 = Person("Marie Schrader")
Person2.talk()