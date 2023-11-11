import re
from typing import Optional
from requests import get
import xml.etree.ElementTree as ET

videoIdPattern = re.compile(r"[sn]m[0-9]+")
thumbInfoApiPrefix = "https://ext.nicovideo.jp/api/getthumbinfo/"


class NicoVideo(object):
    __id: Optional[str] = None
    __isExists: Optional[bool] = None
    __thumbInfoCache: Optional[ET.Element] = None

    def __init__(self, videoId: str):
        matched = videoIdPattern.match(videoId)
        if matched:
            self.__id = matched.group()

    def __str__(self):
        if self.__id is None:
            raise NotImplemented()
        return self.__id

    def __loadThumbInfoCache(self):
        if not (self.__thumbInfoCache is None):
            return
        xmlThumbInfo = get(thumbInfoApiPrefix + str(self))
        xmlThumbInfo.raise_for_status()
        self.__thumbInfoCache = ET.fromstring(xmlThumbInfo.text)

    @property
    def isExists(self):
        if self.__isExists is None:
            self.__loadThumbInfoCache()
            self.__isExists = (self.__loadThumbInfoCache.get("status") == "ok")
        return self.__isExists
