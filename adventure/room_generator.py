import random
from adventure.models import Player, Room
from django.contrib.auth.models import User


def print_grid(grid, l, w):
    for i in range(w):
        grid_line = ''
        for j in range(l):
            grid_line += ' '
            grid_line += str(grid[i][j])
            grid_line += ' '
        print(grid_line)


def print_grid_x(grid, l, w, x, y):
    for i in range(w):
        grid_line = ''
        for j in range(l):
            if i == x and j == y:
                grid_line += 'X'
            else:
                grid_line += str(grid[i][j])
        print(grid_line)


Room.objects.all().delete()
rm_count = 0


def generate_room(x, y, length, width, max_rooms, grid):
    global rm_count
    # width is the x axis
    # length is the y axis
    # Base Case
    if rm_count == max_rooms:
        return
    else:
        # mark this position on the grid with a 1,
        # increment the room count
        grid[x][y] = 1
        new_room = Room(
            title=f'Default room ({x},{y})', description="Default description", x=x, y=y)
        new_room.save()
        if x+1 < width and grid[x+1][y] == 1:
            con_room = Room.objects.filter(x=x+1, y=y)[0]
            new_room.connectRooms(con_room, 'e')
        if y+1 < length and grid[x][y+1] == 1:
            con_room = Room.objects.filter(x=x, y=y+1)[0]
            new_room.connectRooms(con_room, 's')
        if x-1 > 0 and grid[x-1][y] == 1:
            con_room = Room.objects.filter(x=x-1, y=y)[0]
            new_room.connectRooms(con_room, 'w')
        if y-1 > 0 and grid[x][y-1] == 1:
            con_room = Room.objects.filter(x=x, y=y-1)[0]
            new_room.connectRooms(con_room, 'n')
        rm_count += 1
        # Get available connecting rooms based on grid
        available_rooms = []
        # check of available adjacent rooms
        #           i,j+1
        #             |
        # i-1,j -- grid[i][j] -- i+1,j
        #             |
        #           i,j-1
        if x - 1 >= 0:
            if grid[x-1][y] == 0:
                available_rooms.append([x - 1, y])
        if x + 1 < width:
            if grid[x+1][y] == 0:
                available_rooms.append([x + 1, y])
        if y - 1 >= 0:
            if grid[x][y - 1] == 0:
                available_rooms.append([x, y - 1])
        if y + 1 < width:
            if grid[x][y + 1] == 0:
                available_rooms.append([x, y + 1])
        # counts the amount of
        for i in range(len(available_rooms)):
            if random.randint(0, 2) == 1 or i == len(available_rooms) - 1:
                generate_room(available_rooms[i][0], available_rooms[i]
                              [1], length, width, max_rooms, grid)


def world_generator(length, width, max_rooms):
    grid = [[0] * length for i in range(width)]
    generate_room(0, 0, length, width, max_rooms, grid)
    print_grid(grid, length, width)
    return grid


# Running the world generator here
width = 20
length = 20
rooms = 10

# Generates the world as a 2D list
new_grid = world_generator(length, width, rooms)

# Counts the amount of rooms in the new world grid
rm_counter = 0

for i in range(width):
    for j in range(length):
        rm_counter += new_grid[i][j]

print(f'final room count: {rm_counter}')
