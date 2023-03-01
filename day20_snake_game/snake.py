"""This module contains the Snake class."""
from tkinter import RIGHT
from turtle import Turtle

STARTING_POSITION  = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20

UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

class Snake:
    """A class to represent a snake."""
    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]

    def create_snake(self):
        """Create a snake."""
        for position in STARTING_POSITION:
            self.add_segment(position)

    def add_segment(self, position):
        """Add a new segment to the snake."""
        new_segment = Turtle(shape="square")
        new_segment.color('white')
        new_segment.penup()
        new_segment.goto(position)
        self.segments.append(new_segment)

    def extend(self):
        """Add a new segment to the snake."""
        self.add_segment(self.segments[-1].position())

    def move(self):
        """Move the snake forward by 20 pixels."""
        for seg_num in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[seg_num - 1].xcor()
            new_y = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(new_x, new_y)
        self.head.forward(MOVE_DISTANCE)

    def up(self):
        """Move the snake up."""
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        """Move the snake down."""
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        """Move the snake left."""
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        """Move the snake right."""
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)
        