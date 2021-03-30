import json

import requests
from fer import FER
from fer import Video


def vid_proc(path):
    video_filename = path
    video = Video(video_filename)

    detector = FER(mtcnn=True)

    raw_data = video.analyze(detector, frequency=5, save_frames=False, save_video=False)

    for x in raw_data:
        x.pop('box0')
        key_max = max(x, key=x.get)
        x['result'] = key_max

    return json.dumps(raw_data)


def vid_convert(link):
    r = requests.get(link, allow_redirects=True, stream=True)
    with open('new.mp4', 'wb') as f:
        for chunk in r.iter_content(chunk_size=1024 * 1024):
            if chunk:
                f.write(chunk)
    if chunk:
        return 'new.mp4'
    else:
        return ''
