# -*- coding: utf-8 -*-
#    ________  __      ________  _______   ______          _______    _______   ________     __      _____  ___  ___________  _______    _______  _____  ___   
#   /"       )|" \    /"       )/"     "| /    " \        |   __ "\  /"     "| /"       )   /""\    (\"   \|"  \("     _   ")/"      \  /"     "|(\"   \|"  \  
#  (:   \___/ ||  |  (:   \___/(: ______)// ____  \       (. |__) :)(: ______)(:   \___/   /    \   |.\\   \    |)__/  \\__/|:        |(: ______)|.\\   \    | 
#   \___  \   |:  |   \___  \   \/    | /  /    ) :)      |:  ____/  \/    |   \___  \    /' /\  \  |: \.   \\  |   \\_ /   |_____/   ) \/    |  |: \.   \\  | 
#    __/  \\  |.  |    __/  \\  // ___)(: (____/ //       (|  /      // ___)_   __/  \\  //  __'  \ |.  \    \. |   |.  |    //      /  // ___)_ |.  \    \. | 
#   /" \   :) /\  |\  /" \   :)(:  (    \        /       /|__/ \    (:      "| /" \   :)/   /  \\  \|    \    \ |   \:  |   |:  __   \ (:      "||    \    \ | 
#  (_______/ (__\_|_)(_______/  \__/     \"_____/       (_______)    \_______)(_______/(___/    \___)\___|\____\)    \__|   |__|  \___) \_______) \___|\____\) 
#
#

                                                                                                                                                            

{
    'name': "Modul Guru SISFO Pesantren",

    'summary': """
        Aplikasi SISFO Pesantren
        - Modul Guru untuk SISFO Pesantren""",

    'description': """
        Aplikasi SISFO Pesantren memiliki fitur-fitur sebagai berikut :
        ===============================================================
        * Modul Base / Dasar
        * Modul Akademik
        * Modul Keuangan
        * Modul Guru
        * Modul Orang Tua
        * Modul Kesantrian

        Developed by : 
        - Imam Masyhuri
        - Supriono

        Maret 2022

        Informasi Lebih lanjut, hubungi :
            PT. Cendana Teknika Utama 
            - Ruko Permata Griyashanta NR 24-25 
              Jl Soekarno Hatta - Malang
    """,

    'author': "PT. Cendana Teknika Utama",
    'website': "https://www.cendana2000.co.id",
    'category': 'Education',
    'version': '18.0.1.0',
    'license': 'LGPL-3',

    # any module necessary for this one to work correctly
    'depends': ['base','pesantren_base','report_xlsx'],

    # always loaded
    'data': [
        'security/groups.xml',
        'security/ir.model.access.csv',
        # wizard

         # data
        'views/menu.xml',
        # views
        # 'data/ks_guru_data.xml',
        'views/absensi_siswa.xml',
        'views/master_rpp.xml',
        'views/penilaian.xml',
        'views/penugasan.xml',
        'views/penilaian_akhir.xml',
        'views/penilaian_akhir_guru.xml',
        'views/predikat.xml',
        # reports
        'reports/report_penilaian_akhir.xml'
    ],
    # only loaded in demonstration mode
    # 'demo': [
    #     'demo/demo.xml',
    # ],
    "installable": True,
	"auto_install": False,
	"application": True,  
}