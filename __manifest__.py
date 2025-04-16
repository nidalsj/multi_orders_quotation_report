{
    'name': 'Multi Orders Quotation Report',
    'version': '18.0.1.0.0',
    'depends': ['sale', 'sale_management'],
    'data': [
        'report/order_report_views.xml',
        'report/order_report_template.xml',
    ],
    'installable': True,
    'auto_install': False,
}