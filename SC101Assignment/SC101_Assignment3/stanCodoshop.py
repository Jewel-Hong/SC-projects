"""
File: stanCodoshop.py
Name: 洪禎蔚
----------------------------------------------
SC101_Assignment3
Adapted from Nick Parlante's
Ghost assignment by Jerry Liao.
-----------------------------------------------
TODO: To remove people in the picture by calculate the average of RGB value of each pixel
    and pick the pixel that have the shortest color distance to the average.
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
    dist = ((red-pixel.red)**2 + (green-pixel.green)**2 + (blue-pixel.blue)**2) ** .5
    return dist


def get_average(pixels):
    """
    Given a list of pixels, finds the average red, blue, and green values

    Input:
        pixels (List[Pixel]): list of pixels to be averaged
    Returns:
        rgb (List[int]): list of average red, green, blue values across pixels respectively

    Assumes you are returning in the order: [red, green, blue]

    """
    red_lst = []
    green_lst = []
    blue_lst = []
    rgb = []
    for i in range(len(pixels)):
        red = pixels[i].red
        red_lst.append(red)
        green = pixels[i].green
        green_lst.append(green)
        blue = pixels[i].blue
        blue_lst.append(blue)
    rgb.append(average(red_lst))
    rgb.append(average(green_lst))
    rgb.append(average(blue_lst))
    return rgb


def average(lst):
    """
    To calculate the average of the numbers in the list.
    :param lst (List[int]): a list of numbers
    :return (int): the average
    """
    total = 0
    for i in range(len(lst)):
        total += lst[i]
    return total // len(lst)


def get_best_pixel(pixels):
    """
    Given a list of pixels, returns the pixel with the smallest
    distance from the average red, green, and blue values across all pixels.

    Input:
        pixels (List[Pixel]): list of pixels to be averaged and compared
    Returns:
        best (Pixel): pixel closest to RGB averages

    """
    red = get_average(pixels)[0]
    green = get_average(pixels)[1]
    blue = get_average(pixels)[2]
    base = get_pixel_dist(pixels[0], red, green, blue)
    best = pixels[0]
    for i in range(1, len(pixels)):
        minn = get_pixel_dist(pixels[i], red, green, blue)
        if minn < base:
            base = minn
            best = pixels[i]
    return best


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
    pixels = []
    for i in range(len(images)):
        pixels.append(0)
    for x in range(width):
        for y in range(height):
            r = result.get_pixel(x, y)
            for i in range(len(images)):
                pixels[i] = images[i].get_pixel(x, y)
            r.red = get_best_pixel(pixels).red
            r.green = get_best_pixel(pixels).green
            r.blue = get_best_pixel(pixels).blue
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
