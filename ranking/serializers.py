def parse_comparisons(request_data):
    image_ids = request_data.get("image_ids")
    comparison_data = request_data.get("comparison_data")
    comparisons = []
    for item in comparison_data:
        winner = item.get('winner').get('id')
        loser = item.get('loser').get('id')
        pair = (winner, loser)
        comparisons.append(pair)
    return image_ids, comparisons

