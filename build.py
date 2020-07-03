#!/usr/bin/python3
# encoding: utf-8

#{{recipe-name}} found in header
#{{recipe-path}} found in header, more specificity (relates to file)

#{{recipe-ingredients}} speaks for itself, inside a <li></li> block
#{{recipe-steps}}       speaks for itself, inside a <li></li> block

# TODO
# Need to
# - Store all recipes before building? Dictionary?
# - Load html template files and modify them (replace text)
# - Produce engine for pagination
# - Produce engine for producing recipe cards Son homepage (snippet in file)
# - Produce engine for limiting 15 recipe cards to each page
# - Produce engine for listing steps and ingredients with proper <li> tags
# - Make sure all link references work properly
# - Done?

from os import listdir
from os.path import isfile, join

def get_contents(filename):
  with open("./recipe/" + filename) as f:
    return f.read()

recipes = [f for f in listdir("recipe") if isfile(join("recipe", f))]

if (len(recipes) < 1):
  print("No recipes found in ./recipe")

for i in range(0, len(recipes)):
  plaintext = get_contents(recipes[i])
  contents = plaintext.split("\n")

  # This section is looking for an asciidoc file structured like this:
  # Header looks like this:     "= [Name]"
  # Ingredients look like this: "* [Name]"
  # Steps look like this:       ". [Name]"

  needsName = True
  needsIngredients = True
  needsSteps = True

  for i in range (0,len(contents)):
    if (contents[i].startswith("= ")):
      contents[i].split("= ")[1]         # The name of the recipe
      needsName = False
    if (contents[i].startswith("* ")):
      contents[i].split("* ")[1]         # An ingredient
      needsIngredients = False
    if (contents[i].startswith(". ")):
      contents[i].split(". ")[1]         # A step in the recipe
      needsSteps = False

  if needsName or needsIngredients or needsSteps:
    print("This isn't a valid recipe!")
    break
