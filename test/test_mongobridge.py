from unittest import TestCase
from datalayer.mongobridge import MongoBridge


class TestMongoBridge(TestCase):

    def setUp(self) -> None:
        self.mongo_bridge = MongoBridge("mongodb://localhost:27017/", "BristolData", "Artists")

    def test_get_all_artists(self):
        artists = self.mongo_bridge.get_all_artists()
        #        self.assertEqual(1826136, artists[60]["artistID"])
        #        self.assertEqual(628155, artists[178]["artistID"])
        a0 = next(item for item in artists if item["artistID"] == 1826136)["artistName"]
        self.assertEqual("Stephen Tarter", a0)
        a1 = next(item for item in artists if item["artistID"] == 628155)["artistName"]
        self.assertEqual("A. P. Carter", a1)
        a2 = next(item for item in artists if item["artistID"] == 2029909)["artistName"]
        self.assertEqual("Paul Johnson (27)", a2)

    def test_get_artists_from_list(self):
        ids = [938895, 2634203, 1141486, 908705, 2411933, 2304638, 3895080, 1448909, 1448911, 1141474, 2916175, 353265, 1141476, 938862, 1141491, 1141484, 1141487, 307357, 1141480, 516930, 1001138, 1141475, 269365, 1141488, 1141483, 1141489, 2867358, 2867360, 2189637, 908699, 1420640, 2867359, 1826135]
        artists = self.mongo_bridge.get_artists_from_list(ids)
        self.assertEqual(33, len(artists))
        # tests whether the artistID at artists[2] is 1141486
        self.assertEqual(1141486, artists[2]["artistID"])
        # test whether the artistName at artists[3] is "Uncle Eck Dunford"
        self.assertEqual("Uncle Eck Dunford", artists[3]["artistName"])
    def test_get_artist_by_id(self):
        # Artist exists
        artist = self.mongo_bridge.get_artist_by_id(269365)
        self.assertEqual(269365, artist["artistID"])
        self.assertEqual("Jimmie Rodgers", artist["artistName"])
        self.assertEqual(0, artist["level"])
        self.assertEqual("James Charles Rodgers", artist["realname"])
        self.assertEqual("American country singer, guitarist and songwriter (born September 08, 1897 in Meridian, Mississippi - died May 26, 1933 in New York City, New York).\r\nIn the early 20th century known most widely for his rhythmic yodeling. Among the first country music superstars and pioneers, Rodgers was also known as The Singing Brakeman, The Blue Yodeler, and The Father of Country Music.\r\nInducted into Songwriters Hall of Fame in 1970.\r\nInducted into Rock And Roll Hall of Fame in 1986 (Early Influence). \r\nInducted into Country Music Hall of Fame in 1961.\r\n\r\n[b]Note! Please be careful when assigning credits to this artist.[/b] Other artists with a same or similar name exist (list not complete):\r\n- [a=Jimmy Rogers] - Chicago blues singer and guitarist\r\n- [a=Jimmie Rogers] - multi-instrumentalist (flute, didgeridoo, jew's harp ...)\r\n- [a=Jimmie Rogers (2)] - rock n' roll songwriter\r\n- [a=Jimmie Rodgers (2)] - folk/pop singer (born 1933)", artist["profile"])
        # Artist does not exist
        artist2 = self.mongo_bridge.get_artist_by_id(0)
        self.assertIsNone(artist2)
