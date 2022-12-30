class ParserException(Exception):
    pass


class UnknownCommandTypeException(ParserException):
    def __str__(self):
        return "Unknown command type"


class UnknownRegisterException(ParserException):
    def __str__(self):
        return "Unknown register name"


class WrongJumpArgumentException(ParserException):
    def __str__(self):
        return "Unknown jump argument"
