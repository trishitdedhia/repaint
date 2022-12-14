#!/bin/python
from PIL import Image
import sys

#Get image
img = Image.open(sys.argv[2])

#Convert image to rgb
img = img.convert('RGBA')


#Get old pixels
print("What are the RGB values of the pixels you want to repaint?")
rr=int(input(f'R (0-255) : '))
gg=int(input(f'G (0-255) : '))
bb=int(input(f'B (0-255) : '))
#aa=input(f'A (0-1) : ')


#Get old pixels
print("What are the RGBA values of the new paint?")
r=int(input(f'R (0-255) : '))
g=int(input(f'G (0-255) : '))
b=int(input(f'B (0-255) : '))
a=int(input(f'A (0-255) : '))

#Get image data
data = img.getdata()
newdata = []

#Set variables for the loops
total = img.width * img.height
sum = 0
progress = 0
prev=0

#Insert Progress
print(f'Processing Image... 0%', end="")

#Run a loop for each pixel
for px in data:
    #print(px[0])
    #print(px[1])
    #print(px[2])

    #Check if the pixel matches
    if px[0] == rr and px[1] == gg and px[2] == bb:
        newdata.append((r, g, b, a))
        sum += 1
    else:
        newdata.append(px)
    
    #Increment Progress and print
    progress += 1
    percent = int((progress / total) * 10) * 10
    # Print only if there is a new value
    if prev != percent:
        print(f'\rProcessing Image... {percent}%', end="")
        prev = percent

#End process Image
print("\nImage Processed.")

#Put data and save image
img.putdata(newdata)
img.save(sys.argv[1])






