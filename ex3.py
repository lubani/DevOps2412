"""
Luba Ira
email lubacareer@gmail.com
"""

from PIL import Image
import random

# Image size
width, height = 256, 256

try:
    a = 1 / 0
except ZeroDivisionError as e:
    print(e)

try:
    x = 1
finally:
    print('finally')

print('3.')
print('The above code is legal.')

print('4.')
print("Using the Except handler we can catch exception classes "
      "which are derived from the BaseException class"
      "- itself or its children.\n"
      "Also, it is not recommended to use a bare 'Except:' statement.")

print('5.')
print("Using a bare except: statement in Python is not recommended because it catches all exceptions, "
      "including system-exiting ones like SystemExit and KeyboardInterrupt, "
      "which can obscure specific errors and make debugging difficult. "
      "It leads to less maintainable code by handling all exceptions in the same way, "
      "potentially hiding bugs and making the code harder to understand and correctly modify.")

print('6.')
print("The IOError exception in Python is used to catch input/output-related errors, "
      "such as failing to read or write to a file, "
      "typically due to the file not being accessible or not existing. "
      "In Python 3, IOError has been merged with OSError and is essentially an alias for OSError, "
      "meaning it can catch a range of errors related to system operations, "
      "including but not limited to file I/O errors.")

print("The except ZeroDivisionError specifically catches the ZeroDivisionError exception, "
      "which occurs when a division or modulo operation is attempted with zero as the divisor. "
      "There are no subtypes or additional exceptions directly related to ZeroDivisionError; "
      "it is a standalone exception type that handles this specific case of "
      "attempting to divide by zero in a mathematical operation.")

print('7.')
with open('words.txt', 'w+', encoding='utf-8') as words_file:
    print("file opened successfully for writing/creating.")
    words_file.write("Luba Ira\n")
    words_file.write("מנסה לכתוב בעברית")
with open('words.txt', 'r', encoding='utf-8') as words_file:
    print("file opened successfully for reading.")
    words = words_file.read()
print(words)


# Create a new image with RGB mode
image = Image.new("RGB", (width, height))

# Populate the image with random pixel colors
for x in range(width):
    for y in range(height):
        # Generate a random color
        rand_color = (random.randint(0, 255),  # Red component
                      random.randint(0, 255),  # Green component
                      random.randint(0, 255))  # Blue component
        # Set the pixel to the random color
        image.putpixel((x, y), rand_color)

# Display the image
image.show()

# Save the image to a file
image.save("random_image.png")

print("Image displayed and saved as random_image.png")
