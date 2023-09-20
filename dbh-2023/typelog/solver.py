#!/usr/bin/env python3

import matplotlib.pyplot as plt

def printlayout():
    layout = [
    [47.0,-123.0,"z"],
    [62.0,-123.0,"x"],
    [77.0,-123.0,"c"],
    [92.0,-123.0,"v"],
    [107.0,-123.0,"b"],
    [122.0,-123.0,"n"],
    [137.0,-123.0,"m"],
    [152.0,-123.0,","],
    [167.0,-123.0,"."],
    [40.0,-110.0,"a"],
    [55.0,-110.0,"s"],
    [70.0,-110.0,"d"],
    [85.0,-110.0,"f"],
    [100,-110.0,"g"],
    [115,-110.0,"h"],
    [130,-110.0,"j"],
    [145,-110.0,"k"],
    [160,-110.0,"l"],
    [35.0,-93.0,"q"],
    [50.0,-93.0,"w"],
    [65.0,-93.0,"e"],
    [80.0,-93.0,"r"],
    [95.0,-93.0,"t"],
    [110.0,-93.0,"y"],
    [125.0,-93.0,"u"],
    [140.0,-93.0,"i"],
    [155.0,-93.0,"o"],
    [170.0,-93.0,"p"],
    [40.0,-77.0,"2"],
    [55.0,-77.0,"3"],
    [70.0,-77.0,"4"],
    [85.0,-77.0,"5"],
    [100.0,-77.0,"6"],
    [115.0,-77.0,"7"],
    [130.0,-77.0,"8"],
    [145.0,-77.0,"9"],
    [160.0,-77.0,"0"],
    [175.0,-77.0,"-"],
    [190.0,-77.0,"="],
    [205.0,-77.0,"<-"],
    ]
    
    for char in layout:
        plt.text(char[0],char[1],str(char[2]))
        #plt.show()
    
def main():
      
    down_x = 0
    down_y = 0
    up_x = 0
    up_y = 0
    
    printlayout()
    
    with open("type.log", encoding="ascii") as lines:
        counter = 1
        outputline = 1
        for line in lines:
            line_elements = line.split('\t')
            x,y = line_elements[2].split('/')
            
            if "down" in line:
                down_x = x.strip('*')
                down_y = y.strip('*')
            
            if "up" in line:
                up_x = x
                up_y = y
                
                plt.plot([float(down_x),float(up_x)],[-1*float(down_y),-1*float(up_y)])
                
                # print counter
                plt.text(float(down_x),-1*float(down_y),str(counter))
                
                counter += 1
                if (counter > 10):
                    printlayout()
                    print("showing "+ str(outputline))
                    plt.show()
                    outputline += 1
                    counter=1

    printlayout()
    print("showing "+ str(outputline))
    plt.show()
            
if __name__ == "__main__":
    main()
