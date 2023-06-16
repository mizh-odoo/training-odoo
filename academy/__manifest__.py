
{
    'name': 'Odoo Academy',
    'summary': """Module to handle Course and Sessions""",
    'description': """Module to handle:
    	- Courses
        - Sessions
        - Attendees
        """,
    'license': 'OPL-1',
    'author': 'mizh-odoo',
    'website': 'https://www.github.com/mizh-odoo/training-odoo',
    'category': 'Kawiil',
    'depends': ['base', 'sale'],
    'data': [
        'security/academy_groups.xml',
        'security/ir.model.access.csv',
        'security/academy_security.xml',
        
		'data/session_data.xml',
        
		'views/academy_menuitems.xml',
        'views/course_view.xml',
	],
    'demo': ['demo/course_demo.xml'],
    'application': True,
}