from folium import Map, CircleMarker, Popup, FeatureGroup, GeoJson
from nodes_loc import nodes_loc
from process_world import nodes_counts_quantiles


def create_map(data, file_name="index.html"):
    map = Map(
        location=[data[col].mean() for col in ["latitude", "longitude"]],
        tiles="Stamen Toner",
        zoom_start=2,
    )

    fg = FeatureGroup(name="My Map")
    circles = [
        {
            "radius": 5,
            "stroke": False,
            "fill": True,
            "fill_color": "crimson",
            "fill_opacity": opacity,
            "location": [latitude, longitude],
            "popup": Popup(
                html=f"""
                <style>
                    tbody {{
                        text-align: center;
                    }}
                    table,
                    tr,
                    td {{
                        border-collapse: collapse;
                        border: 1px solid black;
                    }}
                </style>
                <h3>{ip}</h3>
                <table>
                    <tbody>
                        <tr>
                        <td><strong>ISP</strong></td>
                        <td>{org}</td>
                        </tr>
                        <tr>
                        <td><strong>Completed requests</strong></td>
                        <td>{completed_requests}</td>
                        </tr>
                    </tbody>
                </table>
            """,
                max_width=300,
            ),
        }
        for ip, latitude, longitude, org, completed_requests, opacity in [
            named_tuple[2:] for named_tuple in data.itertuples(index=False)
        ]
    ]

    q1, q2, q3, q4 = nodes_counts_quantiles()
    print(q1, q2, q3, q4)

    def opacity(scaled_nodes_count):
        # print(scaled_nodes_count)
        if scaled_nodes_count < q1:
            return 0
        elif q1 <= scaled_nodes_count < q2:
            return 0.1
        elif q2 <= scaled_nodes_count < q3:
            return 0.25
        elif q3 <= scaled_nodes_count < q4:
            return 0.5
        else:
            return 0.75

    def style_function(feature):
        fillOpacity = opacity(feature["properties"]["scaled_nodes_count"])
        return {"fillColor": "blue", "weight": 0, "fillOpacity": fillOpacity}

    fg.add_child(
        GeoJson(
            data=open("data/enriched_world.json", encoding="utf-8-sig").read(),
            style_function=style_function,
        )
    )

    for circle in circles:
        fg.add_child(CircleMarker(**circle))

    map.add_child(fg)
    map.save(file_name)


create_map(nodes_loc())

# count_nodes_per_polygon(nodes_loc()[["latitude", "longitude"]])
