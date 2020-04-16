from .analysis import do_analysis, get_available_analyses

from rest_framework.decorators import parser_classes, api_view
from rest_framework.parsers import JSONParser
from rest_framework.response import Response
import threading
import os


@api_view(['POST'])
@parser_classes([JSONParser])
def analyze(request):
    """
    Takes in an annotation group and the analyses to be performed on it,
    and starts the analyses.
    """
    host_info = {
        "host": os.getenv("CYTOMINE_TOP_URL"),
        "public_key": os.getenv("CYTOMINE_PUBLIC_KEY"),
        "private_key": os.getenv("CYTOMINE_PRIVATE_KEY"),
        "project_id": request.data.get("projectId")
    }
    analysis_id = request.data.get("analysisId")
    annotation_ids = request.data.get("annotations")
    analysis_names = request.data.get("analysis")
    callback_urls = request.data.get("callbackURLs")
    analysis_results_url = callback_urls.get("analysisResults")
    update_status_url = callback_urls.get("updateStatus")

    # Check that all arguments have been provided and start analysis
    args = (analysis_id, annotation_ids, analysis_names, host_info, analysis_results_url, update_status_url)
    if all(args):
        analysis_thread = threading.Thread(target=do_analysis, args=args)
        analysis_thread.start()
        return Response(status=202)
    else:
        return Response(data=request.data, status=400)


@api_view(['GET'])
def available_analyses(request):
    return Response(data={"names": get_available_analyses()})
