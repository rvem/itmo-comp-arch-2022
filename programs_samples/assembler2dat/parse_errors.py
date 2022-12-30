class ParserException(Exception):
    pass


class UnknownCommandTypeException(ParserException):
    pass


class UnknownRegisterException(ParserException):
    pass


class WrongJumpArgumentException(ParserException):
    pass
