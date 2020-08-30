# Landwatch

A project to aggregate, query, and display property listings based on demographics, climate, topography, and other features.

Checkout the [Backlog](./planning.org) to see planning and progress. 

## Services

* [Zip Code Demographics](./demographics "Demographics")
* [Property Listings](./scrape_landandfarm "Listings")
* [Weather History](./noaa_weather "Weather")

## Run

This project uses [Docker](https://docs.docker.com/ "Docker Documentation") and[Docker Compose](https://github.com/docker/compose "Docker Compose Repository"). Please install and configure these as you see fit.

In the top level directory, run the following command to start:

```shell
docker-compose up --build
```

## Access

While development of the dashboard is in progress, please use pgAdmin to access the PostgreSQL data served to your [browser](http://localhost:8080 "Landwatch Pgadmin")

Use email "admin@email.com" and password "secret" to login.

Once logged in, you should see the pgAdmin dashboard.

Now, to add the PostgreSQL server running as a Docker container, right click on **Servers**, and then go to **Create** > **Server...**

In the **General** tab, type in your server **Name**.

Now, go to the **Connection** tab and type in pgsql-server as **Host name/address**, 5432 as **Port**, postgres as **Maintenance database**, postgres as **Username**, postgres as **Password** and check **Save password?** checkbox. Then, click on **Save**.

Click on **Servers** > **server-name** > **Databases** > **landwatch** > **Schemas** > **public** > **Tables** to see the available tables.

In the top toolbar select **Tools** > **Query Tool** and try running the following queries to see Beverly Hills data:

```sql
select * from zip_codes order by 90210;
```

```sql
select * from zip_demographics order by 90210;
```

```sql
select * from zip_households order by 90210;
```