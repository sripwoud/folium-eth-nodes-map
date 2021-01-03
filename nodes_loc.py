import requests
import ast
import pandas as pd
from sklearn.preprocessing import MinMaxScaler


def get_node_loc(ip):
    r = requests.get(f"http://ipwhois.app/json/{ip}").json()
    return r


def save_nodes_loc(path="data/nodes-loc.csv"):
    data = pd.read_csv("data/export-nodestrackerlist.csv", header=2)[["Host"]]
    data.rename(columns={"Host": "host"}, inplace=True)
    data["loc"] = data["host"].apply(get_node_loc)
    data.to_csv("nodes-loc.csv", index=False)


def get_nodes_loc_df():
    data = pd.read_csv("data/nodes-loc.csv")
    data["loc"] = data["loc"].apply(lambda x: ast.literal_eval(x))
    for col in ["ip", "latitude", "longitude", "org", "completed_requests"]:
        if col in ["latitude", "longitude", "completed_requests"]:
            data[col] = data["loc"].apply(lambda x: float(x[col]))
        else:
            data[col] = data["loc"].apply(lambda x: x[col])

    scaler = MinMaxScaler()
    data["opacity"] = scaler.fit_transform(data[["completed_requests"]])

    return data


def nodes_loc():
    try:
        return get_nodes_loc_df()
    except FileNotFoundError:
        save_nodes_loc()
        return get_nodes_loc_df()
