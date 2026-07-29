class AttemptCount:
    MIN_ATTEMPT_COUNT = 1

    def __init__(self, value: int) -> None:
        self._value = value

    @classmethod
    def from_value(cls, value: int) -> "AttemptCount":
        cls._validate(value)
        return cls(value)

    @staticmethod
    def _validate(value: int) -> None:
        if value < AttemptCount.MIN_ATTEMPT_COUNT:
            raise ValueError("시도 횟수는 1 이상이어야 합니다.")

    @property
    def value(self) -> int:
        return self._value
