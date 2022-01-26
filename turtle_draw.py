import turtle as turd
import time
## commands can be shortened turd.rt/fd/lt/bk
screen = turd.getscreen()
s = turd.getturtle()
m = s.clone()
h = m.clone()

s.pencolor("orange")
m.pencolor("red")
h.pencolor("white")
s.hideturtle()
m.hideturtle()
h.hideturtle()

turd.bgcolor("black")

s.speed(6)
s.lt(135)
m.speed(10)
m.lt(135)
h.speed(10)
h.lt(135)


seconds_count = 1; minute_count = 1; hour_count = 1
# t0 = time.time()
while True:
    
    s.fd(223.22)
    if seconds_count % 4 == 0:
        s.rt(96)
        # t1 = time.time()-t0
        # print(t1)
    else:
        s.rt(90)
    
    if seconds_count % 240 == 0:
        s.clear()
        minute_count = minute_count + 1
        # print(minute_count)
        m.fd(155)
        m.rt(90)
        m.fd(155)
        m.rt(90)
        m.fd(155)
        m.rt(90)
        m.fd(155)
        m.rt(96)
        # t2 = time.time() - t0
        print(t2)       
        if minute_count % 240 == 0:
            m.clear
            hour_count = hour_count +1
            h.fd(100)
            h.rt(90)
            h.fd(100)
            h.rt(90)
            h.fd(100)
            h.rt(90)
            h.fd(100)
            h.rt(120)
        
          
    seconds_count = seconds_count + 1


