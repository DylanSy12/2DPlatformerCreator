from typing import Tuple, Union, List, overload, Sequence

from pygame.cursors import Cursor
from pygame.surface import Surface

def get_pressed(num_buttons: int = 3) -> Union[Tuple[bool, bool, bool], Tuple[bool, bool, bool, bool, bool]]: ...
def get_pos() -> Tuple[int, int]: ...
def get_rel() -> Tuple[int, int]: ...
@overload
def set_pos(pos: Union[List[float], Tuple[float, float]]) -> None: ...
@overload
def set_pos(x: float, y: float) -> None: ...
def set_visible(value: bool) -> int: ...
def get_visible() -> bool: ...
def get_focused() -> bool: ...


@overload
def set_cursor(cursor: Cursor) -> None: ...
@overload
def set_cursor(constant: int) -> None: ...
@overload
def set_cursor(
    size: Union[Tuple[int, int], List[int]],
    hotspot: Union[Tuple[int, int], List[int]],
    xormasks: Sequence[int],
    andmasks: Sequence[int],
    ) -> None: ...
@overload
def set_cursor(hotspot: Union[Tuple[int, int], List[int]],
               surface: Surface,
               ) -> None: ...

def get_cursor() -> Cursor: ...
def set_system_cursor(cursor: int) -> None: ...
