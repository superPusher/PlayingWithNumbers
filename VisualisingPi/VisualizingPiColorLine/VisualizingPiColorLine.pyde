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
    i = 1
    while i < cHeight and i< len(pi):
        digit = int(pi[i])
        stroke(d_color[digit][0], d_color[digit][1], d_color[digit][2])
        noFill()
        line(0,i, cWidth, i)
        i += 1
    save('pi_color_lines.png')    
    exit()
