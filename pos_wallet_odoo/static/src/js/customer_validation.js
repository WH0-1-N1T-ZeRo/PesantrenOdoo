odoo.define('pos_customer_validation', function(require) {
    'use strict';

    const { Gui } = require('point_of_sale.Gui');
    const PosComponent = require('point_of_sale.PosComponent');
    const ProductScreen = require('point_of_sale.ProductScreen');
    const Registries = require('point_of_sale.Registries');
    const { useState } = owl.hooks;

    class CustomerValidationButton extends PosComponent {
        constructor() {
            super(...arguments);
            this.state = useState({ pin: '' });
        }

        async onClick() {
            const currentOrder = this.env.pos.get_order();

            // Validasi apakah customer sudah dipilih
            if (!currentOrder.get_client()) {
                await Gui.showPopup('ErrorPopup', {
                    title: this.env._t('Customer Required'),
                    body: this.env._t('Please select a customer before proceeding with payment.'),
                });
                return;
            }

            // Munculkan popup PIN untuk customer
            const { confirmed, payload } = await this.showPopup('NumberPopup', {
                title: this.env._t('Enter Customer PIN'),
                body: this.env._t('Please enter the PIN for the selected customer.'),
            });

            if (confirmed) {
                // Contoh validasi PIN. Di sini kamu bisa tambahkan logika untuk memvalidasi PIN dari server.
                const customer = currentOrder.get_client();
                if (payload === customer.pin) { // Misalnya, PIN customer disimpan di field `pin`
                    console.log('PIN validated successfully');
                } else {
                    await Gui.showPopup('ErrorPopup', {
                        title: this.env._t('Invalid PIN'),
                        body: this.env._t('The PIN you entered is incorrect.'),
                    });
                }
            }
        }
    }

    CustomerValidationButton.template = 'CustomerValidationButton';

    ProductScreen.addControlButton({
        component: CustomerValidationButton,
        condition: function() {
            return true;
        },
        position: ['before', 'SetPricelistButton'], // Posisi tombol
    });

    Registries.Component.add(CustomerValidationButton);

    return CustomerValidationButton;
});
