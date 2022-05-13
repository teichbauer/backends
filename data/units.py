# ------------------------------------------------------------------------------
# Copyright 2022 SNG
# Author: Raymond Wei
# 2022-05
# -----------------------------------------------------------------------------

# -----------------------------------------------------------------------------
#   00000: piece-count
#   010nn: weights
#   011nn: length
#   012nn: cubics
#   013nn: area
#   013nn: time
#   014nn: speed
#   015nn: force
#   016nn: pressure
#   017nn: energy
#   020nn: temperature
#   0210n: electric voltag
#   0211n: electric current
#   0212n: electric capacity
#   0213n: electric resistance
#   0214n: electric inductivity
#   0215n: electric magnetic
#   0216n: electric frequency
# --------------------------------
#   10nnn: units-packages
# ------------------------------------------------------------------------------
data = [
    # ---------------------------------
    # count units: simply the number
    # ---------------------------------
    {
        "_id": "META-US-00000",
        "category": "piece-count",
        "properties": {
            "LS_name": {
                "zh": "個數",
                "en": "number"
            },
        },
    },
    # ---------------------------------
    # weight units: gram, kg, ...
    # ---------------------------------
    # -----
    # gram
    # -----
    {
        '_id': 'META-US-01000',
        'category': 'weights',
        'properties': {
            'LS_name': {
                'en': 'gram',
                'zh': '克'
            },
            'LS_symbol': {
                'en': 'g',
                'zh': '克'
            },
        },
    },
    # -----
    # kilo gram
    # -----
    {
        '_id': 'META-US-01001',
        'category': 'weights',
        'properties': {
            'LS_name': {
                'en': 'kilogram',
                'zh': '千克'
            },
            'LS_symbol': {
                'en': 'kg',
                'zh': '公斤'
            },
        }
    },
    # -----------
    # metric ton
    # -----------
    {
        '_id': 'META-US-01002',
        'category': 'weights',
        'properties': {
            'LS_name': {
                'en': 'metric ton',
                'zh': '吨'
            },
            'LS_symbol': {
                'en': 't',
                'zh': '公吨'
            },
        }
    },
    # ----------------
    # metric kilo-ton
    # ----------------
    {
        '_id': 'META-US-01003',
        'category': 'weights',
        'properties': {
            'LS_name': {
                'en': 'metric kilo-ton',
                'zh': '千吨'
            },
            'LS_symbol': {
                'en': 'kt',
                'zh': '千吨'
            },
        }
    },
    # --------------------
    # metric ten-kilo-ton
    # --------------------
    {
        '_id': 'META-US-01004',
        'category': 'weights',
        'properties': {
            'LS_name': {
                'en': 'metric ten kilo-ton',
                'zh': '萬吨'
            },
            'LS_symbol': {
                'en': 'ten-kt',
                'zh': '萬吨'
            },
        }
    },
]
