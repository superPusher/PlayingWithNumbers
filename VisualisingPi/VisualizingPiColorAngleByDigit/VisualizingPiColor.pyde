import time

cWidth = 800
cHeight = 800

def setup():
    size(cWidth, cHeight)
    global pi
    pi = loadStrings("../pi.txt")[0]
    print(len(pi))
    global d_color
    d_color=[[224, 187, 228], [255,179,186], [255,200,186], [255,223,186], [255,245,186], [255,255,186], [230,255,193], [186,255,201], [186,225,226], [186,225,255]]
    global diagonal_length
    diagonal_length = sqrt( cWidth**2 + cHeight**2)

def draw():
    background(0)
    translate(cWidth/2,cHeight/2)
    
    last = 0
    radio = 1
    i = 0
    
    while radio < diagonal_length:
        digit = int(pi[i])
        angle = (digit + 1)*TWO_PI/10
        total_angle = last + angle
        strokeWeight(2)  
        if total_angle < TWO_PI:
            stroke(d_color[digit][0], d_color[digit][1], d_color[digit][2] )
            noFill()
            arc(0, 0, radio, radio, last, total_angle)
            last = total_angle
        else:    
            stroke(d_color[digit][0], d_color[digit][1], d_color[digit][2] )
            noFill()            
            arc(0, 0, radio, radio, last, TWO_PI)
            difference = total_angle - TWO_PI
            radio += 1
            arc(0, 0, radio, radio, 0, difference)
            last = difference
        i += 1
    save('pi_color.png')    
    #exit()
    
