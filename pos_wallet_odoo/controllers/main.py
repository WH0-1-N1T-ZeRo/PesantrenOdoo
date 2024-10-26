from odoo import http
from odoo.http import request, Response

class POSPinController(http.Controller):

    @http.route('/pos/check_pin', type='json', auth='user', methods=['POST'])
    def check_pin(self, partner_name, entered_pin):
        try:
            # Cari partner berdasarkan nama yang mirip menggunakan operator 'ilike'
            partner = request.env['res.partner'].sudo().search([('name', 'ilike', partner_name)], limit=1)

            if not partner:
                return {'status': 'error', 'message': 'Customer Not Found'}

            # Cek apakah wallet_pin dari partner cocok
            if partner.wallet_pin == entered_pin:
                return {'status': 'success', 'message': 'PIN Valid'}
            else:
                return {'status': 'error', 'message': 'PIN Incorrect'}

        except Exception as e:
            return {'status': 'error', 'message': str(e)}


