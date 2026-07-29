from python_racing_car.model.attempt_count import AttemptCount
from python_racing_car.model.cars import Cars


class RacingGame:
    def __init__(
        self,
        cars: Cars,
        attempt_count: AttemptCount,
    ) -> None:
        self._cars = cars
        self._attempt_count = attempt_count

    @classmethod
    def from_input(
        cls,
        names: list[str],
        attempts: int,
    ) -> "RacingGame":
        return cls(
            Cars.from_names(names),
            AttemptCount.from_value(attempts),
        )

    @property
    def cars(self) -> Cars:
        return self._cars

    def play(self) -> None:
        import random

        for _ in range(self._attempt_count.value):
            random_numbers = [random.randint(0, 9) for _ in self._cars.cars]
            self._cars.move(random_numbers)

    def winners(self) -> list[str]:
        return self._cars.find_winners()
