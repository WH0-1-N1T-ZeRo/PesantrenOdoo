from odoo import api, fields, models


class OrangTua(models.Model):
    _inherit = 'cdn.orangtua'

    @api.model
    def create(self, vals):
        res = super(OrangTua, self).create(vals)
        user = self.env['res.users'].with_context(no_reset_password=True).sudo().create({
            'login': res.email,
            'name': res.name,
            'company_id': self.env.ref('base.main_company').id,
            'partner_id': res.partner_id.id,
            'password': 'partner',
            #assign to internal user
            'groups_id': [(6, 0, [self.env.ref('base.group_user').id]),
                          # assign to group ortu
                            (4, self.env.ref('pesantren_kesantrian.group_kesantrian_orang_tua').id),
                          ]
        })
        res.user_id = user.id
        return res
    def unlink(self):
        for orangtua in self:
            users = self.env['res.users'].search([('partner_id', '=', orangtua.partner_id.id)])
            if users:
                partner = users.partner_id
                users.unlink()
                partner.unlink()
        return super(OrangTua,self).unlink()
    


