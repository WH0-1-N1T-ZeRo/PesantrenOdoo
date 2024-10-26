odoo.define('point_of_sale.MessagePopup', function(require){
    'use strict';

    const AbstractAwaitablePopup = require('point_of_sale.AbstractAwaitablePopup');
    const Registries = require('point_of_sale.Registries');
    const { useState, useRef, onMounted } = owl;

    class MessagePopup extends AbstractAwaitablePopup {
        setup(){
            super.setup();
            this.state = useState({ text_value: '' });
            this.txtRef = useRef('text-value');
            this.txtplaceholder = "PIN Santri";

            // Fokuskan input ketika popup ditampilkan
            onMounted(() => this.txtRef.el.focus());
        }

        // Simpan nilai input saat confirm
        getPayload(){
            return this.state.text_value;
        }
    }

    MessagePopup.template = 'MessagePopup';
    Registries.Component.add(MessagePopup);

    return MessagePopup;
});
