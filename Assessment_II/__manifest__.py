{
    'name': 'Modul Pemesanan Ruangan',
    'version': '1.0',
    'depends': ['base'],
    'data': [
        'views/ruangan_views.xml',
        'data/ir_sequence_data.xml',
        'security/ir.model.access.csv',
    ],
    'installable': True,
    'application': True,
}