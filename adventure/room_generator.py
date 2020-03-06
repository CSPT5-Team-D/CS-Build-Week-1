# Defign the rooms
# Description and name
# Save Room

# Connect Rooms

# World Generator (length, width, num_rooms)
# grid = [[0] * length] * width
# incert our [1's]

# grid.Save()

# def room_generator(room_x = 0, rom)

# from django.contrib.auth.models import User
# from adventure.models import Player, Room

# Room.objects.all().delete()

import random


def print_grid(grid, l, w):
    for i in range(w):
        grid_line = ''
        for j in range(l):
            grid_line += str(grid[i][j])
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


def generate_room(x, y, length, width, max_rooms, room_count, grid):

    # width is the x axis
    # length is the y axis

    # Base Case
    if room_count == max_rooms:
        return
    else:
        # mark this position on the grid with a 1,
        # increment the room count, and print the grid
        grid[x][y] = 1
        _room_count = room_count + 1
        print_grid_x(grid, length, width, x, y)

        # some debuging
        print(f'generating room {x}:{y}')
        print(f'room_count: {_room_count}, max_rooms: {max_rooms}')

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

        # debugging
        print(f'--available rooms--\n{available_rooms}')

        counter = 0
        for i in range(len(available_rooms)):
            if random.randint(0, 2) == 1 or counter == len(available_rooms) - 1:
                generate_room(available_rooms[i][0], available_rooms[i]
                              [1], length, width, max_rooms, _room_count, grid)
            else:
                counter += 1


def world_generator(length, width, max_rooms):
    grid = [[0] * length for i in range(width)]
    generate_room(0, 0, length, width, max_rooms, 0, grid)
    print_grid(grid, length, width)


world_generator(50, 50, 100)
