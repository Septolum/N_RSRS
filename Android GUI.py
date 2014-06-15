import android
droid = android.Android()
from modules import *
import os
from time import sleep
import sys

ok = "Ok"

def NYI():
	droid.dialogCreateAlert("Sorry", "That feature is not yet implemented :(")
	droid.dialogSetNeutralButtonText(ok)
	droid.dialogShow()
	response=droid.dialogGetResponse().result
	droid.dialogDismiss()

droid.dialogCreateAlert("Welcome to", "Nat's Recipe Storage & Retrieval System\n\nWritten in Python")
droid.dialogSetNeutralButtonText(ok)
droid.dialogShow()
response=droid.dialogGetResponse().result
droid.dialogDismiss()
print response

def top_menu():
	headers = ["Title: ", "Ingredients: \n", "Equipment: \n", "Preparation Time: \n", "Cooking Time: \n", "Method: \n", "Tags: \n"]
	droid.dialogCreateAlert("What would you like to do?")
	droid.dialogSetItems(("Read", "Write", "Edit", "Search", "Delete", "Exit"))
	droid.dialogShow()
	response=droid.dialogGetResponse().result
	droid.dialogDismiss()
	print response

	if response == {u'item' : 0}:
		droid.dialogCreateAlert("Valid Recipes: ")
		items = []
		for item in os.listdir("./Recipes"):
			items.append(item[0:-4])
		droid.dialogSetItems(items)
		droid.dialogShow()
		response=droid.dialogGetResponse().result
		print response
		droid.dialogDismiss()
		droid.dialogCreateAlert("Recipe:", read_recipe(items[int(str(response)[10:-1])])[0:-2])
		droid.dialogSetNeutralButtonText(ok)
		droid.dialogShow()
		response=droid.dialogGetResponse().result
		print response
		droid.dialogDismiss()
		top_menu()

	if response == {u'item' : 1}:
		for i in [0,1,2,3,4,5,6]:
			droid.dialogGetInput("Write", ((headers[i])[0:-1] + " (type '\\n' for a new line)"))
			if str(droid.dialogGetResponse().result)[13:21] != "positive":
				droid.dialogDismiss()
				top_menu()
			else:
				headers[i] = str(droid.dialogGetResponse().result)[36:-2]
				print headers[i]
			droid.dialogDismiss()
		droid.dialogGetInput("Write", "Filename")
		if str(droid.dialogGetResponse().result)[13:21] != "positive":
			droid.dialogDismiss()
			top_menu()
		else:
			filename = str(droid.dialogGetResponse().result)[36:-2]
		droid.dialogDismiss()
		droid.CreateAlert("Saving...")
		write_recipe(headers[0], headers[1], headers[2], headers[3], headers[4], headers[5], headers[6], filename)
#		print (headers[0], headers[1], headers[2], headers[3], headers[4], headers[5], headers[6], filename)
		droid.dialogDismiss()
		droid.dialogCreateAlert("Saved") 
		droid.dialogSetNeutralButtonText(ok)
		droid.dialogShow()
		response=droid.dialogGetResponse().result
		droid.dialogDismiss()
		top_menu()

	if response == {u'item' : 2}:
		droid.dialogCreateAlert("Valid Recipes: ")
		items = []
		for item in os.listdir("./Recipes"):
			items.append(item[0:-4])
		droid.dialogSetItems(items)
		droid.dialogShow()
		response=droid.dialogGetResponse().result
		print response
		droid.dialogDismiss()
		list = edit_recipe(items[int(str(response)[10:-1])])
		print list
		for i in [0,1,2,3,4,5,6]:
			droid.dialogGetInput("Edit", ((headers[i])[0:-1] + " (type '\\n' for a new line)"), list[i])
			if str(droid.dialogGetResponse().result)[13:21] != "positive":
				droid.dialogDismiss()
				top_menu()
			else:
				list[i] = str(droid.dialogGetResponse().result)[36:-2]
				print list[i]
			droid.dialogDismiss()
		filename = (items[int(str(response)[10:-1])])
		droid.dialogDismiss()
		droid.dialogCreateAlert("Saving...")
		droid.dialogShow()
		write_recipe(list[0], list[1], list[2], list[3], list[4], list[5], list[6], filename)
#		print (list[0], list[1], list[2], list[3], list[4], list[5], list[6], filename)
		droid.dialogDismiss()
		droid.dialogCreateAlert("Saved") 
		droid.dialogSetNeutralButtonText(ok)
		droid.dialogShow()
		response=droid.dialogGetResponse().result
		droid.dialogDismiss()
		top_menu()

	if response == {u'item' : 3}:
		NYI()
		top_menu()

	if response == {u'item' : 4}:
		NYI()
		top_menu()

	if response == {u'item' : 5} or response == {u'canceled' : True}:
		droid.makeToast("Bye! :)")
		sys.exit()

top_menu()
