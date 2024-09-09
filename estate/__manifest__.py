{
    "name": "Estate",  # The name that will appear in the App list
    "version": "17.0.0",  # Version
    "application": True,  # This line says the module is an App, and not a module
    "depends": ["base"],  # dependencies
    "data": [
        'views/mi_modelo_view.xml'
    ],
    "installable": True,
    'license': 'LGPL-3',
}
