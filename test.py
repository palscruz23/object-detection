


# def hex2rgb(hex):

    


#     return r,g,b

hex2num = {"0": 0, "1": 1, "2":2, "3": 3, "4": 4, "5":5, 
           "6": 6, "7": 7, "8":8, "9": 9, "a": 10, "b":11, 
           "c": 12, "d": 13, "e":14, "f": 15}

hex = "#ff1020"
print(hex[1:3])

red = hex[1:3]
r = hex2num[red[1]]*16 + hex2num[red[0]]

green = hex[1:3]
print(r)


for i in range(1, len(hex)-1, 2):
    red = hex[i:i+2]
    r = hex2num[hex[i]]*16 + hex2num[hex[i+1]]
    print(red)
    print(hex2num[hex[i]]*16)

