import pytest

from python_racing_car.model.car import Car


class TestCar:

    def test_자동차를_생성한다(self):
        car = Car.from_name("pobi")

        assert car.name == "pobi"
        assert car.position == 0

    @pytest.mark.parametrize(
        "name",
        [
            "",
            "abcdef",
        ],
    )
    def test_자동차_이름이_유효하지_않으면_예외가_발생한다(self, name):
        with pytest.raises(ValueError):
            Car.from_name(name)

    def test_랜덤값이_4이상이면_전진한다(self):
        car = Car.from_name("pobi")

        car.move(4)

        assert car.position == 1

    def test_랜덤값이_4미만이면_전진하지_않는다(self):
        car = Car.from_name("pobi")

        car.move(3)

        assert car.position == 0
