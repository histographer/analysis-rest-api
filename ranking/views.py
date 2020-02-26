from rest_framework.decorators import api_view
from rest_framework.decorators import parser_classes
from rest_framework.parsers import JSONParser
from rest_framework.response import Response
from histographer.analysis.ranking.high_level import suggest_pair as new_pair


@api_view(['POST'])
@parser_classes([JSONParser])
#@renderer_classes([JSONRenderer])
#@authentication_classes(...)
def suggest_pair(request):
    """
    Suggests a new pair for comparison.
    """
    image_ids = request.data.get("image_ids")
    comparison_data = request.data.get("comparison_data")
    comparisons = []
    for item in comparison_data:
        winner = item.get('winner').get('id')
        loser = item.get('loser').get('id')
        pair = (winner, loser)
        comparisons.append(pair)

    pair = new_pair(image_ids, comparisons)  # tuple left right

    response = {'pair': pair}
    return Response(response)



