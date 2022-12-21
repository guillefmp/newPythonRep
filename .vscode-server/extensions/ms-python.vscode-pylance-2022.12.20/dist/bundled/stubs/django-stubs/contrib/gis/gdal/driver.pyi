from typing import Any

from django.contrib.gis.gdal.base import GDALBase as GDALBase

class Driver(GDALBase):
    ptr: Any = ...
    def __init__(self, dr_input: Any) -> None: ...
    @classmethod
    def ensure_registered(cls) -> None: ...
    @classmethod
    def driver_count(cls) -> Any: ...
    @property
    def name(self) -> Any: ...
