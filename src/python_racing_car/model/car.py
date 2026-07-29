import random

MOVE_CONDITION = 4
MAX_NAME_LENGTH = 5


class Car:
    def __init__(self, name: str) -> None:
        self._name = name
        self._position = 0

    @classmethod
    def from_name(cls, name: str) -> "Car":
        cls._validate_name(name)
        return cls(name)

    @staticmethod
    def _validate_name(name: str) -> None:
        if not name:
            raise ValueError("자동차 이름은 비어 있을 수 없습니다.")
        if len(name) > MAX_NAME_LENGTH:
            raise ValueError(f"자동차 이름은 {MAX_NAME_LENGTH}자를 초과할 수 없습니다.")

    @property
    def name(self) -> str:
        return self._name

    @property
    def position(self) -> int:
        return self._position

    def move(self, random_number: int) -> None:
        if random_number >= MOVE_CONDITION:
            self._position += 1

    def is_winner(self, max_position: int) -> bool:
        return self._position == max_position
