"""CLUE Spirit Level Demo"""
import board
from adafruit_clue import clue
from adafruit_display_shapes.circle import Circle
import displayio

display = board.DISPLAY
group = displayio.Group(max_size=4)

outer_circle = Circle(120, 120, 119, outline=clue.WHITE)
middle_circle = Circle(120, 120, 75, outline=clue.YELLOW)
inner_circle = Circle(120, 120, 35, outline=clue.GREEN)
group.append(outer_circle)
group.append(middle_circle)
group.append(inner_circle)

x, y, _ = clue.acceleration
bubble_group = displayio.Group(max_size=1)
level_bubble = Circle(int(x + 120), int(y + 120), 20, fill=clue.RED, outline=clue.RED)
bubble_group.append(level_bubble)

group.append(bubble_group)
display.show(group)

while True:
    x, y, _ = clue.acceleration
    bubble_group.x = int(x * 10)
    bubble_group.y = int(y * 10)
