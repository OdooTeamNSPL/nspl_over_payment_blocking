{
    'name': 'Vendor Bill Overpayment Prevention',

    'version': '17.0',
    'summary': """
        Prevents overpayment on Vendor Bills by validating payments against bill totals.
    """,

    'description': """
    ✔ Prevents overpayments on Vendor Bills  
    ✔ Automatically validates payment amounts against vendor bill totals  
    ✔ Alerts users when payment exceeds the bill amount  
    ✔ Ensures financial accuracy and control  
    ✔ Helps reduce payment errors and duplicate payments  

    This module provides an additional layer of protection by preventing or warning users when they attempt to overpay a Vendor Bill. It enhances financial integrity and streamlines the accounts payable process.
    """,

    'category': 'Purchase',
    'sequence': 2,
    'author': 'Namah Softech Private Limited',
    'website': 'https://www.namahsoftech.com/',
    'license': 'OPL-1',
    'price': 9.99,
    'currency': 'USD',
    'support': 'support@namahsoftech.com',
    'contributors': ["Rutik Patil"],
    'depends': ['mail', 'account', 'account_accountant'],
    'data': [

    ],
    'images': ['static/description/img/banner.png'],
    'installable': True,
    'auto_install': False,
    'application': False,
}
