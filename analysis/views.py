from .analysis import do_analysis

from rest_framework.decorators import parser_classes, api_view
from rest_framework.parsers import JSONParser
from rest_framework.response import Response
import threading
from yaml import safe_load


HE_ANALYSIS, RGB_ANALYSIS = "he", "rgb"


@api_view(['POST'])
@parser_classes([JSONParser])
def analyze(request):
    """
    Takes in an annotation group and the analyses to be performed on it,
    and starts the analyses.
    """
    with open('secrets.yml', 'r') as f:
        # TODO: Enter correct secrets
        host_info = safe_load(f)['host']
    try:
        analysis_id = request.data.get("analysisId")
        annotation_ids = request.data.get("annotations")
        analysis_names = request.data.get("analysis")
        args = (host_info, annotation_ids, analysis_names)
        analysis_thread = threading.Thread(target=do_analysis, args=args)
        return Response(status=202)
    except AttributeError as e:
        print(e)
        return Response(data=e, status=400)




