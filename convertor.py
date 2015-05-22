import json


with open("config.json", "r") as fh:
	filecontent = fh.read()
	config = json.loads(filecontent)

buildings = config["buildings"]
reverse_table = {}
for building_type, sub_buildings in buildings.iteritems():
	for building in sub_buildings:
		#print building["name"], [level["res_snapshoot"] for level in building["levels"]]
		for level in building["levels"]:
			reverse_table[level["res_snapshoot"]] = {
				"name":building["name"],
				"level":level["town_hall_level"]
			}


with open("test_sg.json", "r") as fh:
	content = fh.read().decode("gb2312")
	content = json.loads(content)
	#print content["image"]

final_result = []
for image in content["image"]:
	image_path = image["filepath"]
	image_path = image_path[image_path.find("data"):]
	image_path = image_path.replace("\\", "/")
	name_level = reverse_table[image_path]
	final_result.append(
		{
			"x":image["row"],
			"y":image["col"],
			"building_name":name_level["name"],
			"level":name_level["level"],
		}
	)
print final_result