from collections import UserList


class CaseInsensitiveList(UserList):
    """
    Simple list type for storing and comparing strings case-insensitively
    """
    def __contains__(self, item: object) -> bool:
        if isinstance(item, str):
            return any(item.casefold() == x.casefold() for x in self.data)
        return item in self.data

    def append(self, item: object) -> None:
        if isinstance(item, str):
            self.data.append(item.casefold())
        else:
            self.data.append(item)
