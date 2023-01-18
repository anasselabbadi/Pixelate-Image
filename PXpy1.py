from PIL import Image

def pixelate_image(image_path, pixel_size):
    with Image.open(image_path) as im:
        # Resize the image to a smaller size
        im = im.resize((im.width // pixel_size, im.height // pixel_size), Image.BOX)
        # Resize the image back to its original size
        im = im.resize((im.width * pixel_size, im.height * pixel_size), Image.NEAREST)
        im.save("pixelated_"+image_path)

if __name__ == '__main__':
    image_path = "your_image.png"
    pixel_size = 10
    pixelate_image(image_path, pixel_size)
