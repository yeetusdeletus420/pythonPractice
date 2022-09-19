def setup():
    size(480, 120)
    
def draw():
    if mousePressed:
        fill(0)
    else:
        fill(225)
    ellipse(mouseX, mouseY, 80, 80)
