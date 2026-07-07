from PIL import Image

try:
    img = Image.open('c:/Users/steph/Downloads/theos/static/images/logo.png')
    # Convert to RGBA if not already to handle transparency
    img = img.convert("RGBA")
    
    # Get bounding box of non-transparent / non-white pixels
    # Find bounding box based on alpha and color
    bbox = img.getbbox()
    
    # Actually, if the background is solid white instead of transparent, getbbox() might not crop it.
    # We can try making white transparent first.
    datas = img.getdata()
    newData = []
    for item in datas:
        # If it's pure white or very close to it, make it transparent
        if item[0] > 240 and item[1] > 240 and item[2] > 240:
            newData.append((255, 255, 255, 0))
        else:
            newData.append(item)
    
    img.putdata(newData)
    bbox = img.getbbox()
    
    if bbox:
        img = img.crop(bbox)
        img.save('c:/Users/steph/Downloads/theos/static/images/logo.png', "PNG")
        print("Logo cropped successfully.")
    else:
        print("Could not find bounding box.")
except Exception as e:
    print("Error cropping logo:", e)
