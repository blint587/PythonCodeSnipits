
class RadioSwitch(object):

    class RadioNode():

        def __init__(self, host, representer, default=False):
            """
            Constructor of RadioNode.
            Sets initial value to 0.

            :param host:
            :param representer:
            :param val:
            :return:
            """
            self._value = 0
            self._blocked = False

            if not default and representer != "Default":
                self.repr = representer
            elif not default:
                raise Exception("Incorrect implementation!")
            elif default:
                self.repr = representer

            self._default = default
            if isinstance(host, RadioSwitch):
                self.host = host
            else:
                raise Exception("Incorrect implementation!")

        def __bool__(self):
            return bool(self._value)

        def set(self):
            """
            Sets the selected 'choice'.
            :return:
            """
            if not self._blocked:
                self.host._set_to_null()
                self._value = 1

        def block(self):
            if not self._default:
                self._blocked = True

        def __del__(self):
            """
            Destructor of RadioNode

            :return:
            """
            # print("Deleting RadioNode")
            del self.host
            del self._value

    def __init__(self):
        """
        :return:
        """
        self._rep = {}
        self.Empty = RadioSwitch.RadioNode(self, "Default", True)
        self.Empty.set()

    def representation(self):
        """
        :return:
        """
        for tag, attr in vars(self).items():
            if isinstance(attr, RadioSwitch.RadioNode):
                self._rep[attr.repr] = attr._value
        return self._rep

    def set_state(self, state):
        """
        :param state:
        :return:
        """
        pass

    def __str__(self):
        """
        :return:
        """
        return str(self.representation())

    def check(self):
        """
        :return:
        """
        the_sum = 0
        for tag, attr in vars(self).items():
            if isinstance(attr, RadioSwitch.RadioNode):
                the_sum += attr

        return the_sum == 1

    def active(self):
        """
        :return:
        """
        if self.check:
            for tag, attr in vars(self).items():
                if isinstance(attr, RadioSwitch.RadioNode):
                    if attr._value == 1:
                        return tag

    def set(self, wich):
        """
        :param wich:
        :return:
        """
        for tag, attr in vars(self).items():
            if isinstance(attr, RadioSwitch.RadioNode):
                if attr.repr == wich:
                    attr.set()

    def _set_to_null(self):
        """
        :return:
        """
        for tag, attr in vars(self).items():
            if isinstance(attr, RadioSwitch.RadioNode):
                attr._value = 0

    def __del__(self):
        """
        :return:
        """
        # print("Deleting RadioSwitch")
        attrs = [tag for tag, attr in vars(self).items()]
        try:
            for at in attrs:
                self.__delattr__(at)
        finally:
            del attrs


class CheckRadioSwitch(RadioSwitch):

    def __init__(self):
        RadioSwitch.__init__(self)
        self.a = RadioSwitch.RadioNode(self, "just this")
        self.b = RadioSwitch.RadioNode(self, "just that")
        self.c = RadioSwitch.RadioNode(self, "this and that")
        self.d = RadioSwitch.RadioNode(self, "all")
        self.e = RadioSwitch.RadioNode(self, "None")

if __name__ == "__main__":

    i = CheckRadioSwitch()
    print(i)
    i.a.set()
    print(i)
    i.a.block()

    i.b.set()
    print(i)

    i.d.set()
    print(i)

    i.set("just this")
    print(i)
    print(i.active())


# del i