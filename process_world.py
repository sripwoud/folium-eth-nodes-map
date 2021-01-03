import json
from shapely.geometry import shape, Point
from numpy import quantile


def count_nodes_per_polygon(
    coords,
    original_world_geojson_path="data/world.json",
    enriched_world_json_path="data/enriched_world.json",
):
    with open(original_world_geojson_path, encoding="utf-8-sig") as f:
        geo_data = json.load(f)

        for feature in geo_data["features"]:
            feature["properties"]["nodes_count"] = 0
            polygon = shape(feature["geometry"])

            for i, latitude, longitude in coords.itertuples():
                point = Point(longitude, latitude)  # lat,lon
                if polygon.contains(point):
                    feature["properties"]["nodes_count"] += 1

        nodes_counts = [
            feature["properties"]["nodes_count"] for feature in geo_data["features"]
        ]

        min_nodes_count = min(nodes_counts)
        max_nodes_count = max(nodes_counts)
        width = max_nodes_count - min_nodes_count
        scaled_nodes_counts = [
            (nodes_count - min_nodes_count) / width for nodes_count in nodes_counts
        ]

        for feature, scaled_nodes_count in zip(
            geo_data["features"], scaled_nodes_counts
        ):
            feature["properties"]["scaled_nodes_count"] = scaled_nodes_count

        with open(enriched_world_json_path, "w") as enriched_f:
            enriched_f.write(json.dumps(geo_data))
            enriched_f.close()

        f.close()


def _nodes_counts_quantiles(path):
    with open(path, encoding="utf-8-sig") as f:
        data = json.load(f)
        scaled_nodes_counts = [
            feature["properties"]["scaled_nodes_count"] for feature in data["features"]
        ]
        return quantile(scaled_nodes_counts, [0.8, 0.9, 0.99, 0.999])


def nodes_counts_quantiles(path="data/enriched_world.json"):
    try:
        return _nodes_counts_quantiles(path)
    except FileNotFoundError:
        count_nodes_per_polygon()
        return _nodes_counts_quantiles(path)
