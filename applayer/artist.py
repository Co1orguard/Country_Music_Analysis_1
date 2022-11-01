from multipledispatch import dispatch
from typing import List


class Artist(object):

    @dispatch(dict)
    def __init__(self, raw_in: dict):
        """
        Takes a mongodb dictionary from the Artist collection and creates an Artist object
        :param raw_in: dictionary based on schema from mongo database
        """
        self.__artistID = abs(int(raw_in["artistID"]))
        self.__artistName = raw_in["artistName"]
        self.__realname = raw_in["realname"]
        self.__profile = raw_in["profile"]
        self.__collaborators = raw_in["collaborators"]
        self.__level = abs(raw_in["level"])

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
        self.__artistID: int = abs(aid)
        self.__artistName: str = name
        self.__realname: str = real_name
        self.__collaborators = None
        self.__profile: str = profile
        self.__level: int = abs(level)

    @property
    def artistID(self) -> int:

        return self.__artistID

    @property
    def artistName(self) -> str:

        return self.__artistName

    @property
    def realName(self) -> str:

        return self.__realname

    @property
    def profile(self) -> str:

        return self.__profile

    @property
    def level(self) -> int:

        return self.__level

    @property
    def collaborators(self) -> List[dict]:

        return self.__collaborators

    @level.setter
    def level(self, lev: int) -> None:

        # ensure input conforms to desired type and value range
        if(lev < 0):
            self.__level: int = abs(lev)
        else:
            self.__level: int = lev
    def __str__(self) -> str:
        """
        Prints an artist name and artist ID
        ex. Alcoa Quartet (1141480)
        :return: string formatted as in example
        """
        return "{} ({})".format(self.__artistName, self.__artistID)
