SIZE = 400
# we will have 4 columns and 4 rows
GRID_LEN = 4
# each cell in grid will have of 10
GRID_PADDING = 10

# background colour of the game
BACKGROUND_COLOR_GAME = "#a6bdbb"

# background colour of an empty cell
BACKGROUND_COLOR_CELL_EMPTY = "#8eaba8"

#back tile color of each cell
BACKGROUND_COLOR_DICT = {2: "#daeddf", 4: "#9ae3ae", 8: "#6ce68d", 16: "#42ed71",
                   32: "#17e650", 64: "#17c246", 128: "#149938",
                   256: "#107d2e", 512: "#0e6325", 1024: "#0b4a1c",
                   2048: "#031f0a", 4096: "#000000", 8192: "#000000",}

#text color for each number
CELL_COLOR_DICT = {2: "#011c08", 4: "#011c08", 8: "#011c08", 16: "#011c08",
                   32: "#011c08", 64: "#f2f2f0", 128: "#f2f2f0",
                   256: "#f2f2f0", 512: "#f2f2f0", 1024: "#f2f2f0",
                   2048: "#f2f2f0", 4096: "#f2f2f0", 8192: "#f2f2f0",}

# font-style , font-size and font-weight
FONT = ("Verdana", 40 , "bold")

# w will be considered as UP, s will be considered as DOWN, a will be considered as left, d will be considered as right
KEY_UP = "'w'"
KEY_DOWN = "'s'"
KEY_LEFT= "'a'"
KEY_RIGHT = "'d'"
