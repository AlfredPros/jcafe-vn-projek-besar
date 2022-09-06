label start:
    scene black
    n "Aduh{w=0.1}.{w=0.1}.{w=0.1}. kepalaku terasa sakit{w=0.1}.{w=0.1}.{w=0.1}."
    n "{w=0.1}.{w=0.1}.{w=0.1}.?"

    #(BG di hutan, day) Dissolve 1s
    scene hutan with dissolve
    n "Di mana aku{w=0.1}.{w=0.1}.{w=0.1}.?{w=0.3} Aku tidak bisa mengingat apa-apa.{w=0.3} Kecuali{w=0.1}.{w=0.1}.{w=0.1}."
    r "Remil{w=0.1}.{w=0.1}.{w=0.1}. namaku adalah Remil."
    r "{w=0.1}.{w=0.1}.{w=0.1}. Kenapa aku berada di tengah hutan begini?"
    r "Tidak ada waktu untuk hanya berdiam diri{w=0.1}.{w=0.1}.{w=0.1}. Aku harus segera pergi dari hutan ini!"

    #(BG di hutan, night) Fade 2s
    scene hutan_night with fade
    r "*Grooowl*"
    r "Perutku terasa lapar sekali{w=0.1}.{w=0.1}.{w=0.1}. Aku tidak sanggup berjalan kalau tidak makan sesuatu dulu."
    r "Tunggu,{w=0.3} sepertinya di pohon itu ada buah.{w=0.3} Bentuknya agak aneh tapi mungkin bisa dimakan?"
    r "Hup{w=0.1}.{w=0.1}.{w=0.1}.!{w=0.3} Hup{w=0.1}.{w=0.1}.{w=0.1}.!{w=0.3} Sedikit lagi{w=0.1}.{w=0.1}.{w=0.1}. dapat!"
    r "*Kraus kraus kraus*"
    r "Enak sekali!{w=0.3} Mungkin aku akan ambil beberapa lagi{w=0.1}.{w=0.1}.{w=0.1}."
    r "*Nyam{w=0.1}.{w=0.1}.{w=0.1}. nyam{w=0.1}.{w=0.1}.{w=0.1}. Ng{w=0.1}.{w=0.1}.{w=0.1}.?{w=0.3} Sepertinya aku mendengar suara mendesis{w=0.1}.{w=0.1}.{w=0.1}."
    r "UAAAH{w=0.1}.{w=0.1}.{w=0.1}.{w=0.1}!!" with vpunch
    play sound sfx_snakehiss
    ur "HISSSSS{w=0.1}.{w=0.1}.{w=0.1}.!!!"
    r "Be{w=0.1}.{w=0.1}.{w=0.1}. besar sekali!!{w=0.3} Apa itu?{w=0.3} Apa itu?!"
    play sound sfx_drap3x
    "*drap drap drap*"
    r "Ular itu terus mengejarku,{w=0.3} kalau terus seperti ini aku akan terpojokkan!{w=0.3} Aku harus melakukan sesuatu..."

    menu:
        "Tetap lari":
            play sound sfx_snakehiss
            ur "HISSSSS{w=0.1}.{w=0.1}.{w=0.1}.!!!"
            r "Aku rasa lebih bijak kalau aku tidak sok kuat.{w=0.3} Aku akan berusaha kabur!!"
            play sound sfx_drap3x
            r "*drap drap* Tidak mungkin!{w=0.3} Di depan sana jalan buntu!!"
            play sound sfx_snakehiss
            ur "HISSSSS{w=0.1}.{w=0.1}.{w=0.1}.!!!"
            r "Mau tidak mau aku harus menghadapinya{w=0.1}.{w=0.1}.{w=0.1}. Tapi bagaimana caranya?"
            ur "SHAAAA{w=0.1}.{w=0.1}.{w=0.1}.!!!"
            r "Gawat,{w=0.3} ular itu menyerangku!{w=0.3} Aku{w=0.1}.{w=0.1}.{w=0.1}.{w=0.1}!!{w=0.3}{nw}"
            #*Byuuur* (Suara jatuh ke sungai)
            window hide
            play sound sfx_nyebur
            scene black
            pause 5

        "Mencoba menghadapi musuh":
            r "Ular ini sangat besar,{w=0.3} pasti dia akan sulit melewati pepohonan hutan ini.{w=0.3} Jadi aku akan mencoba berlari di antara pepohonan ini."
            play sound sfx_drap3x
            "*drap drap drap*"
            r "Berhasil!{w=0.3} Ular itu mengikutiku dan dia kesulitan mengejarku!{w=0.3} Kalau ku teruskan aku pasti bisa lolos dari monster raksasa ini!"
            play sound sfx_drap3x
            r "*drap drap* Tidak mungkin!{w=0.3} Di depan sana jalan buntu!!"
            play sound sfx_snakehiss
            ur "HISSSSS{w=0.1}.{w=0.1}.{w=0.1}.!!!"
            r "Dan ular itu berhasil mengejarku{w=0.1}.{w=0.1}.{w=0.1}. Sekarang aku harus bagaimana?"
            "Ular raksasa itu tampak sangat marah,{w=0.3} Remil terpojok di ujung tebing"
            r "Uuuh{w=0.1}.{w=0.1}.{w=0.1}."
            ur "SHAAAA{w=0.1}.{w=0.1}.{w=0.1}.!!!"
            r "Gawat,{w=0.3} ular itu menyerangku!{w=0.3} Aku{w=0.1}.{w=0.1}.{w=0.1}.!!{w=0.3}{nw}"
            #*Byuuur* (Suara jatuh ke sungai)
            window hide
            play sound sfx_nyebur
            scene black
            pause 5

    scene dekat_sungai_dusk with Dissolve (2.0)
    r "Haaa{w=0.1}.{w=0.1}.{w=0.1}. haa{w=0.1}.{w=0.1}.{w=0.1}. tidak kusangka aku akan terjun bebas dan masih selamat,{w=0.3} sekarang aku hanyut entah di mana{w=0.1}.{w=0.1}.{w=0.1}. paling tidak aku sudah aman dari ular itu."
    r "Hei,{w=0.3} di sebelah sana ada tenda!{w=0.3} Apakah ada yang tinggal di sini?"
    #Elena M in
    show elena_surprise at enter
    #*Surprise face M Elena
    n "Aaah!"
    r "(!!!)" with vpunch
    #*Surprise face M Elena
    n "Kamu terluka!{w=0.3} Tunggu sebentar,{w=0.3} biar aku lihat!"
    r "Ini hanya tergores!"
    show elena_sad as elena_surprise at sigh
    #*Sad face M Elena
    n "Ini tidak bisa dibiarkan,{w=0.3} aku akan mengobatinya sebelum terinfeksi!{w=0.3} Jadi aku olesi ini dulu{w=0.1}.{w=0.1}.{w=0.1}. lalu{w=0.1}.{w=0.1}.{w=0.1}."
    r "{w=0.1}.{w=0.1}.{w=0.1}."
    show elena_happy as elena_surprise at normal
    #*Happy face M Elena
    n "{w=0.1}.{w=0.1}.{w=0.1}.Dan selesai!"
    r "Kamu tinggal di sini{w=0.1}.{w=0.1}.{w=0.1}.?"
    show elena_normal as elena_surprise
    #*Normal face M Elena
    show elena_happy as elena_surprise at bounce
    n "Benar,{w=0.3} beberapa hari lalu aku terbangun dekat sini dan karena tidak tahu harus bagaimana aku mencoba tinggal di sini."
    r "Sama sepertiku{w=0.1}.{w=0.1}.{w=0.1}."
    #*Happy face M Elena
    e "Aku senang sekali akhirnya bertemu seseorang!{w=0.3} Oh iya namaku Elena."
    r "Aku Remil{w=0.1}.{w=0.1}.{w=0.1}."
    #*Happy face M Elena
    e "Remil!{w=0.3} Apa kamu lapar?{w=0.3} Aku baru saja memetik buah,{w=0.3} ini ambillah beberapa!"
    r "{w=0.1}.{w=0.1}.{w=0.1}.Tidak usah,{w=0.3} terima kasih"
    r "(Aku tidak boleh merepotkan orang lain,{w=0.3} lagipula sebaiknya aku segera pergi dari sini.)"
    show elena_surprise as elena_surprise
    #*Surprise face M Elena
    e "Hei kamu mau kemana?!"
    r "Aku akan cari makan sendiri."
    e "Jangan begitu!{w=0.3} Aku tidak keberatan untuk berbagi loh!"
    r "Tidak.{w=0.3} Aku tidak bisa menerimanya."
    show elena_sad as elena_surprise at sigh
    #*Sad face M Elena
    e "{w=0.1}.{w=0.1}.{w=0.1}."
    e "{w=0.1}.{w=0.1}.{w=0.1}.Setelah akhirnya aku menemukan seseorang di sini{w=0.1}.{w=0.1}.{w=0.1}. aku tidak mau sendirian lagi."

    scene hutan_night with Dissolve (2)
    r "Huft{w=0.1}.{w=0.1}.{w=0.1}. sudah berapa lama aku berjalan dan aku masih tidak tahu harus kemana{w=0.1}.{w=0.1}.{w=0.1}. Dan aku sekarang lapar sekali."
    play sound sfx_anakpanahlewat
    "*Syuuung*"
    r "Suara apa itu?{w=0.1}.{w=0.1}.{w=0.1}. !!!{w=0.3} Hei di sana ada orang!"
    r "Orang itu memiliki busur{w=0.1}.{w=0.1}.{w=0.1}. Apa dia yang membunuh hewan besar itu?{w=0.3} Hebat sekali{w=0.1}.{w=0.1}.{w=0.1}."
    play sound sfx_anakpanahlewat
    "*Syuung*"
    r "{w=0.1}.{w=0.1}.{w=0.1}.!!!!" with vpunch
    r "(Ada panah melesat tepat di sampingku{w=0.1}.{w=0.1}.{w=0.1}.)"
    #Jeffrey M in
    show jeffrey_angry2 at enter
    #*Angry face M Jeffery
    n "Siapa di sana?"
    show jeffrey_angry1 as jeffrey_angry2
    r "Orang ini sepertinya sangat berbahaya{w=0.1}.{w=0.1}.{w=0.1}. Sebaiknya aku kabur perlahan saja{w=0.1}.{w=0.1}.{w=0.1}."
    play sound sfx_anakpanahlewat
    "*Syuung*"
    r "{w=0.1}.{w=0.1}.{w=0.1}.!!!!" with vpunch
    n "Tunjukkan dirimu!"
    r "(Orang itu mengarah kemari!{w=0.3} Kalau begitu{w=0.1}.{w=0.1}.{w=0.1}.!)"
    r "Hup!!"
    show jeffrey_surprised as jeffrey_angry2
    #*Surprise face M Jeffery
    n "Uaaah!!"
    hide jeffrey_angry2
    #Jeffrey out
    play sound sfx_gedebruk
    "*Bruuuk*" with vpunch
    #Jeffrey M in
    #*Surprise face M Jeffery
    show jeffrey_surprised at enter
    n "Hei,{w=0.3} hei,{w=0.3} tidak perlu sampai menarik kakiku begini kan?"
    r "Tapi kau menyerangku!"
    n "Itu karena aku kira ada monster!{w=0.3} Maaf,{w=0.1} maaf!{w=0.3} Tolong menyingkir dari badanku!"
    r "Baiklah{w=0.1}.{w=0.1}.{w=0.1}."
    #*Normal face M Jeffery
    show jeffrey_normal as jeffrey_surprised
    n "Fyuh,{w=0.3} tapi kau berani juga langsung menyerang seperti itu tanpa senjata."
    r "Karena aku melihat ada celah."
    j "Aku rasa kau punya potensi untuk menjadi petarung handal.{w=0.3} Siapa namamu?{w=0.3} Aku Jeffrey."
    r "Aku Remil."
    #*Happy face M Jeffrey
    show jeffrey_happy as jeffrey_surprised
    j "Remil,{w=0.3} bagaimana kalau kau ikut aku?{w=0.3} Aku akan mengajarimu cara bertarung."
    #*Normal face M Jeffrey
    show jeffrey_normal as jeffrey_surprised
    j "Kau pasti sudah sadar,{w=0.1} kan,{w=0.3} kalau tempat ini berbahaya?"
    r "Kau benar.{w=0.3} Tapi{w=0.1}.{w=0.1}.{w=0.1}."
    #*Happy face M Jeffrey
    show jeffrey_happy as jeffrey_surprised
    j "Tidak usah ragu!{w=0.3} Kalau ikut aku kau akan mendapatkan tenda sendiri dan makanan enak tiga kali sehari!"
    r "Makanan enak tiga kali sehari?!"
    j "Benar!{w=0.3} Aku ini bergabung dengan kelompok yang dipimpin Alios."
    j "Kelompok ini terbuka untuk siapa saja yang mau bekerja untuk Alios."
    #*Normal face M Jeffrey
    show jeffrey_normal as jeffrey_surprised
    j "Tentu saja karena itu untuk bisa tinggal dan makan enak kau harus bekerja!"
    j "Entah sebagai pemburu,{w=0.3} juru masak,{w=0.3} atau lainnya!"
    r "Kalau tidak kerja maka tidak akan dapat makanan ya{w=0.1}.{w=0.1}.{w=0.1}."
    j "Iya! Sekarang pun aku sedang berburu,{w=0.3} tangkapan hari ini cukup besar loh!{w=0.3} Rasanya pasti gurih dan nikmat!"
    r "*Gulp*"
    #*Happy face  M Jeffrey
    show jeffrey_happy as jeffrey_surprised
    j "Bagaimana Remil?"
    n "Tunggu!{w=0.3} Tolong ajak aku juga!!" with vpunch
    r "E-Elena?!"
    #*Surprise face  M Jeffrey
    show jeffrey_surprised as jeffrey_surprised
    j "Siapa dia?"
    #Elena R in
    show jeffrey_surprised as jeffrey_surprised at m2
    show elena_happy at enterr
    pause 0.3
    #Jeffery go left
    #*Happy face R Elena
    show elena_happy as elena_happy at talk
    e "Namaku Elena!{w=0.3} Kelompok yang tadi anda ceritakan{w=0.1}.{w=0.1}.{w=0.1}. Apakah ada banyak orang di sana?"
    show elena_happy as elena_happy at notalk
    #*Surprise face L Jeffrey
    show jeffrey_surprised as jeffrey_surprised at talk
    j "Iya lumayan banyak."
    j "Elena apa kamu mengikutiku?!"
    show jeffrey_surprised as jeffrey_surprised at notalk
    #*Sad face R Elena
    show elena_sad as elena_happy at sigh
    e "Habis aku khawatir dengan lukamu!{w=0.3} Dan aku juga{w=0.1}.{w=0.1}.{w=0.1}. tidak mau sendirian lagi."
    #*Happy face L Jeffrey
    show jeffrey_happy as jeffrey_surprised
    j "Hahaha! Kalau begitu kenapa kau tidak ikut dengan kami saja?"
    #*Happy face R Elena
    show elena_happy as elena_happy at normal
    e "Boleh?!{w=0.3} Hore!"
    r "Tapi aku tidak bilang{w=0.1}.{w=0.1}.{w=0.1}."
    #*Normal face R Elena
    show elena_normal as elena_happy at talk
    e "Ayolah Remil!{w=0.3} Aku tahu kamu pasti kelaparan kan setelah berjalan sangat jauh?"
    show elena_normal as elena_happy at notalk
    r "Uuugh{w=0.1}.{w=0.1}.{w=0.1}."
    show jeffrey_happy as jeffrey_surprised at talk
    j "Sudah diputuskan!{w=0.3} Sekarang,{w=0.3} ayo kita pergi ke perkemahan Alios."
    scene black with dissolve
    pause 1
    scene chp_blank with dissolve
    pause 0.5
    show transition1 with dissolve
    pause 3
    scene black with dissolve
    pause 1
    #Transition

    #(BG di perkemahan Alios, dusk with dissolve)
    scene tenda_gelap with dissolve
    show jeffrey_happy at enterl
    show elena_happy at enterr
    #Jeffrey L in & Elena R in
    #Happy face L Jeffrey
    pause 0.3
    show jeffrey_happy as jeffrey_happy at talk
    j "Baik,{w=0.3} kita sudah sampai!"
    show jeffrey_happy as jeffrey_happy at notalk
    #Happy face R Elena
    show elena_happy as elena_happy at talk
    e "Wah ada banyak orang!"
    show elena_happy as elena_happy at notalk
    show jeffrey_happy as jeffrey_happy at talk
    j "Ayo kuajak kalian bertemu pemimpin kelompok ini dulu!"
    show jeffrey_happy as jeffrey_happy at notalk
    r "(Kira-kira seperti apa ya pemimpinnya{w=0.1}.{w=0.1}.{w=0.1}.)"
    show jeffrey_normal as jeffrey_happy at talk
    #Normal face L Jeffrey
    j "Hei Alios!{w=0.3} Aku bertemu dengan dua orang ketika berburu tadi."
    show jeffrey_normal as jeffrey_happy at notalk
    hide elena_happy
    show alios_normal at enterr
    pause 0.3
    #Elena out & Alios R in
    #Normal face R Alios
    show alios_normal as alios_normal at talk
    al "Huh?{w=0.3} Siapa mereka?"
    show alios_normal as alios_normal at notalk
    show jeffrey_normal as jeffrey_happy at talk
    j "Mereka adalah Elena dan Remil."
    show jeffrey_normal as jeffrey_happy at notalk
    show alios_normal as alios_normal at talk
    al "Selama kalian berguna untukku,{w=0.3} kalian diterima di sini."
    show alios_normal as alios_normal at notalk
    r "(Orang ini tampak kuat dan sombong sekali{w=0.1}.{w=0.1}.{w=0.1}.)"
    #Happy face L Jeffrey
    show jeffrey_happy as jeffrey_happy at talk
    j "Ya,{w=0.3} aku melihat potensi bahwa Remil bisa sangat membantu di sini.{w=0.3} Makanya aku ajak kemari,{w=0.3} hahaha!"
    show jeffrey_happy as jeffrey_happy at notalk
    #Happy face R Alios
    show alios_happy as alios_normal at talk
    al "Heh,{w=0.3} sebaiknya memang begitu."
    show alios_happy as alios_normal at notalk
    pause 0.3
    #alios out
    hide alios_normal
    r "{w=0.1}.{w=0.1}.{w=0.1}."
    #Normal face L Jeffrey
    show jeffrey_normal as jeffrey_happy
    j "Kalau begitu aku akan mengantar kalian ke tenda masing-masing.{w=0.3} Istirahatlah dulu sampai waktu makan malam."
    #Elena R in
    show elena_happy at enterr
    #Happy face R Elena
    e "Baik!{w=0.3} Terima kasih!"

    #(BG di kantin, Night) Dissolve 1s
    scene canteen_night2 with dissolve
    #Elena L in & Jeffrey R in
    #*Happy face L Elena
    show jeffrey_normal at enterl
    show elena_happy at enterr
    pause 0.3
    show elena_happy as elena_happy at talk
    e "Waah banyak sekali makanannya!"
    show elena_happy as elena_happy at notalk
    #*Normal face R Jeffrey
    show jeffrey_normal as jeffrey_normal at talk
    j "Tentu saja!{w=0.3} Ini jatah untuk puluhan orang."
    show jeffrey_normal as jeffrey_normal at notalk
    #*Normal face L Elena
    show elena_normal as elena_happy at talk
    e "Kalau begitu kita tidak boleh rakus,{w=0.3} ya kan Remil?"
    show elena_normal as elena_happy at notalk
    r "*Kraus kraus*"
    show elena_surprise as elena_happy
    #*Surprise face L Elena
    e "{w=0.1}.{w=0.1}.{w=0.1}."
    #*Happy face R Jeffrey
    show jeffrey_happy as jeffrey_normal at talk
    j "Hahaha!{w=0.3} Tidak masalah kok,{w=0.3} makan saja yang banyak!"
    show jeffrey_happy as jeffrey_normal at notalk
    n "Hei Jeffrey,{w=0.3} siapa mereka?"
    #*Normal face R Jeffrey
    show jeffrey_normal as jeffrey_normal at talk
    j "Oh ya,{w=0.3} Cherry,{w=0.1} mereka adalah Remil dan Elena,{w=0.3} orang yang baru bergabung dengan kita."
    show jeffrey_normal as jeffrey_normal at m21
    show elena_surprise as elena_happy at m34
    show cherry_normal at enter
    #Cherry M in
    #*Normal face M Cherry
    pause 0.3
    show cherry_normal as cherry_normal at talk
    c "Oh?"
    show cherry_normal as cherry_normal at notalk
    pause 0.3
    show cherry_happy as cherry_normal at talk
    #*Happy face M Cherry
    c "Hehe!{w=0.3} Halo,{w=0.1} aku Cherry!"
    show cherry_happy as cherry_normal at notalk
    #*Normal face L Elena
    show elena_normal as elena_happy at talk
    e "Ah halo{w=0.1}.{w=0.1}.{w=0.1}. kamu imut sekali."
    show elena_normal as elena_happy at notalk
    show jeffrey_normal as jeffrey_normal at talk
    j "Cherry ini yang paling muda di sini.{w=0.3} Jadi dia diperlakukan seperti anak bawang."
    show jeffrey_normal as jeffrey_normal at notalk
    show cherry_happy as cherry_normal at talk
    c "Itu benar!{w=0.3} Jadi sebaiknya kalian berlaku baik pada Cherry!"
    show cherry_happy as cherry_normal at notalk
    show elena_normal as elena_happy at talk
    e "Ahahaha{w=0.1}.{w=0.1}.{w=0.1}. Ngomong-ngomong Remil,{w=0.3} kamu diam saja dari tadi?"
    show elena_normal as elena_happy at notalk
    r "*Kraus kraus* Hm?"
    #*Angry face M Cherry
    show cherry_angry as cherry_normal at talk
    c "Hei!{w=0.3} Apa dia mendengarkanku?!"
    show cherry_angry as cherry_normal at notalk
    show jeffrey_normal as jeffrey_normal at talk
    j "Sudahlah Cherry,{w=0.3} sekarang kita nikmati makan malam dulu oke?"
    show jeffrey_normal as jeffrey_normal at notalk
    #*Normal face M Cherry
    show cherry_normal as cherry_normal at talk
    c "Tentu saja,{w=0.3} Hmp!"
    show cherry_normal as cherry_normal at notalk
    #(black screen with dissolve)
    scene black with dissolve
    pause(3)
    #(BG di kantin, Night) Dissolve 1s
    scene canteen_night2 with dissolve
    r "(Wah ini pertama kalinya aku makan daging sepuas itu{w=0.1}.{w=0.1}.{w=0.1}.)"
    #Jeffrey M in
    #*Normal face M Jeffrey
    show jeffery_normal at enter
    j "Remil,{w=0.3} apa kamu sudah selesai makan?"
    r "Iya.{w=0.3} Terima kasih untuk santapannya."
    j "Lagipula itu tidak gratis,{w=0.3} istirahatlah sekarang karena besok kamu akan ikut pergi bersamaku."
    r "Aku tahu{w=0.1}.{w=0.1}.{w=0.1}. baiklah"
    scene black with dissolve
    pause(5)

    #(BG di hutan, day) Dissolve 1s
    scene hutan_2
    #*Normal face M Jeffrey
    j "Sekarang kamu mungkin belum bisa memanah,{w=0.3} jadi cukup perhatikan aku saja nanti."
    r "Baiklah."
    play sound sfx_drap3x
    "*Drap drap drap*" #sfx
    r "Hei mereka mau kemana?"
    j "Oh itu regu pengintai,{w=0.3} kadang Alios memerintah beberapa orang untuk pergi melihat situasi dan keadaan."
    r "Untuk apa?"
    j "Agar tempat ini tetap aman dari hewan berbahaya dan untuk mencari sumber daya baru juga."
    r "Tampaknya tugas mereka penting sekali{w=0.1}.{w=0.1}.{w=0.1}."
    #*Happy face M Jeffrey
    j "Tugas kita tidak kalah penting tahu!{w=0.3} Memangnya nanti malam kamu mau makan apa?"
    #*Normal face M Jeffrey
    j "Tapi,{w=0.3} tugas mereka memang lebih berbahaya daripada berburu."
    r "Begitu ya{w=0.1}.{w=0.1}.{w=0.1}."

    #(BG di perkemahan Alios, dusk) Dissolve 1s
    scene campsite with dissolve
    #Elena L in & Jeffrey R in
    show jeffrey_normal at enterl
    show elena_happy at enterr
    #*Happy face L Elena
    e "Ah kalian sudah kembali!"
    #*Normal face R Jeffrey
    j "Hari ini pun tangkapan besar!"
    r "Dan aku tidak melakukan apa-apa selain mengangkut hasil buruan{w=0.1}.{w=0.1}.{w=0.1}."
    e "Aku juga bekerja dari tadi pagi dan sekarang tugasku baru selesai!"
    j "Wah kamu sepertinya semangat sekali ya."
    e "Tentu saja!{w=0.3} Rasanya aku sudah biasa bekerja keras seperti ini."
    a "TOLONG{w=0.1}.{w=0.1}.{w=0.1}.!!!"
    #*Surprise face L Elena
    e "!!!"
    r "!!!"
    r "(Hei,{w=0.3} mereka regu pengintai tadi pagi!)"
    #*Angry face R Jeffrey
    j "Hei jangan bawa monster itu kemari!!!"
    b "DIA MENGEJAR KAMI!!!"
    j "Jangan kemari!!{w=0.3} Kalian akan menghancurkan perkemahannya!!!"

    "*Syuuung{w=0.1}.{w=0.1}.{w=0.1}.{w=0.1}. Jleeeb!!*" #sfx
    #*Surprise face L Elena
    e "Ah!"
    r "He{w=0.1}.{w=0.1}.{w=0.1}. hebat{w=0.1}.{w=0.1}.{w=0.1}. hanya dengan satu tebasan bisa membunuh monster itu{w=0.1}.{w=0.1}.{w=0.1}."
    #All out & Alios M in
    #*Angry face M Alios
    al "Apa yang kalian pikirkan?!"
    a "Maafkan kami!{w=0.3} Tiba-tiba saja kami dikejar ketika sedang mengintai{w=0.1}.{w=0.1}.{w=0.1}."
    al "Alasan kalian tidak bisa diterima!!{w=0.3} Apa kalian mau menghancurkan kerajaanku?!"
    #Alios out & Jeffrey M in
    #*Surprise face M Jeffrey
    j "Hei setidaknya sekarang sudah baik-baik sa-"
    play sound sfx_greatsword
    a "UAAAAH!!" with vpunch #sfx sword?
    j "Alios!!{w=0.1} Apa yang kau lakukan?!{w=0.1} Ka{w=0.1}.{w=0.1}.{w=0.1}. kau membunuhnya!!"
    #Jeffrey out & Alios M in
    #*Angry face M Alios
    al "Aku tidak membutuhkan orang yang tidak berguna!!"
    b "Ti{w=0.1}.{w=0.1}.{w=0.1}. tidak tolong jangan bunuh aku{w=0.1}.{w=0.1}.{w=0.1}.!{w=0.2} Kasihani aku{w=0.1}.{w=0.1}.{w=0.1}.!"
    r "(Ini gila!{w=0.3} Aku harus menghentikannya!)"
    al "Kalau kau memang mau kumaafkan,{w=0.3} kau harus menjadi lebih berguna!!"
    b "A{w=0.1}.{w=0.1}.{w=0.1}. aku mengerti!{w=0.3} Aku tidak akan kabur lagi!{w=0.3} A{w=0.1}.{w=0.1}.{w=0.1}. aku akan menghadapi musuh dengan mempertaruhkan nyawaku!{w=0.3} Ja{w=0.1}.{w=0.1}.{w=0.1}. jadi{w=0.1}.{w=0.1}.{w=0.1}."
    #*Happy face M Alios
    al "Hahaha!{w=0.3} Bagus,{w=0.1} bagus,{w=0.1} kau akan mempertaruhkan nyawamu kan?"
    #*Smirk face M Alios
    al "Kalau begitu sekarang saatnya."
    r "He{w=0.1}.{w=0.1}.{w=0.1}. hei!!"
    #*Normal face M Alios
    al "Apa masalahmu anak baru?"
    r "Kau tidak bisa bersikap seenaknya seperti itu!{w=0.3} Kau adalah pemimpin kan?!"
    #*Angry face M Alios
    al "Hah?!{w=0.2} Apa kau punya masalah denganku?!{w=0.2} Apa kau menentang caraku?!"
    r "(Tentu saja!{w=0.1} Tidak mungkin aku membiarkan pembunuhan apapun yang terjadi!)"
    al "Katakan sesuatu!!"
    #Elena L in
    #*Angry face L Elena
    e "Tentu saja kami menentang hal itu!{w=0.3} Kau telah membunuh seseorang!"
    al "Jeffrey!!{w=0.3} Beritahu mereka peraturan di tempat ini!!{w=0.1} Kalau kalian masih ingin berada di sini,{w=0.1} sebaiknya jangan pernah melawanku!!"
    #*Surprise face L Elena
    e "{w=0.1}.{w=0.1}.{w=0.1}.!"
    #Alios out & Jeffrey R in
    #*Sad face R Jeffrey
    j "Maaf semuanya,{w=0.3} kalian harus menyaksikan hal mengerikan seperti itu{w=0.1}.{w=0.1}.{w=0.1}."
    #*Sad face L Elena
    e "{w=0.1}.{w=0.1}.{w=0.1}."
    r "{w=0.1}.{w=0.1}.{w=0.1}."
    #All out
    r "(Kalau aku tetap berada di sini{w=0.1}.{w=0.1}.{w=0.1}. mungkin saja akan membahayakan hidupku{w=0.1}.{w=0.1}.{w=0.1}.)"
    menu:
        "Menetap di sini":
            r "(Kalau Aku tetap berada di sini{w=0.1}.{w=0.1}.{w=0.1}. mungkin saja akan membahayakan hidupku{w=0.1}.{w=0.1}.{w=0.1}.)"
            jump branch1

        "Pergi sendiri":
            r "{w=0.1}.{w=0.1}.{w=0.1}."
            r "(Aku tidak bisa mengikuti perintah dia.)"
            jump branch2

        "Ajak Elena pergi":
            r "Tegarkan dirimu, Elena. Aku akan berusaha untuk keluar dari tempat ini. Ikutlah denganku."
            #show normal elena as elena di tengah
            e "Aku sangat berterima kasih. Tetapi, aku takut bahwa nanti aku yang akan mati. Aku sangat khawatir"
            r "Aku punya rencana yang lumayan efektif buat kita."
            "Remil menjelaskan rencananya ke Elena."
            #scene Black dissolve(1.0)
            jump branch3

    return
