from airflow.decorators import task, dag
from pendulum import datetime
import requests


doc_md_DAG = """
### The Activity DAG: great thing

This DAG will help me decide what to do today. It uses the [BoredAPI](https://www.boredapi.com/) to do so. Very cool!

Before I get to do the activity I will have to:

- Clean up the kitchen.
- Check on my pipelines.
- Water the plants.

Here are some happy plants:

<img src="https://www.publicdomainpictures.net/pictures/80000/velka/succulent-roses-echeveria.jpg" alt="plants" width="300"/>
"""


@dag(
    start_date=datetime(2022,11,1),
    schedule="@daily",
    catchup=False,
    doc_md=doc_md_DAG
)
def docs_example_dag():

    @task
    def tell_me_what_to_do():
        response = requests.get("https://www.boredapi.com/api/activity")
        return response.json()["activity"]

    tell_me_what_to_do()

docs_example_dag()
