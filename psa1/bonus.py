import extcolors
import PIL
img = PIL.Image.open("danger_zone.png")
colors, pixel_count = extcolors.extract_from_image(img)
area = 42
p = 0
for i in range(len(colors)):
    if colors[i][0] == (255, 0, 0):
        p = colors[i][i] * area / pixel_count
print("Red color are: ", p)