class InputView:
    @staticmethod
    def read_car_names() -> list[str]:
        names = input("자동차 이름을 입력하세요 (쉼표로 구분): \n")
        return [name.strip() for name in names.split(",")]

    @staticmethod
    def read_try_count() -> int:
        attempts = input("시도할 횟수를 입력하세요: \n")
        return int(attempts)
