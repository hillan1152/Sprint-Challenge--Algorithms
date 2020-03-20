class SortingRobot:
    def __init__(self, l):
        """
        SortingRobot takes a list and sorts it.
        """
        self._list = l          # The list the robot is tasked with sorting
        self._item = None       # The item the robot is holding
        self._position = 0      # The list position the robot is at
        self._light = "OFF"     # The state of the robot's light
        self._time = 0          # A time counter (stretch)

    def can_move_right(self):
        """
        Returns True if the robot can move right or False if it's
        at the end of the list.
        """
        return self._position < len(self._list) - 1

    def can_move_left(self):
        """
        Returns True if the robot can move left or False if it's
        at the start of the list.
        """
        return self._position > 0

    def move_right(self):
        """
        If the robot can move to the right, it moves to the right and
        returns True. Otherwise, it stays in place and returns False.
        This will increment the time counter by 1.
        """
        self._time += 1
        if self._position < len(self._list) - 1:
            self._position += 1
            return True
        else:
            return False

    def move_left(self):
        """
        If the robot can move to the left, it moves to the left and
        returns True. Otherwise, it stays in place and returns False.
        This will increment the time counter by 1.
        """
        self._time += 1
        if self._position > 0:
            self._position -= 1
            return True
        else:
            return False

    def swap_item(self):
        """
        The robot swaps its currently held item with the list item in front
        of it.
        This will increment the time counter by 1.
        """
        self._time += 1
        # Swap the held item with the list item at the robot's position
        self._item, self._list[self._position] = self._list[self._position], self._item

    def compare_item(self):
        """
        Compare the held item with the item in front of the robot:
        If the held item's value is greater, return 1.
        If the held item's value is less, return -1.
        If the held item's value is equal, return 0.
        If either item is None, return None.
        """
        if self._item is None or self._list[self._position] is None:
            return None
        elif self._item > self._list[self._position]:
            return 1
        elif self._item < self._list[self._position]:
            return -1
        else:
            return 0

    def set_light_on(self):
        """
        Turn on the robot's light
        """
        self._light = "ON"

    def set_light_off(self):
        """
        Turn off the robot's light
        """
        self._light = "OFF"

    def light_is_on(self):
        """
        Returns True if the robot's light is on and False otherwise.
        """
        return self._light == "ON"

    def sort(self):
        """
        Sort the robot's list.
        """
        # Fill this out
        # Robot starts at position 0
        #   if the robot can move to the left it = true, if not = false
        #   Pick up current card and turn on light
        #       true/false is used to indicate whether to continue a loop
        #       move right and compare each card
        #   compare > = 1, < = -1, 0 = 0, None
        #   while light is on,

        # THIS IS BUBBLE SORT: SET THE LIGHT TO TRUE,
        #   CREATE WHILE LOOP THAT TELLS THE FUNCTION IT'S TIME TO SWAP (THE LIGHT)
        #   SET LIGHT OFF AND CREATE A LOOP FOR MOVING RIGHT (WHILE CAN_MOVE_RIGHT)
        #   IF THE COMPARED ITEM IS 1: SWAP EM, MOVE RIGHT, AND MAKE THE LIGHT TRUE AGAIN, THIS WILL RESTART THE NEXT ITERATION.
        #   THE ROBOT REPRESENTS THE I OF THE FOR/WHILE LOOP, IT WILL TAKE IN THE INDEX

        #   Turn light on AKA TRUE
        self.set_light_on()
        # Swap item to get it in robots hands
        self.swap_item()
        # Move to the next available number
        self.move_right()
        # While the light is true run through the loop
        while self.light_is_on():
            # Immediately set light to off to control the loops
            self.set_light_off()
            # Create loop that is able to move right, and also not have empty spaces in the array
            while self.can_move_right() and self.compare_item() is not None:
                # if number being held is greater than the next, swap it, move right, and restart the loop (true)
                if self.compare_item() == 1:
                    self.swap_item()
                    self.move_right()
                    self.set_light_on()
                else:
                    self.move_right()
                    self.set_light_off()
            while self.can_move_left() and self.compare_item() is not None:
                if self.compare_item() == 1:
                    self.swap_item()
                    self.move_left()
                    self.set_light_on()
                else:
                    self.move_left()
                    self.set_light_off()
        self.move_right()
        self.set_light_on()


print("THIS IS ROBOT ---> ", SortingRobot([15, 41, 58, 49, 26, 4, 28, 8]))
if __name__ == "__main__":
    # Test our your implementation from the command line
    # with `python robot_sort.py`

    l = [15, 41, 58, 49, 26, 4, 28, 8, 61, 60, 65, 21, 78, 14, 35, 90, 54, 5, 0, 87, 82, 96, 43, 92, 62, 97, 69, 94, 99, 93, 76, 47, 2, 88, 51, 40, 95, 6, 23, 81, 30, 19, 25, 91, 18, 68, 71, 9, 66, 1,
         45, 33, 3, 72, 16, 85, 27, 59, 64, 39, 32, 24, 38, 84, 44, 80, 11, 73, 42, 20, 10, 29, 22, 98, 17, 48, 52, 67, 53, 74, 77, 37, 63, 31, 7, 75, 36, 89, 70, 34, 79, 83, 13, 57, 86, 12, 56, 50, 55, 46]

    robot = SortingRobot(l)

    robot.sort()
    print(robot._list)
