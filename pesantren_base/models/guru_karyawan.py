from odoo import api, fields, models


class hr_employee(models.Model):
    _inherit            = 'hr.employee'

    nip                 = fields.Char('NIP')
    lembaga             = fields.Selection([('SMP','SMP/MTS'),('SMA','SMA/MA')], string='Lembaga', default='SMA')
    pendidikan_guru_ids = fields.One2many(comodel_name="edu.employee",  inverse_name="employee_id",  string="Riwayat Pendidikan",  help="")
    marital             = fields.Selection(string='Status Pernikahan', selection=[('single', 'Belum Kawin'), ('married', 'Menikah'),('divorced', 'Cerai Hidup'),('cerai', 'Cerai Mati'),])
    jns_pegawai         = fields.Selection([
                            ('musyrif', 'Musyrif'),
                            ('ustadz', 'Ustadz'),
                            ('guru', 'Guru'),
                            ("guruquran", "Guru Qur'an"),
                            ('keamanan', 'Keamanan'),
                            ('kesehatan', 'Kesehatan'),
                            ('kasrama', 'Kepala Asrama')
                        ], string='Jenis Pegawai')
    mata_pelajaran_ids  = fields.Many2many(comodel_name="cdn.mata_pelajaran", string="Mata Pelajaran",  help="")
    # jadwal_pelajaran_lines_ids = fields.Many2many(comodel_name="cdn.jadwal_pelajaran_lines", string="Jadwal Pelajaran", help="")
class pendidikan_guru(models.Model):
    _name               = 'edu.employee'
    _description        = 'Riwayat Pendidikan Guru'

    name                = fields.Char(string='Nama Institusi')
    jenjang             = fields.Selection(string='Jenjang', selection=[('sd', 'SD/MI'), ('smp', 'SMP/MTS'),('sma', 'SMA/MA'),('diploma', 'D1/D2/D3'),('sarjana', 'D4/S1'),('pasca', 'S2/S3'),('lainnya', 'Lainnya/Non Formal')])
    fakultas            = fields.Char(string='Fakultas/Jurusan')
    gelar               = fields.Char(string='Gelar')
    karya_ilmiah        = fields.Char(string='Skripsi/Tesis/Disertasi')
    lulus               = fields.Date(string='Lulus')
    employee_id         = fields.Many2one(comodel_name="hr.employee",  string="Guru/Karyawan",  help="")
    