import os, sys
import cv2
from PIL import Image, ImageDraw, ImageOps
from cv2 import stylization
# method = cv2.TM_SQDIFF_NORMED

# # Read the images from the file
# image = cv2.imread('test.jpg')
# small_image1 = cv2.imread('small1.jpg')
# small_image2 = cv2.imread('small2.jpg')


# result = cv2.matchTemplate(small_image, large_image, method)
# result1 = cv2.matchTemplate(small_image1, large_image, method)
# result2 = cv2.matchTemplate(small_image2, large_image, method)

output= sys.argv[1]
def crop2(img,name):
    im = Image.open(img)
    bb= im.getbbox()
    # Get rid of existing black border by flood-filling with white from top-left corner
    ImageDraw.floodfill(im,xy=(0,0),value=(255,255,255),thresh=10)

    # Get bounding box of text and trim to it
    bbox = ImageOps.invert(im).getbbox()
    print(bb)
    x , y , w , h = bb
    if bbox:
        _ , y , _ , h = bbox
        trimmed = im.crop((x,y,w,h))
        res = ImageOps.expand(trimmed, border=10, fill=(255,255,255))
        res.save(name)  

def locate(key , pic):
    method = cv2.TM_SQDIFF_NORMED
    k = cv2.imread(key)
    p = cv2.imread(pic)
    result = cv2.matchTemplate(k,p,method)
    mn,_,mnLoc,_ = cv2.minMaxLoc(result)
    trows,tcols = k.shape[:2]
    StX,StY=mnLoc
    # crop_image = p[StY:StY+trows, StX:StX + tcols]
    # im = Image.fromarray(crop_image)
    # im.save("aaaaa.jpg")
    return StX,StY,StX+tcols,StY+trows
# We want the minimum squared difference
# mn,_,mnLoc,_ = cv2.minMaxLoc(result)
# mn,_,mnLoc1,_ = cv2.minMaxLoc(result1)

# mn,_,mnLoc2,_ = cv2.minMaxLoc(result2)
# # Draw the rectangle:
# # Extract the coordinates of our best match
# MPx,MPy = mnLoc
# MPx1,_ = mnLoc1
# _,MPy2 = mnLoc2

# Step 2: Get the size of the template. This is the same size as the match.
# trows,tcols = small_image.shape[:2]
# print(locate("small.jpg","test2.jpg"))
# def crop(name,source,x,y):
#     s = cv2.imread(source)
#     _,sy = s.shape[:2]
#     startY,_,_,startX = locate(x,source)
#     # endY,_,_,_ = locate(l,source)
#     _,endX,_,_ = locate(y,source)
#     endY = sy-startY
#     if startX<endX and startY<endY:
#         print(startX,startY,endX,endY)
#         image = Image.fromarray(s[startX:endX,startY-15:endY])
#         image.save(name)
def crop(name,source,x,y):
    s = cv2.imread(source)
    _,sy = s.shape[:2]
    startY,_,_,startX = locate(x,source)
    # endY,_,_,_ = locate(l,source)
    _,endX,_,_ = locate(y,source)
    endY = sy-startY
    if startX<endX and startY<endY:
        print(startX,startY,endX,endY)
        image = Image.fromarray(s[startX:endX,startY-15:endY])
        image.save(name)

for x in os.listdir(f"Output/{output}-temp"):
    print(x)
    # crop(f"Output/{output}/"+x,f"Output/{output}-temp/"+x,"key1.png","key2.png")
    crop2(f"Output/{output}-temp/"+x,f"Output/{output}/"+x)


# crop("out/math.jpg","math/math_page-0001.jpg","small.jpg","small2.jpg")



# # Step 3: Draw the rectangle on large_image
# cv2.rectangle(image, locate('small.jpg','test.jpg'),0)

# cv2.imshow('output',image)

# # The image is only displayed if we call this
# cv2.waitKey(0)