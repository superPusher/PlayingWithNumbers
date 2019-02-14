
cWidth = 2000
cHeight = 2000

def setup():
    size(cWidth, cHeight)
    global pi
    pi = loadStrings("../pi.txt")[0]

def draw():
    background(0)
    translate(cWidth/2,cHeight/2)
    for i in range(int(cWidth*1.41)):
        digit = int(pi[i])
        grey = int(digit*255/9)
        stroke(grey)
        noFill()
        arc(0,0,i,i, 0,TWO_PI)
    save('pi_greyscale.png')    
    exit()
    
    
