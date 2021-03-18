from autojson import __version__
from autojson import Int, Float, String, Array, Object, String, Boolean
import json

def test_version():
    assert __version__ == '0.1.1'

def test_autojson():
    class RedisConfig(Object):
        host = String()
        port = Int()
        db = Int()

    class DetectionConfig(Object):
        area = Array(Array(Int(), 2))
        threshold = Float()
        flag = Boolean()

    class Rectangle(Object):
        left = Int()
        top = Int()
        right = Int()
        bottom = Int()

    class Config(Object):
        redis = RedisConfig()
        detection = DetectionConfig()
        rectangles = Array(Rectangle())

    txt = """
    {
        "redis": {
            "host": "127.0.0.1",
            "port": 50007,
            "db": 0
        },
        "detection": {
            "area": [
                [0, 0],
                [1920, 1080],
                [0, 1080]
            ],
            "threshold": 0.35,
            "flag": true
        },
        "rectangles": [
            {
                "left": 0,
                "top": 0,
                "right": 100,
                "bottom": 200
            },
            {
                "left": 100,
                "top": 100,
                "right": 300,
                "bottom": 200
            }
        ]
    }
    """

    obj = json.loads(txt)
    config: Config = Config().parse_json(obj)

    assert config.redis.host == "127.0.0.1"
    assert config.redis.port == 50007
    assert config.redis.db == 0

    assert config.detection.area == [[0, 0], [1920, 1080], [0, 1080]]
    assert config.detection.threshold == 0.35
    assert config.detection.flag.value == True

    assert config.rectangles[0].left == 0
    assert config.rectangles[0].top == 0
    assert config.rectangles[0].right == 100
    assert config.rectangles[0].bottom == 200

    assert config.rectangles[1].left == 100
    assert config.rectangles[1].top == 100
    assert config.rectangles[1].right == 300
    assert config.rectangles[1].bottom == 200

    r = config.rectangles[0]
    r.get_default_json()
    r = config.rectangles[0:1]
    r.get_default_json()
    r[0]

    config = Config()
    obj = config.get_default_json()

    assert obj["redis"]["host"] == ""
    assert obj["redis"]["port"] == 0
    assert obj["redis"]["db"] == 0

    assert obj["detection"]["area"] == [[0, 0]]
    assert obj["detection"]["threshold"] == 0.0

    assert obj.rectangles[0].left == 0
    assert obj.rectangles[0].top == 0
    assert obj.rectangles[0].right == 0
    assert obj.rectangles[0].bottom == 0

    obj.redis.port = Int(100)
    assert obj.redis.port == 100
    assert obj["redis"]["port"] == 100

    obj["redis"]["port"] = Int(200)
    assert obj.redis.port == 200
    assert obj["redis"]["port"] == 200

def test_boolean():
    b1 = Boolean(False)
    b2 = Boolean(False)
    b3 = Boolean(True)
    assert b1 == False
    assert False == b1
    assert b3 == True
    assert True == b3
    assert b1 == b2
    assert b1 != b3
    assert not b1
    assert b3
    assert (not b1) == True
    assert (not b3) == False
