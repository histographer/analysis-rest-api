from histographer.analysis.image.high_level import image_analysis
import json
import requests


def do_analysis(analysis_id, annotation_ids, analysis_names, host_info):
    url = "http://digipat.no/analysisResults"
    args = (host_info, annotation_ids, analysis_names)
    try:
        results = image_analysis(analysis_id, annotation_ids, analysis_names, host_info)
        response = requests.post(url, data=json.dumps(results))
    except ConnectionError as e:
        # TODO: Send different request to a different URL, details will be declared later
        response = requests.post(url, data="502 – Error during analysis.")
    # TODO: Other errors we should handle, or just have a generic except instead?




