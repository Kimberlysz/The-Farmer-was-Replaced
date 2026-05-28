# import functions
# ERROR: not allow to use in a defined function

from AU import *
from CH import *
from displacement import *
from farm import *
# from Harv import *
from IE import *
from maze import *
from pumpkin import *
from random import *

# tag: Harv
# the Constructor (Initializer)
def __init__(self, attr_name_1, attr_name_2):
	self.__init__ = attr_name_0 # is this an output result when you call the function constructor? 
	self.attr1 = attr_name_1
	self.attr2 = attr_name_2

def your_func_0(self):
	self.items = []

def harvest_001():
	# plant Entities.Grass and harvest Items.Hay

	clear()
	while True:
		if can_harvest():
			harvest()

		move(North)

def harvest_002():
	# plant Entities.Grass and harvest Items.Hay
	clear()
	while True:
		plant(Entities.Bush)

		if can_harvest():
			harvest()
		else:
			pass

		move(North)

def harvest_003():
	# plant Entities.Bush and harvest Items.Wood
	clear()
	while True:
		for i in range(get_world_size()):
			for j in range(get_world_size()):
				if can_harvest():
					harvest()

				plant(Entities.Bush)
				
				# add waterting at right stage, get_water() >= 250
				# if get_water() < 0.5 and num_items(Items.Water):
				#     use_item(Items.Water)

				move(North)

			move (East)

def harvest_004():
	# plant Entities.Carrot and harvest Items.Carrot
	clear()
	while True:
		for i in range(get_world_size()):
			for j in range(get_world_size()):

				if can_harvest():
					harvest()
				
				if get_ground_type() != Grounds.Soil:
					till()
				
				else:
					pass

				plant(Entities.Carrot)

				move(North)

			move (East)

def harvest_005():
	# plant Entities.Tree and harvest Items.Wood
	# import functions
	# from ESH import *
	# from CH import *
	# from IE import *

	# define functions
		# !important: import function() available then just import functions
	def is_even(n):
		return n % 2 == 0

	# main body
	clear()
	while True:
		for i in range(get_world_size()):
			for j in range(get_world_size()):

				if is_even(i) == is_even(j):
					if can_harvest():
						harvest()
					else:
						pass

					plant(Entities.Tree)
				
					# add waterting at right stage, get_water() >= 250
					# if get_water() < 0.5 and num_items(Items.Water):
					# 	use_item(Items.Water)

				else:
					if can_harvest():
						harvest()
					else:
						pass

					plant(Entities.Bush)
				
					# add waterting at right stage, get_water() >= 250
					# if get_water() < 0.5 and num_items(Items.Water):
					#     use_item(Items.Water)

				move(North)
				
			move (East)

def harvest_005a():
	# plant Entities.Tree and harvest Items.Wood
	# import functions
	# from ESH import *
	# from CH import *
	# from IE import *

	# define functions
		# !important: import function() available then just import functions
	def is_even(n):
		return n % 2 == 0

	# main body
	clear()
	crop = Entities.Tree
	crop1 = Entities.Bush
	while True:
		for i in range(get_world_size()):
			for j in range(get_world_size()):

				if is_even(i) == is_even(j):
					if can_harvest():
						harvest()
					else:
						pass

					farm_001(crop)
					plant_companion_002()

					while not can_harvest():
						pass
					
					harvest()
				
				else:
					if can_harvest():
						harvest()
					else:
						pass

					farm_001(crop1)
					plant_companion_002()

					while not can_harvest():
						pass

					harvest()

				move(North)
				
			move (East)

def harvest_006():
	# plant Entities.Tree, Entities.Grass and harvest Items.Wood, Items.Hay

	# import functions
	# ERROR: not allow to use in a defined function
	# from CH import *
	# from ESH import *
	# from IE import *
	# from displacement import *
	# from pumpkin import *

	# define functions
	# def is_even(n):
	#     return n % 2 == 0

	# main body
	clear()
	while True:
		for i in range(get_world_size()):
			for j in range(get_world_size()):

				if is_even(i) == is_even(j):
					if can_harvest():
						harvest()
					else:
						pass

					plant(Entities.Tree)

					# use Items.Fertilizer and harvest Items.Weird_Substance 
					# use it at right stage, set a bottom line
					# example num_items(Items.Fertilizer) > 400
					if num_items(Items.Fertilizer) > 400:
						use_item(Items.Fertilizer)

					# add waterting at right stage, set a bottom line
					# example num_items(Items.Fertilizer) > 1000
					# if get_water() < 0.5 and num_items(Items.Water) > 1000:
					# 	use_item(Items.Water)

				else:
					if can_harvest():
						harvest()
					else:
						pass

					if get_ground_type() != Grounds.Grassland:
						till()
					else:
						pass

					# plant(Entities.Bush)
				
					# add waterting at right stage, get_water() >= 250
					# if get_water() < 0.5 and num_items(Items.Water):
					#     use_item(Items.Water)

				move(North)
				
			move (East)

def harvest_007():
	# plant Entities.Pumpkin and harvest Items.Pumpkin

	# import functions
	# ERROR: not allow to use in a defined function
	# from CH import *
	# from ESH import *
	# from IE import *
	# from displacement import *
	# from pumpkin import *

	# main body
	clear() 
	while True:

		for i in range(get_world_size()):
			for j in range(get_world_size()):

				if get_ground_type() != Grounds.Soil:
					till()

				plant(Entities.Pumpkin)

				# add waterting at right stage, set a bottom line
				# example num_items(Items.Fertilizer) > 1000
				if get_water() < 0.5 and num_items(Items.Water) > 1000:
					use_item(Items.Water)

				move(North)

			move(East)

		entity_dict = {}
		for i in range(get_world_size()):
			for j in range(get_world_size()):

				x, y = get_pos_x(), get_pos_y()
				entity_dict[(x, y)] = get_entity_type()
				# entity_dict[(get_pos_x(), get_pos_y())] = get_entity_type()

				move(North)
					
			move(East)
		
		dead_pumpkin_001(entity_dict)

		displacement_002(0, 0)
		if can_harvest():
			harvest()

# def harvest_008():
	# plant Entities.Sunflower and harvest Items.Power

def harvest_009():
	# plant Entities.Treasure and harvest Items.Gold
	# this method purely focus on Walk along the right wall, if there are walls removed, bugs appear

	# direction
	directions = [North, East, South, West]
	# create a random direction, fixed random direction
	direction = random_element_001(directions)

	# if get_entity_type() == Entities.Hedge:
	while get_entity_type() != Entities.Treasure:
		if get_entity_type() == Entities.Grass:
			# make a full field maze
			plant(Entities.Bush)
			substance = get_world_size() * 2**(num_unlocked(Unlocks.Mazes) - 1)
			use_item(Items.Weird_Substance, substance)

		# define directions based on the created direction above
		right = angular_displacement_002(direction, 'right')
		left = angular_displacement_002(direction, 'left')
		back = angular_displacement_002(direction, 'return')

		if can_move(right):
			direction = right
		elif can_move(direction):
			pass
		elif can_move(angular_displacement_002(direction, 'left')):
			direction = angular_displacement_002(direction, 'left')
		else:
			direction = back

		move(direction)

		if get_entity_type() == Entities.Treasure:
			harvest()

def harvest_010():
	# plant Entities.Treasure and harvest Items.Gold
	# This method alternates between "walking along the right wall" and "walking along the left wall," switching every four cycles; this program is highly inefficient and contains potential errors.

	# direction
	directions = [North, East, South, West]
	# create a random direction, fixed random direction
	direction = random_element_001(directions)

	path = {}

	while get_entity_type() != Entities.Treasure:

		if get_entity_type() == Entities.Grass:
			# make a full field maze for the first time
			plant(Entities.Bush)
			substance = get_world_size() * 2**(num_unlocked(Unlocks.Mazes) - 1)
			use_item(Items.Weird_Substance, substance)

		# define directions based on the created direction above
		right = angular_displacement_002(direction, 'right')
		left = angular_displacement_002(direction, 'left')
		back = angular_displacement_002(direction, 'return')

		# sensing current location
		x = get_pos_x()
		y = get_pos_y()

		# dict[key] = value
		# path[(x, y)] = 1

		# dict = {key0: value0, key1: value1}
		# path = {(0, 0): 1}
		# entity_dict = {(x,y):get_entity_type()}

		# path.update({(x, y): get_entity_type()})
		# path[(x, y)] += 1

		if (x, y) not in path:
			# walk-along-the-wall-to-the-right
			if can_move(right):
				direction = right
			elif can_move(direction):
				pass
			elif can_move(angular_displacement_002(direction, 'left')):
				direction = angular_displacement_002(direction, 'left')
			else:
				direction = back

			move(direction)
			path[(x, y)] = 1

		elif (x, y) in path and (path[(x, y)]//4) % 2 != 0:
			# walk-along-the-wall-to-the-right
			if can_move(right):
				direction = right
			elif can_move(direction):
				pass
			elif can_move(angular_displacement_002(direction, 'left')):
				direction = angular_displacement_002(direction, 'left')
			else:
				direction = back

			move(direction)
			path[(x, y)] += 1

		elif (x, y) in path and (path[(x, y)]//4) % 2 == 0:
			# walk-along-the-wall-to-the-left
			if can_move(left):
				direction = left
			elif can_move(direction):
				pass
			elif can_move(angular_displacement_002(direction, 'right')):
				direction = angular_displacement_002(direction, 'right')
			else:
				direction = back

			move(direction)
			path[(x, y)] += 1

		if get_entity_type() == Entities.Treasure:
			# harvest()
			# recreate and reuse the maze
			use_item(Items.Weird_Substance, substance)

def harvest_011():
	# plant Entities.Treasure and harvest Items.Gold
	# Breadth-First Search (BFS), but re-mapping everytime a treasure is found, not efficient

	# assign a value to a key in dict
		# dict[key] = value
		# path[(x, y)] = 1

		# dict = {key0: value0, key1: value1}
		# path = {(0, 0): 1}
		# entity_dict = {(x,y):get_entity_type()}

		# path.update({(x, y): get_entity_type()})
		# path[(x, y)] += 1

	if get_entity_type() == Entities.Grass:
		plant(Entities.Bush)
		substance = get_world_size() * 2**(num_unlocked(Unlocks.Mazes) - 1)
		use_item(Items.Weird_Substance, substance)

	while True:
		# sensing current location
		x = get_pos_x()
		y = get_pos_y()

		# sensing treasure coordinates
		x_des, y_des = measure()

		# start and goal coordinates
		start = (x, y) # tuple
		goal = (x_des, y_des) # tuple

		map = maze_mapping(start)
		path = bfs_shortest(start, goal, map)

		for direction in path:
			move(direction)

		if get_entity_type() == Entities.Treasure:
			use_item(Items.Weird_Substance, substance)

def harvest_012():
	# plant Entities.Treasure and harvest Items.Gold
	# Breadth-First Search (BFS) w/ mapping just 1x, most efficient algorithm

	# assign a value to a key in dict
		# dict[key] = value
		# path[(x, y)] = 1

		# dict = {key0: value0, key1: value1}
		# path = {(0, 0): 1}
		# entity_dict = {(x,y):get_entity_type()}

		# path.update({(x, y): get_entity_type()})
		# path[(x, y)] += 1

	if get_entity_type() == Entities.Grass:	
		plant(Entities.Bush)
		substance = get_world_size() * 2**(num_unlocked(Unlocks.Mazes) - 1)
		use_item(Items.Weird_Substance, substance)

	# sense initial position and build the map once before the loop
	# sensing current location
	x = get_pos_x()
	y = get_pos_y()

	# sensing treasure coordinates
	x_des, y_des = measure()

	# start and goal coordinates
	start = (x, y) # tuple
	goal = (x_des, y_des) # tuple

	map = maze_mapping(start)

	while True:
		# sensing current location
		x = get_pos_x()
		y = get_pos_y()

		# sensing treasure coordinates
		x_des, y_des = measure()

		# start and goal coordinates
		start = (x, y) # tuple
		goal = (x_des, y_des) # tuple

		# map = maze_mapping(start)
		path = bfs_shortest(start, goal, map)

		for direction in path:
			move(direction)

		if get_entity_type() == Entities.Treasure:
			use_item(Items.Weird_Substance, substance)

def harvest_013():
	# plant Entities.Treasure and harvest Items.Gold
	# Breadth-First Search (BFS) w/ mapping at a control frequency, could be even more efficient for execution

	# assign a value to a key in dict
		# dict[key] = value
		# path[(x, y)] = 1

		# dict = {key0: value0, key1: value1}
		# path = {(0, 0): 1}
		# entity_dict = {(x,y):get_entity_type()}

		# path.update({(x, y): get_entity_type()})
		# path[(x, y)] += 1

	if get_entity_type() == Entities.Grass:
		plant(Entities.Bush)
		substance = get_world_size() * 2**(num_unlocked(Unlocks.Mazes) - 1)
		use_item(Items.Weird_Substance, substance)

	# define how frequently maze_mapping is called
	remap_frequency = 50 # change frequency here

	# count of treasures collected
	harvest_count = 0

	# initialize map and use it as a condition to trigger maze_mapping()
	# map = None
	map = {}

	while True:
		# sensing current location
		x = get_pos_x()
		y = get_pos_y()

		# sensing treasure coordinates
		x_des, y_des = measure()

		# start and goal coordinates
		start = (x, y) # tuple
		goal = (x_des, y_des) # tuple

		if map == {} or harvest_count % remap_frequency == 0:
		# if not map or harvest_count % remap_frequency == 0:
			# map = {}, False
			map = maze_mapping(start)
		path = bfs_shortest(start, goal, map)

		for direction in path:
			move(direction)

		if get_entity_type() == Entities.Treasure:
			use_item(Items.Weird_Substance, substance)

		harvest_count += 1

