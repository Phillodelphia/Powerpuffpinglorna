import monster_enounter_example as MSE


# Class for creating maps
class GameMap:
    def __init__(self, x, y):
        self.x_max = x
        self.y_max = y
        self.player_x = 0
        self.player_y = 0
        self.player = 'X'
        self.map_grid = []

    # Creating map
    def create_map(self):
        for y in range(0, self.y_max):
            x_axis = []

            for x in range(0, self.x_max):
                x_axis.append(Room(f'{y}{x}'))
            self.map_grid.append(x_axis)

    # Prints the map with inverted y axis
    def print_map_grid(self):

        # Fetches grid state and converts...
        # self.map_grid's x axis list into 1 row string, (temp_x_string).
        # Stores temp_x_string in y axis list, (temp_y_list)
        temp_y_list = []
        for y in range(self.y_max):
            temp_x_string = f'{y+1} '
            for x in range(self.x_max):

                temp_x_string += f'{self.map_grid[y][x].get_room_state()} '
            temp_y_list.append(temp_x_string)

        # Prints map with inverted y axis
        for y in range(self.y_max, 0, -1):
            print(temp_y_list[y-1])

        # Prints a x axis bottom row of numbers
        space = ' '
        bottom_info_row = f'0{space}'
        for i in range(1, self.x_max+1):
            bottom_info_row += f'{i}{space}'
        print(bottom_info_row)

    # Check boundaries inside map
    def check_bound(self, x, y):
        if 0 <= y < self.y_max:
            if 0 <= x < self.x_max:
                return True

        return False

    # Handles movement directions
    def make_direction(self, x, y, direction):
        directionsDict = {
            'U': (x, y+1),
            'R': (x+1, y),
            'D': (x, y-1),
            'L': (x-1, y)
            }

        return directionsDict[direction]

    def set_start_position(self, x, y):
        self.player_x = x
        self.player_y = y
        self.map_grid[y][x].change_state('X')

    # Move the player
    def make_move(self, x, y, direction):

        new_pos = self.make_direction(x, y, direction)
        old_x = x
        old_y = y
        x = new_pos[0]
        y = new_pos[1]

        if self.check_bound(x, y):
            self.map_grid[old_y][old_x].change_state('O')
            self.player_x = x
            self.player_y = y
            self.map_grid[y][x].change_state('X')
        else:
            print("Not a position, you donkey!")


class Room:
    def __init__(self, name):
        self.name = name
        self.state = '-'
        self.description = ''
        self.enemies = self.spawn_enemies()

    # Spawns enemyes in room, return list of
    # Enemy objects from enemies.py
    def spawn_enemies(self):
        enemies = MSE.randomiseMonsterEncounter()
        return enemies.return_enemies()

    def get_room_name(self):
        return self.name

    # Prints name of enemies object
    def enemies_name(self):
        for i in range(len(self.enemies)):
            print(self.enemies[i].get_name())

    # Changes Room state
    def change_state(self, new_state):
        self.state = new_state

    def spawn_tressure(self):
        # call funtion to generate tresure
        # save tresure to map
        pass

    def won_room(self):
        # save to json something to indicate the room is completed
        # chnage json-side map_grid to "x" (completed)

        # chnage client side map_grid to "x" (completed)
        pass

    # Retuns state of grid
    def get_room_state(self):
        return self.state


# test methods
playMap = GameMap(8, 8)
playMap.create_map()
playMap.set_start_position(0, 0)

playRoom = Room("hej")
playRoom.spawn_enemies()
playRoom.enemies_name()

input_dir = ''
while input_dir != 'e':
    input_dir = input("choose direction")
    playMap.make_move(playMap.player_x, playMap.player_y, input_dir)
    playMap.print_map_grid()
