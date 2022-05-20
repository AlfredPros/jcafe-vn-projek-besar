
label branch3:

    #Chapter 1
    #“Kabur Bersama” with dissolve(1.0)

    #scene BG di kantin, day dissolve(1.0)
    r " Haduh, demi melakukan rencana ini aku harus bangun pagi ini."
    #show normal elena as elena di tengah
    e "Sst, rencana ini harus dilakukan sekarang atau kita akan gagal. Seriuslah dari sekarang"
    r "Baiklah. Sekarang kita sarapan dahulu, ada yang mau aku lakukan."
    #show normal elena as elena di tengah
    e " ok."
    #hide elena
    #show normal jeffrey  as jeffrey di kanan
    j "Hei kalian berdua, makanlah yang banyak. Ada yang akan kita lakukan setelah hal ini."
    #show happy elena as elena di kiri
    e "Waah. semuanya terlihat enak, ya kan Remil?"
    r " *Nyam… nyam… kraus… kraus… gulp*"
    #show laugh jeffrey  as jeffrey di kanan
    j "Memang tidak ada yang bisa mengaturmu, kecuali daging yang manis."

    #Black screen dissolve 1 sec

    r "Ugh… Kenyang sekali…"
    #show normal elena as elena di tengah
    e "Hei, kamu tidak apa-apa? Jika sakit perut, istirahat dulu saja. Rencana tersebut akan kita laksanakan di esok hari."
    menu:
        "Iya, aku tidak apa-apa. Jangan hiraukan aku dan lanjutkan rencana ":
            jump b3deca
        "Uh, aku hanya mual. Aku masih sanggup untuk mengikuti rencana.":
            jump b3decb
    return


label b3deca:
    #show serious elena as elena di tengah
    e "Apa kamu yakin? Sepertinya orang itu ingin membawa kita ke tempat berburu"
    #show normal jeffrey  as jeffrey di kanan
    j "Biarkan dia, Elena. Dia hanya akan mengambil terlalu banyak kesenangan. Nanti, dia akan merasa kelaparan sebentar lagi."

    #Black screen with Dissolve(1.0)
    #scene BG Hutan 1, day with dissolve(1.0)
    #(Scene melihat monster musuh)
    #show normal jeffrey  as jeffrey di kiri
    j "Itu adalah musuh yang akan kita lawan. Hei pria hebat (Remil), hadiahnya adalah daging monster itu. Aku akan bantu dengan pasukanku yang lainnya."
    r "Dengan senang hati"
    #show normal elena as elena di kanan
    e "Hati-hati. Bekerjasamalah, Remil."
    #hide jeffrey

    #Scene Elena mendekati Remil berbisik
    #show serious elena as elena di tengah
    e "Menurutku, kita bisa keluar dari hutan ini. Tidak jalankan rencana, dan keluar dari pepohonan ini."
    r "Kenapa kamu bisa seyakin itu?"
    #show serious elena as elena di tengah
    e "Hutan itu sangat luas. Bukannya itu adalah hal yang menguntungkan jika ingin kabur?"
    r "Bisa saja kita akan diincar oleh monster itu, bukan?"
    #show normal elena as elena di tengah
    e "Manusia lebih menakutkan daripada monster itu. Alios membunuh bawahannya sendiri."
    r "Walaupun…."
    #show serious elena as elena di tengah
    e "Aku tidak rela kalau kamu mati melawan monster itu daripada kabur. Sekarang, pilihlah."
    menu:
        "Kabur melalui hutan":
            jump b3decaa
        "Melawan monster":
            jump b3decab

    return

label b3decaa:
    r "Ayo kita kabur melalui hutan."
    #show normal elena as elena di tengah
    e "Pilihan yang bagus. Sepertinya monster itu harus kita bunuh. Jeffrey memantau kita."
    r "Baiklah, saatnya bekerjasama."
    "(Tidak butuh waktu lama sampai monster itu berhasil dikalahkan Remil dan Elena.)"
    r "Ayo, Elena. Kita kabur"
    #show normal elena as elena di tengah
    e "Mereka tidak akan melihat kita kan?"
    r "Tentu saja, monster ini sangat besar, dan kita ditutupi oleh badannya yang besar itu. Belum lagi, dirinya akan dihajar oleh Alios karena banyaknya pasukan yang mati."
    #show normal elena as elena di tengah
    e "Baiklah. Ayo kita lakukan dengan cepat."
    # scene BG Hutan, day to noon 12 ish
    #show normal elena as elena di tengah
    "Menurutmu, berapa lama kita akan berjalan di semak-semak ini?"
    r "Sampai kita tidak melihat hijau lagi, Elena. Bertahanlah"

    #Black Screen. Dissolve(1.0)
    #scene BG Hutan 1, night
    r "Huft-huft, akhirnya kita diluar. Elena, apa kamu tidak apa-apa? Perjalanan melalui hutan ini sangat panjang."
    #show normal elena as elena di tengah
    e "Ya, aku tidak apa-apa. Terima kasih. Untuk sekarang, apa yang harus kita lakukan"
    r "Bagaimana kalau kita menggunakan kuda yang ada disana untuk melanjutkan perjalanan?"
    #show normal elena as elena di tengah
    e "Baiklah."
    r "Percayalah kepadaku. Kita akan menemukan sesuatu yang lebih bagus."

    # scene Black screenwirh  Dissolve(1.0)
    jump b3ch2
    return

label b3decab:
    r "Aku rasa aku sanggup membunuh monster itu. Lagipula, dagingnya terlihat lezat"
    #show serious elena as elena di tengah
    e "Hei. Monster itu beracun."
    r "Darimana kamu tahu hal tersebut?"
    #show serious elena as elena di tengah
    e "Banyak orang yang menyerangnya. Dan mereka mengkonsumsi monster tersebut. Semuanya mati dalam keadaan mulut terbuka"
    r "Oh ya, kamu benar. Kalau begitu kita tidak bisa membunuh monster itu."
    r "Berarti pilihan kita hanya kabur melalui hutan."
    jump b3decaa
    return


label b3decb:
    #show sad elena as elena di tengah
    e "Kamu serius? Kita bisa menunda untuk pergi loh."
    r "Tidak, sekarang adalah kesempatan yang baik. Kamu sendiri yang bilang kalau tidak dilakukan sekarang kita akan gagal kan?"
    #show serious elena as elena di tengah
    e "Benar juga, kalau begitu sebelum ada yang sadar, ayo kita pergi."
    #hide elena
    #show normal jeffrey as jeffrey di kanan
    #show serious elena as elena di kiri
    j "Hei kalian mau kemana? Kalau sudah selesai makan, ayo ikuti aku."
    #show suprise elena as elena di kiri
    e "Aaah!"
    r " …"
    #show suprise jeffrey as jeffrey di kanan
    j "Kenapa kalian kaget begitu?"
    #show suprise elena as elena di kiri
    e "Ba… Bagaimana ini terjadi?"
    #show sad jeffrey as jeffrey di kanan
    j "Apakah ada yang kalian sembunyikan? Kelihatan mencurigakan… Apa ‘jangan-jangan’ karena kejadian kemarin?"
    r " …"
    #show sad elena as elena di kiri
    e "Sebenarnya kami…"
    #show sad jeffrey as jeffrey di kanan
    j "Haah… aku tahu, kalian pasti takut setelah kejadian itu kan?"
    #show sad elena as elena di kiri
    e "Iya. Kami tidak siap untuk melihat pembunuhan."
    #show sad jeffrey as jeffrey di kanan
    j "Karena itu kalian berniat untuk lari ya?"
    #show suprise elena as elena di kiri
    e "Huh?!"
    r "(Bagaimana dia bisa tahu?!)"
    #show normal jeffrey as jeffrey di kanan
    j "Aku paham. Lagipula aku yang memaksa kalian kemari, kalau kalian mau pergi, aku akan membantu."
    #show suprise elena as elena di kiri
    e "Serius? Apa tidak masalah?"
    j "Aku juga merasa tindakan Alios kemarin tidak manusiawi. kalian bisa bilang aku berada di pihak kalian."
    r "Kamu serius?"
    #hide jeffrey
    #hide elena
    #show happy elena as elena di kanan
    #show happy jeffrey as jeffrey di kiri
    j "Tenang saja, aku serius! Kalian tunggu saja di luar hutan sana, aku akan mempersiapkan kebutuhan kalian."
    e "Terima kasih banyak Jeffrey."

    #scene BG hutan 1, day
    #show happy elena as elena di tengah
    e "Wah aku tidak menyangka Jeffrey akan melakukan itu untuk kita."
    r "Aku juga tidak menyangka."
    #show normal elena as elena di tengah
    e "Omong-omong perutmu sudah tidak sakit?"
    r "Ya. Aku sudah tidak apa-apa."
    j "Hei kalian"
    #show happy elena as elena di tengah
    e "Itu dia!"
    r "Kenapa dia menaiki kuda?"
    #hide elena
    #show happy jeffrey as jeffry di kanan
    j "Ini tas berisi perlengkapan dan bekal untuk kalian. Lalu gunakan kuda ini untuk menjauh dari sini."
    #show normal elena as elena di kiri
    e "Remil apa kamu tahu cara berkuda?"
    r "Tentu saja tidak, aku tidak pernah…"
    j "Tenang saja ini lebih mudah daripada yang kalian pikirkan!"
    r "Aku harap seperti itu…"
    #show normal jeffrey as jeffry di kanan
    j "Kalian pergilah kesana. Kudengar di sana ada semacam desa."
    r "Desa?"
    j "Tidak ada waktu untuk menjelaskan, cepatlah pergi dari sini!"
    e "Terima kasih banyak, Jeffrey."
    r " …Terima kasih."
    #show happy jeffrey as jeffry di kanan
    j "Sama-sama! Sekarang pergilah!"

    #scene Black Screen with Dissolve(1.0)
    return

label b3ch2:
    #Chapter 2
    #“Kai Yang Aneh” with dissolve(1.0)

    #scene BG di hutan 1, day
    #show sad elena as elena di tengah
    e "Sudah berapa lama sejak kita pergi? Dan bekal kita sudah semakin menipis…"
    r " Bertahanlah sebentar lagi."
    #show normal elena as elena di tengah
    e "Iya, aku yakin aku bisa bertahan. 1 hari, dan tidak lebih."
    #hide elena

    #scene BG desa Kai, day with dissolve(1.0)
    r "Kita telah sampai."
    r "Aku sangat lelah. Tenagaku habis."
    #play sound gedebruk
    #use vpunc/hpunch
    #show normal kai as kai di tengah
    k "Jauhkanlah dirinya dari mara bahaya, dengan kekuatan Albert Einstein dan semacamnya, lindungilah dirinya."
    #show seriousl kai as kai di tengah
    k "Hei, kalian! Cepat bantu dia untuk mendapatkan penginapan yang layak. Lihat ini Karl, seseorang yang memerlukan bantuan telah dibantu dengan kekuatan sosial."
    #hide kai
    #show normal elena as elena di kanan
    e "(Orang ini gila ya? Tapi dia membantu Remil. Aku harus mengikutinya.)"
    e "(Bagaimana caraku mengikutinya? Apa menggunakan cara bodoh akan berhasil? Aku coba saja)"
    #show begging elena as elena di kanan
    e "Duh, aku merasa pusing. Apakah aku bisa mendapatkan dukungan darimu?"
    #show normal elena as elena di kanan
    e "(Apakah aktingku bagus?)"
    #show happy kai as kai di kiri
    k "Tentu saja. Aku tidak akan menolak kesempatan untuk membantu orang lain."
    #show normal kai as kai di kiri
    k "Bawa orang itu dan wanita ini kerumahku."

    #scene BG dalam rumah Kai. With Dissolve(2.0)
    #show normal kai as kai di tengah
    k "Istirahatlah dengan tenang. Pria ini hanya tidak punya stamina lagi, sama sepertimu."
    k "Apa ya yang harus ku masak…"

    #scene BG dalam rumah Kai with Fade(1.0)
    #show normal kai as kai di tengah
    k "Pagi semuanya, oh kamu bangun terlebih dahulu."
    r "Oh… Kamu siapa? Aku dimana?"
    k "Namaku Kai. Dulunya aku adalah ********* bidang ***** yang menciptakan area ***** dan ***** dari dunia ***** ini. Aku tahu bahwa kamu tidak percaya, jadi lupakanlah."
    r "(Apa yang dia bilang? Aku tidak dapat mendengarnya)"
    k "Kamu belum makan beberapa hari bukan? Makanlah yang puas sekarang. Aku sudah menyiapkan seluruhnya."
    menu:
        "Dimana Elena ?":
            jump b3deca2
        "Aku tidak dapat mendengarmu":
            jump b3decb2
    return

label b3decb2:
    r "Maaf, aku tidak dapat mendengar perkataanmu. Dulunya kamu seorang apa?"
    #show normal kai as kai di tengah
    k "Oh, tentu saja kamu tidak dapat mendengarnya. Aku lupa hal itu. Anggap saja aku adalah orang hebat."
    r "Kenapa? Itu adalah hal yang sangat aneh"
    #show sad kai as kai di tengah
    k "Semua orang mengatakan bahwa aku orang gila karena mereka mendengar hal yang kamu tanyakan. Lupakan saja."
    jump b3deca2

label b3deca2:
    r "Izinkan aku ucapkan terima kasih. Apakah kamu melihat temanku, seorang wanita?"
    #show normal kai as kai di tengah
    k "Iya, aku sudah menyiapkan kamar kalian secara terpisah. Dia hanya kelelahan, tenang saja."
    r "Baiklah, kalau begitu izinkan aku makan terlebih dahulu."
    #hide kai
    #show normal kai as kai di kanan
    #show normal elena as elena di kiri
    k "Akhirnya, gubuk ini diisi ******* lagi. Mulai aktif seperti dunia ***** yang memiliki burung berkicau dan anjing menggonggong."
    e "Terima kasih karena telah membantuku dan Remil. Aku ucapkan terima kasih"
    k "Kamu terlalu sopan untuk orang yang tidak religius."
    #show confused elena as elena di kiri
    e "(Uh, masih saja aku tidak mengerti bahasanya)"
    #show normal elena as elena di kiri
    e "Mil, siapa nama orang ini?"
    r "Namanya adalah Kai. Dia mengatakan bahwa dirinya orang yang sangat hebat, tetapi disini dia sering dipanggil orang gila. Dan menurutku juga dia gila."
    #show suprise elena as elena di kiri
    e "Jangan mengejutkanku! Aku juga merasa kamu gila."
    #show laugh kai as kai di kanan
    k "HAHAHA, sudah lama aku tidak dipanggil gila didepan mataku. Terima kasih. Para ********* memang orang gila."
    #show serious elena as elena di kiri
    e "HAH? Suara apa itu? Aku tidak mengerti."
    r "Suara itulah yang membuat dirinya gila. Aku rasa ia ingin mengatakan sesuatu, tetapi ia tidak diperbolehkan."
    #show suprise elena as elena di kiri
    e "Benarkah?! Coba lakukan sekali lagi!"
    #show happy kai as kai di kanan
    k "***** ***** ****** *****!"
    e "Woah aku sama sekali tidak bisa mengerti perkataannya!"
    #show normal elena as elena di kiri
    e "Sekarang aku jadi penasaran apa yang ingin kamu katakan sebenarnya?"
    #show sad kai as kai di kanan
    k "Tidak akan ada yang mengerti. Tidak ada yang paham, padahal aku berusaha untuk *****!"
    #show sad elena as elena di kiri
    e "Aku jadi merasa kasihan padamu."
    r "Memang apa yang ingin kamu katakan sebenarnya?"
    k "Kamu juga tidak akan mengerti, tapi biar kuberitahu kalian."
    #show serious kai as kai di kanan
    k "Dunia ini adalah *****. Kalian harus ambil ***** di ***** dan bawa kemari."
    #show normal elena as elena di kiri
    e " …."
    r " …"
    #show sad kai as kai di kanan
    k "Sudah kuduga!"
    #show normal elena as elena di kiri
    e "Ta.. tapi kalau pelan-pelan kami mungkin bisa mengerti!"
    #show serious kai as kai di kanan
    k "Yang ingin kukatakan adalah kalian perlu ke ***** untuk mengambil ***** lalu kembali!"
    r " …"
    r "Aku rasa percuma…"
    #show sad kai as kai di kanan
    k "Sudah kuduga… Urgh ini sungguh mengesalkan!"
    #show serious elena as elena di kiri
    e "Kai, coba ucapkan sekali lagi! Kami pasti akan mengerti."
    r "Hei kamu benar-benar tidak pantang menyerah ya?"
    #show serious kai as kai di kanan
    k "Baik. Jadi ada ***** yang terkubur dalam *****, kalian perlu menggalinya dan bawa kemari."
    #show normal elena as elena di kiri
    e "Terkubur di mana?"
    r "Menemukan apa?"
    k "***** ****! ***** ****!"
    r " …"
    r "Lagipula kenapa kamu tidak mencarinya sendiri? Kurasa itu sesuatu yang hanya kamu tahu."
    #show sad kai as kai di kanan
    k "Tidak bisa, aku tidak bisa mendekati benda itu karena tembok *****."
    #show suprise elena as elena di kiri
    e "Kurasa semua orang punya masalahnya sendiri."
    r "Jadi kami yang harus menemukan benda itu untukmu?"
    #show suprise kai as kai di kanan
    k "Tidak, anak muda! Ini demi kalian!"
    r "Demi kami?"
    k "Hei aku tahu sesuatu!!"
    e "Woah kamu mau ke mana?!"
    #hide kai
    #hide elena
    r "Dia pergi…"
    #show suprise elena as elena di tengah
    e "Dan… dia kembali membawa sesuatu!"

    #hide elena
    #show happy kai as kai di kanan
    k "Ini! Ini!"
    r "Apa itu?!"
    #show suprise elena as elena di kiri
    e "Pasir…?"
    r "Kenapa dengan pasir?"
    #show serious kai as kai di kanan
    k "Kalian perlu ke *****!"
    #show confuse elena as elena di kiri
    e " …"
    r " …"
    r " (Pantas saja dia disebut gila)"
    #show sad kai as kai di kanan
    k "Sudahlah, mau bagaimanapun kalian tak akan mengerti."
    #show sad elena as elena di kiri
    e "Maafkan aku…"
    #show laugh kai as kai di kanan
    k "Bukan masalah! Toh memang semua orang menganggapku gila, hahaha!"
    #show normal kai as kai di kanan
    k "Ngomong-ngomong kalian sudah selesai makan, aku akan bereskan piringnya dulu."
    #show normal elena as elena di kiri
    e "Ah terima kasih."
    #hide kai
    #hide elena

    #show normal elena as elena di tengah
    e "Remil, Menurutmu soal perkataan Kai…"
    r "Ucapannya memang sangat aneh dan kurang bisa dimengerti, tapi entah kenapa aku merasa kita harus mencoba mencari tahu soal hal itu."
    e "Kamu benar, kata Kai itu terkubur dalam entah-apa-itu, tapi di mana ya?"
    r "Hm…"
    r "Ah! Apa jangan-jangan ada kaitannya dengan yang dia bawa tadi?"
    #show suprise elena as elena di tengah
    e "Maksudmu pasir?"
    r "Apa mungkin dia mau bilang kalau benda itu terkubur di dalam pasir?"
    e "Mungkin saja begitu! Jadi… mungkin di sekitar pantai?"
    r "Atau mungkin ada di padang gurun,"
    #show happy elena as elena di tengah
    e "Remil kamu jenius! Lagipula padang gurun memang menyimpan banyak misteri!"
    r "Bagaimana kamu tahu soal itu?"
    #show normal elena as elena di tengah
    e "Maksudku, di sana pasti ada semacam piramid kan?"
    r "Apa maksudmu? Jangan-jangan kamu sudah ikutan gila?"
    #show suprise elena as elena di tengah
    e "Tidak kok! Tapi… piramid itu apa ya?"
    r "Sudah tidak usah dipikirkan lagi. Kita harus tahu di mana gurun itu sekarang."
    #hide elena
    #show normal kai as kai di kanan
    k "Kenapa kalian tampak semangat sekali?"
    #show normal elena as elena di kiri
    e "Kami sedikit paham maksudmu tadi, apakah kamu ingin bilang gurun?"
    #show suprise kai as kai di kanan
    k "*****! Itu yang sejak tadi ingin kukatakan!"
    r "Kurasa tebakan kita benar…"
    #show happy elena as elena di kiri
    e "Kai, apa kamu tahu di mana arah gurun itu?"
    #show happy kai as kai di kanan
    k "Ya, tentu! Kalian hanya perlu melewati ****!!"
    #show sad kai as kai di kanan
    k " …."
    #show nervous elena as elena di kiri
    e "Tampaknya kita perlu menebak apa yang ingin dia ucapkan lagi."
    r "Kenapa orang ini sangat merepotkan?"
    #show suprise kai as kai di kanan
    k "******, *******! ****** **** *****!"
    r "Haah… sepertinya kita harus menunda untuk pergi sampai memahami apa yang ingin ia katakan."

    #scene Black Screen with Fade(1.0)
    #show normal elena as elena di kiri
    e "Baik, akan ku ulangi sekarang… Kita harus pergi ke Utara melewati lembah dan plateau sampai menemukan gurun, lalu di tengah gurun adalah tempat jawaban yang kita cari?"
    #show happy kai as kai di kanan
    k "Benar!"
    #show happy elena as elena di kiri
    e "Asik akhirnya kita berhasil menerjemahkannya!"
    r "Tidak kusangka satu kalimat itu memakan waktu seharian untuk ditebak…"
    #show normal kai as kai di kanan
    k "Sekarang sudah malam jadi kalau kalian ingin pergi sebaiknya besok saja.."
    #show normal elena as elena di kiri
    e "*Hoam*  aku juga sudah mengantuk,"
    r "Kalau begitu, selamat malam."
    k "Ya, selamat malam."

    #scene Black Screen with Dissolve(1.0)

    #show happy kai as kai di tengah
    k "Selamat pagi semua! Apa kalian sudah siap untuk pergi?"
    r "(Uugh… dia semangat sekali walau masih pagi.)"
    k "Aku sangat senang bisa membantu kalian. Ini sudah ku siapkan sarapan, dan aku juga sudah memasok bekal untuk kalian. Dan aku akan menuliskan catatan untuk membantu perjalanan kalian."
    r "Woaah…"
    #hide kai
    #show normal elena as elena di kiri
    e "Terima kasih banyak Kai, aku penasaran kenapa kamu sebaik ini pada kami."
    #show laugh kai as kai di kanan
    k " Hahaha! Sudah sewajarnya aku harus bertanggung jawab!"
    #show confuse elena as elena di kiri
    e "Bertanggung jawab untuk apa?"
    #show happy kai as kai di kanan
    k "Karena kalian teman-teman baruku, yang datang kemari dan harus kubantu."
    " …?"
    r "Sudahlah Elena, kamu tahu ucapannya sulit dipahami kan?"
    #show normal kai as kai di kanan
    k "Kamu benar! Sudah, sudah tidak usah terlalu dipikirkan! Makanlah, makan!"
    #show normal elena as elena di kiri
    e "Baiklah… terima kasih."


    #scene BG desa Kai, day with Fade(1.0)
    #show normal kai as kai di tengah
    k "Semuanya sudah siap kan?"
    r "Sudah, dan terima kasih untuk catatannya."
    #show happy kai as kai di tengah
    k "Ya, ada beberapa tempat yang berbahaya jadi sering-seringlah baca catatan yang kuberikan."
    #hide kai
    #show normal elena as elena di kiri
    e "Kami akan berangkat sekarang. Terima kasih sudah merawat kami selama dua hari ini."
    #show happy kai as kai di kanan
    k "Tidak masalah. Dan jangan lupa untuk kembali setelah kalian mendapatkan apa yang ada di ***** itu!"
    #show happy elena as elena di kiri
    e "Tentu saja! Sampai jumpa, jaga dirimu."
    k "Sampai jumpa!"


    #scene Black Screen with dissolve(1.0)

    #Chapter 3
    #“Perjalanan Ke Gurun” with dissolve(1.0)

    #scen BG lembah, day. With dissolve(1.0)
    #show happy elena as elena di tengah
    e "Wah tempat ini bagus sekali ya!"
    r "Kurasa kita bisa istirahat sebentar di sini."
    e "Ide bagus. Ah! Di sana ada mata air, mungkin kita bisa istirahat di sana saja? Perjalanan kemari telah membuat air yang kita bawa hampir habis."
    r "Mata air yang di sana? Menurut catatan yang diberikan Kai, tempat itu mungkin saja dekat dengan sarang monster yang mengerikan."
    #show suprised elena as elena di tengah
    e "Eeeh?! Kalau begitu sebaiknya cari tempat lain saja…"
    r "Tapi kita butuh airnya. Mungkin kita hanya mengisi botol kita lalu langsung pergi saja."
    #show nervous elena as elena di tengah
    e "Apa akan baik-baik saja?"
    r "Kai memberi kita pisau. Kita bisa menggunakannya sebagai senjata."
    e "Well kalau begitu mari kita dekati mata air itu."

    #CG mereka depan mata air. With dissolve(1.0)
    e "Wah segar sekali!"
    r "Ayo segera isi botolnya sebagai air minum tambahan sebelum pergi dari sini."
    e "Tunggu, aku mau cuci muka juga…"
    r "Hei jangan lama-lama!"
    e "Sebentar saja…"

    #scene BG lembah, day. With fade(1.0)
    #show suprise elena as elena di tengah
    e "Uaaah apa itu?!"
    r "Elena hati-hati!"
    e "Remil jangan sakiti dia!"
    r "Huh?! Tapi bukannya kamu diserang…?"
    #show sad elena as elena di tengah
    e " Aku cuma kaget karena makhluk itu muncul tiba-tiba."
    #show normal elena as elena di tengah
    e "Dan kalau kamu perhatikan, dia ini masih anak-anak. Tidak boleh disakiti!"
    r "Menurut catatan Kai, setelah monster itu tumbuh besar dia akan berubah menjadi ganas dan mengerikan."
    #show angry elena as elena di tengah
    e "Tapi yang ada di depanmu ini sekarang bukan makhluk ganas dan mengerikan bukan?!"
    r "Iya, iya, kalau begitu ayo kita pergi sebelum yang ganas muncul."
    #show normal elena as elena di tengah
    e "Baiklah, sampai jumpa makhluk kecil."
    r " … Aku tidak tahu kamu suka binatang."
    #show happy elena as elena di tengah
    e "Ya, sejak dulu aku selalu dibilang penyayang."
    r " Oleh siapa?"
    #show confused elena as elena di tengah
    e "Hm… entah lah? Aku hanya merasa begitu, tapi aku tidak bisa ingat."
    r "Aku juga merasa seperti melupakan sesuatu sejak kemarin."
    #show supprise elena as elena di tengah
    e "Kamu juga?!"
    r "Yah kalau kita melupakannya berarti itu tidak penting kan?"
    #show normal elena as elena di tengah
    e "Iya mungkin kamu benar."
    r "(Meski begitu, aku sangat ingin mengetahui apa yang sebenarnya tidak bisa kuingat ini.)"

    #scene BG di Plateau, dusk. With Fade(1.0)
    #show happy elena as elena di tengah
    e"Woaah, Remil lihat sunset disana!"
    r "Berarti kita harus segera cari tempat istirahat yang aman."
    #show angry elena as elena di tengah
    e "Kamu ini sejak kemarin selalu saja waspada! Sekali-kali nikmatilah matahari tenggelam!"
    r "Lalu mati karena diserang monster? Tidak terima kasih."
    #show sad elena as elena di tengah
    e "Tidak buruk kok bersantai sedikit. Lagipula selama berhari-hari ini kita sudah berhasil bertahan hidup kan?"
    r "Ya tapi itu di lembah. Menurut catatan Kai tempat ini lebih berbahaya daripada lembah itu. Untung saja monster di sini katanya tidak suka api, aku akan mencoba menyalakan api sekarang."
    #show normal elena as elena di tengah
    e "Remil, kamu memiliki kemampuan bertahan hidup yang tinggi ya."
    r "Apa maksudnya?"
    e "Kamu berhati-hati, teliti, dan jago membuat api."
    #show happy elena as elena di tengah
    e "Aku merasa aman karena ikut denganmu."
    r "Ini hanya pengetahuan dasar, semua orang juga bisa."
    #show normal elena as elena di tengah
    e "Sebenarnya sebelum bertemu denganmu di tepi sungai itu, aku hampir tidak bisa bertahan hidup."
    r "Ah… saat itu…"
    r "Aku terbangun di dekat sungai. Aku berusaha mati-matian bertahan hidup dan menghindari monster untuk mendapat makanan, sampai tiga hari kemudian aku melihatmu yang terluka."
    #show happy elena as elena di tengah
    e "Untung saja waktu itu aku terus mengikutimu! Jadinya aku tidak mati sendirian di sana, hahaha!"
    r "(Apa itu sesuatu yang bisa ditertawakan?)"
    r "Tapi kamu bilang terbangun di dekat sungai? Apa kamu ingat sesuatu sebelum itu?"
    #show confused elena as elena di tengah
    e "Sama sekali tidak ada."
    r "(Sama sepertiku, terbangun di tempat aneh dan tidak bisa ingat apapun yang terjadi sebelumnya)"
    #show normal elena as elena di tengah
    e "Ah mataharinya sudah hampir menghilang!"
    r "Kalau begitu sebaiknya kita siap siaga sekarang."

    # scene Black Screen. With Dissolve(1.0)

    #Chapter 4
    #“Benda Misterius” with dissolve(1.0)

    #scene BG di padang gurun, day. With Dissolve(1.0)

    r "(Kami tiba di padang gurun sekitar dua jam lalu, sudah lama berjalan dan sejak tadi sejauh mata memandang semuanya hanya pasir....)"
    r "Jangan jauh-jauh ya kita bisa kehilangan arah dan tersesat."
    #show normal elena as elena di tengah
    e "Tenang saja, kita hanya perlu terus berjalan lurus tanpa belok ke mana-mana"
    r "Menurut catatan Kai, kadang-kadang akan ada badai pasir dan bisa membuat kita hilang arah."
    #show suprised elena as elena di tengah
    e "Badai pasir?! Apa kita akan baik-baik saja?"
    r "Aku tidak tahu, jadi sebaiknya kita segera menemukan tengah gurun ini."
    #show normal elena as elena di tengah
    e "Tapi sejauh apa ya tengah gurun itu?"
    r "Aku juga tidak tahu, kenapa? Kamu mulai kelelahan?"
    #show nervous elena as elena di tengah
    e "Aku tidak kelelahan. Tapi aku takut air kita akan habis sebelum sampai ke tengah gurun."
    r "Berdoa saja kita menemukan oasis di pertengahan jalan nanti."
    #show happy elena as elena di tengah
    e "Apa di catatan Kai tertulis ada oasis di sini?!"
    r "Tidak ada."
    #show sad elena as elena di tengah
    e "Ooh…"
    #play sound  *Syuuuu* (suara angin)
    #show suprised elena as elena di tengah
    e "Hei!!"
    r " Badai pasir!!"
    r "(Baru saja dibicarakan, dan tiba-tiba badai pasirnya datang?!)"
    e"Remil pegang tanganku! Jangan sampai kita terpisah!"
    r "Tutup matamu!"

    #scene Black screen dissolve(1.0)

    r "Hei, Elena! Semua sudah baik-baik saja sekarang!"
    #show happy elena as elena di tengah
    e "Hahaha! Remil, badanmu penuh dengan pasir!"
    r "amu juga tahu! Dan sekarang bukan saatnya tertawa! Apa kamu lihat sesuatu di sana?"
    #show confuse elena as elena di tengah
    e "Hmm?"
    #show suprised elena as elena di tengah
    e "Aaah! Ada semacam puing-puing di sana! Apa ternyata kita sudah sangat dekat dengan jawabannya?"
    r "Sepertinya badai pasir itu membuat puing-puing itu jadi terlihat."
    #show happy elena as elena di tengah
    e "Bukankah berarti kita beruntung? Mungkin itu yang kita cari!"
    r "Semoga saja begitu. Ayo kita dekati tempat itu."

    #scene BG tengah gurun with Dissolve(1.0)

    #show confuse elena as elena di tengah
    e "Hmmm… kalau ini benar merupakan tengah gurun, berarti benda itu terkubur di bawah pedestal ini ya?"
    r "Kurasa begitu. Ayo coba kita gali."
    #show suprised elena as elena di tengah
    e "Loh kita punya sekop?!"
    r "Ya, Kai memberikannya waktu kita hendak pergi. Apa kamu lupa?"
    #show confuse elena as elena di tengah
    e "Well sudah berhari-hari kita pergi dan sekarang aku baru tahu kita punya sekop."
    r "Sudah tidak perlu dibahas lagi, ayo kita gali."
    #show happy elena as elena di tengah
    e "Serahkan saja padaku! Aku ini cukup kuat, loh!"
    r "Ya aku percaya. Karena tadi saat badai kamu mencengkramku sangat kuat sampai tanganku memerah."
    #show nervous elena as elena di tengah
    e "Ahahaha aku hanya takut kamu terbawa angin."
    r "Terima kasih."
    #show suprised elena as elena di tengah
    e "Hei kamu tidak perlu marah karena itu kan?"
    r "Aku tidak marah kok! Aku berterima kasih!"
    #show happy elena as elena di tengah
    e "Oke, oke aku percaya!"
    #hide elena

    #scene Black Screen with dissolve(1.0)
    #play sound digging
    "..Dug"

    #show suprised elena as elena di tengah
    e "Hei tampaknya aku mengenai sesuatu!"
    r "Apakah akhirnya kita berhasil menggalinya?! Cepat kita keluarkan benda itu!"
    #show happy elena as elena di tengah
    e "Woaah bendanya indah sekali!"
    r "Jadi ini benda yang Kai minta untuk kita cari…"
    e "Aku sangat senang perjalanan kita tidak sia-sia!"
    r "Ya, tapi setelah ini masih perlu jalan kembali ke desa itu."
    e "Tapi daripada padang gurun ini, lembah dan plateau itu jauh lebih baik kan?"
    r "Hehe kamu benar. Sini, biar kubawakan."
    #show happy normal as elena di tengah
    e "Sekarang kita tinggal berjalan balik sampai keluar gurun ini. Apa kamu masih punya tenaga?"
    r "Kalaupun aku kehabisan tenaga, kita harus berjuang agar bisa keluar dari gurun ini secepatnya. Kamu tidak mau pingsan kepanasan ataupun terkena badai pasir lagi kan?"
    e "Kamu benar. Aku tidak mau ada pasir di rambutku lagi."


    #scene Black Screen with dissolve(1.0)

    #Chapter 5
    #“Pertemuan Tak Terduga” with dissolve(1.0)

    #scene BG di Plateau, dusk to night. With dissolve(1.0)

    r "Akhirnya kita bisa santai sementara ketika berjalan pulang."
    r "(Aku juga merasa harus beristirahat lama)"
    #show  normal elena as elena di tengah
    e "Berikan saja terlebih dahulu kepadaku, Remil. Aku rasa kamu sudah tidak memiliki tenaga lagi untuk melakukan sesuatu."
    r "(memberikan alat tersebut)"
    e "Menurutmu, apakah ini adalah barang yang Kai maksud?"
    r "(Sejujurnya, aku pun merasa bahwa bukan ini barang yang diperlukan, tetapi entahlah)"
    r "Benda ini ada misteriusnya, dan aku rasa ini adalah benda yang benar."
    e "Baiklah kalau begitu. Aku akan menjaganya dengan baik. Kembali ke desa sangatlah jauh, bagaimana jika kita berdiam satu malam terlebih dahulu?"
    r "Ide bagus."
    #hide elena

    #scene BG Kelompok Alios camping. With fade(1.0)
    #show normal jeffrey as jeffrey di kanan
    j "Halo, halo. Sudah lama kita tidak bertemu."
    r "(Waduh.. Bagaimana bisa kita bertemu dengan Jeffrey kembali? Ini akan menjadi masalah)"
    r "Hahaha, halo."
    #hide jeffrey
    #show  normal elena as elena di tengah
    e " (Hei Remil, Apa yang harus kita lakukan?)"
    r "(Aku juga tidak tahu, Elena. Apakah kita harus kabur?)"
    #show normal jeffrey as jeffrey di kanan
    j "Aku rasa kalian perlu untuk menginap disini. Kami sedang berkemah disini. Jadi, silahkan saja menginap disini. Kami sangat membuka diri kepada kalian"
    r "Hmm, aku ingin mempercayaimu, tetapi aku tidak ingin bertemu dengan Alios."
    j "Percayalah kepada kami. Bukannya kami yang memberikan kalian makanan, benar kan Remil?"
    r "(Aku merasa ada yang aneh… lagipula, benda ini sepertinya lebih penting daripada penginapan ini. Kalau Alios tahu… entah apa yang akan dia lakukan untuk merebut benda ini dari kami.)"
    r "Maaf, tetapi sepertinya kita memiliki sesuatu malam ini. Kita harus pergi."
    #show serious jeffrey as jeffrey di kanan
    j "Serius? Baiklah. Pergi dari sini."


    #scen BG Lembah,Dusk. With fade(1.0)
    #show  normal elena as elena di tengah
    r "Maafkan aku, Elena. Kita jadi harus mencari tempat lain untuk beristirahat"
    e "Tidak apa-apa. Aku juga tidak dapat percaya kepada kelompok itu."
    r "(Aku juga)"
    #show  serious elena as elena di tengah
    e "Aku rasa kita sudah tidak aman lagi, bagaimana jika kita bergegas menuju desa dengan cepat? Malam ini kita akan gempur."
    r "(Itu bukan ide yang buruk, tetapi apakah kita punya tenaga sebesar itu?)"
    menu:
        "Bergegas langsung malam ini":
            jump b3deca3
        "Mencari tempat istirahat":
            jump b3decb3
    return

label b3deca3:
    #show  normal elena as elena di tengah
    r "Ayo. Aku rasa aku tidak punya tenaga yang kuat, apa kamu punya ide?"
    e "Bagaimana jika kita menunggangi kuda untuk lebih cepat sampai kesana?"
    r "Tapi kau tahu kan kuda kita juga sudah kelelahan sejak keluar dari gurun tadi…"
    e "Kamu benar. Sepertinya ide ini adalah ide gilaku agar kita cepat aman kedalam desa dan bertemu Kai."
    r "Tidak apa-apa. Semua ide harus kuhargai."
    jump b3decb3
    return

label b3decb3:
    r "Ayo kita mencari tempat istirahat. Kita sudah tidak punya tenaga yang besar karena perjalanan padang gurun."
    #show  normal elena as elena di tengah
    e "DImana? Tempat ini terlalu luas dan kita tidak bisa melakukan perkemahan yang enak."
    r "Kita bisa berkemah yang sederhana saja. Mungkin kita bisa membuat tempat istirahat di dalam hutan, bagaimana menurutmu?"
    e "Apakah itu adalah ide yang aman?"
    r "Aman, dari serangan manusia."
    e "Aku tidak bisa percaya."
    r "Aku akan menjaga di area hutan. Bagaimana?"
    #show happy elena as elena di tengah
    e "Ide yang bagus"

    #scene BG hutan 1, night. With dissolve 1sec)
    #show  normal elena as elena di tengah
    r "Tidurlah terlebih dahulu. Kita masih punya bendanya, bukan?"
    e "Ya, kita punya. Benda itu aman denganku, Remil. Aku tidur terlebih dahulu."
    r "Baiklah, aku akan menjaga daerah ini."

    #scene BG hutan 1, day. With fade(1.0)
    r "(Gawat aku ketiduran!)"
    r "Hei, Elena. Bangunlah!"
    #show confuse elena as elena di tengah
    e "Huuh, Remil?"
    r "Elena, apa benda itu masih ada?"
    #show normal elena as elena di tengah
    e "Oh. Tentu saja. Masih ada di sini kok…"
    r "(Untung saja…)"
    e "Kenapa panik begitu?"
    r "Tidak apa-apa, ayo kita bergegas kembali ke desa."

    #scene BG desa kai, day. With fade(1.0)
    #show normal elena as elena di tengah
    r " Apa bendanya masih aman?"
    e "Aku sudah menyimpannya di tempat yang aman. Tenang saja."
    r "Baiklah. Kalau begitu, kita akan melaporkannya kepada Kai."


    #scene BG Desa Kai. With fade (2.0)
    #show normal kai as kai di kanan
    #show normal elena elena di kiri

    r "Kai, ini adalah benda yang mungkin kamu cari."
    k "Berikan padaku. Aku akan mengeceknya."
    e "(Memberikan benda tersebut ke Kai)"
    e "Aku rasa sudah benar"
    k " Aku rasa benda ini salah. Ini bukan yang aku mau walaupun ********* ****"
    r "(Salah?!)"
    #show suprise elena elena di kiri
    e "Apa kamu serius?!"
    r "(Bendanya berbeda? Aku punya firasat yang buruk mengenai hal ini)"
    k "Benda ini sangat mirip tapi sebenarnya palsu, pasti ada yang menukarnya dengan yang asli.."
    r "(Jangan-jangan ini karena aku ketiduran kemarin?!)"
    #show sad elena elena di kiri
    e "Maaf… padahal aku bilang akan menjaganya…"
    r "Sepertinya ini salahku karena semalam tidak berjaga dengan benar, maafkan aku."
    k "Sepertinya kamu dimusuhi banyak orang ya."
    k "(Alat ini sepertinya dibuat khusus untuk memalsukan hal-hal seperti ini. Benar-benar pencuri yang jenius)"
    r "Sepertinya aku harus kembali."
    r " …"
    r "Elena, ini bukan salahmu."
    #show serious  elena elena di kiri
    e "Biarkan aku ikut bersamamu. Aku ingin menghajar mereka juga."
    r "Jangan. Aku masih belum yakin dan ini mungkin berbahaya. Biarkan aku melakukannya sendiri."
    #show normal elena elena di kiri
    e "Baiklah, tapi berjanjilah bahwa kamu akan pulang baik-baik saja."
    r "Tentu saja."
    r "(Aku juga tidak ingin menyelesaikan masalah dengan setengah-setengah)"



    #scene Black screen with dissolve(1.0)

    #Chapter 6
    #“Pertarungan” with dissolve(1.0)

    #scene BG Perkemahan Alios. Day. with Dissolve(1.0)
    #show normal jeffrey as jeffrey di tengah
    j "Wah, lihat ada yang datang kembali."
    r "(Dia semakin licik. Aku rasa saat ini aku harus lebih keras kepadanya)"
    r "Bagaimana jika aku langsung berbicara saja?"
    j "Kamu ingin kembali kedalam kelompok ini? Silahkan. Aku sangat menyukainya."
    r "Kembalikan benda yang bukan milikmu! Kenapa kau mencuri benda itu?!"
    #jeffrey manipulativ(?)
    j "Apa kau lupa? Dulu aku sengaja membiarkanmu kabur, itu karena aku dan Alios ingin mencari benda ini juga…"
    r "(Apa maksud dari semua ini?)"
    j "Ini benda yang kamu inginkan bukan?"
    "Jeffrey menunjukkan benda yang ditemukan Remil di Gurun."
    r "(Dia benar-benar memiliki benda aslinya!)"
    r "Dasar pencuri!!"
    #show laugh jeffrey as jeffrey di tengah
    j "Kamu menginginkannya kembali? Baiklah."
    #show normal jeffrey as jeffrey di tengah
    #jeffrey manipulativ(?)
    j "Kalau begitu lawan aku dan pasukanku dulu! Kita lihat seberapa serius kamu menginginkan benda ini… Hahaha"
    r "(Licik sekali. Dia benar-benar menikmati acara seperti ini)"
    r " Ayo datanglah kepadaku!!"
    #show serious jeffrey as jeffrey di tengah
    #jeffrey manipulativ(?)
    j "Hancurkan dia!"
    r "(Sepertinya aku tidak bisa menyerang tanpa rencana)"
    menu:
        "Menyerang prajurit terlebih dahulu":
            jump b3deca4
        "Menyerang Jeffrey ":
            jump b3decb4

    return

label b3deca4:
    #scene CG Remil mengincar prajuritnya. Menampilkan Jeffrey di belakang prajurit. with Dissolve(1.0)
    r "(Aku akan mengalahkan prajuritnya dulu)"
    r "(Aku akan mengincar secara jumlah. Masalah ini akan selesai dengan cepat)"
    #scene CG Remil berdiri dan prajurit semua tewas. Menampilkan Jeffrey. With fade(2.0)
    j "Kamu memang ingin duel denganku ya…"
    r "(Ada yang ingin kutanyakan padanya…)"
    r "Kenapa kau dan Alios menginginkan benda itu?"
    j "Mau tahu? Dulu Pria gila di desa itu memberitahu kami soal benda itu… Alios menginginkannya, jadi aku akan menghadiahkan untuknya."
    r "(Dasar penjilat, aku akan mengalahkanmu secepat mungkin!)"
    # scene CG Remil menang melawan Jeffrey. Remil terluka. With fade(1.0)
    r "Akhirnya aku menang…"
    al "Hei ada ribut-ribut ap…"
    al "APA YANG KAMU LAKUKAN PADA TEMPATKU?"
    r " Aku hanya merebut kembali milikku."
    al "Dasar monster!!"
    r "Aku masih punya kekuatan untuk menghancurkanmu."
    al "Tolong ampuni aku…"
    r "(Baguslah. Tanpa pasukannya dia sangat menyedihkan.)"
    r "Pergilah! Dan jangan kembali ke area ini lagi."
    al "Aku.. Aku tidak akan memaafkanmu!"
    r "Saatnya pulang, kembali dengan benda ini."
    jump b3ch7
    return

label b3decb4:
    #scene CG Remil mengincar Jeffrey. Tidak ada prajurit. Jeffrey muka emosi. with Dissolve(1.0)
    r "(Aku hanya harus menghancurkan intinya, bukan)"
    r "Hei, Jeffrey. Aku tahu kamu mencurigakan sejak awal…"
    j "Oh? Aku membiarkanmu lolos dulu, tapi itu demi rencanaku sih… hahaha."
    r "Rencana?!"
    j "Alios menginginkan benda itu, aku merasa bisa memanfaatkanmu untuk mendapatkan benda ini.."
    r "Dasar licik. Ayo datang kesini dan lawanlah aku"
    j " Atas dasar apa?"
    r "Kejantanan. Daripada kamu bermain seperti orang licik terus menerus, kan?"
    j "Aku tidak licik. Aku hanya pintar"
    r "Kalau begitu kamu pintar tapi penakut."
    j "Apa maksudmu?"
    r "Kamu membawa pasukan dan tidak berani berduel denganku."
    j "Heh, Baiklah. Ayo kita bertarung. Jangan salahkan aku jika kamu akan mati ditanganku"
    r "Ayo kita lakukan."

    #scene CG Remil menang melawan Jeffrey. Remil terluka. With fade(2.0)
    r "Akhirnya aku menang..."
    al "Hei ada ribut-ribut ap…"
    al "APA YANG KAMU LAKUKAN PADA TEMPATKU?"
    r "Aku hanya merebut kembali milikku."
    al "Dasar monster!!"
    r "Aku masih punya kekuatan untuk menghancurkanmu."
    al "Tolong ampuni aku…"
    r "(Baguslah. Tanpa pasukannya dia sangat menyedihkan.)"
    r "Pergilah! Dan jangan kembali ke area ini lagi."
    al "Aku.. Aku tidak akan memaafkanmu!"
    r "Saatnya pulang, kembali dengan benda ini."
    jump b3ch7
    return

label b3ch7:
    #Chapter 7
    #“Kembali” with dissolve(1.0)

    #BG desa Kai, day With fade(2.0)
    r "Kai, aku berhasil mendapatkan benda ini lagi."
    #show suprise kai as kai di tengah
    k "Hei kamu babak belur!"
    r "Ya… ada sedikit pertarungan tadi."
    #hide kai
    #show nervous elena as elena di kiri
    e "Remil kamu tidak perlu sok kuat…"
    r "Tenang saja Elena,"
    r "Jadi bagaimana Kai?"
    #show normal kai as kai di kanan
    k "Tidak diragukan lagi, ini adalah benda yang asli."
    r "Kalau begitu sekarang apa?"
    k "Ikuti aku sekarang. Kalian tidak akan siap dengan apa yang akan terjadi nanti."
    r " Semoga ini bukan sesuatu yang buruk."

    #CG Pedestal di tengah desa With dissolve(1.0)
    e "Apa ini?"
    k "Aku akan menaruh benda ini di sana, lalu kalian bisa kembali."
    r "Kembali? Kemana?"
    k "Dunia **** kalian. Kalian seharusnya tidak berada di sini."
    e "Apa yang kamu katakan?"
    r "Apa ini… bukan dunia kami?"
    k "Ada orang jahat yang membawa kalian kemari."
    e "Huh?!"
    k "Tidak hanya kalian, aku yakin ada orang lain yang juga dipaksa kemari."
    r "Siapa orang yang membawa kami kemari?"
    k "Dulunya dia adalah rekanku. Tapi entah kenapa dia berubah menjadi jahat dan berkhianat. Saat kalian kembali nanti, kalian harus menyelamatkan yang lainnya juga."
    e "Tunggu dulu, kenapa kamu bicara seperti itu? Seakan kamu tidak ikut dengan kami…?"

    #scene BG desa Kai, day with dissolve(1.0)
    #show sad kai as kai di kanan
    #show normal elena as elena di kiri
    k "Meskipun aku ingin kembali, aku tidak mungkin bisa."
    e "Kenapa?"
    k "Aku sudah tidak ada di dunia ****. Aku tidak lain adalah bug, semacam system error."
    r ": Apa maksudnya?!"
    k "Semua terjadi begitu cepat. Yang kuingat aku disuruh menguji coba alat terbaru kami."
    #show norma kai as kai di kanan
    k " Sudahlah, tidak perlu mendengar cerita suramku. Kalian pasti sudah tidak sabar untuk kembali kan?"
    r "Aku tidak tahu… apa dunia asli kami lebih baik dari ini?"
    #show happy kai as kai di kanan
    k "Tentu saja kan? Dunia kalian punya segalanya, dan tidak ada monster. Kalian pasti lebih baik di sana."
    #show sad elena as elena di kiri
    e  "Ooh seandainya ada cara untuk membawamu kembali juga…"
    k "Sudah, sudah. Pesanku hanyalah, setelah kalian kembali, tolong beritahu semua kejahatan rekanku itu pada dunia. Agar tidak ada korban selanjutnya."
    r "Baiklah… akan kuingat pesanmu."
    k "Terima kasih, Remil. Kalau begitu benda ini akan langsung kutaruh. Lalu kalian segera pergilah lewat portal yang terbuka nanti."
    "Kai meletakkan benda itu, angin berhembus kencang dan muncul portal di depan mereka"
    #show normal kai as kai di kanan
    k "Selamat tinggal semuanya."
    r "Ya, selamat tinggal."
    e "Selamat tinggal Kai. Kami pasti akan melakukan apa yang kamu minta"
    #show happy kai as kai di kanan
    "Terima kasih Elena. Aku percaya pada kalian berdua, sampai jumpa."

    #White screen with dissolve(1.0)


    #Chapter 8
    #“Akhir Dari Semua” with dissolve(1.0)

    #CG fasilitas penelitian, ada Gordon duduk. Remil & Elena mau menghampirinya. With white fade(1.0)
    r "Kau…!"
    n "Wah, wah… Ada dua orang yang lolos?"
    e "A… aku ingat semuanya! Kamu adalah orang aneh yang menculik aku!"
    r "Kau juga menarikku dengan paksa untuk ikut denganmu!!"
    g "Ya, itu semua perbuatanku, Gordon."
    e "Apa tujuanmu?! Apa kau orang jahat yang disebut Kai?!"
    g "Kai? Kai katamu? Kukira aku sudah membereskan orang itu, ck."
    r "Apa yang kau gumamkan?!"
    g "Kai adalah orang yang membantuku untuk membangun taman bermain ini. Tapi tidak kusangka dia justru mau menghancurkan taman bermainku dari dalam."
    e "Taman bermain?! Kau menculik orang hanya untuk kesenanganmu?!"
    g "YA!"
    g "Aku membunuhnya karena dia menggangguku, kesalahanku membuat eksistensinya terperangkap dalam sistem."
    g "Aku berusaha memperbaiki masalah itu tapi kenapa dia masih ada di sana?!"
    g "Apa yang salah?! BAGIAN APA? APA YANG SALAH?!"
    e "Dasar orang gila! Kau bisa membunuh orang hanya untuk ini?! Kami akan melaporkan semuanya pada polisi!!"
    g "Polisi? ahaha… AHAHAHA.."
    e " Apa yang kau tertawakan?!"
    g "AHAHAHA…!!!"

    #scene Black Screen With fade(1.0)
    #scene BG Hitam


    #show normal gordon as gordon di tengah
    g "Sebelumnya aku hidup bahagia… keluarga yang saling menyayangi dan pekerjaan yang stabil…"
    g "Tapi tiba-tiba Kai teman lamaku mengajakku untuk membuat sistem, sistem di mana orang dapat masuk ke dalamnya sebagai hiburan atau rekreasi. Seperti game."
    #show smirk gordon as gordon di tengah
    g "Kupikir itu ide yang bagus dan sangat menarik. Aku terlena dengan pekerjaan itu, dan keluargaku…"
    #show angry gordon as gordon di tengah
    g "Keluargaku meninggalkanku karena aku terlalu fokus dengan Sistem itu!! Tempatku bekerja memecatku karena aku tidak bisa fokus!! Semua SALAH Kai yang mengajakku!! Tapi Kai tampak bahagia, dan dia tampak semangat sekali membuat sistem untuk MENYENANGKAN orang-orang!!"
    g "Angry face M Gordon : KENAPA?! Kenapa aku harus membuat sistem untuk menyenangkan orang lain sedangkan aku sendiri tidak bahagia?!"
    #show smirk gordon as gordon di tengah
    g "Jadi kuputuskan, aku akan sepenuhnya mengambil alih pekerjaan ini. Kai tidak perlu terlibat sama sekali. Dia bisa tidur saja untuk selama-lamanya…"
    #show evil laugh gordon as gordon di tengah
    g "DAN ITU YANG KULAKUKAN!! Aku mengembangkan sistem ini untuk menjadi taman bermainku!! Menculik orang dan memaksa mereka menjalani kehidupan yang kubuat! Menertawai mereka ketika saling membunuh atau terbunuh monster!!"
    g "Tidak ada yang lebih menyenangkan daripada ini!! AHAHAHA! AHAHAHAHAHAHA….!!!"

    #play sound *BRUUUK*

    #fade in
    #scene CG Gordon nyerang Remil, pisau depan lehernya
    e " REMIL!!!"
    r "Si… sial…!!"
    g "Aku sangat tidak senang kalau kalian pergi dari sini!! Hei wanita! Cepat lapor polisi kalau kau tidak masalah temanmu ini mati!!"
    e  "Dasar licik!!!"
    g "Hahaha aku tidak peduli apa yang mau kalian katakan. Sana pergi dan kau akan menemukan tubuh kaku anak ini besok!"
    e "U… urgh…!!!"
    r "Elena! Jangan pedulikan aku! Ini saatnya kamu untuk lari dan kabulkan permohonan Kai!"
    e "Mana mungkin aku bisa melakukannya?!"
    g "YA KAU TIDAK MUNGKIN BISA!! Karena itu kembali lah ke dunia virtual yang kubuat!! AHAHAHA!!!"
    r "Elena jangan dengarkan dia!"
    g "Elena kehidupan anak ini ada di tanganmu!!"
    e "A… apa yang harus kulakukan…?"
    r "Elena!!"
    g "ELENA!!!"

    menu:
        "Ikuti perkataan Remil":
            jump b3deca5
        "Ikuti perkataan Gordon":
            jump b3decb5
    return

label b3deca5:
    e "Remil… aku akan segera kembali!"
    r "Ya…"
    g "Jadi kau tidak peduli padanya, hah?!"

    #scene black
    e "(Aku berlari sekencang mungkin, meninggalkan fasilitas penelitian di bawah tanah itu. Begitu melihat cahaya matahari, aku langsung berteriak. Meminta pertolongan dan bantuan polisi…)"
    e "(Untungnya tempat itu berada di perkotaan. Tidak butuh waktu lama sampai polisi datang dan menggeledah fasilitas penelitian itu.)"
    e "(Gordon ditangkap. Sistem itu dimatikan dan korban penculikan lain yaitu Alios, Jeffrey, Cherry, dan beberapa orang lainnya kembali sadar. Tetapi Kai sudah menghilang sepenuhnya…)"
    e "(Dan Remil… Gordon tidak bohong soal akan membunuhnya. Begitu aku dan polisi tiba tubuh Remil sudah berlumuran darah. Aku sangat panik dan takut. Remil langsung dibawa ke rumah sakit…)"
    e "(Satu minggu sudah berlalu sejak kejadian mengerikan itu. Dan Remil…)"

    #fade in
    #scene (CG Remil di rumah sakit dengan perban di lehernya, Elena tersenyum)
    e "(...Remil akhirnya sadar dari koma.)"

    "(TRUE ENDING)"
    return


label b3decb5:
    e "Baik! Jangan sakiti Remil, kami akan ikuti perkataanmu"
    r "Elena!!"
    g "Bagus, bagus!! Kalau begitu mulai dari kau, kembali lah ke alatnya!"
    r " Hei Elena, jangan dengarkan dia!"
    e "Aku tidak mau ada pertumpahan darah di sini Remil, apalagi kalau yang mati adalah kamu!"
    r "Elena, percaya padaku! Apa kamu mau mengecewakan Kai?!"
    g "BERISIK!! HEI CEPAT KEMBALI KE ALATNYA!!"
    r "Uargh!"
    e "Hei jangan sakiti dia!!"
    g "KALAU BEGITU CEPAT!!!"
    r "Aku… mohon…!"
    e "Uuh… uh…"
    jump b3deca5
    return
