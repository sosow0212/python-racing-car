from python_racing_car.view.input_view import InputView
from python_racing_car.view.output_view import OutputView


class RacingController:

    # TODO: RacingController 클래스의 run 메서드 구현
    def run(self) -> None:
        car_names = InputView.read_car_names()
        try_count = InputView.read_try_count()

        print(car_names)
        print(try_count)

        OutputView.print_result()
