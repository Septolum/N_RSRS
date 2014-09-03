import elementtree.ElementTree as ET
import os
def indent(elem, level=0):
    i = "\n" + level*"  "
    if len(elem):
        if not elem.text or not elem.text.strip():
            elem.text = i + "  "
        if not elem.tail or not elem.tail.strip():
            elem.tail = i
        for elem in elem:
            indent(elem, level+1)
        if not elem.tail or not elem.tail.strip():
            elem.tail = i
    else:
        if level and (not elem.tail or not elem.tail.strip()):
            elem.tail = i

headers = ["Title: ", "Ingredients: \n", "Equipment: \n", "Preparation Time: \n", "Cooking Time: \n", "Method: \n", "Tags: \n"]
	
def write_recipe(title_text, ingredients_text, equipment_text, prep_time_text, cook_time_text, method_text, tags_text, filename):
	"Arguments: title_text, ingredients_text, equipment_text, method_text, tags_text, filename"
	root = ET.Element("root")
	title = ET.SubElement(root, "title")
	title.text = title_text
	ingredients = ET.SubElement(root, "ingredients")
	ingredients.text = ingredients_text
	equipment = ET.SubElement(root, "equipment")
	equipment.text = equipment_text
	prep_time = ET.SubElement(root, "prep_time")
	prep_time.text = prep_time_text
	cook_time = ET.SubElement(root, "cook_time")
	cook_time.text = cook_time_text
	method = ET.SubElement(root, "method")
	method.text = method_text
	tags = ET.SubElement(root, "tags")
	tags.text = tags_text
	
	indent(root)
	
	xml = ET.ElementTree(root)
	xml.write("./Recipes/" + filename + ".xml")

def read_recipe(filename):
	"Prints file and imports it as current tree"
	root = ET.ElementTree(file=("./Recipes/" + filename + ".xml"))
	elem = root.getroot()
	indent(elem)
#	print
#	for node in elem:
#		print node
#		print node.text
#		print
# ^ Debug Stuff	
	retur = ""
	for i in [0,1,2,3,4,5,6]:
		retur += headers[i] + elem[i].text
		retur += "\n\n"
	return retur

def edit_recipe(filename):
	root = ET.ElementTree(file=("./Recipes/" + filename + ".xml"))
	elem = root.getroot()
	indent(elem)
	list = []
	for i in [0,1,2,3,4,5,6]:
		list.append(elem[i].text)
	return list
def search_recipes(string, header_index):
	item_list = []
	for item in range(len(os.listdir("./Recipes"))):
		root = ET.ElementTree(file=("./Recipes/" + os.listdir("./Recipes")[item]))
		elem = root.getroot()
		indent(elem)
		print string, "in", elem[header_index].text
		if (string.lower() in elem[header_index].text.lower()) == True:
			item_list.append(str(os.listdir("./Recipes")[item])[0:-4])
	return item_list

def get_recipe_dir():
	return os.getcwd().replace('\\', '/') + "/Recipes/"