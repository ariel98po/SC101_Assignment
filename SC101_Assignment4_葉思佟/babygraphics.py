"""
SC101 Baby Names Project
Adapted from Nick Parlante's Baby Names assignment by
Jerry Liao.

This program gives out the rank and show the popularity of the baby name from 1900s-2010s.
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

    x_coordinate = GRAPH_MARGIN_SIZE + year_index * ((width - 2*GRAPH_MARGIN_SIZE)/len(YEARS))
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

    canvas.create_line(GRAPH_MARGIN_SIZE, GRAPH_MARGIN_SIZE, CANVAS_WIDTH-GRAPH_MARGIN_SIZE, GRAPH_MARGIN_SIZE,
                       width=LINE_WIDTH, fill='black')
    canvas.create_line(GRAPH_MARGIN_SIZE, CANVAS_HEIGHT-GRAPH_MARGIN_SIZE, CANVAS_WIDTH-GRAPH_MARGIN_SIZE,
                       CANVAS_HEIGHT-GRAPH_MARGIN_SIZE, width=LINE_WIDTH, fill='black')


    for i in range(len(YEARS)):
        canvas.create_line(get_x_coordinate(CANVAS_WIDTH, i), 0, get_x_coordinate(CANVAS_WIDTH, i), CANVAS_HEIGHT,
                           width=LINE_WIDTH, fill='black')
        canvas.create_text(TEXT_DX + get_x_coordinate(CANVAS_WIDTH, i), CANVAS_HEIGHT-GRAPH_MARGIN_SIZE,
                           text=YEARS[i], anchor=tkinter.NW, fill='black', font='times 10')




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

    y_rank_gap = (CANVAS_HEIGHT-2*GRAPH_MARGIN_SIZE) / (MAX_RANK-1) # The gap of each rank at y coordinate

    for x in range(len(lookup_names)):
        if lookup_names[x] in name_data:
            for year in YEARS:
                # If the rank of the name < 1000, this year has data and is in the dict
                # Key is a string in the dict

                # If the rank of the name > 1000, we do not have data of this year in the dict
                # y coordinate is CANVAS_HEIGHT - GRAPH_MARGIN_SIZE

                if str(year) in name_data[lookup_names[x]]:
                    # The rank of the name < 1000

                    i = YEARS.index(year)
                    if i == len(YEARS) - 1: # The last year only need the text, no line.
                        canvas.create_text(TEXT_DX + get_x_coordinate(CANVAS_WIDTH, i),
                                           GRAPH_MARGIN_SIZE + (int(name_data[lookup_names[x]][str(YEARS[i])]) - 1) * y_rank_gap,
                                           text=lookup_names[x] + ' ' + name_data[lookup_names[x]][str(YEARS[i])],
                                           anchor=tkinter.SW, fill=COLORS[x % 4], font='times 10')

                    elif str(YEARS[i+1]) not in name_data[lookup_names[x]]: # The rank of Year[i+1] is > 1000
                        canvas.create_line(get_x_coordinate(CANVAS_WIDTH, i),
                                           GRAPH_MARGIN_SIZE + (int(name_data[lookup_names[x]][str(YEARS[i])]) - 1) * y_rank_gap ,
                                           get_x_coordinate(CANVAS_WIDTH, i + 1),
                                           CANVAS_HEIGHT - GRAPH_MARGIN_SIZE,
                                           width=LINE_WIDTH, fill=COLORS[x % 4])

                        canvas.create_text(TEXT_DX + get_x_coordinate(CANVAS_WIDTH, i),
                                           GRAPH_MARGIN_SIZE + (int(name_data[lookup_names[x]][str(YEARS[i])]) - 1) * y_rank_gap,
                                           text=lookup_names[x] + ' ' + name_data[lookup_names[x]][str(YEARS[i])],
                                           anchor=tkinter.SW, fill=COLORS[x % 4], font='times 10')

                    else:
                        canvas.create_line(get_x_coordinate(CANVAS_WIDTH, i),
                                           GRAPH_MARGIN_SIZE + (int(name_data[lookup_names[x]][str(YEARS[i])]) - 1) * y_rank_gap,
                                           get_x_coordinate(CANVAS_WIDTH, i+1),
                                           GRAPH_MARGIN_SIZE + (int(name_data[lookup_names[x]][str(YEARS[i+1])])-1) * y_rank_gap,
                                           width=LINE_WIDTH, fill=COLORS[x % 4])

                        canvas.create_text(TEXT_DX + get_x_coordinate(CANVAS_WIDTH, i),
                                               GRAPH_MARGIN_SIZE + (int(name_data[lookup_names[x]][str(YEARS[i])]) - 1) * y_rank_gap,
                                               text=lookup_names[x] + ' ' + name_data[lookup_names[x]][str(YEARS[i])],
                                               anchor=tkinter.SW, fill=COLORS[x % 4], font='times 10')


                else:
                    # The rank of the name > 1000

                    i = YEARS.index(year)
                    if i == len(YEARS) - 1: # The last year only need the text, no line.
                        canvas.create_text(TEXT_DX + get_x_coordinate(CANVAS_WIDTH, i),
                                           CANVAS_HEIGHT - GRAPH_MARGIN_SIZE,
                                           text=lookup_names[x] + ' *', anchor=tkinter.SW, fill=COLORS[x % 4],
                                           font='times 10')

                    elif str(YEARS[i+1]) in name_data[lookup_names[x]]: # The rank of Year[i+1] is < 1000
                        canvas.create_line(get_x_coordinate(CANVAS_WIDTH, i), CANVAS_HEIGHT - GRAPH_MARGIN_SIZE,
                                           get_x_coordinate(CANVAS_WIDTH, i + 1),
                                           GRAPH_MARGIN_SIZE + (int(name_data[lookup_names[x]][str(YEARS[i+1])])-1) * y_rank_gap,
                                           width=LINE_WIDTH, fill=COLORS[x % 4])
                        canvas.create_text(TEXT_DX + get_x_coordinate(CANVAS_WIDTH, i),
                                           CANVAS_HEIGHT - GRAPH_MARGIN_SIZE,
                                           text=lookup_names[x] + ' *', anchor=tkinter.SW, fill=COLORS[x % 4],
                                           font='times 10')


                    else:
                        # The rank of the name in Year[i] and Year[i+1] are both > 1000, horizontal line
                        canvas.create_line(get_x_coordinate(CANVAS_WIDTH, i), CANVAS_HEIGHT - GRAPH_MARGIN_SIZE,
                                           get_x_coordinate(CANVAS_WIDTH, i+1), CANVAS_HEIGHT-GRAPH_MARGIN_SIZE,
                                           width=LINE_WIDTH, fill=COLORS[x % 4])
                        canvas.create_text(TEXT_DX + get_x_coordinate(CANVAS_WIDTH, i), CANVAS_HEIGHT-GRAPH_MARGIN_SIZE,
                                           text=lookup_names[x] + ' *', anchor=tkinter.SW, fill=COLORS[x % 4], font='times 10')



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
