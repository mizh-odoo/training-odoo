
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
    'depends': ['base'],
    'data': [
        'security/academy_groups.xml',
        'security/ir.model.access.csv',
        'security/academy_security.xml',
	],
    'demo': ['demo/course_demo.xml'],
    'application': True,
}