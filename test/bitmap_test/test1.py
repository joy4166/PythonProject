from PIL import Image


def create_colored_heart_bitmap(file_name):
    # Define the heart shape as a list of strings
    heart_shape = [
        "01100110",
        "11111111",
        "11100111",
        "01111110",
        "00122100",
        "00011000",
    ]

    # Define colors for each pixel
    colors = {
        "0": (255, 255, 255),  # White for 0 (empty space)
        "1": (255, 180, 20),  # Red for 1 (heart shape)
        "2": (200, 100, 10),
    }

    # Create a new blank image with the dimensions of the heart shape
    width = len(heart_shape[0])
    height = len(heart_shape)
    image = Image.new("RGB", (width, height))

    # Set pixel colors in the image based on the heart shape and colors dictionary
    for y, row in enumerate(heart_shape):
        for x, pixel in enumerate(row):
            color = colors[pixel]
            image.putpixel((x, y), color)

    # Save the image
    image.save(file_name)


# Example usage
file_name = "colored_heart_bitmap.bmp"  # Name of the output file
create_colored_heart_bitmap(file_name)
