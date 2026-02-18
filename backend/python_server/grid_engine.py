def generate_grid(pois, crime_areas):

    grid = []

    min_lat = 28.40
    max_lat = 28.90
    min_lon = 76.90
    max_lon = 77.35

    step = 0.02   # grid resolution (~2km blocks)

    lat = min_lat
    while lat <= max_lat:
        lon = min_lon
        while lon <= max_lon:

            base = 3  # default base safety

            score = base

            grid.append({
                "lat": lat,
                "lon": lon,
                "score": score
            })

            lon += step
        lat += step

    return grid
