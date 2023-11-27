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

    def __str__(self) -> str:
        if self.__id is None:
            raise NotImplemented()
        return self.__id

    def __getThumbInfo(self) -> ET.Element:
        if self.__thumbInfoCache is None:
            xmlThumbInfo = get(thumbInfoApiPrefix + str(self))
            xmlThumbInfo.raise_for_status()
            self.__thumbInfoCache = ET.fromstring(xmlThumbInfo.text)
        return self.__thumbInfoCache

    @property
    def isExists(self) -> bool:
        if self.__isExists is None:
            self.__isExists = (self.__getThumbInfo().get("status") == "ok")
        return self.__isExists

    @classmethod
    def fromUri(cls, uri: str):
        pattern = re.compile("[sn]m[0-9]+")
        matched = pattern.search(uri)
        return cls(matched.group() if matched else "sm0")
