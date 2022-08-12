from enum import Enum
from typing import List, Any, TypeVar, Callable, Type, cast, Optional, Union
from datetime import datetime
import dateutil.parser
T = TypeVar("T")


def from_list(f: Callable[[Any], T], x: Any) -> List[T]:
    assert isinstance(x, list)
    return [f(y) for y in x]


def from_float(x: Any) -> float:
    if not x:
        return 0
    assert isinstance(x, (float, int)) and not isinstance(x, bool)
    return float(x)


def to_float(x: Any) -> float:
    if not x:
        return 0
    assert isinstance(x, float)
    return x


def from_str(x: Any) -> str:
    if not x:
        return ""
    assert isinstance(x, str)
    return x


def from_datetime(x: Any) -> Optional[datetime]:
    if not x:
        return None
    return dateutil.parser.parse(x)


def from_int(x: Any) -> Union[Optional[int], Any]:
    if not x:
        return None
    assert isinstance(x, int) and not isinstance(x, bool)
    return x


def from_bool(x: Any) -> Optional[bool]:
    if not x:
        return None
    assert isinstance(x, bool)
    return x


def to_class(c: Type[T], x: Any) -> dict:
    assert isinstance(x, c)
    return cast(Any, x).to_dict()


class Geometry:
    coordinates: List[List[List[float]]]
    geom_type: str

    def __init__(self, coordinates: List[List[List[float]]], geom_type: str) -> None:
        self.coordinates = coordinates
        self.geom_type = geom_type

    @staticmethod
    def from_dict(obj: Any) -> 'Geometry':
        assert isinstance(obj, dict)
        coordinates = from_list(lambda x: from_list(lambda x1: from_list(from_float, x1), x), obj.get("coordinates"))
        geo_type = str(obj.get("type"))
        return Geometry(coordinates, geo_type)

    def to_dict(self) -> dict:
        result: dict = dict()
        result["coordinates"] = from_list(lambda x: from_list(lambda x1: from_list(to_float, x1), x), self.coordinates)
        result["type"] = self.geom_type
        return result


class FeatureLinks:
    links_self: str
    assets: str
    thumbnail: str

    def __init__(self, links_self: str, assets: str, thumbnail: str) -> None:
        self.links_self = links_self
        self.assets = assets
        self.thumbnail = thumbnail

    @staticmethod
    def from_dict(obj: Any) -> 'FeatureLinks':
        assert isinstance(obj, dict)
        links_self = from_str(obj.get("_self"))
        assets = from_str(obj.get("assets"))
        thumbnail = from_str(obj.get("thumbnail"))
        return FeatureLinks(links_self, assets, thumbnail)

    def to_dict(self) -> dict:
        result: dict = dict()
        result["_self"] = from_str(self.links_self)
        result["assets"] = from_str(self.assets)
        result["thumbnail"] = from_str(self.thumbnail)
        return result


class Permission(Enum):
    ASSETS_BASIC_ANALYTIC_4_B_DOWNLOAD = "assets.basic_analytic_4b:download"
    ASSETS_BASIC_ANALYTIC_4_B_RPC_DOWNLOAD = "assets.basic_analytic_4b_rpc:download"
    ASSETS_BASIC_ANALYTIC_4_B_XML_DOWNLOAD = "assets.basic_analytic_4b_xml:download"
    ASSETS_BASIC_ANALYTIC_8_B_DOWNLOAD = "assets.basic_analytic_8b:download"
    ASSETS_BASIC_ANALYTIC_8_B_XML_DOWNLOAD = "assets.basic_analytic_8b_xml:download"
    ASSETS_BASIC_UDM2_DOWNLOAD = "assets.basic_udm2:download"
    ASSETS_ORTHO_ANALYTIC_3_B_DOWNLOAD = "assets.ortho_analytic_3b:download"
    ASSETS_ORTHO_ANALYTIC_3_B_XML_DOWNLOAD = "assets.ortho_analytic_3b_xml:download"
    ASSETS_ORTHO_ANALYTIC_4_B_DOWNLOAD = "assets.ortho_analytic_4b:download"
    ASSETS_ORTHO_ANALYTIC_4_B_SR_DOWNLOAD = "assets.ortho_analytic_4b_sr:download"
    ASSETS_ORTHO_ANALYTIC_4_B_XML_DOWNLOAD = "assets.ortho_analytic_4b_xml:download"
    ASSETS_ORTHO_ANALYTIC_8_B_DOWNLOAD = "assets.ortho_analytic_8b:download"
    ASSETS_ORTHO_ANALYTIC_8_B_SR_DOWNLOAD = "assets.ortho_analytic_8b_sr:download"
    ASSETS_ORTHO_ANALYTIC_8_B_XML_DOWNLOAD = "assets.ortho_analytic_8b_xml:download"
    ASSETS_ORTHO_UDM2_DOWNLOAD = "assets.ortho_udm2:download"
    ASSETS_ORTHO_VISUAL_DOWNLOAD = "assets.ortho_visual:download"


class Properties:
    acquired: datetime
    anomalous_pixels: float
    clear_confidence_percent: int
    clear_percent: int
    cloud_cover: float
    cloud_percent: int
    ground_control: bool
    gsd: float
    heavy_haze_percent: int
    instrument: str
    item_type: str
    light_haze_percent: int
    pixel_resolution: float
    provider: str
    published: datetime
    publishing_stage: str
    quality_category: str
    satellite_azimuth: float
    satellite_id: str
    shadow_percent: int
    snow_ice_percent: int
    strip_id: str
    sun_azimuth: float
    sun_elevation: float
    updated: datetime
    view_angle: float
    visible_confidence_percent: int
    visible_percent: int

    def __init__(self, acquired: datetime, anomalous_pixels: float, clear_confidence_percent: int, clear_percent: int,
                 cloud_cover: float, cloud_percent: int, ground_control: bool, gsd: float, heavy_haze_percent: int,
                 instrument: str, item_type: str, light_haze_percent: int, pixel_resolution: float,
                 provider: str, published: datetime, publishing_stage: str,
                 quality_category: str, satellite_azimuth: float, satellite_id: str, shadow_percent: int,
                 snow_ice_percent: int, strip_id: str, sun_azimuth: float, sun_elevation: float, updated: datetime,
                 view_angle: float, visible_confidence_percent: int, visible_percent: int) -> None:
        self.acquired = acquired
        self.anomalous_pixels = anomalous_pixels
        self.clear_confidence_percent = clear_confidence_percent
        self.clear_percent = clear_percent
        self.cloud_cover = cloud_cover
        self.cloud_percent = cloud_percent
        self.ground_control = ground_control
        self.gsd = gsd
        self.heavy_haze_percent = heavy_haze_percent
        self.instrument = instrument
        self.item_type = item_type
        self.light_haze_percent = light_haze_percent
        self.pixel_resolution = pixel_resolution
        self.provider = provider
        self.published = published
        self.publishing_stage = publishing_stage
        self.quality_category = quality_category
        self.satellite_azimuth = satellite_azimuth
        self.satellite_id = satellite_id
        self.shadow_percent = shadow_percent
        self.snow_ice_percent = snow_ice_percent
        self.strip_id = strip_id
        self.sun_azimuth = sun_azimuth
        self.sun_elevation = sun_elevation
        self.updated = updated
        self.view_angle = view_angle
        self.visible_confidence_percent = visible_confidence_percent
        self.visible_percent = visible_percent

    @staticmethod
    def from_dict(obj: Any) -> 'Properties':
        assert isinstance(obj, dict)
        acquired = from_datetime(obj.get("acquired"))
        anomalous_pixels = from_float(obj.get("anomalous_pixels"))
        clear_confidence_percent = from_int(obj.get("clear_confidence_percent"))
        clear_percent = from_int(obj.get("clear_percent"))
        cloud_cover = from_float(obj.get("cloud_cover"))
        cloud_percent = from_int(obj.get("cloud_percent"))
        ground_control = from_bool(obj.get("ground_control"))
        gsd = from_float(obj.get("gsd"))
        heavy_haze_percent = from_int(obj.get("heavy_haze_percent"))
        instrument = obj.get("instrument")
        item_type = obj.get("item_type")
        light_haze_percent = from_int(obj.get("light_haze_percent"))
        pixel_resolution = from_float(obj.get("pixel_resolution"))
        provider = obj.get("provider")
        published = from_datetime(obj.get("published"))
        publishing_stage = obj.get("publishing_stage")
        quality_category = str(obj.get("quality_category"))
        satellite_azimuth = from_float(obj.get("satellite_azimuth"))
        satellite_id = from_str(obj.get("satellite_id"))
        shadow_percent = from_int(obj.get("shadow_percent"))
        snow_ice_percent = from_int(obj.get("snow_ice_percent"))
        strip_id = from_str(obj.get("strip_id"))
        sun_azimuth = from_float(obj.get("sun_azimuth"))
        sun_elevation = from_float(obj.get("sun_elevation"))
        updated = from_datetime(obj.get("updated"))
        view_angle = from_float(obj.get("view_angle"))
        visible_confidence_percent = from_int(obj.get("visible_confidence_percent"))
        visible_percent = from_int(obj.get("visible_percent"))
        return Properties(acquired, anomalous_pixels, clear_confidence_percent, clear_percent, cloud_cover,
                          cloud_percent, ground_control, gsd, heavy_haze_percent, instrument, item_type,
                          light_haze_percent, pixel_resolution, provider, published, publishing_stage, quality_category,
                          satellite_azimuth, satellite_id, shadow_percent, snow_ice_percent, strip_id, sun_azimuth,
                          sun_elevation, updated, view_angle, visible_confidence_percent, visible_percent)

    def to_dict(self) -> dict:
        result: dict = {}
        result["acquired"] = self.acquired.isoformat()
        result["anomalous_pixels"] = to_float(self.anomalous_pixels)
        result["clear_confidence_percent"] = from_int(self.clear_confidence_percent)
        result["clear_percent"] = from_int(self.clear_percent)
        result["cloud_cover"] = to_float(self.cloud_cover)
        result["cloud_percent"] = from_int(self.cloud_percent)
        result["ground_control"] = from_bool(self.ground_control)
        result["gsd"] = to_float(self.gsd)
        result["heavy_haze_percent"] = from_int(self.heavy_haze_percent)
        result["instrument"] = self.instrument
        result["item_type"] = self.item_type
        result["light_haze_percent"] = from_int(self.light_haze_percent)
        result["pixel_resolution"] = from_float(self.pixel_resolution)
        result["provider"] = self.provider
        result["published"] = self.published.isoformat()
        result["publishing_stage"] = self.publishing_stage
        result["quality_category"] = str(self.quality_category)
        result["satellite_azimuth"] = to_float(self.satellite_azimuth)
        result["satellite_id"] = from_str(self.satellite_id)
        result["shadow_percent"] = from_int(self.shadow_percent)
        result["snow_ice_percent"] = from_int(self.snow_ice_percent)
        result["strip_id"] = from_str(str(self.strip_id))
        result["sun_azimuth"] = to_float(self.sun_azimuth)
        result["sun_elevation"] = to_float(self.sun_elevation)
        result["updated"] = self.updated.isoformat()
        result["view_angle"] = to_float(self.view_angle)
        result["visible_confidence_percent"] = from_int(self.visible_confidence_percent)
        result["visible_percent"] = from_int(self.visible_percent)
        return result


class FootprintFeature:
    links: FeatureLinks
    permissions: List[str]
    assets: List[str]
    geometry: Geometry
    id: str
    properties: Properties
    feature_type: str

    def __init__(self, links: FeatureLinks, permissions: List[str], assets: List[str], geometry: Geometry,
                 sid: str, properties: Properties, in_type: str) -> None:
        self.links = links
        self.permissions = permissions
        self.assets = assets
        self.geometry = geometry
        self.id = sid
        self.properties = properties
        self.feature_type = in_type

    @staticmethod
    def from_dict(obj: Any) -> 'FootprintFeature':
        try:
            assert isinstance(obj, dict)
            links = FeatureLinks.from_dict(obj.get("_links"))
            permissions = obj.get("_permissions")
            assets = obj.get("assets")
            geometry = Geometry.from_dict(obj.get("geometry"))
            sid = from_str(obj.get("id"))
            properties = Properties.from_dict(obj.get("properties"))
            f_type = obj.get("type")
            return FootprintFeature(links, permissions, assets, geometry, sid, properties, f_type)
        except Exception as ex:
            print("error deserializing feature with ID {0}. Exception::  ".format(str(obj.get("id"), str(ex))))
            raise ex

    def to_dict(self) -> dict:
        result: dict = {}
        result["_links"] = to_class(FeatureLinks, self.links)
        result["_permissions"] = self.permissions
        result["assets"] = self.assets
        result["geometry"] = to_class(Geometry, self.geometry)
        result["id"] = from_str(self.id)
        result["properties"] = to_class(Properties, self.properties)
        result["type"] = self.feature_type
        return result


class SearchResultLinks:
    first: str
    next: str
    links_self: str

    def __init__(self, first: str, s_next: str, links_self: str) -> None:
        self.first = first
        self.next = s_next
        self.links_self = links_self

    @staticmethod
    def from_dict(obj: Any) -> 'SearchResultLinks':
        assert isinstance(obj, dict)
        first = from_str(obj.get("_first"))
        s_next = from_str(obj.get("_next"))
        links_self = from_str(obj.get("_self"))
        return SearchResultLinks(first, s_next, links_self)

    def to_dict(self) -> dict:
        result: dict = {}
        result["_first"] = from_str(self.first)
        result["_next"] = from_str(self.next)
        result["_self"] = from_str(self.links_self)
        return result


class SearchResult:
    links: SearchResultLinks
    features: List[FootprintFeature]
    type: str

    def __init__(self, links: SearchResultLinks, features: List[FootprintFeature], s_type: str) -> None:
        self.links = links
        self.features = features
        self.type = s_type

    @staticmethod
    def from_dict(obj: Any) -> 'SearchResult':
        try:
            assert isinstance(obj, dict)
            links = SearchResultLinks.from_dict(obj.get("_links"))
            features = from_list(FootprintFeature.from_dict, obj.get("features"))
            search_type = from_str(obj.get("type"))
            return SearchResult(links, features, search_type)
        except Exception as ex:
            print(ex)
            raise TypeError(str(ex))

    def to_dict(self) -> dict:
        result: dict = dict()
        result["_links"] = to_class(SearchResultLinks, self.links)
        result["features"] = from_list(lambda x: to_class(FootprintFeature, x), self.features)
        result["type"] = from_str(self.type)
        return result

