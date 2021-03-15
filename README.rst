========
Overview
========

By defining a Python class, you can define a JSON format.
There is no need to define your own JSON parser.
You can convert JSON to Python classes with a short code and support the type hints available in vscode's Pylance extension.
Here's an example of it.

.. code-block:: python

    import json
    from autojson import Object, Array, Int, Float, String

    # JSON file
    txt = """
    {
        "name": "config",
        "threshold": 0.5,
        "rectangles": [
            {
                "left": 0,
                "top": 0,
                "width": 100,
                "height": 200
            },
            {
                "left": 100,
                "top": 100,
                "width": 100,
                "height": 200
            }
        ],
        "area": [
            [0, 0],
            [1920, 0],
            [1920, 1080],
            [0, 1080]
        ]
    }
    """

    # define your JSON format
    class Rectangle(Object):
        left = Int()
        top = Int()
        width = Int()
        height = Int()


    class Config(Object):
        name = String()
        threshold = Float()
        rectangles = Array(Rectangle())
        area = Array(Array(Int(), size=2))


    # load JSON to your class
    config = Config().parse_json(json.loads(txt))
    # To change parameter
    config.threshold = 0.7
    # or
    config["threshold"] = 0.3

    # if you don't have json template, create the template
    print(json.dumps(Config().get_default_json()))
    # Object is subclass of dict
    # so you can save it as json

=====
Usage
=====

This module provides five classes: Object, Array, Int, Float, and String.


