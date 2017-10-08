from sodapy import Socrata
import csv
import bigquery


class MapData(object):

    def get_unique_locations(self):
        # Unauthenticated client only works with public data sets. Note 'None'
        # in place of application token, and no username or password:
        client = Socrata("data.melbourne.vic.gov.au", None)

        # Example authenticated client (needed for non-public datasets):
        # client = Socrata(data.melbourne.vic.gov.au,
        #                  MyAppToken,
        #                  userame="user@example.com",
        #                  password="AFakePassword")

        # First 2000 results, returned as JSON from API / converted to Python list of
        # dictionaries by sodapy.
        results = client.get("mxb8-wn4w", limit=1000)

        locations = set()
        for value in results:
            for key in value:
                if 'sensor_name' in key:
                    locations.add(value[key])

        """
        feature_collection = []
        for location in locations:
            print locations
            location.append
        """
        print locations
        return None


    def get_average_daily_traffic(self):

        location_data = []
        f = open('location_data.csv', 'rt')

        try:
            reader = csv.reader(f)
            for row in reader:
                location_data.append(row)
        finally:
            f.close()

        avg_data = bigquery.BigQuery().get_average_daily()

        new_location_data = []
        for data in location_data:
            for avg in avg_data:
                if data[0] in avg['sensor_name']:
                    new_location_data.append([
                        data[0],
                        avg['count'],
                        data[1],
                        data[2],
                    ])

        return new_location_data
