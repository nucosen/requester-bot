import re
from typing import Optional
from requests import get
import xml.etree.ElementTree as ET
from dataclasses import dataclass


@dataclass
class NicoVideo:
    id: str
    idPattern: re.Pattern[str] = re.compile(r"[sn]m[0-9]+")
    errorVideoId: Optional[str] = "sm0"

    infoApiPrefix: str = "https://ext.nicovideo.jp/api/getthumbinfo/"
    isExists: Optional[bool] = None
    title: Optional[str] = None
    watchUrl: Optional[str] = None
    thumbnailUrl: Optional[str] = None

    def __post_init__(self):
        matched = self.idPattern.search(self.id)
        self.id = matched.group() if matched else "sm0"

        infoXml = get(self.infoApiPrefix + self.id)
        infoXml.raise_for_status()
        thumbInfoTree = ET.fromstring(infoXml.text)

        self.isExists = bool(thumbInfoTree.get("status") == "ok")
        titleElement = thumbInfoTree.find(".//title")
        self.title = titleElement.text if not titleElement is None else self.title
        watchUrlElement = thumbInfoTree.find(".//watch_url")
        self.watchUrl = watchUrlElement.text if not watchUrlElement is None else self.watchUrl
        thumbnailUrlElement = thumbInfoTree.find(".//thumbnail_url")
        self.thumbnailUrl = thumbnailUrlElement.text if not thumbnailUrlElement is None else self.thumbnailUrl

    def __str__(self) -> str:
        return self.id
