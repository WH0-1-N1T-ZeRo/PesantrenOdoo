from odoo import models, fields, api


class PSBDataPendaftaran(models.Model):
    _name           = 'web.data.daftaran'
    _description    = 'Bank'

    name            = fields.Char(string="Nama", required="True")
    tanggal         = fields.Date(string="Tanggal")
    jenjang         = fields.Char(string="Jenjang Tujuan")
    nomor           = fields.Char(string="Nomor Rekening")
    nik             = fields.Char(string="Nomor Induk Kependudukan (NIK) Santri")
    kk              = fields.Char(string="KK") 
    tgl_lahir       = fields.Date(string="Tanggal Lahir")
    gender          = fields.Selection([('l','Laki - Laki'),('p','Perempuan')], string="Jenis Kelamin", default='l')

    status          = fields.Selection([('aktif','Aktif'),('mati','Tidak Aktif')],string="Status")
    keterangan      = fields.Text(string="Keterangan")
