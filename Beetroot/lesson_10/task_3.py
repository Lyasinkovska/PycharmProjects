"""
first_channel() - turns on the first channel from the list.
last_channel() - turns on the last channel from the list.
turn_channel(N) - turns on the N channel. Pay attention that the channel numbers start from 1, not from 0.
next_channel() - turns on the next channel. If the current channel is the last one, turns on the first channel.
previous_channel() - turns on the previous channel. If the current channel is the first one, turns on the last channel.
current_channel() - returns the name of the current channel.
is_exist(N/'name') - gets 1 argument - the number N or the string 'name' and returns "Yes", if the channel N or 'name'
exists in the list, or "No" - in the other case.
The default channel turned on before all commands is №1.

Your task is to create the TVController class and methods described above.

CHANNELS = ["BBC", "Discovery", "TV1000"]
class TVController:
pass
controller = TVController(CHANNELS)
"""


class TVController:

    counter = -1

    def __init__(self, channels):
        self.channels = channels
        self.length = len(self.channels)
        self.counter = 0

    def first_channel(self):
        return self.channels[0]

    def last_channel(self):
        return self.channels[-1]

    def next_channel(self):
        TVController.counter += 1
        while True:
            if TVController.counter == self.length:
                TVController.counter = 0
            return self.channels[TVController.counter]

    def previous_channel(self):
        pass

    def current_channel(self):
        pass

    def is_exist(self, name):
        return 'Yes' if name in self.channels else 'No'


if __name__ == '__main__':

    CHANNELS = ["BBC", "Discovery", "TV1000"]
    controller = TVController(CHANNELS)
    print(controller.first_channel())
    print(controller.last_channel())
    for i in range(10):
        print(controller.next_channel())
    print(controller.is_exist('BBC'))
    print(controller.is_exist('BBS'))
