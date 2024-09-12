# -*- coding: utf-8 -*-
{
    'name': "test_eventlight",
    'summary': "Short (1 phrase/line) summary of the module's purpose",
    'description': """
        Long description of module's purpose.
    """,
    'author': "My Company",
    'website': "https://www.yourcompany.com",
    'category': 'Uncategorized',
    'version': '0.1',
    'depends': ['base'],
    'data': [
        'security/ir.model.access.csv', # Uncomment if you have this file
        'views/views.xml',
        'views/templates.xml',
    ],
    'demo': [
        'demo/demo.xml',
    ],
    'installable': True,
    'application': True,
}
