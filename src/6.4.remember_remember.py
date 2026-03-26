from PIL import Image

def remember_remember(image_path):
    """
    Decode a hidden message from an image.
    In each column, a black pixel indicates the row number
    corresponding to the ASCII value of the character.

    :param image_path: Path to the image file
    :return: Decoded message
    """
    image = Image.open(image_path).convert("L")   # Open in grayscale
    width, height = image.size

    message = ""

    for x in range(width):                  # Iterate over each column
        for y in range(height):             # Iterate over each row
            if image.getpixel((x, y)) == 0:  # Black pixel found
                message += chr(y)           # Convert row index to character
                break                       # Move to next column

    return message


# Backward-compatible alias
dechiffrer = remember_remember