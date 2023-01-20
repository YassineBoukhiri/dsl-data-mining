from enum import Enum

class Operator(Enum):
    EQUAL = 0
    NOT_EQUAL = 1
    GREATER = 2
    LESS = 3
    GREATER_EQUAL = 4
    LESS_EQUAL = 5

    def __str__(self):
        if self == Operator.EQUAL:
            return "=="
        elif self == Operator.NOT_EQUAL:
            return "!="
        elif self == Operator.GREATER:
            return ">"
        elif self == Operator.LESS:
            return "<"
        elif self == Operator.GREATER_EQUAL:
            return ">="
        elif self == Operator.LESS_EQUAL:
            return "<="
        else:
            raise ValueError("ERROR: Invalid operator.")

    @staticmethod
    def from_string(string: str):
        if string == "==":
            return Operator.EQUAL
        elif string == "!=":
            return Operator.NOT_EQUAL
        elif string == ">":
            return Operator.GREATER
        elif string == "<":
            return Operator.LESS
        elif string == ">=":
            return Operator.GREATER_EQUAL
        elif string == "<=":
            return Operator.LESS_EQUAL
        else:
            raise ValueError("ERROR: Invalid operator.")


class ComparisonParameter:
    def __init__(self, key: str, value, operator: Operator):
        self.key = key
        self.value = value
        self.operator = operator

    def __str__(self):
        key = ""
        if self.key == "loss":
            key = "value[1][0]"
        elif self.key == "accuracy":
            key = "value[1][1]"
        return f"{key} {str(self.operator)} {self.value}"
        