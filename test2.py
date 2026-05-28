def displacement_003(x, y):
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