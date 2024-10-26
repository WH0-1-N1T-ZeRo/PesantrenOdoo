import { _t } from "@web/core/l10n/translation";
import { NumberPopup } from "@point_of_sale/app/utils/input_popups/number_popup";
import { AlertDialog } from "@web/core/confirmation_dialog/confirmation_dialog";
import { ControlButtons } from "@point_of_sale/app/screens/product_screen/control_buttons/control_buttons";
import { patch } from "@web/core/utils/patch";

let pinAttempt = 0; // Counter untuk percobaan pin
let lockoutTimeout = null; // Timeout untuk blokir
let enteredPin = ''; // Simpan PIN yang dimasukkan

patch(ControlButtons.prototype, {
    async clickSetSubTotal() {
        this.dialog.add(NumberPopup, {
            title: _t('Masukkan PIN'),
            startingValue: 0,
            getPayload: (num) => {
                this.apply_pin(num);
            },
        });
    },

    async apply_pin(pc) {
        // Ambil teks dari elemen set-partner (menggambarkan nama partner yang dipilih)
        const partnerNameElement = document.querySelector('.set-partner .text-truncate');
        const partnerName = partnerNameElement ? partnerNameElement.innerText.trim() : null;
        console.log(partnerName);  // Untuk debugging

        // Pastikan teks nama customer ada
        if (!partnerName) {
            this.dialog.add(AlertDialog, {
                title: _t('No Customer Selected'),
                body: _t('Please select a customer from the list before entering the PIN.'),
            });
            return;
        }

        // Cek apakah sudah 3 kali percobaan PIN
        if (pinAttempt >= 3) {
            this.dialog.add(AlertDialog, {
                title: _t('PIN Blocked'),
                body: _t('You have entered the wrong PIN 3 times. Please wait for 1 hour to try again.'),
            });
            return;
        }

        // Reset PIN yang dimasukkan
        enteredPin = ''; 
        enteredPin += pc; // Simpan PIN yang baru dimasukkan

        // Kirim PIN dan nama customer ke backend untuk dicek
        try {
            const response = await this.rpc({
                route: '/pos/check_pin',
                params: {
                    partner_name: partnerName,
                    entered_pin: enteredPin,
                },
            });

            if (response.status === 'success') {
                pinAttempt = 0; // Reset counter percobaan PIN
                const order = this.pos.get_order();
                const selectedLine = order.get_selected_orderline();
                if (selectedLine && selectedLine.product_id.is_subtotal_to_qty_pp) {
                    const qty = pc / selectedLine.get_lst_price();
                    selectedLine.set_quantity(qty);
                }
                return true; // Validasi berhasil
            } else if (response.status === 'error') {
                pinAttempt += 1; // Tambah percobaan PIN
                if (pinAttempt >= 3) {
                    this.dialog.add(AlertDialog, {
                        title: _t('PIN Blocked'),
                        body: _t('You have entered the wrong PIN 3 times. Please wait for 1 hour to try again.'),
                    });
                    // Set timeout untuk 1 jam
                    lockoutTimeout = setTimeout(() => {
                        pinAttempt = 0;
                    }, 3600000); // 1 jam dalam milidetik
                } else {
                    this.dialog.add(AlertDialog, {
                        title: _t('PIN Incorrect'),
                        body: _t(`PIN Salah, Anda memiliki ${3 - pinAttempt} kesempatan lagi.`),
                    });
                }
            }

        } catch (error) {
            this.dialog.add(AlertDialog, {
                title: _t('Error'),
                body: _t('Terjadi kesalahan saat memvalidasi PIN.'),
            });
        }
    },
});
