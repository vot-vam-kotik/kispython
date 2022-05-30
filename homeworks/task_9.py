from enum import Enum


class State(Enum):
    A = 1
    B = 2
    C = 3
    D = 4
    E = 5
    F = 6
    G = 7


class main:
    def __init__(self):
        self.__state = State.A

    def march(self) -> int:
        match self.__state:
            case State.A:
                self.__state = State.B
                return 0
            case State.B:
                self.__state = State.C
                return 1
            case State.C:
                self.__state = State.D
                return 3
            case State.E:
                self.__state = State.G
                return 6
            case State.G:
                self.__state = State.D
                return 9

        raise KeyError

    def close(self) -> int:
        match self.__state:
            case State.B:
                return 2
            case State.D:
                self.__state = State.E
                return 4
            case State.E:
                self.__state = State.F
                return 5
            case State.F:
                self.__state = State.G
                return 7
            case State.G:
                self.__state = State.A
                return 8
        raise KeyError
