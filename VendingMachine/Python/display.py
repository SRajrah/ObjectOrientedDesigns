class Display:
    def __init__(self):
        self.__message = ""

    def show_message(self, message: str):
        self.__message = message
        print(f"DISPLAY: {message}")

    def get_last_message(self) -> str:
        return self.__message