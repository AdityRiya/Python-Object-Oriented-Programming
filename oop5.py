class Circle():
    pi = 3.1415
    def __init__(self,radius=1):
        self.radius = radius
        
    def area(self):
        return self.radius*self.radius * Circle.pi
    
    def set_r(self,new_r):
        self.radius = new_r

myc= Circle(5)
print(myc.radius)      
print(myc.area())   
myc.set_r(100)
print(myc.area())  