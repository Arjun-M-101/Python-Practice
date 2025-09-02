Songs=["Believer", "Shape of You", "Blinding Lights", "Despacito"]
Artists=["Imagine Dragons", "Ed Sheeran", "The Weeknd", "Luis Fonsi"]
#Albums=["Evolve", "Divide", "After Hours", "Vida"]
Albums=[]
for i in range (len(Songs)):
    Albums.append(f"{Songs[i]} by {Artists[i]}")
print(Albums)