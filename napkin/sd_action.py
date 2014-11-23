import sd


class _Action(object):
    def __eq__(self, other):
        return self.__dict__ == other.__dict__


class Call(_Action):
    def __init__(self, caller, callee, method_name, params=None):
        self.caller = caller
        self.callee = callee
        self.method_name = method_name
        self.params = sd.Params() if params is None else params

    def __repr__(self):
        return "call from %s to %s::%s(%s)" % (self.caller,
                                               self.callee,
                                               self.method_name,
                                               self.params)

    def __eq__(self, other):
        return (self.caller is other.caller and
                self.caller is other.caller and
                self.method_name == other.method_name and
                self.params == other.params)


class Return(_Action):
    def __init__(self, params=None):
        self.params = sd.Params() if params is None else params

    def __repr__(self):
        return "return (%s)" % (self.params)

    def __eq__(self, other):
        return self.params == other.params


class ImplicitReturn(_Action):
    def __init__(self):
        pass

    def __eq__(self, other):
        return self.__class__ is other.__class__

    def __repr__(self):
        return "implicit return"


class FragBegin(_Action):
    def __init__(self, op_name, condition=None):
        self.op_name = op_name
        self.condition = condition

    def __repr__(self):
        s = "%s begin" % self.op_name
        if self.condition:
            s += " [%s]" % self.condition
        return s

    def __eq__(self, other):
        return (self.__class__ is other.__class__ and
                self.__dict__ == other.__dict__)


class FragEnd(_Action):
    def __init__(self, op_name):
        self.op_name = op_name

    def __repr__(self):
        return "%s end" % self.op_name

    def __eq__(self, other):
        return (self.__class__ is other.__class__ and
                self.__dict__ == other.__dict__)
