from displacement import *

# tag: farm and watering
# the Constructor (Initializer)
def __init__(self, attr_name_1, attr_name_2):
	self.__init__ = attr_name_0 # is this an output result when you call the function constructor? 
	self.attr1 = attr_name_1
	self.attr2 = attr_name_2

def your_func_0(self):
	self.items = []

def farm_001(crop):
	# from Harv import *

	# create a plant list
	crops = [
		Entities.Apple, 
		Entities.Bush, 
		Entities.Cactus, 
		Entities.Carrot, 
		Entities.Dinosaur, 
		Entities.Grass, 
		Entities.Pumpkin, 
		Entities.Sunflower, 
		Entities.Tree
	]

	crops_till = [
		Entities.Cactus,
		Entities.Carrot,
		Entities.Pumpkin,
		Entities.Sunflower
	]

	crops_water = [
		Entities.Bush,
		Entities.Carrot,
		Entities.Pumpkin,
		Entities.Sunflower,
		Entities.Tree
	]

	crops_fertilize = {
		Entities.Tree
	}

	crops_harvest_order = {
		Entities.Sunflower
	}


	if crop not in crops_harvest_order:
		harvest()
	else:
		pass
		# # Retrieve a dictionary containing all coordinate data.
		# dictionary_origin = {}
		# for k in range(15, 6, -1):
		# 	dictionary_origin[k] = []

		# harvest_column_001()

	if crop not in crops:
		print('unknown crop: {crop}')

	if crop in crops_till and get_ground_type() != Grounds.Soil:
		till()

	plant(crop)

	if crop in crops_fertilize:
		if num_items(Items.Fertilizer) > 500000:
			use_item(Items.Fertilizer)

	if crop in crops_water:
		watering_001()

def plant_companion_002():
	crops_companion = [
		Entities.Bush,
		Entities.Carrot,
		Entities.Grass,
		Entities.Tree
	]

	# (companion_type, (companion_x_position, companion_y_position)) = get_companion() 
	companion = get_companion()

	# unpack the companion type and its target coordinates
	plant_type, (x, y) = companion

	# if companion is None:
	# if companion == None:
	# 	return

	# if Polyculture exists, then 
	if plant_type not in crops_companion:
		return

	# move to (x, y)
	dx, dy = displacement_002(x, y)

	# plant(plant_type)
	farm_001(plant_type)

	# return to current position (get_pos_x, get_pos_y)
	displacement_return_001(dx, dy)

def plant_companion_001():
	# (companion_type, (companion_x_position, companion_y_position)) = get_companion() 
	companion = get_companion()

	# if companion is None:
	if companion == None:
		return
	
	# unpack the companion type and its target coordinates
	plant_type, (x, y) = companion

	# move to (x, y)
	dx, dy = displacement_002(x, y)

	# plant(plant_type)
	farm_001(plant_type)

	# return to current position (get_pos_x, get_pos_y)
	displacement_return_001(dx, dy)

def watering_001():
	# tag: watering
	# add waterting at right stage, set a bottom line
	# example num_items(Items.Fertilizer) > num_water

	if num_items(Items.Water) > 1700000:
		
		if get_water() == 0:
			use_item(Items.Water, 4)

		elif 0 < get_water() <= 0.25:
			use_item(Items.Water, 3)

		elif 0.25 < get_water() <= 0.5:
			use_item(Items.Water, 2)

		elif 0.5 < get_water() <= 0.75:
			use_item(Items.Water, 1)

		else:
			pass

	else:
		quick_print("watering failed:", "at", get_pos_x(), ",", get_pos_y())
