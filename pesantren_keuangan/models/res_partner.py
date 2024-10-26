from odoo import api, fields, models
import random

class ResPartner(models.Model):
    _inherit        = 'res.partner'

    virtual_account = fields.Char(string='Virtual Account', store=True)
    va_saku         = fields.Char(string='No. VA Uang Saku', store=True)
    saldo_uang_saku = fields.Float(string='Saldo Uang Saku', compute='_compute_saldo_uang_saku', store=True)
    wallet_pin      = fields.Char(string='PIN Dompet', store=True)
    has_wallet_pin  = fields.Boolean(string='Apakah ada Wallet PIN', compute='_compute_has_wallet_pin', store=True, readonly=True)
    nis             = fields.Char(string="No Induk Siswa", related='siswa_id.nis', readonly=True)
    barcode_santri  = fields.Char(string="Barcode Santri", related='siswa_id.barcode_santri', store=True)
    siswa_id        = fields.One2many('cdn.siswa', 'partner_id', string='Siswa')
    name            = fields.Char(string='Siswa')


    def _generate_virtual_account(self):
        """Helper method untuk generate Virtual Account"""
        return f"{random.randint(10000000, 99999999)}"

    def _generate_va_saku(self):
        """Helper method untuk generate No. VA Uang Saku"""
        return f"{random.randint(10000000, 99999999)}"

    def create_data_account(self):
        """Method untuk auto generate Virtual Account dan No. VA Uang Saku"""
        for partner in self:
            # Generate virtual account jika belum diisi
            if not partner.virtual_account:
                partner.virtual_account = "001"+partner._generate_virtual_account()

            # Generate VA untuk uang saku jika belum diisi
            if not partner.va_saku:
                partner.va_saku = "002"+partner._generate_va_saku()

        return True  
    @api.depends('siswa_id')
    def _compute_saldo_uang_saku(self):
        for partner in self:
            partner.saldo_uang_saku = partner.calculate_saku()

    def calculate_wallet(self):
        WalletTransaction = self.env['pos.wallet.transaction'].search([('partner_id', '=', self.id)])
        total_amount = 0
        for transaction in WalletTransaction:
            if transaction.wallet_type == 'debit':
                total_amount = total_amount - float(transaction.amount)
            else:
                total_amount = total_amount + float(transaction.amount)
        return total_amount
    def calculate_saku(self,timestamp=None):
        UangSaku = self.env['cdn.uang_saku'].search([('siswa_id', '=', self.id)])
        if timestamp:
            UangSaku = UangSaku.filtered(lambda x: x.validasi_time < timestamp)
        total_amount = 0
        for uang_saku in UangSaku:
            if uang_saku.state == 'confirm':
                if uang_saku.jns_transaksi == 'masuk':
                    total_amount = total_amount + uang_saku.amount_in
                else:
                    total_amount = total_amount - uang_saku.amount_out
        return total_amount

    @api.depends('wallet_pin')
    def _compute_has_wallet_pin(self):
        for rec in self:
            rec.has_wallet_pin = rec.wallet_pin != False
    @api.model
    def check_wallet_pin(self,args):
        Partner = self.env['res.partner'].browse(args['partner_id'])
        return {'has_wallet_pin':Partner.has_wallet_pin,'match':Partner.wallet_pin == args['wallet_pin']}
    