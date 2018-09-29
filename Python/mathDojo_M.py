class MathDojo():
    def __init__(self,value=0):
        self.value=value
    def add(self,left,*right):
        self.value+=left+sum(right)
        return self
    def subtract(self,left,*right):
        self.value-=left+sum(right)
        return self
    def result(self):
        print(self.value)
one=MathDojo(7).result()
two=MathDojo(4).add(5,6,7,8).subtract(12).result()
three=MathDojo(-12).add(4).subtract(-8,0,1,-1).result()