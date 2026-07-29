import pytest

from python_racing_car.model.cars import Cars


class TestCars:

    def test_자동차_목록을_생성한다(self):
        cars = Cars.from_names(["pobi", "woni", "jun"])

        assert len(cars.cars) == 3

    def test_자동차들이_전진한다(self):
        cars = Cars.from_names(["pobi", "woni"])

        cars.move([4, 3])

        assert cars.cars[0].position == 1
        assert cars.cars[1].position == 0

    def test_우승자를_반환한다(self):
        cars = Cars.from_names(["pobi", "woni"])

        cars.move([4, 3])
        cars.move([4, 4])

        assert cars.find_winners() == ["pobi"]

    def test_공동_우승자를_반환한다(self):
        cars = Cars.from_names(["pobi", "woni"])

        cars.move([4, 4])

        assert cars.find_winners() == [
            "pobi",
            "woni",
        ]

    def test_자동차가_없으면_예외(self):
        with pytest.raises(ValueError):
            Cars.from_names([])

    def test_랜덤값의_개수가_다르면_예외(self):
        cars = Cars.from_names(["pobi", "woni"])

        with pytest.raises(ValueError):
            cars.move([4])
