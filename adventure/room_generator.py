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


class vector2:
    def __inti__(self, x, y):
        self.x = x
        self.y = y

    def get_val(self):
        return_list = [self.x, self.y]
        return return_list


def generate_room(x, y, length, width, max_rooms, room_count, grid):
    if room_count == max_rooms:
        return
    else:
        available_rooms = []
        # Get available connecting rooms based on grid
        if x - 1 >= 0:
            if y - 1 >= 0:
                available_rooms.append([x-1, y-1])
            if y+1 < length:
                available_rooms.append([x-1, y+1])
        if x + 1 < length:
            if y - 1 >= 0:
                available_rooms.append([x+1, y-1])
            if y+1 < length:
                available_rooms.append([x+1, y+1])
        if grid[x][y] != 1:
            grid[x][y] = 1
            room_count += 1

        for i in available_rooms:
            print('runing loop')
            if random.randint(0, 2) == 1:
                generate_room(x+i[0], y+i[1], length, width,
                              max_rooms, room_count, grid)

    # check of available adjacent rooms
    #           0,1
    #            |
    # -1,0 -- grid[i][j] -- 1,0
    #            |
    #           0,-1

            # Random_num_rooms = math.random(available_rooms_list.lenght())
            # for k in range(random_num_rooms):


def world_generator(length, width):
    grid = [[0] * length] * width
    generate_room(0, 0, length, width, 10, 0, grid)
    print(grid, sep='\n')


world_generator(25, 25)
