class Fraction:

    # parameterized constructor
    def __init__(self,x,y):
        self.num = x
        self.den = y
    
    # exicutes when print function is called
    def __str__(self):
        return '{}/{}'.format(self.num,self.den)
    
    # exicutes when + is placed between the two object of same class
    def __add__(self, other):
        new_num = self.num * other.den + other.num * self.den
        new_den = self.den*other.den
        return '{}/{}'.format(new_num,new_den)
    
    #similarly -
    def __sub__(self,other):
        new_num = self.num * other.den - other.num * self.den
        new_den = self.den*other.den
        return '{}/{}'.format(new_num,new_den)
    
    #similarly *
    def __mul__(self,other):
        new_num = self.num * other.num
        new_den = self.den * other.den
        return '{}/{}'.format(new_num,new_den)
    
    #similarly /
    def __truediv__(self,other):
        new_num = self.num * other.den
        new_den = self.den * other.num
        return '{}/{}'.format(new_num,new_den)
    
    #non-magic method
    def convert_to_decimal(self):
        return self.num/self.den


fr1 = Fraction(3,4)
fr2 = Fraction(2,3)
print(fr1, fr2)
print(fr1 + fr2)
print(fr1 - fr2)
print(fr1 * fr2)
print(fr1/fr2)
print(fr1.convert_to_decimal())