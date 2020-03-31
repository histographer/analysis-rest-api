from rest_framework.decorators import parser_classes, api_view
from rest_framework.parsers import JSONParser
from rest_framework.response import Response

HE_ANALYSIS, RGB_ANALYSIS = "he", "rgb"


@api_view(['POST'])
@parser_classes([JSONParser])
def analyze(request):
    """
    Takes in an annotation group and the analyses to be performed on it,
    and starts the analyses.
    """
    group_id = request.data.get("group_id")
    annotation_ids = request.data.get("annotations")
    analyses = request.data.get("analysis")
    if HE_ANALYSIS in analyses:
        pass
        # start_he_analysis(group_id, annotation_ids)
    if RGB_ANALYSIS in analyses:
        pass
        # start_rgb_analysis(group_id, annotation_ids)
    return Response(status=202)
