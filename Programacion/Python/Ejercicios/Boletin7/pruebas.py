tamaño=3
for i in range(-1,tamaño+1):
    if (i+2)%2!=0:
        espacios=tamaño-i
        print(" "*espacios+"* "*(i+2))