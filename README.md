# rabbitmq-redshift-streamer

A Storm topology to stream data from RabbitMQ to Redshift/Postgres.

## Installation

To get psycopg2 to work, install the following packages (Ubuntu):

```bash
sudo apt-get install libpq-dev python-dev
```

Now, install the required packages (in a virtualenv preferably):

```bash
pip install -r virtualenvs/requirements.txt
```

## Creating Tables

Run the sql file `schema/tables.sql` against your database to create the tables
necessary for running this example.

## Running Topology

Make sure to set the environment variables for your db instance (`RS_DBNAME`,
`RS_HOST`, `RS_PORT`, `RS_USER`, `RS_PASS`) as well as your RabbitMQ instance
(`RABBITMQ_SCHEME`). It will connect to your local instance (if any) by default.

### Local

To run the topology in your local machine, do:

```bash
cd rabbitmq-redshift-streamer
sparse run
```

### Production

To submit the topology to a production cluster, do:

```bash
sparse submit
```

## Feeding Data

To see the topology in action, feed data to a RabbitMQ queue `users` as json:
```
{"id": "<user-id>", "name": "<user-name>"}
```
