alien_0 = {'x_position': 0, 'y_position': 25}
print("Original x-position: " + str(alien_0['x_position']))

speed = input('Enter Key: ')
measure = input('Enter Value: ')
alien_0[speed] = measure

# Move the alien to the right.
# Determine how far to move the alien based on its current speed.
if alien_0['speed'] == 'slow':
    x_increment = 1
elif alien_0['speed'] == 'medium':
    x_increment = 2
else:
 # This must be a fast alien.
    x_increment = 3

# The new position is the old position plus the increment.
alien_0['x_position'] = alien_0['x_position'] + x_increment
print("New x-position: " + str(alien_0['x_position']))