# Analysis REST API

The API is divided in to two parts, `ranking` and `analysis`. 

## Ranking

The `ranking` part provides services for the DigiPat comparison app. 

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
The `analysis` part provides services for the DigiPat quality analysis app.

Available endpoints:

None so far.