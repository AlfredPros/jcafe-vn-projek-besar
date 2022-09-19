
label branch2:
    #WOOOOSH CHAPTER 1
    scene black with Dissolve (2)
    pause 2
    scene chp_1 with Dissolve (2)
    pause 4
    scene black with Dissolve (2)
    pause 2
    scene tenda_gelap with Dissolve (2)
    #BG Perkemahan Alios, night with fade 1s
    #Sad M in  Elena
    show elena_sad at enter
    e "Hei.. Remil, kamu tidak apa-apa?"
    e "Kamu jadi banyak melamun, waktu makan malam tadi juga kamu tidak lahap seperti biasanya."
    #Nervous Elena
    show elena_nervous as elena_sad
    e "...Remil?"
    show elena_confused as elena_sad
    #Confused Elena
    e "(Tendanya kosong. Apa dia kabur?!)"
    e "(Tetapi aneh. Semua barang-barangnya ada disini.)"
    hide elena_sad
    #Elena out
    pause 0.5

    scene hutan_night with fade
    #BG Hutan, night with fade 1s
    r "(Sepertinya aku sudah berjalan cukup jauh. Untung saja dari tadi aku belum bertemu dengan monster besar.)"
    #SFX: *Srak* *Srak* (suara semak-semak)
    play sound sfx_treeshaking
    r "Hm? Sepertinya aku belum pernah ke tempat ini sebelumnya."

    scene gubuk_luar_night with dissolve
    #BG luar gubuk tua, night with dissolve 1s
    r "Ada gubuk tua di tengah hutan gini?"
    r "(Sebelum aku memasukinya, aku harus memeriksanya dulu. Bahaya jika ada jebakan atau sesuatu yang berbahaya di dalamnya.)"
    #SFX: *Srak* *Srak* (suara semak-semak)
    play sound sfx_treeshaking
    r "(Sepertinya tempat ini kosong.)"

    #BG dalam gubuk tua, night
    scene dalam_gubuk_gelap with dissolve
    r "Haah.. Rupanya tempat ini jauh lebih nyaman dibanding tenda."
    show vignette with dissolve
    pause 0.5
    show old_book with dissolve:
        align (0.5, 0.4)
        zoom 0.1
    pause 0.5
    #show item buku catatan 1
    r "(Buku catatan?)"
    r "!!!"
    r "(Hebat! Buku ini berguna sekali. Di dalamnya banyak informasi mengenai tumbuhan yang dapat dikonsumsi, beracun, dan bahkan ada yang bisa dijadikan obat.)"
    r "(Isi buku ini juga terlihat seperti tulisan tangan, siapa orang yang menulis buku ini?)"
    #item buku catatan 1 out
    hide old_book with dissolve
    pause 0.5
    hide vignette with dissolve
    pause 0.5
    #*Hiiissss*
    play sound sfx_snakehiss
    r "(Ada monster di luar, sepertinya aku harus menghabiskan malam di sini.)"
    #Fade in black 1s
    scene black with dissolve
    pause 2

    scene gubuk_luar_day with dissolve
    #BG Luar gubuk tua, day
    r "(M-Monster itu masih ada! Itu kan ular yang pernah menyerang aku sebelumnya. Aku tidak bisa tinggal di sekitar sini, aku harus segera pergi)."
    #transition BG Hutan, day
    scene hutan with dissolve
    r "*Groowl*"
    r "Aku lapar.."
    r "Kebetulan sekali aku menemukan buah beri di sini!"
    r "Tetapi.. Kenapa rasanya aku pernah melihat buah ini sebelumnya ya?"
    #show item buku catatan 1
    show vignette with dissolve
    pause 0.5
    show old_book with dissolve:
        align (0.5, 0.4)
        zoom 0.1
    pause 0.5
    "Aku mengambil buku catatan yang aku temukan di gubuk itu."
    r "(!!!)" with vpunch
    r "Ternyata buah beri yang aku petik barusan ini beracun. Untung saja aku belum memakan satu pun."
    #item buku catatan 1 out
    hide old_book with dissolve
    pause 0.5
    hide vignette with dissolve
    pause 0.5
    r "*Groowl*"
    r "Aduh perutku.. Aku harus mulai berburu."
    #show kelinci berbulu pink dan bertanduk
    show vignette with dissolve
    pause 0.5
    show pink_bunny with dissolve:
        align (0.5, 0.4)
        zoom 0.3
    pause 0.5
    "Aku melihat seekor kelinci bertanduk yang sedang melompat ke suatu arah. Dengan cepat aku menangkap kelinci itu dan membunuhnya dengan pisau milikku."
    #kelinci berbulu pink dan bertanduk out
    hide pink_bunny with dissolve
    pause 0.5
    hide vignette with dissolve
    pause 0.5
    r "Lumayan lah."
    r "Sekarang aku harus menyiapkan api unggun."
    #SFX: *Tak* *Tak* (suara mukul kayu?)
    r "Berhasil!" with vpunch
    r "*Kraus! Kraus!*"
    "*Grrrr..*"
    r "Lagi-lagi ada monster. Aku harus segera pergi dari sini."


    #BG Hutan 2, day with dissolve 1s
    r "Hawanya mengerikan sekali, sepertinya banyak monster yang jauh lebih mengerikan di sana."
    #show item buku catatan 1
    show vignette with dissolve
    pause 0.5
    show old_book with dissolve:
        align (0.5, 0.4)
        zoom 0.1
    pause 0.5
    r "Tetapi di selipan buku catatan ini, semakin seram wilayahnya maka barang-barang yang tersedia di dalamnya juga semakin bagus."
    #item buku catatan 1 out
    hide old_book with dissolve
    pause 0.5
    hide vignette with dissolve
    pause 0.5

    menu:
        "Jelajahi hutan.":
            r "Semoga ada sesuatu yang berguna di sana."
            r "(Tempat ini kenapa berkabut sekali...)"
            r "(!!!)" with vpunch
            "Aku melihat sesuatu yang berkilauan. Benda apa itu?"
            #show item pisau belati berwarna ungu
            show vignette with dissolve
            pause 0.5
            show dagger_ungu_jeffry with dissolve:
                align (0.5, 0.4)
                zoom 0.3
            pause 0.5
            r "Wow, ini pisau belati? Keren sekali."
            hide dagger_ungu_jeffry with dissolve
            pause 0.5
            hide vignette with dissolve
            pause 0.5
            #item pisau belati berwarna ungu out
            scene r2_1_wolf_remil_1 with fade
            #CG serigala dengan bulu yang dihiasi kristal berdiri di belakang Remil 1 with fade in 0,5s
            "*Grrrr*"
            "Rauman dari serigala itu membuat tubuhku terguncang dan tanpa sengaja tangan kananku melepaskan pisau yang barusan aku pungut."
            r "Pisaunya!!"
            #*Roarrr*
            "Serigala itu melompat ke arah pisau itu terjatuh. Seolah untuk mendapatkan pisau itu, aku harus melawannya."
            r "Sial, aku tidak akan bisa melawannya sendiri. Aku harus pergi dari sini!"
            #*Roarrr*

            #BG Hutan, day with fade in 1s
            scene hutan with fade
            r "Huft, nyaris saja. Padahal pisau belati itu keren sekali."

        "Kembali":
            r "Lupakan saja. Sepertinya aku belum cukup kuat untuk memasuki area itu."

    r " Aku harus lebih gigih latihan bertarung."

    #CHAPTER 1 END
    #(Black Screen. With Dissolve 1sec)
    #CHAPTER 2 UWOOOOOOOOOOOH
    scene black with Dissolve (2)
    pause 2
    scene chp_2 with Dissolve (2)
    pause 4
    scene black with Dissolve (2)
    pause 2

    scene hutan_night with Dissolve (2)
    #BG Hutan, night with dissolve in 1s
    r "(Sepertinya malam ini aku akan tidur di atas pohon. Semoga tidak ada ular atau hewan berbahaya lainnya.)"
    "Aku pun memanjat pohon yang tertinggi."
    n "{b}AAAAAA!!{/b}" with vpunch
    r "(Suara teriakan siapa itu?!)"
    "Aku melompat turun dari pohon, lalu bergegas mendekati sumber suara."
    #SFX: “Drap Drap” (suara langkah kaki cepat)
    play sound sfx_drap3x
    pause 0.5
    show vignette with dissolve
    pause 0.5
    show beruang_ungu with dissolve:
        align (0.5, 0.4)
        zoom 0.15
    pause 0.5
    #show beruang berwarna ungu
    r "(Suara teriakan tadi.. Berasal dari beruang itu?!)"
    "Beruang itu terus meraung kesakitan karena jebakan yang melukainya."
    hide beruang_ungu with dissolve
    pause 0.5
    hide vignette with dissolve
    pause 0.5
    #beruang berwarna ungu out
    play sound sfx_anakpanahlewat
    #SFX: *Ctak* *Ctak* (suara panah)
    "Sebuah anak panah pun meluncur dan menusuk bagian dadanya, suara teriakan dari beruang itu semakin keras hingga bergema."

    show jeffrey_sad at enter
    #Sad M in Jeffrey
    j "Hah.. sepertinya racun yang aku oles di ujung anak panah itu kurang kuat."
    #Happy M Jeffrey
    show jeffrey_happy as jeffrey_sad
    j "Oh, hai Remil, kita bertemu lagi!"
    ber "{b}Roaarr{/b}" with vpunch
    "Beruang tersebut meraung ke arah kami. Karena kakinya terkena jebakan, beruang tersebut terus mencoba untuk melepaskan kakinya menggunakan cakar tajamnya."
    j "sepertinya beruang itu sedang ingin melepaskan dirinya."
    j "Apa yang bisa kamu lakukan Remil?"

    menu:
        "Atur strategi":
            #show beruang ungu
            r "Biar aku yang urus, kamu tarik perhatian beruang tersebut dengan panah kamu."
            #Serious M Jeffrey
            show jeffrey_serious as jeffrey_sad at sigh
            j "Baiklah, aku akan mencoba menarik perhatiannya dari atas pohon dengan panahku."
            #Jeffrey out
            hide jeffrey_sad
            "Beruang tersebut mulai menyerang mereka, Aku dan Jeffrey akan membalas serangan tersebut."
            "Aku mulai menggores tubuh beruang tersebut bersamaan dengan serangan panah beracun dari jeffrey ke arah wajah beruang tersebut."
            "Karena beruang tersebut dalam kondisi yang hampir dikalahkan, Aku melihat sedikit celah dan dengan penuh percaya diri aku menyerang mata si beruang dari sisi kiri."
            "Namun tiba tiba serangan spontan dariku berhasil dipatahkan oleh beruang tersebut."
            #beruang ungu out
            #SFX: *Bruk!* (suara badan jatuh ke permukaan kasar)
            play sound sfx_bodydrop
            r "AAKH!!"
            r "(Serangannya cepat sekali!)"
            #show beruang ungu
            #*AAAAAA!!!*
            "Beruang tersebut menggunakan cakarnya yang tajam dan berhasil melepaskan dirinya dari jebakan yang menancap pada kakinya."
            #Angry M in Jeffrey
            show jeffrey_angry2 at enter
            j "Tidak akan kubiarkan!!"
            "Jeffrey melepaskan anak panah yang dibidiknya ke arah mata beruang dan berhasil membuat beruang kehilangan arah serangan."
            ber "{b}Roaarr{/b}" with vpunch
            r "(!!!)" with vpunch
            "Teriakan beruang itu membuat kesadaranku kembali."
            j "Serang lehernya!"
            hide jeffrey_angry2
            #Jeffrey out
            "Dengan cepat aku bergegas mengambil pisau yang terlempar dan menusukan pisau tersebut ke leher beruang."
            ber "{b}{cps=10}Roaarr-{w=0.3}{nw}{/b}"
            #beruang ungu out
            "Teriakan beruang tersendat. Seketika beruang tumbang serta kehilangan penglihatannya."
            #BG hutan, night
            "Aku dan Jeffrey akhirnya menarik nafas masing-masing sehabis pertarungan selesai. Kami pun melihat satu sama lain dengan nafas lega."
            r "(Seketika aku merasa lebih aman dengan Jeffrey.)"
            r "(Haruskah aku mempercayainya?)"
            show jeffrey_happy at enter
            #Happy M in Jeffrey
            j "Hey gerakan bagus yang kau lakukan tadi."
            r "..Panahanmu juga hebat."
            show jeffrey_normal as jeffrey_happy
            #Normal M Jeffrey
            j "Hmm.. bagaimana jika malam ini kamu ikut ke tempatku?"
            r "Ah, tidak usah. Aku tidak mau berjalan ke tempat lebih jauh."
            show jeffrey_normal_manipulative as jeffrey_happy
            #Normal manipulative M Jeffrey
            j "Oh tidak, tempatku cukup dekat dari sini dan kamu bisa percaya denganku bahwa tidak ada orang disana. Lagipula aku juga tidak suka banyak orang."
            r "Baiklah aku akan ikut denganmu."
            show jeffrey_laugh as jeffrey_happy
            #Laugh M Jeffrey
            j "Bagus! Ada beberapa hasil buruanku juga di sana, jadi kita bisa. menghabiskannya malam ini. Tapi sebelum itu, izinkan aku untuk mengobati kepalamu dulu."
            hide jeffrey_happy
            pause 0.5
            scene black with Dissolve (2)
            pause 1
            #Jeffrey out

        "Serang beruang itu sendiri.":
            r "Aku akan menyerangnya sendiri."
            #Surprise M Jeffrey
            show jeffrey_surprised as jeffrey_sad
            j "Kamu yakin?"
            j "REMIL AWAS!!" with vpunch
            hide jeffrey_sad
            play sound sfx_bodydrop
            #Jeffrey out
            #SFX: *Bruk!* (suara badan jatuh ke permukaan kasar)
            #show beruang ungu
            show vignette with dissolve
            pause 0.5
            show beruang_ungu with dissolve:
                align (0.5, 0.4)
                zoom 0.15
            pause 0.5
            "Beruang itu menghantamku dengan keras hingga membuatku terpental ke pohon. Aku bisa mendengar cakaran beruang itu yang sangat tajam hingga berhasil melepaskan dirinya dari jebakan itu."
            hide beruang_ungu with dissolve
            pause 0.5
            hide vignette with dissolve
            pause 0.5
            #beruang ungu out
            show jeffrey_angry2 at enter
            #Angry M in Jeffrey
            j "Sial.."
            hide jeffrey_angry2
            #Jeffrey out

            scene black with Dissolve (2)
            #Black screen
            r "(Kepalaku sakit..)"
            j "Shh.. Jangan membuka mata dan bergerak terlalu banyak dahulu. Kepalamu terbentur cukup parah."
            r "Jeffrey..? Kenapa kau menyelamatkanku?"
            j "Bila ada orang terluka dan tidak sadar, siapa yang tidak mau lompat menyelamatkan mereka?"
            r "Kau benar...Terima kasih."
            j "Hehe, sama-sama."
            r "Oh iya bagaimana dengan beruang tadi?"
            j "Ah sudah ku tangani. Ada beberapa hasil buruan aku di tenda ini, diantaranya ada daging segar. Kamu mau? Jika tidak, Aku ingin memakan semuanya malam ini."
            r "Jika boleh, aku tidak akan menolak."
            j "Nah selesai! Kamu boleh membuka matamu sekarang."

    #CG Remil (dengan perban di kepalanya) duduk di samping perapian dengan Jeffrey. Di sekitar perapian banyak daging hasil buruan dan beberapa buah-buahan.
    #*Kraus* *Kraus*
    scene r2_2_rem_jef with Dissolve (2)
    r "Jeffrey, aku ingin bertanya sesuatu."
    j "*Kraus* Hmm?"
    r "Kamu kenapa membangun tenda disini? Bukannya kamu seharusnya bersama kelompok Alios?"
    j "..."
    r "Uhh.. Kamu tidak bisa menjawabnya ya..?"
    j "Tidak, aku diam karena sedang mengunyah tadi. Kita memang sedang berpencar dan kebetulan saja aku bertemu denganmu."
    r "Tapi aku sudah bukan bagian dari kelompok Alios lagi."
    j "Soal itu aku tidak peduli. Lebih seru bertarung denganmu daripada si Alios itu."
    j "Ini buah berinya tidak mau kamu makan?"
    "Jeffrey mengambil beberapa buah beri dan hendak memakannya."
    "Buah beri itu terlihat seperti buah beri beracun yang hampir aku makan tadi, aku pun menepis tangan Jeffrey hingga membuatnya menjatuhkan buah itu."
    scene hutan_night with dissolve
    show jeffrey_sad at enter
    #BG hutan, night with dissolve in  0,5s
    #Sad M in Jeffrey
    #show tiga buah beri terjatuh di tanah (menjadi kotor)
    show vignette with dissolve
    pause 0.5
    show berry with dissolve:
        align (0.5, 0.4)
        zoom 0.1
    pause 0.5
    j "Tidaakk, buah beriku!!"
    hide berry with dissolve
    pause 0.5
    hide vignette with dissolve
    pause 0.5
    #tiga buah beri terjatuh di tanah (menjadi kotor) out
    r "Itu beracun."
    show jeffrey_surprised as jeffrey_sad
    #Surprise M Jeffrey
    j "Dari mana kamu tahu kalau itu beracun?!"

    menu:
        "Katakan itu hanya instingmu saja":
            r "Itu hanya naluriku saja."
            #Normal manipulative M Jeffrey
            show jeffrey_normal_manipulative as jeffrey_sad
            j "Oh begitu.."
            #Laugh M Jeffrey
            show jeffrey_laugh as jeffrey_sad
            j "Huwah, tidak kebayang kalau di sini tidak ada kamu dan aku malah langsung memakan beri itu. Terima kasih banyak, ya!"
            "Tanpa kusadari aku tersenyum."
            r "Omong-omong, aku waktu itu menemukan gubuk tua dan aku ingin pergi kesana lagi besok pagi. Sekarang sudah larut, boleh aku tidur di sini?"
            #Normal M Jeffrey
            show jeffrey_normal as jeffrey_sad
            j "O-Oh iya, tentu saja. Selamat malam."
            r "Malam..."
            hide jeffrey_sad
            #Jeffrey out

            scene hutan_night with fade
            show jeffrey_sad at enter
            #BG hutan, night with fade in 1s
            #Sad M in Jeffrey
            j "Huaa.. Aku tidak bisa tidur."
            show vignette with dissolve
            pause 0.5
            show old_book with dissolve:
                align (0.5, 0.4)
                zoom 0.1
            pause 0.5
            #show item buku catatan 1
            #Serious M Jeffrey
            show jeffrey_serious as jeffrey_sad
            j "Eh, buku siapa ini di sebelah Remil?"
            j "..."
            j "Dia mencatat semua ini?!"
            j "..atau jika bukan, siapa yang menulis buku ini?"
            j "Apa Remil tahu lebih banyak dariku?"
            hide old_book with dissolve
            pause 0.5
            hide vignette with dissolve
            pause 0.5
            hide jeffrey_sad
            #item buku catatan 1 out
            #Jeffrey out

        "Beri tahu mengenai catatan itu":
            #show item buku catatan 1
            show vignette with dissolve
            pause 0.5
            show old_book with dissolve:
                align (0.5, 0.4)
                zoom 0.1
            pause 0.5
            r "Di buku ini tertulis bahwa buah yang kamu petik barusan beracun."
            show jeffrey_surprised as jeffrey_sad
            #Surprise M Jeffrey
            j "Hah, buku apa itu?"
            r "Aku menemukan buku ini di suatu gubuk yang tua, di isi buku ini ada beberapa informasi mengenai buah-buahan dan tanaman di sekitar hutan ini."
            #item buku catatan 1 out
            hide old_book with dissolve
            pause 0.5
            hide vignette with dissolve
            pause 0.5
            show jeffrey_normal as jeffrey_sad
            #Normal M Jeffrey
            j "Hmm.."
            j "Aneh ya?"
            r "Eh?"
            show jeffrey_serious as jeffrey_sad
            #Serious M Jeffrey
            j "Tidak mungkin buku dengan tulisan tangan seperti ini ada dengan sendirinya kan? Pasti ada seseorang yang menulisnya."
            #Happy M Jeffrey
            show jeffrey_happy as jeffrey_sad
            j "Hey Remil, bisa kah kamu memperlihatkan kepadaku gubuk tua itu?"
            r "(Dia bersemangat sekali..)"
            r "Boleh, mungkin kita bisa kesana besok pagi. Kita harus berhati-hati karena ada monster yang cukup seram di sana."
            #Normal M Jeffrey
            show jeffrey_normal as jeffrey_sad
            j "Ah.. baiklah selamat malam."
            r "Malam."
            hide jeffrey_sad
            #Jeffrey out

    scene hutan with fade
    show jeffrey_happy at enter
    #BG hutan, day with fade in 1s
    #Happy M in Jeffrey
    j "Remil, ayo bangun! Kamu bilang pagi ini akan menunjukan dimana gubuk tua itu kan?"
    r "Hmngh? Oh… iya benar."
    hide jeffrey_happy
    #Jeffrey out
    "Kami pun bersiap dengan gear masing-masing untuk menelusuri hutan tersebut lagi."

    #CHAPTER 2 END
    #(Black Screen. With Dissolve 1sec)
    #CHAPTER 3
    #BG luar gubuk, day with dissolve in 1s
    scene black with Dissolve (2)
    pause 2
    scene chp_3 with Dissolve (2)
    pause 4
    scene black with Dissolve (2)
    pause 2
    scene gubuk_luar_day
    r "Hmm.. gubuknya tidak terlihat seperti yang kulihat sebelumnya.."
    show jeffrey_surprised at enter
    #Surprise M in Jeffrey
    j "Maksudmu ini… gubuk yang salah?!"
    r "Mungkin… aku lupa bentuknya."
    j "Hahh?!"
    r "Ayo kita coba masuk."
    hide jeffrey_surprised
    #Jeffrey out
    pause 0.5

    scene dalam_gubuk_api_mati with dissolve
    show jeffrey_happy at enter
    #BG dalam gubuk, day with dissolve in 1s
    #Happy M in Jeffrey
    j "Wah, gubuk ini lebih nyaman dibanding tenda. Tunggu, apa itu?"
    show vignette with dissolve
    pause 0.5
    show buku_2 with dissolve:
        align (0.5, 0.4)
        zoom 0.1
    pause 0.5
    #show item buku catatan 2
    r "(Berbeda dari buku yang aku temukan sebelumnya, di buku ini isinya mengenai monster-monster dan kelemahannya.)"
    hide buku_2 with dissolve
    pause 0.5
    hide vignette with dissolve
    pause 0.5
    #item buku catatan 2 out
    show jeffrey_laugh as jeffrey_happy
    #Laugh M Jeffrey
    j "Dengan buku ini kita akan semakin mudah untuk membasmi monster di sini. Benar kan? Ya kan?"
    r "Benar."
    r "..."
    #Normal M Jeffrey
    show jeffrey_normal as jeffrey_happy
    j "..."
    show jeffrey_normal_manipulative as jeffrey_happy
    #Normal manipulative M Jeffrey
    j "Sekarang bagaimana kalau kita berpencar? Aku akan melihat-lihat luar dan kamu yang menyelidiki area dalam."
    r "Sepertinya itu ide bagus."
    hide jeffrey_happy
    #Jeffrey out
    "Jeffrey pun keluar dari gubuk, kini aku sendiri yang berada dalam gubuk ini."
    r "(Seperti ada sesuatu...)"
    r "(!!!)" with vpunch
    r "(Ini..)"
    #show ukiran kasar di tembok kayu
    show vignette with dissolve
    pause 0.5
    show ukiran_kayu with dissolve:
        align (0.5, 0.4)
        zoom 0.3
    pause 0.5
    r "(Apa maksud dari gambar ini?!)"
    #ukiran kasar di tembok kayu out
    r "(Ada tulisan di bawahnya, tetapi sebagian huruf dan katanya tercoret.)"
    "S.. r... orang n.. g... u... dan ..n c... s.. g.. l."
    r "(...Gimana cara membacanya?!)"
    "Layar dan tali penghubung."
    r "..."
    r "(Maksudnya?)"
    r "(Aku harus memberitahu Jeffrey tentang ukiran dan tulisan ini.)"

    play sound sfx_drap3x
    scene gubuk_luar_day with dissolve
    show elena_surprise at enterl
    show jeffrey_normal_manipulative at enterr
    #SFX: “Drap Drap” (suara langkah kaki cepat)
    #BG luar gubuk, day with dissolve in 1s
    #Surprise L in Elena
    #Normal manipulative R in Jeffrey
    e "Itu Remil!"
    r "Elena? Apa yang kamu lakukan disini?"
    #Nervous L Elena
    show elena_nervous as elena_surprise
    r "Anu, Remil.. Jeffrey.."
    #Normal R Jeffrey
    show jeffrey_normal as jeffrey_normal_manipulative
    j "Hm?"
    e "Izinkan aku bergabung dengan kalian!"
    r "Eh?"
    #Normal R Jeffrey
    j "Elena maaf.."
    show jeffrey_normal_manipulative as jeffrey_normal_manipulative
    #Normal manipulative R Jeffrey
    j "Aku tidak mau terlibat lagi dengan kelompok Alios dan sepertinya Alios menganggapmu berguna."
    j "Selain itu, aku dan Remil berpetualang bersama karena kita cocok, bagiku tidak pantas untuk disebut rombongan."
    r "(Jeffrey..)"
    #Surprise Elena & Jeffrey
    show elena_surprise as elena_surprise
    show jeffrey_surprised as jeffrey_normal_manipulative
    al "Elena!! Kamu dimana?!"
    j "Sepertinya itu suara Alios. Aku tidak ingin dia melihatku.. Remil, ayo kita lari."
    "Jeffrey menarik tanganku dan membawaku ke suatu tempat."
    #Elena & Jeffrey out

    scene hutan with fade
    show jeffrey_normal at enter
    #BG hutan 2 with fade in 1s
    #Normal M in Jeffrey
    j "Huft.. hampir saja."
    show jeffrey_normal as jeffrey_normal at m4
    show elena_nervous at enterl
    #Nervous L in Elena
    #Jeffrey move to R
    e "..."
    show jeffrey_surprised as jeffrey_normal
    #Surprise R Jeffrey
    j "Loh, Elena kamu disini?- Ah sudahlah."
    show jeffrey_happy as jeffrey_normal
    #Happy R Jeffrey
    j "Ngomong-ngomong aku baru lihat tempat ini, hawanya berbeda sekali ya."
    r "(Tempat ini..)"
    e "Ada apa, Remil?"
    r "Perasaanku tidak enak."
    #Happy R Jeffrey
    j "Hmm~ Karena hutan ini berkabut ya? Tapi tenang saja, kita kan bertiga disini!"
    j "Kamu bisa menggunakan sihir kan, Elena?"
    #Happy L Elena
    show elena_happy as elena_nervous
    e "Iya!"
    #Happy R Jeffrey
    j "Bagus bagus, aku dan Elena yang menyerang dari jauh dan Remil akan menjadi penyerang jarak dekat."
    #Elena & Jeffrey out
    hide jeffrey_normal
    hide elena_nervous
    show vignette with dissolve
    pause 0.5
    show dagger_hijau with dissolve:
        align (0.5, 0.4)
        zoom 0.1
    pause 0.5
    #show item pisau belati berwarna hijau with dissolve
    r "(Pisau itu..)"
    r "Jeffrey, Elena, aku mau mengambil pisau itu. Kalian tolong berjaga ya, aku takut kalau nanti akan ada monster yang menyerangku."
    #item pisau belati berwarna hijau out
    hide dagger_hijau with dissolve
    pause 0.5
    hide vignette with dissolve
    pause 0.5
    scene r2_1_wolf_remil_2 with fade
    #CG serigala dengan bulu yang dihiasi kristal berdiri di belakang Remil 2 with fade in 0,5s
    "*Grrrr*"
    "*Roarrr*"
    e "REMIL AWAS!!"
    #CG Elena, Jeffrey, dan Remil menyerang serigala itu with dissolve in 0,5s
    scene r2_3_remil_jeff_elena_wolf with dissolve
    e "Remil, kau tidak apa-apa?!"
    r "Aku tidak apa-apa, terima kasih Jeffrey sudah menarikku."
    j "Nanti saja, sekarang kita harus berhadapan dengan serigala ini."
    play sound sfx_anakpanahlewat
    #SFX: “Ctak Ctak” (suara anak panah)
    "Jeffrey melayangkan anak panah ke tubuh serigala itu, sayangnya anak panah tersebut tidak melukai serigala. Begitu juga dengan serangan sihir dari Elena."
    j "Serigala ini kuat sekali!"
    e "Sihirku juga tidak mempan!"
    r "Elena, kamu bisa membuat tameng sihir?"
    e "Bisa!"
    r "Jeffrey, kamu pancing serigala ini dan begitu aku melihat celah, aku akan menyerangnya dengan pisau ini."
    "Dengan gesit Jeffrey mendekat ke serigala itu agar dirinya menjadi umpan. Melihat adanya celah, aku menebas leher serigala dan serigala itu pun langsung tumbang."


    #BG hutan 2 with fade in 1s
    #Surprise L in Elena
    #Surprise R in Jeffrey
    scene hutan with fade
    show elena_surprise at enterl
    show jeffrey_surprised at enterr
    r "(!!!)" with vpunch
    show elena_surprise at talk
    e "Wow.. hebat sekali."
    show elena_surprise at notalk
    #Happy R Jeffrey
    show jeffrey_happy as jeffrey_surprised at talk
    j "Pisau belati itu pasti sangat tajam. Kau baru saja mengalahkan serigala itu dengan sekali serangan!"
    #Sad R Jeffrey
    show jeffrey_sad as jeffrey_surprised
    j "Semoga ada busur dan anak panah yang bagus di sekitar sini. Aku merasa tidak berguna karena seranganku tadi tidak ada apa-apanya."
    #Normal L Elena
    show jeffrey_sad as jeffrey_surprised at notalk
    show elena_normal as elena_surprise at talk
    e "Hei ayolah, jangan berpikir seperti itu. Kita akan berjuang bersama disini."
    show elena_normal as elena_surprise at notalk
    r "Aku melihat gua diujung sana. Mau coba masuk ke dalamnya?"
    #Happy Jeffrey & Elena
    show elena_happy as elena_surprise
    show jeffrey_happy as jeffrey_surprised
    jne "Ayo."
    #Jeffrey & Elena out
    hide elena_surprise
    hide jeffrey_surprised
    pause 0.5

    show goa1 with dissolve
    #BG gua 1 with dissolve
    #Normal M in Jeffrey
    show jeffrey_normal at enter
    j "Tidak ada apa-apa, ayo kita telusuri lebih dalam."
    #SFX: “Drap Drap Drap” (suara langkah kaki berjalan)
    play sound sfx_drap3x
    show jeffrey_sad as jeffrey_normal at m2
    show elena_nervous at enterr
    #Jeffrey move to L
    #Sad L Jeffrey
    j "Kepalaku kok tiba-tiba pusing ya.."
    #Nervous R in Elena
    e "Aku juga.."
    r "(Aneh.. Penglihatanku juga tiba-tiba kabur.)"
    hide jeffrey_normal with fade
    #Jeffrey out with fade
    "{i}Bruk{/i}"
    #Surprise L Elena
    show elena_surprise as elena_nervous
    e "Jeffrey!!"
    "{i}Bruk{/i}"
    hide elena_nervous with fade
    pause 0.5
    #Elena out with fade

    #CHAPTER 3 END
    #black screen in 2s
    scene black with Dissolve (2)
    pause 2
    scene chp_4 with Dissolve (2)
    pause 4
    scene black with Dissolve (2)
    pause 2
    #CHAPTER 4
    #Scene di rumah Kai, day with dissolve in 1s
    scene dalam_gubuk_terang with dissolve
    r "Ugh.."
    #Normal M in Kai
    show kai_normal at enter
    n "Kamu sudah sadar?"
    r "...Kamu siapa?"
    n "Aku penghuni rumah yang berada di desa kosong ini."
    r "Desa?"
    r "Di mana teman-temanku?"
    k "Teman-temanmu?"
    r "Iya, seingat aku terakhir kali kita berada di gua."
    r "Tetapi entah apa yang terjadi, kami sama-sama merasa pusing dan mungkin kami semua pingsan di dalam gua itu."
    #Serious M Kai
    show kai_normal as kai_normal at sigh
    n "Gua? hmm.."
    n "Aku menemukanmu pingsan di hutan tidak jauh dari desa ini."
    n "-dan kamu sendirian."
    r " (Apa?!)"
    n "..."
    show kai_normal as kai_normal at normal
    #Normal M Kai
    n "Mungkin kamu bisa berkeliling sekitar desa untuk menenangkan pikiranmu."
    r "Baiklah.."
    r "Ah iya, sebelum itu terima kasih karena telah menolongku. Boleh tahu namamu siapa?"
    #Happy M Kai
    show kai_smile as kai_normal
    k "Kai."
    #Kai out
    hide kai_normal
    pause 0.5

    #BG desa Kai, day with dissolve in 1s (disini memakai versi yang tidak hancur)
    scene desa_kai with dissolve
    r "(Apa yang barusan terjadi..)"
    r "(Aku bahkan tidak tahu di mana arah menuju tempat ini.)"
    "Aku merogoh-rogoh saku dan tas kecilku."
    #show item pisau belati berwarna hijau in 1s
    #item pisau belati berwarna hijau out
    #show item buku catatan 1 in 1s
    #item buku catatan 1 out
    show vignette with dissolve
    pause 0.5
    show dagger_hijau with dissolve:
        align (0.5, 0.4)
        zoom 0.1
    pause 1
    hide dagger_hijau with dissolve
    pause 0.5
    show old_book with dissolve:
        align (0.5, 0.4)
        zoom 0.2
    pause 1
    hide old_book with dissolve
    pause 0.5
    hide vignette with dissolve
    pause 0.5
    r "Syukurlah dua barang itu masih ada."
    show kai_normal at enter
    #Normal M in Kai
    k "Permisi."
    k "Siapa namamu?"
    r "Eh, namaku Remil."
    k "Kamu mau mencari teman-temanmu kan? Ini."
    #show item peta
    show vignette with dissolve
    pause 0.5
    show map with dissolve:
        align (0.5, 0.4)
        zoom 0.3
    pause 0.5
    #Serious M Kai
    k "Agar kamu tidak nyasar. Tempat ini adalah tempat teraman, kamu bisa beristirahat disana. Saya rasa kamu adalah orang baik."
    #item peta out
    hide map with dissolve
    pause 0.5
    hide vignette with dissolve
    pause 0.5
    "Peta ini.. Tulisan tangannya terasa mirip"
    #show item buku catatan 1
    show vignette with dissolve
    pause 0.5
    show old_book with dissolve:
        align (0.5, 0.4)
        zoom 0.1
    pause 0.5
    r "Tunggu, kamu yang menulis buku ini?"
    #Surprise M Kai
    k "(!!!)" with vpunch
    #Happy M Kai
    show kai_laugh as kai_normal
    k "Kamu menemukannya ya. Benar, aku yang menulis buku itu."
    #item buku catatan 1 out
    hide old_book with dissolve
    pause 0.5
    hide vignette with dissolve
    pause 0.5
    r "Buku ini berguna sekali. Hampir saja aku dan temanku memakan buah beri beracun."
    r "Kalau begitu, buku ini akan aku kembalikan."
    #Normal M Kai
    show kai_normal as kai_normal
    k "Tidak usah, aku memang sengaja meninggalkan buku itu untuk membantu."
    k "Lagipula aku tidak butuh buku itu karena aku sudah hafal setiap tanaman dan monster di hutan ini."
    r "(Orang ini sepertinya sudah lama berada di sini.)"
    #show item peta
    hide map with dissolve
    pause 0.5
    hide vignette with dissolve
    pause 0.5
    r "(Di peta ini sama sekali tidak ada petunjuk keluar hutan, bahkan ada gurun disini?!)"
    #item peta out
    hide map with dissolve
    pause 0.5
    hide vignette with dissolve
    pause 0.5
    r "(Setidaknya aku sudah menemukan tempat yang aman disini. Kai meskipun terlihat dingin, namun dia baik sekali.)"
    r "(Sekarang aku harus mencari Jeffrey dan Elena.)"
    r "Terima kasih, Kai. Aku permisi dulu."
    k "Berhati-hatilah."
    #Kai out
    hide kai_normal
    pause 0.5

    scene lembah_day with dissolve
    #CG lembah, day with dissolve in 1s
    r "(Aku belum pernah ke tempat ini sebelumnya.)"
    r "Sepertinya tidak ada apa-apa disini, dari tadi juga aku hanya bertemu dengan monster-monster kecil."
    #SFX: *Drap* *Drap* (suara langkah kaki terburu-buru)
    play sound sfx_drap3x
    r "(!!!)" with vpunch
    r "AARGH!!"
    r "(Mayat ini.. Darahnya masih segar, kemungkinan dia baru saja dibunuh sebelum aku sampai ke tempat ini.)"
    r "(Tunggu, dia bukannya salah satu anggota kelompok Alios ya?)"
    #show item pisau belati berwarna hijau
    show vignette with dissolve
    pause 0.5
    show dagger_hijau with dissolve:
        align (0.5, 0.4)
        zoom 0.1
    pause 0.5
    "Aku mengeluarkan pisau belati dari saku untuk berjaga-jaga."
    #item pisau belati berwarna hijau out
    hide dagger_hijau with dissolve
    pause 0.5
    hide vignette with dissolve
    pause 0.5
    r "(Aku tidak tahu dia dibunuh oleh manusia atau monster. Tidak aman jika aku diam disini terlalu lama, aku harus segera pergi.)"
    #SFX: *Drap* *Drap* (suara langkah kaki terburu-buru)
    play sound sfx_drap3x

    scene padang_gurun_day with fade
    #BG gurun, day with fade in 1s
    r "Hah.. aku sudah berlari cukup jauh."
    n "Tolong!!"
    r "Siapa disana?!"
    "Aku bergegas menuju sumber suara."
    show cherry_serius at enter
    #Serious M in Cherry
    c "I-Ini kak Remil kan?"
    r "Iya.. Ada apa?"
    #Angry M Cherry
    show cherry_angry as cherry_serius
    c "Kak Alios menggila! Dia hampir membunuh semua anggota kelompoknya!"
    r "(Jangan-jangan mayat yang tadi aku temukan itu..)"
    r "Kamu tahu di mana keberadaan Alios sekarang?"
    #Serious M Cherry
    show cherry_serius as cherry_serius
    c "Tidak, terakhir kali kita berada di tengah gurun dan disitu ia mulai menggila."
    c "Cherry hampir diserang dan untung saja Cherry bisa bersembunyi."
    #Sad M Cherry
    show cherry_sadpout as cherry_serius
    c "Sudah seharian Cherry tinggal disini, sekarang cadangan makanan dan minuman Cherry habis."
    r "Baiklah, kalau begitu kamu ikut saja denganku."
    #Angry M Cherry
    show cherry_angry as cherry_serius
    c "Mana bisa?! Kak Remil kan tidak sekuat kak Alios."
    r "...Trus kamu maunya apa?"
    c "..."
    #Bored M Cherry
    show cherry_bored as cherry_serius
    c "Baiklah, Cherry ikut."
    #Cherry out
    hide cherry_serius
    "Aku dan Cherry pun berkeliling gurun."
    #Normal M in Cherry
    show cherry_normal at enter
    c "Memangnya kak Remil mencari apa disini?"
    r "Entahlah."
    #Angry M Cherry
    show cherry_angry as cherry_normal
    c "Terus ngapain kita dari tadi?! Ayolah mending kita balik saja. Disini panas, Cherry sudah tidak kuat!"
    r "(Aku merasa di tempat ini ada sesuatu.)"
    r "Tadi Alios tiba-tiba menggila di tempat ini kan?"
    r "Aku penasaran apa yang membuatnya menggila."
    #Normal M Cherry
    show cherry_normal as cherry_normal
    c "Oh, ikut Cherry."
    #Cherry out
    hide cherry_normal


    #BG tengah gurun, day with dissolve in 1s
    #Normal M in Cherry
    show cherry_normal at enter
    c "Disini."
    #Sad M Cherry
    show cherry_sadpout as cherry_normal
    c "Aku juga.. terpisah dengan Elena di tempat ini."
    r "Tunggu, kamu sebelumnya bersama Elena?"
    #Serious M Cherry
    show cherry_serius as cherry_normal
    c "Iya, lalu aku bersembunyi sendiri."
    c "Elena juga menjadi aneh semenjak dia hilang seharian, tatapannya selalu kosong."
    r "..."
    r "(Sepertinya kita bertiga memang terpisah setelah pingsan dari goa itu. Tapi siapa yang memisahkan kita dan ada apa dengan goa itu?)"
    "Aku memperhatikan tiap puing-puing di gurun itu."
    #show item bola kristal
    show vignette with dissolve
    pause 0.5
    show crystal_ball with dissolve:
        align (0.5, 0.4)
        zoom 0.1
    pause 0.5
    #Happy M Cherry
    show cherry_happy as cherry_normal
    c "Bola kristal itu cantik sekali! Cherry mau!"
    r "Hati-hati, sepertinya bola ini sedikit berbahaya. Kalau kamu suka, kamu bisa melihatnya saja."
    #Sad M Cherry
    show cherry_sadpout as cherry_normal
    c "Cih."
    r "(Bisa jadi bola kristal ini ada hubungannya dengan Alios yang tiba-tiba menggila. Lebih baik aku mengamankannya.)"
    #item bola kristal out
    #Bored M Cherry
    hide crystal_ball with dissolve
    pause 0.5
    hide vignette with dissolve
    pause 0.5
    show cherry_bored as cherry_normal
    c "Hei, kakak sudah menemukan yang kakak cari kan? Ayo kita kembali, Cherry tidak tahan berada di sini lama-lama."
    r "Baiklah."
    #Cherry out
    hide cherry_normal
    pause 0.5

    #BG plateau, dusk with dissolve in 1s
    scene plateau with dissolve
    show cherry_happy at enter
    #Happy M in Cherry
    c "Pisau belati kak Remil bagus dan kuat sekali, dengan pisau itu kakak bisa membunuh monster-monster yang menyerang kita selama perjalanan tadi."
    c "Dari mana kak Remil mendapatkan pisau itu? Cherry mau tongkat dan buku sihir yang baru!"
    r "(Hah.. Aku lelah.)"
    r "(Cherry sama sekali tidak membantu, padahal dia bisa saja meringankan pekerjaanku dengan menyihir monster-monster itu. Tetapi yang dia lakukan hanya meneriaki namaku dan malah membuatku sedikit pusing.)"
    #Angry M Cherry
    show cherry_angry as cherry_happy
    c "Hei jawab! Kak Remil kok sering mengabaikan Cherry sih."
    r "Ada hutan yang berkabut di sana. Aku menemukan pisau ini dari tempat itu."
    #Happy M Cherry
    show cherry_happy as cherry_happy
    c "Wah, hutan berkabut? Cherry mau kesana. Ayo temani Cherry!"
    r "Jangan sekarang, aku mau beristirahat."
    r "..."
    r "(Aku merasakan sesuatu yang aneh dalam diriku.)"
    r "(Kenapa semenjak aku terbangun di rumah Kai, aku belum merasakan lapar hingga sekarang?)"
    r "Cherry, apa kamu tidak lapar?"
    #Bored M Cherry
    show cherry_bored as cherry_happy
    c "Makanan disini aneh dan hambar, membuat nafsu makanku cepat hilang."
    c "Kalau kak Remil mau makan, makan saja sendiri. Cherry tidak lapar."
    n "REMILL!!!"
    r "Suara itu.. Jeffrey?!"
    show cherry_normal as cherry_happy at m4
    #Normal M Cherry move to R
    show jeffrey_sad at enterl
    #Sad L in Jeffrey
    j "Remil! Kamu disini rupanya!"
    #show tangan dan kaki Jeffrey terlihat luka dan diperban
    show vignette with dissolve
    pause 0.5
    show tangan_kaki_jeff_perban with dissolve:
        align (0.5, 0.4)
        zoom 0.1
    pause 0.5
    r "(Tangan dan kakinya terluka?)"
    #tangan dan kaki Jeffrey terlihat luka dan diperban out
    hide tangan_kaki_jeff_perban with dissolve
    pause 0.5
    hide vignette with dissolve
    pause 0.5
    show jeffrey_serious as jeffrey_sad at talk
    #Serious L Jeffrey
    j "(!!!)"
    j "Hati-hati."
    hide jeffrey_sad
    hide cherry_happy
    #Jeffrey & Cherry out
    #Smirk M in Alios
    show alios_smirk at enter
    al "Di sini kau rupanya, Remil."
    hide alios_smirk
    #Alios out
    show jeffrey_surprised at enter
    #Surprise M in Jeffrey
    j "Remil.. Sepertinya dia benar-benar membencimu."
    r "Apa? Kenapa bisa?!"
    #Jeffrey out
    hide jeffrey_surprised
    #Angry M in Alios
    show alios_angry3 at enter
    al "Semua ini gara-gara kau, kelompok aku terpecah belah. Kaulah yang mengacaukan kerajaanku!"
    r "(Kerajaan?)"
    al "Remil, ayo bertarung denganku."
    hide alios_angry3
    #Alios out
    #Surprise M in Cherry
    show cherry_surprised at enter
    c "Kak Remil hati-hati, Kakak tidak akan bisa melawannya seorang!"
    r "(Cherry benar, terlalu beresiko jika aku bertarung dengannya.)"
    r "(Aku harus kabur.)"
    hide cherry_surprised
    #Cherry out
    #Angry M in Alios
    show alios_angry2 at enter
    al "Kau tidak akan bisa kabur dariku!"
    "Tiba-tiba cahaya putih datang menyilaukan pandangan kami."
    hide alios_angry2
    #Alios out

    #CHAPTER 4 END
    #white screen in 1,5s
    #CHAPTER 5
    scene black with Dissolve (2)
    pause 2
    scene chp_5 with Dissolve (2)
    pause 4
    scene black with Dissolve (2)
    pause 2

    #BG rumah Kai, day with dissolve in 0,5s
    scene dalam_gubuk_terang with dissolve
    r "Ugh.."
    show jeffrey_happy at enterl
    show kai_normal at enterr
    pause 0.5
    #Happy L in Jeffrey
    #Normal R in Kai
    show jeffrey_happy as jeffrey_happy at talk
    j "Ah, Remil sudah sadar."
    show jeffrey_happy as jeffrey_happy at notalk
    #Serious R Kai
    show kai_normal as kai_normal at talk
    k "Anak itu sangat berbahaya. Jika saja aku terlambat menggunakan sihir untuk melerai kalian, kemungkinan terburuknya kalian semua bisa terbunuh olehnya."
    show kai_normal as kai_normal at notalk
    #Sad L Jeffrey
    show jeffrey_sad as jeffrey_happy at talk
    j "Huaa, terima kasih banyak tuan karena telah menyelamatkan kami."
    show jeffrey_sad as jeffrey_happy at notalk
    r "Tuan?"
    #Normal L Jeffrey
    show jeffrey_normal as jeffrey_happy at talk
    j "Dari gaya bicaranya kelihatan kalau dia jauh lebih tua dari kita."
    show jeffrey_normal as jeffrey_happy at notalk
    r "(Tapi tampangnya terlalu muda untuk disebut “tuan”...)"
    #Laugh R Kai
    show kai_laugh as kai_normal at talk
    k "Hahaha."
    show kai_normal as kai_normal
    #Normal R Kai
    k "Saya sudah menyiapkan makanan untuk kalian, silahkan dimakan."
    show kai_normal as kai_normal at notalk
    #Happy L Jeffrey
    show jeffrey_happy as jeffrey_happy at talk
    j "*Kraus* Ini enak sekali! Rasanya seperti sudah lama aku tidak memakan makanan berbumbu."
    show jeffrey_happy as jeffrey_happy at notalk
    r "(Benar, ini enak sekali.)"
    #Happy R Kai
    show kai_smile as kai_normal at talk
    k "Ada beberapa tumbuhan obat-obatan disini yang juga bisa dijadikan bumbu."
    #Normal L Jeffrey
    show kai_smile as kai_normal at notalk
    show jeffrey_normal as jeffrey_happy at talk
    j "*Kraus* Sepertinya tuan sudah lama tinggal di hutan ini ya? *Kraus*"
    show jeffrey_normal as jeffrey_happy at notalk
    r "(Telan dulu makananmu..)"
    #Normal R Kai
    show kai_normal as kai_normal at talk
    k "Benar, saya tinggal disini bertahun-tahun sebelum kalian."
    show kai_normal as kai_normal at notalk
    r "(!!!)" with vpunch
    r "(Bertahun-tahun?!)"
    #Normal manipulative L Jeffrey
    show jeffrey_normal_manipulative as jeffrey_happy at talk
    j "Tunggu, sepertinya kita kurang seorang."
    show jeffrey_normal_manipulative as jeffrey_happy at notalk
    r "Oh iya! Aku melupakan dia."
    show kai_normal as kai_normal at talk
    k "Anak berambut pirang itu ya?"
    k "Dia bangun lebih awal dibanding kalian, tetapi begitu melihatku dia malah memarahiku dengan memanggilku “Orang aneh” lalu kabur."
    show kai_normal as kai_normal at notalk
    r "Haah.."
    #Normal L Jeffrey
    show jeffrey_normal as jeffrey_happy at talk
    j "Lalu, bagaimana dengan Alios?"
    show jeffrey_normal as jeffrey_happy at notalk
    show kai_normal as kai_normal at talk
    k "Saya.. meninggalkannya di tempat tadi."
    show kai_normal as kai_normal at notalk
    show jeffrey_normal as jeffrey_happy at talk
    j "Eh Remil, apa habis ini kita cari Cherry saja ya? Masalahnya, dia kan tidak bisa bertarung."
    show jeffrey_normal as jeffrey_happy at notalk
    r "Boleh."

    #BG hutan, day with dissolve in 1s
    #Normal M in Jeffrey
    #show item busur berwarna silver dihiasi bebatuan biru
    scene hutan with dissolve
    show vignette with dissolve
    pause 0.5
    show item_busur with dissolve:
        align (0.5, 0.4)
        zoom 0.1
    pause 0.5
    r "Wah, dari mana kamu mendapatkan busur itu?"
    #Happy M Jeffrey
    j "Setelah aku sadar dari gua itu, tiba-tiba saja busur ini sudah ada di sebelahku."
    r "Wow.."
    #item busur berwarna silver dihiasi bebatuan biru out
    hide item_busur with dissolve
    pause 0.5
    hide vignette with dissolve
    pause 0.5
    show jeffrey_normal_manipulative at enter
    #Normal manipulative M Jeffrey
    j "Oh iya, memangnya kamu pergi ke mana setelah sadar dari gua itu?"
    j "Aku mengira kamu dibawa oleh monster, jadinya aku bertarung hingga ke dasar gua."
    r "Dasar gua? Lalu kamu menemukan apa saja disana?"
    show jeffrey_laugh at jeffrey_normal_manipulative
    #Laugh M Jeffrey
    j "Yup! Ternyata tidak sedalam yang aku kira dan berkat busur ini aku jadi bisa melawan monster yang tertutupi kristal itu."
    r "Jadi luka-luka di tangan dan kakimu karena monster-monster di gua itu?"
    #Normal M Jeffrey
    show jeffrey_normal at jeffrey_normal_manipulative
    j "Yah.. Bisa dikatakan begitu."
    #Happy M Jeffrey
    show jeffrey_happy at jeffrey_normal_manipulative
    j "Oh iya, lupakan soal tadi! Aku juga menemukan sesuatu di sana."
    j "Tapi sebelum aku memberitahukannya, bisa kamu berikan kepadaku bola kristal yang kamu temukan di gurun?"
    r "(Dari mana dia tahu?)"

    menu:
        "Berikan bola kristal":
            #show bola kristal
            show vignette with dissolve
            pause 0.5
            show crystal_ball with dissolve:
                align (0.5, 0.4)
                zoom 0.1
            pause 0.5
            r "Ini."
            j "Wah, keren!"
            r "Kamu tahu fungsi bola kristal ini?"
            #Normal manipulative M Jeffrey
            show jeffrey_normal_manipulative as jeffrey_normal_manipulative
            j "..Sedikit."
            #bola kristal out
            hide crystal_ball with dissolve
            pause 0.5
            hide vignette with dissolve
            pause 0.5
            show cherry_bored as cherry_normal
            r "Oh ya, Apa itu?"
            play sound sfx_treeshaking
            #SFX: *Srak* *Srak* (suara semak-semak)
            #Serious M Jeffrey
            show jeffrey_serious as jeffrey_normal_manipulative
            j "Remil, apa kamu mendengar sesuatu?"
            r "Sepertinya ada sesuatu di sana, entah itu manusia atau monster."
            #Sad M Jeffrey
            show jeffrey_sad as jeffrey_normal_manipulative
            j "Aku takut jika itu Alios, bagaimana kalau kita berpencar lalu bertemu di gubuk tua?"
            r "Sepertinya itu yang terbaik."
            #Jeffrey out
            hide jeffrey_normal_manipulative

        "Tolak":
            r "Maaf, aku tidak bisa."
            #Sad M Jeffrey
            show jeffrey_sad as jeffrey_normal_manipulative
            j "Kenapa? Aku pikir kamu sudah percaya padaku.."
            r "Ini seperti.. Harus aku yang menjaganya."
            #SFX: *Srak* *Srak* (suara semak-semak)
            #Serious M Jeffrey
            play sound sfx_treeshaking
            show jeffrey_serious as jeffrey_normal_manipulative
            j "Remil, apa kamu mendengar sesuatu?"
            r "Sepertinya ada sesuatu di sana, entah itu manusia atau monster."
            #Sad M Jeffrey
            show jeffrey_sad as jeffrey_normal_manipulative
            j "Aku takut jika itu Alios.."
            r "(Apa yang sudah Alios perbuat hingga Jeffrey ketakutan seperti itu?)"
            #Serious M Jeffrey
            show jeffrey_serious as jeffrey_normal_manipulative
            j "Remil, sepertinya kamu harus menitipkan bola itu kepadaku. Kamu menganggap itu barang penting kan?"
            j "Akan bahaya kalau Alios mengejarmu dan merampas bola kristal itu. Apalagi Alios sangat mengincarmu."
            r "Kamu benar, ini."
            #show item bola kristal
            #Normal manipulative M Jeffrey
            show jeffrey_normal_manipulative as jeffrey_normal_manipulative
            show vignette with dissolve
            pause 0.5
            show crystal_ball with dissolve:
                align (0.5, 0.4)
                zoom 0.1
            pause 0.5
            j "Baik, kita bertemu lagi di gubuk tua itu ya."
            #item bola kristal out
            #Jeffrey out

    #BG gubuk tua, day with fade in 1s
    scene gubuk_luar_day with fade
    r "Huft.. aku sudah sampai sini saja, tidak terasa."
    "Aku merogoh tas kecilku."
    r "Hah?! Petanya kok tidak ada?"
    r "...sepertinya peta itu terbawa oleh Jeffrey waktu aku kasih bola kristal itu ke dia."
    r "Hah.. yah, setidaknya aku bisa tinggal di gubuk ini sementara."
    r "Toh pisau aku sudah cukup kuat untuk melawan monster di hutan ini sendirian."
    #SFX: *Srak* *Srak* (suara semak-semak)
    play sound sfx_treeshaking
    "Aku mencium bau aneh, aku pun berjalan mengelilingi sisi luar gubuk tua itu."
    r "(!!!)" with vpunch
    #CG Remil melihat mayat Cherry with fade in 1s
    scene R2_4_remil_deadcherry with fade
    r "Cherry!! Hei!"
    r "Cherry, bangunlah!"
    r "(Tidak ada respon..)"
    r "(Aku pun memeriksa denyut nadi Cherry.)"
    r "..."
    #BG gubuk tua, day with dissolve in 1s
    scene gubuk_luar_day with dissolve
    r "..."
    r "(Darah di lukanya juga sudah mengering, sepertinya dia dibunuh lama sebelum aku tiba di sini.)"
    r "(Seingatku ada beberapa kain di dalam gubuk, mungkin bisa aku gunakan untuk menutupinya.)"
    #fade in 0,5s
    scene black with dissolve
    "Aku menutupi mayat Cherry dengan kain putih yang tadi aku temukan di dalam gubuk."
    r "(Luka di sekujur tubuhnya memanjang, seperti tebasan.. pedang?!)"
    r "(Dan seseorang yang memiliki senjata pedang disini..)"
    r "(!!!)" with vpunch
    r "Alios..."

    #BG hutan 2, day with fade in 1,5s
    #Normal manipulative M in Jeffrey
    j "..."
    #Serious M Jeffrey
    j "Ini semua perbuatan kamu kan, Elena?"
    #Jeffrey out
    ##CG Elena berdiri ketakutan di belakang Jeffrey, Jeffrey sedang memeriksa mayat Alios dissolve in 0,5s
    e "A-Ah.."
    j "Aku juga menyadarinya bahwa kamu diam-diam mengikutiku semenjak aku memasuki area hutan ini kan."
    e "A-Aku sama sekali tidak berbuat apa-apa.."
    j "Lalu kenapa gesture kamu seolah sedang-"
    j "-berancang-ancang ingin memukulku dengan tongkatmu?"
    e "(!!!)"
    #BG hutan 2, day with dissolve in 0,5s
    #Angry M in Elena
    e "I-Ini tidak seperti yang kamu kira!"
    e "Aku tidak membunuh Alios!!"
    #Elena move to L
    #Normal manipulative R in Jeffrey
    j "Lalu? Siapa lagi kalau bukan kamu."
    j "Kamu sangat membenci Alios kan?"
    e "H-Hei, tidak hanya aku saja ya! Kamu juga."
    #Serious R Jeffrey
    j "Lalu, apa aku punya kesempatan untuk membunuhnya?"
    j "Di Antara aku, Remil, dan kamu, hanya kamu yang punya kesempatan untuk menemui Alios kapan saja."
    j "Alios pasti akan menerimamu karena dia membutuhkanmu."
    e "Memangnya apa yang Alios butuhkan kepadaku hah?!"
    #Nervous L Elena
    e "Lagipula aku.. Aku tidak akan bisa membunuh orang.."
    #show luka di tangan dan kaki Jeffrey
    #Angry Jeffrey
    j "Tidak akan bisa katamu?! Lalu luka-luka ini?"
    #luka di tangan dan kaki Jeffrey out
    #Surprise L Elena
    j "Ini semua perbuatanmu."
    j "Kamu tiba-tiba menyerangku dengan tongkatmu itu!"
    j "Aku tidak tahu rupanya tongkatmu tajam, goresan di tangan dan kakiku jadi lumayan parah!"
    e "A-Aku.. Melakukan itu?"
    e "K-Kamu tidak mengarang kan? Aku tidak mengingat ini semua.."
    #Normal manipulative R Jeffrey
    j "Itu karena kamu melakukannya secara tidak sadar, Elena."
    #Serious R Jeffrey
    j "Entahlah itu akibat kejadian di gua waktu itu, kamu pernah salah makan, terkena racun monster, atau semacamnya."
    #Angry R Jeffrey
    j "Faktanya, kamu menyerangku dengan tatapan kosong."
    e "..."
    e "Maafkan.. Maafkan aku… Kumohon maafkan aku!"
    #Sad L Elena
    e "Aku tidak bisa berlama-lama di sini!!"
    #Elena out
    #SFX: *Drap* *Drap* *Drap* (langkah kaki cepat)
    #Jeffrey move to M
    #Surprise M Jeffrey
    j "Elena tunggu!!"
    #Angry M Jeffrey
    j "Disini sangat berbahaya! Kamu harus berhati-hati!!"
    #Jeffrey out
    #Black Screen. With Dissolve in 0,3s
    n "Hahahaha"
    n "Sangat menarik."

    #CHAPTER 5 END
    #CHAPTER 6

    #BG dekat sungai, dusk with dissolve in 0,5s
    r "Ini bekas tendanya Elena waktu itu kan?"
    r "Entahlah sudah berapa hari berlalu, sepertinya waktu itu aku pingsan cukup lama."
    r "Aku merasa tertinggal.."
    n "Remil."
    r "...!?!"
    #Normal M in Kai
    r "Kai?! Kenapa kamu bisa berada disini?"
    k "Aku khawatir, jadi aku terus mencarimu."
    k "Ada apa? Kamu terlihat lesu."
    r "Kamu masih ingat perempuan berambut pirang yang kamu selamatkan bersama aku dan Jeffrey?"
    k "Ingat."
    r "Dia dibunuh.."
    #Surprise M Kai
    k "..."
    #Sad M Kai
    k "Saya turut berduka.."
    r "Sepertinya.. Dia dibunuh oleh Alios."
    #Serious M Kai
    k "..."
    k "Aku ingin menunjukkan sesuatu."
    r "Apa itu?"
    k "Ikutlah denganku."
    #Kai move to L
    j "Remil!!"
    r "Jeffrey?!"
    #Sad face R in Jeffrey
    j "Hosh.. Hosh.."
    #Angry R Jeffrey
    j "Remil, jangan ikuti dia! Ikut denganku, aku tahu sesuatu."
    r "(Ada apa ini?)"
    #Serious R Jeffrey
    j "Kamu tidak bisa mempercayainya! Dia memang tahu banyak hal dan tinggal di sini lebih lama, tetapi justru itu yang membuatnya makin mencurigakan."
    r "Jeffrey.."
    #Normal L Kai
    k "..."
    j "Alios dibunuh.."
    r "Apa?! Bagaimana bisa?!"
    #Sad R Jeffrey
    j "Dilihat dari lukanya, sepertinya dia dibunuh oleh pedang."
    r "(Pedang? Tunggu dulu– tapi..)"
    #Serious R Jeffrey
    j "Hanya tuan Kai selain Alios yang memiliki pedang, iya kan?"
    k "..."
    #Happy L Kai
    k "Benar, tapi aku jarang membawanya. Aku lebih nyaman memakai sihirku."
    #Angry R Jeffrey
    j "Alasan! Bisa jadi itu hanya alibi jadi-jadian dia karena ada bekas darah di pedang itu."
    j "Tadi aku mendengarnya ingin menunjukkan sesuatu padamu, apa kamu tahu itu apa?"
    j "Bagaimana kalau yang dia tunjukkan itu pedang yang ia gunakan untuk membunuh dan akan membunuhmu juga dengan benda itu?!"

    menu:
        "Ikuti Kai":
            r "Jeffrey, maaf.."
            r "Aku percaya kalau Kai adalah orang baik."
            #Kai out
            #Jeffrey move to M
            #Sad M Jeffrey
            j "Tunggu, Remil!!"
            #Jeffrey out

            #CG Remil dan Kai di tepi danau with fade in 0,5s
            "Kai membawaku ke tepi danau."
            k "Di dalam pusaran air itu ada gua."
            k "Aku akan mendorongmu. Tenang saja, kamu tidak akan tenggelam."
            r "Tunggu, apa?!"
            "Tanpa aba-aba, Kai mendorongku." with vpunch

        "Ikuti Jeffrey":
            r "Jeffrey.. Aku percaya padamu."
            #Normal manipulative R Jeffrey
            j "Terima kasih sudah percaya padaku. Lagipula aku yang selama ini menemanimu berpetualang kan!"
            #Angry L Kai
            k "Tidak bisa.."
            "Kai menarik paksa tanganku."
            #Kai out
            #Jeffrey move to M
            #Angry M Jeffrey
            j "HEI!!"
            #Jeffrey out

            #CG Remil dan Kai di tepi danau with fade in 0,5s
            k "Kamu akan berterima kasih kepadaku nanti."
            "Kai mendorongku menuju pusaran air di danau." with vpunch

    #BG gua 2 with fade in 1s
    r "(Tempat ini.. Di bawah air?)"
    "Aku melihat sekeliling tempat ini, yang paling menarik perhatianku adalah pohon menyala yang berada tepat di tengah gua ini."
    r "Air disini jernih sekali.."
    "Aku spontan mengambil air dengan telapak tanganku dan meminumnya."
    "*Deg*"

    #(blackscreen)

    r "Tunggu, ini..."
    r "(!!!)" with vpunch
    r "Bola kristalnya pecah?"
    r "Ditambah lagi pelakunya.."
    r "Jeffrey?!"
    r "Dan dia memecahkannya dengan sengaja?!"

    #BG gua 2 with fade in 0,5s
    r "(!!!)" with vpunch
    r "(Apa yang terjadi barusan?)"
    k "Air yang berada di gua ini memiliki memori para penghuni dunia ini."
    r "(Penghuni? Tempat ini?)"
    r "(Tunggu.. Suara ini..)"
    r "Kai?!"
    #Happy M in Kai
    k "Saya adalah salah satu pembuat dunia ini."
    r "Dunia.. ini?"
    #Serious M Kai
    k "Singkat cerita, saya bekerja sama dengan rekan saya untuk menciptakan dunia baru melalui virtual."
    k "Tetapi saya dikhianati oleh rekan saya, begitu saya sedang mencoba untuk memasuki dunia buatan ini, dia membunuhku diri saya yang berada dunia nyata."
    k "Akhirnya saya terjebak disini, meskipun saya yang ada di dunia nyata sudah tiada."
    r "..."
    "Aku berusaha mencerna penjelasan Kai barusan."
    r "Aku.. belum begitu paham."
    r "Semua ini.. Palsu?"
    r "Bagaimana aku bisa berada di dalam sini?"

    #Black Screen with dissolve in 0,3s
    r "..."

    #BG gua 2 with dissolve in 0,3s
    #Serious M in Kai
    r "(Sudah beberapa kali aku mencoba, kenapa aku tidak bisa mengingatnya?!)"
    r "(Yang aku ingat hanyalah latar belakangku, aku sudah biasa hidup di kota yang berbahaya tanpa rumah.)"
    r "Lalu kenapa.."
    #Normal M Kai
    k "Jika tebakanku benar, kamu diculik oleh rekan saya dan dijadikan sebagai tikus percobaan untuk dunia buatan ini."
    r "Kenapa dia membawaku kesini? Kenapa dia memilihku? Lalu bagaimana dengan yang lain, apa mereka juga bernasib sama denganku?"
    k "Serupa tetapi tidak sama, karena latar belakang tiap orang berbeda-beda bukan?"
    k "Lalu alasan rekanku menculik kamu dan teman-temanmu, mungkin hanyalah untuk kesenangan pribadinya."
    #Sad M Kai
    k "Dia sangat menyukai bermain-main dengan emosi manusia dan membuat kekacauan."
    r "Seperti.. Alios yang sombong dan pemarah ya?"
    #Serious M Kai
    k "..."
    k "Tepatnya lagi-"
    #Kai out
    #SFX: *Bruuk!* (suara badan jatuh)
    r "(!!!)"
    r "Kai!!"
    "Kai jatuh tersungkur akibat ujung pisau menembus dadanya."
    "Kini aku semakin percaya dengan omongannya barusan karena Kai sama sekali tidak mengeluarkan darah dan setelah ia terjatuh, tubuhnya berubah menjadi kepingan cahaya yang melayang ke atas."
    #Normal manipulative M in Jeffrey
    j "Hm? Wah, ternyata benar kalau dia bukan manusia."
    "Jeffrey mengambil pisau yang tergeletak di permukaan tanah, tadinya pisau itulah yang menancap di tubuh Kai."
    #show pisau belati bersinar berwarna ungu
    r "Pisau itu kan.."
    #pisau belati bersinar berwarna ungu out
    #Serious M Jeffrey
    j "Tidak kusangka orang itu benar-benar membawamu kesini."
    r "Jeffrey?! Kamu juga tahu tempat ini?"
    #Laugh M Jeffrey
    j "Iya, tetapi ada informasi yang lebih penting dibanding itu."
    #show pisau belati bersinar berwarna ungu
    j "Senjata pembunuhan yang sebenarnya ada di tanganku ini!"
    #Happy M Jeffrey
    j "Aku berbohong soal mencurigai Kai, pembunuh mereka adalah diriku sendiri"
    j "Pisau belati ini sangat tajam, bahkan bisa jadi lebih hebat dibanding punyamu. Aku sengaja membuat seolah mereka dibunuh oleh pedang berkat ketajaman pisau ini."
    #pisau belati bersinar berwarna ungu out
    r "J-Jadi.. Pengintai yang dibunuh di lembah.. Cherry.. Bahkan Alios.. Itu semua perbuatanmu?!"
    #Smile M Jeffrey
    j "Menggemaskan, kamu polos sekali Remil."
    j "Aku membunuh mereka semua saat aku tidak berada di pandanganmu."
    r "Jangan-Jangan.. Elena juga?!"
    #Happy M Jeffrey
    j "Untuk Elena lain cerita~ Dia terbawa emosi hingga lari ke tempat yang berbahaya dan malah mati dibunuh oleh monster di sana."
    #Laugh M Jeffrey
    j "Hahaha, dia percaya saja waktu aku bilang kalau dia membunuh Alios dengan tidak sadar."
    r "..."
    #Sad M Jeffrey
    j "Aku ditipu."
    #Normal Manipulative M Jeffrey
    j "Aku hanyalah seorang murid yang bekerja sambilan menjadi penyanyi sekaligus gitaris di sebuah cafe."
    j "Aku bekerja untuk memenuhi kebutuhan pribadi dan mengejar cita-citaku karena orang tuaku bukan orang yang mampu."
    j "Tiba-tiba seorang paman dengan jas hitam memberikan kartu namanya kepadaku, ia bilang bahwa ia akan menjadikanku idola terkenal apabila aku akan menemuinya di suatu tempat."
    j "Bodohnya aku percaya dengan paman itu."
    #Sad M Jeffrey
    j "Paman itu berbohong, ia malah menculikku dan membawaku ke tempat ini."
    j "Bahkan bisa jadi dia dapat mengendalikanku, begitu juga denganmu."
    #Serious M Jeffrey
    j "Dia adalah ‘Mastermind’, orang yang mengatur dan merancang segalanya."
    r "D-Dari mana kau tahu semua ini?"
    #show luka di tangan dan kaki Jeffrey
    #Normal M Jeffrey
    j "Mungkin.. Hadiah aku membunuh semua monster di gua itu sendirian?"
    j "Lalu tiba-tiba saja aku teringat soal itu. Sulit loh, lihat saja tangan dan kakiku ini."
    #luka di tangan dan kaki Jeffrey out
    j "Lalu.. Kamu mau tahu alasanmu terpisah denganku dan Elena?"
    j "Setelah aku terbangun di gua itu, aku membawamu dan Elena ke pergi dari gua itu dan membawa kalian ke suatu tempat."
    #Happy M Jeffrey
    j "Tentu saja di dua tempat yang berbeda, hanya saja aku menaruhmu di tempat yang sangat aman."
    #Laugh M Jeffrey
    j "Aku sama sekali tidak peduli dengan si Elena itu, hahahaha."
    #Smile M Jeffrey
    j "Karena aku tidak mau didahului oleh monster-monster itu untuk membunuhmu."
    r "..Aku tidak peduli apapun masa lalu dan usaha-usahamu."
    r "Itu tidak bisa dijadikan alasan untuk membunuh yang lain!!"
    #Serious M Jeffrey
    j "Hei.. Remil."
    #Jeffrey out

    #CG Jeffrey menodong Pisau belati ungu ke leher Remil with fade in 0,3s
    j "Untuk bertahan hidup, kita harus menghabiskan apapun yang menjadi ancaman bagi kita."
    j "Benar kan~? Anak yang hidup gelandangan sepertimu pasti paham soal ini."
    j "Dan kamu adalah ancaman terbesarku, karena itu aku sengaja mengikutimu dan berpura-pura ingin menjadi temanmu untuk mendapatkan kepercayaanmu-"
    j "-agar aku tahu kelemahanmu dan mencari kesempatan untuk membunuhmu."
    r "T-Tidak.."
    j "Di buku yang kita temukan ini, ada selipan kertas mengenai jalan keluar dari dunia ini."
    j "Salah satunya adalah bola kristal yang kamu temukan."
    j "Cih, sayangnya yang bisa menggunakan itu adalah orang yang pertama kali menyentuhnya."
    j "Karena itu aku merusaknya, membuatnya pecah berbeling-beling."
    j "Aku tidak ingin kamu yang berhasil keluar dari tempat ini, Remil."
    r "K-Kenapa kamu tidak mengajak kita semua untuk keluar bersama-sama?!"
    j "Hah.."
    j "Cukup sampai sini saja aku berbicara denganmu."
    j "Kamu tidak akan paham."
    "Jeffrey menjauhkan pisaunya dari leherku."
    "Dia mendorongku.. ke perairan." with vpunch

    #Black Screen with dissolve in 0,2s
    #SFX: *Byuuurr* (suara orang nyebur ke perairan)

    #CG Remil melayang terjatuh di udara with dissolve in 1s
    #(backsound/SFX suara air dalam lautan)
    r "..."
    "Dibawah sini tidak ada air."
    "Aku tidak tenggelam."
    "Rasanya seperti.."
    "Aku terjatuh selamanya."

    #Black screen in 2s with dissolve
    #BG gua 2 with dissolve in 1s
    #Normal manipulative M in Jeffrey
    #show buku catatan 2
    j "Menurut buku catatan ini, tempat ini disebut ‘The End’."
    j "Jika seseorang terjatuh ke dalam perairan ini, ia akan merasakan terjatuh tenggelam selamanya hingga dunia ini hancur."
    #buku catatan 2 out
    #Sad M Jeffrey
    j "Wah~ ngeri juga ya."
    #Normal manipulative M Jeffrey
    "Jeffrey mendekati pohon bercahaya."
    #show tangan Jeffrey menyentuh batang pohon bersinar
    j "Selamat tinggal, Remil."
    #Happy M Jeffrey
    j "Senang bertemu denganmu, sayang sekali kita bertemu di waktu yang tidak tepat."
    #tangan Jeffrey menyentuh batang pohon bersinar out
    #Jeffrey out
    #Fade in 1s
    #-Bad Ending-


    return
