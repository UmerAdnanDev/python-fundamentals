Cube = {x:x**3 for x in range(1,11)}
print(Cube)#{1: 1, 2: 8, 3: 27, 4: 64, 5: 125, 6: 216, 7: 343, 8: 512, 9: 729, 10: 1000}
ODD = {f"{x}":x for x in range(1,11) if x%2!=0}
print(ODD)