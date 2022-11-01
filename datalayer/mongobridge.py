import pymongo
from typing import List, Any
from multipledispatch import dispatch


class MongoBridge(object):
    """
    MongoBridge reads raw data from the mongo database for the BristolData database.
    """
    @dispatch(str, str, str)
    def __init__(self, uri: str, db: str, col: str):
        """
        Connects to the uri server, db database, and the col collection
        """
        self.__mongoClient = pymongo.MongoClient(uri)

        self.__myCollection = self.__mongoClient[db][col]

    @dispatch()
    def __init__(self):
        """
        Connects to the mongo server, BristolData database, and the Artists collection
        """
        self.__mongoClient = pymongo.MongoClient("mongodb://localhost:27017/")

        self.__myCollection = self.__mongoClient["BristolData"]["Artists"]

    def get_all_artists(self) -> List[dict]:
        """
        Get all artists in the database/collection. The returned list is a dictionary
        formatted with the following fields:
        * _id: str
        * artistID: int
        * artistName: str
        * realname: str
        * profile: str
        * collaborators: List of dictionaries
        * level: int
        See the test_artist.py for an example
        :return: list of the dictionaries returned from mongo
        """
        result: List[dict] = []
        artists = self.__myCollection.find()

        for a in artists:
            result.append(a)

        return result
    def get_artists_from_list(self, a_list: list[int]) -> List[dict]:
        """
        Get artists using the id list from the database/collection
        The returned list is a dictionary formatted with the following fields:
        * _id: str
        * artistID: int
        * artistName: str
        * realname: str
        * profile: str
        * collaborators: List of dictionaries
        * level: int
        See the test_artist.py for an example
        :return: list of the dictionaries returned from mongo
        """
        result: List[dict] = []

        for a in a_list:
            mongo_filter = {"artistID": a}
            result.append(self.__myCollection.find_one(mongo_filter))
        return result

    def get_artist_by_id(self, aid: int) -> dict:
        """
        Get the dictionary for a single artist from the database/collection.
        The returned dictionary is formatted with the following fields:
        * _id: str
        * artistID: int
        * artistName: str
        * realname: str
        * profile: str
        * collaborators: List of dictionaries
        * level: int
        See the test_artist.py for an example
        :param aid: artist id
        :return: dictionary with artist info
        """
        mongo_filter = {"artistID": aid}
        artists = self.__myCollection.find_one(mongo_filter)

        return artists
