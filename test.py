import numpy as np 

n = 1_000_000
tenth = n//10
prog = 0

x = np.sort(np.random.rand(2, n), axis=0)
b_points = np.column_stack([x[0], x[1]-x[0], 1.0-x[1]]) @ np.array([(0, 0), (0.5, 0), (0, 1)])
r_points = np.column_stack(np.random.rand(2, n))

successes = 0
false_positives = 0

for i in range(n):
	if (i == prog):
		print(f'[{i}/{n}]')
		prog += tenth

	(bx, by) = b_points[i]
	(rx, ry) = r_points[i]

	is_in_circle_1 = rx**2 + ry**2 < bx**2 + by**2
	is_in_circle_2 = rx**2 + ry**2 < (1 - bx)**2 + by**2

	if (is_in_circle_1 ^ is_in_circle_2):
		successes += 1
	elif (is_in_circle_1 and is_in_circle_2):
		false_positives += 1
	
print(successes)
print(false_positives)