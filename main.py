from pathlib import Path

from PlanetQuery.QueryPlanetFootprints import QueryPlanetFootprints
from secret import APIKey


def run():

    json_file = Path(__file__).parent / "simpleQuery.json"

    footprint_download = QueryPlanetFootprints(APIKey, json_file)
    print("{0} Footprints found in AOI".format(footprint_download.total_count))
    for footprint in footprint_download:
        print(footprint.id)
        print(footprint.properties.published)


if __name__ == "__main__":
    run()
