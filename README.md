# Analysis REST API

The API is divided in to two parts, `ranking` and `analysis`. 

## Ranking

The `ranking` part provides services for the DigiPat comparison app. 

Available endpoints:

### Suggest pair
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

Response:

```json
{
    "pair": [
        38,
        99
    ]
}
```

## Analysis
The `analysis` part provides services for the DigiPat quality analysis app.

Available endpoints:

None so far.