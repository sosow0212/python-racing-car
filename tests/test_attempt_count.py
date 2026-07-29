import pytest

from python_racing_car.model.attempt_count import AttemptCount


class TestAttemptCount:

    def test_시도횟수를_생성한다(self):
        attempt_count = AttemptCount.from_value(5)

        assert attempt_count.value == 5

    @pytest.mark.parametrize(
        "value",
        [
            0,
            -1,
        ],
    )
    def test_시도횟수가_1미만이면_예외(self, value):
        with pytest.raises(ValueError):
            AttemptCount.from_value(value)
