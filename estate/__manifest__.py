{
    "name": "Estate",  # The name that will appear in the App list
    "version": "16.0.0",  # Version
    "application": True,  # This line says the module is an App, and not a module
    "depends": ["base"],  # dependencies
    "data": [
        'views/estate_property_views.xml'
    ],
    "installable": True,
    'application': True,
    'license': 'LGPL-3',
}
