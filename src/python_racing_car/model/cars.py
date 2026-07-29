from python_racing_car.model.car import Car


class Cars:
    def __init__(self, cars: list[Car]) -> None:
        self._cars = cars

    @classmethod
    def from_names(cls, names: list[str]) -> "Cars":
        cls._validate_car_names(names)
        cars = [Car.from_name(name) for name in names]
        return cls(cars)

    @classmethod
    def _validate_car_names(cls, names: list[str]) -> None:
        if not names:
            raise ValueError("자동차 이름 목록은 비어 있을 수 없습니다.")

    @property
    def cars(self) -> list[Car]:
        return self._cars

    def move(self, random_numbers: list[int]) -> None:
        if len(random_numbers) != len(self._cars):
            raise ValueError("자동차 수와 랜덤 값의 개수가 일치하지 않습니다.")

        for car, random_number in zip(self._cars, random_numbers):
            car.move(random_number)

    def find_winners(self) -> list[str]:
        max_position = max(car.position for car in self._cars)

        return [car.name for car in self._cars if car.is_winner(max_position)]
