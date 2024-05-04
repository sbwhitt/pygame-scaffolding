class Point:
    def __init__(self, x: int, y: int) -> None:
        self.x = x
        self.y = y

    def __str__(self) -> str:
        return "(" + str(self.x) + ", " + str(self.y) + ")"

    def to_tuple(self) -> tuple[int, int]:
        return (self.x, self.y)

    # operators

    def __add__(self, other: "Point") -> "Point":
        '''
        overloads + operator
        '''
        return Point(self.x + other.x, self.y + other.y)

    def __iadd__(self, other: "Point") -> "Point":
        '''
        overloads += operator
        '''
        self.x += other.x
        self.y += other.y

    def __sub__(self, other: "Point") -> "Point":
        '''
        overloads - operator
        '''
        return Point(self.x - other.x, self.y - other.y)

    def __isub__(self, other: "Point") -> "Point":
        '''
        overloads -= operator
        '''
        self.x -= other.x
        self.y -= other.y

    def __mul__(self, other: "Point") -> "Point":
        '''
        overloads * operator
        '''
        return Point(self.x * other.x, self.y * other.y)
