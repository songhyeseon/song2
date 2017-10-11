import turtle as t
n=6
t.color("orange")
for x in range(12):
    t.begin_fill()
    for x in range(12):
        t.forward(20)
        t.left(360/n)
    t.end_fill()
    for x in range(n):
        t.forward(20)
        t.right(360/n)
    t.right(30)
    t.forward(60)
    
