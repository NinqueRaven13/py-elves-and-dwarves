from abc import ABC, abstractmethod


class Player(ABC):

    def __init__(self, nickname : str, *args, **kwrgs) -> None:
        super().__init__()
        self.nickname = nickname

    @abstractmethod
    def get_rating(self) -> int:
        pass

    @abstractmethod
    def player_info(self) -> str:
        pass
