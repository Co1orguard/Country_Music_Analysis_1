from unittest import TestCase
from applayer.artist import Artist


class TestArtist(TestCase):

    def setUp(self) -> None:
        self.artist_0: Artist = Artist(2309551, "Frank Stamps", "", "", 0)
        testdata_1 = {
          "_id": {
            "$oid": "630176cbc210d497ecd5db2e"
          },
          "artistID": 2309551,
          "artistName": "Frank Stamps",
          "realname": None,
          "profile": "Hello, Frank",
          "collaborators": [],
          "level": 0
        }
        self.artist_1 = Artist(testdata_1)
        testdata_2 = {
          "_id": {
            "$oid": "63016fde0f877215590c12a3"
          },
          "artistID": 2968305,
          "artistName": "Mr. & Mrs. Ernest Stoneman",
          "realname": None,
          "profile": "",
          "collaborators": [
            {
              "collaboratorID": 938895,
              "collaboratorName": "Ernest Stoneman",
              "releaseID": 10594844,
              "roles": None
            },
            {
              "collaboratorID": 1448909,
              "collaboratorName": "Hattie Stoneman",
              "releaseID": 10594844,
              "roles": [
                "Fiddle [Uncredited]"
              ]
            }
          ],
          "level": 0
        }
        self.artist_2 = Artist(testdata_2)
        testdata_3 = {
          "_id": {
            "$oid": "630173f08346c99bd3d978b7"
          },
          "artistID": 603612,
          "artistName": "Jack White (4)",
          "realname": "Eugene Joseph White",
          "profile": "Born: 2nd December 1905, Liverpool, England.\r\nDied: 25th June 1988, Brighton, England. (Aged 82).\r\n\r\nWhite was a popular UK dance band leader and instrumentalist during the two world wars.\r\n\r\nHis father, Jack, was an MC at local dances in Liverpool and this inspired him to learn both the drums and saxophone. A family band was formed, which he fronted with his father on the drums, called \"Jack White & His Collegians\". The band's followers assumed Eugene was \"Jack White\" and so the name stuck for the rest of his career.\r\n\r\nWhite's two bothers also joined the band. Jay, the eldest, played banjo and his younger brother Tom played saxophone. Between 1928 and 1929 they played two summer seasons on the Isle Of Man, gained recognition in 'Melody Maker' magazine and, in the 'All Lancashire Bands Championship', they won the Jack Hylton Trophy. At this point Tom was now drummer and Jay was on tenor saxophone.\r\n\r\nIn November 1929 Jack's band were resident in Liverpool's Rialto Ballroom for two years, followed by a residency at the State Café for a further two years. During the Depression the band remained in work at the West End Ballroom, Birmingham and then moved south for a season on the Isle Of Wight and then Brighton in 1935. During that summer the band then played regularly at the Hammersmith Palais in London where the band's talent came to much attention.\r\n\r\nWhite and the band then got their big break in May 1936, when they replaced the famous Joe Loss band at The Astoria. Loss had taken his band on a variety tour and White took up the engagement so effectively that by 1937 the band had secured a recording deal with Parlophone. Radio broadcasts from The Astoria by the band continued at the outbreak of war, raising British spirits with such favourites as \"The Lambeth Walk\". Some broadcasts and recordings had vocal support from the likes of Anne Lenner, Marjorie Stedeford and Dorothy Carless and, by June 1940, White's band were regulars on BBC's \"Music While You Work\".\r\n\r\nIn 1941 all three brothers were called up for wartime service. Jack and Jay toured the UK with the Central Band of the RAF. After the war White and the band returned to The Astoria, this time having to compete with their wartime replacement of Harry Leader and his band.\r\n\r\nWhite's brother Jay had left in poor health and moved to Hove, where he died in 1957. Tom also moved to Hove and began a grocery business and so, by 1957, the original group were no more. White continued performing with freelance musicians for a period, until 1966, when he retired and moved to Brighton where he began a printing business. By the time he died age 82 he had become somewhat of a recluse and had discarded much of his memorabilia of the dance band years.\r\n",
          "collaborators": [],
          "level": 0
        }
        self.artist_3 = Artist(testdata_3)

        testdata_4 = {
            "_id": {
                "$oid": "630173f08346c99bd3d978b7"
            },
            "artistID": "603612",
            "artistName": 123,
            "realname": 123,
            "profile": 123,
            "collaborators": [],
            "level": -3
        }

        self.artist_4 = Artist(testdata_4)

    def test_collaborators(self):
        self.assertEqual(2, len(self.artist_2.collaborators))
        self.assertEqual(0, len(self.artist_3.collaborators))

    def test_realname(self):
        self.assertIsNone(self.artist_1.realName)
        self.assertIsNone(self.artist_2.realName)
        self.assertEqual("Eugene Joseph White", self.artist_3.realName)
        self.assertIsNotNone(self.artist_3.realName)

    def test_profile(self):
        self.assertEqual("Hello, Frank", self.artist_1.profile)
        self.assertEqual("", self.artist_2.profile)
        self.assertEqual("Born: 2nd December 1905, Liverpool, England.\r\nDied: 25th June 1988, Brighton, England. (Aged 82).\r\n\r\nWhite was a popular UK dance band leader and instrumentalist during the two world wars.\r\n\r\nHis father, Jack, was an MC at local dances in Liverpool and this inspired him to learn both the drums and saxophone. A family band was formed, which he fronted with his father on the drums, called \"Jack White & His Collegians\". The band's followers assumed Eugene was \"Jack White\" and so the name stuck for the rest of his career.\r\n\r\nWhite's two bothers also joined the band. Jay, the eldest, played banjo and his younger brother Tom played saxophone. Between 1928 and 1929 they played two summer seasons on the Isle Of Man, gained recognition in 'Melody Maker' magazine and, in the 'All Lancashire Bands Championship', they won the Jack Hylton Trophy. At this point Tom was now drummer and Jay was on tenor saxophone.\r\n\r\nIn November 1929 Jack's band were resident in Liverpool's Rialto Ballroom for two years, followed by a residency at the State Café for a further two years. During the Depression the band remained in work at the West End Ballroom, Birmingham and then moved south for a season on the Isle Of Wight and then Brighton in 1935. During that summer the band then played regularly at the Hammersmith Palais in London where the band's talent came to much attention.\r\n\r\nWhite and the band then got their big break in May 1936, when they replaced the famous Joe Loss band at The Astoria. Loss had taken his band on a variety tour and White took up the engagement so effectively that by 1937 the band had secured a recording deal with Parlophone. Radio broadcasts from The Astoria by the band continued at the outbreak of war, raising British spirits with such favourites as \"The Lambeth Walk\". Some broadcasts and recordings had vocal support from the likes of Anne Lenner, Marjorie Stedeford and Dorothy Carless and, by June 1940, White's band were regulars on BBC's \"Music While You Work\".\r\n\r\nIn 1941 all three brothers were called up for wartime service. Jack and Jay toured the UK with the Central Band of the RAF. After the war White and the band returned to The Astoria, this time having to compete with their wartime replacement of Harry Leader and his band.\r\n\r\nWhite's brother Jay had left in poor health and moved to Hove, where he died in 1957. Tom also moved to Hove and began a grocery business and so, by 1957, the original group were no more. White continued performing with freelance musicians for a period, until 1966, when he retired and moved to Brighton where he began a printing business. By the time he died age 82 he had become somewhat of a recluse and had discarded much of his memorabilia of the dance band years.\r\n", self.artist_3.profile)

    def test_ids(self):
        self.assertEqual(2968305, self.artist_2.artistID)
        self.assertNotEqual(0, self.artist_2.artistID)
        self.assertEqual(603612, self.artist_3.artistID)

    def test_artistName(self):
        self.assertEqual("Frank Stamps", self.artist_0.artistName)
        self.assertEqual("Mr. & Mrs. Ernest Stoneman", self.artist_2.artistName)
        self.assertEqual("Jack White (4)", self.artist_3.artistName)

    def test_str(self):
        self.assertEqual("Frank Stamps (2309551)", self.artist_0.__str__())
        self.assertEqual("Frank Stamps (2309551)", self.artist_1.__str__())
        self.assertEqual("Jack White (4) (603612)", self.artist_3.__str__())

    def test_set(self):

        self.artist_1.level = 5

        self.assertEqual(5, self.artist_1.level)

    def test_edge_cases(self):

        # test whether our setter will accept negative numbers and mishandle the edge case
        self.artist_1.level = -1
        self.assertNotEqual(-1, self.artist_1.level)

        # ensure all string designated input is of type string

        self.assertTrue(isinstance(self.artist_4.artistID, int))
        self.assertFalse(isinstance(self.artist_4.artistName, str))
        self.assertFalse(isinstance(self.artist_4.realName, str))
        self.assertFalse(isinstance(self.artist_4.profile, str))
        self.assertTrue(self.artist_4.level >= 0)
