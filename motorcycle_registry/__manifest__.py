{
    'name': 'Motorcycle Registry',
    'summary': 'Manage Registration of Motorcycles',
    'description': """Motorcycle Registry
	====================
	This Module is used to keep track of the Motorcycle Registration and Ownership of each motorcycled of the brand.""",
	'author': 'mizh-odoo',
	'website': 'https://www.github.com/mizh-odoo/training-odoo',
    'category': 'Kawiil',
	'depends': ['base'],
    'data': [
        'security/motorcycle_registry_groups.xml',
        'security/ir.model.access.csv',
        
		'views/motorcycle_registry_menuitems.xml',
        'views/motorcycle_registry_view.xml'
	],
    'demo': ['demo/motorcycle_registry_demo.xml'],
    'application': True,
    'license': 'OPL-1'
}