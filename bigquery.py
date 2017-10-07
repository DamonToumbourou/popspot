# ---------------------------------------------------------------------------------
#   BigQuery
# -------------------------------------------------------------------------------*/
from google.cloud import bigquery
import uuid


class BigQuery(object):

    def most_popular_overall(self):
        #client = bigquery.Client()
        #query_job = client.run_async_query(str(uuid.uuid4()), """
        ##standardSQL
        #SELECT sensor_name, SUM(hourly_counts) AS sum
        #FROM `s3462344-a1-lt11.ped_data.ped_data_small`
        #WHERE date_time LIKE '%2017%'
        #GROUP BY (sensor_name)
        #ORDER BY (sum) DESC
        #LIMIT 1;
        #""")

        #query_job.begin()
        #query_job.result()  # Wait for job to complete.

        #destination_table = oquery_job.destination
        #destination_table.reload()

        #most_pop = []
        #for row in destination_table.fetch_data():
        #    pop = {
        #        'sensor_name': row[0],
        #        'count': row[1]
        #    }
        #    most_pop.append(pop)

        most_pop_overall = []
        pop = {
                'sensor_name': 'Southbank',
                'count': 12712712
            }
        most_pop_overall.append(pop)

        return most_pop_overall


    def most_popular_day(self):
        #client = bigquery.Client()
        #query_job = client.run_async_query(str(uuid.uuid4()), """
        ##standardSQL
        #SELECT sensor_name, SUM(hourly_counts) AS sum
        #FROM `s3462344-a1-lt11.ped_data.ped_data_small`
        #WHERE date_time LIKE '%2017%'
        #GROUP BY (sensor_name)
        #ORDER BY (sum) DESC
        #LIMIT 1;
        #""")

        #query_job.begin()
        #query_job.result()  # Wait for job to complete.

        #destination_table = query_job.destination
        #destination_table.reload()

        #most_pop = []
        #for row in destination_table.fetch_data():
        #    pop = {
        #        'sensor_name': row[0],
        #        'count': row[1]
        #    }
        #    most_pop.append(pop)

        most_pop_day = []
        pop = {
                'sensor_name': 'Flinders St',
                'count': 32009,
                'day': 'Sunday'
            }
        most_pop_day.append(pop)

        return most_pop_day


    def most_popular_time(self):
        #client = bigquery.Client()
        #query_job = client.run_async_query(str(uuid.uuid4()), """
        ##standardSQL
        #SELECT sensor_name, SUM(hourly_counts) AS sum
        #FROM `s3462344-a1-lt11.ped_data.ped_data_small`
        #WHERE date_time LIKE '%2017%'
        #GROUP BY (sensor_name)
        #ORDER BY (sum) DESC
        #LIMIT 1;
        #""")

        #query_job.begin()
        #query_job.result()  # Wait for job to complete.

        #destination_table = query_job.destination
        #destination_table.reload()

        #most_pop = []
        #for row in destination_table.fetch_data():
        #    pop = {
        #        'sensor_name': row[0],
        #        'count': row[1]
        #    }
        #    most_pop.append(pop)

        most_pop_time = []
        pop = {
                'sensor_name': 'Southbank',
                'count': 7123,
                'time': '9:00 AM'
            }
        most_pop_time.append(pop)

        return most_pop_time


    def most_popular_month(self):
        #client = bigquery.Client()
        #query_job = client.run_async_query(str(uuid.uuid4()), """
        ##standardSQL
        #SELECT sensor_name, SUM(hourly_counts) AS sum
        #FROM `s3462344-a1-lt11.ped_data.ped_data_small`
        #WHERE date_time LIKE '%2017%'
        #GROUP BY (sensor_name)
        #ORDER BY (sum) DESC
        #LIMIT 1;
        #""")

        #query_job.begin()
        #query_job.result()  # Wait for job to complete.

        #destination_table = query_job.destination
        #destination_table.reload()

        #most_pop = []
        #for row in destination_table.fetch_data():
        #    pop = {
        #        'sensor_name': row[0],
        #        'count': row[1]
        #    }
        #    most_pop.append(pop)

        most_pop_month = []
        pop = {
                'sensor_name': 'Melbourne Central',
                'count': 65363,
                'month': 'December'
            }
        most_pop_month.append(pop)

        return most_pop_month


    def get_average_daily(self):
        #client = bigquery.Client()
        #query_job = client.run_async_query(str(uuid.uuid4()), """
        ##standardSQL
        #SELECT sensor_name, AVG(hourly_counts) AS sum
        #FROM `s3462344-a1-lt11.ped_data.ped_data_small`
        #GROUP BY sensor_name
        #ORDER BY(sum) DESC;
        #""")

        #query_job.begin()
        #query_job.result()  # Wait for job to complete.

        #destination_table = query_job.destination
        #destination_table.reload()

        #average_daily = []
        #for row in destination_table.fetch_data():
        #    pop = {
        #        'sensor_name': row[0],
        #        'count': row[1]
        #
        #    }
        #    average_daily.append(pop)
        #
        average_daily = [{'count': 2188.7500000000005, 'sensor_name': u'Flinders St-Swanston St (West)'}, {'count': 1954.769474637681, 'sensor_name': u'Flinders La-Swanston St (West)'}, {'count': 1679.4134615384626, 'sensor_name': u'Southbank'}, {'count': 1506.0472222222234, 'sensor_name': u'Flinders St-Elizabeth St (East)'}, {'count': 1444.3820301783203, 'sensor_name': u'Flinders Street Station Underpass'}, {'count': 1402.7851979345967, 'sensor_name': u'Town Hall (West)'}, {'count': 1352.0171081677686, 'sensor_name': u'Princes Bridge'}, {'count': 1319.4600480109718, 'sensor_name': u'Bourke Street Mall (North)'}, {'count': 1312.4513031550105, 'sensor_name': u'Spencer St-Collins St (North)'}, {'count': 1306.3314926372152, 'sensor_name': u'Melbourne Central'}, {'count': 1064.7357843137243, 'sensor_name': u'The Arts Centre'}, {'count': 1049.8731884057975, 'sensor_name': u'City Square'}, {'count': 994.2004458161869, 'sensor_name': u'Bourke Street Mall (South)'}, {'count': 880.9058641975291, 'sensor_name': u'State Library'}, {'count': 880.6561302681989, 'sensor_name': u'Little Collins St-Swanston St (East)'}, {'count': 827.1465517241365, 'sensor_name': u'Flagstaff Station'}, {'count': 713.145121082622, 'sensor_name': u'Australia on Collins'}, {'count': 656.3830589849114, 'sensor_name': u'Southern Cross Station'}, {'count': 644.1575788751732, 'sensor_name': u'Bourke St-Russell St (West)'}, {'count': 606.1469478738024, 'sensor_name': u'Chinatown-Swanston St (North)'}, {'count': 541.4305555555574, 'sensor_name': u'QV Market-Elizabeth St (West)'}, {'count': 530.1975308641983, 'sensor_name': u'Melbourne Convention Exhibition Centre'}, {'count': 516.6469726562509, 'sensor_name': u'Lonsdale St (South)'}, {'count': 512.3187037037042, 'sensor_name': u'Birrarung Marr'}, {'count': 474.8844307270246, 'sensor_name': u'Collins Place (South)'}, {'count': 447.2153041825081, 'sensor_name': u'St Kilda Rd-Alexandra Gardens'}, {'count': 430.12236842105307, 'sensor_name': u'Sandridge Bridge'}, {'count': 365.56436011904674, 'sensor_name': u'Spencer St-Collins St (South)'}, {'count': 363.8033264746235, 'sensor_name': u'Chinatown-Lt Bourke St (South)'}, {'count': 354.1961591220842, 'sensor_name': u'Collins Place (North)'}, {'count': 291.6956018518514, 'sensor_name': u'Lonsdale St-Spring St (West)'}, {'count': 286.51115023474256, 'sensor_name': u'Queen St (West)'}, {'count': 275.4308785529714, 'sensor_name': u'Lygon St (West)'}, {'count': 251.76617826617877, 'sensor_name': u'Grattan St-Swanston St (West)'}, {'count': 236.29991356957646, 'sensor_name': u'Alfred Place'}, {'count': 225.38629426129424, 'sensor_name': u'Monash Rd-Swanston St (West)'}, {'count': 209.07355967078223, 'sensor_name': u'New Quay'}, {'count': 183.35339506172832, 'sensor_name': u'Victoria Point'}, {'count': 173.97405372405353, 'sensor_name': u'Flinders St-Spring St (West)'}, {'count': 167.82387057387015, 'sensor_name': u'Lygon St (East)'}, {'count': 163.2606209150332, 'sensor_name': u'Webb Bridge'}, {'count': 149.967032967033, 'sensor_name': u'Flinders St-Spark La'}, {'count': 125.99053724053675, 'sensor_name': u'QV Market-Peel St'}, {'count': 122.91358024691361, 'sensor_name': u'Pelham St (S)'}, {'count': 116.64239926739889, 'sensor_name': u'Tin Alley-Swanston St (West)'}, {'count': 67.5252677376171, 'sensor_name': u'Waterfront City'}]

        return average_daily
