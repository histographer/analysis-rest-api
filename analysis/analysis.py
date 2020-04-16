import histographer.analysis.image.analysis as image_analysis_module
from histographer.analysis.image.high_level import image_analysis
import inspect
import json
import requests
import traceback


def do_analysis(analysis_id, annotation_ids, analysis_names, host_info, analysis_results_url, update_status_url):
    try:
        url = f"{analysis_results_url}"
        results = image_analysis(host_info, annotation_ids, analysis_names)
        data = {
            "analysisId": analysis_id,
            "annotations": results
        }
        print(f"Data: {data}")
        response = requests.post(url, data=json.dumps(data))
    except Exception:
        # TODO: More sophisticated error handling/logging?
        print(f"Exception: {traceback.format_exc()}")
        url = f"{update_status_url}"
        data = {
            "analysisId": analysis_id,
            "status": "failure"
        }
        print(data)
        response = requests.post(url, data=json.dumps(data))
    # TODO: Error handling/raising if unable to send request to middleware?
    # if response.status_code == 200:
    #     pass
    # else:
    #     pass


def get_available_analyses():
    """
    Assumes that the image analysis module of histographer only contains valid image analysis functions,
    and that internal functions start with underscore.

    :return: List of strings with names of available analyses
    """
    available_analyses = []
    for name, func in inspect.getmembers(image_analysis_module, inspect.isfunction):
        if func.__module__ == image_analysis_module.__name__ and not name.startswith("_"):
            available_analyses.append(name)
    return available_analyses
