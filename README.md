# Installation
- Create a copy of `env.sample` called `.env`
- Fill the `.env` where appropriate

Run with `docker-compose up -d`. 

# Analysis REST API

The API is divided in to two parts, `ranking` and `analysis`. 

## Ranking

The `ranking` part provides services for the DigiPat Comparison application. 

Available endpoints:

### Suggest pair
Suggests a new pair for comparison, given a list of ids and a list of comparisons. The new pair is selected to maximize the information gathered for establishing a ranking.  

Endpoint: `POST /ranking/suggestpair`

Sample API call:
```json
{
   "image_ids":[
      48,
      38,
      99,
      6
   ],
   "comparison_data":[
      {
         "winner":{
            "id":48
         },
         "loser":{
            "id":99
         }
      },
      {
         "winner":{
            "id":48
         },
         "loser":{
            "id":38
         }
      }
   ],
   "skipped":[
      [38, 6]
   ] 
}
```

Sample response:

```json
{
    "pair": [
        38,
        99
    ]
}
```

### Ranking
Provides an *ascending* ranking of all the provided ids and their corresponding scores, given a list of ids and a list of comparisons.

Endpoint: `POST /ranking/ranking`

Sample API call:
```json
{
   "image_ids":[
      48,
      38,
      99
   ],
   "comparison_data":[
      {
         "winner":{
            "id":48
         },
         "loser":{
            "id":99
         }
      },
      {
         "winner":{
            "id":48
         },
         "loser":{
            "id":38
         }
      }
   ]
}
```

Sample response:
```json
{
    "ranking": [
        99,
        38,
        48
    ],
    "scores": [
        {
            "id": 48,
            "score": 1503.8987706591831
        },
        {
            "id": 38,
            "score": 903.8987706591831
        },
        {
            "id": 99,
            "score": 800.0
        }
    ]
}
```


## Analysis
The `analysis` part provides services for the DigiPat Wizard application.

Available endpoints:

### Available analyses
Returns the names of the analyses which are available.

Endpoint: `GET /analysis/available`

Response:

```json
{
  "names": ["he"]
}
```


### Analyze
Starts image analysis of the provided annotations, and sends the results to a provided URL when they are ready. The annotations must be from images in the same project, and there should only be one annotation per image. 

Endpoint: `POST /analysis/analyze`

Sample API call:
```json
{
    "projectId": 385494,
    "analysisId": 41,
    "annotations": [1064743, 1064530],
    "analysis": ["he"],
    "callbackURLs":{
           "analysisResults": "http://wizard.backend.digipat.no/analysisResults",
           "updateStatus": "http://wizard.backend.digipat.no/analysisInformation"
           }
}
```

Response: 202 OK

When the analysis backend is finished with all the requested analyses, it sends a POST request the provided callback URL "analysisResults":

```JSON
{
   "analysisId":41,
   "csv":",annotationId,results.he.H.mean,results.he.H.std,results.he.E.mean,results.he.E.std\n0,1064743,-0.4473969270406818,0.08928628449947516,0.1478200208776022,0.019399876935551147\n1,1064530,-0.3968743544823937,0.0949864049320937,0.15373742180669883,0.016764408372085374\n",
   "annotations":[
      {
         "annotationId":1064743,
         "results":{
            "he":{
               "H":{
                  "mean":-0.4473969270406818,
                  "std":0.08928628449947516
               },
               "E":{
                  "mean":0.1478200208776022,
                  "std":0.019399876935551147
               }
            }
         }
      },
      {
         "annotationId":1064530,
         "results":{
            "he":{
               "H":{
                  "mean":-0.3968743544823937,
                  "std":0.0949864049320937
               },
               "E":{
                  "mean":0.15373742180669883,
                  "std":0.016764408372085374
               }
            }
         }
      }
   ]
}
```

If the analysis fails, the following is sent to the provided callback URL "updateStatus":

```JSON
{
   "analysisId": 41, 
   "status": "failure"
}
