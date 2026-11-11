{
    "name": "Remove Powered by Odoo from POS Receipt",
    "version": "18.0.1.0.0",
    "category": "Sales/Point of Sale",
    "summary": "Remove the Powered by Odoo text from POS receipts",
    "author": "Arga Dwiki Suwandi",
    "maintainer": "Arga Dwiki Suwandi",
    "support": "argadwiki632@gmail.com",
    "license": "OPL-1",
    "images": ["static/description/banner.png"],
    "depends": ["point_of_sale"],
    "assets": {
        "point_of_sale._assets_pos": [
            "arga_pos_receipt_remove_odoo_brand/static/src/xml/order_receipt.xml",
        ],
    },
    "installable": True,
}
