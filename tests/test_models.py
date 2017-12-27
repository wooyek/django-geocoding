import json
from decimal import Decimal

from django.test import TestCase
from mock import patch

from .test_app import factories


class GeocodingTests(TestCase):
    @patch("opencage.geocoder.OpenCageGeocode.geocode")
    def test_geocode_pl(self, geocode):
        geocode.return_value = [PL]
        work_location = factories.NamedModelFactory()
        work_location.location = "Poczty Gdańskiej 20, Warszawa"
        work_location.save()
        work_location.geocode()
        work_location.refresh_from_db()
        self.assertEqual(Decimal("20.8985"), work_location.lng)
        self.assertEqual(Decimal("52.19851"), work_location.lat)
        self.assertEqual("Poczty Gdańskiej", work_location.street)
        self.assertEqual("20", work_location.street_no)
        self.assertEqual("02-495", work_location.postal_code)
        self.assertEqual("Warsaw", work_location.city_town)
        self.assertEqual("Masovian Voivodeship", work_location.municipality)
        self.assertEqual("PL", work_location.country)

    @patch("opencage.geocoder.OpenCageGeocode.geocode")
    def test_geocode_gb(self, geocode):
        geocode.return_value = [GB]
        work_location = factories.NamedModelFactory()
        work_location.location = "Poczty Gdańskiej 20, Warszawa"
        work_location.save()
        work_location.geocode()
        work_location.refresh_from_db()
        self.assertEqual(Decimal("55.976246"), work_location.lat)
        self.assertEqual(Decimal("-3.234449"), work_location.lng)
        self.assertEqual("Royston Mains Avenue", work_location.street)
        self.assertEqual(None, work_location.street_no)
        self.assertEqual("EH5 1LB", work_location.postal_code)
        self.assertEqual("City of Edinburgh", work_location.city_town)
        self.assertEqual("Scotland", work_location.municipality)
        self.assertEqual("GB", work_location.country)


PL = json.loads("""{
   "components": {
      "city": "Warsaw",
      "country": "Poland",
      "state": "Masovian Voivodeship",
      "road": "Poczty Gdańskiej",
      "neighbourhood": "Skorosze",
      "postcode": "02-495",
      "county": "Warszawa",
      "suburb": "Ursus",
      "country_code": "pl",
      "house_number": "20",
      "_type": "building"
   },
   "annotations": {
      "Maidenhead": "KO02ke77tp",
      "MGRS": "34UDC9306283122",
      "callingcode": 48,
      "Mercator": {
         "x": 2326410.5,
         "y": 6802314
      },
      "currency": {
         "iso_code": "PLN",
         "decimal_mark": ",",
         "html_entity": "z&#322;",
         "smallest_denomination": 1,
         "subunit_to_unit": 100,
         "name": "Polish Złoty",
         "alternate_symbols": [],
         "iso_numeric": 985,
         "subunit": "Grosz",
         "symbol_first": 0,
         "symbol": "zł",
         "thousands_separator": " "
      },
      "qibla": 147.39,
      "sun": {
         "set": {
            "civil": 1478273820,
            "nautical": 1478276280,
            "apparent": 1478271660,
            "astronomical": 1478278620
         },
         "rise": {
            "civil": 1478235780,
            "nautical": 1478233320,
            "apparent": 1478237940,
            "astronomical": 1478230980
         }
      },
      "timezone": {
         "name": "Europe/Warsaw",
         "offset_string": 100,
         "short_name": "CET",
         "offset_sec": 3600,
         "now_in_dst": 0
      },
      "DMS": {
         "lng": "20° 53' 54.60099'' E",
         "lat": "52° 11' 54.63060'' N"
      },
      "OSM": {
         "url": "https://www.openstreetmap.org/?mlat=52.19851&mlon=20.89850#map=17/52.19851/20.89850",
         "edit_url": "https://www.openstreetmap.org/edit?way=369527093#map=17/52.19851/20.89850"
      },
      "what3words": {
         "words": "raves.trumpet.rescue"
      },
      "geohash": "u3qbgw3y675rb455e8bb"
   },
   "formatted": "Poczty Gdańskiej 20, 02-495 Warsaw, Poland",
   "bounds": {
      "northeast": {
         "lng": 20.898638,
         "lat": 52.198605
      },
      "southwest": {
         "lng": 20.898365,
         "lat": 52.198414
      }
   },
   "geometry": {
      "lng": 20.8985,
      "lat": 52.19851
   },
   "confidence": 10
}
""")

GB = json.loads("""{
      "annotations": {
        "DMS": {
          "lat": "55° 58' 34.48452'' N",
          "lng": "3° 14' 4.01676'' W"
        },
        "MGRS": "30UVH8536803460",
        "Maidenhead": "IO85jx14uh",
        "Mercator": {
          "x": -360057.227,
          "y": 7518245.832
        },
        "OSGB": {
          "easting": 323061.334,
          "gridref": "NT 230 766",
          "northing": 676605.969
        },
        "OSM": {
          "edit_url": "https://www.openstreetmap.org/edit?way=4997970#map=17/55.97625/-3.23445",
          "url": "https://www.openstreetmap.org/?mlat=55.97625&mlon=-3.23445#map=17/55.97625/-3.23445"
        },
        "callingcode": 44,
        "currency": {
          "alternate_symbols": [

          ],
          "decimal_mark": ".",
          "html_entity": "&#x00A3;",
          "iso_code": "GBP",
          "iso_numeric": 826,
          "name": "British Pound",
          "smallest_denomination": 1,
          "subunit": "Penny",
          "subunit_to_unit": 100,
          "symbol": "£",
          "symbol_first": 1,
          "thousands_separator": ","
        },
        "geohash": "gcvwqqhtrb7zyr9zbrq7",
        "qibla": 119.48,
        "sun": {
          "rise": {
            "apparent": 1478763660,
            "astronomical": 1478755860,
            "civil": 1478761140,
            "nautical": 1478758440
          },
          "set": {
            "apparent": 1478794320,
            "astronomical": 1478802120,
            "civil": 1478796840,
            "nautical": 1478799540
          }
        },
        "timezone": {
          "name": "Europe/London",
          "now_in_dst": 0,
          "offset_sec": 0,
          "offset_string": 0,
          "short_name": "GMT"
        },
        "what3words": {
          "words": "spirit.brains.gross"
        }
      },
      "bounds": {
        "northeast": {
          "lat": 55.9764711,
          "lng": -3.2321886
        },
        "southwest": {
          "lat": 55.9759374,
          "lng": -3.237638
        }
      },
      "components": {
        "_type": "road",
        "city": "City of Edinburgh",
        "country": "United Kingdom",
        "country_code": "gb",
        "neighbourhood": "Royston Mains",
        "postcode": "EH5 1LB",
        "road": "Royston Mains Avenue",
        "state": "Scotland",
        "suburb": "Granton"
      },
      "confidence": 10,
      "formatted": "Royston Mains Avenue, City of Edinburgh EH5 1LB, United Kingdom",
      "geometry": {
        "lat": 55.9762457,
        "lng": -3.2344491
      }
    }
""")

SAN_FRANCISCO = [{
    'formatted': 'San Francisco, San Francisco City and County, California, United States of America',
    'geometry': {
        'lng': -122.4192362,
        'lat': 37.7792808
    },
    'annotations': {
        'currency': {
            'symbol_first': 1,
            'subunit': 'Cent',
            'iso_numeric': 840,
            'smallest_denomination': 1,
            'symbol': '$',
            'iso_code': 'USD',
            'decimal_mark': '.',
            'name': 'United States Dollar',
            'subunit_to_unit': 100,
            'alternate_symbols': ['US$'],
            'html_entity': '$',
            'disambiguate_symbol': 'US$',
            'thousands_separator': ','
        },
        'sun': {
            'set': {
                'apparent': 1480294200,
                'astronomical': 1480299780,
                'nautical': 1480297860,
                'civil': 1480295940
            },
            'rise': {
                'apparent': 1480345440,
                'astronomical': 1480339860,
                'nautical': 1480341720,
                'civil': 1480343700
            }
        },
        'qibla': 18.84,
        'DMS': {
            'lng': "122° 25' 9.25032'' W",
            'lat': "37° 46' 45.41088'' N"
        },
        'Mercator': {
            'y': 4522112.901,
            'x': -13627647.037
        },
        'callingcode': 1,
        'MGRS': '10SEG5114281485',
        'OSM': {
            'url': 'https://www.openstreetmap.org/?mlat=37.77928&mlon=-122.41924#map=17/37.77928/-122.41924',
            'edit_url': 'https://www.openstreetmap.org/edit?relation=111968#map=17/37.77928/-122.41924'
        },
        'timezone': {
            'short_name': 'PST',
            'offset_sec': -28800,
            'name': 'America/Los_Angeles',
            'offset_string': -800,
            'now_in_dst': 0
        },
        'geohash': '9q8yym90303kjn7d80f6',
        'Maidenhead': 'CM87ss97qa',
        'what3words': {
            'words': 'plus.orange.hammer'
        }
    },
    'confidence': 1,
    'bounds': {
        'northeast': {
            'lng': -122.2817799,
            'lat': 37.9298443
        },
        'southwest': {
            'lng': -123.1738249,
            'lat': 37.6403143
        }
    },
    'components': {
        'county': 'San Francisco City and County',
        'country': 'United States of America',
        '_type': 'city',
        'city': 'San Francisco',
        'state': 'California',
        'country_code': 'us'
    }
}, {
    'formatted': 'San Francisco City and County, California, United States of America',
    'geometry': {
        'lng': -122.4629896,
        'lat': 37.7647993
    },
    'annotations': {
        'currency': {
            'symbol_first': 1,
            'subunit': 'Cent',
            'iso_numeric': 840,
            'smallest_denomination': 1,
            'symbol': '$',
            'iso_code': 'USD',
            'decimal_mark': '.',
            'name': 'United States Dollar',
            'subunit_to_unit': 100,
            'alternate_symbols': ['US$'],
            'html_entity': '$',
            'disambiguate_symbol': 'US$',
            'thousands_separator': ','
        },
        'sun': {
            'set': {
                'apparent': 1480294200,
                'astronomical': 1480299780,
                'nautical': 1480297860,
                'civil': 1480295940
            },
            'rise': {
                'apparent': 1480345440,
                'astronomical': 1480339860,
                'nautical': 1480341720,
                'civil': 1480343700
            }
        },
        'qibla': 18.8,
        'DMS': {
            'lng': "122° 27' 46.76256'' W",
            'lat': "37° 45' 53.27748'' N"
        },
        'Mercator': {
            'y': 4520082.026,
            'x': -13632517.643
        },
        'callingcode': 1,
        'MGRS': '10SEG4729879855',
        'OSM': {
            'url': 'https://www.openstreetmap.org/?mlat=37.76480&mlon=-122.46299#map=17/37.76480/-122.46299',
            'edit_url': 'https://www.openstreetmap.org/edit?relation=396487#map=17/37.76480/-122.46299'
        },
        'timezone': {
            'short_name': 'PST',
            'offset_sec': -28800,
            'name': 'America/Los_Angeles',
            'offset_string': -800,
            'now_in_dst': 0
        },
        'geohash': '9q8yv6c5vsbd8mfjzezu',
        'Maidenhead': 'CM87ss43kn',
        'what3words': {
            'words': 'scope.exam.tulip'
        }
    },
    'confidence': 1,
    'bounds': {
        'northeast': {
            'lng': -122.2817799,
            'lat': 37.9298443
        },
        'southwest': {
            'lng': -123.1738249,
            'lat': 37.6403143
        }
    },
    'components': {
        'county': 'San Francisco City and County',
        'country': 'United States of America',
        '_type': 'county',
        'country_code': 'us',
        'state': 'California'
    }
}, {
    'formatted': 'San Francisco, Philippines',
    'geometry': {
        'lng': 125.9512492,
        'lat': 8.444585
    },
    'annotations': {
        'currency': {
            'symbol_first': 1,
            'subunit': 'Centavo',
            'smallest_denomination': 1,
            'symbol': '₱',
            'iso_code': 'PHP',
            'decimal_mark': '.',
            'name': 'Philippine Peso',
            'subunit_to_unit': 100,
            'alternate_symbols': ['PHP', 'PhP', 'P'],
            'html_entity': '&#x20B1;',
            'iso_numeric': 608,
            'thousands_separator': ','
        },
        'sun': {
            'set': {
                'apparent': 1480324560,
                'astronomical': 1480329000,
                'nautical': 1480327440,
                'civil': 1480325880
            },
            'rise': {
                'apparent': 1480368900,
                'astronomical': 1480364460,
                'nautical': 1480366020,
                'civil': 1480367580
            }
        },
        'qibla': 290.76,
        'DMS': {
            'lng': "125° 57' 4.49707'' E",
            'lat': "8° 26' 40.50600'' N"
        },
        'Mercator': {
            'y': 937198.302,
            'x': 14020828.924
        },
        'callingcode': 63,
        'MGRS': '51PZK2500134677',
        'OSM': {
            'url': 'https://www.openstreetmap.org/?mlat=8.44459&mlon=125.95125#map=17/8.44459/125.95125',
            'edit_url': 'https://www.openstreetmap.org/edit?relation=3870466#map=17/8.44459/125.95125'
        },
        'timezone': {
            'short_name': 'PHT',
            'offset_sec': 28800,
            'name': 'Asia/Manila',
            'offset_string': 800,
            'now_in_dst': 0
        },
        'geohash': 'wc98416ckbdremqx670t',
        'Maidenhead': 'PJ28xk46dq',
        'what3words': {
            'words': 'unseasoned.playlists.landlady'
        }
    },
    'confidence': 4,
    'bounds': {
        'northeast': {
            'lng': 126.04258,
            'lat': 8.566772
        },
        'southwest': {
            'lng': 125.862424,
            'lat': 8.3240049
        }
    },
    'components': {
        'county': 'San Francisco',
        'country': 'Philippines',
        '_type': 'county',
        'country_code': 'ph',
        'state': 'Agusan Del Sur'
    }
}, {
    'formatted': 'San Francisco, Guatemala',
    'geometry': {
        'lng': -90.0004401,
        'lat': 16.7480375
    },
    'annotations': {
        'currency': {
            'symbol_first': 1,
            'subunit': 'Centavo',
            'smallest_denomination': 1,
            'symbol': 'Q',
            'iso_code': 'GTQ',
            'decimal_mark': '.',
            'name': 'Guatemalan Quetzal',
            'subunit_to_unit': 100,
            'alternate_symbols': [],
            'html_entity': '',
            'iso_numeric': 320,
            'thousands_separator': ','
        },
        'sun': {
            'set': {
                'apparent': 1480375440,
                'astronomical': 1480293600,
                'nautical': 1480292040,
                'civil': 1480376820
            },
            'rise': {
                'apparent': 1480335060,
                'astronomical': 1480330500,
                'nautical': 1480332060,
                'civil': 1480333680
            }
        },
        'qibla': 53.89,
        'DMS': {
            'lng': "90° 0' 1.58453'' W",
            'lat': "16° 44' 52.93500'' N"
        },
        'Mercator': {
            'y': 1879208.54,
            'x': -10018803.168
        },
        'callingcode': 502,
        'MGRS': '15QZU1982954096',
        'OSM': {
            'url': 'https://www.openstreetmap.org/?mlat=16.74804&mlon=-90.00044#map=17/16.74804/-90.00044',
            'edit_url': 'https://www.openstreetmap.org/edit?relation=4558860#map=17/16.74804/-90.00044'
        },
        'timezone': {
            'short_name': 'CST',
            'offset_sec': -21600,
            'name': 'America/Guatemala',
            'offset_string': -600,
            'now_in_dst': 0
        },
        'geohash': '9fzzrbzsmsrz1tyrd1x0',
        'Maidenhead': 'EK46xr99wm',
        'what3words': {
            'words': 'interlaced.tropical.reefs'
        }
    },
    'confidence': 4,
    'bounds': {
        'northeast': {
            'lng': -89.8975314,
            'lat': 16.9345555
        },
        'southwest': {
            'lng': -90.1367184,
            'lat': 16.6410123
        }
    },
    'components': {
        'county': 'San Francisco',
        'country': 'Guatemala',
        '_type': 'county',
        'country_code': 'gt',
        'state': 'Petén'
    }
}, {
    'formatted': 'San Francisco, Honduras',
    'geometry': {
        'lng': -87.0173932,
        'lat': 15.6497222
    },
    'annotations': {
        'currency': {
            'symbol_first': 1,
            'subunit': 'Centavo',
            'iso_numeric': 340,
            'smallest_denomination': 5,
            'symbol': 'L',
            'iso_code': 'HNL',
            'decimal_mark': '.',
            'name': 'Honduran Lempira',
            'subunit_to_unit': 100,
            'alternate_symbols': [],
            'html_entity': '',
            'disambiguate_symbol': 'HNL',
            'thousands_separator': ','
        },
        'sun': {
            'set': {
                'apparent': 1480374840,
                'astronomical': 1480293000,
                'nautical': 1480291440,
                'civil': 1480376220
            },
            'rise': {
                'apparent': 1480334220,
                'astronomical': 1480329660,
                'nautical': 1480331280,
                'civil': 1480332840
            }
        },
        'qibla': 56.01,
        'DMS': {
            'lng': "87° 1' 2.61541'' W",
            'lat': "15° 38' 58.99974'' N"
        },
        'Mercator': {
            'y': 1752674.084,
            'x': -9686731.898
        },
        'callingcode': 504,
        'MGRS': '16PDC9813530190',
        'OSM': {
            'url': 'https://www.openstreetmap.org/?mlat=15.64972&mlon=-87.01739#map=17/15.64972/-87.01739',
            'edit_url': 'https://www.openstreetmap.org/edit?relation=6051824#map=17/15.64972/-87.01739'
        },
        'timezone': {
            'short_name': 'CST',
            'offset_sec': -21600,
            'name': 'America/Tegucigalpa',
            'offset_string': -600,
            'now_in_dst': 0
        },
        'geohash': 'd4f15bgy5z8ugjddv6qt',
        'Maidenhead': 'EK65lp75vw',
        'what3words': {
            'words': 'noneconomic.antacids.foreign'
        }
    },
    'confidence': 4,
    'bounds': {
        'northeast': {
            'lng': -86.953203,
            'lat': 15.7875447
        },
        'southwest': {
            'lng': -87.108576,
            'lat': 15.5120544
        }
    },
    'components': {
        'county': 'San Francisco',
        'country': 'Honduras',
        '_type': 'county',
        'country_code': 'hn',
        'state': 'Atlántida'
    }
}, {
    'formatted': 'San Francisco, Terrenos de la Ex-hacienda de Jamaya, Mexico',
    'geometry': {
        'lng': -97.5396999,
        'lat': 20.2947
    },
    'annotations': {
        'currency': {
            'symbol_first': 1,
            'subunit': 'Centavo',
            'iso_numeric': 484,
            'smallest_denomination': 5,
            'symbol': '$',
            'iso_code': 'MXN',
            'decimal_mark': '.',
            'name': 'Mexican Peso',
            'subunit_to_unit': 100,
            'alternate_symbols': ['MEX$'],
            'html_entity': '$',
            'disambiguate_symbol': 'MEX$',
            'thousands_separator': ','
        },
        'sun': {
            'set': {
                'apparent': 1480376880,
                'astronomical': 1480295160,
                'nautical': 1480293540,
                'civil': 1480291920
            },
            'rise': {
                'apparent': 1480337220,
                'astronomical': 1480332540,
                'nautical': 1480334160,
                'civil': 1480335840
            }
        },
        'qibla': 47.38,
        'DMS': {
            'lng': "97° 32' 22.91964'' W",
            'lat': "20° 17' 40.92000'' N"
        },
        'Mercator': {
            'y': 2293161.443,
            'x': -10858069.725
        },
        'callingcode': 52,
        'MGRS': '14QPH5248144767',
        'OSM': {
            'url': 'https://www.openstreetmap.org/?mlat=20.29470&mlon=-97.53970#map=17/20.29470/-97.53970',
            'edit_url': 'https://www.openstreetmap.org/edit?relation=4720121#map=17/20.29470/-97.53970'
        },
        'timezone': {
            'short_name': 'CST',
            'offset_sec': -21600,
            'name': 'America/Mexico_City',
            'offset_string': -600,
            'now_in_dst': 0
        },
        'geohash': '9gdekqtc0q230ff235dm',
        'Maidenhead': 'EL10fh50fr',
        'what3words': {
            'words': 'vilified.trial.unchosen'
        }
    },
    'confidence': 10,
    'bounds': {
        'northeast': {
            'lng': -97.5379902,
            'lat': 20.2968753
        },
        'southwest': {
            'lng': -97.5411951,
            'lat': 20.2928236
        }
    },
    'components': {
        'county': 'Terrenos de la Ex-hacienda de Jamaya',
        'country': 'Mexico',
        '_type': 'city',
        'city': 'San Francisco',
        'state': 'Veracruz',
        'country_code': 'mx'
    }
}, {
    'formatted': 'San Francisco, Muisne, Ecuador',
    'geometry': {
        'lng': -80.0661132,
        'lat': 0.6539774
    },
    'annotations': {
        'MGRS': '17NPA0391672293',
        'OSM': {
            'url': 'https://www.openstreetmap.org/?mlat=0.65398&mlon=-80.06611#map=17/0.65398/-80.06611',
            'edit_url': 'https://www.openstreetmap.org/edit?relation=3659105#map=17/0.65398/-80.06611'
        },
        'timezone': {
            'short_name': 'ECT',
            'offset_sec': -18000,
            'name': 'America/Guayaquil',
            'offset_string': -500,
            'now_in_dst': 0
        },
        'geohash': 'd0p5dp19sq4z5udmfckg',
        'qibla': 65.34,
        'DMS': {
            'lng': "80° 3' 58.00752'' W",
            'lat': "0° 39' 14.31864'' N"
        },
        'Maidenhead': 'EJ90xp26bw',
        'what3words': {
            'words': 'confederate.birthmarks.swallowing'
        },
        'Mercator': {
            'y': 72314.669,
            'x': -8912918.951
        },
        'callingcode': 593,
        'sun': {
            'set': {
                'apparent': 1480374600,
                'astronomical': 1480292700,
                'nautical': 1480377540,
                'civil': 1480375980
            },
            'rise': {
                'apparent': 1480331100,
                'astronomical': 1480326660,
                'nautical': 1480328220,
                'civil': 1480329780
            }
        }
    },
    'confidence': 4,
    'bounds': {
        'northeast': {
            'lng': -79.8966672,
            'lat': 0.7931309
        },
        'southwest': {
            'lng': -80.2042428,
            'lat': 0.5807154
        }
    },
    'components': {
        'county': 'Muisne',
        'country': 'Ecuador',
        '_type': 'city',
        'city': 'San Francisco',
        'state': 'Esmeraldas',
        'country_code': 'ec'
    }
}, {
    'formatted': 'Provincia San José, San Francisco, 10802 Costa Rica',
    'geometry': {
        'lng': -84.0718977,
        'lat': 9.9419793
    },
    'annotations': {
        'currency': {
            'symbol_first': 1,
            'subunit': 'Céntimo',
            'smallest_denomination': 500,
            'symbol': '₡',
            'iso_code': 'CRC',
            'decimal_mark': ',',
            'name': 'Costa Rican Colón',
            'subunit_to_unit': 100,
            'alternate_symbols': ['¢'],
            'html_entity': '&#x20A1;',
            'iso_numeric': 188,
            'thousands_separator': '.'
        },
        'sun': {
            'set': {
                'apparent': 1480374720,
                'astronomical': 1480292760,
                'nautical': 1480291200,
                'civil': 1480376040
            },
            'rise': {
                'apparent': 1480332960,
                'astronomical': 1480328520,
                'nautical': 1480330020,
                'civil': 1480331580
            }
        },
        'qibla': 59.82,
        'DMS': {
            'lng': "84° 4' 18.83172'' W",
            'lat': "9° 56' 31.12548'' N"
        },
        'Mercator': {
            'y': 1104959.808,
            'x': -9358840.842
        },
        'callingcode': 506,
        'MGRS': '16PHS2109500415',
        'OSM': {
            'url': 'https://www.openstreetmap.org/?mlat=9.94198&mlon=-84.07190#map=17/9.94198/-84.07190',
            'edit_url': 'https://www.openstreetmap.org/edit?relation=5413731#map=17/9.94198/-84.07190'
        },
        'timezone': {
            'short_name': 'CST',
            'offset_sec': -21600,
            'name': 'America/Costa_Rica',
            'offset_string': -600,
            'now_in_dst': 0
        },
        'geohash': 'd1u0wcusnz32we4ufpsn',
        'Maidenhead': 'EJ79xw16ib',
        'what3words': {
            'words': 'bottled.ferrets.warns'
        }
    },
    'confidence': 8,
    'bounds': {
        'northeast': {
            'lng': -84.0645107,
            'lat': 9.9449263
        },
        'southwest': {
            'lng': -84.0785165,
            'lat': 9.9390026
        }
    },
    'components': {
        'county': 'Cantón Goicoechea',
        'country': 'Costa Rica',
        '_type': 'city',
        'city': 'San Francisco',
        'postcode': '10802',
        'state': 'Provincia San José',
        'country_code': 'cr'
    }
}, {
    'formatted': 'Provincia Heredia, San Francisco, 40103 Costa Rica',
    'geometry': {
        'lng': -84.1279717,
        'lat': 9.9950234
    },
    'annotations': {
        'currency': {
            'symbol_first': 1,
            'subunit': 'Céntimo',
            'smallest_denomination': 500,
            'symbol': '₡',
            'iso_code': 'CRC',
            'decimal_mark': ',',
            'name': 'Costa Rican Colón',
            'subunit_to_unit': 100,
            'alternate_symbols': ['¢'],
            'html_entity': '&#x20A1;',
            'iso_numeric': 188,
            'thousands_separator': '.'
        },
        'sun': {
            'set': {
                'apparent': 1480374720,
                'astronomical': 1480292760,
                'nautical': 1480291200,
                'civil': 1480376040
            },
            'rise': {
                'apparent': 1480332960,
                'astronomical': 1480328520,
                'nautical': 1480330080,
                'civil': 1480331640
            }
        },
        'qibla': 59.77,
        'DMS': {
            'lng': "84° 7' 40.69812'' W",
            'lat': "9° 59' 42.08424'' N"
        },
        'Mercator': {
            'y': 1110916.221,
            'x': -9365082.971
        },
        'callingcode': 506,
        'MGRS': '16PHS1489006232',
        'OSM': {
            'url': 'https://www.openstreetmap.org/?mlat=9.99502&mlon=-84.12797#map=17/9.99502/-84.12797',
            'edit_url': 'https://www.openstreetmap.org/edit?relation=5640079#map=17/9.99502/-84.12797'
        },
        'timezone': {
            'short_name': 'CST',
            'offset_sec': -21600,
            'name': 'America/Costa_Rica',
            'offset_string': -600,
            'now_in_dst': 0
        },
        'geohash': 'd1u0veechpmsuz6eex9t',
        'Maidenhead': 'EJ79wx48pt',
        'what3words': {
            'words': 'quality.lights.bared'
        }
    },
    'confidence': 7,
    'bounds': {
        'northeast': {
            'lng': -84.1088393,
            'lat': 10.0001851
        },
        'southwest': {
            'lng': -84.1646163,
            'lat': 9.9709693
        }
    },
    'components': {
        'county': 'Cantón Heredia',
        'country': 'Costa Rica',
        '_type': 'city',
        'city': 'San Francisco',
        'postcode': '40103',
        'state': 'Provincia Heredia',
        'country_code': 'cr'
    }
}, {
    'formatted': 'Provincia Heredia, San Francisco, 40604 Costa Rica',
    'geometry': {
        'lng': -84.0710467,
        'lat': 10.0044725
    },
    'annotations': {
        'currency': {
            'symbol_first': 1,
            'subunit': 'Céntimo',
            'smallest_denomination': 500,
            'symbol': '₡',
            'iso_code': 'CRC',
            'decimal_mark': ',',
            'name': 'Costa Rican Colón',
            'subunit_to_unit': 100,
            'alternate_symbols': ['¢'],
            'html_entity': '&#x20A1;',
            'iso_numeric': 188,
            'thousands_separator': '.'
        },
        'sun': {
            'set': {
                'apparent': 1480374720,
                'astronomical': 1480292760,
                'nautical': 1480291200,
                'civil': 1480376040
            },
            'rise': {
                'apparent': 1480332960,
                'astronomical': 1480328520,
                'nautical': 1480330080,
                'civil': 1480331640
            }
        },
        'qibla': 59.79,
        'DMS': {
            'lng': "84° 4' 15.76812'' W",
            'lat': "10° 0' 16.10100'' N"
        },
        'Mercator': {
            'y': 1111977.38,
            'x': -9358746.109
        },
        'callingcode': 506,
        'MGRS': '16PHS2112807333',
        'OSM': {
            'url': 'https://www.openstreetmap.org/?mlat=10.00447&mlon=-84.07105#map=17/10.00447/-84.07105',
            'edit_url': 'https://www.openstreetmap.org/edit?relation=5731007#map=17/10.00447/-84.07105'
        },
        'timezone': {
            'short_name': 'CST',
            'offset_sec': -21600,
            'name': 'America/Costa_Rica',
            'offset_string': -600,
            'now_in_dst': 0
        },
        'geohash': 'd1u0yvm268u501zdssmz',
        'Maidenhead': 'EK70xa11lb',
        'what3words': {
            'words': 'frock.flashcards.case'
        }
    },
    'confidence': 7,
    'bounds': {
        'northeast': {
            'lng': -84.0554974,
            'lat': 10.0235949
        },
        'southwest': {
            'lng': -84.0759256,
            'lat': 9.9963333
        }
    },
    'components': {
        'county': 'Cantón San Isidro',
        'country': 'Costa Rica',
        '_type': 'city',
        'city': 'San Francisco',
        'postcode': '40604',
        'state': 'Provincia Heredia',
        'country_code': 'cr'
    }
}]
