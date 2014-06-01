import sys
if sys.version_info>(2,9,9):
  sys.stderr.write("I won't work with Python 3. Try using Python 2.7\n")
  exit(1)

from modules import *
import os

def top_response():
	response = raw_input("What would you like to do? (Read, Write, Edit or Search)\n").lower()
	
	if response == "read" or response == "r":
		print
		read_response()
	
	if response == "write" or response == "w":
		print
		write_response()
		#print "Not yet Implemented\n"
		#top_response()
	
	if response == "edit" or response == "e":
		#print
		#edit_response()
		print "Not yet Implemented\n"
		top_response()
	
	if response == "search" or response =="s":
		#print
		#search_response()
		print "Not yet Implemented\n"
		top_response()
	
	else:
		print "Please enter a valid response\n"
		top_response()

def read_response():
	print "Valid recipes: "
	for item in os.listdir("./Recipes"):
		print item[:-4]
	print
	file = raw_input("Which Recipe would you like to read?\n").lower()
	print
	read_recipe(file)
	top_response()

def write_response():
	title_text = raw_input("What is the recipe's title?\n")
	print
	ingredients_text = raw_input("What is the recipe's ingredients? (Make an new line with \"\\n\")\n")
	print
	equipment_text = raw_input("What equipment is needed? (Make an new line with \"\\n\")\n")
	print
	prep_time_text = raw_input("How long will it take to prepare it?\n")
	print
	cook_time_text = raw_input("How long will it take to cook?\n")
	print
	method_text = raw_input("What is the method? (Make an new line with \"\\n\")\n")
	print
	tags_text = raw_input("What tags would you like to add? (Separate with spaces, used for searching, include things such as country of origin, author, season, etc...)\n")
	print
	filename = raw_input("What filename do you want to give the recipe? (The file extension will automatically be added)\n")
	print
	print "Saving file..."
	write_recipe(title_text, ingredients_text, equipment_text, prep_time_text, cook_time_text, method_text, tags_text, filename)
	print "File saved."
	print
	top_response()

print """
+-----------------------------------------+
|                                         |
|          |\  |  /  _    _  \ 2          |
|          | \ | |  |_|  |_   |           |
|          |  \|  \ | \   _| /            |
|                                         |
| Nat's Recipe Storage & Retrieval System |
+-----------------------------------------+
"""
print "Welcome to Nat's Recipe Storage & Retrieval System\n\nWritten in Python using the ElementTrees module for handling XML"
print "\n\n"
top_response()