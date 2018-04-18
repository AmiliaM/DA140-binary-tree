CHILDREN_PER_NODE = 2
BUFFER_SIZE = 100
MIN_LENGTH, MAX_LENGTH = 50, 90
X_SIZE, Y_SIZE = 1100, 450

#DIRECTION = true #true = up, false = down

class Node:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.children = []
        
    def add_child(self, child):
        self.children.append(child)
    
def gen_nodes(x, y):
    n = Node(x, y)
    if y > BUFFER_SIZE:
        for i in range(0, CHILDREN_PER_NODE):
            angle_ = random(180, 360)
            length_ = random(MIN_LENGTH, MAX_LENGTH)
            y_len = length_*sin(radians(angle_))
            x_len = length_*cos(radians(angle_))
            o = gen_nodes(x + x_len, y + y_len)
            n.add_child(o)
    return n
    
def draw_nodes(node):
    x, y = node.x, node.y
    i = 0
    for child in node.children:
        child_x, child_y = child.x, child.y
        if i:
            stroke(100, map(y, 0, Y_SIZE, 0, 255), 100)
        else:
            stroke(map(y, 0, Y_SIZE, 0, 255), 100, 100)
        line(x, y, child.x, child.y)
        draw_nodes(child)  
        i = (i + 1)%2



add_library('pdf')
def setup():
    size(X_SIZE, Y_SIZE)
    strokeWeight(2)
    #colorMode(HSB, y_size_, 100, 100)
    background(0, 0, 55)

def draw():
    pass


def mousePressed():
    beginRecord(PDF, "tree.pdf")
    background(0, 0, 55)
    draw_nodes(gen_nodes(X_SIZE/2, Y_SIZE-50))
    
    endRecord()