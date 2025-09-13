{
    'name': 'Legal Case Management',
    'version': '1.0',
    'summary': 'Minimal Legal Case Management module',
    'category': 'Legal',
    'author': 'Legal Team / OCA style',
    'license': 'AGPL-3',
    'depends': ['base', 'mail', 'account', 'calendar'],
    'data': [
    'security/security.xml',
    'security/ir.model.access.csv',
    'data/sequences.xml',
    'views/legal_case_views.xml',  # load action first
    'views/menus.xml',             # then menus referencing actions
    'views/res_partner_views.xml',
    'views/legal_hearing_views.xml',
    'views/report_case_summary.xml',
    'reports/case_summary_template.xml',
    'data/demo_data.xml',
],

    'demo': ['data/demo_data.xml'],
    'installable': True,
    'application': True,
    'auto_install': False,
}
