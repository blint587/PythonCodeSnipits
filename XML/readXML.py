__author__ = 'Balint'

import xml.etree.ElementTree as ET

with open("Variables.xml") as myfile:
    data="".join(line.rstrip() for line in myfile)

root = ET.fromstring(data)

for node in root.findall(".//Unit[@Name='Influent']/Variables/Variable"):
    print node.attrib['Name']


