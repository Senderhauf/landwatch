#NOAA Weather

This directory contains data and the means to gather it from NOAA

The data is availab e at NOAA's [Climate Data Online Search](https://www.ncdc.noaa.gov/cdo-web/search)

See this directorys [Org-mode](./planning.org) to see planning and progress. 

##NOAA API

See documentation at [https://www.ncdc.noaa.gov/cdo-web/webservices/v2](https://www.ncdc.noaa.gov/cdo-web/webservices/v2)

API Call

```shell
curl -H "token:QYumHTESHvMktBsArZIjYseYqPxbHiom" "https://www.ncdc.noaa.gov/cdo-web/api/v2/datatypes" | json_pp
```

Output (truncated)

```json
{
   "metadata" : {
         "resultset" : {
           "count" : 1532,
           "limit" : 25,
           "offset" : 1
         }
            
   },
   "results" : [
      {
        "datacoverage" : 1,
        "id" : "ACMC",
        "maxdate" : "1996-05-28",
        "mindate" : "1994-03-19",
        "name" : "Average cloudiness midnight to midnight from 30-second ceilometer data"
      },
      {
        "datacoverage" : 1,
        "id" : "ACMH",
        "maxdate" : "2005-12-31",
        "mindate" : "1965-01-01",
        "name" : "Average cloudiness midnight to midnight from manual observations"
      },
      {
        "datacoverage" : 1,
        "id" : "ACSC",
        "maxdate" : "1996-05-28",
        "mindate" : "1994-02-01",
        "name" : "Average cloudiness sunrise to sunset from 30-second ceilometer data"
      }
  ]
}
```

API call

```shell
 curl -H "token:QYumHTESHvMktBsArZIjYseYqPxbHiom" "https://www.ncdc.noaa.gov/cdo-web/api/v2/data?datasetid=GSOM&startdate=2010-01-01&enddate=2010-01-01&locationid=FIPS:US&locationid=ZIP:00001" | json_pp
```

Output (truncated)

```json
{
   "metadata" : {
      "resultset" : {
          "count" : 292495,
          "limit" : 25,
          "offset" : 1
      }
   },
    "results" : [
        {
           "attributes" : ",0",
            "datatype" : "DP01",
            "date" : "2010-01-01T00:00:00",
            "station" : "GHCND:AQC00914000",
            "value" : 28

        },
        {
            "attributes" : ",0",
            "datatype" : "DP10",
            "date" : "2010-01-01T00:00:00",
            "station" : "GHCND:AQC00914000",
            "value" : 28
        },
        {
            "attributes" : ",0",
            "datatype" : "DP1X",
            "date" : "2010-01-01T00:00:00",
            "station" : "GHCND:AQC00914000",
            "value" : 6

        }

    ]
}

```
