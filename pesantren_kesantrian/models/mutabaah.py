from odoo import api, fields, models


class Mutabaah(models.Model):
    _name = 'cdn.mutabaah'
    _description = 'Tabel Mutabaah'

    name = fields.Char(string='Nama', required=True)
    kategori_id = fields.Many2one(comodel_name='cdn.mutabaah.kategori', string='Kategori', required=True)
    sesi_id = fields.Many2one(comodel_name='cdn.mutabaah.sesi', string='Sesi Mutabaah')
    skor = fields.Integer(string='Skor/Nilai', default="1", required=True)
    active = fields.Boolean(string='Aktif', default=True)
    
class MutabaahKategori(models.Model):
    _name = 'cdn.mutabaah.kategori'
    _description = 'Cdn Mutabaah Kategori'

    name = fields.Char(string='Kategori Mutabaah', required=True)
    active = fields.Boolean(string='Aktif', default=True)


class MutabaahSesi(models.Model):
    _name = 'cdn.mutabaah.sesi'
    _description = 'Cdn Mutabaah Sesi'

    name = fields.Char(string='Sesi Mutabaah', required=True)
    jam_mulai = fields.Float(string='Jam Mulai', required=True)
    jam_selesai = fields.Float(string='Jam Selesai', required=True)
    active = fields.Boolean(string='Aktif', default=True)
    keterangan = fields.Text(string='Keterangan')
    
    
    

    

    


    
    








    

