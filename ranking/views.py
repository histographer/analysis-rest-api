from rest_framework.decorators import api_view
from rest_framework.decorators import parser_classes
from rest_framework.parsers import JSONParser
from rest_framework.response import Response
from histographer.analysis.ranking.high_level import suggest_pair as new_pair
from histographer.analysis.ranking.high_level import compute_elo_scores
from ranking.serializers import parse_comparisons
import numpy as np


@api_view(['POST'])
@parser_classes([JSONParser])
def suggest_pair(request):
    """
    Suggests a new pair for comparison.
    """
    image_ids, comparisons, skipped = parse_comparisons(request.data)
    try:
        pair = new_pair(image_ids, comparisons, skipped)  # tuple left right
        response = {'pair': pair}
        return Response(response)
    except ValueError as e:
        return Response(data=str(e), status=404)


@api_view(['POST'])
@parser_classes([JSONParser])
def ranking(request):
    """Get the ranked order of """
    image_ids, comparisons, skipped = parse_comparisons(request.data)
    scores = compute_elo_scores(image_ids, comparisons)
    ranked = list(np.array(image_ids)[np.argsort(scores)])
    response = {
        'ranking': ranked,
        'scores': [
            {
                'id': i,
                'score': score
            }
            for i, score in zip(image_ids, scores)
        ]
    }
    return Response(response)
