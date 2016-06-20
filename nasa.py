class NasaRover(object):
    """Rover class.

    excute run function to run the rover.
    """
    Xn, Yn = 0, 0
    rover_occup_coords = []

    def direction(self, D, head):
        """return head after `L` or `R` commands

        D : direction e.g: S, W, N, E
        head: 'L' or 'R'
        """
        dlist = ['S', 'W', 'N', 'E']
        index_of_d = dlist.index(head)
        if D == 'L':
            new_d = dlist[index_of_d - 1]
        elif D == 'R':
            new_d = 'S' if index_of_d == 3 else dlist[index_of_d + 1]
        else:
            raise ValueError('Invalid direction. Valid options a')
        return new_d

    def get_coordinate(self, x, y, h, token):
        """return coordinate after command.

        x, y , d: x axis, y axis, d: direction
        token: 'L', 'R' or 'M'
        """
        if token in ['L', 'R']:
            h = self.direction(token, h)
        elif token == 'M':
            if h == 'S':
                y -= 1
            elif h == 'W':
                x -= 1
            elif h == 'N':
                y += 1
            elif h == 'E':
                x += 1
        if self.Xn < x or x < -1 or self.Yn < y or y < -1:
            raise ValueError('Invalid command: Rover will lost in infinite space if'
                             'moved outside platique')
        if (x, y) in self.rover_occup_coords:
            raise ValueError('Invalid Command: Two rovers can not be on the same'
                             'coordinates.')
        return (x, y, h)

    def main(self):
        try:
            self.Xn, self.Yn = [int(i) for i in raw_input().split()]
        except ValueError as e:
            print(e)
            print('First line of input should contain space sparated top right'
                  'coordinate. e.g. 5 5')
            return

        rover_data_input = []
        while True:
            inp = raw_input().strip()
            if not inp:
                break
            rover_data_input.append(inp)

        if not (len(rover_data_input) % 2 == 0):
            # 1st line: initial coordinate , 2nd line: commad
            # so len of list will be even
            raise ValueError('Invalid Input. Rover initial coordiante and commands'
                             'not provided properly')

        rover_data = [(x, y) for x, y in zip(rover_data_input[::2],
                      rover_data_input[1::2])]
        # [(initial_coordinate for rover 1, command for rover 1), (..,..), ....]
        output_list = []
        for item in rover_data:
            row_init_coord, row_command = item
            try:
                x, y, d = [i.strip() for i in row_init_coord.split()]
                x, y = int(x), int(y)
            except ValueError:
                raise ValueError('Initial coordiante of rover must contain space saparated'
                                 'x, y axis and head. e.g. 1 2 N')

            if d not in ['S', 'W', 'N', 'E']:
                raise ValueError(
                    'Head can only one of the option: `S`, `W`, `N`, `E`')

            command = filter(lambda x: x in ['L', 'R', 'M'], row_command)
            if command != row_command:
                raise ValueError(
                    'Comannd can contain only `L`, `R` or `M` charachters')

            for char in command:
                x, y, d = self.get_coordinate(x, y, d, char)
            self.rover_occup_coords.append((x, y))
            output_list.append('{} {} {}'.format(x, y, d))
        return output_list

    def run(self):
        result_list = self.main()
        for result in result_list:
            print(result)

if __name__ == '__main__':
    rover = NasaRover()
    rover.run()
