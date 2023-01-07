image cg_1 = "cgColored/R1_1_alios_remil_snake.png"
image cg_2 = "cgColored/R1_2_remil_airterjun.png"
image cg_3 = "cgColored/R1_3_alios_remil_cherry.png"
image cg_4 = "cgColored/R1_4_remil_kai.png"
image cg_5 = "cgColored/R1_5_remil_jalan_pincang.png"
image cg_6 = "cgColored/R1_6_cherry_remil.png"
image remi_cg_end= "cgColored/R1_7_remil.png"

label branch1:
    #CHAPTER 1
    #“Pemimpin dari Kelompok yang Berbahaya” with dissolve(3.0)
    scene black with Dissolve(1.0)
    scene chp_1 with Dissolve (2.5)
    "Pemimpin dari Kelompok yang Berbahaya"
    scene tenda_gelap with Dissolve (2.5)
    # scene perkemahan dusk with dissolve(3.0)
    #show angry Alios  as alios di kiri
    show alios_angry3 at enterl1
    al "Mengerikan?{w=0.1} Kau dan pikiran bodohmu!{w=0.1} Orang tidak berguna ini pantas mendapatkannya setelah datang dengan sembrono.{w=0.1} Mereka bisa menghabisi kita!"
    # show angry elena as elina di kanan
    show elena_angry at enterr1
    e "Bagaimana bisa kamu mengatakan itu! {w=0.2}Laki-laki itu juga teman kita, bukan?"
    hide elena_angry
    hide alios_angry3
    #hide alios
    #hide elena
    "Kepala monster tersebut bergelinding di tanah setelah ditebas oleh kapak besar Alios. Namun, Alios baru saja menghabisi orang itu."

    #show normal alios as alios di kiri
    show alios_normal at enterl1
    al "Daritadi apa yang kau lihat, bocah? {w=0.2}Kau tidak senang padaku?"
    r "(Apa-apaan?)"
    r "Sombong sekali kamu dengan wajah pembunuhmu itu?"
    hide alios_normal
    #show normal jeffrey as jeffrey di kanan
    show jeffrey_normal at enterr1
    j "Tenanglah, kawan. Bos tidak akan melakukan hal yang merugikan kita. Ini pastinya lebih baik, bukan? Dibanding kepala kita yang bergelinding di situ."
    r "(Benar, Aku juga berpikir begitu sekilas{w=0.3}.{w=0.3}.{w=0.3}. Tunggu, apa yang baru saja kupikirkan!)"
    r "Kau!"
    r "(Aku mengarahkan belatiku ke Jeffrey)"
    j "Baiklah, lupakan masalah seriusnya. {w=0.1}Kita harus cepat memotong daging itu"
    hide jeffrey_normal
    #hide jeffrey
    "Setelah itu, Aku memutuskan untuk diam agar tidak merusak suasana. Aku percaya bahwa Alios melakukan ini untuk keselamatan kami."
    #dissolve selama 3s

    #scene kantin malam
    scene canteen_night2 with Dissolve (2.5)
    #show jeffrey laugh as jeffrey di kiri
    show jeffrey_laugh at enterl1
    j "Hahaha"
    #show jeffrey happy as jeffrey di kiri
    show jeffrey_happy as jeffrey_laugh
    j "Anda berlebihan melakukannya, Bos!"
    show alios_sad at enterr1
    #show sad alios as alios di kanan
    al "Itu bukan pengalaman yang menyenangkan, tapi terima kasih"
    hide jeffrey_laugh
    #hide jeffrey
    show alios_normal as alios_sad
    #show Alios normal as alios di kanan
    al "Kau tidak masalah bukan? Kalian sendiri yang datang membawa monster seolah-olah ingin menghancurkan tempatku"
    a "Y-Ya"
    hide alios_sad
    #hide alios
    "Dia terlihat seperti menahan amarahnya... aku harus menenangkanya"

    #show normal  jeffrey as jeffrey di kiri
    show jeffrey_normal at enterl1
    j "Hey, Remil, apa yang kamu lakukan dari tadi mengintip ke sana kemari?"
    r  "Tidak ada"
    r "Aku akan pergi membawakan makan malam Elena. Aku khawatir dia masih memikirkan tentang masalah saat sore tadi."
    #show normal cherry di kanan
    show cherry_normal at enterr1
    c "Memang kamu siapanya? Dasar bodoh"

    #scene perkemahan night with dissolve(1.0)
    scene tenda_gelap with Dissolve (1.0)
    r "Maaf, Aku masuk untuk membawakanmu makan malam"
    #show sad elena as elena di kanan
    show elena_sad at enterr1
    e "Masuklah"
    r "Apa kamu masih memikirkan itu?"
    e "Ya. Aku masih ingat bagimana Alios menghancurkan kepala anak itu"
    #show confused elena as elena di kanan
    show elena_confused as elena_sad
    e "sebenarnya, apa yang dia pikir dia lakukan!"
    r "...."
    #show sad elena as elena di kanan
    show elena_sad as elena_sad
    e "Terima kasih, tolong ditinggalkan saja di sana"
    r " Aku akan berada di tendaku kalau kamu butuh sesuatu, jangan lupa makanlah nanti"
    #hide elena
    hide  elena_sad
    "Setelah itu, Aku memutuskan untuk diam agar tidak merusak suasana. Aku percaya bahwa Alios melakukan ini untuk keselamatan kami"

    #scene bg kantin night with dissolve(3.0)
    scene canteen_night2
    "Di luar, semua orang berkumpul, kecuali Elena"
    r "Hei, apa yang terjadi? Kemana Elena"
    #show sad cherry as cherry di kiri
    show cherry_sadpout at enterl1
    c "Saat bangun, Cherry tidak melihat kak Elena di manapun. Cherry tidak tahu dia ke mana"

    menu:
        "Alios! Apa yang telah kamu lakukan pada Elena!":
            jump b1deca
        "(Apa Elena pergi memberontak?)":
            jump b1decb
    return


label b1decb:
    r "Elena kemungkinan pergi sendiri.."
    #show suprise cherry as cherry di kiri
    show cherry_surprised as cherry_sadpout
    c "!!"
    r "Dan, semua ini salahmu, Alios!"
    jump b1deca


label b1deca:
    r "Alios! Apa yang telah kamu lakukan pada Elena!"
    #show angry alios as alios di kanan
    show alios_angry1 at enterr1
    al "Apa maksudmu, bocah? Kau masih tidak senang dengan apa yang terjadi semalam?"
    #hide cherry
    hide cherry_sadpout
    #show normal jeffrey as jeffrey di kiri
    show jeffrey_normal at enterl1
    j "Tidak, Bos. Dia hanya.."
    #show normal alios as alios di kanan
    show alios_normal as alios_angry1
    al "Tenang, bukan Aku. Kau bisa camkan kataku"
    #hide jeffrey
    hide jeffrey_normal
    al "Aku tidak akan pernah merugikan diriku sendiri dengan menghilangkan pekerja terbaik kita"
    b "Maaf, Aku ragu dengan katamu"
    hide alios_angry1
    #hide alios
    "Raut wajah Alios menatap laki-laki tersebut dengan tidak senang, namun dia tidak mundur"

    #show angry jeffrey as jefrey di tengah
    show jeffrey_angry1 at enter
    j "Ah tolong tenang, kalian! Berpikirlah dengan jernih dulu."
    r " …"
    #show normal jeffrey as jefrey di tengah
    show jeffrey_normal as jeffrey_angry1
    j "Untuk masalah ini, kurang lebih Aku bisa diandalkan karena sering pergi berburu bersamanya. Biar kita pergi mencari jejaknya dulu, ya?"
    "(Bagaimana kita bisa yakin kita bisa menemukan Elena, jika dia masih hidup)"
    hide jeffrey_angry1
    #hide jeffrey
    "Jeffrey mendekat dan menepuk pundakku"

    #show normal jeffrey as jeffrey di tengah
    show jeffrey_normal at enter
    j"Aku menemukan tempat yang menarik kemarin, kita akan mulai mencari dari situ"
    #show normal alios as alios di kanan
    show alios_normal at enterr1
    al "Baiklah, begini lebih mudah. Aku biarkan kau memimpin, bocah. Kita serahkan jalan ke Jeffrey"
    #show serious cherry as cherry di kiri
    show cherry_serius at enterl1
    c  "Cherry ikut dengan kalian!"
    r "Baiklah. Kita bergerak selagi masih pagi. Kemas bawaan kalian secepat mungkin sebelum siang!"

    #scene hutan day with dissolve(3.0)
    scene hutan with Dissolve (2.5)
    #show normal alios as alios di kiri
    show alios_normal at enterl1
    al "Kemana kau mengarahkanku, Jeffrey?"
    #show normal jeffrey as jeffrey di kanan
    show jeffrey_normal at enterr1
    j "Tenang saja, Bos- Maksudku, Alios. Lurus dari sini terdapat rahasia yang mendebarkan"
    #hide alios
    hide alios_normal
    j "Dan seharusnya kita sudah sampai"
    "Mereka menemukan sebuah gubuk besar yang dibangun di tengah hutan"
    hide jeffrey_normal
    #hide jeffrey

    #scene gubuk luar day with dissolve(1.0)
    scene gubuk_luar_day with Dissolve (1.0)
    r "ini bukannya gazebo biasa?"
    show jeffrey_angry2 at enter
    #show angry jeffrey as jeffrey di tengah
    j "Kamu pasti bercanda, gubuk ini luar biasa! Lihatlah ke dalam"
    r "Maaf, ini terlalu berdebu, tolong bersihkan"
    "Remil mengibas-ngibas sekitar sambil menutup mulutnya."
    #hide jeffrey
    hide jeffrey_angry2
    #show normal alios as alios di kanan
    show alios_normal at enterr1
    al "Kau dengar? Lakukan, Cherry"
    show cherry_normal at enterl1
    #show normal cherry as cherry di kiri
    c "Baaik!"
    hide alios_normal
    hide cherry_normal
    #hide alios
    #hide cherry
    "Cherry beranjak masuk ke dalam dan mulai menggunakan sihir yang mendorong debu keluar"
    r "Ini mengerikan! (Remil tetap batuk batukmeski menunggu di luar)"
    "Tidak lama kemudian, Cherry keluar"
    r "Terima kasih! Kamu tidak apa-apa, Cherry?"
    #show bored cherry as cherry di tengah
    show cherry_bored at enter
    c "Tidak apa, Cherry menghempas debu dari sekeliling jadi tidak kenapa-napa, tidak sepertimu"
    #show normal jeffrey as jeffrey di kanan
    show  jeffrey_normal at enterr1
    j  "Tunggu, apa kamu melihat seseorang di dalam?"
    #hide cherry
    hide cherry_bored
    r "Bukankah ini tempat yang sudah ditinggalkan? Habis kayak begini sih tempatnya."
    #show sad jeffrey as jeffrey di kanan
    show jeffrey_sad as jeffrey_normal
    j "Tidak, kemarin-kemarin Aku melihat tanda-tanda seseorang tinggal di sini, kupikir tadi kita bisa bertanya kepada orang itu."

    #scene bg gubuk dalam day with dissolve(1.0)
    scene dalam_gubuk_api_mati with Dissolve (1.0)
    #show happy jeffrey as jeffrey di kiri
    show jeffrey_happy at enterl1
    j "Hey, tempat ini cukup luas! Tidak bisakah kita pindah ke sini?"
    r "(Orang ini emosinya labil sekali ya)"
    show alios_surprised at enterr1
    #show suprised alios as alios di kanan
    al "Ini terlihat berguna, mungkinkah ini buatan seseorang?” Melihat ke arah kumpulan botol tanah liat di rak"
    hide alios_surprised
    hide jeffrey_happy
    #hide alios
    #hide jeffrey
    "Aku masuk ke salah satu ruangan di dalam gubuk?"

    r"(Ruangan ini cukup sempit…)"
    r "Ke mana tempat ini mengarah? "
    "…"
    "Di dalam sini cahaya sangat minim dan terdapat banyak jasad monster, selain itu juga terdapat potongan organ yang baunya kurang menyenangkan. Di atas meja, Aku menemukan lembaran kertas"
    #show item lembaran penelitian
    show old_book
    pause 2.0
    hide old_book
    #hide item lembar penelitian
    "(Beruang, serigala, kambing, ikan, semua ini… monster..?)"
    r "Tunggu, ular besar kemarin juga monster, kan? Kenapa tidak ada?"
    r "(Aku harus kembali berkumpul dengan yang lain)"
    r "Teman-teman! Tolong keluar dulu!"

    #scene gubuk luar day with dissolve(3.0)
    #show normal alios as alios di kiri
    al "Ada apa, Remil?"
    r  "Ini, baru saja Aku menemukannya"
    #show item lembaran penelitian
    show old_book
    pause 2.0
    hide old_book
    #hide item lembar penelitian
    show cherry_bored at enterr1
    #show bored cherry as alios di kanan
    c "Jadi, apa ini sampah yang kamu temukan di dalam?” Seolah menyindir Alios yang membawa botol tanah liat"
    #show happy alios as alios di kiri
    show alios_happy at enterl1
    al "Kertas? Hahaha, menarik!"
    #show smirk alios as alios di kiri
    show alios_smirk as alios_happy
    al  "Mungkin mereka yang meninggalkan ini masih di sekitar sini, Aku jadi suka ini"
    #hide cherry
    hide cherry_bored
    #show normal jeffrey as jeffrey di kanan
    show jeffrey_normal at enterr1
    j "Aku kurang yakin, kertas ini mencurigakan. Mungkin saja sesuatu ini yang menculik Elena, kan?"
    #hide alios
    hide alios_happy
    r " …"
    #hide jeffrey
    hide jeffrey_normal
    #show normal alios as alios di kiri
    show alios_normal at enterl1
    al "Dengarkan, kurasa jika kita ingin mencari perempuan itu, kita harus berpencar, sampai kita menemukan kota orang-orang."
    #show normal jeffrey as jeffrey di kanan
    show jeffrey_normal at enter
    j "Baiklah, jika mereka orang jahatnya kita hanya perlu menghajarnya, bukan?"
    #hide alios
    hide alios_normal
    r "Kamu pasti bercanda…"
    j "Kalau begitu, tolong ikuti Aku."
    #hide jeffrey
    hide jeffrey_normal
    "Kami berjalan lurus dari arah gubuk"

    #show CHAPTER 2
    scene chp_2 with Dissolve (2.5)
    "Hukum Rimba: Memangsa atau Dimangsa"
    #“Hukum Rimba: Memangsa atau Dimangsa” with dissolve(3.0)

    #show bg Hutan - Day with dissolve(3.0)
    show hutan with Dissolve(3.0)
    r "Di hutan ini benar-benar tidak ada orangnya ya?"
    #show normal jeffrey as jeffrey di tengah
    show jeffrey_normal at enter
    j "Kita tidak bisa mengambil kesimpulan itu, semenjak kita bahkan belum keluar dari hutan ini."
    r "(Sungai ini…)"
    j "Kurasa kita harus berpencar.."
    j "Aku akan mengambil jalan di kanan bersama teman kita yang satu ini."
    r "(jeffrey melihat ke arahku)"
    menu:
        "Baiklah. Kalau begitu Aku, Alios, dan Cherry ke kiri":
            jump b1deca1
        "Apa kamu yakin? Aku rasa sebaiknya kita tetap jalan bersama":
            jump b1decb1


    return

label b1decb1:
    r "Apa kamu yakin? Aku rasa sebaiknya kita tetap jalan bersama"
    #show angry jeffrey as jeffrey di tengah
    show jeffrey_angry1 as jeffrey_normal
    j "Remil, nyawa Elena mungkin sedang terancam. Di saat seperti inilah kita harusnya berpencar"
    r "Baiklah. Kalau begitu Aku, Alios, dan Cherry ke kiri"
    jump b1deca1
    return


label b1deca1:
    #scene bg dekat sungai dusk with fade (3.0)
    scene dekat_sungai with Fade(1.0,1.0,1.0)
    #show bored cherry as cherry di kiri
    show cherry_bored at enterl1
    c "“Heei, berapa lama kita akan berjalan?"
    #show normal alios as alios di kanan
    show alios_normal at enterr1
    al "Diamlah, Cherry. Kau bahkan tidak membawa apapun bersamamu"
    al "Sebentar, lihat ke bawahmu"
    #hide cherry
    hide cherry_bored
    r "(Jejak ini…)"
    al "Aku baru pertama kali melihat jejak lurus begini, bukankah ini seperti…"
    r "Jejak ular!"
    hide alios_normal
    #hide alios.
    r "Kita harus pergi dari sini. Cepat!"
    play sound "audio/sfx_snakehiss.wav"
    #play sound snake hiss
    ur " hiss"
    show cherry_surprised at enterl1
    #show suprised cherry as cherry di kiri
    c "Hiiih, suara apa itu!"
    r "Cherry! Cepat tahan! Di depanmu"
    show cherry_serius as cherry_surprised
    #show serious cherry as cherry di kiri
    c "Sungai, penghalang terjadilah!"
    r "(Bodoh! Jangan yang itu!)"
    show cherry_surprised as cherry_surprised
    #show suprise cherry as cherry di kiri
    c "Kenapa dia mendekat"
    #hide cherry
    hide cherry_surprised
    "Di saat itu, Alios melemparkan botol ramuan ke ular dan tercipta kabut"
    "Setelah itu, Cherry terpental karena ular menerjang tepat ke arahnya"

    #scene bg dekat sungai dusk with fade (1.0)
    scene dekat_sungai_dusk with fade
    r "Ugh- Sakit."
    show cherry_surprised at enterl1
    #show suprise cherry as cherry di kiri
    c "Aah- Tidak bisa, Cherry tidak bisa!"
    "Cherry Merangkak ke arah hutan"
    hide cherry_surprised
    #hide cherry
    show alios_normal at enterr1
    #show normal alios  as alios di kanan
    al "Ck, tidak berguna."
    r "(Alios hebat, dia menancapkan kapaknya ke dalam tanah)"
    #show angry alios  as alios di kanan
    show alios_angry2 as alios_normal
    al "Bangun, bocah! Kita harus menaklukkan ini berdua"
    r "... (Mengangguk)"
    r "Alios! Aku akan menggiringnya, kamu carilah kesempatan!"
    #show normal alios  as alios di kanan
    show alios_normal as alios_normal
    al "Kau pikir siapa yang kau suruh?"
    r "(Orang ini masih saja sombongnya selangit)"
    #hide alios
    hide alios_normal
    r "(.. Kabut akan mulai menghilang, Aku akan bergerak ke arah yang berbeda mendekati ular)"


    #scene BG Hutan - Day with dissolve(3.0)
    scene hutan with Dissolve(3.0)
    "Remi berlari ke dalam hutan. Di saat yang singkat saat ular menerjang dengan kepalanya, Remi menghindar"
    "Remi mendaki ke atas pohon dan merangkak ke dahan besar, kemudian ular tersebut melihat Remi lalu memutar badannya ke arah Remi"

    #show CG Alios dan Remil melawan ular besar di hutan (Hutan - Day) with fade(3.0)
    $ persistent.cg_R1_1_alios_remil_snake = True
    scene cg_1 with Fade (1.0, 1.0, 1.0)
    al "Kemana kau melihat, dasar serangga!” Mengayunkan kapak untuk mensayat perut ular yang melilit pohon"
    #play sound axe slashing
    play sound sfx_axeslash
    r "(Berhasilkah!?)"
    r "Hah?"
    "Kapak Alios bahkan tidak menggores kulit ular dan dia malah terdorong mundur karena kapaknya yang berat."

    al "Duh, sialan! Keras sekali sih sisikmu, cacing!"
    #play sound tree shaking
    play sound sfx_treeshaking
    r "(Batang pohon ini akan hancur, akan kuserang di saat ini selagi Alios membuka kesempatan)"
    "Aku merunduk dan memegang dahan dengan kuat lalu melompat ke arah kepala ular yang melihat Alios"

    r "Haaaa!” Menusuk belati ke mata ular"
    "Aku melompat dari dahan pohon dan baru saja mengambil pijakanku dan merunduk di bawah"

    #scene  BG Hutan - Day with fade(1.0)
    scene hutan with fade
    r  "Huf-huf"
    n "Habis kau, keeeooong!"
    #play sound felsh tearing
    play sound sfx_fleshtearing
    # show alios angry2 as alios di tengah
    show alios_angry2 at enter
    "Alios merobek mulut ular secara vertikal yang menggeliat kesakitan."

    n "M-Menghindar!"

    #hide allios
    hide alios_angry2
    "Racun ular merembes keluar ke punggungku."
    r "Hah!"
    # show normal alios  as alios di tengah
    show alios_normal at enter
    al "Kau baik-baik saja, bocah?"
    r  "Ya, entah bagaimana.."
    # show happyl alios  as alios di tengah
    show alios_happy as alios_normal
    al "Kerja bagus, sebaiknya kita mengambil bawaan kita karena mulai gelap"
    r " …"
    # show normal alios  as alios di tengah
    show alios_normal as alios_normal
    al "Sebelum itu, Kau bau dan lengket. Melompatlah ke sungai"


    #show BG Dekat Sungai - Dusk with dissolve(3.0)
    scene dekat_sungai_dusk with Dissolve(3.0)
    r "Daging ular ini banyak sekali…"
    # show happy alios  as alios di tengah
    show alios_happy at enter
    al "Ini baru namanya pesta! Hahaha!” Membakar perut ular sangat besar"
    r  "Tunggu, hanya kita berdua yang makan?"
    # show normal alios  as alios di tengah
    show alios_normal as alios_happy
    al "Kukira kau kuat makan banyak?"
    r "?"
    #hide alios
    hide alios_happy
    r "Baiklah, tetapi Aku akan pergi mencari Cherry sebentar"
    # show normal cherry  as cherry di kiri
    show cherry_normal at enterl1
    c "Di sini ada orang? Tolong!"
    r "Oh, Cherry. Panjang umur"
    # show sad cherry  as cherry di kiri
    show cherry_sadpout as cherry_normal
    c "Hiks, kalian selamat? Cherry sangat takut!"
    show alios_angry1 at enterr1
    # show angry alios  as alios di kanan
    al "Berhenti menangis, Cherry! Duduklah dan rawat lukamu"
    r  "Biar kubantu"


    #show BG Perkemahan - Night with fade(3.0)
    scene tenda_gelap with Fade  (1.0,1.0,1.0)
    # show normal  alios  as alios di tengah
    show alios_normal at enter
    al "Hei, Aku lelah. Aku istirahat duluan ya"
    r "Baiklah, giliranku. Aku tidak bisa tidur"
    al "“Bagus, terima kasih"
    r "..."
    "Remil mengangguk kepada alios"
    hide alios_normal
    #hide alios
    "Aku membuka lembar penelitian monster."

    r "(Kertas yang kupungut ini tidak ada ularnya… Sangat tidak berguna)"
    r "(Membahas tentang itu, ular yang sangat besar tadi menguasai daerah sekitar sini, sehingga harusnya tidak ada monster, tetapi kita tidak tahu apa yang akan terjadi karena dia sudah mati)"
    r "(Tapi dengan ini, kita jadi punya petunjuk tentang hilangnya Elena)"

    #show BG Perkemahan - Day with fade(3.0)
    show tenda_terang with Fade (1.0,1.0,1.0)
    #show normal  cherry  as cherrydi tengah
    show cherry_normal at enter
    c "Selamat pagi, Remil! Tidurmu nyenyak?"
    r "Tidak, Aku baru saja tertidur tadi pagi"
    menu:
        "Kemana Alios?":
            jump b1deca2
        "Jam berapa sekarang?":
            jump b1decb2

    return

label b1decb2:
    c "Jam? Kamu melantur soal apa di tengah hari begini?"
    r "Maaf, sepertinya Aku salah ngomong"
    r "Kemana Alios?"
    jump b1deca2

    return

label b1deca2:
    #show sad  cherry  as cherry di tengah
    show cherry_sadpout as cherry_normal
    c "hm, kau tidak menanyakan kabarku?"
    r "?"
    #show bored  cherry  as cherry di tengah
    show cherry_bored as cherry_normal
    c "Alios sedang di sungai mencari ikan"
    r "oke"

    #show BG Dekat sungai - Day with dissolve(1.0)
    scene dekat_sungai with dissolve
    #show angry alios  as alios di tengah
    show alios_angry1 at enter
    a "Hei-hei! Berhenti bergerak dasar makhluk bodoh berinsang!"
    r "Kamu tidak menggunakan pisau untuk menghabisi mereka?"
    al "Mereka berenang di air, bego. Memang kau bisa menusuk mereka?"
    r "Oh"
    r "Kalau gitu, sebaiknya kamu minta Cherry mengumpulkan mereka dengan sihir."
    #show suprise alios  as alios di tengah
    show alios_surprised as alios_angry1
    al "!"
    #show happy alios  as alios di tengah
    show alios_happy as alios_angry1
    al "Hahahaha! Kau benar! Belakangan dia terlihat tidak berguna, Aku lupa"
    r "(Jahat sekali..)"
    r "Kalau begitu, Aku akan coba pergi ke sana dan memeriksa sekitar"


    #show CG Remil di atas tebing dekat air terjun melihat ke sungai (Dekat Air Terjun - Day) with fade(3.0)
    $ persistent.cg_R1_2_remil_airterjun = True
    scene cg_2 with Fade (1.0,1.0,1.0)
    #play sound waterfall
    play sound sfx_waterfall
    r "(Tempat ini mengingatkanku dengan pengalaman buruk..)"
    r "Woah, ikannya banyak sekali di bawah sana"
    r "(Tunggu, Aku merasa pernah melihat mereka)"
    r "..!"
    "aku membalik-balik halamn penelitian monster"
    r "Ikan-ikan itu… monster?"
    "Saat itu, seekor burung terbang melewatiku dan turun sedikit ke sungai tersebut"
    "Salah satu ikan panjang melompat keluar sungai menangkap burung"
    r "(Apa-apaan?)"
    r "Sebaiknya Aku memeriksa tempat lain"


    #scene BG Hutan - Day with fade(0.1)
    scene hutan with fade
    "Entah mengapa monster-monster di sekitar sini semakin banyak, Aku harus mencari jalan keluar dari hutan. Hutan ini tidak bisa dipakai lagi untuk beristirahat"
    r "(!!)"
    r "Di belakang situ, terdapat tempat yang tidak hijau"
    #scene BG Perkemahan - Dawn with dissolve (3.0)
    scene tenda_sore with Dissolve (3.0)
    r "Semuanya dengar, Aku rasa kita bisa mulai bergerak. Aku menemukan jalan keluar dari hutan"
    #show happy chery as cherry di kiri
    show cherry_happy at enterl1
    c "Akhirnya.."
    #show suprise alios as alios di kanan
    show alios_surprised at enterr1
    al "Kau tidak salah lihat kan!?"
    #hide cherry
    hide cherry_happy
    r "Tidak, Aku serius melihatnya"
    #show happy alios as alios di kanan
    show alios_happy as alios_surprised
    al "Baguslah kalau begitu. Pastikan kau pimpin jalannya."
    r "Baiklah, sekarang ayo kemas bawaan kita"

    #scene CHAPTER 3
    #“Pada Semua yang Datang Entah Dari Mana Kemudian Pergi” with fade (3.0)
    scene chp_3 with Fade (1.0,1.0,1.0)
    "Pada Semua yang Datang Entah Dari Mana Kemudian Pergi"
    # scene BG Hutan - Day
    scene hutan with dissolve
    #show serious chery as cherry di left
    show cherry_serius at enterl1
    c "Hey, apa yang akan kalian lakukan setelah keluar dari hutan?"
    r "“Aku ingin menemukan orang untuk mencari petunjuk hilangnya Elena."
    c "Kalau Cherry, ingin beristirahat dan hidup dengan tenang."
    #show normal alios as alios di kanan
    show alios_normal at enterr1
    al "Ada apa kau tiba-tiba, Cherry? Kau bosan?"
    hide cherry_serius
    hide alios_normal
    #hide cherry
    #hide alios
    r "Kurasa tidak ada salahnya bertanya, bukan?"
    #show sad chery as cherry di left
    show cherry_sadpout at enterl1
    c "Habisnya… Cherry tidak tahu apa yang kalian pikirkan!"
    #show normal alios as alios di kanan
    show alios_normal at enterr1
    al "..."
    al "Kau terlalu banyak berpikir, Cherry."
    r "(Cherry…)"
    r "Kau takut, Cherry? Tidak apa, kita semua akan baik-baik saja."


    #show CG Remil, Alios, dan Cherry di jalan setapak alami dari bebatuan di pinggir hutan (Hutan - Day) with fade(3.0)
    $ persistent.cg_R1_3_alios_remil_cherry = True
    scene cg_3 with Fade (1.0,1.0,1.0)
    al "Hey, Remil. Ini begitu menggangguku sejak kemarin.."
    al  "Bagaimana kalau kita bertarung?"
    r "(?)"
    r "Apa tadi kepalamu terbentur di suatu tempat?"
    al "Baiklah, ku anggap itu jawabanmu."
    " Alios memegang pedang besarnya yang dia dapatkan dari membunuh ular"
    #play sound greatsword swing
    play sound sfx_greatsword
    r "(Aku rasa aku akan lari)"
    r "Cherry, tunggu di sana!"
    c "Ap- Hey! Tunggu!"
    c  "Cherry benci kalian, dasar maniak!"
    al "Sini kau, jangan kabur!"
    r "Hentikan, bego. Jangan mentang-mentang semenjak dapat senjata baru lalu mengetesnya denganku!"
    al "Kau lucu. Sini lawan Aku dengan benar!"
    r "(Kamu gila..)"


    #scene BG Lembah - Day with fade(1.0)
    scene lembah_day with fade
    r "Monster!” Aku terhenti di depan lembah. "
    show alios_smirk at enter
    #show smirk alios as alios di tengah
    al "Akhirnya kau berhenti juga!” kata Alios"
    r "Hah- Kamu mengejarku sampai sini? Dengan pedang itu?"
    "Alios melihat kerumunan monster di depan dan dari samping."
    #show normal alios as alios di tengah
    show alios_normal as alios_smirk
    al "Namun, kurasa ini bukan saatnya untuk itu."
    r "Ya."
    hide alios_smirk
    #hide alios
    "Selama beberapa menit, monster-monster turun dari tebing dan terus bertambah jumlahnya di lembah."

    r "(Monster-monster ini tidak ada habisnya..)"
    #show angry alios as alios di tengah
    show alios_angry3 at enter
    al "Sepertinya Aku terkepung."
    r "Kamu kelelahan?"
    al"Tidak. Aku hanya kesulitan menangkis semua serangan proyektill mereka."
    #show angry alios as alios di tengah
    show alios_angry1 as alios_angry3
    al "Mereka monster yang pengecut."
    "Ini memang sulit… apalagi dia belum terbiasa dengan pedang barunya"

    r "Bertahanlah!"
    show alios_normal as alios_angry3
    #show normal alios as alios di tengah
    al "Kau bicara dengan siapa?"
    r "(Nih orang masih aja..)"
    #hide alios.
    hide alios_angry3
    n  "Heeey!"
    r "Jeffrey?!"
    #show normal cherry  as cherry di kiri
    show cherry_normal at enterl1
    c "Cherry membawa teman-teman, Alios, Remil!"
    #show normal elena as elena di kanan
    show elena_normal at enterr1
    e "..."
    r "(Elena juga ada!)"
    r  "!"
    #hide cherry
    hide elena_normal
    hide cherry_normal
    #hide elena
    "Aku merasakan aura bahaya."

    #play sound Sword blocking/ parrying a magic
    play sound sfx_magicblock
    #show normal alios  as alios di tengah
    show alios_normal at enter
    al "Jangan mengalihkan fokusmu, jangan mati."
    "Alios menghalau proyektil monster"
    r "Terima kasih!"
    hide alios_normal
    #hide alios
    #show seriousl elena as elena di kanan
    show elena_angry at enterr1
    e "Kami datang membantu."
    #show normal alios  as alios di kiri
    show alios_normal at enterl1
    al "Jadi, siapa orang yang kau bawa?"
    #hide elena
    hide elena_angry
    #show normal jeffrey  as jeffrey di kanan
    show jeffrey_normal at enterr1
    j "Perkenalkan, ini adalah dokter kita, Kai!"
    #show hapy kai  as kai di tengah
    show kai_smile at enter
    k "Halo kalian! Namaku Kai."
    #hide alios
    hide alios_normal
    hide jeffrey_normal
    #hide jeffrey
    r "Ah- Halo."
    k "Halo untukmu, Remil. Aku sudah dengar tentangmu. Kamu hebat."
    r "Ah, iya-"
    #hide kai
    hide kai_smile
    #play sound  Bullet whizzing/ whooshing
    play sound sfx_bulletwhizzling
    "Remi kemudian menghindar karena ditembaki proyektil dari atas."

    r "(Monster-monster ini tidak bisa tunggu orang selesai bicara ya.)"
    r "Baiklah, kita perkenalkan diri nanti, Aku harus mengurus mereka."
    #show laugh kai  as kai di tengah
    show kai_laugh at enter
    k "Hahaha- baiklah sana!"
    r "(Nih orang nyebelin.)"
    #show serious kai  as kai di tengah
    show kai_normal as kai_laugh
    k "Aku juga sudah dengar tentangmu, Alios. Kamu menghabisi manusia, ya?"
    #hide kai
    hide kai_laugh
    "Kai mengarahkan tongkatnya ke samping muka Alios."

    #show angry alios as alios di kiri
    show alios_angry1 at enterl1
    al "Jauhkan tongkatmu, apa kau tahu bayaran untuk mengganggu pertarunganku?"
    #show serious kai  as kai di kanan
    show kai_normal at enterr1
    k "Jangan lakukan lagi!"
    #show suprise alios as alios di kiri
    show alios_surprised as alios_angry1
    al "!"
    #show normal alios as alios di kiri
    show alios_normal as alios_angry1
    al "Baiklah, tetapi jangan mencoba mengaturku."
    #hide kai
    hide kai_normal
    hide alios_angry1
    #hide alios
    "Di saat itu, bantuan teman-teman sangat berarti hingga kami yakin pertarungan ini bisa berakhir dengan cepat."

    #scene BG Lembah - Day with dissolve(1.0)
    scene lembah_day with fade
    r "Huf-huf."
    show jeffrey_surprisedd at enterl1
    #show suprise jeffrey  as jeffrey di kiri
    j "Oh- Elena, kau terlihat tidak enak badan, kamu baik-baik saja?"
    #show nervous elena  as elena di kanan
    show elena_nervous at enterr1
    e "Ya, tetapi Aku tidak bisa terbiasa dengan monster-monster ini."
    #show laugh jeffrey  as jeffrey di kiri
    show jeffrey_laugh as jeffrey_surprisedd
    j  "Hahaha"
    #hide elena
    hide elena_nervous
    #show normal jeffrey  as jeffrey di kiri
    show jeffrey_normal as jeffrey_surprisedd
    j " Kalau kalian? Apa kalian baik-baik saja?"
    r "Hanya butuh istirahat."
    #show normal alios as alios di kanan
    show alios_normal at enterr1
    al "Aku bisa lanjut.."
    r "(Orang ini gak bisa capek ya?)"
    #show normakai  as kai di tengah
    show kai_normal at enter
    k "Baiklah, mengingat kalian ‘semua’ sudah lelah. Sebaiknya kita beristirahat di sekitar sini. Ikuti Aku."
    #show angry alios as alios di kanan
    show alios_angry2 as alios_normal
    al "Tunggu!"

    #hide jeffrey

    al "Bagaimana kita bisa percaya pada kau? Aku mau Jeffrey yang pimpin jalannya."
    #show normal jeffrey  as jeffrey di kiri

    j "Maaf, Bos. Jujur saja, anak ini lebih tahu jalan dibanding Aku."
    #show normal kai  as kai di tengah
    k "“Yeah."
    #show angry alios as alios di kanan
    al "Ck. Awas saja kau kalau melakukan sesuatu yang mencurigakan."
    #show laugh kai  as kai di tengah
    k "Hahaha."
    hide jeffrey_surprisedd
    hide kai_normal
    hide alios_normal
    #hide kai
    #hide jeffrey
    #hide alios
    pause 2.0
    #show happy kai  as kai di tengah
    show kai_smile at enter
    k "Nah bocah-bocah! Kalian harus pakai nih, ‘cairan’."
    #show item botoh tanah liat
    show botol_tanah_liat
    pause 2.0
    hide botol_tanah_liat
    #hide item botol tanah liat
    r"(Cairan?)"
    #show suprise  alios as alios di kanan
    show alios_surprised at enterr1
    al "Ini! Kau yang membuatnya!?"
    #show normal kai  as kai di tengah
    show kai_normal as kai_smile
    k "Benar. Kamu tahu sesuatu?"
    #show happy alios as alios di kanan
    show alios_happy as alios_surprised
    al "Aku melihatnya cukup banyak di hutan. Itu benda yang berguna sekali!"
    #show seriousl kai  as kai di tengah

    k "Kamu mengambil itu?! Itu barang yang berbahaya, anak bego."
    r "Lalu Anda memberi kami ini?"
    #hide alios
    hide alios_surprised
    k "Dua itu benda yang berbeda."
    r "Bagaimana aku bisa yakin denganmu?"
    #show normal elena  as elena di kiri
    show elena_normal at enterl1
    e "Tenanglah, Remil. Kamu bisa percaya dengannya."
    e "Dia sudah menyelamatkanku."
    r "..."
    "Remil membuka tutup botol tanah liat"
    #hide elena
    hide elena_normal
    hide kai_smile
    #hide kai
    #show normal  alios as alios di kanan
    show alios_normal at enterr1
    al "Hei, Kai. Bagaimana cara memakai cairan ini, diminum?"
    #show normal kai  as kai di kiri
    show kai_normal at enterl1
    k "Lebih baik dioleskan atau disiram, untuk diminum sangat tidak disarankan. Meskipun pada dasarnya itu hanyalah cairan semut."
    r "(Hampir saja, kukira diminum)"
    al "Oke."
    #hide kai
    hide alios_normal
    hide kai_normal
    #hide alios
    "Setelah mengoleskan tangan dan wajah dengan ‘cairan’’, kami bergerak mengikuti Kai, orang yang menganggap dirinya dokter."

    #scene BG Lembah - Day with dissolve(1.0)
    scene lembah_day with dissolve
    r "Jadi, Anda datang dari mana? Anda terlihat tahu banyak hal."
    #show normal kai  as kai di tengah
    show kai_normal at enter
    k "Kamu tanya padaku? Aku sudah beberapa tahun tinggal di tempat ini."
    #show happyl kai  as kai di tengah
    show kai_smile as kai_normal
    k "Aku kebetulan di sini ingin membantu kalian karena Aku sudah bertemu anak-anak ini saat di desa."
    r "(Anak?)"
    #show normal  alios as alios di kanan
    show alios_normal at enterr1
    al "Kau tidak terlihat seperti orang yang baik."
    #show normal  jeffrey as jeffrey di kiri
    show jeffrey_normal at enterl1
    j "Benarkah? Dia ramah untukku.” balas Jeffrey"
    al "Dia hanya ramah karena kau menjilatinya, Jeffrey."
    r "..."
    hide jeffrey_normal
    hide alios_normal
    hide kai_normal
    #hide alios
    #hide jeffrey
    #hide kai
    #show serious kai  as kai di tengah
    show kai_normal at enter
    k "Aku tertarik dengan kalian, bocah yang seolah datang entah dari mana."
    r "(Entah dari mana?)"
    hide kai_normal
    #hide kai
    "Semua orang terlihat diam, apa mereka sendiri tidak sadar?"

    r "Baiklah, lupakan masalah seriusnya. Kita harus membangun perkemahan, benar?"
    #show normal  jeffrey as jeffrey di kiri
    show jeffrey_normal at enterl1
    j "Oh, benar."
    r ".. Apa Anda bisa membangun punyamu sendiri, Kai. Kami tidak punya cukup bahan di sekitar sini."
    #show normal  kai as kai di kanan
    show kai_normal at enterr1
    k "Oh tidak apa, Aku tidak terlalu menginginkannya."
    hide jeffrey_normal
    hide kai_normal


    #CHAPTER 4
    scene chp_4 with Dissolve (3.0)
    " Ketenangan yang Menakutkan Sebelum Badai"
    #“Ketenangan yang Menakutkan Sebelum Badai” with disolve(3.0)
    #scene BG Kantin - Night with dissolve(3.0)
    scene canteen_night2 with Dissolve (3.0)
    #show happy jeffrey as jeffrey di kiri
    show jeffrey_happy at enterl1
    j "Selamat datang, Kai. Ini pesta penyambutan untukmu!"
    j "Dan untuk reuni kita!"
    #show happy alios as alios di kanan
    show alios_happy at enterr1
    al "Kau benar."
    #hide jeffrey
    hide jeffrey_happy
    r "(Tumben sekali dia terlihat patuh, biasanya sombong banget)"
    r "Aku lelah."
    #show normal alios as alios di kanan
    show alios_normal as alios_happy
    al "Ya, aku juga."
    al "Jadi, bagaimana kalian bisa berkumpul dan menemukan Elena?"
    #show nervous elena as elena di kiri
    show elena_nervous at enterl1
    e "Saat itu, Aku-"
    r "(Elena…)"
    #hide elna
    hide elena_nervous
    hide alios_happy
    #hide alios
    #show serious  kai as kai di tengah
    show kai_normal at enter
    k "Jadi begini, Aku menemukan perempuan ini saat di desa yang secara mendadak dikuasai oleh monster."
    k "Saat itu, Aku beberapa hari berjalan ke desa dari tanah di barat. Jadi, dasarnya, Aku adalah orang lewat."
    r "(Kosakatanya ituloh.)"
    #show normal alios as alios di kanan
    show alios_normal at enterr1
    al "Lalu dari sana kau menyelamatkan Elena dan membawa Jeffrey ke desa?"
    k "Benar, lalu kami tinggal di desa. Beberapa hari setelahnya, kami mengikuti suara teriak perempuan dari kejauhan dan mengikutinya sampai sini."
    hide alios_normal
    hide kai_normal
    #hide alios
    #hide kai
    "Aku merasa ini belum menjelaskan semuanya."
    r "Elena, kenapa kamu menghilang? Tidak mungkin tidak ada dari kita yang sadar saat kamu menghilang."
    show elena_angry at enter
    #show serious elena as elena di tengah
    e "Jadi, saat itu."
    e "Aku sedang pergi ke sungai untuk mengisi air di pagi hari. Lalu, ternyata Aku diincar oleh monster dan kemudian dibawa sampai ke desa."
    #show suprise jeffrey as jeffrey di kiri
    show jeffrey_surprisedd at enterl1
    j "Jadi kamu tidak diculik orang?"
    #show happy jeffrey as jeffrey di kiri
    show jeffrey_happy as jeffrey_surprisedd
    j "Itu sungguh melegakan!"
    r "Bagian mananya?"
    show alios_smirk at enterr1
    #show smirk alios as alios di kanan
    al "“Lupakan saja dia, tolong lanjutkan."
    #hide alios
    hide alios_smirk
    hide jeffrey_surprisedd
    #hide jeffrey
    #show serious elena as elena di tengah
    show elena_angry at enter
    e "Jadi, di desa, Aku melihat beruang besar yang menggunakan sihir untuk mengikatku. Dia terlihat seperti pemimpinnya dan jauh berbeda dengan monster yang kita biasa temui."
    e "Keesokan paginya, Aku terbangun di dalam kamar yang sejuk dan sadar kalau Aku telah diselamatkan oleh Kai."
    #hide elena
    hide elena_angry
    "Ceritanya lompat sangat jauh jadi tidak masuk akal."

    r "Bagaimana caranya kamu menyelamatkan Elena, Kai?"
    #show serious kai as kai di tengah
    show kai_normal at enter
    k "Malam itu, Aku pergi menyelamatkannya dengan menidurkan semua monster dan mengangkut mereka pergi."
    r "Bagaimana, tepatnya?"
    #show happy kai as kai di tengah
    show kai_smile as kai_normal
    k "Dengan sihir, kuterbangkan semuanya."
    #show happy alios as alios di kanan
    show alios_happy at enterr1
    al "Hebat! Kau pasti orang yang kuat. Tidak seperti pengguna sihir kita satu ini."
    r "(Jahat sekali…)"
    #show angry cherry as cherry di kiri
    show cherry_angry at enterl1
    c "Hei!"
    r "..."
    hide cherry_angry
    hide alios_happy
    hide kai_normal
    #hide cherry
    #hide alios
    #hide kai
    #show serious kai as kai di tengah
    show kai_normal at enter
    k "Ah maaf, kawan. Kurasa ini saatnya untuk kalian beristirahat. Aku akan berada di belakang sana kalau kamu butuh Aku."
    hide kai_normal
    #hide kai
    r "Permisi, Aku akan ikuti Kai."

    #scene BG Perkemahan - Night with fade(1.0)
    scene tenda_gelap with fade
    #show normal alios as alios di kiri
    show alios_normal at enterl1
    al "Cherry."
    show cherry_normal at enterr1
    #show normal cherry as cherry di kanan
    c "Ya?"
    al "Tentang yang kau katakan sebelumnya. Aku juga takut sepertimu."
    #show serious cherry as cherry di kanan
    show cherry_serius as cherry_normal
    c "..."
    c "Ada apa tiba-tiba, Alios? Kau bosan?"
    #show happy  alios as alios di kiri
    show alios_happy as alios_normal
    al "Hahaha! Ya!"
    #show normal cherry as cherry di kanan
    show cherry_normal as cherry_normal
    c "..."
    #show normal  alios as alios di kiri
    show alios_normal as alios_normal
    al "Kau mau tahu apa? Aku paling takut saat Remil mulai membalikkan taringnya padaku."
    al "Dia sangat berpotensi, Aku ingin dia jadi tangan kananku sebelum dia bertemu lebih banyak orang."
    #show normal cherry as cherry di kanan
    show cherry_normal as cherry_normal
    c "Jadi itu yang kamu pikirkan.."
    hide cherry_normal
    hide alios_normal
    #hide cherry
    #hide alios
    #show normal jeffrey as jeffrey di kanan
    show jeffrey_normal at enterr1
    j "Alios terlihat tidak biasa, huh?"
    #show serious alios as alios di kiri'
    show alios_serious at enterl1
    al "Jeffrey!"
    #show supprise jeffrey as jeffrey di kanan
    show jeffrey_surprisedd as jeffrey_normal
    j "Hah! Ya?"
    #show normal alios as alios di kiri
    show alios_normal as alios_serious
    al "Bagaimana kabarmu? Kau benar-benar membantu di sana."
    #show happy jeffrey as jeffrey di kanan
    show jeffrey_happy as jeffrey_normal
    j "Yah, Aku baik! Dan Elena juga."
    #show nervous elena as elena di tengah
    show elena_nervous at enter
    e "Ya."
    al".. Bagus."
    hide elena_nervous
    hide jeffrey_normal
    hide alios_serious
    #hide elena
    #hide jeffrey
    #hide alios
    #show normal alios as alios di kiri
    show alios_normal at enterl1
    al "Jadi, apa yang dilakukan Remil di sana?"
    #show normal jeffrey as jeffrey di kanan
    show jeffrey_normal at enterr1
    j "Kurasa dia ingin berbicara dengan paman jadi-jadian itu."
    #show normal cherry as cherry di tengah
    show cherry_normal at enter
    c "Paman itu mencurigakan."
    j "..."
    #hide cherry
    hide cherry_normal
    al "Lalu, kemana orang yang pergi bersamamu?"
    j "Oh, iya. Dia menghilang kemana ya?"
    j "Dia sebenarnya ikut dengan kami, tapi sepertinya dia tidak ada semenjak pertarungan di lembah."
    #show sad alios as alios di kiri
    show alios_sad as alios_normal
    al "Kurasa Aku belum cukup meminta maaf padanya."
    j "Lupakan saja, Bos. Dia terlihat sudah baik-baik saja bersamaku."
    hide alios_normal


    #scene CG Remil dan Kai berbicara di lembah (Lembah - Night) with fade(3.0)
    $ persistent.cg_R1_4_remil_kai = True
    scene cg_4 with Fade (1.0,1.0,1.0)
    r "Aku tahu Anda berbohong dari tadi."
    k "Hmm?"
    k "Kamu mengikutiku, Remil? Ada apa?"
    r "Katakan sejujurnya. Anda tidak mungkin hanya orang lewat biasa kalau bisa menidurkan dan menghempas kerumunan beruang. Aku yakin Anda pernah melihat kertas ini."
    k "Ho?"
    k "Kamu menemukan itu di gubuk lamaku? Apakah itu berguna?"
    r "Lumayan- Tunggu, jadi kau yang menulisnya!"
    k "Ya."
    r "..."
    r "Kalau begitu, apa Anda juga yang menculik Elena?"
    k "Tidak, Aku jujur tentang menemukannya. Tetapi, dia diculik dan dibawa ke hutan karena keinginannya sendiri. Sepertinya dia berencana membawa beruang ke perkemahanmu."
    r "Apa?!"
    k "Aku katakan jujur lagi, Elena, temanmu merencanakan banyak hal di belakang kalian. Namun, dia sudah baik-baik saja karena Aku merawatnya di desaku."
    r "(Desaku?)"
    r "Kau sudah berbohong dari awal, rupanya."
    "Orang ini sangat tidak bisa dipercaya.."

    k "Lalu, apa kamu tidak penasaran siapa sebenarnya Aku?"
    r "Anda adalah.. Dokter di desa, kan?"
    k "Kurang tepat, Aku adalah Kai, **** di dunia ini."
    r "Tunggu, apa yang Anda katakan?"
    k "***** ini merupakan ***** yang ku *****."
    r "Ugh- Maaf Aku tidak mendengarmu.” Pandanganku mulai kabur"


    #scene CG Remil dan Kai berbicara di lembah (Lembah - Night) with fade(1.0)
    #$ persistent.cg_R1_4_remil_kai = True
    scene cg_4 with Fade (0.5,1.0,0.5)
    r "..."
    rg "Ah, lama tidak berjumpa, wahai rekanku-"
    k "Kau!"
    rg "Atau harus kubilang, data teman lamaku, Kai!"
    k "Gordon!"
    rg "Kukukuku, ini menarik. Aku bisa berbincang denganmu. Aku tidak akan pernah menduga kamu akan membuat desa dan segala macamnya di belakang sana. Kamu bahkan menghalangi tempat itu."
    k "Kau akhirnya keluar! Aku telah lama berusaha menggali core makhluk hidup yang bisa menghubungkanku dengan sistem."
    rg "Lalu apa? Kamu kira bisa meretas sistem ini dari dalam?"
    rg "Kau hanya beruntung! Pada dasarnya, memang Aku tidak begitu peduli dengan satu dua monster yang mati, dan Aku juga beruntung kamu tidak menemukan bonekaku yang berkeliaran."
    k "Huh?"
    rg "Kukuku, tidurlah, Kai. Aku akan memulai urusan kita setelah anak-anak bangun di pagi hari."

    #scene CG Remil dan Kai berbicara di lembah (Lembah - Night) with dissolve(1.0)
    scene cg_4 with Fade (0.5,1.0,0.5)
    r "Ugh!"
    k "Kamu kembali, anak muda!"
    r ".. Apa yang terjadi?"
    k  "Tidak ada, sebaiknya kita kembali dan tidur."



    #CHAPTER 5
    scene chp_5 with Fade (1.0,1.0,1.0)
    "Kebencian seperti Meminum Racun, Namun Berharap Musuhmu Terbunuh"
    #“Kebencian seperti Meminum Racun, Namun Berharap Musuhmu Terbunuh” with fade(3.0)
    #scene BG Perkemahan - Day with fade(3.0)
    scene tenda_terang with Dissolve (3.0)
    #show happy jeffrey as jeffrey di tengah
    show jeffrey_happy at enter
    j "Halo, Remil. Tidurmu nyenyak?"
    r "Tidak juga.."
    show jeffrey_normal as jeffrey_happy
    #show normal jeffrey as jeffrey di tengah
    j "Ngomong-ngomong, kita sudah berencana kembali ke desa pagi ini. Sebaiknya kamu berkemas."
    r "Baiklah."


    #scene BG Lembah - Day with dissolve (1.0)
    scene lembah_day with dissolve
    r "Monster! Dan dalam jumlah yang banyak sekali."
    "b “HAHAHAHAHHAA- AKU KEMBALI, ALIOS!"
    #show suprise alios as alios di tengah
    show alios_surprised at enter
    al "Kau!"
    #show angry alios as alios di tengah
    show alios_angry as alios_surprise
    al "Aku tahu kau sampah, tetapi kau jatuh sedalam ini dan sampai melibatkan semuanya!"
    b "AKU TIDAK PEDULI LAGI. MATI KALIAN!"
    #show suprise jeffrey as jeffrey di kiri
    show jeffrey_surprisedd at enterl1
    j "Waduh, beruangnya banyak banget."
    #show normal jeffrey as jeffrey di kiri
    show jeffrey_normal as jeffrey_surprisedd
    j "Tunggu, kemana Remil?"
    #show serious elena as elena di kanan
    show elena_angry at enterr1
    e "!"
    #show suprise elena as elena di kanan
    show elena_surprise as elena_angry
    e "Di atas sana, Remil?"
    #show angry jeffrey as jeffrey di kiri
    show jeffrey_angry as jeffrey_surprised
    j "Remil, cepat ke sini! Di sini kita kesulitan."
    rg  "Kaaamu siaaapa?"
    j "?"
    al "Remil! Berhenti bercanda, kita semua sedang dihadang monster!"
    # hide alios
    hide alios_surprise
    #hide elena
    hide elena_angry
    #hide jeffrey
    hide jeffrey_surprised
    "Remil menerjang ke arah Alios, tetapi dihadang oleh Elena."

    rg "Hmmmmmmmm?"
    #show angry cherry as cherry di kanan
    show cherry_angry at enterr1
    c "Remil, kamu sudah gila! Lepaskan kak Elena!"
    "Cherrymenciptakan banyak bola api lalu ditembakkan ke arah Remil namun terus-menerus ditangkis"
    c "Hah- Lepaskan.."
    "Cherry kehabisan tenaganya lalu pingsan."
    #hide cherry
    hide cherry_anggry

    #With fade 1
    #scene BG Lembah - Day with fade(1.0)
    scene lembah_day with fade
    #show angry kai as kai di tengah
    show kai_normal at enter
    k "Berhenti di sana, kalian!"
    hide kai_normal
    "Saat itu, Kai bertukar posisi dengan Elena dan membuat lengan bawah Remil patah."

    #show serious kai as kai di tengah
    show kai_normal at enter
    k "Kalian, tolong urus beruangnya dan jaga anak perempuan di sana."
    #show angry alios as alios di kanan
    show alios_angry1 at enterr1  # 1-3, not sure.
    al "Ck, darimana saja kau?"
    k "Maafkan Aku."
    #hide kai
    hide kai_normal
    #show normal alios as alios di kanan
    show alios_normal as alios_angry1
    al "Baiklah. Jeffrey! Pindahkan Cherry!"
    #show normal jeffrey as jeffrey di kiri
    show jeffrey_normal at enterl1
    j ".. Bagaimana dengan Elena?"
    #show sad alios as alios di kanan
    show alios_sad as alios_angry1
    al "Keadaannya sudah tidak bagus. Dia mati."
    #show sad jeffrey as jeffrey di kiri
    show jeffrey_sad as jeffrey_normal
    j "..."
    #show serious jjeffrey as jeffrey di kiri
    show jeffrey_serious as jeffrey_normal
    j "Baiklah, Aku akan menembak dari belakang."
    #hide jeffrey
    hide jeffrey_normal
    #show normal alios as alios di kanan
    al "Dan kau bocah putih, kita bicarakan masalah ini nanti!"
    show alios_normal as alios_angry1
    #show normal kai as kai di kiri
    show kai_normal at enterl1
    k "Bocah.."
    #hide kai
    hide kai_normal
    hide alios_angry1
    #hide alios
    "Kai melempar Remil dengan sihirnya lalu membuatnya lumpuh sementara."

    #show serious kai as kai di tengah
    show kai_normal at enter
    k "Remil! Sadarlah!"
    #play soind  Earthquake rumbling
    play sound sfx_earthquake
    rg "Hmmmm?"
    #show angry  kai as kai di tengah
    k "Haaaaa!” Kai berusaha untuk menekan Remil dengan gravitasi, namun Remil tetap bisa melawan"
    #hide kai
    hide kai_normal
    "Kai pun mencoba sihir pelumpuh, pembuat tidur, penekan darah, namun tidak bekerja."


    #scene BG Lembah - Day with dissolve(1.0)
    scene lembah_day with dissolve
    #show angry alios as alios di kanan
    show alios_angry1 at enterr1
    al "Jeffrey!"
    al "Jeffrey, kuatkan dirimu! Tembakkan panahmu dengan benar!"
    #show angry jeffrey as jeffrey di kiri
    show jeffrey_angry1 at enterl1
    j "Aku tahu!"
    #show normal alios as alios di kanan
    show alios_normal as alios_angry1
    al "Saat kuberi tanda, kau tembaklah perutnya. Aku akan tangkis sihirnya!"
    #hide jeffrey
    hide jeffrey_angry1
    hide alios_angry1
    #hide alios
    "Alios kemudian menerjang ke arah beruang dan memanfaatkan pedangnya yang besar untuk menerobos ke depan. Lalu, dia menghantam beruang besar dengan sisi pedangnya."
    #show normal alios as alios di kiri
    show alios_normal at enterl1
    al "Sekarang!"

    #play sound  Bow drawing

    #show serious jeffrey as jeffrey di kanan
    show jeffrey_serious at enterr1
    j "!"
    "Jeffrey kemudian menembak panah yang telah dilumuri racun ke perut beruang."
    #hide jeffrey
    hide jeffrey_serious
    #show angry alios as alios di kiri
    show alios_angry2 as alios_normal
    al "Habis kau!” Menebas secara diagonal ke arah bahu beruang"
    #play sound  Flesh tearing
    play sound sfx_fleshtearing
    #hide alios
    hide alios_normal
    #show happy jeffrey as jeffrey di kanan
    show jeffrey_happy at enterr1
    j "Bagus, Alios! Rajanya sudah dikalahkan."
    #show normal alios as alios di kiri
    show alios_normal at enterl1
    al "Belum, masih ada keroco lainnya."
    #show serious jeffrey as jeffrey di kanan
    show jeffrey_serious as jeffrey_happy
    j "..."
    #hide alios
    hide alios_nomal
    #hide jeffrey
    hide jeffrey_happy
    "Alios kemudian menerjang ke depan dan melawan beruang-beruang di depannya dan Jeffrey menjaganya dari belakang."

    # scene BG Lembah - Day with dissolve(1.0)
    scene lembah_day
    show kai_normal at enter
    #show serious kai as kai di tengah

    k "Sadarlah!!"
    "Kai yang mulai kehabisan sebagian mananya berteriak kepada Remil"
    rg " …"
    rg  "Hentikan sajalah, Kai."
    #show angry kai as kai di tengah
    k "Gordon!"
    rg "Kamu kira bisa melawanku? Di duniaku?"
    k "Kukira kita hanya akan bicara!"
    rg "Kamu pikir Aku akan dengan senang hati melakukannya?"
    k "Ck."
    "Kai lalu mundur karena sihirnya tidak bekerja pada Remil."
    #hide kai
    hide kai_normal
    #show suprise alios as alios di kiri
    show alios_surprised at enterl1
    al "!"
    #show normal alios as alios di kiri
    show alios_normal as alios_surprised
    al "Bocah putih! Bawa Cherry, kau pasti sudah kehabisan mana!"
    rg "Haha, Kai! Kamu lari?"
    #hide alios
    hide alios_surprised
    "Kai mendekat ke arah Cherry lalu menghilang, meninggalkan Remil yang dikendalikan di sana. Lalu, Alios berlari menghampiri Remil."

    #show angry alios as alios di tengah
    show alios_angry3 at enter
    al "REMIL! Sadarlah!"
    "Alios mengayunkan pedang besarnya ke Remil"
    #play sound Heavy sword swinging
    play sound sfx_greatsword
    #hide alios.
    hide alios_angry3
    "Lalu, Remil menghindar."

    #show angry alios as alios di tengah
    show alios_angry2 at enter
    al "Kau! Ini bukan saatnya bercanda!"
    rg  "Hihihi. Bercanda?” Remil kemudian melihat ke arah lain"
    #hide alios
    hide alios_angry2
    rg "Akan kutunjukkan maksudnya bercanda."
    #show normal alios as alios di kiri
    show alios_normal  at enterl1
    al "Jeffrey! Merunduk!"
    show jeffrey_surprisedd at enter
    #show suprise jeffrey as jeffrey di tengah
    j "Ap-"
    #hide alios
    hide alios_normal
    #hide jeffrey
    hide jeffrey_surprisedd
    "Kepalanya terpenggal."


    #scene BG Lembah - Day with fade(1.0)
    scene lembah_day with fade
    #show angry alios as alios di tengah
    show alios_angry1 at enter
    al "Kaaaaaau!"
    "Alios mengayunkan pedang besarnya."
    #hide alios.
    hide alios_angry1
    "Remil menangkap pedang tersebut, lalu dihancurkan."
    #play sound Sword breaking
    play sound sfx_sword

    #show angry alios as alios di tengah
    show alios_angry1 at enter
    al "Ck, pedang baruku sangat tidak berguna."
    al "Kalau begitu Aku gunakan kapak lamaku, khusus untukmu!"
    "Lalu, Alios mengayunkan kapaknya, namun perutnya ditendang oleh Remil dan genggamannya pada kapak terlepas."
    #play sound Object dropping on sand
    play sound sfx_sanddrop
    #hide alios
    hide alios_angry1
    pause 1.5
    #play sound  Body falling
    play sound sfx_bodydrop
    "Alios terkapar di tanah."


    #play music  sad music loop
    play music sad_song
    show alios_smirk at enter
    #show smirk alios as alios di tengah
    al "Hahaha, jadi kau masih dendam tentang Aku, lalu kau merencanakan semua ini?"

    rg "Berhenti berbicara, bocah."
    #show sad alios as alios di tengah
    show alios_sad as alios_smirk
    al "Kau pasti sangat membenciku, huh?"
    "Kemudian, Remil menghancurkan rusuk Alios dengan pijakannya."
    #play sound  Bone cracking
    play sound sfx_bonecrack
    #show suprise alios as alios di tengah'
    show alios_surprised as alios_smirk
    al "!"
    "Alios batuk darah."
    #show sad alios as alios di tengah
    show alios_sad as alios_smirk
    al "Harusnya kita adalah keluarga. Aku merasa dikhianati..” Alios kehilangan tenaganya untuk bicara"
    #hide alios.
    hide alios_smirk

    # scene BG Lembah - Day with dissolve(1.0)
    scene lembah_day with dissolve
    n "Gordon! Kau sudah keterlaluan!!"
    n "Dengan sisa manaku, kau akan kubakar! Gordooon!"
    "Dari atas, lembah tersebut tertutupi sinar dan semua beruang terbakar api membara, termasuk Alios yang masih dalam keadaan kritis."

    #show sad alios as alios di tenga
    show alios_sad at enter
    al "Maaf.."
    al ".. Terima kasih."
    rg "..."
    b "HAHAHAHAHAHA- RASAKAN ITU! AKU BERHASIL-"
    b "AAAAAAAAAARGH"
    "Dia terbakar menjadi abu."
    #hide alios
    hide alios_sad
    "Di atas sana, Remil sadar kembali sesaat dan menengadah ke atas. Dia sekilas melihat Kai yang mengangkat tongkatnya dan Cherry yang terkapar."
    " (..!)"
    "Remil kemudian pingsan."


    #scene CG Lembah dan Remil di tengah jalan yang sedang pincang (Lembah - Day) With fade(3.0)
    $ persistent.cg_R1_5_remil_jalan_pincang = True
    scene cg_5 with Fade (1.0,1.0,1.0)
    "Aku terbangun di daratan yang tidak kuketahui."

    r "Dimana ini?"
    r"(Ugh- Kepalaku sakit)"
    r "Lembah ini.."
    r "Halo, apakah ada seseorang?"
    "(Duh, kakiku mati rasa)"
    "Aku menemukan banyak tulang-belulang di arah lembah dan bekas pertarungan."

    r "Tulang.."
    r "(Ugh)"
    r "Halo, seseorang di sana?"
    r "Kapak..?"
    r "(Kenapa kapaknya ada di sini?)"
    r "Benar juga!"
    r "Alios! Cherry! Kalian ke mana?"
    r "(!!)"
    r "Elena! Kamu baik-baik saja?"
    "Aku mencoba membangunkan Elena"
    r  "Hei!"
    r "(Ugh)"
    r "Ayolah, ini tidak lucu, ya kan, Jeffrey."
    r "(Jeffrey..)"
    "Aku berlari dan melihat lebih dekat, dan ternyata itu adalah ‘kepala’ Jeffrey."

    r "Hah- Jeffrey! Elena! Alios!"
    r "AAAAAAAARGHH!"
    #stop music fadeout 1.0
    stop music fadeout 2.0


    # BG Lembah - Day with fade(1.0)
    scene lembah_day with fade
    "Aku teringat, hari itu, Aku ingat pisauku yang berlumuran darah dan menghabisi mereka semua."

    r "Maaf! Maafkan Aku!"
    r "Aku, Aku akan ikut dengan kalian!"
    "Aku menusuk perutku dengan pisau, tetapi hanya meninggalkan rasa sakit."

    r "!!"
    "Aku melihat bagian yang ditusuk lukanya menghilang."
    r "Tunggu, Aku akan coba cari cara lain!"
    r "(Mungkin dari atas?)"
    "Aku ingat, Kai dan Cherry menghilang menjadi partikel."

    "Aku kemudian menangis dan muntah setelah mengingat semua hal yang terjadi tersebut."
    "Aku di sini hanya untuk tidak mengetahui apapun dan ditinggal sendirian di dunia ini."
    "Beberapa minggu kemudian."

    #CHAPTER 6
    scene chp_6 with Dissolve (2.5)
    "Akhir dari Perjalanan Para Pengembara di Dunia Lain"
    #“Akhir dari Perjalanan Para Pengembara di Dunia Lain” with dissolve (3.0)
    # scene BG Hutan with disolve(3.0)
    scene hutan with Dissolve (2.5)
    "Aku mengalahkan banyak monster di perjalanan dengan kekuatan listrik aneh yang kudapatkan setelah pertarungan di lembah hari itu."
    "Beberapa bulan kemudian."

    #BG Padang Gurun - Day with dissolve(3.0)
    scene padang_gurun_day with Dissolve (2.5)
    "Aku telah mengalahkan banyak monster di perjalanan dan Aku mulai terbiasa membunuh dengan tangan kosong."
    "Akan tetapi, kurasa tanganku berkata lain. Rasanya aneh saat mencengkeram sesuatu yang berdenyut."
    "Meski di sini dan di sana banyak monster, Aku sangat jarang bertemu orang lain"

    #BG Desa Kai - Day with fade(1.0)
    scene desa_kai with Dissolve (1.5)
    a "Terima kasih sudah datang membantu, tuan Kai sudah lama tidak kembali, sehingga anda menyelamatkan kami."
    r "“Ya, Aku juga berterima kasih untuk perawatanmu."
    a "Sama-sama."

    #BG Hutan - Day with dissolve(3.0)
    scene hutan with Dissolve (2.5)
    r "(Aku dengar jika kita memutari lembah, ada dataran tinggi yang dijaga monster di sana.)"
    "Aku masih dalam perjalananku mencari alasan untuk hidup. Bahkan, jika itu artinya Aku harus mati."


    #BG Lembah - Daywith dissolve(3.0)
    scene lembah_dusk with Dissolve (2.5)
    r "(Monster di sini memang semakin banyak)"
    "Aku menyadari, Aku tidak pernah memikirkan ini."
    r "(Tetapi, sebenarnya dari mana semua monster ini?)"

    #With fade 3
    #BG Plateau - Dusk with fade (3.0)
    scene plateau with Fade (1.0,1.0,1.0)
    "Aku merasakan atmosfer yang berbeda di hadapanku."
    "Masuk di dalamnya, Aku melihat perkemahan di dalam."

    r "!"
    "Aku hampir menginjak jebakan di dalam."
    #show suprise kai as kai di kanan
    show kai_normal at enterr1
    k "Oh! Hey, Remil!"
    r "Kai.."
    #show normal kai as kai di kanan
    k "Kamu butuh tiga bulan untuk sampai di sini. Apa kepala desa yang memberitahumu?"
    r "Ya. Maaf, Aku-"
    #show happy kai as kai di kanan
    show kai_smile as kai_normal
    k "Tidak apa, kamu pasti telah menderita sangat lama dalam perjalanan yang melelahkan."
    #show sad kai as kai di kanan
    show kai_normal as kai_normal
    k "Tidak, malah. Ini sebenarnya terlalu jahat untuk anak kecil sepertimu."
    "(Anak kecil?)"
    #show normal kai as kai di kanan
    "Sini, datanglah. Kita bisa berbincang sebentar."
    r "..."
    r "Tidak bisa, Aku akan pergi."
    #show happy kai as kai di kanan
    show kai_laugh as kai_normal
    k "Aku ada bakar daging juga."
    r "(...)"
    r "Satu aja deh."
    #hide kai
    hide kai_normal
    "Aku memutuskan untuk duduk bersama Kai di tanah yang luas itu."

    #scene BG Plateau - Dusk with dissolve(1.0)
    scene plateau with dissolve
    #show happy kai as kai di kanan
    show kai_smile at enterr1
    k "Dagingnya enak bukan?"
    r "(Benar, daging apa siih ini)"
    #show laugh kai as kai di kanan
    k "Hahaha!"
    #show happy kai as kai di kanan
    k "Kamu pasti bertanya-tanya, ini adalah paha kambing gunung. Ini bukan sesuatu yang bisa kamu dapatkan bahkan jika kamu menginginkannya."
    r "..."
    "Aku menelan dagingku dan menenggak air."
    r "Jadi, tentang di lembah pada hari itu."
    #show normal kai as kai di kanan
    show kai_normal as kai_smile
    k "Ya?"
    r "Aku hanya ingat sedikit, tentang Alios, tentang Elena, tentang Jeffrey.."
    r "Sebenarnya, apa yang terjadi padaku? Mengapa ini semua terjadi?"
    #show serious kai as kai di kanan
    k "..."
    "Kai berpikir sebentar."
    k "Kamu penasaran bagaimana kamu kehilangan kendali?"
    r "Ya."
    k "Hmm.."
    k "Apa kamu ingat pernah tergigiti sesuatu atau terluka jauh sebelum di lembah?"
    r "Tergigit? Kurasa tidak.."
    #hide kai
    hide kai_smile
    "Tergigit? Aku mencoba mengingat yang pernah kulakukan."

    r "(!!)"
    r "Racun ular!"
    #show suprise kai as kai di kanan
    show kai_normal at enterr1
    k "Ular? Ada hewan seperti itu ya di dunia ini?"
    r "Ada! Kami menemukan satu yang sangat besar!"
    #show serious kai as kai di kanan
    k "Hmm. Jadi itu yang dimaksud oleh ‘dia’."
    r "(Dia?)"
    k "Kemungkinan, itu boneka Gordon."
    r "Siapa, Gordon?"
    k "..."
    "Kai memalingkan pandangannya."
    #show normal kai as kai di kanan
    k "Ayo kita berbicara di belakang."
    r "(?)"
    #hide kai
    hide kai_normal

    #scene BG Plateau - Dusk with dissolve(1.0)
    scene plateau with dissolve
    r "Jadi ada apa?"
    #show serious kai as kai di tengah
    show kai_normal at enter
    k "Aku akan menjelaskan latar belakangku dulu."
    k "Singkatnya, Aku adalah pencipta dunia ini, dan sebenarnya Aku telah lama mati. Kurasa Aku belum mengatakan itu."
    r "(Apa?!)"
    k "Kamu dan teman-temanmu berasal dari luar, kalian adalah tikus yang diamati di dalam sini."
    r ".. Oleh siapa?"
    k "Temanku, atau tepatnya mantan rekanku. Dia disebut Gordon."
    r "Lalu, maksudmu, kita semua juga orang mati di luar sana?"
    #show normal kai as kai di tengah
    k "Tidak. Aku adalah tubuh sisa yang kubuat untuk masuk di dunia ini. Aku hanya salinan dari dunia nyata yang sudah lama mati."
    #show serious kai as kai di tengah
    k "Berbeda denganku, kalian adalah anak-anak yang hidup."
    r "Tunggu- Ini semua tidak masuk akal!"
    r "Ini dunia apa, kenapa Kau bisa menciptakannya?"
    #show laugh kai as kai di tengah
    show kai_laugh as kai_normal
    k "Hahaha-"
    #show happy kai as kai di tengah
    show kai_smile  as kai_normal
    k "Maaf, anak sepertimu tidak akan mengerti."
    r "Lalu, bagaimana cara kita kembali?"
    #show serious kai as kai di tengah
    show kai_normal as kai_normal
    k "..."
    "Kai hanya menatap dengan serius."
    #show normal kai as kai di tengah
    k "Aku juga penasaran."
    r "Jadi kau kira kau bisa diam saja?"
    "Aku mengarahkan belatiku ke Kai, namun tanganku terhenti"
    k "Kalahkan Aku, maka akan kujelaskan semuanya."
    #hide kai.
    hide kai_normal
    "Saat itu, Aku terdorong mundur oleh sihir."
    #play sound Strong wind blowing


    r "Kau pasti bercanda."
    "Aku menerobos ke depan sekuat tenaga, tetapi Aku kembali terdorong mundur."
    "Saat Aku melempar belatiku dan bergerak memutari sekeliling Kai, Aku harus menghindar karena belatiku kembali."
    r "(Bagaimana tepatnya caraku mengalahkan dewa?)"
    r "Haaaaaa!"
    "Aku mengarahkan tinju ke Kai, namun ada dinding tak terlihat yang mematahkan tanganku."
    r "Kai! Aku menyerah!"
    #show suprise kai as kai di tengah
    show kai_normal at enter
    k "!"
    #show laugh kai as kai di tengah
    show kai_laugh as kai_normal
    k "Hahahaha, Kamu anak yang jujur."
    r "(?)"
    #show happy kai as kai di tengah
    show kai_smile as kai_normal
    k "Baiklah, mari kita bicara di luar."
    #show serious kai as kai di tengah
    show kai_normal as kai_normal
    k "Ikuti Aku."
    r "!"
    #hide out
    hide kai_normal
    "Aku melihat Cherry mengintip dari kejauhan."

    #show normal kai as kai di kanan
    show kai_normal at enterr1
    k "Kamu tidak jalan?"
    r "Lupakan saja, tolong setidaknya bawa Cherry pergi."
    #show serious kai as kai di kanan
    k "Cukup. Ikuti Aku."
    r "!"
    "(Lukaku perlahan menutup sendiri.)"
    #hide out.
    hide kai_normal

    #scene BG Plateau - Dusk with dissolve(1.0)
    scene plateau with dissolve
    "Saat itu, Kai menunggu di ujung tebing."
    "Di saat Aku melangkahkan kaki di luar, tanganku menembus jantung Kai."

    r "AAAAH! Tidak!"
    uv "Bagaimana kabarmu, Kai?"
    "Gordon yang berbicara melalui kepala mereka"
    #show suprise kai as kai di kanan
    show kai_normal at enterr1
    k "!"
    uv "Dapat kau. Kau tidak boleh lari karena ini akan jadi menyenangkan. Hihihihi."
    #hide kai
    hide kai_ normal
    r "Kau, Gordon! Orang sinting, Aku tahu semuanya! Lepaskan Aku!"
    uv "Lalu apa? Kamu merasa kamu bisa mengancamku?"
    uv "Aku adalah penyelamatmu!"
    r "Hah? Berhenti berbicara omong kosong!"
    uv "Kamu hanya anak buangan! Kamu kira kamu bisa hidup kalau bukan karena…"
    #show normal kai as kai di kanan
    show kai_normal at enterr1
    k "Sh- Jangan dengarkan dia."
    r "!"
    "Aku didorong kembali ke dalam penghalang."
    #show happy kai as kai di kanan
    show kai_smile as kai_normal
    k "Lakukanlah yang kamu inginkan."
    "Kata Kai dengan sisa tenaganya dan jatuh dari tebing"
    r "Kai!!"
    #hide kai
    hide kai_normal
    "Aku teringat pada Cherry."

    #With fade 1
    #scene BG Plateau - Dusk with fade(1.0)
    scene plateau with fade
    r "Cherry, kamu dimana!"
    uv "..."
    r "Cherry!!"
    show cherry_angry at enter
    #show angry as cherry di tengah
    c "Diam!"
    c "Kamu bohong! Kamu bilang semua akan baik-baik saja."
    "Cherry menembakkan pedang cahaya dan mengores bahu Remil"
    r "Maafkan Aku, Cherry-”"
    #show normal as cherry di tengah
    show cherry_normal as cherry_angry
    c "Cherry sempat percaya padamu! Kamu pikir maaf saja cukup?"
    #show angry as cherry di tengah
    show cherry_angry as cherry_angry
    c "Kamu menghancurkan tulang Alios! Kamu memenggal kepala Jeffrey!"
    r " …"
    #show sad as cherry di tengah
    show cherry_sadpout as cherry_angry
    c "Dan, kamu tidak puas hanya dengan mencekik leher kak Elena!"
    r "Dengarkan Aku!"
    "Aku berusaha mendekat dan menjelaskan semuanya."

    c "Berhenti di sana!"
    "Cherry memunculkan sinar besar dari atasnya."
    #hide cherry
    hide cherry_angry
    "Aku berusaha untuk menghindar, namun bagian kiri tubuhku terpotong habis."
    "Aku terkapar dan Cherry mulai menghampiriku."

    #With fade 3
    #show CG Cherry duduk menangis di samping saat Remil kehilangan sebagian badannya (Plateau - Dusk)
    $ persistent.cg_R1_6_cherry_remil = True
    scene cg_6 with Fade (1.0,1.0,1.0)
    "(Ugh!)"
    #play music  sad music
    play music sad_song
    r "Maafkan Aku, Cherry."
    "Aku mulai kehabisan tenagaku untuk berbicara."
    "(Cherry..)"
    r "Cherry, suatu hari.."
    r "Mari kita bertemu yang lain di luar sana."
    scene plateau with fade
    "Saat barrier tidak lagi melingkupi tubuhku, bahu kiriku tumbuh dan tanganku mencengkeram tangan Cherry."

    r "Hentikan- HENTIKAN! GORDOOOOOOON!"


    #BG Plateau - Dusk with fade(1.0)

    "Di saat itu, badan Cherry terpisah dua atas bawah."
    "Tubuhku kembali utuh dan barrier sudah lenyap, seutuhnya."

    #scene CG Remil berjalan ke ujung tebing di plateau (Plateau - Dusk) wirth dissolve(3.0)
    $ persistent.cg_R1_7_remil = True
    scene remi_cg_end with Dissolve(3.0)
    r "Hahahaha- Akhirnya begini!"
    c "Hentikan- Remil"
    r "GORDON{w=0.1}, HABISI SAJA AKU!"
    r "Kalau kau tidak{w=0.1}, Aku akan melompat!"
    g "Kikikik-"
    "Aku berjalan ke ujung tebing."

    r "3{w=0.3}.{w=0.3}."
    g "KAAHAHAHAHAHAHAH!"
    r "2{w=0.3}.{w=0.3}."
    r " {w=0.3}.{w=0.3}.{w=0.3}."
    r "1{w=0.3}."
    "(Selamat tinggal, semuanya..)"
    "Di bawah sana, Aku melihat badan Kai yang tertusuk oleh batuan."

    "Aku menutup mataku dan berharap ini akan berakhir. Dunia yang penuh penderitaan ini."

    #With fade to black 3s
    scene black with Fade(1.0, 1.0, 1.0)
    "Jumlah karakter hidup tersisa = 0."
    "Catatan: Avatar subjek E{w=0.3} dicekik oleh subjek R yang berada di luar kendali setelah otaknya beresonansi dengan AI"
    "Catatan: Avatar subjek J{w=0.3} dipenggal oleh subjek R yang dikontrol"
    "Catatan: Avatar subjek A{w=0.3} keberadaannya menghilang oleh kekuatan misterius"
    "Catatan: Avatar subjek C{w=0.3} dibelah dua oleh subjek R yang dikontrol"
    "Catatan: Avatar subjek R{w=0.3} meninggal karena tekanan berat psikologis"

    scene end_alternative with Dissolve (3.0)
    "The Alternative Ending"



    return
