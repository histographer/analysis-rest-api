from histographer.analysis.image.high_level import image_analysis
import json
import requests
from .encode import dict_list_to_csv, recursive_flatten
import traceback


def do_analysis(project_id, analysis_id, annotation_ids, analysis_names, host_info, analysis_results_url, update_status_url):
    try:
        url = f"{analysis_results_url}"
        results = image_analysis(host_info, annotation_ids, analysis_names)  # TODO: image_analysis(project_id, ...)
        csv = dict_list_to_csv(recursive_flatten(results))
        data = {
            "analysisId": analysis_id,
            "csv": csv,
            "annotations": results
        }
        print(data)
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
