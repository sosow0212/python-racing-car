class OutputView:
    @staticmethod
    def print_result() -> None:
        print()
        print("실행 결과")

    @staticmethod
    def print_round_result(car_name: str, position: int) -> None:
        print(f"{car_name} : {'-' * position}")

    @staticmethod
    def print_blank() -> None:
        print()

    @staticmethod
    def print_winners(winners: list[str]) -> None:
        print(f"최종 우승자 : {', '.join(winners)}")
