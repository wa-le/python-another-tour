import colorgram

# list to store colours extracted
rgb_colors = []

# the extract class takes an image and the amount of colors you wish to extract from the image
colors = colorgram.extract('image.jpg', 5)

for t_color in colors:
    r = t_color.rgb.r
    g = t_color.rgb.g
    b = t_color.rgb.b
    new_color = (r, g, b)
    rgb_colors.append(new_color)

print(rgb_colors)
