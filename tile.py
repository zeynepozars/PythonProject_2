import stddraw # the stddraw module is used as a basic graphics library
from color import Color # used for coloring the tile and the number on it
from point import Point # used for representing the position of the tile
import copy as cp # the copy module is used for copying tile positions
import random
import math # math module that provides mathematical functions

# Class used for representing numbered tiles as in 2048
class Tile: 
   # Class attributes shared among all Tile objects
   # ---------------------------------------------------------------------------
   # value used for the thickness of the boxes (boundaries) around the tiles
   boundary_thickness = 0.004
   # font family and size used for displaying the tile number
   font_family, font_size = "Arial", 14

   # Constructor that creates a tile at a given position with 2 or 4 as its number
   def __init__(self, position = Point(0, 0)): # (0, 0) is the default position
      rand_num = [2,4]
      # assign the number on the tile
      self.number = random.choice(rand_num)
      # set the colors of the tile
      self.background_color = Color(151, 178, 199) # background (tile) color
      self.foreground_color = Color(0, 100, 200) # foreground (number) color
      self.boundary_color = Color(0, 100, 200) # boundary (box) color
      # set the position of the tile as the given position
      self.position = Point(position.x, position.y)

   # Setter method for the position of the tile
   def set_position(self, position):
      # set the position of the tile as the given position
      self.position = cp.copy(position) 

   # Getter method for the position of the tile
   def get_position(self):
      # return the position of the tile
      return cp.copy(self.position) 
   
   # Setter method for the color of the each tile value
   def set_color(self):
     if self.number == 4:
        self.background_color = Color(238, 225, 201)
     else:
      self.foreground_color = Color(255, 255, 255)  # foreground (number) color
      if self.number == 8:
        self.background_color = Color(243, 178, 122) # background (tile) color
      elif self.number == 16:
        self.background_color = Color(246, 150, 100)  # background (tile) color
      elif self.number == 32:
        self.background_color = Color(247, 124, 95)  # background (tile) color
      elif self.number == 64:
        self.background_color = Color(247, 95, 59)  # background (tile) color
      elif self.number == 128:
        self.background_color = Color(237, 208, 115)  # background (tile) color
      elif self.number == 256:
        self.background_color = Color(237, 204, 98)
      elif self.number == 512:
        self.background_color = Color(238, 199, 82)
      elif self.number == 1024:
        self.background_color = Color(238, 199, 66)
      elif self.number == 2048:
        self.background_color = Color(239, 194, 46)
      else: # after 2048
        self.background_color = Color(60,59,50)


   # Method for moving the tile by dx along the x axis and by dy along the y axis
   def move(self, dx, dy):
      self.position.translate(dx, dy)

   # Method for drawing the tile
   def draw(self):
      # draw the tile as a filled square
      stddraw.setPenColor(self.background_color)
      stddraw.filledSquare(self.position.x, self.position.y, 0.5)
      # draw the bounding box of the tile as a square
      stddraw.setPenColor(self.boundary_color)
      stddraw.setPenRadius(Tile.boundary_thickness)
      stddraw.square(self.position.x, self.position.y, 0.5)
      stddraw.setPenRadius()  # reset the pen radius to its default value
      # draw the number on the tile
      stddraw.setPenColor(self.foreground_color)
      stddraw.setFontFamily(Tile.font_family)
      stddraw.setFontSize(Tile.font_size)
      stddraw.boldText(self.position.x, self.position.y, str(self.number))
      
      # Method for drawing next tetromino's tiles
   def draw_next(self):
      # draw the tile as a filled square
      stddraw.setPenColor(self.background_color)
      stddraw.filledSquare(self.position.x+12.2, self.position.y-10, 0.5)
      # draw the bounding box of the tile as a square
      stddraw.setPenColor(self.boundary_color)
      stddraw.setPenRadius(Tile.boundary_thickness)
      stddraw.square(self.position.x+12.2, self.position.y-10, 0.5)
      stddraw.setPenRadius()  # reset the pen radius to its default value
      # draw the number on the tile
      stddraw.setPenColor(self.foreground_color)
      stddraw.setFontFamily(Tile.font_family)
      stddraw.setFontSize(Tile.font_size)
      stddraw.boldText(self.position.x+12.2, self.position.y-10, str(self.number))

      
