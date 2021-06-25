"""
File: blur.py
Name: 洪禎蔚
-------------------------------
This file shows the original image first,
smiley-face.png, and then compare to its
blurred image. The blur algorithm uses the
average RGB values of a pixel's nearest neighbors
"""

from simpleimage import SimpleImage


def blur(img):
    """
    :param img: img, pre-blurred image
    :return: img, post-blurred image
    """
    new_img = SimpleImage.blank(img.width, img.height)
    for x in range(img.width):
        for y in range(img.height):
            pixel = new_img.get_pixel(x, y)
            total_red = 0
            total_blue = 0
            total_green = 0
            total_num = 0
            if x == 0:
                left_limit = x
            else:
                left_limit = x - 1
            if y == 0:
                top_limit = y
            else:
                top_limit = y - 1
            if x == img.width - 1:
                right_limit = x
            else:
                right_limit = x + 1
            if y == img.height - 1:
                bottom_limit = y
            else:
                bottom_limit = y + 1
            # each pixel
            for w in range(left_limit, right_limit + 1):
                for h in range(top_limit, bottom_limit + 1):
                    # count the total RGB values of each pixel according to their limits
                    total_red += img.get_pixel(w, h).red
                    total_blue += img.get_pixel(w, h).blue
                    total_green += img.get_pixel(w, h).green
                    # the number of their neighbor
                    total_num += 1
            pixel.red = total_red / total_num
            pixel.green = total_green / total_num
            pixel.blue = total_blue / total_num
    return new_img


def main():
    """
    TODO: To blur the image 5 times...
    """
    old_img = SimpleImage("images/smiley-face.png")
    old_img.show()

    blurred_img = blur(old_img)
    for i in range(5):
        blurred_img = blur(blurred_img)
    blurred_img.show()


if __name__ == '__main__':
    main()
