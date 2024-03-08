import time
import board
import neopixel

# Calls the CircuitPython neopixel library, specifies the default board 
# pins for the NeoPixels, and the number of neopixels to access.  Returns a 
# list 'pixels' of indexable neopixels
pixels = neopixel.NeoPixel(board.NEOPIXEL, 10)

# Define a function to generate rainbow colors
def rainbow_color(steps):
    for i in range(steps):
        # Generate rainbow colors across 10 NeoPixels
        for j in range(len(pixels)):
            # Convert rainbow color to RGB values
            color = wheel((i+j) & 255)
            # Set the color of the current NeoPixel
            pixels[j] = color
        # Show the colors on the NeoPixels
        pixels.show()
        # Delay between each color change
        time.sleep(0.05)

# Define a function to generate rainbow colors
def wheel(pos):
    # Input a value 0 to 255 to get a color value.
    # The colours are a transition r - g - b - back to r.
    if pos < 85:
        return (255 - pos * 3, pos * 3, 0)
    elif pos < 170:
        pos -= 85
        return (0, 255 - pos * 3, pos * 3)
    else:
        pos -= 170
        return (pos * 3, 0, 255 - pos * 3)

while True:
    # Call the rainbow_color function to display the rainbow effect
    rainbow_color(255)
 
