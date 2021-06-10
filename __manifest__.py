{
    'name': 'Stesi Dynamic Snippet Filter',
    'Description': 'This module allow to create dynamic website snippets',
    'author': 'STeSI Srl',
    'license': 'OPL-1',
    'depends': ['website'],
    'data': [
                'security/ir.model.access.csv',
                'data/snippet_data.xml',
                'views/dynamic_snippet_filter_view.xml',
                'views/snippets_templates.xml',
                'views/templates.xml',
            ]
}