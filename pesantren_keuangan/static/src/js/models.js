odoo.define('pesantren_keuangan.models',function(require){
    'use strict'
    var models = require('pos_wallet_odoo.models')
    
    models.load_fields('res.partner', ['has_wallet_pin', 'wallet_pin', 'barcode_santri']);

    var _super_posmodel = models.PosModel.prototype;
    models.PosModel = models.PosModel.extend({
        initialize: function(session, attributes) {
            var partner_model = this.models.find(model => model.model === 'res.partner');
            partner_model.fields.push('has_wallet_pin', 'wallet_pin', 'barcode_santri');
            return _super_posmodel.initialize.call(this, session, attributes);
        },
    });

})