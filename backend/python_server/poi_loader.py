import requests

OVERPASS_URL = "https://overpass-api.de/api/interpreter"

def fetch_pois():
    query = """
    [out:json][timeout:25];
    area["name"="Delhi"]->.searchArea;
    (
      node["railway"="station"](area.searchArea);
      node["highway"="bus_stop"](area.searchArea);
      node["amenity"="police"](area.searchArea);
      node["shop"="alcohol"](area.searchArea);
      node["amenity"="bar"](area.searchArea);
      node["amenity"="pub"](area.searchArea);
    );
    out center;
    """

    response = requests.post(OVERPASS_URL, data=query)
    data = response.json()

    pois = []

    for el in data["elements"]:
        tags = el.get("tags", {})
        weight = 0

        if tags.get("railway") == "station":
            weight = -20
        elif tags.get("highway") == "bus_stop":
            weight = -10
        elif tags.get("amenity") == "police":
            weight = -25
        elif tags.get("shop") == "alcohol":
            weight = 20
        elif tags.get("amenity") in ["bar", "pub"]:
            weight = 20

        pois.append({
            "lat": el["lat"],
            "lon": el["lon"],
            "weight": weight
        })

    return pois
