from odoo import models, fields, api


class PSBBank(models.Model):
    _name           = 'web.bank'
    _description    = 'Bank'

    name            = fields.Char(string="Nama Bank", required="True")
    nomor           = fields.Char(string="Nomor Rekening")
    penjelasan      = fields.Text(string="Penjelasan")
    status          = fields.Selection([('aktif','Aktif'),('mati','Tidak Aktif')],string="Status",)
