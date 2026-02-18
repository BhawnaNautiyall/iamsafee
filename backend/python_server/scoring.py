from geopy.distance import geodesic

def calculate_score(lat, lon, base_score, pois, crime_zones):

    score = base_score

    for poi in pois:
        dist = geodesic((lat, lon), (poi["lat"], poi["lon"])).meters

        if dist < 200:
            score += poi["weight"]
        elif dist < 500:
            score += poi["weight"] * 0.5

    # Nearby red crime zone = +20
    for zone in crime_zones:
        dist = geodesic((lat, lon), (zone["lat"], zone["lon"])).meters
        if dist < 1500 and zone["score"] > 7:
            score += 20

    return max(0, round(score, 2))
