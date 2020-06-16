#!/usr/bin/python3
# encoding: utf-8

#{{recipe-name}} found in header
#{{recipe-path}} found in header, more specificity (relates to file)

#{{recipe-ingredients}} speaks for itself, inside a <li></li> block
#{{recipe-steps}}       speaks for itself, inside a <li></li> block

# TODO
# - Currently this just prints out filenames in the ./recipes dir
# Need to
# - Load file contents (if they exist, easy)
# - Interpret variables as described above
# - Load html template files and modify them (replace text)
# - Produce engine for pagination
# - Produce engine for producing recipe cards on homepage (snippet in file)
# - Produce engine for limiting 15 recipe cards to each page
# - Produce engine for listing steps and ingredients with proper <li> tags
# - Make sure all link references work properly
# - Done?

from os import listdir
from os.path import isfile, join

categories = ["Breakfast", "Lunch", "Dinner"]

recipes = [f for f in listdir("recipe") if isfile(join("recipe", f))]

if (len(recipes) < 1):
  print("No recipes found in ./recipe")

for i in range(0, len(recipes)):
  print (recipes[i])
