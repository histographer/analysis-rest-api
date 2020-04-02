from histographer.analysis.image.high_level import image_analysis
import json
import requests
from analysis.encode import dict_list_to_csv_b64


def do_analysis(analysis_id, annotation_ids, analysis_names, host_info):
    print(analysis_id, annotation_ids, analysis_names, host_info)
    #url = "http://??.digipat.no/analysisResults"
    args = (host_info, annotation_ids, analysis_names)
    try:
        results = image_analysis(host_info, annotation_ids, analysis_names)
        csv_b64 = dict_list_to_csv_b64(results)
        print(results)
    #    # TODO: Send b64 encoded CSV
    #    response = requests.post(url, data=json.dumps(results))
    except ConnectionError as e:
        print(e)
    #    # TODO: Send different request to a different URL, details will be declared later
    #    response = requests.post(url, data="502 – Error during analysis.")
    # TODO: Other errors we should handle, or just have a generic except instead?




