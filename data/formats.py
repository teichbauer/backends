data = [
    {
        '_id': 'META-CS-ENTITIES',
        'category': 'ES-specification',
        'properties': {
            'descr': '''All physical entities tha can be measured. 
                All entities should be worth tracing as an unit.
                Entities will be grouped into limited number of categories,
                whic are listed in META-CS-ES-CATEGORIES.
            ''',
            'examples': [
                'mechanical part, singlar or grioup of them',
                'equipment, singlar or group of them',
                'physical, measurable material',
            ]
        }

    },
    {
        '_id': 'META-CS-ENTITY-CATEGORIES',
        'category': 'ES-specification',
        'properties': {
            # all possible categories under collection named ES
            'categories': [
                {
                    'name': 'work-piece',
                    'descr': 'a physical piece being processed'
                },
                {
                    'name': 'mechanical-part',
                    'descr': 'a specific part of a work-piece, or an equipment'
                },
                {
                    'name': 'electric-part',
                    'descr': 'a specific part of a work-piece or an equipment'
                },
                {
                    'name': 'equipment',
                    'descr': 'equipment that can be commerially, or ' +
                             'funcationally identified.'
                },
            ]

        }

    },
    {
        '_id': 'META-CS-CONCEPTS',
        'category': 'CS-specification',
        'properties': {
            'descr': '''any artificial set-ups, structural groupings, 
                configurations, geo-locations, design modelings,
                information-packages
                ''',
            'examples': [
                'configuration, or group of them',
                'work-post, or group of them',
                'account, or group of them',
                'design model info-package'
            ]
        }

    },
    {
        '_id': 'META-CS-CONCEPTS-CATEGORIES',
        'category': 'CS-specification',
        'properties': {
            'categories': [
                {
                    'name': 'info-package',
                    'descr': 'design model info, ...'
                },
                {
                    'name': 'configuration',
                    'descr': 'settings for configuration'
                },
                {
                    'name': 'account',
                    'descr': 'account for bank, login, ...'
                },
                {
                    'name': 'geo-location',
                    'descr': 'with attitude and longitude, or address, or' +
                    'customizable location description'
                },
            ]
        }
    },
    {
        '_id': 'META-CS-DOCUMENTS',
        'category': 'DS-specification',
        'properties': {
            'descr': '''all documentation, be it paper form, or electronic form
                (file), images, picture, drawings, videos.. or groups of them''',
            'examples': [
                'drawings(file or paper form), or groups of them',
                'pictures(file or prints), or groups of them',
                'video, or groups of them',
                'paper-documents, or groups of them',
                'document-folder',
            ]
        }
    },
    {
        '_id': 'META-CS-DOCUMENT-CATEGORIES',
        'category': 'DS-specification',
        'properties': {
            'categories': [

            ]
        }
    },
    {
        '_id': 'META-CS-UNITS',
        'category': 'US-specification',
        'properties': {
            'descr': '',
            'examples': [
                'kilogram',
                'tons',
                'meter',
                'temperatur: 34 degree'
            ]
        }
    },
    {
        '_id': 'META-CS-UNITS-CATEGORIES',
        'category': 'US-specification',
        'properties': {
            'categories': [
                {
                    'name': 'piece-coumt',
                    'descr': 'number count'
                },
                {
                    'name': 'weights',
                    'descr': 'all possible units for measuring weight'
                },
                {
                    'name': 'length',
                    'descr': 'all possible units for measuring length'
                },
                {
                    'name': 'area',
                    'descr': 'all possible units for measuring area'
                },
                {
                    'name': 'cubics',
                    'descr': 'all possible units for measuring cubics'
                },
                {
                    'name': 'time',
                    'descr': 'all possible units for measuring time/duration'
                },
                {
                    'name': 'speed',
                    'descr': 'all possible units for measuring speed'
                },
                {
                    'name': 'force',
                    'descr': 'all possible units for measuring force'
                },
                {
                    'name': 'pressure',
                    'descr': 'all possible units for measuring pressure'
                },
                {
                    'name': 'energy',
                    'descr': 'all possible units for measuring energy/power'
                },
                {
                    'name': 'temperature',
                    'descr': 'all possible units for measuring temperature'
                },
                {
                    'name': 'electric-voltage',
                    'descr': 'all possible units for measuring electric-voltage'
                },
                {
                    'name': 'electric-current',
                    'descr': 'all possible units for measuring electric-current'
                },
                {
                    'name': 'electric-capacity',
                    'descr': 'all possible units for measuring electric-capacity'
                },
                {
                    'name': 'electric-resistance',
                    'descr': 'all possible units for measuring electric-resistance'
                },
                {
                    'name': 'electric-inductivity',
                    'descr': 'all possible units for measuring electric-inductivity'
                },
                {
                    'name': 'magnetic-strength',
                    'descr': 'all possible units for measuring magnetic-strength'
                },
                {
                    'name': 'frequency',
                    'descr': 'all possible units for measuring frequency'
                },
                {
                    'name': 'unit-package',
                    'descr': 'group of units in use'
                },
            ]
        }
    },
    {
        '_id': 'META-CS-PERSON',
        'category': 'PS-specification',
        'properties': {
            'descr': '''all human involved parties: individual, couple,
                group, organization, company, institution ''',
            'examples': [
                'person',
                'couple',
                'group',
                'department',
                'division',
                'sub-division',
                'institution',
                'committee'
            ]
        }

    },
    {
        '_id': 'META-CS-PERSON-CATEGORIES',
        'category': 'PS-specification',
        'properties': {
            'categories': [

            ]
        }

    },
    {
        '_id': 'META-CS-TIMESERIE',
        'category': 'TS-specification',
        'properties': {

        }

    },
    {
        '_id': 'META-CS-TIMESERIE-CATEGORIES',
        'category': 'TS-specification',
        'properties': {

        }

    },
]
