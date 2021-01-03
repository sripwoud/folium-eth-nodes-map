from folium import Map, CircleMarker, Popup, FeatureGroup
from nodes_loc import nodes_loc

data = nodes_loc()

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

for circle in circles:
    fg.add_child(CircleMarker(**circle))

map.add_child(fg)
map.save("index.html")
