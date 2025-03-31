from __future__ import annotations

from variance import *

def test_biggest_shape() -> None:
    small_rect = Rectangle(3, 5)
    big_rect = Rectangle(7, 9)
    small_square = Square(4)
    big_square = Square(7)

    # small helper functions to assert that we receive the correct types
    def ensure_shape(shape: Shape) -> Shape:
        return shape
    def ensure_rect(rect: Rectangle) -> Rectangle:
        return rect
    def ensure_square(square: Square) -> Square:
        return square

    assert ensure_shape(biggest_shape([small_rect, small_square])) is small_square
    assert ensure_rect(biggest_shape([big_rect, small_rect])) is big_rect
    assert ensure_square(biggest_shape([small_square, big_square])) is big_square

def test_combine_shape_lists() -> None:
    small_rect = Rectangle(3, 5)
    big_rect = Rectangle(7, 9)
    small_square = Square(4)
    big_square = Square(7)

    # small helper functions to assert that we receive the correct types
    def ensure_shape_list(xs: list[Shape]) -> list[Shape]:
        return xs
    def ensure_rect_list(xs: list[Rectangle]) -> list[Rectangle]:
        return xs
    def ensure_square_list(xs: list[Square]) -> list[Square]:
        return xs

    shape_list: list[Shape] = [small_rect, big_square]
    rect_list: list[Rectangle] = [small_rect, big_rect]
    square_list: list[Square] = [big_square, small_square]

    assert ensure_shape_list(combine_shape_lists(shape_list, shape_list)) \
        == [small_rect, big_square, small_rect, big_square]
    assert ensure_rect_list(combine_shape_lists(rect_list, rect_list)) \
        == [small_rect, big_rect, small_rect, big_rect]
    assert ensure_shape_list(combine_shape_lists(rect_list, square_list)) \
        == [small_rect, big_rect, big_square, small_square]
    assert ensure_square_list(combine_shape_lists(square_list, square_list)) \
        == [big_square, small_square, big_square, small_square]
