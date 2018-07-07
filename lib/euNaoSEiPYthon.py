
Xs =[26, 64, 100, 138,
    48, 83, 118, 153,
    33, 66, 100, 133,
    51, 83, 115, 147,
    36, 67, 98, 129,
    55, 84, 113, 143,
    41, 70, 97, 124,
    56, 83, 110, 137
    ]

Ys =[162, 162, 162, 162,
    140, 140, 140, 140, 
    122, 122, 122, 122, 
    105, 105, 105, 105, 
    90, 90, 90, 90,
    74, 74, 74, 74, 
    61, 61, 61, 61, 
    48, 48, 48, 48
 ]

Name = ["A8", "C8", "E8", "G8", 
        "B7", "D7", "F7", "H7",
        "A6", "C6", "E6", "G6", 
        "B5", "D5", "F5", "H5",
        "A4", "C4", "E4", "G4", 
        "B3", "D3", "F3", "H3",
        "A2", "C2", "E2", "G2", 
        "B1", "D1", "F1", "H1"]

def fileWrite(g, i):
    
    file.write(".eqv "+ Name[i] + " " +  g + "\n") 

def main():
    for i in range (len(Xs)):
        x = Xs[i]
        y = Ys[i]
        f = int(x)+(320*int(y))+4278190080
        print(f)
        f= hex(f)
        print(f)
        fileWrite(f, i)



if __name__ == '__main__':
    file = open("mapping.s","w")
    main()
    file.close()

