import elementtree.ElementTree as ET
root = ET.Element("root")
title = ET.SubElement(root, "title")
title.text = "Hello World"
ingredients = ET.SubElement(root, "ingredients")
ingredients.text = " Some time\n An Idea\n And Some Willing"
equipment = ET.SubElement(root, "equipment")
equipment.text = " A computer\n Reference Material\n Food"
method = ET.SubElement(root, "method")
method.text = "Add all ingredients and mix thoroughly"
tags = ET.SubElement(root, "tags")
tags.text = "Programming Python Laptop"

xml = ET.ElementTree(root)
xml.write("xmltest.xml")