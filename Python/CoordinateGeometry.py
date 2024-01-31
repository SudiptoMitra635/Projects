
class Point:

    def __init__(self,x,y):
        self.x_cod = x
        self.y_cod = y
    
    def __str__(self):
        return '<{},{}>'.format(self.x_cod,self.y_cod)
    
    # to find the distance between two points
    def distance(self,other):
        return ((self.x_cod - other.x_cod)**2 + (self.y_cod - other.y_cod)**2)**0.5
    # to find the distance a point from origin
    def distance_from_origin(self):
        return self.distance(Point(0,0))
    
class Line:

    def __init__(self,A,B,C):
        self.A = A
        self.B = B
        self.C = C

    def __str__(self):
        return '{}x + {}y + {}'.format(self.A,self.B,self.C)
    
    # To check if a point lie on the line
    def point_on_line(line,Point):
        if line.A*Point.x_cod + line.B*Point.y_cod + line.C ==0:
            return "lie on the line"
        else:
            return "Does not lie on the line"
    
    # Shortest between line and a point
    def shortest_distance(line,point):
        return abs(line.A*point.x_cod + line.B*point.y_cod + line.C)/(line.A**2 + line.B**2)


l1 = Line(1,1,-2)
p1 = Point(1,1)
print(p1.distance_from_origin())
print(l1.point_on_line(p1))
print(l1.shortest_distance(p1))
