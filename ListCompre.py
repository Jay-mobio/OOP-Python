squares = []
for x in range(10):
    squares.append(x**2)
print(squares)

l1 = [(x,y) for x in (1,2,3) for y in (4,5,6) if x!=y]
print(l1)
