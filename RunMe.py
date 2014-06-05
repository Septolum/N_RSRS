import sys
if sys.version_info>(2,8,0):
  sys.stderr.write("I won't work with this version of Python. Try using Python 2.7\n")
  exit(1)

from modules import *
import os
import colorama as ca
ca.init()

def top_response():
	response = raw_input("What would you like to do? (Read, Write, Edit or Search)\n" + ca.Fore.RESET).lower()
	print ca.Fore.CYAN
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
		print (ca.Fore.RED + "Not yet Implemented\n" + ca.Fore.CYAN)
		top_response()
	
	if response == "search" or response =="s":
		#print
		#search_response()
		print (ca.Fore.RED + "Not yet Implemented\n" + ca.Fore.CYAN)
		top_response()
	
	else:
		print (ca.Fore.RED + "Please enter a valid response\n" + ca.Fore.CYAN)
		top_response()

def read_response():
	print "Valid recipes: "
	for item in os.listdir("./Recipes"):
		print (ca.Fore.RESET + item[:-4])
	print ca.Fore.CYAN
	file = raw_input("Which Recipe would you like to read?\n" + ca.Fore.RESET)
	print ca.Fore.CYAN
	if (file + ".xml") in os.listdir("./Recipes"):
		print ca.Fore.RESET
		read_recipe(file)
		print ca.Fore.CYAN
	else:
		print (ca.Fore.RED + "That file does not exist.\n" + ca.Fore.CYAN)
	top_response()

def write_response():
	title_text = raw_input("What is the recipe's title?\n" + ca.Fore.RESET)
	print ca.Fore.CYAN
	ingredients_text = raw_input("What is the recipe's ingredients? (Make an new line with \"\\n\")\n" + ca.Fore.RESET)
	print ca.Fore.CYAN
	equipment_text = raw_input("What equipment is needed? (Make an new line with \"\\n\")\n" + ca.Fore.RESET)
	print ca.Fore.CYAN
	prep_time_text = raw_input("How long will it take to prepare it?\n" + ca.Fore.RESET)
	print ca.Fore.CYAN
	cook_time_text = raw_input("How long will it take to cook?\n" + ca.Fore.RESET)
	print ca.Fore.CYAN
	method_text = raw_input("What is the method? (Make an new line with \"\\n\")\n" + ca.Fore.RESET)
	print ca.Fore.CYAN
	tags_text = raw_input("What tags would you like to add? (Separate with spaces, used for searching, include things such as country of origin, author, season, etc...)\n" + ca.Fore.RESET)
	print ca.Fore.CYAN
	filename = raw_input("What filename do you want to give the recipe? (The file extension will automatically be added)\n" + ca.Fore.RESET)
	print ca.Fore.CYAN
	print "Saving file..."
	write_recipe(title_text, ingredients_text, equipment_text, prep_time_text, cook_time_text, method_text, tags_text, filename)
	print "File saved."
	print
	top_response()

print (ca.Fore.CYAN + ca.Back.BLUE + ca.Style.BRIGHT + """
+-----------------------------------------+
|                                         |
|          |\  |  /  _    _  \ 2          |
|          | \ | |  |_|  |_   |           |
|          |  \|  \ | \   _| /            |
|                                         |
| Nat's Recipe Storage & Retrieval System |
+-----------------------------------------+
""")
print (ca.Back.RESET + ca.Fore.RESET + "Welcome to Nat's Recipe Storage & Retrieval System\n\nWritten in Python using the ElementTrees module for handling XML\nColours by " + ca.Fore.RED + "C" + ca.Fore.BLUE + "o" + ca.Fore.GREEN + "l" + ca.Fore.YELLOW + "o" + ca.Fore.MAGENTA + "r" + ca.Fore.CYAN + "a" + ca.Fore.RED + "m" + ca.Fore.BLUE + "a")
print ("\n\n" + ca.Fore.CYAN)
top_response()
