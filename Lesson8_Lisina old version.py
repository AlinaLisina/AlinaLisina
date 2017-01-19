import random

dishes_string = input('What would you like? \n')

dishes_list = dishes_string.split(",")
dishes_list2 = [element.capitalize().strip() for element in dishes_list]

dishes_dict = {element:random.randint(0, 1000) for element in dishes_list2}

for element, time in dishes_dict.items():
       print("Ordered dish: ", element, "Coocking time: ", time, "min")

print("Bon appetit!")
