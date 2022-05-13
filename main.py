import cv2 as cv
import numpy as np

img=cv.imread("luffy.jpg")
gray=cv.imread("luffy.jpg", 0)

print("""
ACTIVITY #5:

The program should be:

    1. Accept/load colored img. Grayscale should be rejected.
    2. Output a pixel value.
    3. Modify a pixel value.
    4. Set img dimensions. Within boundaries or not.
    5. Set img total pixel count. Higher or lower than the set pixel.
    6. Show the currently loaded image's data type.
    7. exit
""")

opt=int(input("input number: "))
if opt == 1 :
    imgLen = len(img.shape)
    grayLen = len(gray.shape)
    if imgLen > grayLen:
        cv.imshow("colored", img)
        cv.waitKey(0)
    else:
        exit()

elif opt == 2:
    x = int(input("for x axis: "))
    y = int(input("for y axis: "))
    color = int(input("BGR selection: [1. BLUE] [2. GREEN] [3. RED]: "))
    print(img.item(x, y , color))

elif opt == 3:
    x = int(input("for x axis: "))
    y = int(input("for y axis: "))
    print(img[x, y])
    for i in range(0, 3, 1):
        color = int(input("BGR selection: [1. BLUE] [2. GREEN] [3. RED]: "))
        pixelValue = int(input("Pixel Value: "))
        img.itemset((x, y, color), pixelValue)
    print(img[x, y])
    cv.imshow("colored", img)
    cv.waitKey(0)

elif opt == 4:
    x=450
    y=150
    print(img.shape)
    print(f"""
                total pixel in x-axis: {img.shape[0]}
                total pixel in y-axis: {img.shape[1]}
                compared value in x-axis: {x}
                compared value in y-axis: {y}
            """)

    if x <= img.shape[0] and y <= img.shape[1] :
        print("Within boundaries")
    else :
        print("Out of boundaries")

elif opt == 5:
    x=150
    y=150
    fixedValue=x * y
    totalPixel=img.shape[0] * img.shape[1]

    print(f"""
              total fixed variable: {fixedValue}
              total image pixels: {totalPixel}
            """)

    if fixedValue > totalPixel :
        print("higher")
    elif fixedValue < totalPixel :
        print("lower")
    else :
        print("equal")

elif opt == 6:
    print(f"image data type is: {img.dtype}")

else:
    exit()