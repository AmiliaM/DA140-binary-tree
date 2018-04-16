add_library('pdf')
#import * from processing.pdf
x_size_, y_size_ = 1100, 450

class Node:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        
    def add_child(self, child):
        self.children.append(child)



def setup():
    size(x_size_,  y_size_)
    strokeWeight(2)
    #colorMode(HSB, y_size_, 100, 100)
    background(0, 0, 55)


def gen_tree(start_x, start_y):
    i = 0
    end_points = [(start_x, start_y)]
    while end_points:
        x, y = end_points.pop()
        if y > 100:
            angle = random(180, 360)
            length_ = random(50, 90)
            y_len = length_*sin(radians(angle))
            x_len = length_*cos(radians(angle))
            stroke(map(y, 0, 450, 0, 255), 100, 100)
            line(x, y, x + x_len, y + y_len)
            end_points.append((x + x_len, y + y_len))    
            i+=1
            angle = random(180, 360)
            length_ = random(50, 90)
            y_len = length_*sin(radians(angle))
            x_len = length_*cos(radians(angle))
            stroke(100, map(y, 0, 450, 0, 255), 100)
            line(x, y, x + x_len, y + y_len)
            end_points.append((x + x_len, y + y_len))
            i+=1
    print(i)
    

def draw():
    pass


def mousePressed():
    beginRecord(PDF, "tree.pdf")
    background(0, 0, 55)
    gen_tree(x_size_/2, y_size_-50)
    endRecord()