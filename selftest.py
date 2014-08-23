from modules import *

title_text = "Hello World"
ingredients_text = " Some time\n An Idea\n And Some Willing"
equipment_text = " A computer\n Reference Material\n Food"
prep_time_text = " Until Stable"
cook_time_text = " Until Perfect (Indefinitely then...)" 
method_text = "Add all ingredients and mix thoroughly"
tags_text = "Programming Python Laptop"
filename = "selftest"

write_recipe(title_text, ingredients_text, equipment_text, prep_time_text, cook_time_text, method_text, tags_text, filename)

print read_recipe(filename)