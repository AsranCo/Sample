class Proxy:
    def __init__(self, obj):
        self._obj = obj

    def last_invoked_method(self):
        pass

    def count_of_calls(self, method_name):
        pass

    def was_called(self, method_name):
        pass



class Radio():
    def __init__(self):
        self._channel = None
        self.is_on = False
        self.volume = 0

    def get_channel(self):
        return self._channel

    def set_channel(self, value):
        self._channel = value

    def power(self):
        self.is_on = not self.is_on


    #     class Second:
    #
    # def __init__(self, x):
    #     self.x = x
    #
    # @property
    # def x(self):
    #     print("---> getter <---")
    #     return self.__x
    #
    # @x.setter
    # def x(self, x):
    #     print("---> setter <---")
    #     if x < 0:
    #         self.__x = 0
    #     elif x > 1000:
    #         self.__x = 1000
    #     else:
    #         self.__x = x