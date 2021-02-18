import turtle as t

x = -200
y = 0

length = 100
depth = 7

def practal(l, d):
    if d == 0:
        t.left(30); t.fd(l); 
        
        t.left(180); t.fd(l);
        
        t.right(240); t.fd(l); 
        
        t.left(180); t.fd(l);
        
        t.left(30);
    else:
        t.left(30); t.fd(l); practal(l*3/4,d-1)
        
        t.fd(l);
        
        t.left(120); t.fd(l); practal(l*3/4,d-1)
        
        t.fd(l);
        
        t.left(30);
        
        


t.speed(0)
t.setheading(90)
t.fd(length)

practal(length*3/4,depth)
