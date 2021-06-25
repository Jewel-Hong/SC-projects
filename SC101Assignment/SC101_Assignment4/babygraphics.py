"""
File: babygraphics.py
Name: 洪禎蔚
-----------------------
SC101 Baby Names Project
Adapted from Nick Parlante's Baby Names assignment by
Jerry Liao.

YOUR DESCRIPTION HERE
"""

import tkinter
import babynames
import babygraphicsgui as gui

FILENAMES = [
    'data/full/baby-1900.txt', 'data/full/baby-1910.txt',
    'data/full/baby-1920.txt', 'data/full/baby-1930.txt',
    'data/full/baby-1940.txt', 'data/full/baby-1950.txt',
    'data/full/baby-1960.txt', 'data/full/baby-1970.txt',
    'data/full/baby-1980.txt', 'data/full/baby-1990.txt',
    'data/full/baby-2000.txt', 'data/full/baby-2010.txt'
]
CANVAS_WIDTH = 1000
CANVAS_HEIGHT = 600
YEARS = [1900, 1910, 1920, 1930, 1940, 1950, 1960, 1970, 1980, 1990, 2000, 2010]
GRAPH_MARGIN_SIZE = 20
COLORS = ['red', 'purple', 'green', 'blue']
TEXT_DX = 2
LINE_WIDTH = 2
MAX_RANK = 1000


def get_x_coordinate(width, year_index):
    """
    Given the width of the canvas and the index of the current year
    in the YEARS list, returns the x coordinate of the vertical
    line associated with that year.

    Input:
        width (int): The width of the canvas
        year_index (int): The index of the current year in the YEARS list
    Returns:
        x_coordinate (int): The x coordinate of the vertical line associated
                              with the specified year.
    """
    interval = (width - 2*GRAPH_MARGIN_SIZE) / len(YEARS)
    x_coordinate = GRAPH_MARGIN_SIZE + year_index * interval
    return x_coordinate


def draw_fixed_lines(canvas):
    """
    Erases all existing information on the given canvas and then
    draws the fixed background lines on it.

    Input:
        canvas (Tkinter Canvas): The canvas on which we are drawing.

    Returns:
        This function does not return any value.
    """
    canvas.delete('all')            # delete all existing lines from the canvas

    # Write your code below this line
    #################################
    w = CANVAS_WIDTH
    h = CANVAS_HEIGHT
    m = GRAPH_MARGIN_SIZE
    canvas.create_line(m, m, w - m, m)
    canvas.create_line(m, h - m, w - m, h - m)


def draw_names(canvas, name_data, lookup_names):
    """
    Given a dict of baby name data and a list of name, plots
    the historical trend of those names onto the canvas.

    Input:
        canvas (Tkinter Canvas): The canvas on which we are drawing.
        name_data (dict): Dictionary holding baby name data
        lookup_names (List[str]): A list of names whose data you want to plot

    Returns:
        This function does not return any value.
    """
    draw_fixed_lines(canvas)        # draw the fixed background grid

    # Write your code below this line
    #################################
    w = CANVAS_WIDTH
    h = CANVAS_HEIGHT
    m = GRAPH_MARGIN_SIZE
    color_n = 0
    y_portion = (h - 2 * m) / 999
    for name in lookup_names:
        d_info = name_data[name]
        y1 = 0
        # Choose the color of the line of this name
        color = COLORS[color_n % 4]
        for i in range(len(YEARS)):
            x1 = get_x_coordinate(w, i - 1)
            x2 = get_x_coordinate(w, i)
            # Draw the vertical line and label the x coordinate with the year
            canvas.create_line(x2, 0, x2, h)
            canvas.create_text(x2 + TEXT_DX, h - m, text=str(YEARS[i]), anchor=tkinter.NW)
            # Label the first rank of the name
            if i == 0:
                if str(YEARS[i]) in d_info:
                    rank = d_info[str(YEARS[i])]
                    y1 = m + (int(rank)-1)*y_portion
                    canvas.create_text(x2 + TEXT_DX, y1, text=f'{name} {rank}', anchor=tkinter.SW)
                else:
                    y1 = CANVAS_HEIGHT-m
                    canvas.create_text(x2 + TEXT_DX, y1, text=f'{name} *', anchor=tkinter.SW)
            # Label the rest ranks of the name and draw lines between the consecutive years
            else:
                if str(YEARS[i]) in d_info:
                    rank = d_info[str(YEARS[i])]
                    y2 = m + (int(rank) - 1) * y_portion
                    canvas.create_text(x2 + TEXT_DX, y2, text=f'{name} {rank}', anchor=tkinter.SW)
                    canvas.create_line(x1, y1, x2, y2, width=LINE_WIDTH, fill=color)
                    y1 = y2
                else:
                    y2 = h - m
                    canvas.create_text(x2 + TEXT_DX, y2, text=f'{name} *', anchor=tkinter.SW)
                    canvas.create_line(x1, y1, x2, y2, width=LINE_WIDTH, fill=color)
                    y1 = y2
        color_n += 1


# main() code is provided, feel free to read through it but DO NOT MODIFY
def main():
    # Load data
    name_data = babynames.read_files(FILENAMES)

    # Create the window and the canvas
    top = tkinter.Tk()
    top.wm_title('Baby Names')
    canvas = gui.make_gui(top, CANVAS_WIDTH, CANVAS_HEIGHT, name_data, draw_names, babynames.search_names)

    # Call draw_fixed_lines() once at startup so we have the lines
    # even before the user types anything.
    draw_fixed_lines(canvas)

    # This line starts the graphical loop that is responsible for
    # processing user interactions and plotting data
    top.mainloop()


if __name__ == '__main__':
    main()
