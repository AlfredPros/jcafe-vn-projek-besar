label start:
    #(BG hitam)
    n "Aduh... kepalaku terasa sakit..."
    n "...?"

    #(BG di hutan, day) Dissolve 1s
    n "Di mana aku...? Aku tidak bisa mengingat apa-apa. Kecuali..."
    r "Remil... namaku adalah Remil."
    r "... Kenapa aku berada di tengah hutan begini?"
    r "Tidak ada waktu untuk hanya berdiam diri... Aku harus segera pergi dari hutan ini!"

    #(BG di hutan, night) Fade 2s
    r "*Grooowl*"
    r "Perutku terasa lapar sekali… Aku tidak sanggup berjalan kalau tidak makan sesuatu dulu."
    r "Tunggu, sepertinya di pohon itu ada buah. Bentuknya agak aneh tapi mungkin bisa dimakan?"
    r "Hup...! Hup...! Sedikit lagi... dapat!"
    r "*Kraus kraus kraus*"
    r "Enak sekali! Mungkin aku akan ambil beberapa lagi..."
    r "*Nyam... nyam...* Ng...? Sepertinya aku mendengar suara mendesis..."
    r "UAAAH...!!" with vpunch
    ur "HISSSSS...!!!"
    r "Be... besar sekali!! Apa itu? Apa itu?!"
    "*drap drap drap*"
    r "Ular itu terus mengejarku, kalau terus seperti ini aku akan terpojokkan! Aku harus melakukan sesuatu..."

    menu:
        "Tetap lari":
            ur "HISSSSS...!!!"
            r "Aku rasa lebih bijak kalau aku tidak sok kuat. Aku akan berusaha kabur!!"
            r "*drap drap* Tidak mungkin! Di depan sana jalan buntu!!"
            ur "HISSSSS...!!!"
            r "Mau tidak mau aku harus menghadapinya... Tapi bagaimana caranya?"
            ur "SHAAAA...!!!"
            r "Gawat, ular itu menyerangku! Aku...!!"
            #*Byuuur* (Suara jatuh ke sungai)
            #(Black screen)

        "Mencoba menghadapi musuh":
            r "Ular ini sangat besar, pasti dia akan sulit melewati pepohonan hutan ini. Jadi aku akan mencoba berlari di antara pepohonan ini."
            "*drap drap drap*"
            r "Berhasil! Ular itu mengikutiku dan dia kesulitan mengejarku! Kalau ku teruskan aku pasti bisa lolos dari monster raksasa ini!"
            r "*drap drap* Tidak mungkin! Di depan sana jalan buntu!!"
            ur "HISSSSS...!!!"
            r "Dan ular itu berhasil mengejarku... Sekarang aku harus bagaimana?"
            "Ular raksasa itu tampak sangat marah, Remil terpojok di ujung tebing"
            r "Uuuh..."
            ur "SHAAAA...!!!"
            r "Gawat, ular itu menyerangku! Aku...!!"
            #*Byuuur* (Suara jatuh ke sungai)
            #(Black screen)

    #(BG dekat sungai, day with dissolve)
    r "Haaa... haa... tidak kusangka aku akan terjun bebas dan masih selamat, sekarang aku hanyut entah di mana... paling tidak aku sudah aman dari ular itu."
    r "Hei, di sebelah sana ada tenda! Apakah ada yang tinggal di sini?"
    #Elena M in
    #*Surprise face M Elena
    n "Aaah!"
    r "!!!"
    #*Surprise face M Elena
    n "Kamu terluka! Tunggu sebentar, biar aku lihat!"
    r "Ini hanya tergores!"
    #*Sad face M Elena
    n "Ini tidak bisa dibiarkan, aku akan mengobatinya sebelum terinfeksi! Jadi aku olesi ini dulu... lalu..."
    r "..."
    #*Happy face M Elena
    n "...Dan selesai!"
    r "Kamu tinggal di sini...?"
    #*Normal face M Elena
    n "Benar, beberapa hari lalu aku terbangun dekat sini dan karena tidak tahu harus bagaimana aku mencoba tinggal di sini."
    r "Sama sepertiku..."
    #*Happy face M Elena
    e "Aku senang sekali akhirnya bertemu seseorang! Oh iya namaku Elena."
    r "Aku Remil..."
    #*Happy face M Elena
    e "Remil! Apa kamu lapar? Aku baru saja memetik buah, ini ambillah beberapa!"
    r "...Tidak usah, terima kasih"
    r "(Aku tidak boleh merepotkan orang lain, lagipula sebaiknya aku segera pergi dari sini.)"
    #*Surprise face M Elena
    e "Hei kamu mau kemana?!"
    r "Aku akan cari makan sendiri."
    e "Jangan begitu! Aku tidak keberatan untuk berbagi loh!"
    r "Tidak. Aku tidak bisa menerimanya."
    #*Sad face M Elena
    e "..."
    e "...Setelah akhirnya aku menemukan seseorang di sini... aku tidak mau sendirian lagi."

    #(BG di hutan, day) Fade 2s
    r "Huft... sudah berapa lama aku berjalan dan aku masih tidak tahu harus kemana... Dan aku sekarang lapar sekali."
    "*Syuuung*"
    r "Suara apa itu?... !!! Hei di sana ada orang!"
    r "Orang itu memiliki busur... Apa dia yang membunuh hewan besar itu? Hebat sekali..."
    "*Syuung*"
    r "...!!!!" with vpunch
    r "(Ada panah melesat tepat di sampingku…)"
    #Jeffrey M in
    #*Angry face M Jeffery
    n "Siapa di sana?"
    r "Orang ini sepertinya sangat berbahaya... Sebaiknya aku kabur perlahan saja..."
    "*Syuung*"
    r "...!!!!" with vpunch
    n "Tunjukkan dirimu!"
    r "(Orang itu mengarah kemari! Kalau begitu...!)"
    r "Hup!!"
    #*Surprise face M Jeffery
    n "Uaaah!!"
    #Jeffrey out
    "*Bruuuk*" #sfx
    #Jeffrey M in
    #*Surprise face M Jeffery
    n "Hei, hei, tidak perlu sampai menarik kakiku begini kan?"
    r "Tapi kau menyerangku!"
    n "Itu karena aku kira ada monster! Maaf, maaf! Tolong menyingkir dari badanku!"
    r "Baiklah..."
    #*Normal face M Jeffery
    n "Fyuh, tapi kau berani juga langsung menyerang seperti itu tanpa senjata."
    r "Karena aku melihat ada celah."
    j "Aku rasa kau punya potensi untuk menjadi petarung handal. Siapa namamu? Aku Jeffrey."
    r "Aku Remil."
    #*Happy face M Jeffrey
    j "Remil, bagaimana kalau kau ikut aku? Aku akan mengajarimu cara bertarung."
    #*Normal face M Jeffrey
    j "Kau pasti sudah sadar, kan, kalau tempat ini berbahaya?"
    r "Kau benar. Tapi..."
    #*Happy face M Jeffrey
    j "Tidak usah ragu! Kalau ikut aku kau akan mendapatkan tenda sendiri dan makanan enak tiga kali sehari!"
    r "Makanan enak tiga kali sehari?!"
    j "Benar! Aku ini bergabung dengan kelompok yang dipimpin Alios."
    j "Kelompok ini terbuka untuk siapa saja yang mau bekerja untuk Alios."
    #*Normal face M Jeffrey
    j "Tentu saja karena itu untuk bisa tinggal dan makan enak kau harus bekerja!"
    j "Entah sebagai pemburu, juru masak, atau lainnya!"
    r "Kalau tidak kerja maka tidak akan dapat makanan ya..."
    j "Iya! Sekarang pun aku sedang berburu, tangkapan hari ini cukup besar loh! Rasanya pasti gurih dan nikmat!"
    r "*Gulp*"
    #*Happy face  M Jeffrey
    j "Bagaimana Remil?"
    n "Tunggu! Tolong ajak aku juga!!" with vpunch
    r "E-Elena?!"
    #*Surprise face  M Jeffrey
    j "Siapa dia?"
    #Elena R in
    #Jeffery go left
    #*Happy face R Elena
    e "Namaku Elena! Kelompok yang tadi anda ceritakan... Apakah ada banyak orang di sana?"
    #*Surprise face L Jeffrey
    j "Iya lumayan banyak."
    j "Elena apa kamu mengikutiku?!"
    #*Sad face R Elena
    e "Habis aku khawatir dengan lukamu! Dan aku juga... tidak mau sendirian lagi."
    #*Happy face L Jeffrey
    j "Hahaha! Kalau begitu kenapa kau tidak ikut dengan kami saja?"
    #*Happy face R Elena
    e "Boleh?! Hore!"
    r "Tapi aku tidak bilang..."
    #*Normal face R Elena
    e "Ayolah Remil! Aku tahu kamu pasti kelaparan kan setelah berjalan sangat jauh?"
    r "Uuugh..."
    j "Sudah diputuskan! Sekarang, ayo kita pergi ke perkemahan Alios."

    #Transition

    #(BG di perkemahan Alios, dusk with dissolve)
    #Jeffrey L in & Elena R in
    #*Happy face L Jeffrey
    j "Baik, kita sudah sampai!"
    #*Happy face R Elena
    e "Wah ada banyak orang!"
    j "Ayo kuajak kalian bertemu pemimpin kelompok ini dulu!"
    r "(Kira-kira seperti apa ya pemimpinnya...)"
    #*Normal face L Jeffrey
    j "Hei Alios! Aku bertemu dengan dua orang ketika berburu tadi."
    #Elena out & Alios R in
    #*Normal face R Alios
    al "Huh? Siapa mereka?"
    j "Mereka adalah Elena dan Remil."
    al "Selama kalian berguna untukku, kalian diterima di sini."
    r "(Orang ini tampak kuat dan sombong sekali...)"
    #*Happy face L Jeffrey
    j "Ya, aku melihat potensi bahwa Remil bisa sangat membantu di sini. Makanya aku ajak kemari, hahaha!"
    #*Happy face R Alios
    al "Heh, sebaiknya memang begitu."
    #Alios out
    r "..."
    #*Normal face L Jeffrey
    j "Kalau begitu aku akan mengantar kalian ke tenda masing-masing. Istirahatlah dulu sampai waktu makan malam."
    #Elena R in
    #*Happy face R Elena
    e "Baik! Terima kasih!"

    #(BG di kantin, Night) Dissolve 1s
    #Elena L in & Jeffrey R in
    #*Happy face L Elena
    e "Waah banyak sekali makanannya!"
    #*Normal face R Jeffrey
    j "Tentu saja! Ini jatah untuk puluhan orang."
    #*Normal face L Elena
    e "Kalau begitu kita tidak boleh rakus, ya kan Remil?"
    r "*Kraus kraus*"
    #*Surprise face L Elena
    e "..."
    #*Happy face R Jeffrey
    j "Hahaha! Tidak masalah kok, makan saja yang banyak!"
    n "Hei Jeffrey, siapa mereka?"
    #*Normal face R Jeffrey
    j "Oh ya, Cherry, mereka adalah Remil dan Elena, orang yang baru bergabung dengan kita."
    #Cherry M in
    #*Normal face M Cherry
    c "Oh?"
    #*Happy face M Cherry
    c "Hehe! Halo, aku Cherry!"
    #*Normal face L Elena
    e "Ah halo... kamu imut sekali."
    j "Cherry ini yang paling muda di sini. Jadi dia diperlakukan seperti anak bawang."
    c "Itu benar! Jadi sebaiknya kalian berlaku baik pada Cherry!"
    e "Ahahaha... Ngomong-ngomong Remil, kamu diam saja dari tadi?"
    r "*Kraus kraus* Hm?"
    #*Angry face M Cherry
    c "Hei! Apa dia mendengarkanku?!"
    j "Sudahlah Cherry, sekarang kita nikmati makan malam dulu oke?"
    #*Normal face M Cherry
    c "Tentu saja, Hmp!"
    #(black screen with dissolve)
    pause(2)
    #(BG di kantin, Night) Dissolve 1s
    r "(Wah ini pertama kalinya aku makan daging sepuas itu...)"
    #Jeffrey M in
    #*Normal face M Jeffrey
    j "Remil, apa kamu sudah selesai makan?"
    r "Iya. Terima kasih untuk santapannya."
    j "Lagipula itu tidak gratis, istirahatlah sekarang karena besok kamu akan ikut pergi bersamaku."
    r "Aku tahu... baiklah"

    #(BG di hutan, day) Dissolve 1s
    #*Normal face M Jeffrey
    j "Sekarang kamu mungkin belum bisa memanah, jadi cukup perhatikan aku saja nanti."
    r "Baiklah."
    "*Drap drap drap*" #sfx
    r "Hei mereka mau kemana?"
    j "Oh itu regu pengintai, kadang Alios memerintah beberapa orang untuk pergi melihat situasi dan keadaan."
    r "Untuk apa?"
    j "Agar tempat ini tetap aman dari hewan berbahaya dan untuk mencari sumber daya baru juga."
    r "Tampaknya tugas mereka penting sekali..."
    #*Happy face M Jeffrey
    j "Tugas kita tidak kalah penting tahu! Memangnya nanti malam kamu mau makan apa?"
    #*Normal face M Jeffrey
    j "Tapi, tugas mereka memang lebih berbahaya daripada berburu."
    r "Begitu ya..."

    #(BG di perkemahan Alios, dusk) Dissolve 1s
    #Elena L in & Jeffrey R in
    #*Happy face L Elena
    e "Ah kalian sudah kembali!"
    #*Normal face R Jeffrey
    j "Hari ini pun tangkapan besar!"
    r "Dan aku tidak melakukan apa-apa selain mengangkut hasil buruan..."
    e "Aku juga bekerja dari tadi pagi dan sekarang tugasku baru selesai!"
    j "Wah kamu sepertinya semangat sekali ya."
    e "Tentu saja! Rasanya aku sudah biasa bekerja keras seperti ini."
    a "TOLONG...!!!"
    #*Surprise face L Elena
    e "!!!"
    r "!!!"
    r "(Hei, mereka regu pengintai tadi pagi!)"
    #*Angry face R Jeffrey
    j "Hei jangan bawa monster itu kemari!!!"
    b "DIA MENGEJAR KAMI!!!"
    j "Jangan kemari!! Kalian akan menghancurkan perkemahannya!!!"
    "*Syuuung…. Jleeeb!!*" #sfx
    #*Surprise face L Elena
    e "Ah!"
    r "He... hebat... hanya dengan satu tebasan bisa membunuh monster itu..."
    #All out & Alios M in
    #*Angry face M Alios
    al "Apa yang kalian pikirkan?!"
    a "Maafkan kami! Tiba-tiba saja kami dikejar ketika sedang mengintai..."
    al "Alasan kalian tidak bisa diterima!! Apa kalian mau menghancurkan kerajaanku?!"
    #Alios out & Jeffrey M in
    #*Surprise face M Jeffrey
    j "Hei setidaknya sekarang sudah baik-baik sa-"
    a "UAAAAH!!" with vpunch #sfx sword?
    j "Alios!! Apa yang kau lakukan?! Ka... kau membunuhnya!!"
    #Jeffrey out & Alios M in
    #*Angry face M Alios
    al "Aku tidak membutuhkan orang yang tidak berguna!!"
    b "Ti... tidak tolong jangan bunuh aku...! Kasihani aku...!"
    r "(Ini gila! Aku harus menghentikannya!)"
    al "Kalau kau memang mau kumaafkan, kau harus menjadi lebih berguna!!"
    b "A... aku mengerti! Aku tidak akan kabur lagi! A... aku akan menghadapi musuh dengan mempertaruhkan nyawaku! Ja... jadi..."
    #*Happy face M Alios
    al "Hahaha! Bagus, bagus, kau akan mempertaruhkan nyawamu kan?"
    #*Smirk face M Alios
    al "Kalau begitu sekarang saatnya."
    r "He... hei!!"
    #*Normal face M Alios
    al "Apa masalahmu anak baru?"
    r "Kau tidak bisa bersikap seenaknya seperti itu! Kau adalah pemimpin kan?!"
    #*Angry face M Alios
    al "Hah?! Apa kau punya masalah denganku?! Apa kau menentang caraku?!"
    r "(Tentu saja! Tidak mungkin aku membiarkan pembunuhan apapun yang terjadi!)"
    al "Katakan sesuatu!!"
    #Elena L in
    #*Angry face L Elena
    e "Tentu saja kami menentang hal itu! Kau telah membunuh seseorang!"
    al "Jeffrey!! Beritahu mereka peraturan di tempat ini!! Kalau kalian masih ingin berada di sini, sebaiknya jangan pernah melawanku!!"
    #*Surprise face L Elena
    e "...!"
    #Alios out & Jeffrey R in
    #*Sad face R Jeffrey
    j "Maaf semuanya, kalian harus menyaksikan hal mengerikan seperti itu..."
    #*Sad face L Elena
    e "..."
    r "..."
    #All out
    r "(Kalau aku tetap berada di sini... mungkin saja akan membahayakan hidupku...)"
    menu:
        "Menetap di sini":
            r "(Kalau Aku tetap berada di sini…mungkin saja akan membahayakan hidupku…)"
            jump branch1

        "Pergi sendiri":
            r "..."
            r "(Aku tidak bisa mengikuti perintah dia.)"
            jump branch2

    return
