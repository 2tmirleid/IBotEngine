from abc import abstractmethod


class Pagen:
    def __init__(self):
        ...

    @abstractmethod
    async def build_admins_pagen(self) -> list:
        pass

    @abstractmethod
    async def build_users_pagen(self) -> list:
        pass
