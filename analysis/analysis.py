from histographer.analysis.image.high_level import image_analysis
import json
import requests
from .encode import dict_list_to_csv_b64
import os
import traceback

WIZARD_BACKEND_URL = os.getenv("WIZARD_BACKEND_URL")


def do_analysis(analysis_id, annotation_ids, analysis_names, host_info):
    args = (host_info, annotation_ids, analysis_names)
    try:
        # TODO: WIZARD_BACKEND_URL as environment variable in .env
        # url = f"{WIZARD_BACKEND_URL}/analysisResults"
        results = image_analysis(host_info, annotation_ids, analysis_names)
        csv_b64 = dict_list_to_csv_b64(results).decode()
        data = {
            "csvBase64": csv_b64,
            "analysisId": analysis_id,
            "annotations": results
        }
        print(data)
    #    response = requests.post(url, data=json.dumps(data))
    except Exception:
        # TODO: More sophisticated error handling/logging?
        print(f"Exception: {traceback.format_exc()}")

        # url = f"{WIZARD_BACKEND_URL}/analysisInfo" TODO: Check that this endpoint is correct
        data = {"status": "failure"}
        print(data)
        # response = requests.post(url, data=json.dumps(data)
