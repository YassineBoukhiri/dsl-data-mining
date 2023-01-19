from enum import Enum

class Operator(Enum):
    EQUAL = 0
    NOT_EQUAL = 1
    GREATER = 2
    LESS = 3
    GREATER_EQUAL = 4
    LESS_EQUAL = 5


class ComparisonParameter:
    def __init__(self, key: str, value, operator: Operator):
        self.key = key
        self.value = value
        self.operator = operator
        