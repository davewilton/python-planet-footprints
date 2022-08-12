# python-planet-footprints
Simple python class to return planet footprints

Provide an API key and a json file containing search criteria and an iterable class of footprints will be returned

Example

```
json_file = Path(__file__).parent / "simpleQuery.json"

footprint_download = QueryPlanetFootprints(APIKey, json_file)
print("{0} Footprints found in AOI".format(footprint_download.total_count))
for footprint in footprint_download:
    print(footprint.id)
    print(footprint.properties.published)

```
