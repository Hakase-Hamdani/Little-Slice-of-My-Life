# Kamu dapat taruh script game mu di file ini.

# Deklarasikan gambar di bawah line ini, menggunakan pernyataan image.
# cnth. image eileen happy = "eileen_happy.png"
image bg uni = "images/bg uni.jpg"
image bg lapangan = "images/bg meadow.jpg"
image bg kelas = "images/bg lecturehall.jpg"
image bg kantor = "images/bg club.jpg"
image black = "images/blck.png"
image intro = Movie(play="images/intro.mp4", pos=(10, 10), anchor=(0, 0))


# Deklarasikan karakter yang digunakan di game.
define l = Character('Amanda', color="#c8ffc8")
define a = Character('Me', color="#ccffcf")
define anvl = Character ('Me', color="#ccffcf", kind=nvl)
define author = Character ('', color="#ccffcc", kind=nvl)
define disclaimer = Character ('Disclaimer', color="#ccffcc", kind=nvl)

# Game dimulai disini.

label splashscreen:
    #$ renpy.movie_cutscene("intro_1.webm")
    show intro
    #jump intro
    #scene bg uni with dissolve
    with Pause(3.0)

#label intro:
    #scene black
    #$ renpy.pause(11, hard=True)
    #$ renpy.movie_cutscene("intro.webm")
    # show intro
    return


label start:
    scene black with dissolve

    anvl "Sangatlah wajar bagi seorang manusia untuk jatuh cinta, tidak peduli apakah kau laki-laki atau perempuan. Yang jelas jatuh cinta itu menunjukkan kalau manusia memiliki emosi."
    anvl "Di sini kau akan bermain sebagai diriku yang didefinisikan sebagai \"Me\" yang merupakan seorang laki-laki."
    anvl "Kau akan melihat bagaimana aku jatuh cinta pada seorang gadis."
    anvl "Hanya itu yang bisa kulakukan, karena sisanya kau yang menentukan."
    anvl "Jadi, semoga pilihanmu adalah yang baik."
    anvl "Karena hidupku sekarang berada di tanganmu, {i}User{/i}."

    nvl clear

    anvl "Jangan dianggap terlalu serius."
    anvl "Ini hanya permainan."

    nvl clear

    anvl "Remember, this is just a game."
    anvl "Have fun with my life!"

    nvl clear

    anvl "And...{w}{cps=15}Enjoy a little slice of my life!{/cps}"

    nvl hide
    nvl clear



    scene bg kelas with dissolve
    a "Satu hari lagi yang melelahkan, kadang berada di kelas itu membosankan."

    a "Untungnya, guru kali ini tidak membosankan."

    scene bg uni with dissolve
    show smile3

    a "Lalu, aku melihatnya. Saat di taman aku melihatnya."
    a "Aku sudah sering melihatnya, senyumnya itu familiar bagiku."
    a "Aku tahu siapa namanya, dia adalah Amanda. Dia orangnya baik dan selalu bersikap baik pada semua orang."
    a "Dia adalah temanku, kami sudah saling mengenal lama. Tapi hari itu, aku merasakan sesuatu yang lain..."
    a "{cps=20}...Aku merasa ingin lebih.{/cps}"

    hide smile3
    show scared1

    l "Hai, apa kau tidak apa-apa?"
    a "\"A...\""
    a "{w}\"...Aku baik.\""


    l "Apa kau yakin? Kurasa tidak begitu."
    a "\"Ya, aku baik-baik saja.\""
    l "..."
    a "\"Sungguh.\""

    hide scared1
    show smile3

    l "Baik. Kalau begitu, sampai jumpa besok!"

    hide smile3 with dissolve

    a "Sayang sekali, dia sudah pergi."
    a "Padahal aku menikmati perbincangan itu."
    a "Aku ingin perbicangan tadi menjadi lebih lama. Setidaknya lebih lama satu menit."

    scene black with dissolve

    a "Entah aku ini bodoh atau apa... Aku tidak bisa menyingkirkan wajahnya dari ingatanku."

    show smile3 with fade

    a "Dia ibarat hantu, menggentayangiku dalam tidurku."

    hide smile3 with fade

    a "Tapi, itu tidak berlangsung lama.{p}Karena pagi sudah tiba."

    scene bg kelas with dissolve

    a "Seperti biasa, aku kembali ke sekolah. Pagi-pagi sekali, tetapi kurasa aku datang terlalu pagi."
    a "\"Wah, masih tidak ada orang disini.\""

    show default

    l "Ternyata kau. Ku kira kau tadi siapa."
    a "Suara yang familiar itu sempat membuatku terkejut. Tapi, aku harus tampak biasa. Aku harus bersikap normal."
    a "\"Kenapa kau datang sepagi ini?\""

    hide default
    show embarrassed2

    l "Sebenarnya, aku biasanya memang datang sepagi ini, 'kan rumahku jauh."

    hide embarrassed2
    show default

    a "\"Oh, benar juga. Aku baru ingat.\""
    a "Sial, entah kenapa aku selalu merasa tidak nyaman didekat seorang gadis."

    hide default
    show scared1

    l "Apa kau tidak apa-apa?"

    menu:

        "\"Ya, aku tidak apa-apa.\"":

            jump tidakapa

        "\"Ya, aku tidak apa-apa. Aku hanya tidak terbiasa berada didekat gadis, apa lagi yang seperti kamu.\"":

            jump gadis

label tidakapa:

    a "\"Ya, aku tidak-apa.\""

    hide scared1
    show smile2

    l "Oh, bagus. Kebetulan aku sedang kesulitan dengan tugas matematika. Maukah kau membantuku?"
    a "\"Ya, tentu. Selama tugasnya tidak terlalu sulit.\""

    hide smile2
    show smile3

    l "Aku tidak bisa janji tugasnya tidak sulit."

    hide smile3

    a "Cukup lama kami berduaan. Perbincangan kami terkesan ringan, matematika dicampur dengan topik umum khas para pemuda pemudi."
    a "Aku menikmati perbincangan ini. Hanya kami berdua, tanpa ada orang lain. Hingga akhirnya momen itu harus terhenti karena teman-teman kami yang lain mulai berdatangan."

    jump tidakapa2

label gadis:

    a "\"Ya, aku tidak apa-apa. Aku hanya tidak terbiasa berada didekat gadis, apa lagi yang seperti kamu.\""

    hide scared1
    show embarrassed2

    a "Sial! Apa yang barusan kukatakan?"

    hide embarrassed2
    show angry5

    l "Kita anggap yang barusan tadi tidak pernah terjadi, oke?"

    hide angry5

    a "Dia langsung pergi menjauhiku."
    a "Sial! Sial! Sial! Bodohnya aku!"
    a "Sekarang aku semakin canggung jika berada didekatnya, dan sepertinya dia juga merasa tidak nyaman berada didekatku."
    a "Lupakan tentang itu, kami berdua harus bersikap seperti biasa sekarang. Karena teman-teman kami yang lain sudah berdatangan."

    jump bad1

label bad1:

    scene black with dissolve

    a "Semenjak hari itu, kami jadi jarang bicara."
    a "Kurasa, dia tidak akan pernah tahu bagaimana perasaanku padanya."
    a "Ini mengajarkanku satu hal, mungkin."
    a "Jaga mulutmu, apalagi dihadapan gadis yang kau sukai."
    a "Atau kau akan berakhir sepertiku."

    "{b}Bad Ending{\b}"

    a "Kurasa aku harus melupakannya."

    "{b}The End{\b}"

    jump credits

label tidakapa2:

    scene black with dissolve

    a "Hari demi hari berlalu, kami jadi semakin dekat lebih dekat dari sebelumnya."
    a "Kami mulai berbagi banyak hal, suka dan duka, rahasia kecil kami. Kami menjadi saling mengenal."
    a "Hingga saatnya tiba hari kelulusan."

    scene bg kelas with dissolve
    show smile2

    l "Jadi bagaimana, apa kau lulus?"
    a "\"Ya, aku dapat peringkat ke 3. Kau sendiri?\""

    hide smile2
    show smile3

    l "Tenang, aku lulus...{w} dan aku juga mendapatkan peringkat pertama!"
    a "\"Ya, aku juga turut senang untukmu.\""
    a "Aku harus berani, aku harus cari akal. Aku harus bisa mengatakannya sekarang."
    a "Sekarang, atau tidak sama sekali."

    menu:

        "Aku akan..."

        "Mengantarnya pulang, dan mengatakannya saat itu juga.":
            jump pulang

        "Mengatakannya saat kami sudah berada diluar.":
            jump diluar

label diluar:
    scene bg uni with dissolve
    a "Aku memperhatikan bagaimana keadaan sekitar, memastikan tidak ada siapa-siapa disini."
    a "Kurasa hanya ada kami berdua, karena yang lainnya sudah pulang duluan."

    show default

    l "Jadi, kenapa kita kesini?"
    a "Aku benar-benar gugup, setiap kalimat yang akan ku katakan padanya sudah berada di ujung lidah, dan aku berusaha agar aku tidak menenggaknya lagi."
    a "\"Jadi begini Amanda. Kita berdua tahu bahwa kita sudah sering bersama selama satu semester ini. Berbagi cerita dan rahasia, menjadi lebih saling mengenal.\""
    a "\"Sebenarnya aku mencintaimu, Amanda. Dan aku ingin hubungan kita lebih dari sekedar sahabat.\""

    hide default
    show shock2

    a "Aku sudah siap untuk kemungkinan terburuk."

    hide shock2
    show smile3

    l "Aku senang akhirnya kau berani mengungkapkan perasaanmu."
    a "Jawabannya itu membuatku lega, tapi menurutku itu belumlah jawaban final."


    l "Sebenarnya aku juga mau mengucapkan hal yang sama, hanya saja aku sedang mencari momen yang tepat."

    hide smile3
    show smile2

    l "Jika boleh aku mengaku, aku juga menginginkan hubungan kita lebih dari sekedar persahabatan."
    l "Jadi, kau mau jalan denganku?"

    menu:

        "Ya, kenapa tidak?":
            jump normal

label normal:

    hide smile2
    scene black with dissolve

    a "Sejak saat itu, kami menjadi semakin dekat."
    a "Hanya saja, sejak kami berdua bekerja demi bisa meneruskan ke universitas. Kami jadi jarang bertemu."
    a "Aku baru sadar, di saat aku mengungkapkan perasaanku. Kami masih begitu naif."
    a "Aku baru sadar, hubungan kami hanya sekedar cinta tanpa komitmen."
    a "Dan sekarang, aku juga sadar hubungan kami ujungnya tidaklah pasti."

    "{b}Normal Ending{/b}"

    a "{i}Katakan saja hubungan kami ini hanya sekedar pacaran, jadi sudah jelas bahwa ujungnya tidak jelas.{\i}"

    jump credits

label pulang:

    a "\"Jadi, apa kau ingin ku antar pulang?\""

    hide smile3
    show scared1

    l "Kenapa kau tiba-tiba ingin mengantarku pulang?"
    a "\"Kita 'kan sudah lulus. Aku hanya takut kita mungkin akan jarang bertemu.\""

    hide scared1
    show smile2

    l "Kurasa kau ada benarnya."

    hide smile2
    scene bg lapangan

    a "Jadi, aku mengantarnya pulang, jarak rumahnya agak jauh. Apa lagi aku mengantarnya hanya dengan sepeda."
    a "Semuanya bertambah runyam saat ban sepedaku bocor, jadi kami harus meneruskan perjalanan kami dengan jalan kaki."
    a "Cukup jauh kami berjalan, rumah Amanda juga masih jauh. Jadi, kami harus beristirahat sebentar. Kami istirahat di pinggir jalan."

    show sad1

    l "Aduh, masih jauh lagi."
    a "\"Maaf ya, karena aku kita harus jalan kaki.\""

    hide sad1
    show default

    l "Tidak apa-apa. Kita 'kan juga tidak tahu kalau bisa jadi begini."
    a "Aku harus mengatakannya sekarang, sekarang atau tidak sama sekali."
    a "\"Amanda, bolehkah aku mengatakan sesuatu?\""

    hide default
    show relieved1

    l "Ya, silahkan."
    a "Dia sudah memperbolehkanku. Inilah kesempatanku."
    a "Aku mau mengatakannya, setiap katanya, seluruh kalimatnya sudah ada diujung lidahku. Tapi sayangnya aku harus menenggak kembali semua itu."
    a "Aku tidak cukup berani."

    hide relieved1
    show scared1

    l "Jadi, apa yang mau katakan?"
    a "\"Sebenarnya...{w}Apa kau mau membuat Visual Novel denganku?\""

    hide scared1
    show embarrassed2

    a "Sunyi."
    a "Aku sudah bersiap untuk yang terburuk."

    hide embarrassed2
    show scared1

    l "Umm... Apa itu \"Visual Novel\"?"

    menu:

        "Visual Novel adalah..."

        "Sebuah game...":
            jump game

        "Sebuah buku interaktif...":
            jump buku

label game:

    a "\"Visual Novel adalah sebuah game yang bisa kau mainkan di komputer, atau smartphone.\""
    a "\"Visual Novel adalah game yang sederhana. Hanya terdiri dari gambar dan suara. Lalu juga terdiri dari pilihan-pilihan yang dapat mempengaruhi hasil dari game.\""

    hide scared1
    show default

    l "Jadi, Visual Novel itu adalah semacam game dengan multi ending. Begitu?"
    a "\"Ya.\""

    hide default
    show smile2

    l "Terdengar menyenangkan. Aku dulu pernah membuat komik web. Kurasa kemampuan itulah yang nanti kau perlukan, walau hasilnya nanti akan agak mengecewakan."
    a "\"Kau tahu kau tidak pernah mengecewakanku. Tidak pernah, sekalipun.\""

    jump nikah

label buku:

    a "\"Sebuah buku interaktif yang bisa kau mainkan di komputer atau smartphone. Di dalam Visual Novel kau bisa memilih hasil ceritanya, yang mana endingnya ditentukan oleh pilihanmu sepanjang alur cerita.\""

    hide scared1
    show default

    l "Semacam buku choose-your-story, begitu?"
    a "\"Tepat sekali.\""

    hide default
    show scared1

    l "Lalu, dimana bagian \"Visual\"-nya?"
    a "\"Visual Novel seringkali menggunakan gambar sebagai salah satu cara penceritaannya. Kadang juga menggunakan suuara dan video.\""

    hide scared1
    show smile2

    l "Terdengar menyenangkan. Aku dulu pernah mengurus sebuah komik web, kurasa kemampuanku itulah yang kau perlukan."
    a "\"Dan aku bisa menggunakan kemampuan programmingku.\""

    jump nikah

label nikah:

    scene black with dissolve

    a "Tak lama setelah kelulusan, kami sudah merilis visual novel pertama kami, walau sebenarnya mengurus visual novel hanyalah pekerjaan paruh waktu."
    a "Karena, saat itu aku bekerja di sebuah kantor, menjadi pengantar surat-surat, dan Amanda bekerja di sebuah restoran, menjadi seorang pelayan."
    a "Kami melakukan itu agar kami bisa meneruskan ke universitas."
    a "Lalu, visual novel kami mendapat review positif dan sempat diulas di salah satu majalah literasi dan gaming."
    a "Visual novel kami mendapat pujian dari sisi penceritaan, yang mana itu datang dariku. Dan pujian dari sisi ilustrasi, yang mana itu datang dari Amanda."
    a "Kami bisa meneruskan ke universitas pilihan kami menggunakan uang dari visual novel kami, dan kami terus membuat banyak visual novel."
    a "Lalu, saat kami berdua lulus, kami direkrut oleh salah satu perusahaan developer game. Kami menjadi semakin terkenal, dan hidup kami menjadi semakin mapan."
    a "Tapi, selama bertahun-tahun itu, aku selalu menyembunyikan perasaanku dari dia. Aku masih terlalu takut."
    a "{cps=20}Aku sudah menyembunyikan perasaanku terlalu lama...{/cps}"

    scene bg kantor with dissolve

    a "{cps=20}...Dan hari ini aku akan mengungkapkannya.{/cps}"

    show defaultc

    l "Maukah kau ku ajak ke suatu tempat?"
    a "Aku baru mau mengatakannya, tapi dia sudah bertanya lebih dulu. Kurasa aku harus menyimpan ini untuk nanti, untuk waktu dekat."
    a "\"Ya, tentu. Kemana kita akan pergi.\""
    l "Ke tempat dimana kita bisa mengenang masa lalu kita."

    hide defaultc
    scene bg lapangan with dissolve

    a "Aku ingat tempat ini, walau sudah bertahun-tahun berlalu."

    show defaultc

    l "Apa kau ingat saat kau mengantarku dengan sepeda, tetapi ban sepedamu bocor dan kita harus berjalan kaki sampai kerumah? Disinilah semua kejadian itu terjadi."
    a "\"Ya, aku masih ingat. Sungguh momen yang menyenangkan.\""

    hide defaultc
    show embarrassed2c

    l "Sebenarnya, aku membawamu kesini karena aku ingin mengatakan sesuatu."
    a "Ucapannya benar-benar mengejutkanku. Aku takut dia akan mengatakan yang terburuk, jadi kurasa inilah saatnya."
    a "\"Sebenarnya, aku juga ingin mengatakan sesuatu padamu.\""
    a "Setiap kata yang kuucapkan tadi, terlontar begitu saja tanpa dirangkai sedikitpun. Aku takut ini malah mengganggu momennya."

    hide embarrassed2c
    show defaultc

    l "Kalau begitu, kau duluan."

    menu:
        "Tidak, kau saja duluan.":
            jump amandaduluan

        "Baik, aku duluan.":
            jump akuduluan

label amandaduluan:

    hide defaultc
    show embarrassed2c

    l "Baik."
    l "Kau tahu kita sudah lama berteman, kita juga sudah lama bersama."
    a "Aku sudah siap untuk yang terburuk."
    l "Lalu, kita sudah sering berbagi suka duka, berbagi cerita, berbagi rahasia. Kita sudah saling mengenal."
    l "Aku merasa kau ingin sesuatu yang lebih."
    l "...{w}Aku juga menginginkan lebih, lebih dari sekedar teman, lebih dari sekedar sahabat."
    a "Ucapannya itu membuat jantungku berdegup kencang."
    l "Jadi...{w}Maukah kau menjadi pendamping hidupku?"
    a "Sebenarnya aku yang mau membuat momen ini, tapi kurasa dia sudah duluan, dan sekarang aku hanya punya satu jawaban untuk di ucapkan."

    menu:

        "Ya, aku mau.":
            jump nikah2

label nikah2:
    a "\"Ya, aku mau.\""

    hide embarrassed2c
    show smile2c

    l "Senangnya aku sudah mengungkapkan perasaanku."

    hide smile2c
    show smile3c

    l "Jadi, mari pulang dan rencanakan bagaimana pestanya."

    hide smile3c

    a "Itu tadi sungguh tidak terduga."

    scene black with dissolve

    a "Jadi, setelah pernikahan kami dan sembilan bulan penentuan. Anak pertama kami lahir, dia adalah seorang gadis. Aku benar-benar berharap bisa menunjukkan dia pada kalian, tapi sayangnya pencipta game ini tidak punya gambar ilustrasinya."
    a "Amanda telah menjadi istri yang baik, dan karena itulah aku akan mencintainya. Lalu, kehadiran anak pertama kami seakan memberikan warna pada kehidupan kami."
    a "Ayah, ibu. Andai kalian bisa melihat ini. Anakmu ini sudah menjadi seoarang ayah."
    a "Lalu, pesan untuk anakku untuk saat ini. Jadilah anak yang baik, dan jangan nakal."


    "{b}Good Ending 2{/b}"

    a "{i}And we live happily ever after.{/i}"
    "{b}FIN{/b}"

    jump credits

label akuduluan:

    a "\"Baik, jadi begini. Kita berdua tahu bahwa kita berdua sudah lama berteman, dan sudah lama saling mengenal.\""
    a "\"Kita berdua sudah sering berbagi cerita, dan berbagi rahasia.\""
    a "\"Diantara semua rahasia yang sudah kuberitahukan padamu, ada satu rahasia yang masih kupendam.\""
    a "\"Jadi...{w}Melawan sifatku yang terlalu perhitungan dan pemalu.{w} Aku akan mengatakan rahasia terbesarku, langsung di intinya.\""
    a "Dari sini, aku sudah siap untuk yang terburuk."

    hide defaultc
    show shock2c

    a "\"Jadi, bersediakah kau menjadi pendamping hidupku...\""


    a "\"Menemaniku, mencintaiku, dan selalu ada disampingku...{w}Tak peduli apapun yang terjadi...{w}Hingga ajal memisahkan kita?\""

    hide shock2c
    show smile2c

    l "Ya...{w}aku bersedia."
    a "Sunyi."
    a "Jawaban itu terus menggema di kepalaku."
    a "Hingga akhirnya, tanpa sadar bibirku membentuk seukir senyuman."

    hide smile2c
    show smile3c

    l "Kau lihat, lebih mudah diungkapkan dari pada dipendam."

    hide smile3c
    show smile2c

    l "Sebenarnya aku sudah tahu, kau memendam perasaan terhadapku. Tapi, lupakanlah. Kau sudah mengatakannya dan aku sudah memberikan jawabannya."
    a "\"Bagus, jadi mari kita pulang dan merencanakan bagaimana berikutnya.\""

    hide smile2c

    a "Itu berjalan lebih mulus dari yang kuduga."
    a "Ahh...{w}Lega rasanya akhirnya aku mengatakannya."

    scene black with dissolve
    l "Sayang?"
    a "\"Ya?\""
    l "Bolehkah kali ini giliranku yang bercerita?"
    a "\"Tentu, silahkan.\""

    scene bg lapangan with dissolve
    show defaultc with dissolve

    l "Hebat, bukan?"
    l "Aku bisa bermain-main dengan gambar-gambar yang sedang menjadi fokusmu."
    l "Kembali ke cerita."

    hide defaultc
    show smile2c

    l "Jadi, setelah hari pernikahan kami dan menunggu selama sembilan bulan. Akhirnya aku memberikan seorang anak gadis yang menjadi pengisi kehidupan rumah tangga kami."
    l "Aku benar-benar berharap bisa menunjukkan bayiku pada kalian, tapi sayangnya author Visual Novel ini tidak mempunyai sprite yang diperlukan."
    l "Dia yang selama ini didefinisikan sebagai \"Me\" telah menjadi suami yang baik, walau kadang dia bisa menjadi kekanakanakan dan membuatku kesal."

    hide smile2c
    show smile3c

    l "Tapi itulah salah satu hal yang membuatku terus mencintainya."

    hide smile3c
    show smile2c

    l "Satu pesan untuk anakku. Jadilah anak yang baik, dan turuti kata-kata ayah dan ibumu ini."

    hide smile2c
    show smile3c

    l "Sampai jumpa."

    hide smile3c
    scene black with dissolve

    "{b}Good Ending 1{/b}"
    l "{i}And we live happily ever after.{/i}"
    "{b}FIN{/b}"

jump credits

label credits:
    author "Sebelumnya aku berterima kasih pada Tom \"Pytom\" Rothamel untuk software hebat ini."
    author "Aku juga berterima kasih pada Mugenjohncel untuk background, dan Elzee yang telah memperbolehkan sprite character buatannya digunakan di proyek kecil non-komersial ini."

    nvl clear

    anvl "Aku juga mau berterima kasih pada pemain, karena telah mau bermain sebagai diriku dalam sepotong kecil kisah dari hidupku."

    nvl clear
    nvl hide

    show smile2c

    l "Aku juga mau berterima kasih pada author karena telah menciptakan dunia yang begitu sempit ini."

    nvl clear
    nvl hide

    hide smile2c
    show smile3c

    l "Thank you for playing!"

    hide smile3c

    menu:

        "Pesan tambahan dari author.":
            jump ptmhn

        "Kembali ke menu.":
            jump baper

label ptmhn:
    author "Sebenarnya, aku ingin mendedikasikan ini pada seseorang, tapi...{w}{cps=15} sekarang aku sedang bimbang.{/cps}"
    nvl clear

jump baper

label baper:
    author "{size=40}Jangan baper,ya.{w} Ingat, ini hanya cerita."
    nvl clear
    author "{size=40}See ya!"

jump ret

label ret:
    return
