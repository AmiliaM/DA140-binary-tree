CHILDREN_PER_NODE = 2
BUFFER_SIZE = 100 #This is the buffer between the top of the window and the point where new nodes can be generated - NOT a buffer in memory
MIN_LENGTH, MAX_LENGTH = 50, 90 #Min and max distance between nodes
X_SIZE, Y_SIZE = 1100, 450 #Size of window

DRAW_UPWARDS = True #true = Tree is drawn from bottom up, false = vice versa

class Node:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.children = []
        
    def add_child(self, child):
        self.children.append(child)
    
def gen_nodes(x, y):
    n = Node(x, y)
    if y > BUFFER_SIZE: #checks if node is too close to the top of the window to generate children
        for i in range(0, CHILDREN_PER_NODE):
            angle_ = (random(180, 360)*.5) + (map(noise(x), 0, 1, 180, 360)*.5)
            length_ = random(MIN_LENGTH, MAX_LENGTH)
            y_len = length_*sin(radians(angle_))
            x_len = length_*cos(radians(angle_))
            o = gen_nodes(x + x_len, y + y_len) 
            n.add_child(o)
    return n
    
def draw_nodes(node, left_shift):
    x, y = node.x, node.y
    i = 0
    for child in node.children:
        if i:
            stroke(100, map(y, 0, Y_SIZE, 0, 255), 100)
        else:
            stroke(map(y, 0, Y_SIZE, 0, 255), 100, 100)
        line(x, y, child.x, child.y)
        draw_nodes(child, left_shift)  
        i = (i + 1)%2 #i alternates between 1 and 0



add_library('pdf')
def setup():
    global head_node
    size(X_SIZE, Y_SIZE) #create window
    if DRAW_UPWARDS:
        head_node = gen_nodes(X_SIZE/2, Y_SIZE-50)  
    strokeWeight(2)

i = 0; 
def draw():
    global i
    background(0, 0, 55)
    draw_nodes(head_node, i)
    i+=1
    if i > X_SIZE: i = 0


def mousePressed():
    global head_node
    beginRecord(PDF, "tree.pdf")
    background(0, 0, 55)
    head_node = gen_nodes(X_SIZE/2, Y_SIZE-50)
    draw_nodes(head_node, 0)
    endRecord()
