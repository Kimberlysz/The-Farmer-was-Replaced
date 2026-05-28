
# reference
class Dog:
	# A simple class attribute 简单的类属性
	species = "Canine"

	# The Constructor (Initializer)
	def __init__(self, name, breed):
		self.name = name   # Instance attribute 实例属性
		self.breed = breed # Instance attribute 实例属性

	# An instance method
	def bark(self):
		return f"{self.name} says Woof!"

class your_class:
	# the Constructor (Initializer)
	def __init__(self, attr_name_1, attr_name_2):
		self.__init__ = attr_name_0 # is this an output result when you call the function constructor? 
		self.attr1 = attr_name_1
		self.attr2 = attr_name_2
	
	def your_func_0(self):
		self.items = []

# the above are Constructor examples

# classes and functions of the game
class auto_unlock:
	# tag: AU
	def __init__(self, attr1, attr2):
		pass

	def auto_unlock_001():
		list = [Unlocks.Auto_Unlock, Unlocks.Cactus, Unlocks.Carrots, Unlocks.Costs, Unlocks.Debug_2, Unlocks.Debug, Unlocks.Dictionaries, Unlocks.Dinosaurs, Unlocks.Expand, Unlocks.Fertilizer, Unlocks.Functions, Unlocks.Grass, Unlocks.Grass, Unlocks.Hats, Unlocks.Import, Unlocks.Leaderboard, Unlocks.Lists, Unlocks.Loops, Unlocks.Mazes, Unlocks.Megafarm, Unlocks.Operators, Unlocks.Plant, Unlocks.Polyculture, Unlocks.Pumpkins, Unlocks.Senses, Unlocks.Simulation, Unlocks.Speed, Unlocks.Sunflowers, Unlocks.Timing, Unlocks.Top_Hat, Unlocks.Trees, Unlocks.Utilities, Unlocks.Variables, Unlocks.Watering] # an object list
		
		for i in range(len(list)):

			unlock_item = list[i]
			cost = get_cost(unlock_item)
		
			for item in cost:
				if num_items(item) < cost[item]:
					quick_print('not enough to unlock tech tree item')
				else:
					unlock(unlock_item)
					print('successfully unlock tech tree item')

class change_hat:
	# tag: CH
	# the Constructor (Initializer)
	def __init__(self, attr_name_1, attr_name_2):
		self.__init__ = attr_name_0 # is this an output result when you call the function constructor? 
		self.attr1 = attr_name_1
		self.attr2 = attr_name_2

	def your_func_0(self):
		self.items = []

	def change_hat_001():
		change_hat(Hats.Brown_Hat)
		do_a_flip()
		change_hat(Hats.Gray_Hat)
		do_a_flip()
		change_hat(Hats.Green_Hat)
		do_a_flip()
		change_hat(Hats.Purple_Hat)    
		do_a_flip()

class displacement:
	# import modules
	# from displacement import *

	# the Constructor (Initializer)
	def __init__(self, attr_name_1, attr_name_2):
		self.__init__ = attr_name_0 # is this an output result when you call the function constructor? 
		self.attr1 = attr_name_1
		self.attr2 = attr_name_2

	def your_func_0(self):
		self.items = []

	def move_n_dir(n, dir):
		for i in range(n):
			move(dir)

	def displacement_return_001(dx, dy):
		displacement_002(get_pos_x() - dx, get_pos_y() - dy)

	def displacement_002(x, y):
		# calculate coordinates difference
		dx = x - get_pos_x()
		dy = y - get_pos_y()

		# # solution 1
		# if dx < 0:
		# 	move_n_dir(abs(dx), West)
		
		# else:
		# 	move_n_dir(abs(dx), East)
		
		# if dy < 0:
		# 	move_n_dir(abs(dy), South)

		# else:
		# 	move_n_dir(abs(dy), North)

		# solution 0
		if dx < 0:
			if abs(dx) <= abs(get_world_size()/2):
				move_n_dir(abs(dx), West)

			else:
				move_n_dir(get_world_size() - abs(dx), East)
		
		else:
			if abs(dx) <= abs(get_world_size()/2):
				move_n_dir(abs(dx), East)

			else:
				move_n_dir(get_world_size() - abs(dx), West)				 
		
		if dy < 0:
			if abs(dy) <= abs(get_world_size()/2):
				move_n_dir(abs(dy), South)
			else:
				move_n_dir(get_world_size() - abs(dy), North)
		
		else:
			if abs(dy) <= abs(get_world_size()/2):
				move_n_dir(abs(dy), North)

			else:
				move_n_dir(get_world_size() - abs(dy), South)

		return (dx, dy)

	def displacement_001(x, y):
		# calculate coordinates difference
		dx = x - get_pos_x()
		dy = y - get_pos_y()

		# solution 1
		if dx < 0:
			move_n_dir(abs(dx), West)
		
		else:
			move_n_dir(abs(dx), East)
		
		if dy < 0:
			move_n_dir(abs(dy), South)

		else:
			move_n_dir(abs(dy), North)

		# solution 0
		# if dx < 0:
		# 	if dx <= abs(get_world_size()/2):
		# 		move_n_dir(abs(dx), West)

		# 	else:
		# 		move_n_dir(get_world_size() - abs(dx), East)
		
		# else:
		# 	if dx <= abs(get_world_size()/2):
		# 		move_n_dir(abs(dx), East)

		# 	else:
		# 		move_n_dir(get_world_size() - abs(dx), West)				 
		
		# if dy < 0:
		# 	if dy <= abs(get_world_size()/2):
		# 		move_n_dir(abs(dy), South)
		# 	else:
		# 		move_n_dir(get_world_size() - abs(dy), North)
		
		# else:
		# 	if dy <= abs(get_world_size()/2):
		# 		move_n_dir(abs(dy), North)

		# 	else:
		# 		move_n_dir(get_world_size() - abs(dy), South)

		return (dx, dy)

	def angular_displacement_002(dir, str): # 角位移
		directions = [North, East, South, West]
		for index in range(len(directions)):
			if directions[index] == dir:
				# Use % 4 to allow it to rotate "around the circle", so that after West it wraps back to North.

				if str == 'right':
					# Clockwise， turn right
					index = (index + 1) % 4
				
				elif str == 'left':
					# Counter-clockwise，turn left
					index = (index - 1) % 4
				
				elif str == 'return':
					# return
					index = (index + 2) % 4

				return directions[index]

	def angular_displacement_001(dir, str): # 角位移
		# concerns
		# 1. str a good method?
		# 

		directions = [North, East, South, West]
		index = directions.index(dir)
		# index = 0 is wrong, no abs num assign to index

		# Use % 4 to allow it to rotate "around the circle", so that after West it wraps back to North.

		if str == 'right':
			# Clockwise， turn right
			index = (index + 1) % 4
		
		elif str == 'left':
			# Counter-clockwise，turn left
			index = (index - 1) % 4
		
		elif str == 'return':
			# return
			index = (index + 2) % 4

		else:
			# go straight, ignore
			pass

		return directions[index]

class harvest:
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

class is_even:
	# tag: IE
	# the Constructor (Initializer)
	def __init__(self, attr_name_1, attr_name_2):
		self.__init__ = attr_name_0 # is this an output result when you call the function constructor? 
		self.attr1 = attr_name_1
		self.attr2 = attr_name_2
	
	def your_func_0(self):
		self.items = []

	def is_even(n):
		return n % 2 == 0

class maze:
	# the Constructor (Initializer)
	def __init__(self, attr_name_1, attr_name_2):
		self.__init__ = attr_name_0 # is this an output result when you call the function constructor? 
		self.attr1 = attr_name_1
		self.attr2 = attr_name_2

	def your_func_0(self):
		self.items = []

	def bfs_shortest(start, goal, map):
		# Breadth-First Search (BFS), this algorithm is used to determine the minimum number of steps needed to go from a start position to a destination position within a 2D map (grid) that contains walls or obstacles.

		(x, y) = start
		(x_des, y_des) = goal

		direction_coordinates = {
			North: (0, 1),
			East: (1, 0),
			South: (0, -1),
			West: (-1, 0)
		}

		# list[tuples]
		movement_final = [
			(
				(x, y),
				[]
			)
		]

		# set
		records_process = {
			(x, y)
		}

		while movement_final:
			# movement_final != 0; True

			position, path = movement_final.pop(0)
				# movement_final.pop(0)
				# 	(
				# 		(x, y),
				# 		[]
				# 	),

				# position = (x, y)
				# x = position[0]
				# y = position[1]
				# path = []


				# 	{
				# 		(x_next, y_next),
				# 		[] + [North] # path = [] doesn't change in a for loop
				# 	},

				# position = (x_next, y_next)
				# x = position[0]
				# y = position[1]
				# path = [North]

				# 	{
				# 		(0, 1),
				# 		[] + [North]
				# 	},

				# position = (0, 1)
				# x = position[0] = 0
				# y = position[1] = 1
				# path = [North]


			if position == (x_des, y_des):
					# position = (x, y)
				return path
					# path = []

			if position in map:

				# map = {
				# 	(x, y): [North, East],
				# 	(x_next, y_next): [North, East, South],
				# 	...
				# 	(x_2nd_to_the_last, y_2nd_to_the_last): [South, West],
				# 	(x_last, y_last): [North]
				# } 

				# map[(x, y)] = [North, East, South]

				coordinate_direction_list = map[position]
					# coordinate_direction_list = map[(x, y)] = [North, East]
					# coordinate_direction_list = map[(x_next, y_next)] = [North, East, South]

			else:
				coordinate_direction_list = []

			for direction in coordinate_direction_list:
				# coordinate_direction_list = map[(x, y)] = [North, East]
				# coordinate_direction_list = map[(x_next, y_next)] = [North, East, South]

				dx, dy = direction_coordinates[direction]
					# only iterate the first element
					# dx, dy = direction_coordinates[North] = (0, 1)

					# dx, dy = direction_coordinates[East] = (1, 0)

					# dx, dy = direction_coordinates[South] = (0, -1)

				(x_next, y_next) = (position[0] + dx, position[1] + dy)
					# x_next = position[0] + dx
					# y_next = position[1] + dy

				if (x_next, y_next) not in records_process:
					# set
					# records_process = {
					# 	(x, y)
					# }

					# records_process = {
					# 	(0, 0)
					# }

					# records_process = {
					# 	(x, y),
					# 	(x_next, y_next)
					# }

					# records_process = {
					# 	(0, 0),
					#	(0, 1)
					# }

					#...

					# records_process = {
					# 	(x, y),
					# 	(x_next, y_next),
					#	(x_next_1, y_next_1),
					#	(x_next_0a, y_next_0a),
					#	(x_next_0b, y_next_0b),
					#	(x_next_0c, y_next_0c)
					# }

					# records_process = {
					# 	(0, 0),
					#	(0, 1),
					#	(1, 0),
					#	(0, 2),
					# 	(1, 1),
					#	(0, 0),
					#	(1, 1),
					#	(2, 0),
					#	(1, -1)
					# }

					#...

					records_process.add(
						(
							x_next, 
							y_next
						)
					)

					# set
					# records_process = {
					# 	(x, y),
					# 	(x_next, y_next)
					# }

					# records_process = {
					# 	(0, 0),
					#	(0, 1)
					# }

					# records_process = {
					# 	(x, y),
					# 	(x_next, y_next),
					#	(x_next_1, y_next_1)
					# }

					# records_process = {
					# 	(0, 0),
					#	(0, 1),
					#	(1, 0)
					# }

					#...

					# records_process = {
					# 	(x, y),
					# 	(x_next, y_next),
					#	(x_next_1, y_next_1),
					#	(x_next_0a, y_next_0a),
					#	(x_next_0b, y_next_0b),
					#	(x_next_0c, y_next_0c)
					# }

					# records_process = {
					# 	(0, 0),
					#	(0, 1),
					#	(1, 0),
					#	(0, 2),
					# 	(1, 1),
					#	(0, 0),
					#	(1, 1),
					#	(2, 0),
					#	(1, -1)
					# }

					#...

					movement_final.append(
						(
							(x_next, y_next),
							path + [direction]
						)
					)

					# movement_final = [
					# 	{
					# 		(x_next, y_next),
					# 		[] + [North] # path = [] doesn't change in a for loop
					# 	},
					# 	(
					# 		(x_next_1, y_next_1),
					# 		[] + [East]
					# 	),
					# 	(
					# 		(x_next_0a, y_next_0a),
					# 		[North] + [North] # [North, North] 
					# 	),
					# 	(
					# 		(x_next_0b, y_next_0b),
					# 		[North] + [East] # [North, East]
					# 	),
					# 	(
					# 		(x_next_0c, y_next_0c),
					# 		[North] + [South] # [North, South]
					# 	),
					# ]

					# movement_final = [
					# 	{
					# 		(0, 1),
					# 		[] + [North]
					# 	},
					# 	(
					# 		(1, 0),
					# 		[] + [East]
					# 	),
					# 	(
					# 		(0, 1),
					# 		[North] + [North] # [North, North] 
					# 	),
					# 	(
					# 		(1, 0),
					# 		[North] + [East] # [North, East]
					# 	),
					# 	(
					# 		(0, -1),
					# 		[North] + [South] # [North, South]
					# 	),
					# ]

		return []

	def maze_mapping(start):
		# explore the whole map everytime to find the shortest route to get to the treasure

		(x, y) = start

		# list
		directions = [North, East, South, West] 

		# dict
		direction_coordinates = {
			North: (0, 1),
			East: (1, 0),
			South: (0, -1),
			West: (-1, 0)
		}

		# dict
		direction_reverse = { 
			North: South,
			East:  West,
			South: North,
			West:  East
		}

		# dict empty
		map = {
		}

		# list[tuples]
		records_final = [
			(
				(x, y),
				None
			)
		]

		# set
		records_process = {
			(x, y)
		}

		while records_final:
			# records_final != 0; True

			position, direction_from = records_final[-1]
				# unpack tuple
				# records_final[-1] = ((x, y), None)
				# position, direction_from = ((x, y), None)

				# position = (X, y)
				# position[0] = x
				# position[1] = y
				# direction_from = None

				# position = (X_next, y_next)
				# position[0] = x_next
				# position[1] = y_next
				# direction_from = South

			if position not in map:
				map[position] = []
					# assign key-value pair in dict
					# map = {
					# 	(x, y): []
					# } 

				for direction in directions:
					# directions = [North, East, South, West] 
					if can_move(direction):
						map[position].append(direction)

						# map = {
						# 	(x, y): [North, East],
						# 	(x_next, y_next): [North, East, South],
						# 	...
						# 	(x_2nd_to_the_last, y_2nd_to_the_last): [South, West],
						# 	(x_last, y_last): [North]
						# } 

						# map[(x, y)] = [North, East, South]

			movement = False # no movement for drone yet

			for direction in map[position]:
				# for direction in [North, East, South]

				dx, dy = direction_coordinates[direction]
					# only iterate the first element
					# dx, dy = direction_coordinates[North] = (0, 1)

					# not exec
					# dx, dy = direction_coordinates[East] = (1, 0)

					# not exec
					# dx, dy = direction_coordinates[South] = (0, -1)

				(x_next, y_next) = (position[0] + dx, position[1] + dy)
				# x_next = position[0] + dx
				# y_next = position[1] + dy

				if (x_next, y_next) not in records_process:
					records_process.add((x_next, y_next))
						# set add an element
							# records_process = {
							# 	(x, y),
							# 	(x_next, y_next)
							# }

							# records_process = {
							# 	(0, 0),
							# 	(0, 1)
							# }

					move(direction)
						# move(North)

					records_final.append(
						(
							(x_next, y_next),
							direction_reverse[direction]
						)
					)
						# append a tuple to a list
						# records_final = [
						# 	(
						# 		(x, y),
						# 		None
						# 	),
						# 	(
						# 		(x_next, y_next),
						# 		South
						# 	),
						# 	...
						# 	{
						# 		(x_2nd_to_the_last, y_2nd_to_the_last),
						# 		West
						# 	},
						# 	{
						# 		(x_last, y_last),
						# 		South
						# 	},
						# ]

						# records_final = [
						# 	(
						# 		(0, 0),
						# 		None
						# 	),
						# 	(
						# 		(0, 1),
						# 		South
						# 	),
						# 	{
						# 		(1, 0),
						# 		West
						# 	},
						# 	{
						# 		(0, 1),
						# 		South
						# 	},
						# ]

					movement = True # drone moved

					break # stop checking other directions, we already moved

			if not movement:
				# only executes when movement = False

				records_final.pop()
					# records_final = [
					# 	(
					# 		(x, y),
					# 		None
					# 	),
					# 	(
					# 		(x_next, y_next),
					# 		South
					# 	),
					# 	...
					# 	{
					# 		(x_2nd_to_the_last, y_2nd_to_the_last),
					# 		West
					# 	},
					# 	{
					# 		(x_last, y_last),
					# 		South
					# 	},
					# ]

					# records_final.pop()
						# 	(
						# 		(x_last, y_last),
						# 		South
						# 	)

				if records_final:
					# records_final = [
					# 	(
					# 		(x, y),
					# 		None
					# 	),
					# 	(
					# 		(x_next, y_next),
					# 		South
					# 	),
					# 	...
					# 	{
					# 		(x_2nd_to_the_last, y_2nd_to_the_last),
					# 		West
					# 	},
					# ]
					move(direction_from) # South, move the last

		return map

	def maze_001():
		clear()
		# Define directions in clockwise order: North (0), East (1), South (2), West (3)
		directions = [North, East, South, West]
		index = 0

		while get_entity_type() != Entities.Treasure:
			# 1. Try to turn Right (relative to current facing)
			index = (index + 1) % 4
			
			# 2. If blocked, keep turning Left until you can move
			while not can_move(directions[index]):
				Index = (index - 1) % 4
				
			# 3. Move in the successful direction
			move(directions[index])
			
		# Optional: Check if we found the treasure
		if get_entity_type() == Entities.Treasure:
			harvest()

class pumpkin:
	# import modules
	from displacement import *

	# tag: pumpkin
	# the Constructor (Initializer)
	def __init__(self, attr_name_1, attr_name_2):
		self.__init__ = attr_name_0 # is this an output result when you call the function constructor? 
		self.attr1 = attr_name_1
		self.attr2 = attr_name_2
	
	def your_func_0(self):
		self.items = []

	def dead_pumpkin_001(dict):
		# create a list for Entities.Dead_Pumpkin
		list_pumpkin = []
		
		# list all Dead_Pumpkin coordinates from dict
		for (x, yc) in dict:
			if dict[(x, y)] == Entities.Dead_Pumpkin:
				list_pumpkin.append((x, y))

		while len(list_pumpkin) > 0:
			x, y = list_pumpkin.pop(0) # pop the first coordinates to the list

			displacement_001(x, y)

			if get_entity_type() == Entities.Dead_Pumpkin:
				plant(Entities.Pumpkin)

				# add waterting at right stage, set a bottom line
				# example num_items(Items.Fertilizer) > 1000
				if get_water() < 0.5 and num_items(Items.Water) > 1000:
					use_item(Items.Water)

				while not can_harvest():
					if get_entity_type() == Entities.Dead_Pumpkin:
						plant(Entities.Pumpkin)

						# add waterting at right stage, set a bottom line
						# example num_items(Items.Fertilizer) > 1000
						if get_water() < 0.5 and num_items(Items.Water) > 1000:
							use_item(Items.Water)

	# (@test) can I use nested list?
	def dead_pumpkin_002(list, list):

class random:
	# the Constructor (Initializer)
	def __init__(self, attr_name_1, attr_name_2):
		self.__init__ = attr_name_0 # is this an output result when you call the function constructor? 
		self.attr1 = attr_name_1
		self.attr2 = attr_name_2
	
	def your_func_0(self):
		self.items = []

	def random_element_001(list):
		index = random() * len(list) // 1
		return list[index]

class sunflower:
	# import modules
	from displacement import *

	# tag: sunflower
	# the Constructor (Initializer)
	def __init__(self, attr_name_1, attr_name_2):
		self.__init__ = attr_name_0 # is this an output result when you call the function constructor? 
		self.attr1 = attr_name_1
		self.attr2 = attr_name_2
	
	def your_func_0(self):
		self.items = []

	def sunflower_001():

class farm:
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

class farm0:
    # CHANGED: __init__ only stores crop category sets as instance attributes
    # REMOVED: self.__init__ = attr_name_0 — this overwrites the constructor, never valid
    def __init__(self):

        # CHANGED: lists → sets, ordering not needed, membership check is faster
        self.crops_all = {
            Entities.Apple,
            Entities.Bush,
            Entities.Cactus,
            Entities.Carrot,
            Entities.Dinosaur,
            Entities.Grass,
            Entities.Pumpkin,
            Entities.Sunflower,
            Entities.Tree
        }
        self.crops_till = {
            Entities.Cactus,
            Entities.Carrot,
            Entities.Pumpkin,
            Entities.Sunflower
        }
        self.crops_water = {
            Entities.Bush,
            Entities.Carrot,
            Entities.Pumpkin,
            Entities.Sunflower,
            Entities.Tree
        }
        # ADDED: separate set for fertilizer requirement
        # Tree is the only crop that uses fertilizer currently
        self.crops_fertilize = {
            Entities.Tree
        }
        self.crops_companion = {
            Entities.Bush,
            Entities.Carrot,
            Entities.Grass,
            Entities.Tree
        }

    # CHANGED: farm_001 → plant_crop, universal single entry point for all planting
    # CHANGED: nested if/elif → independent sequential checks per requirement
    # each requirement is now its own block — adding new requirements in future
    # only means adding one new set in __init__ and one new if block here
    def plant_crop(self, crop):

        # guard: do nothing if crop is not recognized
        if crop not in self.crops_all:
            quick_print("unknown crop:", crop)
            return

        # step 1: till if required and ground is not already Soil
        if crop in self.crops_till and get_ground_type() != Grounds.Soil:
            till()

        # step 2: plant — always happens after any tilling
        plant(crop)

        # step 3: fertilize if required and stock is above threshold
        if crop in self.crops_fertilize:
            if num_items(Items.Fertilizer) > 500000:
                use_item(Items.Fertilizer)

        # step 4: water if required
        if crop in self.crops_water:
            self.watering_001()

    def watering_001(self):
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



















