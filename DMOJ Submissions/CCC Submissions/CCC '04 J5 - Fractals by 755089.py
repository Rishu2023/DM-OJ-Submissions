#-----------------------------------------------------------------------------
# Name:  CCC '04 J5 - Fractals (main.py)
# Author:      Aryan Mittal
# Created:     18-Feb-2024
# Updated:     18-Feb-2024
#---------------------------------------------------------------------------
# Reads inputs: level, width, and x-coordinate to check
level, width, check = map(int, input().split())

# Initializes list of fractals with initial block fractal
fractals = [(0, width, 1, 1, 1)]

# Generates fractals up to given level
for _ in range(level):
    new_fractals = []
    # Iterates through fractals and generate new ones based on their lines
    for fractal in fractals:
        start_x, end_x, start_y, end_y, direction = fractal
        # If the is horizontal
        if start_y == end_y:
            # Calculate new width
            new_width = abs(start_x - end_x) // 3
            # Generate new X lines
            new_fractals.append((start_x, start_x + new_width, start_y, end_y, direction))
            new_fractals.append((end_x - new_width, end_x, start_y, end_y, direction))
            new_fractals.append((start_x + new_width, end_x - new_width, start_y + direction * new_width, start_y + direction * new_width, direction))
            # Generate new Y lines
            new_start_y, new_end_y = sorted((start_y + direction * new_width, end_y))
            new_fractals.append((start_x + new_width, start_x + new_width, new_start_y, new_end_y, -1))
            new_fractals.append((end_x - new_width, end_x - new_width, new_start_y, new_end_y, 1))
        # If the line is vertical
        else:
            # Calculate new width
            new_width = abs(start_y - end_y) // 3
            # Generate new Y lines
            new_fractals.append((start_x, end_x, start_y, start_y + new_width, direction))
            new_fractals.append((start_x, end_x, end_y - new_width, end_y, direction))
            new_fractals.append((start_x + direction * new_width, start_x + direction * new_width, start_y + new_width, end_y - new_width, direction))
            # Generate new X lines
            new_start_x, new_end_x = sorted((start_x + direction * new_width, end_x))
            new_fractals.append((new_start_x, new_end_x, start_y + new_width, start_y + new_width, -1))
            new_fractals.append((new_start_x, new_end_x, end_y - new_width, end_y - new_width, 1))
    fractals = new_fractals[::]

# Initializes set to store y-coordinates of intersecting lines
answers = set()

# Iterates through all generated fractals
for fractal in fractals:
    start_x, end_x, start_y, end_y, _ = fractal
    # If x-coordinate to check falls within fractal's x-range
    if start_x <= check <= end_x:
        # Add all y-coordinates within fractal's y-range to answers set
        for y in range(start_y, end_y + 1):
            answers.add(y)

# Prints sorted list of intersecting y-coordinates
print(*sorted(answers))