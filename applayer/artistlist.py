from typing import List, Tuple
from applayer.artist import Artist
from datalayer.mongobridge import MongoBridge
from multipledispatch import dispatch


class ArtistList(object):
    """
    The ArtistList class consists of two attributes:
        * __artist_objects: List[Artist] (must be Artist objects)
        * __artists: List[Tuple[int, str]] (ex. [(1141480, Alcoa Quartet), (1141491, Alfred G. Karnes)]
          this list must be sorted
    """
    @dispatch(list)
    def __init__(self, ids: List[int]):
        """
        The constructor uses data in mongo to create attributes based on the input ids list;
        Use a Mongobridge object to pull data from the Mongo database; the artists attribute
        must be a sorted list.
        """
        pass

    @dispatch()
    def __init__(self):
        """
        Read all of the data from mongo and attributes for all artists; See comment at head of the
        class; the artists attribute must be a sorted list.
        Use a Mongobridge object to pull data from the Mongo database
        """
        pass

    @property
    def artists(self) -> List[Tuple[int, str]]:
        """
        Returns the list of artists as list of tuples of (artistid: int, name: str)
        :return: list of artists
        """
        pass

    @property
    def artist_objects(self) -> List[Artist]:
        """
        Returns the list of Artist objects
        :return:
        """
        pass

    def __str__(self) -> str:
        """
        Prints a list of Artist objects separated by a comma ','
        ex: Alcoa Quartet (1141480), Alfred G. Karnes (1141491)
        Note that the formatting of the print of the Artist object is determined by
        the Artist class
        :return: str
        """
        pass
