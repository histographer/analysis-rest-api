from rest_framework.decorators import api_view
from rest_framework.decorators import parser_classes
from rest_framework.parsers import JSONParser
from rest_framework.response import Response
from .ranking import random_pair


@api_view(['POST'])
@parser_classes([JSONParser])
#@renderer_classes([JSONRenderer])
#@authentication_classes(...)
def suggest_pair(request):
    """
    Suggests a new pair for comparison. Currently returns a random pair.
    """
    number_of_items = request.data.get("number_of_items")
    comparison_data = request.data.get("comparison_data")
    pairs = []
    for item in comparison_data:
        if item == 'id':
            pass
        chosen = item.get('chosen').get('id')
        other = item.get('other').get('id')
        pair = (chosen, other)
        pairs.append(pair)
    pair = random_pair(number_of_items)
    response = {'left': {'id': pair[0]}, 'right': {'id': pair[1]}}
    return Response(response)