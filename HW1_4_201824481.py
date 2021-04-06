restitution = float(input('Enter coefficient of restitution: '))
height = float(input('Enter initial height in meters: '))
presentHeight = height
bounces = 0
meters = -height
while presentHeight > 0.1:
    meters += 2 * presentHeight
    presentHeight *= restitution
    bounces += 1
print('Number of bounces:', bounces)
print('Meters traveled: {:,.2f}'.format(meters))