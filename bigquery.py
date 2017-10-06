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
