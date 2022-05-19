label branch1:
    #CHAPTER 1
    #“Pemimpin dari Kelompok yang Berbahaya” with dissolve(3.0)

    # scene perkemahan dusk with dissolve(3.0)
    #show angry Alios  as alios di kiri
    al "Mengerikan? Kau dan pikiran bodohmu! Orang tidak berguna ini pantas mendapatkannya setelah datang dengan sembrono. Mereka bisa menghabisi kita!"
    # show angry elena as elina di kanan
    e "Bagaimana bisa kamu mengatakan itu! Laki-laki itu juga teman kita, bukan?"
    #hide alios
    #hide elena
    "Kepala monster tersebut bergelinding di tanah setelah ditebas oleh kapak besar Alios. Namun, Alios baru saja menghabisi orang itu."

    #show normal alios as alios di kiri
    al "Daritadi apa yang kau lihat, bocah? Kau tidak senang padaku?"
    r "(Apa-apaan?)"
    r "Sombong sekali kamu dengan wajah pembunuhmu itu?"
    #hide alios
    #show normal jeffry as jeffry di kanan
    j "Tenanglah, kawan. Bos tidak akan melakukan hal yang merugikan kita. Ini pastinya lebih baik, bukan? Dibanding kepala kita yang bergelinding di situ."
    r "(Benar, Aku juga berpikir begitu sekilas… Tunggu, apa yang baru saja kupikirkan!)"
    r "Kau!” Aku mengarahkan belatiku ke Jeffrey"
    j "Baiklah, lupakan masalah seriusnya. Kita harus cepat memotong daging itu"
    #hide jeffry
    "Setelah itu, Aku memutuskan untuk diam agar tidak merusak suasana. Aku percaya bahwa Alios melakukan ini untuk keselamatan kami."
    #dissolve selama 3s

    #scene kantin malam
    #show jeffrey laugh as jeffry di kiri
    j "Hahaha"
    #show jeffrey happy as jeffry di kiri
    j "Anda berlebihan melakukannya, Bos!"
    #show sad alios as alios di kanan
    al "Itu bukan pengalaman yang menyenangkan, tapi terima kasih"
    #hide jeffrey
    #show Alios normal as alios di kanan
    al "Kau tidak masalah bukan? Kalian sendiri yang datang membawa monster seolah-olah ingin menghancurkan tempatku"
    a "Y-Ya"

    #hide alios
    "Dia terlihat seperti menahan amarahnya... aku harus menenangkanya"

    #show normal  jeffry as jeffry di kiri
    J "Hey, Remil, apa yang kamu lakukan dari tadi mengintip ke sana kemari?"
    r  "Tidak ada"
    r "Aku akan pergi membawakan makan malam Elena. Aku khawatir dia masih memikirkan tentang masalah saat sore tadi."
    #show normal cherry di kiri
    c "Memang kamu siapanya? Dasar bodoh"

    #scene perkemahan night with dissolve(1.0)
    r "Maaf, Aku masuk untuk membawakanmu makan malam"
    #show sad elena as elena di kanan
    e "Masuklah"
    r "Apa kamu masih memikirkan itu?"
    e "Ya. Aku masih ingat bagimana Alios menghancurkan kepala anak itu"
    #show confused elena as elena di kanan
    e "sebenarnya, apa yang dia pikir dia lakukan!"
    r "...."
    #show sad elena as elena di kanan
    e "Terima kasih, tolong ditinggalkan saja di sana"
    r " Aku akan berada di tendaku kalau kamu butuh sesuatu, jangan lupa makanlah nanti"
    #hide elena
    "Setelah itu, Aku memutuskan untuk diam agar tidak merusak suasana. Aku percaya bahwa Alios melakukan ini untuk keselamatan kami"

    #scene bg kantin night with dissolve(3.0)
    "Di luar, semua orang berkumpul, kecuali Elena"
    r "Hei, apa yang terjadi? Kemana Elena"
    #show sad cherry as cherry di kiri
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
    c "!!"
    r "Dan, semua ini salahmu, Alios!"
    jump b1deca


label b1deca:
    r "Alios! Apa yang telah kamu lakukan pada Elena!"
    #show angry alios as alios di kanan
    al "Apa maksudmu, bocah? Kau masih tidak senang dengan apa yang terjadi semalam?"
    #hide cherry
    #show normal jeffrey asjeffrey di kiri
    j "Tidak, Bos. Dia hanya.."
    #show normal alios as alios di kanan
    al "Tenang, bukan Aku. Kau bisa camkan kataku"
    #hide jeffrey
    al "Aku tidak akan pernah merugikan diriku sendiri dengan menghilangkan pekerja terbaik kita"
    b "Maaf, Aku ragu dengan katamu"
    #hide alios
    "Raut wajah Alios menatap laki-laki tersebut dengan tidak senang, namun dia tidak mundur"

    #show angry jeffry as jefrey di tengah
    j "Ah tolong tenang, kalian! Berpikirlah dengan jernih dulu."
    r " …"
    #show normal jeffry as jefrey di tengah
    j "Untuk masalah ini, kurang lebih Aku bisa diandalkan karena sering pergi berburu bersamanya. Biar kita pergi mencari jejaknya dulu, ya?"
    "(Bagaimana kita bisa yakin kita bisa menemukan Elena, jika dia masih hidup)"
    #hide jeffrey
    "Jeffrey mendekat dan menepuk pundakku"

    #show normal jeffry as jeffrey di tengah
    j"Aku menemukan tempat yang menarik kemarin, kita akan mulai mencari dari situ"
    #show normal alios as alios di kanan
    al "Baiklah, begini lebih mudah. Aku biarkan kau memimpin, bocah. Kita serahkan jalan ke Jeffrey"
    #show serious cherry as cherry di kiri
    c  "Cherry ikut dengan kalian!"
    r "Baiklah. Kita bergerak selagi masih pagi. Kemas bawaan kalian secepat mungkin sebelum siang!"

    #scene hutan day with dissolve(3.0)
    #show normal alios as alios di kiri
    al "Kemana kau mengarahkanku, Jeffrey?"
    #show normal jeffry as jeffrey di kanan
    j "Tenang saja, Bos- Maksudku, Alios. Lurus dari sini terdapat rahasia yang mendebarkan"
    #hide alios
    j "Dan seharusnya kita sudah sampai"
    "Mereka menemukan sebuah gubuk besar yang dibangun di tengah hutan"
    #hide jeffrey

    #scene gubuk luar day with dissolve(1.0)
    r "ini bukannya gazebo biasa?"
    #show angry jeffry as jeffrey di tengah
    j "Kamu pasti bercanda, gubuk ini luar biasa! Lihatlah ke dalam"
    r "Maaf, ini terlalu berdebu, tolong bersihkan"
    "Remil mengibas-ngibas sekitar sambil menutup mulutnya."
    #hide jeffrey
    #show normal alios as alios di kanan
    al "Kau dengar? Lakukan, Cherry"
    #show normal cherry as cherry di kiri
    c "Baaik!"
    #hide alios
    #hide cherry
    "Cherry beranjak masuk ke dalam dan mulai menggunakan sihir yang mendorong debu keluar"
    r "Ini mengerikan! (Remil tetap batuk batukmeski menunggu di luar)"
    "Tidak lama kemudian, Cherry keluar"
    r "Terima kasih! Kamu tidak apa-apa, Cherry?"
    #show bored cherry as cherry di tengah
    c "Tidak apa, Cherry menghempas debu dari sekeliling jadi tidak kenapa-napa, tidak sepertimu"
    #show normal jeffry as jeffry di kanan
    j  "Tunggu, apa kamu melihat seseorang di dalam?"
    #hide cherry
    r "Bukankah ini tempat yang sudah ditinggalkan? Habis kayak begini sih tempatnya."
    #show sad jeffry as jeffry di kanan
    j "Tidak, kemarin-kemarin Aku melihat tanda-tanda seseorang tinggal di sini, kupikir tadi kita bisa bertanya kepada orang itu."

    #scene bg gubuk dalam day with dissolve(1.0)
    #show happy jeffry as jeffry di kiri
    j "Hey, tempat ini cukup luas! Tidak bisakah kita pindah ke sini?"
    r "(Orang ini emosinya labil sekali ya)"
    #show suprised alios as alios di kanan
    al "Ini terlihat berguna, mungkinkah ini buatan seseorang?” Melihat ke arah kumpulan botol tanah liat di rak"
    #hide alios
    #hide jeffry
    "Aku masuk ke salah satu ruangan di dalam gubuk?"

    r"(Ruangan ini cukup sempit…)"
    r "Ke mana tempat ini mengarah?” Melihat ke dalam dan berjalan masuk"
    "…"
    "Di dalam sini cahaya sangat minim dan terdapat banyak jasad monster, selain itu juga terdapat potongan organ yang baunya kurang menyenangkan. Di atas meja, Aku menemukan lembaran kertas"
    #show item lembaran penelitian
    pause 2.0
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
    pause 2.0
    #hide item lembar penelitian
    #show bored cherry as alios di kanan
    c "Jadi, apa ini sampah yang kamu temukan di dalam?” Seolah menyindir Alios yang membawa botol tanah liat"
    #show happy alios as alios di kiri
    al "Kertas? Hahaha, menarik!"
    #show smirk alios as alios di kiri
    al  "Mungkin mereka yang meninggalkan ini masih di sekitar sini, Aku jadi suka ini"
    #hide cherry
    #show normal jeffry as jeffry di kanan
    j "Aku kurang yakin, kertas ini mencurigakan. Mungkin saja sesuatu ini yang menculik Elena, kan?"
    #hide alios
    r " …"
    #hide jeffry
    #show normal alios as alios di kiri
    al "Dengarkan, kurasa jika kita ingin mencari perempuan itu, kita harus berpencar, sampai kita menemukan kota orang-orang."
    #show normal jeffry as jeffry di kanan
    j "Baiklah, jika mereka orang jahatnya kita hanya perlu menghajarnya, bukan?"
    #hide alios
    r "Kamu pasti bercanda…"
    j "Kalau begitu, tolong ikuti Aku."
    #hide jeffry
    "Kami berjalan lurus dari arah gubuk"

    #show CHAPTER 2
    #“Hukum Rimba: Memangsa atau Dimangsa” with dissolve(3.0)

    #show bg Hutan - Day with dissolve(3.0)
    r "Di hutan ini benar-benar tidak ada orangnya ya?"
    #show normal jeffry as jeffry di tengah
    j "Kita tidak bisa mengambil kesimpulan itu, semenjak kita bahkan belum keluar dari hutan ini."
    r "(Sungai ini…)"
    j "Kurasa kita harus berpencar.."
    j "Aku akan mengambil jalan di kanan bersama teman kita yang satu ini."
    r "(jeffry melihat ke arahku)"
    menu:
        "Baiklah. Kalau begitu Aku, Alios, dan Cherry ke kiri":
            jump b1deca1
        "Apa kamu yakin? Aku rasa sebaiknya kita tetap jalan bersama":
            jump b1decb1


    return

label b1decb1:
    r "Apa kamu yakin? Aku rasa sebaiknya kita tetap jalan bersama"
    #show angry jeffry as jeffry di tengah
    j "Remil, nyawa Elena mungkin sedang terancam. Di saat seperti inilah kita harusnya berpencar"
    r "Baiklah. Kalau begitu Aku, Alios, dan Cherry ke kiri"
    jump b1deca1
    return


label b1deca1:
     #scene bg dekat sungai dusk with fade (3.0)
    #show bored cherry as cherry di kiri
    c "“Heei, berapa lama kita akan berjalan?"
    #show normal alios as alios di kanan
    al "Diamlah, Cherry. Kau bahkan tidak membawa apapun bersamamu"
    al "Sebentar, lihat ke bawahmu"
    #hide cherry
    r "(Jejak ini…)"
    al "Aku baru pertama kali melihat jejak lurus begini, bukankah ini seperti…"
    r "Jejak ular!"
    #hide alios.
    r "Kita harus pergi dari sini. Cepat!"
    #play sound snake hiss
    ur " hiss"
    #show suprised cherry as cherry di kiri
    c "Hiiih, suara apa itu!"
    r "Cherry! Cepat tahan! Di depanmu"
    #show serious cherry as cherry di kiri
    c "Sungai, penghalang terjadilah!"
    r "(Bodoh! Jangan yang itu!)"
    #show suprise cherry as cherry di kiri
    c "Kenapa dia mendekat"
    #hide cherry
    "Di saat itu, Alios melemparkan botol ramuan ke ular dan tercipta kabut"
    "Setelah itu, Cherry terpental karena ular menerjang tepat ke arahnya"

    #scene bg dekat sungai dusk with fade (1.0)
    r "Ugh- Sakit."
    #show suprise cherry as cherry di kiri
    c "Aah- Tidak bisa, Cherry tidak bisa!"
    "Cherry Merangkak ke arah hutan"
    #hide cherry
    #show normal alios  as alios di kanan
    al "Ck, tidak berguna."
    r "(Alios hebat, dia menancapkan kapaknya ke dalam tanah)"
    #show angry alios  as alios di kanan
    al "Bangun, bocah! Kita harus menaklukkan ini berdua"
    r "... (Mengangguk)"
    r "Alios! Aku akan menggiringnya, kamu carilah kesempatan!"
    #show normal alios  as alios di kanan
    al "Kau pikir siapa yang kau suruh?"
    r "(Orang ini masih saja sombongnya selangit)"
    #hide alios
    r "(.. Kabut akan mulai menghilang, Aku akan bergerak ke arah yang berbeda mendekati ular)"


    #scene BG Hutan - Day with dissolve(3.0)
    "Aku berlari ke dalam hutan. Di saat yang singkat saat ular menerjang dengan kepalanya, Aku menghindar"
    "Aku mendaki ke atas pohon dan merangkak ke dahan besar, kemudian ular tersebut melihatku lalu memutar badannya ke arahku"

    #show CG Alios dan Remil melawan ular besar di hutan (Hutan - Day) with fade(3.0)
    al "Kemana kau melihat, dasar serangga!” Mengayunkan kapak untuk mensayat perut ular yang melilit pohon"
    #play sound axe slashing
    r "(Berhasilkah!?)"
    r "Hah?"
    "Kapak Alios bahkan tidak menggores kulit ular dan dia malah terdorong mundur karena kapaknya yang berat."

    al "Duh, sialan! Keras sekali sih sisikmu, cacing!"
    #play sound tree shaking
    r "(Batang pohon ini akan hancur, akan kuserang di saat ini selagi Alios membuka kesempatan)"
    "Aku merunduk dan memegang dahan dengan kuat lalu melompat ke arah kepala ular yang melihat Alios"

    r "Haaaa!” Menusuk belati ke mata ular"
    "Aku melompat dari dahan pohon dan baru saja mengambil pijakanku dan merunduk di bawah"

    #scene  BG Hutan - Day with fade(1.0)
    r  "Huf-huf"
    n "Habis kau, keeeooong!” Melompat"
    #play sound felsh tearing
    # show alios angry2 as alios di tengah
    "Alios merobek mulut ular secara vertikal yang menggeliat kesakitan."

    n "M-Menghindar!"

    #hide allios
    "Racun ular merembes keluar ke punggungku."
    r "Hah!"
    # show normal alios  as alios di tengah
    al "Kau baik-baik saja, bocah?"
    r  "Ya, entah bagaimana.."
    # show happyl alios  as alios di tengah
    al "Kerja bagus, sebaiknya kita mengambil bawaan kita karena mulai gelap"
    r " …"
    # show normal alios  as alios di tengah
    al "Sebelum itu, Kau bau dan lengket. Melompatlah ke sungai"


    #show BG Dekat Sungai - Dusk with dissolve(3.0)
    r "Daging ular ini banyak sekali…"
    # show happy alios  as alios di tengah
    al "Ini baru namanya pesta! Hahaha!” Membakar perut ular sangat besar"
    r  "Tunggu, hanya kita berdua yang makan?"
    # show normal alios  as alios di tengah
    al "Kukira kau kuat makan banyak?"
    r "?"
    #hide alios
    r "Baiklah, tetapi Aku akan pergi mencari Cherry sebentar"
    # show normal cherry  as cherry di kiri
    c "Di sini ada orang? Tolong!"
    r "Oh, Cherry. Panjang umur"
    # show sad cherry  as cherry di kiri
    c "Hiks, kalian selamat? Cherry sangat takut!"
    # show angry alios  as alios di kanan
    al "Berhenti menangis, Cherry! Duduklah dan rawat lukamu"
    r  "Biar kubantu"


    #show BG Perkemahan - Night with fade(3.0)
    # show normal  alios  as alios di tengah
    al "Hei, Aku lelah. Aku istirahat duluan ya"
    r "Baiklah, giliranku. Aku tidak bisa tidur"
    al "“Bagus, terima kasih"
    r "..."
    "aku mengangguk kepada alios"
    #hide alios
    "Aku membuka lembar penelitian monster."

    r "(Kertas yang kupungut ini tidak ada ularnya… Sangat tidak berguna)"
    r "(Membahas tentang itu, ular yang sangat besar tadi menguasai daerah sekitar sini, sehingga harusnya tidak ada monster, tetapi kita tidak tahu apa yang akan terjadi karena dia sudah mati)"
    r "(Tapi dengan ini, kita jadi punya petunjuk tentang hilangnya Elena)"

    #show BG Perkemahan - Day with fade(3.0)
    #show normal  cherry  as cherrydi tengah
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
    c "hm, kau tidak menanyakan kabarku?"
    r "?"
    #show bored  cherry  as cherry di tengah
    c "Alios sedang di sungai mencari ikan"
    r "oke"

    #show BG Dekat sungai - Day with dissolve(1.0)
    #show angry alios  as alios di tengah
    a "Hei-hei! Berhenti bergerak dasar makhluk bodoh berinsang!"
    r "Kamu tidak menggunakan pisau untuk menghabisi mereka?"
    al "Mereka berenang di air, bego. Memang kau bisa menusuk mereka?"
    r "Oh"
    r "Kalau gitu, sebaiknya kamu minta Cherry mengumpulkan mereka dengan sihir."
    #show suprise alios  as alios di tengah
    al "!"
    #show happy alios  as alios di tengah
    al "Hahahaha! Kau benar! Belakangan dia terlihat tidak berguna, Aku lupa"
    r "(Jahat sekali..)"
    r "Kalau begitu, Aku akan coba pergi ke sana dan memeriksa sekitar"


    #show CG Remil di atas tebing dekat air terjun melihat ke sungai (Dekat Air Terjun - Day) with fade(3.0)
    #play sound waterfall
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
    "Entah mengapa monster-monster di sekitar sini semakin banyak, Aku harus mencari jalan keluar dari hutan. Hutan ini tidak bisa dipakai lagi untuk beristirahat"
    r "(!!)"
    r "Di belakang situ, terdapat tempat yang tidak hijau"
    #scene BG Perkemahan - Dawn with dissolve (3.0)
    r "Semuanya dengar, Aku rasa kita bisa mulai bergerak. Aku menemukan jalan keluar dari hutan"
    #show happy chery as cherry di kiri
    c "Akhirnya.."
    #show suprise alios as alios di kanan
    al "Kau tidak salah lihat kan!?"
    #hide cherry
    r "Tidak, Aku serius melihatnya"
    #show happy alios as alios di kanan
    al "Baguslah kalau begitu. Pastikan kau pimpin jalannya."
    r "Baiklah, sekarang ayo kemas bawaan kita"

    #scene CHAPTER 3
    #“Pada Semua yang Datang Entah Dari Mana Kemudian Pergi” with fade (3.0)
    # scene BG Hutan - Day
    #show serious chery as cherry di left
    c "Hey, apa yang akan kalian lakukan setelah keluar dari hutan?"
    r "“Aku ingin menemukan orang untuk mencari petunjuk hilangnya Elena."
    c "Kalau Cherry, ingin beristirahat dan hidup dengan tenang."
    #show normal alios as alios di kanan
    al "Ada apa kau tiba-tiba, Cherry? Kau bosan?"
    #hide cherry
    #hide alios
    r "Kurasa tidak ada salahnya bertanya, bukan?"
    #show sad chery as cherry di left
    c "Habisnya… Cherry tidak tahu apa yang kalian pikirkan!"
    #show normal alios as alios di kanan
    al "..."
    al "Kau terlalu banyak berpikir, Cherry."
    r "(Cherry…)"
    r "Kau takut, Cherry? Tidak apa, kita semua akan baik-baik saja."


    #show CG Remil, Alios, dan Cherry di jalan setapak alami dari bebatuan di pinggir hutan (Hutan - Day) with fade(3.0)
    al "Hey, Remil. Ini begitu menggangguku sejak kemarin.."
    al  "Bagaimana kalau kita bertarung?"
    r "(?)"
    r "Apa tadi kepalamu terbentur di suatu tempat?"
    al "Baiklah, ku anggap itu jawabanmu."
    " Alios memegang pedang besarnya yang dia dapatkan dari membunuh ular"
    #play sound greatsword swing
    r "(Aku rasa aku akan lari)"
    r "Cherry, tunggu di sana!"
    c "Ap- Hey! Tunggu!"
    c  "Cherry benci kalian, dasar maniak!"
    al "Sini kau, jangan kabur!"
    r "Hentikan, bego. Jangan mentang-mentang semenjak dapat senjata baru lalu mengetesnya denganku!"
    al "Kau lucu. Sini lawan Aku dengan benar!"
    r "(Kamu gila..)"


    #scene BG Lembah - Day with fade(1.0)
    r "Monster!” Aku terhenti di depan lembah. "
    #show smirk alios as alios di tengah
    al "Akhirnya kau berhenti juga!” kata Alios"
    r "Hah- Kamu mengejarku sampai sini? Dengan pedang itu?"
    "Alios melihat kerumunan monster di depan dan dari samping."
    #show normal alios as alios di tengah
    al "Namun, kurasa ini bukan saatnya untuk itu."
    r "Ya."
    #hide alios
    "Selama beberapa menit, monster-monster turun dari tebing dan terus bertambah jumlahnya di lembah."

    r "(Monster-monster ini tidak ada habisnya..)"
    #show angry alios as alios di tengah
    al "Sepertinya Aku terkepung."
    r "Kamu kelelahan?"
    al"Tidak. Aku hanya kesulitan menangkis semua serangan proyektill mereka."
    #show angry alios as alios di tengah
    al "Mereka monster yang pengecut."
    "Ini memang sulit… apalagi dia belum terbiasa dengan pedang barunya"

    r "Bertahanlah!"
    #show normal alios as alios di tengah
    al "Kau bicara dengan siapa?"
    r "(Nih orang masih aja..)"
    #hide alios.
    n  "Heeey!"
    r "Jeffrey?!"
    #show normal cherry  as cherry di kiri
    c "Cherry membawa teman-teman, Alios, Remil!"
    #show normal elena as elena di kanan
    e "..."
    r "(Elena juga ada!)"
    r  "!"
    #hide cherry
    #hide elena
    "Aku merasakan aura bahaya."

    #play sound Sword blocking/ parrying a magic
    #show normal alios  as alios di tengah
    al "Jangan mengalihkan fokusmu, jangan mati."
    "Alios menghalau proyektil monster"
    r "Terima kasih!"
    #hide alios
    #show seriousl elena as elena di kanan
    e "Kami datang membantu."
    #show normal alios  as alios di kiri
    al "Jadi, siapa orang yang kau bawa?"
    #hide elena
    #show normal jeffrey  as jeffry di kanan
    j "Perkenalkan, ini adalah dokter kita, Kai!"
    #show hapy kai  as kai di tengah
    k "Halo kalian! Namaku Kai."
    #hide alios
    #hide jeffrey
    r "Ah- Halo."
    k "Halo untukmu, Remil. Aku sudah dengar tentangmu. Kamu hebat."
    r "Ah, iya-"
    #hide kai
    #play sound  Bullet whizzing/ whooshing
    "Aku kemudian menghindar karena ditembaki proyektil dari atas."

    r "(Monster-monster ini tidak bisa tunggu orang selesai bicara ya.)"
    r "Baiklah, kita perkenalkan diri nanti, Aku harus mengurus mereka."
    #show laugh kai  as kai di tengah
    k "Hahaha- baiklah sana!"
    r "(Nih orang nyebelin.)"
    #show serious kai  as kai di tengah
    k "Aku juga sudah dengar tentangmu, Alios. Kamu menghabisi manusia, ya?"
    #hide kai
    "Kai mengarahkan tongkatnya ke samping muka Alios."

    #show angry alios as alios di kiri
    al "Jauhkan tongkatmu, apa kau tahu bayaran untuk mengganggu pertarunganku?"
    #show serious kai  as kai di kanan
    k "Jangan lakukan lagi!"
    #show suprise alios as alios di kiri
    al "!"
    #show normal alios as alios di kiri
    al "Baiklah, tetapi jangan mencoba mengaturku."
    #hide kai
    #hide alios
    "Di saat itu, bantuan teman-teman sangat berarti hingga kami yakin pertarungan ini bisa berakhir dengan cepat."

    #scene BG Lembah - Day with dissolve(1.0)
    r "Huf-huf."
    #show suprise jeffrey  as jeffry di kiri
    j "Oh- Elena, kau terlihat tidak enak badan, kamu baik-baik saja?"
    #show nervous elena  as elena di kanan
    e "Ya, tetapi Aku tidak bisa terbiasa dengan monster-monster ini."
    #show laugh jeffrey  as jeffry di kiri
    j  "Hahaha"
    #hide elena
    #show normal jeffrey  as jeffry di kiri
    j " Kalau kalian? Apa kalian baik-baik saja?"
    r "Hanya butuh istirahat."
    #show normal alios as alios di kanan
    al "Aku bisa lanjut.."
    r "(Orang ini gak bisa capek ya?)"
    #show normal kai  as kai di tengah
    k "Baiklah, mengingat kalian ‘semua’ sudah lelah. Sebaiknya kita beristirahat di sekitar sini. Ikuti Aku."
    #show angry alios as alios di kanan
    al "Tunggu!"
    #hide jeffrey

    al "Bagaimana kita bisa percaya pada kau? Aku mau Jeffrey yang pimpin jalannya."
    #show normal jeffrey  as jeffry di kiri
    j "Maaf, Bos. Jujur saja, anak ini lebih tahu jalan dibanding Aku."
    #show normal kai  as kai di tengah
    k "“Yeah."
    #show angry alios as alios di kanan
    al "Ck. Awas saja kau kalau melakukan sesuatu yang mencurigakan."
    #show laugh kai  as kai di tengah
    k "Hahaha."
    #hide kai
    #hide jeffrey
    #hide alios
    #show happy kai  as kai di tengah
    k "Nah bocah-bocah! Kalian harus pakai nih, ‘cairan’."
    #show item botoh tanah liat
    pause 2.0
    #hide item botol tanah liat
    r"(Cairan?)"
    #show suprise  alios as alios di kanan
    al "Ini! Kau yang membuatnya!?"
    #show normal kai  as kai di tengah
    k "Benar. Kamu tahu sesuatu?"
    #show happy alios as alios di kanan
    al "Aku melihatnya cukup banyak di hutan. Itu benda yang berguna sekali!"
    #show seriousl kai  as kai di tengah
    k "Kamu mengambil itu?! Itu barang yang berbahaya, anak bego."
    r "Lalu Anda memberi kami ini?"
    #hide alios
    k "Dua itu benda yang berbeda."
    r "Bagaimana aku bisa yakin denganmu?"
    #show normal elena  as elena di kiri
    e "Tenanglah, Remil. Kamu bisa percaya dengannya."
    e "Dia sudah menyelamatkanku."
    r "..."
    "Remil membuka tutup botol tanah liat"
    #hide elena
    #hide kai
    #show normal  alios as alios di kanan
    al "Hei, Kai. Bagaimana cara memakai cairan ini, diminum?"
    #show normal kai  as kai di kiri
    k "Lebih baik dioleskan atau disiram, untuk diminum sangat tidak disarankan. Meskipun pada dasarnya itu hanyalah cairan semut."
    r "(Hampir saja, kukira diminum)"
    al "Oke."
    #hide kai
    #hide alios
    "Setelah mengoleskan tangan dan wajah dengan ‘cairan’’, kami bergerak mengikuti Kai, orang yang menganggap dirinya dokter."

    #scene BG Lembah - Day with dissolve(1.0)
    r "Jadi, Anda datang dari mana? Anda terlihat tahu banyak hal."
    #show normal kai  as kai di tengah
    k "Kamu tanya padaku? Aku sudah beberapa tahun tinggal di tempat ini."
    #show happyl kai  as kai di tengah
    k "Aku kebetulan di sini ingin membantu kalian karena Aku sudah bertemu anak-anak ini saat di desa."
    r "(Anak?)"
    #show normal  alios as alios di kanan
    al "Kau tidak terlihat seperti orang yang baik."
    #show normal  jeffry as jeffrey di kiri
    j "Benarkah? Dia ramah untukku.” balas Jeffrey"
    al "Dia hanya ramah karena kau menjilatinya, Jeffrey."
    r "..."
    #hide alios
    #hide jeffrey
    #hide kai
    #show serious kai  as kai di tengah
    k "Aku tertarik dengan kalian, bocah yang seolah datang entah dari mana."
    r "(Entah dari mana?)"
    #hide kai
    "Semua orang terlihat diam, apa mereka sendiri tidak sadar?"

    r "Baiklah, lupakan masalah seriusnya. Kita harus membangun perkemahan, benar?"
    #show normal  jeffry as jeffrey di kiri
    j "Oh, benar."
    r ".. Apa Anda bisa membangun punyamu sendiri, Kai. Kami tidak punya cukup bahan di sekitar sini."
    #show normal  kai as kai di kanan
    k "Oh tidak apa, Aku tidak terlalu menginginkannya."


    #CHAPTER 4
    #“Ketenangan yang Menakutkan Sebelum Badai” with disolve(3.0)
    #scene BG Kantin - Night with dissolve(3.0)
    #show happy jeffrey as jeffrey di kiri
    j "Selamat datang, Kai. Ini pesta penyambutan untukmu!"
    j "Dan untuk reuni kita!"
    #show happy alios as alios di kanan
    al "Kau benar."
    #hide jeffrey
    r "(Tumben sekali dia terlihat patuh, biasanya sombong banget)"
    r "Aku lelah."
    #show normal alios as alios di kanan
    al "Ya, aku juga."
    al "Jadi, bagaimana kalian bisa berkumpul dan menemukan Elena?"
    #show nervous elena as elena di kiri
    e "Saat itu, Aku-"
    r "(Elena…)"
    #hide elna
    #hide alios
    #show serious  kai as kai di tengah
    k "Jadi begini, Aku menemukan perempuan ini saat di desa yang secara mendadak dikuasai oleh monster."
    k "Saat itu, Aku beberapa hari berjalan ke desa dari tanah di barat. Jadi, dasarnya, Aku adalah orang lewat."
    r "(Kosakatanya ituloh.)"
    #show normal alios as alios di kanan
    al "Lalu dari sana kau menyelamatkan Elena dan membawa Jeffrey ke desa?"
    k "Benar, lalu kami tinggal di desa. Beberapa hari setelahnya, kami mengikuti suara teriak perempuan dari kejauhan dan mengikutinya sampai sini."
    #hide alios
    #hide kai
    "Aku merasa ini belum menjelaskan semuanya."
    r "Elena, kenapa kamu menghilang? Tidak mungkin tidak ada dari kita yang sadar saat kamu menghilang."
    #show serious elena as elena di tengah
    e "Jadi, saat itu."
    e "Aku sedang pergi ke sungai untuk mengisi air di pagi hari. Lalu, ternyata Aku diincar oleh monster dan kemudian dibawa sampai ke desa."
    #show suprise jeffrey as jeffrey di kiri
    j "Jadi kamu tidak diculik orang?"
    #show happy jeffrey as jeffrey di kiri
    j "Itu sungguh melegakan!"
    r "Bagian mananya?"
    #show smirk alios as alios di kanan
    al "“Lupakan saja dia, tolong lanjutkan."
    #hide alios
    #hide jeffrey
    #show serious elena as elena di tengah
    e "Jadi, di desa, Aku melihat beruang besar yang menggunakan sihir untuk mengikatku. Dia terlihat seperti pemimpinnya dan jauh berbeda dengan monster yang kita biasa temui."
    e "Keesokan paginya, Aku terbangun di dalam kamar yang sejuk dan sadar kalau Aku telah diselamatkan oleh Kai."
    #hide elena
    "Ceritanya lompat sangat jauh jadi tidak masuk akal."

    r "Bagaimana caranya kamu menyelamatkan Elena, Kai?"
    #show serious kai as kai di tengah
    k "Malam itu, Aku pergi menyelamatkannya dengan menidurkan semua monster dan mengangkut mereka pergi."
    r "Bagaimana, tepatnya?"
    #show happy kai as kai di tengah
    k "Dengan sihir, kuterbangkan semuanya."
    #show happy alios as alios di kanan
    al "Hebat! Kau pasti orang yang kuat. Tidak seperti pengguna sihir kita satu ini."
    r "(Jahat sekali…)"
    #show angry cherry as cherry di kiri
    c "Hei!"
    r "..."
    #hide cherry
    #hide alios
    #hide kai
    #show serious kai as kai di tengah
    k "Ah maaf, kawan. Kurasa ini saatnya untuk kalian beristirahat. Aku akan berada di belakang sana kalau kamu butuh Aku."
    #hide kai
    r "Permisi, Aku akan ikuti Kai."

    #scene BG Perkemahan - Night with fade(1.0)
    #show normal alios as alios di kiri
    al "Cherry."
    #show normal cherry as cherry di kanan
    c "Ya?"
    al "Tentang yang kau katakan sebelumnya. Aku juga takut sepertimu."
    #show serious cherry as cherry di kanan
    c "..."
    c "Ada apa tiba-tiba, Alios? Kau bosan?"
    #show happy  alios as alios di kiri
    al "Hahaha! Ya!"
    #show normal cherry as cherry di kanan
    c "..."
    #show normal  alios as alios di kiri
    al "Kau mau tahu apa? Aku paling takut saat Remil mulai membalikkan taringnya padaku."
    al "Dia sangat berpotensi, Aku ingin dia jadi tangan kananku sebelum dia bertemu lebih banyak orang."
    #show normal cherry as cherry di kanan
    c "Jadi itu yang kamu pikirkan.."
    #hide cherry
    #hide alios
    #show normal jeffrey as jeffrey di kanan
    j "Alios terlihat tidak biasa, huh?"
    #show serious alios as alios di kiri
    al "Jeffrey!"
    #show supprise jeffrey as jeffrey di kanan
    j "Hah! Ya?"
    #show normal alios as alios di kiri
    al "Bagaimana kabarmu? Kau benar-benar membantu di sana."
    #show happy jeffrey as jeffrey di kanan
    j "Yah, Aku baik! Dan Elena juga."
    #show nervous elena as elena di tengah
    e "Ya."
    al".. Bagus."
    #hide elena
    #hide jeffrey
    #hide alios
    #show normal alios as alios di kiri
    al "Jadi, apa yang dilakukan Remil di sana?"
    #show normal jeffrey as jeffrey di kanan
    j "Kurasa dia ingin berbicara dengan paman jadi-jadian itu."
    #show normal cherry as cherry di tengah
    c "Paman itu mencurigakan."
    j "..."
    #hide cherry
    al "Lalu, kemana orang yang pergi bersamamu?"
    j "Oh, iya. Dia menghilang kemana ya?"
    j "Dia sebenarnya ikut dengan kami, tapi sepertinya dia tidak ada semenjak pertarungan di lembah."
    #show sad alios as alios di kiri
    al "Kurasa Aku belum cukup meminta maaf padanya."
    j "Lupakan saja, Bos. Dia terlihat sudah baik-baik saja bersamaku."


    #scene CG Remil dan Kai berbicara di lembah (Lembah - Night) with fade(3.0)
    r "Aku tahu Anda berbohong dari tadi."
    k "Hmm?"
    k "Kamu mengikutiku, Remil? Ada apa?"
    r "Katakan sejujurnya. Anda tidak mungkin hanya orang lewat biasa kalau bisa menidurkan dan menghempas kerumunan beruang. Aku yakin Anda pernah melihat kertas ini."
    k "Ho?"
    k "Kamu menemukan itu di gubuk lamaku? Apakah itu berguna?"
    r "Lumayan- Tunggu, jadi kau yang menulisnya!"
    k "Ya."
    r "..."
    R "Kalau begitu, apa Anda juga yang menculik Elena?"
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
    r "Ugh!"
    k "Kamu kembali, anak muda!"
    r ".. Apa yang terjadi?"
    k  "Tidak ada, sebaiknya kita kembali dan tidur."



    #CHAPTER 5
    #“Kebencian seperti Meminum Racun, Namun Berharap Musuhmu Terbunuh” with fade(3.0)
    #scene BG Perkemahan - Day with fade(3.0)
    #show happy jeffrey as jeffrey di tengah
    j "Halo, Remil. Tidurmu nyenyak?"
    r "Tidak juga.."
    #show normal jeffrey as jeffrey di tengah
    j "Ngomong-ngomong, kita sudah berencana kembali ke desa pagi ini. Sebaiknya kamu berkemas."
    r "Baiklah."


    #scene BG Lembah - Day with dissolve (1.0)
    r "Monster! Dan dalam jumlah yang banyak sekali."
    "b “HAHAHAHAHHAA- AKU KEMBALI, ALIOS!"
    #show suprise alios as alios di tengah
    al "Kau!"
    #show angry alios as alios di tengah
    al "Aku tahu kau sampah, tetapi kau jatuh sedalam ini dan sampai melibatkan semuanya!"
    b "AKU TIDAK PEDULI LAGI. MATI KALIAN!"
    #show suprise jeffrey as jeffrey di kiri
    j "Waduh, beruangnya banyak banget."
    #show normal jeffrey as jeffrey di kiri
    j "Tunggu, kemana Remil?"
    #show serious elena as elena di kanan
    e "!"
    #show suprise elena as elena di kanan
    e "Di atas sana, Remil?"
    #show angry jeffrey as jeffrey di kiri
    j "Remil, cepat ke sini! Di sini kita kesulitan."
    rg  "Kaaamu siaaapa?"
    j "?"
    al "Remil! Berhenti bercanda, kita semua sedang dihadang monster!"
    # hide alios
    #hide elena
    #hide jeffrey
    "Remil menerjang ke arah Alios, tetapi dihadang oleh Elena."

    rg "Hmmmmmmmm?"
    #show angry cherry as cherry di kanan
    c "Remil, kamu sudah gila! Lepaskan kak Elena!"
    "Cherrymenciptakan banyak bola api lalu ditembakkan ke arah Remil namun terus-menerus ditangkis"
    c "Hah- Lepaskan.."
    "Cherry kehabisan tenaganya lalu pingsan."
    #hide cherry

    #With fade 1
    #scene BG Lembah - Day with fade(1.0)
    #show angry kai as kai di tengah
    k "Berhenti di sana, kalian!"
    #hide kai
    "Saat itu, Kai bertukar posisi dengan Elena dan membuat lengan bawah Remil patah."

    #show serious kai as kai di tengah
    k "Kalian, tolong urus beruangnya dan jaga anak perempuan di sana."
    #show angry alios as alios di kanan
    al "Ck, darimana saja kau?"
    k "Maafkan Aku."
    #hide kai
    #show normal alios as alios di kanan
    al "Baiklah. Jeffrey! Pindahkan Cherry!"
    #show normal jeffry as jeffry di kiri
    j ".. Bagaimana dengan Elena?"
    #show sad alios as alios di kanan
    al "Keadaannya sudah tidak bagus. Dia mati."
    #show sad jeffry as jeffry di kiri
    j "..."
    #show serious jjeffry as jeffry di kiri
    j "Baiklah, Aku akan menembak dari belakang."
    #hide jeffrey
    #show normal alios as alios di kanan
    al "Dan kau bocah putih, kita bicarakan masalah ini nanti!"
    #show normal kai as kai di kiri
    k "Bocah.."
    #hide kai
    #hide alios
    "Kai melempar Remil dengan sihirnya lalu membuatnya lumpuh sementara."

    #show serious kai as kai di tengah
    k "Remil! Sadarlah!"
    #play soind  Earthquake rumbling
    rg "Hmmmm?"
    #show angry  kai as kai di tengah
    k "Haaaaa!” Kai berusaha untuk menekan Remil dengan gravitasi, namun Remil tetap bisa melawan"
    #hide kai
    "Kai pun mencoba sihir pelumpuh, pembuat tidur, penekan darah, namun tidak bekerja."


    #scene BG Lembah - Day with dissolve(1.0)
    #show angry alios as alios di kanan
    al "Jeffrey!"
    al "Jeffrey, kuatkan dirimu! Tembakkan panahmu dengan benar!"
    #show angry jeffry as jeffry di kiri
    j "Aku tahu!"
    #show normal alios as alios di kanan
    al "Saat kuberi tanda, kau tembaklah perutnya. Aku akan tangkis sihirnya!"
    #hide jeffrey
    #hide alios
    "Alios kemudian menerjang ke arah beruang dan memanfaatkan pedangnya yang besar untuk menerobos ke depan. Lalu, dia menghantam beruang besar dengan sisi pedangnya."
    #show normal alios as alios di kiri
    al "Sekarang!"

    #play sound  Bow drawing
    #show serious jeffry as jeffry di kanan
    j "!"
    "Jeffrey kemudian menembak panah yang telah dilumuri racun ke perut beruang."
    #hide jeffrey
    #show angry alios as alios di kiri
    al "Habis kau!” Menebas secara diagonal ke arah bahu beruang"
    #play sound  Flesh tearing
    #hide alios
    #show happy jeffry as jeffry di kanan
    j "Bagus, Alios! Rajanya sudah dikalahkan."
    #show normal alios as alios di kiri
    al "Belum, masih ada keroco lainnya."
    #show serious jeffry as jeffry di kanan
    j "..."
    #hide alios
    #hide jeffrey
    "Alios kemudian menerjang ke depan dan melawan beruang-beruang di depannya dan Jeffrey menjaganya dari belakang."

    # scene  BG Lembah - Day with dissolve(1.0)
    #show serious kai as kai di tengah
    k "Sadarlah!!” kata Kai yang mulai kehabisan sebagian mananya"
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
    #show suprise alios as alios di kiri
    al "!"
    #show normal alios as alios di kiri
    al "Bocah putih! Bawa Cherry, kau pasti sudah kehabisan mana!"
    rg "Haha, Kai! Kamu lari?"
    #hide alios
    "Kai mendekat ke arah Cherry lalu menghilang, meninggalkan Remil yang dikendalikan di sana. Lalu, Alios berlari menghampiri Remil."

    #show angry alios as alios di tengah
    al "REMIL! Sadarlah!"
    "Alios mengayunkan pedang besarnya ke Remil"
    #play sound Heavy sword swinging
    #hide alios.
    "Lalu, Remil menghindar."

    #show angry alios as alios di tengah
    al "Kau! Ini bukan saatnya bercanda!"
    rg  "Hihihi. Bercanda?” Remil kemudian melihat ke arah lain"
    #hide alios
    rg "Akan kutunjukkan maksudnya bercanda."
    #show normal alios as alios di kiri
    al "Jeffrey! Merunduk!"
    #show suprise jeffrey as jeffrey di tengah
    j "Ap-"
    #hide alios
    #hide jeffrey
    "Kepalanya terpenggal."


    #scene BG Lembah - Day with fade(1.0)
    #show angry alios as alios di tengah
    al "Kaaaaaau!"
    "Alios mengayunkan pedang besarnya."
    #hide alios.
    "Remil menangkap pedang tersebut, lalu dihancurkan."
    #play sound Sword breaking

    #show angry alios as alios di tengah
    al "Ck, pedang baruku sangat tidak berguna."
    al "Kalau begitu Aku gunakan kapak lamaku, khusus untukmu!"
    "Lalu, Alios mengayunkan kapaknya, namun perutnya ditendang oleh Remil dan genggamannya pada kapak terlepas."
    #play sound Object dropping on sand

    #hide alios
    pause 1.5
    #play sound  Body falling
    "Alios terkapar di tanah."


    #play music  sad music loop
    #show smirk alios as alios di tengah
    al "Hahaha, jadi kau masih dendam tentang Aku, lalu kau merencanakan semua ini?"

    rg "Berhenti berbicara, bocah."
    #show sad alios as alios di tengah
    al "Kau pasti sangat membenciku, huh?"
    "Kemudian, Remil menghancurkan rusuk Alios dengan pijakannya."
    #play sound  Bone cracking
    #show suprise alios as alios di tengah
    al "!"
    "Alios batuk darah."
    #show sad alios as alios di tengah
    al "Harusnya kita adalah keluarga. Aku merasa dikhianati..” Alios kehilangan tenaganya untuk bicara"
    #hide alios.


    # scene BG Lembah - Day with dissolve(1.0)
    n "Gordon! Kau sudah keterlaluan!!"
    n "Dengan sisa manaku, kau akan kubakar! Gordooon!"
    "Dari atas, lembah tersebut tertutupi sinar dan semua beruang terbakar api membara, termasuk Alios yang masih dalam keadaan kritis."

    #show sad alios as alios di tenga
    al "Maaf.."
    al ".. Terima kasih."
    rg "..."
    b "HAHAHAHAHAHA- RASAKAN ITU! AKU BERHASIL-"
    b "AAAAAAAAAARGH"
    "Dia terbakar menjadi abu."
    #hide alios
    "Di atas sana, Remil sadar kembali sesaat dan menengadah ke atas. Dia sekilas melihat Kai yang mengangkat tongkatnya dan Cherry yang terkapar."
    " (..!)"
    "Remil kemudian pingsan."


    #scene CG Lembah dan Remil di tengah jalan yang sedang pincang (Lembah - Day) With fade(3.0)
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


    # BG Lembah - Day with fade(1.0)
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
    #“Akhir dari Perjalanan Para Pengembara di Dunia Lain” with dissolve (3.0)
    # scene BG Hutan with disolve(3.0)
    "Aku mengalahkan banyak monster di perjalanan dengan kekuatan listrik aneh yang kudapatkan setelah pertarungan di lembah hari itu."
    "Beberapa bulan kemudian."

    #BG Padang Gurun - Day with dissolve(3.0)
    "Aku telah mengalahkan banyak monster di perjalanan dan Aku mulai terbiasa membunuh dengan tangan kosong."
    "Akan tetapi, kurasa tanganku berkata lain. Rasanya aneh saat mencengkeram sesuatu yang berdenyut."
    "Meski di sini dan di sana banyak monster, Aku sangat jarang bertemu orang lain"

    #BG Desa Kai - Day with fade(1.0)
    a "Terima kasih sudah datang membantu, tuan Kai sudah lama tidak kembali, sehingga anda menyelamatkan kami."
    r "“Ya, Aku juga berterima kasih untuk perawatanmu."
    a "Sama-sama."

    #BG Hutan - Day with dissolve(3.0)
    r "(Aku dengar jika kita memutari lembah, ada dataran tinggi yang dijaga monster di sana.)"
    "Aku masih dalam perjalananku mencari alasan untuk hidup. Bahkan, jika itu artinya Aku harus mati."


    #BG Lembah - Daywith dissolve(3.0)
    r "(Monster di sini memang semakin banyak)"
    "Aku menyadari, Aku tidak pernah memikirkan ini."
    r "(Tetapi, sebenarnya dari mana semua monster ini?)"

    #With fade 3
    #BG Plateau - Dusk with fade (3.0)
    "Aku merasakan atmosfer yang berbeda di hadapanku."
    "Masuk di dalamnya, Aku melihat perkemahan di dalam."

    r "!"
    "Aku hampir menginjak jebakan di dalam."
    #show suprise kai as kai di kanan
    k "Oh! Hey, Remil!"
    r "Kai.."
    #show normal kai as kai di kanan
    k "Kamu butuh tiga bulan untuk sampai di sini. Apa kepala desa yang memberitahumu?"
    r "Ya. Maaf, Aku-"
    #show happy kai as kai di kanan
    k "Tidak apa, kamu pasti telah menderita sangat lama dalam perjalanan yang melelahkan."
    #show sad kai as kai di kanan
    k "Tidak, malah. Ini sebenarnya terlalu jahat untuk anak kecil sepertimu."
    "(Anak kecil?)"
    #show normal kai as kai di kanan
    "Sini, datanglah. Kita bisa berbincang sebentar."
    r "..."
    r "Tidak bisa, Aku akan pergi."
    #show happy kai as kai di kanan
    k "Aku ada bakar daging juga."
    r "(...)"
    r "Satu aja deh."
    #hide kai
    "Aku memutuskan untuk duduk bersama Kai di tanah yang luas itu."

    #scene BG Plateau - Dusk with dissolve(1.0)
    #show happy kai as kai di kanan
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
    "Tergigit? Aku mencoba mengingat yang pernah kulakukan."

    r "(!!)"
    r "Racun ular!"
    #show suprise kai as kai di kanan
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

    #scene BG Plateau - Dusk with dissolve(1.0)
    r "Jadi ada apa?"
    #show serious kai as kai di tengah
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
    k "Hahaha-"
    #show happy kai as kai di tengah
    k "Maaf, anak sepertimu tidak akan mengerti."
    r "Lalu, bagaimana cara kita kembali?"
    #show serious kai as kai di tengah
    k "..."
    "Kai hanya menatap dengan serius."
    #show normal kai as kai di tengah
    k "Aku juga penasaran."
    r "Jadi kau kira kau bisa diam saja?"
    "Aku mengarahkan belatiku ke Kai, namun tanganku terhenti"
    k "Kalahkan Aku, maka akan kujelaskan semuanya."
    #hide kai.
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
    k "!"
    #show laugh kai as kai di tengah
    k "Hahahaha, Kamu anak yang jujur."
    r "(?)"
    #show happy kai as kai di tengah
    k "Baiklah, mari kita bicara di luar."
    #show serious kai as kai di tengah
    k "Ikuti Aku."
    r "!"
    #hide out
    "Aku melihat Cherry mengintip dari kejauhan."

    #show normal kai as kai di kanan
    k "Kamu tidak jalan?"
    r "Lupakan saja, tolong setidaknya bawa Cherry pergi."
    #show serious kai as kai di kanan
    k "Cukup. Ikuti Aku."
    r "!"
    "(Lukaku perlahan menutup sendiri.)"
    #hide out.

    #scene BG Plateau - Dusk with dissolve(1.0)
    "Saat itu, Kai menunggu di ujung tebing."
    "Di saat Aku melangkahkan kaki di luar, tanganku menembus jantung Kai."

    r "AAAAH! Tidak!"
    uv "Bagaimana kabarmu, Kai?"
    "Gordon yang berbicara melalui kepala mereka"
    #show suprise kai as kai di kanan
    k "!"
    uv "Dapat kau. Kau tidak boleh lari karena ini akan jadi menyenangkan. Hihihihi."
    #hide kai
    r "Kau, Gordon! Orang sinting, Aku tahu semuanya! Lepaskan Aku!"
    uv "Lalu apa? Kamu merasa kamu bisa mengancamku?"
    uv "Aku adalah penyelamatmu!"
    r "Hah? Berhenti berbicara omong kosong!"
    uv "Kamu hanya anak buangan! Kamu kira kamu bisa hidup kalau bukan karena…"
    #show normal kai as kai di kanan
    k "Sh- Jangan dengarkan dia."
    r "!"
    "Aku didorong kembali ke dalam penghalang."
    #show happy kai as kai di kanan
    k "Lakukanlah yang kamu inginkan."
    "Kata Kai dengan sisa tenaganya dan jatuh dari tebing"
    r "Kai!!"
    #hide kai
    "Aku teringat pada Cherry."

    #With fade 1
    #scene BG Plateau - Dusk with fade(1.0)
    r "Cherry, kamu dimana!"
    uv "..."
    r "Cherry!!"
    #show angry as cherry di tengah
    c "Diam!"
    c "Kamu bohong! Kamu bilang semua akan baik-baik saja."
    "Cherry menembakkan pedang cahaya dan mengores bahu Remil"
    r "Maafkan Aku, Cherry-”"
    #show normal as cherry di tengah
    c "Cherry sempat percaya padamu! Kamu pikir maaf saja cukup?"
    #show angry as cherry di tengah
    c "Kamu menghancurkan tulang Alios! Kamu memenggal kepala Jeffrey!"
    r " …"
    #show sad as cherry di tengah
    c "Dan, kamu tidak puas hanya dengan mencekik leher kak Elena!"
    r "Dengarkan Aku!"
    "Aku berusaha mendekat dan menjelaskan semuanya."

    c "Berhenti di sana!"
    "Cherry memunculkan sinar besar dari atasnya."
    #hide cherry
    "Aku berusaha untuk menghindar, namun bagian kiri tubuhku terpotong habis."
    "Aku terkapar dan Cherry mulai menghampiriku."

    #With fade 3
    #show CG Cherry duduk menangis di samping saat Remil kehilangan sebagian badannya (Plateau - Dusk)
    "(Ugh!)"
    #play music  sad music
    r "Maafkan Aku, Cherry."
    "Aku mulai kehabisan tenagaku untuk berbicara."
    "(Cherry..)"
    r "Cherry, suatu hari.."
    r "Mari kita bertemu yang lain di luar sana."
    "Saat barrier tidak lagi melingkupi tubuhku, bahu kiriku tumbuh dan tanganku mencengkeram tangan Cherry."

    r "Hentikan- HENTIKAN! GORDOOOOOOON!"


    #BG Plateau - Dusk with fade(1.0)
    "Di saat itu, badan Cherry terpisah dua atas bawah."
    "Tubuhku kembali utuh dan barrier sudah lenyap, seutuhnya."

    #scene CG Remil berjalan ke ujung tebing di plateau (Plateau - Dusk) wirth dissolve(3.0)
    r "Hahahaha- Akhirnya begini!"
    c "Hentikan- Remil"
    r "GORDON, HABISI SAJA AKU!"
    r "Kalau kau tidak, Aku akan melompat!"
    g "Kikikik-"
    "Aku berjalan ke ujung tebing."

    r "3.."
    g "KAAHAHAHAHAHAHAH!"
    r "2.."
    r " : …"
    r "“1."
    "(Selamat tinggal, semuanya..)"
    "Di bawah sana, Aku melihat badan Kai yang tertusuk oleh batuan."

    "Aku menutup mataku dan berharap ini akan berakhir. Dunia yang penuh penderitaan ini."

    #With fade to black 3s
    "Jumlah karakter hidup tersisa = 0."
    "Catatan: Avatar subjek E dicekik oleh subjek R yang berada di luar kendali setelah otaknya beresonansi dengan AI"
    "Catatan: Avatar subjek J dipenggal oleh subjek R yang dikontrol"
    "Catatan: Avatar subjek A keberadaannya menghilang oleh kekuatan misterius"
    "Catatan: Avatar subjek C dibelah dua oleh subjek R yang dikontrol"
    "Catatan: Avatar subjek R meninggal karena tekanan berat psikologis"

    "The Alternative Ending"



    return
