from view.input_view import InputView
from view.output_view import OutputView


class RacingController:

    def run(self) -> None:
        car_names = InputView.read_car_names()
        try_count = InputView.read_try_count()

        print(car_names)
        print(try_count)

        OutputView.print_result()
