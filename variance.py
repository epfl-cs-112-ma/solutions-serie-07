from __future__ import annotations

from abc import abstractmethod
from collections.abc import Sequence
from typing import Final

class Shape:
    @abstractmethod
    def area(self) -> float: ...

class Rectangle(Shape):
    width: Final[float]
    height: Final[float]

    def __init__(self, width: float, height: float) -> None:
        self.width = width
        self.height = height

    def __repr__(self) -> str:
        return f"Rectangle({self.width}, {self.height})"

    def area(self) -> float:
        return self.width * self.height

class Square(Shape):
    side: Final[float]

    def __init__(self, side: float) -> None:
        self.side = side

    def __repr__(self) -> str:
        return f"Square({self.side})"

    def area(self) -> float:
        return self.side ** 2

def biggest_shape[S: Shape](shapes: list[S]) -> S:
    assert len(shapes) > 0, "empty list of shapes"

    biggest = shapes[0]
    for shape in shapes:
        if shape.area() > biggest.area():
            biggest = shape
    return biggest

# Pour combine_shape_lists, on utilise
# - le polymorphisme borné ;
# - et la covariance sur Sequence (on aurait même pu utiliser Iterable).
def combine_shape_lists[S: Shape](xs: Sequence[S], ys: Sequence[S]) -> list[S]:
    result = [x for x in xs]
    for y in ys:
        result.append(y)
    return result
