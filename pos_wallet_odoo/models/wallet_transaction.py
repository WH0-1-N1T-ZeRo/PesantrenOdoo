# -*- coding: utf-8 -*-
#############################################################################
#
#    Cybrosys Technologies Pvt. Ltd.
#
#    Copyright (C) 2024-TODAY Cybrosys Technologies(<https://www.cybrosys.com>)
#    Author: Sruthi Pavithran (odoo@cybrosys.com)
#
#    You can modify it under the terms of the GNU LESSER
#    GENERAL PUBLIC LICENSE (LGPL v3), Version 3.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU LESSER GENERAL PUBLIC LICENSE (LGPL v3) for more details.
#
#    You should have received a copy of the GNU LESSER GENERAL PUBLIC LICENSE
#    (LGPL v3) along with this program.
#    If not, see <http://www.gnu.org/licenses/>.
#
#############################################################################
from odoo import api, fields, models


class WalletTransaction(models.Model):
    """Adding wallet transaction fields"""
    _name = 'pos.wallet.transaction'
    _description = "Create Wallet Transaction Details"

    name = fields.Char(string="Name", help="Sequence of wallet transaction")
    type = fields.Char(string="Type", help="Type of wallet transaction")
    customer = fields.Char(string="Customer",
                           help="Customer of wallet transaction")
    wallet_type = fields.Selection([
    ('dompet', 'Dompet'),
    ('kas', 'Kas')],
    string='Wallet Type', default='dompet')

    pos_order_id = fields.Many2one('pos.order',string="POS Order",
                            help="Order reference of wallet transaction")
    amount = fields.Float(string="Amount",
                          help="Amount of wallet transaction")
    currency = fields.Char(string="Currency",
                           help="Currency of wallet transaction")
    reference = fields.Char(string='Reference')
    currency_id = fields.Char(string='Pembayaran')

    @api.model
    def create(self, vals):
        """Create sequence for wallet transaction"""
        vals['name'] = self.env['ir.sequence'].next_by_code(
            'pos.wallet.transaction')
        return super(WalletTransaction, self).create(vals)

    partner_id = fields.Many2one('res.partner', string='Customer')
    siswa_id = fields.Many2one('res.partner', string='Siswa', compute='_compute_siswa')

    @api.depends('partner_id')
    def _compute_siswa(self):
        # Implementasi logika compute di sini
        return


    