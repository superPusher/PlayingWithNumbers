cWidth = 2000
cHeight = 2000

def setup():
    size(cWidth, cHeight)
    global pi
    pi = loadStrings("../pi.txt")[0]
    global d_color
    d_color=[[224, 187, 228], [255,179,186], [255,200,186], [255,223,186], [255,245,186], [255,255,186], [230,255,193], [186,255,201], [186,225,226], [186,225,255]]
    global diagonal_length
    diagonal_length = sqrt( cWidth**2 + cHeight**2)

def draw():
    background(0)
    translate(cWidth/2,cHeight/2)
    i = 1
    radio = 1
    while i < diagonal_length and i< len(pi):
        digit = int(pi[i])
        stroke(d_color[digit][0], d_color[digit][1], d_color[digit][2])
        #strokeWeight(10)  # this prevents some weird lines to appear due to resolution
        angle_digit = (i % 6)*TWO_PI/6
        noFill()
        arc(0, 0, radio, radio, angle_digit, angle_digit + PI/3)
        if i%6==0:
            radio += 1
        i += 1
    save('pi_color_radio.png')    
    #exit()
