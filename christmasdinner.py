#A program to keep an up-to-date shopping list for christmas dinner
from pprint import pprint
import json

def xmas_greeting(banner,greeting,banner2):
    return banner, greeting, banner2

print(xmas_greeting("🎅🎄❄️" * 2, "Happy Christmas 2023!", "🎅🎄❄️" * 2))


christmas_dinner = {}
christmas_dinner["Meats"] = ["Turkey", "Goose", "Beef", "Pigs in blankets"]
christmas_dinner["Vegetables"] = ["Cabbage", "Cauliflower", "Peas", "Brocoli", "Carrots", "Sprouts"]
christmas_dinner["Sauces"] = ["Gravy", "Cranberry Sauce", "Redcurrant Jelly", "Bread Sauce"]
christmas_dinner["Extras"] = ["Roast Potatoes", "Stuffing"]
christmas_dinner["Pudding"] = ["Trifle", "Christmas Pudding", "Profiteroles", "Chocolate Torte"]


christmas_dinner["Meats"].append("Chipolatas") #How could I forget!
christmas_dinner["Pudding"].pop() #Too much to eat!
christmas_dinner["Pudding"].extend(["Custard", "Cream"]) #Can't forget these!

pprint(christmas_dinner, sort_dicts=False)

underline = "\n--------------------------------------------------\n"

with open('christmasdinner.txt', 'a+') as text_file:
    text_file.write("Happy Christmas!\n\n")
    text_file.write(underline)
    text_file.write("Meats\n--------------------------------------------------\n")
    text_file.write(json.dumps(christmas_dinner["Meats"]) + "\n\n")
    text_file.write(underline)
    text_file.write("Vegetables\n--------------------------------------------------\n")
    text_file.write(json.dumps(christmas_dinner["Vegetables"]) + "\n\n")
    text_file.write(underline)
    text_file.write("Sauces\n--------------------------------------------------\n")
    text_file.write(json.dumps(christmas_dinner["Sauces"]) + "\n\n")
    text_file.write(underline)
    text_file.write("Extras\n--------------------------------------------------\n")
    text_file.write(json.dumps(christmas_dinner["Extras"]) + "\n\n")
    text_file.write(underline)
    text_file.write("Puddings\n--------------------------------------------------\n")
    text_file.write(json.dumps(christmas_dinner["Pudding"]) + "\n")



