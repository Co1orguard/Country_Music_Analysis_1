from multipledispatch import dispatch
from typing import List


class Artist(object):

    @dispatch(dict)
    def __init__(self, raw_in: dict):
        """
        Takes a mongodb dictionary from the Artist collection and creates an Artist object
        :param raw_in: dictionary based on schema from mongo database
        """
        pass

    @dispatch(int, str, str, str, int)
    def __init__(self, aid: int, name: str, real_name: str, profile: str, level: int):
        """
        Creates an Artist object using the input parameters; collaborators is set to None
        :param aid: artist id
        :param name: artist name
        :param real_name: artist real name, if known
        :param profile: artist profile
        :param level: artist level
        """
        pass

    @property
    def artistID(self) -> int:
        pass

    @property
    def artistName(self) -> str:
        pass

    @property
    def realName(self) -> str:
        pass

    @property
    def profile(self) -> str:
        pass

    @property
    def level(self) -> int:
        pass

    @property
    def collaborators(self) -> List[dict]:
        pass

    @level.setter
    def level(self, lev: int) -> None:
        pass

    def __str__(self):
        """
        Prints an artist name and artist ID
        ex. Alcoa Quartet (1141480)
        :return: string formatted as in example
        """
        pass
