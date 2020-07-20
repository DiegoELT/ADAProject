import imageio

def luma(imgName):
    #imgName = input("Image name: ")
    umbral = 10 #float(input("Umbral: "))
    type = 'c' #input("CCIR 601 = c, BT. 709 = b, SMPTE 240M = s: " )

    CCIR = (0.299, 0.587, 0.114)
    BT = (0.2126, 0.7152, 0.0722)
    SMPTE = (0.212, 0.701, 0.087)

    if type == 'c':
        coefficients = CCIR
    elif type == 'b':
        coefficients = BT
    else:
        coefficients = SMPTE

    img = imageio.imread(imgName)

    encodedImg = []

    for row in img:
        tempRow = []
        for pixel in row:
            if (pixel[0]*coefficients[0]+pixel[1]*coefficients[1]+pixel[2]*coefficients[2]) >= umbral:
                tempRow.append(1)
            else:
                tempRow.append(0)
        encodedImg.append(tempRow)

    return encodedImg