# -*- coding: utf-8 -*-
{
    'name': 'POS Receipt Customization',
    'version': '18.0.1.0.0',
    'category': 'Point of Sale',
    'summary': 'Customize POS receipts with enhanced features',
    'description': """
        POS Receipt Customization Module
        ================================
        
        This module provides enhanced customization options for POS receipts including:
        * Custom receipt layouts
        * Reprint functionality
        * Additional receipt formatting options
        
        Features:
        ---------
        * Customizable order receipts
        * Enhanced reprint screen
        * Flexible receipt templates
    """,
    'author': 'Guzato Systems',
    'website': 'https://www.guzatosystems.com',
    'license': 'LGPL-3',
    'depends': [
        'base',
        'point_of_sale',
        'web',
    ],
    'data': [
    ],
    'assets': {
        'point_of_sale.assets': [
            'pos_receipt/js/CustomOrderReceipt.js',
            'pos_receipt/js/ReprintReceiptScreen.js',
            'pos_receipt/xml/OrderReceipt.xml',
        ],
    },
    'installable': True,
    'auto_install': False,
    'application': False,
} 