# -*- coding: utf-8 -*-
from odoo import http


class PesantrenPsb(http.Controller):
    @http.route('/pesantren_psb', auth='public')
    def index(self, **kw):
        return request.render('pesantren_psb.psb_data_pendaftaran_template', values)

    @http.route('/pesantren_psb/submit', type='json', auth='public', methods=['POST'])
    def submit_pendaftaran(self, **kwargs):
        # Ambil data dari request
        data = {
            'name': kwargs.get('name'),
            'tanggal': kwargs.get('tanggal'),
            'jenjang': kwargs.get('jenjang'),
            'nomor': kwargs.get('nomor'),
            'nik': kwargs.get('nik'),
            'kk': kwargs.get('kk'),
            'tgl_lahir': kwargs.get('tgl_lahir'),
            'gender': kwargs.get('gender'),
            'status': kwargs.get('status'),
            'keterangan': kwargs.get('keterangan'),
        }
        # Simpan data ke model
        request.env['web.data.daftaran'].sudo().create(data)
        return {'status': 'success'}


