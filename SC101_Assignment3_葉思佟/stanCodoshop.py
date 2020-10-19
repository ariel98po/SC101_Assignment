"""
File: stanCodoshop.py
----------------------------------------------
SC101_Assignment3
Adapted from Nick Parlante's
Ghost assignment by Jerry Liao.

-----------------------------------------------

TODO:
"""

import os
import sys
from simpleimage import SimpleImage


def get_pixel_dist(pixel, red, green, blue):
    """
    Returns the color distance between pixel and mean RGB value

    Input:
        pixel (Pixel): pixel with RGB values to be compared
        red (int): average red value across all images
        green (int): average green value across all images
        blue (int): average blue value across all images

    Returns:
        dist (int): color distance between red, green, and blue pixel values

    """

    color_distance = ((red-pixel.red)**2 + (green-pixel.green)**2 + (blue-pixel.blue)**2) ** 0.5
    return color_distance


def get_average(pixels):
    """
    Given a list of pixels, finds the average red, blue, and green values

    Input:
        pixels (List[Pixel]): list of pixels to be averaged
    Returns:
        rgb (List[int]): list of average red, green, blue values across pixels respectively

    Assumes you are returning in the order: [red, green, blue]

    """


    total_red = 0
    total_green = 0
    total_blue = 0
    average = []

    for pixel in pixels:
        total_red += pixel.red
        total_green += pixel.green
        total_blue += pixel.blue

    red = total_red//len(pixels)
    green = total_green// len(pixels)
    blue = total_blue// len(pixels)
    average = [red, green, blue]

    return average





def get_best_pixel(pixels):
    """
    Given a list of pixels, returns the pixel with the smallest
    distance from the average red, green, and blue values across all pixels.

    Input:
        pixels (List[Pixel]): list of pixels to be averaged and compared
    Returns:
        best (Pixel): pixel closest to RGB averages

    """

    # We have to use get_average function to find RGB averages
    red = get_average(pixels)[0]
    green = get_average(pixels)[1]
    blue = get_average(pixels)[2]
    color_distance = []
    best_distance = 0

    for pixel in pixels:

        color_distance = get_pixel_dist(pixel, red, green, blue)

        if best_distance == 0:
            best_distance = color_distance
            best_pixel = pixel

        elif color_distance < best_distance:
            best_distance = color_distance
            best_pixel = pixel

        else:
            best_distance = best_distance
            best_pixel = best_pixel

    return best_pixel





def solve(images):
    """
    Given a list of image objects, compute and display a Ghost solution image
    based on these images. There will be at least 3 images and they will all
    be the same size.

    Input:
        images (List[SimpleImage]): list of images to be processed
    """
    width = images[0].width
    height = images[0].height
    result = SimpleImage.blank(width, height)
    ######## YOUR CODE STARTS HERE #########
    # Write code to populate image and create the 'ghost' effect



    for x in range(width):
        for y in range(height):
            # Empty the list for different (x,y)
            pixels = []

            for image in images:
                # If the length of pixels is less than Number of pictures,
                # we do not want it to process the rest of work.
                if len(pixels) < len(images) - 1:
                    pixels.append(image.get_pixel(x, y))

                # Add the last pixel to the list and process the rest of work.
                else:
                    pixels.append(image.get_pixel(x, y))
                    best_pixel = get_best_pixel(pixels)
                    result_pixel = result.get_pixel(x, y)
                    result_pixel.red = best_pixel.red
                    result_pixel.green = best_pixel.green
                    result_pixel.blue = best_pixel.blue

    ######## YOUR CODE ENDS HERE ###########
    print("Displaying image!")
    result.show()


def jpgs_in_dir(dir):
    """
    (provided, DO NOT MODIFY)
    Given the name of a directory, returns a list of the .jpg filenames
    within it.

    Input:
        dir (string): name of directory
    Returns:
        filenames(List[string]): names of jpg files in directory
    """
    filenames = []
    for filename in os.listdir(dir):
        if filename.endswith('.jpg'):
            filenames.append(os.path.join(dir, filename))
    return filenames


def load_images(dir):
    """
    (provided, DO NOT MODIFY)
    Given a directory name, reads all the .jpg files within it into memory and
    returns them in a list. Prints the filenames out as it goes.

    Input:
        dir (string): name of directory
    Returns:
        images (List[SimpleImages]): list of images in directory
    """
    images = []
    jpgs = jpgs_in_dir(dir)
    for filename in jpgs:
        print("Loading", filename)
        image = SimpleImage(filename)
        images.append(image)
    return images


def main():
    # (provided, DO NOT MODIFY)
    args = sys.argv[1:]
    # We just take 1 argument, the folder containing all the images.
    # The load_images() capability is provided above.
    images = load_images(args[0])
    solve(images)


if __name__ == '__main__':
    main()
