#This file is part of Little Slice of My Life.

#    Little Slice of My Life is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.

#    Little Slice of My Life is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.

#    You should have received a copy of the GNU General Public License
#    along with Little Slice of My Life.  If not, see <https://www.gnu.org/licenses/>.

## File ini berisi opsi yang dapat di ubah untuk mengkustomisasi game mu.
##
## Baris yang di awali dengan dua 'tanda '#' adalah komentar, dan kamu tidak
## seharusnya menghapus nya. Baris dengan satu '#' adalah kode yang di
## komentari, kamu dapat menghapus tanda '#' jika di butuhkan.


## Dasar #######################################################################

## Nama game yang dapat dibaca oleh manusia. Ini digunakan untuk menset judul
## jendela, dan juga di tampilkan di antarmuka dan laporan kesalahan.
##
## Tanda _() yang mengelilingi string menandai itu dapat di terjemahkan.

define config.name = _("Little Slice Of My Life")


## Meng determinasikan apakah judul yang di berikan di atas di tampilkan di menu
## utama. Set ini ke False untuk menyembunyikan judul.

define gui.show_name = True


## Versi Permainan.

define config.version = "v0.0.3"


## Text that is placed on the game's about screen. Place the text between the
## triple-quotes, and leave a blank line between paragraphs.

define gui.about = _p("""Game ini dikembangkan oleh Muhammad "Hakase" Hamdani. Sebagai bagian dari langkah awal menggunakan Ren'Py.

Lemma Soft Forums: NotReality_

Wattpad: {a=https://www.wattpad.com/user/Penghayal_Pasif}Penghayal_Pasif{/a}

Gmail: mhdhamdani.formal@gmail.com



Sprite Amanda: Elzee

Background Art: Mugenjohncel




Semua cerita disini hanyalah fiksi belaka. Jika ada kesamaan nama tokoh, tempat, atau kejadian maka itu hanya ketidaksengajaan belaka.


""")

define gui.license = _p("""Software ini dilindungi oleh beberapa lisensi terpisah. Ada dua lisensi untuk gambar yang digunakan, dan satu lisensi untuk software itu sendiri, untuk selengkapnya bisa dilihat di bawah. Perlu diingat bawha lisensi yang akan ditampilkan berbahasa Inggris.

This software is protected under several seperated licenses. There's two licenses for the pictures, and one license for the software itself. For details can be seen below.



Little Slice Of My Life

Little Slice Of My Life is licensed under GNU GPL v3:

 This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with this program.  If not, see <https://www.gnu.org/licenses/>.


Sprite Lisa by Elzee

This sprite set is released under the following license:
Creative Commons Attribution-NonCommercial-ShareAlike

You are free to:

Share — copy and redistribute the material in any medium or format

Adapt — remix, transform, and build upon the material

The licensor cannot revoke these freedoms as long as you follow the license terms.

Under the following terms:

Attribution — You must give appropriate credit, provide a link to the license, and indicate if changes were made. You may do so in any reasonable manner, but not in any way that suggests the licensor endorses you or your use.

NonCommercial — You may not use the material for commercial purposes.

No additional restrictions — You may not apply legal terms or technological measures that legally restrict others from doing anything the license permits.


Background by Mugenjohncel

Terms of usage, as copied from {a=https://lemmasoft.renai.us/forums/viewtopic.php?t=17302} UNCLE MUGEN'S FREE VN (OELVN) RESOURCES{/a}:

▪ Feel free to use for whatever purpose it may serve best.

▪ OK for both Commercial and Free projects.

▪ Modifications are OK and highly encouraged.

▪ Not really required but I really do appreciate if you could tell me you have a project using these free resources.

▪ TLDR: Just take them... no strings attached...""")


################################

## Nama pendek permainan yang di gunakan untuk executable dan direktori di
## bangunan distribusi. Ini harus hanya berisi karakter ASCII-saja, dan tidak
## boleh mengandung  spasi, koma, atau kutip.

define build.name = "lsml"


## Suara dan musik #############################################################

## Tiga variabel ini mengendalikan mixer yang mana yang di tampilkan ke pemain
## secara default. Menset salah satu dari ini ke False akan menyembunyikan mixer
## tersebut.

define config.has_sound = False
define config.has_music = False
define config.has_voice = False


## Untuk mengijinkan pengguna memainkan test suara di chanel suara atau musik,
## silahkan hapus tag komentar nya '#' dan set sampel suara untuk di mainkan.

# define config.sample_sound = "sample-sound.ogg"
# define config.sample_voice = "sample-voice.ogg"


## Silahkan hapus komentar dari baris berikut ini untuk men set file audio yang
## akan di mainkan ketika pemain berada di menu utama. File ini akan terus
## dimainkan sampai permainan di mulai, sampai di hentikan atau file lain di
## mainkan.

# define config.main_menu_music = "main-menu-theme.ogg"


## Transisi ####################################################################
##
## Variabel ini menset transisi yang digunakan ketika event tertentu terjadi.
## Setiap variabel harus di set ke transisi, atau 'None' Untuk mengindikasikan
## bahwa tidak ada transisi yang harus di gunakan.

# Transisi setelah splashscreen
define config.end_splash_transition = dissolve

## Memasuki atau keluar dari menu permainan.

define config.enter_transition = dissolve
define config.exit_transition = dissolve


## Antara layar dari menu permainan

define config.intra_transition = dissolve


## Transisi yang di gunakan setelah game di load.

define config.after_load_transition = None


## Digunakan ketika memasuki menu utama setelah game berakhir.

define config.end_game_transition = dissolve


## Variabel untuk menset transisi yang digunakan ketika mulai game tidak
## tersedia. Melainkan, menggunakan pernyataan with setelah menunjukan layar
## tertentu.


## Managemen Jendela ###########################################################
##
## Ini mengendalikan kapan dialog di tampilkan. Jika "show", berarti selalu
## di tampilkan. Juka "hide", berarti itu hanya di tampilkan ketika dialog
## tersedia. jika "auto", jendela di sembunyikan sebelum pernyataan scene dan di
## tunjukkan kembali jika dialog ditampilkan.
##
## Setelah permainan di mulai, ini dapat di ganti dengan pernyataan "window
## show", "window hide", dan "window auto".

define config.window = "auto"


## Transisi yang digunakan untuk menunjukan dan menampilkan jendela dialog

define config.window_show_transition = Dissolve(.2)
define config.window_hide_transition = Dissolve(.2)


## Preferensi defaults #########################################################

## Mengendalikan kecepatan text default. Default nya, 0, ini berarti infiniti,
## Sementara angka yang lain adalah berapa karakter per detik yang akan di
## tampilkan.

default preferences.text_cps = 0


## Delay default otomatis-maju. Nomor yang lebih besar berujung kepada waktu
## menunggu lebih lama, 0 sampai 30 adalah jarak yang valid.

default preferences.afm_time = 15


## Direktori penyimpanan #######################################################
##
## Mengendalikan tempat penyimpanan file save untuk game ini secara spesifik
## untuk setiap platform. File akan di taruh di:
##
## Windows: %APPDATA\RenPy\<config.save_directory>
##
## Macintosh: $HOME/Library/RenPy/<config.save_directory>
##
## Linux: $HOME/.renpy/<config.save_directory>
##
## Ini shearus nya tidak usah di ganti, dan juga iya, harus selalu berisi
## string, bukan expresi.

define config.save_directory = "Untitled-1529658793"


## Ikon ########################################################################
##
## Ikon yang di tampilkan di taskbar atau dock.

define config.window_icon = "gui/window_icon.png"


## Pengaturan Build ############################################################
##
## Bagian ini mengendalikan bagaimana Ren'Py mengubah proyek mu ke file
## distribusi.

init python:

    ## Fungsi berikut mengambil pola file. Pola file merupakan case- insensitiv,
    ## dan sama dengan arah direktori dasar, dengan atau tanpa awalan /. Jika
    ## banyak pola sama, yang pertama yang akan di gunakan.
    ##
    ## Di dalam pola:
    ##
    ## / Ini adlaah
    ##
    ## * mencocokan semua karakter, kecuali pemisah direktori.
    ##
    ## ** mencocokan semua karakter, termasuk pemisah direktori.
    ##
    ## Contohnya, "*.txt" mencocokan file txt di direktori dasar, "game/**.ogg"
    ## matches ogg files in the game directory or any of its subdirectories, and
    ## "**.psd" matches psd files anywhere in the project.

    ## Mengklasifikasi file sebagai None  untuk memisahkannya dari distribusi
    ## build.

    build.classify('**~', None)
    build.classify('**.bak', None)
    build.classify('**/.**', None)
    build.classify('**/#**', None)
    build.classify('**/thumbs.db', None)

    ## Untuk mengarsipkan file, mengklasifikasikannya sebagai 'archive'.

    # build.classify('game/**.png', 'archive')
    # build.classify('game/**.jpg', 'archive')

    ## Alur Dokumentasi pencocokan file di duplikasikan di build app mac, jadi
    ## mereka tampil di kedua aplikasi dan juga file zip.

    build.documentation('*.html')
    build.documentation('*.txt')

## Menonaktifkan auto-relaod di android

define config.save_on_mobile_background = False

## Atur ini ke string yang berisi ID Developer Aplikasi Apple mu untuk
## mengaktifkan codesigning di Mac. Pastikan untuk mengganti nya ke ID mu
## sendiri yang sudah di berikan oleh Apple.

# define build.mac_identity = "Developer ID Application: Guy Shy (XHTE5H7Z42)"


## Kunci Lisensi Google Play di butuhkan untuk mendownload file tambahan dan
## untuk dapat melakukan pembelian in-app. Itu dapat di temukan di halaman
## "Services & APIs" delveloper konsol Google Play.

# define build.google_play_key = "..."


## Nama pengguna dan nama proyek yang di asosiasikan dengan proyek itch.io, di
## pisahkan dengan garis miring.

# define build.itch_project = "renpytom/test-project"
