# ---------------------------------------------------------------------------------
#   BigQuery
# -------------------------------------------------------------------------------*/
from google.cloud import bigquery
import uuid

class BigQuery(object):

    def most_popular(self):
        client = bigquery.Client()
        query_job = client.run_async_query(str(uuid.uuid4()), """
        #standardSQL
        SELECT ID, Sensor_Name
        FROM `s3462344-a1-lt11.ped_data.ped_data_small`
        LIMIT 5   
        """)

        query_job.begin()
        query_job.result()  # Wait for job to complete.

        destination_table = query_job.destination
        destination_table.reload()
        for row in destination_table.fetch_data():
            print(row)
