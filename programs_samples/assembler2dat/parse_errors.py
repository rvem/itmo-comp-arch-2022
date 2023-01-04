class ParserException(Exception):
    pass


class UnknownCommandTypeException(ParserException):
    def __str__(self):
        return "unknown command type"


class UnknownRegisterException(ParserException):
    def __str__(self):
        return "unknown register name"


class WrongJumpArgumentException(ParserException):
    def __str__(self):
        return "unknown jump argument"
