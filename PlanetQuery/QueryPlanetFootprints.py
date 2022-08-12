# script to create footprints of PlanetScope imagery
import logging
import json
from typing import Dict
import requests

from requests.auth import HTTPBasicAuth

from PlanetQuery.PlanetSearchClass import FootprintFeature, SearchResult

HTTP_REQ_SEARCH = 'https://api.planet.com/data/v1/quick-search'
HTTP_REQ_STATS = 'https://api.planet.com/data/v1/stats'


class QueryPlanetFootprints:
    """
    Create an iterator returning planet footprints to matched query json
    """

    total_count = 0
    __features = []
    __strNextPageUrl: str = None
    __iter_counter = 0

    def __init__(self, planet_api_key, json_query_path):
        """
        Create an iterator returning planet footprints to matched query
        :param planet_api_key: API key see https://developers.planet.com/quickstart/apis/
        :param json_query_path: Path to json file containing quick search see
         https://developers.planet.com/docs/apis/data/quick-saved-search/
        """
        self.API_key = planet_api_key
        self.logger = logging.getLogger(None)
        self.config = self.create_config(json_query_path)
        self._get_counts()

    def __iter__(self):
        return self

    def __next__(self) -> FootprintFeature:
        return self.next()

    def next(self) -> FootprintFeature:
        if len(self.__features) > self.__iter_counter:
            feature = self.__features[self.__iter_counter]
        else:
            # load more features?
            if self.__strNextPageUrl and self.__iter_counter < self.total_count:
                self._do_search(self.config)
                feature = self.__features[self.__iter_counter]
            else:
                raise StopIteration
        self.__iter_counter += 1
        return feature

    def create_config(self, json_path):
        try:
            # with open(json_path) as json_file:
            #     json.load(json_path)
            #     query = PlanetQueryClass.from_dict(json.load(json_file))
            return json.loads(open(json_path).read())
        except Exception as Ex:
            self.logger.error(Ex)
            raise PlanetException("Error deserializing input json file")

    def _get_counts(self):

        search_request = self.config

        # get the total count
        search_request["interval"] = "year"

        search_result = requests.post(
            HTTP_REQ_STATS,
            auth=HTTPBasicAuth(self.API_key, ''),
            json=search_request)

        json_results = search_result.json()

        if 'buckets' not in json_results:
            self.logger.error("Error getting counts")
            raise PlanetException("Error getting counts")

        for bucket in json_results['buckets']:
            self.total_count += bucket["count"]

        # get the first lot of features

        del search_request["interval"]

        self._do_search(search_request)

    def _do_search(self, search_request: Dict):
        search_result = requests.post(
            HTTP_REQ_SEARCH,
            auth=HTTPBasicAuth(self.API_key, ''),
            json=search_request)

        json_results = search_result.json()

        if 'features' not in json_results:
            self.logger.error("Error searching planet")
            self.logger.error(json.dumps(json_results, indent=2))
            raise PlanetException("Error searching planet")
        elif len(json_results['features']) == 0:
            self.logger.warning("No features returned")
            return

        result = SearchResult.from_dict(json_results)

        self.__features.extend(result.features)
        if result.links:
            self.__strNextPageUrl = result.links.next

        return result


class PlanetException(Exception):
    pass
