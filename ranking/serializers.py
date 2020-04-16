def parse_comparisons(request_data):
    image_ids = request_data.get("image_ids")
    comparison_data = request_data.get("comparison_data")
    skipped_data = request_data.get("skipped")
    # Parse comparison data JSON objects to list of tuples
    comparisons = []
    for item in comparison_data:
        winner = item.get('winner').get('id')
        loser = item.get('loser').get('id')
        pair = (winner, loser)
        comparisons.append(pair)
    # Parse "skipped" list of lists to list of tuples:
    skipped = []
    for pair in skipped_data:
        skipped.append(tuple(pair))
    return image_ids, comparisons, skipped

