import sys
try:
    sys.path.append("~/../src")
finally:
    from requester import nicoVideo as nv

normal_video = nv.NicoVideo("sm9")
non_exists_video = nv.NicoVideo("sm0")
deleted_video = nv.NicoVideo("sm1")
normal_video_from_string = nv.NicoVideo.fromUri("abc123sm9abc123")
non_exists_video_from_string = nv.NicoVideo.fromUri("abc123sm0abc123")
invalid_uri_video = nv.NicoVideo.fromUri("abc123abc123abc123")

validVideos = [
    normal_video,
    normal_video_from_string,
]

invalidVideos = [
    non_exists_video,
    non_exists_video_from_string,
    invalid_uri_video,
]

deletedVideos = [
    deleted_video,
]


def test_NicoVideo():
    for video in validVideos:
        assert str(video) == "sm9"
    for video in invalidVideos:
        assert str(video) == "sm0"
    for video in deletedVideos:
        assert str(video) == "sm1"


def test_isExists():
    for video in validVideos:
        assert video.isExists
    for video in invalidVideos + deletedVideos:
        assert not video.isExists
