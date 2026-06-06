# -*- coding: utf-8 -*-
"""Romanian (ro) content for cam-streaming-guides."""

_T_ETH = ("Folosește conexiune prin cablu", "Ethernet bate Wi-Fi într-un stream lung — un frame "
          "pierdut e un tip pierdut. Trage un cablu până la PC-ul de stream.")
_T_TEST = ("Fă mai întâi un test privat", "Rulează o transmisiune scurtă de test pentru cameră, "
           "audio, încadrare și overlay-uri înainte să deschizi camera publicului.")

PLATFORMS_RO = [
    {"slug": "chaturbate", "name": "Chaturbate",
     "title": "Transmisie pe Chaturbate cu SplitCam — Token & RTMP",
     "desc": "Transmisie pe Chaturbate cu SplitCam gratuit — broadcast token, RTMP, scene multi-cameră și overlay-uri. Fără filigran.",
     "kw": "transmisie chaturbate, chaturbate broadcast token, chaturbate rtmp obs, chaturbate external encoder, chaturbate live",
     "h1html": 'Cum transmiți pe <span class="accent">Chaturbate</span> cu SplitCam',
     "h1short": "Transmisie Chaturbate",
     "card": "Configurare bazată pe token cu encoder extern pe Chaturbate.",
     "intro": "Chaturbate e una dintre cele mai mari platforme cam, construită pe economia tokenilor. Broadcasterul din browser e o cameră simplă — trecerea pe <strong style='color:var(--text)'>encoder extern</strong> cu <strong style='color:var(--text)'>SplitCam</strong> gratuit deschide scene multi-cameră, overlay-uri și filtre pe același stream bazat pe tokeni.",
     "quick": "Transmisie pe Chaturbate cu SplitCam: instalezi SplitCam, construiești scena, pe Chaturbate deschizi <em>Broadcast Yourself → My Broadcast</em>, copiezi broadcast tokenul, îl lipești în SplitCam, Go Live."
              "<ol><li>Instalează SplitCam.</li><li>Adaugă cameră + scenă.</li>"
              "<li>Copiază broadcast tokenul Chaturbate.</li><li>Lipește în SplitCam.</li>"
              "<li>Apasă Go Live.</li></ol>",
     "key_how": "Pe Chaturbate clic <strong>Broadcast Yourself</strong> pentru pagina <strong>My Broadcast</strong>, apoi <strong>View RTMP/OBS broadcast information and stream key</strong>. Cheia apare ca <strong>broadcast token</strong> — copiază. Tratează ca parolă; niciodată public.",
     "tips": [
         ("Tokenul e cheia", "Chaturbate folosește broadcast tokenul în locul unei stream key generice. Tratează ca parolă și resetează dacă se scurge."),
         ("Marjă mare", "Ingestul RTMP Chaturbate acceptă până la 4K, 60 fps și bitrate mare — limita e uploadul tău. Keyframe la 2 secunde."),
         _T_ETH, _T_TEST,
     ],
     "faq": [
         ("Permite Chaturbate OBS / encodere externe?", "Da — Chaturbate suportă encodere externe oficial cu propriul articol «How do I set up OBS?». Activează prin «Use External Encoder to Broadcast» în setările de transmisie."),
         ("Unde e stream key-ul Chaturbate?", "Broadcast Yourself → My Broadcast → View RTMP/OBS broadcast information and stream key. Cheia e broadcast tokenul."),
         ("Ce bitrate pentru Chaturbate?", "3.500–6.000 Kbps la 1080p e suficient. Plafonul Chaturbate e ridicat — limita reală e uploadul; rulează întâi testul de viteză SplitCam."),
         ("SplitCam e gratuit pentru Chaturbate?", "Da — complet gratuit, fără filigran și fără limită de timp: encoderul nu îți mănâncă din câștigurile în tokeni."),
     ]},
    {"slug": "cam4", "name": "CAM4",
     "title": "Transmisie pe CAM4 cu SplitCam — External Encoder",
     "desc": "Transmisie pe CAM4 cu SplitCam gratuit — External Encoder, stream key, geo-blocare și overlay-uri. Fără filigran.",
     "kw": "transmisie cam4, cam4.com, cam4 external encoder, cam4 stream key, cam4 rtmp obs",
     "h1html": 'Cum transmiți pe <span class="accent">CAM4</span> cu SplitCam',
     "h1short": "Transmisie CAM4",
     "card": "External Encoder pe CAM4 cu geo-controale.",
     "intro": "CAM4 e o platformă cam-and-earn globală cu geo-controale integrate — poți ascunde transmisia în țări selectate. Transmisia prin <strong style='color:var(--text)'>SplitCam</strong> gratuit ca encoder extern deschide schimbări de scenă și overlay-uri pe care broadcasterul de bază nu le face.",
     "quick": "Transmisie pe CAM4 cu SplitCam: instalezi SplitCam, construiești scena, pe CAM4 mergi la <em>Broadcast &amp; Earn Money → Start Broadcast → External Encoder</em>, Get Stream Key, lipești în SplitCam, Go Live."
              "<ol><li>Instalează SplitCam.</li><li>Adaugă cameră + scenă.</li>"
              "<li>Ia stream key-ul CAM4.</li><li>Lipește în SplitCam.</li>"
              "<li>Apasă Go Live.</li></ol>",
     "key_how": "Pe CAM4 clic <strong>Broadcast</strong> → <strong>Broadcast &amp; Earn Money</strong> → <strong>Start Broadcast</strong>, apoi <strong>External Encoder</strong> sus. Completează data nașterii, genul și țara, folosește <strong>Get Stream Key</strong> și copiază. Un slider verde în Stream Settings SplitCam confirmă conexiunea.",
     "tips": [
         ("Setează geo-restricțiile", "CAM4 permite ascunderea transmisiei în țări și regiuni specifice — configurează pe partea CAM4 înainte de go-live."),
         ("Urmărește sliderul verde", "Setupul CAM4 arată un slider verde în Stream Settings SplitCam când cheia e acceptată — roșu înseamnă verifică cheia."),
         ("Bitrate mai mic decât obișnuit", "Ingestul CAM4 limitează bitrate-ul video la circa 3.000 Kbps — mai mic decât majoritatea cam-site-urilor. Nu împinge mai sus."),
         _T_ETH,
     ],
     "faq": [
         ("Suportă CAM4 OBS / encodere externe oficial?", "Da — CAM4 are un OBS Guide oficial pe site-ul de suport și recomandă External Encoder pentru cea mai bună experiență. SplitCam folosește același traseu RTMP."),
         ("Pot geo-bloca transmisia CAM4?", "Da — CAM4 are geo-restricție integrată pentru ascunderea transmisiei în anumite țări. Configurezi pe CAM4, nu în SplitCam."),
         ("Unde e stream key-ul CAM4?", "Broadcast → Broadcast & Earn Money → Start Broadcast → External Encoder → Get Stream Key."),
         ("Ce bitrate pentru CAM4?", "Mai mic decât media — ingestul CAM4 limitează la ~3.000 Kbps la 30 fps cu keyframe de 1 secundă. Tabelul oficial recomandă să nu depășești ~3.000."),
     ]},
    {"slug": "bongacams", "name": "BongaCams",
     "title": "Transmisie pe BongaCams cu SplitCam — External Encoder",
     "desc": "Transmisie pe BongaCams cu SplitCam gratuit — External Encoder, scene multi-cameră, overlay-uri și fundal AI. Fără filigran.",
     "kw": "bongacams, bongcams, transmisie bongacams, bongacams external encoder, bongacams rtmp obs",
     "h1html": 'Cum transmiți pe <span class="accent">BongaCams</span> cu SplitCam',
     "h1short": "Transmisie BongaCams",
     "card": "Setup External Encoder pentru BongaCams.",
     "intro": "BongaCams e o platformă cam globală. Transmisia prin encoder extern nu vine întotdeauna activată — o dată activată, <strong style='color:var(--text)'>SplitCam</strong> gratuit conduce transmisia cu scene multi-cameră, overlay-uri și fundal AI.",
     "quick": "Transmisie pe BongaCams cu SplitCam: instalezi SplitCam, construiești scena, pe BongaCams mergi la <em>Options → Broadcast settings → Select Encoder → External Encoder</em>, copiezi URL și cheia, lipești în SplitCam, Go Live."
              "<ol><li>Instalează SplitCam.</li><li>Adaugă cameră + scenă.</li>"
              "<li>Ia URL și cheia de la BongaCams.</li><li>Lipește în SplitCam.</li>"
              "<li>Apasă Go Live.</li></ol>",
     "key_how": "Pe BongaCams deschide <strong>Options</strong> → <strong>Broadcast settings</strong> → <strong>Select Encoder</strong> → <strong>External Encoder</strong> și copiază URL-ul serverului și stream key afișate. <strong>Dacă butonul External Encoder lipsește</strong>, contactează suportul BongaCams și cere activarea codării externe pe cont.",
     "tips": [
         ("Fără buton External Encoder? Suport", "BongaCams activează codarea externă cont cu cont — dacă opțiunea lipsește din Broadcast settings, suportul o activează."),
         ("Potrivește rezoluția", "BongaCams recomandă ca rezoluția webcam-ului și cea a transmisiei să coincidă — de exemplu ambele 1280×720."),
         _T_ETH, _T_TEST,
     ],
     "faq": [
         ("De ce butonul External Encoder nu apare pe BongaCams?", "Codarea externă nu e activă implicit pe orice cont — contactează suportul BongaCams pentru a o activa și butonul apare în Broadcast settings."),
         ("Trebuie să verific contul BongaCams?", "Da — transmisia necesită 18+, document de identitate pentru verificarea vârstei și aprobarea contului înainte de live."),
         ("Ce bitrate pentru BongaCams?", "Ingestul RTMP BongaCams limitează bitrate-ul video la circa 6.000 Kbps cu keyframe de 2 secunde — 3.500–6.000 la 1080p e zona ideală; testează uploadul înainte."),
         ("SplitCam e gratuit pentru BongaCams?", "Da — complet gratuit, fără filigran și fără limită de timp, deci encoderul nu îți reduce câștigurile în tokeni pe BongaCams."),
     ]},
    {"slug": "stripchat", "name": "Stripchat",
     "title": "Transmisie pe Stripchat cu SplitCam — Strip Cam Setup",
     "desc": "Transmisie pe Stripchat — platforma strip cam — cu SplitCam gratuit. Software extern, cheie-token, scene și overlay-uri.",
     "kw": "strip cam, stripchat live stream, transmisie stripchat, stripchat external software, stripchat stream key, stripchat rtmp obs",
     "h1html": 'Cum transmiți pe <span class="accent">Stripchat</span> cu SplitCam',
     "h1short": "Transmisie Stripchat",
     "card": "Setup software extern pentru transmisii Stripchat.",
     "intro": "Stripchat e o platformă cam mare cu accent pe interactivitate. Modul <em>external software</em> îți dă o cheie bazată pe token — pune-o în <strong style='color:var(--text)'>SplitCam</strong> gratuit ca să transmiți cu scene, overlay-uri și filtre în loc de o cameră simplă.",
     "quick": "Transmisie pe Stripchat cu SplitCam: instalezi SplitCam, construiești scena, pe Stripchat alegi <em>Switch to external software</em>, copiezi stream key-ul, lipești în SplitCam, Go Live."
              "<ol><li>Instalează SplitCam.</li><li>Adaugă cameră + scenă.</li>"
              "<li>Ia stream key-ul Stripchat.</li><li>Lipește în SplitCam.</li>"
              "<li>Apasă Go Live.</li></ol>",
     "key_how": "Pe Stripchat alege <strong>Switch to external software</strong>, apoi <strong>Show external software settings for the stream</strong>. Copiază stream key-ul — Stripchat îl arată ca token. Păstrează privat.",
     "tips": [
         ("Potrivește rezoluția cu site-ul", "FAQ-ul Stripchat avertizează: rezoluția din software trebuie să se potrivească exact cu cea de pe site, altfel video-ul pixelează. Setează ambele la fel."),
         ("Atenție la minimul de 2 Mbps", "Stripchat declară 2 Mbps upload ca minim — și spune direct că nu e suficient pentru streaming OBS sau multistream. Țintește mult mai sus."),
         ("Cheia e un token", "Stream key-ul Stripchat e un token — copiază exact, nu împărtăși niciodată, resetează dacă se scurge."),
         _T_ETH,
     ],
     "faq": [
         ("Recomandă Stripchat OBS / software extern?", "Da — FAQ-ul oficial Stripchat recomandă software de broadcast extern ca OBS «pentru a obține cea mai bună calitate video și audio». SplitCam funcționează la fel."),
         ("Cum trec Stripchat pe software extern?", "În Broadcast Center alege Switch to External Broadcast Software (OBS), apoi deschide external software settings pentru a dezvălui stream key-ul (tokenul)."),
         ("Ce bitrate pentru Stripchat?", "Ingestul RTMP acceptă până la ~6.000 Kbps cu keyframe de 2 secunde. 3.500–6.000 la 1080p e ideal — dar trebuie să fii bine peste minimul de 2 Mbps, mai ales pentru streaming OBS."),
         ("SplitCam e gratuit pentru Stripchat?", "Da — fără taxă de licență, fără filigran, fără limită de timp: chiar și show-uri interactive lungi pe Stripchat nu costă nimic la nivelul encoderului."),
     ]},
    {"slug": "onlyfans", "name": "OnlyFans",
     "title": "Live pe OnlyFans cu SplitCam — Autorizare sau cheie",
     "desc": "Live pe OnlyFans cu SplitCam gratuit — autorizare sau OBS Key, scene multi-cameră, overlay-uri. Fără filigran.",
     "kw": "live onlyfans, onlyfans live stream, onlyfans autorizare splitcam, onlyfans obs key, onlyfans streaming software",
     "h1html": 'Cum intri live pe <span class="accent">OnlyFans</span> cu SplitCam',
     "h1short": "Live OnlyFans",
     "card": "Autorizezi o dată sau lipești cheia — live pe OnlyFans.",
     "intro": "Live-ul OnlyFans e pentru abonații tăi. SplitCam conectează în <strong style='color:var(--text)'>două moduri</strong> — te loghezi o dată cu contul OnlyFans și SplitCam ia stream key-ul automat și îl menține sincronizat, sau lipești OBS Key-ul manual. În ambele cazuri transmiți cu scene multi-cameră, overlay-uri și filtre.",
     "quick": "Live pe OnlyFans cu SplitCam: instalezi SplitCam, construiești scena, deschizi Stream Settings &rarr; Add Channel &rarr; OnlyFans și alegi <em>Autorizare</em> — te loghezi cu contul OnlyFans, SplitCam ia cheia automat — și apeși Go Live. Cu contul conectat poți schimba parametrii streamului OnlyFans din SplitCam, fără să deschizi site-ul OnlyFans.",
     "steps": [
         ("Descarcă și instalează SplitCam",
          "SplitCam e software de streaming gratuit pentru Windows și macOS — fără cont, fără card, fără filigran. E encoderul care îți trimite videoul către OnlyFans."),
         ("Setează camera și scena",
          "Deschide SplitCam și adaugă webcam-ul. Construiește scena pe care o vor vedea spectatorii — overlay-uri, text, a doua cameră, filtre beauty sau fundal AI, totul aplicat live."),
         ("Conectare — Metoda 1: Autorizare (recomandată)",
          "În SplitCam deschide <strong>Stream Settings</strong> &rarr; <strong>Add Channel</strong> &rarr; <strong>OnlyFans</strong> și alege <strong>Autorizare</strong>. Te loghezi cu email și parola OnlyFans. SplitCam îți leagă contul, ia stream key-ul automat și îl menține sincronizat — și te lasă să gestionezi parametrii live-ului OnlyFans din SplitCam, schimbându-i în timpul sau după transmisie fără să deschizi site-ul OnlyFans."),
         ("Conectare — Metoda 2: Stream Key (manual)",
          "Preferi să nu te loghezi? Folosește cheia. Pe OnlyFans mergi la <strong>Profile</strong> &rarr; <strong>Settings</strong> &rarr; secțiunea <strong>Other</strong> și copiază <strong>OBS Key</strong>. În SplitCam, Add Channel &rarr; OnlyFans, lipește în câmpul cheii. Această cheie e statică — pentru a schimba setări mai târziu te întorci pe site-ul OnlyFans."),
         ("Go Live",
          "Indiferent de metodă, apasă <strong>Go Live</strong> în SplitCam. Cu Metoda 1 poți ajusta parametrii OnlyFans din SplitCam în timp real; cu Metoda 2 cheia rămâne exact cum ai setat-o."),
     ],
     "tips": [
         ("Autorizare vs Stream Key", "Două moduri de conectare: <strong>Autorizare</strong> (te loghezi o dată, cheia se ia și se menține sincronizată — cea mai ușoară rută) sau <strong>Stream Key</strong> (copiezi OBS Key din OnlyFans → Profile → Settings → Other și lipești). Autorizarea scutește copy-paste-ul manual."),
         ("Schimbă setări fără să părăsești SplitCam", "Cu autorizare, contul rămâne legat, deci ajustezi parametrii live OnlyFans din SplitCam în timpul sau după transmisie — fără să treci prin site-ul OnlyFans."),
         ("Bitrate modest", "Ingestul RTMP OnlyFans limitează bitrate-ul video la circa 2.500 Kbps — mai strâns decât majoritatea cam-site-urilor. Țintește 720p–1080p la ~2.000–2.500."),
         _T_ETH,
     ],
     "faq": [
         ("Cum conectez OnlyFans la SplitCam?", "Două moduri. <strong>Autorizare</strong> — Stream Settings → Add Channel → OnlyFans → loghezi cu contul OnlyFans și SplitCam ia cheia automat. Sau <strong>Stream Key</strong> — copiezi OBS Key din OnlyFans → Profile → Settings → Other și lipești."),
         ("Pot schimba setări live OnlyFans fără să deschid site-ul?", "Da — cu metoda Autorizare SplitCam rămâne conectat la contul tău OnlyFans, deci cheia și setările sincronizează automat. Schimbi totul din SplitCam în timpul sau după transmisie, fără să vizitezi onlyfans.com."),
         ("Ce bitrate pentru OnlyFans?", "Modest — ingestul RTMP OnlyFans limitează bitrate-ul la circa 2.500 Kbps, mult mai strâns decât alte platforme cam. Țintește 720p–1080p în jur de 2.000–2.500 Kbps."),
         ("SplitCam e gratuit pentru live OnlyFans?", "Da — gratuit, fără filigran și fără limită de timp. Niciun cost la nivelul encoderului."),
     ]},
    {"slug": "camplace", "name": "CamPlace",
     "title": "Transmisie pe CamPlace cu SplitCam — Ghid gratuit",
     "desc": "Transmisie pe CamPlace cu SplitCam gratuit — encoder extern, cheie RTMP, scene și overlay-uri. Pas cu pas, fără filigran.",
     "kw": "transmisie camplace, camplace broadcasting software, camplace rtmp, camplace external encoder, camplace stream key",
     "h1html": 'Cum transmiți pe <span class="accent">CamPlace</span> cu SplitCam',
     "h1short": "Transmisie CamPlace",
     "card": "Setup encoder extern pentru transmisii CamPlace.",
     "intro": "CamPlace e o platformă cam-streaming. Nu există articol OBS public, deci <strong style='color:var(--text)'>ghidul video de mai sus</strong> e referința — <strong style='color:var(--text)'>SplitCam</strong> gratuit conectează prin RTMP standard și adaugă scene, overlay-uri și fundal AI pe care camera de bază nu le face.",
     "quick": "Transmisie pe CamPlace cu SplitCam: instalezi SplitCam, construiești scena, activezi broadcasting extern/RTMP pe CamPlace, copiezi URL-ul serverului și stream key-ul, lipești în SplitCam, Go Live. Urmărește video-ul pentru ruta actuală."
              "<ol><li>Instalează SplitCam.</li><li>Adaugă cameră + scenă.</li>"
              "<li>Ia cheia RTMP de la CamPlace.</li><li>Lipește în SplitCam.</li>"
              "<li>Apasă Go Live.</li></ol>",
     "key_how": "Loghează-te pe CamPlace și deschide setările de broadcasting. Schimbă pe opțiunea encoder extern / RTMP / OBS pentru a dezvălui <strong>URL-ul serverului</strong> și <strong>stream key-ul</strong>, copiază ambele. CamPlace nu publică documentație OBS oficială — <strong>video-ul de mai sus</strong> e ruta pas cu pas cea mai sigură prin interfața actuală.",
     "tips": [
         ("Fără ghid OBS oficial — folosește video-ul", "CamPlace nu are articol public despre encodere externe; video-ul de mai sus e referința pentru ruta actuală."),
         ("RTMP standard funcționează", "Deși nedocumentat, CamPlace acceptă URL standard de server RTMP și o cheie — SplitCam conectează ca destinație RTMP personalizată."),
         ("Suprapune overlay-uri în SplitCam", "Obiective de tip, nume și handle-uri social ca straturi de scenă — camera de bază CamPlace nu le adaugă."),
         _T_ETH,
     ],
     "faq": [
         ("CamPlace are ghid OBS oficial?", "Niciun articol public despre encodere externe găsit. CamPlace acceptă URL RTMP standard și cheie, deci SplitCam funcționează — urmează video-ul."),
         ("Suportă CamPlace encodere externe?", "Da — acceptă o stream key RTMP standard, deci SplitCam conectează ca destinație RTMP personalizată."),
         ("Ce bitrate pentru CamPlace?", "CamPlace nu publică număr oficial — folosește 3.500–6.000 Kbps la 1080p ca interval sigur și lasă testul de viteză SplitCam să fixeze plafonul real."),
         ("SplitCam e gratuit pentru CamPlace?", "Da — gratuit, fără filigran și fără limită de timp. Cum CamPlace nu vine cu encoder propriu, un instrument RTMP gratuit face treaba."),
     ]},
    {"slug": "camsoda", "name": "CamSoda",
     "title": "CamSoda live cu SplitCam — Setup gratuit",
     "desc": "CamSoda live cu SplitCam gratuit — Use OBS Broadcaster, servere regionale, scene și overlay-uri. Fără filigran.",
     "kw": "camsoda live, transmisie camsoda, camsoda obs broadcaster, camsoda rtmp obs, camsoda live broadcast",
     "h1html": 'Cum transmiți pe <span class="accent">CamSoda</span> cu SplitCam',
     "h1short": "Transmisie CamSoda",
     "card": "Setup Use OBS Broadcaster pe CamSoda.",
     "intro": "CamSoda e o platformă cam din SUA cunoscută pentru formate de show interactive și neobișnuite. Suportă streaming OBS oficial — există un buton <strong style='color:var(--text)'>Use OBS Broadcaster</strong> pe pagina Go Live și un ghid OBS oficial în wiki-ul CamSoda. <strong style='color:var(--text)'>SplitCam</strong> gratuit funcționează la fel.",
     "quick": "Transmisie pe CamSoda cu SplitCam: instalezi SplitCam, construiești scena, clic Use OBS Broadcaster pe pagina Go Live CamSoda, copiezi URL-ul serverului și stream key-ul, lipești în SplitCam, Go Live."
              "<ol><li>Instalează SplitCam.</li><li>Adaugă cameră + scenă.</li>"
              "<li>Clic Use OBS Broadcaster pe CamSoda.</li>"
              "<li>Lipește URL + cheia în SplitCam.</li><li>Apasă Go Live.</li></ol>",
     "key_how": "Pe pagina <strong>Go Live</strong> CamSoda clic <strong>Use OBS Broadcaster</strong>. CamSoda afișează URL-ul serverului RTMP și stream key — copiază ambele. Alege serverul regional (America de Nord, Europa, Asia etc.) cel mai apropiat. Wiki-ul CamSoda are un ghid OBS complet dacă ai nevoie de detalii.",
     "tips": [
         ("Verifică-te pentru tipuri", "Pe CamSoda oricine poate transmite, dar pentru a primi tipuri trebuie să finalizezi procesul de verificare CamSoda."),
         ("Alege serverul regional cel mai apropiat", "CamSoda oferă servere de ingest regionale — cel mai apropiat (NA / Europa / Asia / America de Sud / Oceania) reduce latența și frame-urile pierdute."),
         ("Plafon la 1080p / 30 fps", "Ingestul CamSoda merge până la circa 1080p, 30 fps și ~6.000 Kbps — nu împinge mai sus."),
         _T_ETH,
     ],
     "faq": [
         ("Suportă CamSoda OBS / encodere externe?", "Da — oficial. Există un buton Use OBS Broadcaster pe pagina Go Live și un ghid OBS pe wiki-ul CamSoda, deci SplitCam funcționează."),
         ("Trebuie să mă verific pe CamSoda?", "Pentru transmisie, nu. Pentru a primi tipuri, da — CamSoda cere finalizarea procesului de verificare mai întâi."),
         ("Ce rezoluție suportă CamSoda?", "Până la 1920×1080 la 30 fps, în jur de 6.000 Kbps maxim pe ingest RTMP."),
         ("SplitCam e gratuit pentru CamSoda?", "Da — gratuit, fără filigran și fără limită de timp. Funcționează cu modul gratuit Use OBS Broadcaster al CamSoda, deci întreg lanțul nu costă nimic."),
     ]},
    {"slug": "streamate", "name": "Streamate",
     "title": "Transmisie pe Streamate cu SplitCam — Canal integrat",
     "desc": "Transmisie pe Streamate cu SplitCam gratuit — canal integrat, cheie SM Connect, scene și overlay-uri. Fără filigran.",
     "kw": "streamate, streamate sm connect, transmisie streamate, streamate broadcasting software, streamate rtmp",
     "h1html": 'Cum transmiți pe <span class="accent">Streamate</span> cu SplitCam',
     "h1short": "Transmisie Streamate",
     "card": "Streamate e canal integrat în SplitCam — setup rapid.",
     "intro": "Streamate e o platformă cam consacrată — și e una dintre <strong style='color:var(--text)'>destinațiile preconfigurate în SplitCam</strong>, în lista de canale, deci setupul e mai rapid decât intrarea RTMP manuală: alegi Streamate, lipești cheia, gata.",
     "quick": "Transmisie pe Streamate cu SplitCam: instalezi SplitCam, construiești scena, pe Streamate folosești <em>SM Connect → Start Show</em> și copiezi cheia, apoi în SplitCam deschizi <em>Stream Settings → Add Channel → Streamate</em> și lipești."
              "<ol><li>Instalează SplitCam.</li><li>Adaugă cameră + scenă.</li>"
              "<li>Ia cheia Streamate prin SM Connect.</li>"
              "<li>Add Channel → Streamate în SplitCam.</li><li>Apasă Go Live.</li></ol>",
     "key_how": "Pe Streamate deschide <strong>SM Connect</strong>, accepți termenii, clic <strong>Start Show</strong> stânga și închizi fereastra deschisă — apoi copiezi streaming key-ul. În SplitCam deschide <strong>Stream Settings</strong> → <strong>Add Channel</strong>, alegi <strong>Streamate</strong> din listă și lipești cheia. Un slider verde confirmă conexiunea.",
     "tips": [
         ("Streamate e integrat", "Fără URL RTMP manual — SplitCam are Streamate în lista Add Channel; doar selectezi și lipești cheia."),
         ("Închide popup-ul SM Connect", "După Start Show Streamate deschide o fereastră — închide-o; era doar pentru a dezvălui streaming key-ul."),
         ("Fixează rezoluția la 1080p", "Câmpul Video Resolution în SM Connect poate sări la 1440 pe tăcute, ceea ce nu se livrează efectiv și îți reduce calitatea silențios — setează manual la 1080p. Bitrate care scade la imagine statică e normal: streamul Streamate e adaptiv."),
         _T_ETH, _T_TEST,
     ],
     "faq": [
         ("Streamate e integrat în SplitCam?", "Da — Streamate apare în lista Add Channel SplitCam; selectezi în loc să tastezi un URL RTMP."),
         ("Unde e streaming key Streamate?", "SM Connect → accept termeni → Start Show → închizi popup → copiezi cheia."),
         ("Ce bitrate pentru Streamate?", "Streamate nu fixează plafon dur — 3.500–6.000 Kbps la 1080p funcționează bine. Streamul e adaptiv, deci bitrate mai mic la imagine statică e normal, nu bug."),
         ("SplitCam e gratuit pentru Streamate?", "Da — gratuit, fără filigran și fără limită de timp; și pentru că Streamate e canal integrat în SplitCam, nu există nici cost separat de encoder."),
     ]},
    {"slug": "streamray", "name": "StreamRay",
     "title": "Transmisie pe StreamRay cam cu SplitCam — URL chat",
     "desc": "Transmisie pe StreamRay cam cu SplitCam gratuit — URL postat în chat, mod OBS Broadcaster, scene și overlay-uri. Fără filigran.",
     "kw": "streamray, streamray cam, transmisie streamray, streamray obs broadcaster, streamray rtmp",
     "h1html": 'Cum transmiți pe <span class="accent">StreamRay</span> cu SplitCam',
     "h1short": "Transmisie StreamRay",
     "card": "Setup encoder extern URL-chat pentru StreamRay.",
     "intro": "StreamRay are un setup de encoder extern neobișnuit — livrează URL-ul streamului în <strong style='color:var(--text)'>fereastra de chat a transmisiei</strong> și nu folosește stream key separată. <strong style='color:var(--text)'>SplitCam</strong> gratuit gestionează acest flux numai-URL.",
     "quick": "Transmisie pe StreamRay cu SplitCam: instalezi SplitCam, construiești scena, pe StreamRay activezi OBS Broadcaster, copiezi URL-ul streamului din fereastra de chat, lipești în SplitCam (lași câmpul cheii gol), Go Live."
              "<ol><li>Instalează SplitCam.</li><li>Adaugă cameră + scenă.</li>"
              "<li>Copiază URL-ul StreamRay din chat.</li>"
              "<li>Lipește URL-ul în SplitCam.</li><li>Apasă Go Live.</li></ol>",
     "key_how": "Pe StreamRay dublu-clic <strong>Broadcast Now</strong>, deschide meniul <strong>Other</strong>, alege <strong>OBS Broadcaster</strong> și <strong>Save and Close</strong>. StreamRay postează apoi <strong>URL-ul streamului în fereastra de chat</strong> — copiezi de acolo. Lasă câmpul stream key SplitCam <strong>gol</strong>; StreamRay autentifică doar prin URL.",
     "tips": [
         ("URL e în chat", "StreamRay nu afișează URL-ul streamului într-o cutie de setări — îl postează în fereastra de chat a transmisiei. Copiezi de acolo."),
         ("Lasă câmpul cheii gol", "StreamRay nu folosește cheie separată — doar URL. Nu pune nimic în câmpul cheii SplitCam."),
         _T_ETH, _T_TEST,
     ],
     "faq": [
         ("Unde e URL-ul streamului StreamRay?", "După activarea OBS Broadcaster, StreamRay postează URL-ul în fereastra de chat — copiezi din chat."),
         ("De ce nu e stream key pe StreamRay?", "StreamRay autentifică doar prin URL — lasă câmpul cheii SplitCam gol."),
         ("Ce bitrate pentru StreamRay?", "StreamRay nu declară plafon oficial — țintește 3.500–6.000 Kbps la 1080p și rulează testul de viteză SplitCam, pentru că fluxul numai-URL nu dă feedback de bitrate."),
         ("SplitCam e gratuit pentru StreamRay?", "Da — gratuit, fără filigran și fără limită de timp, ceea ce se potrivește cu fluxul numai-URL StreamRay: lipești un link și ești live."),
     ]},
    {"slug": "xlovecam", "name": "XLoveCam",
     "title": "Transmisie pe XLoveCam cu SplitCam — Link RTMP & cheie",
     "desc": "Transmisie pe XLoveCam cu SplitCam gratuit — link RTMP și cheie, servere regionale, scene și overlay-uri. Fără filigran.",
     "kw": "xlovecam, x love cam, transmisie xlovecam, xlovecam rtmp link, xlovecam stream key",
     "h1html": 'Cum transmiți pe <span class="accent">XLoveCam</span> cu SplitCam',
     "h1short": "Transmisie XLoveCam",
     "card": "Setup link RTMP + cheie pentru XLoveCam.",
     "intro": "XLoveCam e o platformă cam europeană multilingvă. Setările contului expun atât un <strong style='color:var(--text)'>link RTMP</strong>, cât și o <strong style='color:var(--text)'>stream key</strong> — <strong style='color:var(--text)'>SplitCam</strong> gratuit ia ambele și transmite cu scene și overlay-uri complete.",
     "quick": "Transmisie pe XLoveCam cu SplitCam: instalezi SplitCam, construiești scena, pe XLoveCam deschizi <em>My Account → settings</em>, copiezi linkul RTMP și stream key-ul, lipești ambele în SplitCam, începi show-ul."
              "<ol><li>Instalează SplitCam.</li><li>Adaugă cameră + scenă.</li>"
              "<li>Copiază linkul RTMP + cheia de la XLoveCam.</li><li>Lipește ambele în SplitCam.</li>"
              "<li>Apasă Go Live.</li></ol>",
     "key_how": "Pe XLoveCam deschide <strong>My Account</strong> → <strong>settings</strong>. Setările afișează atât un <strong>link RTMP</strong>, cât și o <strong>stream key</strong> — copiezi ambele în câmpurile URL server și cheie ale SplitCam, apoi <strong>Start your show</strong> pe XLoveCam.",
     "tips": [
         ("Copiază link ȘI cheie", "XLoveCam îți dă un link RTMP ȘI o stream key separată — ai nevoie de ambele în SplitCam, nu doar una."),
         ("Public multilingv", "XLoveCam e european și multilingv — un overlay text clar în limba ta îi ajută pe spectatori să te găsească."),
         ("Alege serverul cel mai apropiat", "XLoveCam oferă servere RTMP regionale — Europa, America de Nord, America de Sud și Asia. Cel mai apropiat reduce latența și frame-urile pierdute."),
         _T_ETH,
     ],
     "faq": [
         ("Unde sunt datele RTMP XLoveCam?", "My Account → settings — afișează atât linkul RTMP, cât și cheia."),
         ("Suportă XLoveCam encodere externe?", "Da — oferă link RTMP și cheie, deci SplitCam funcționează ca encoder."),
         ("Ce bitrate pentru XLoveCam?", "XLoveCam nu publică limită fixă; 3.500–6.000 Kbps la 1080p e ideal. Alegerea serverului regional cel mai apropiat contează la fel de mult — reduce frame-urile pierdute."),
         ("SplitCam e gratuit pentru XLoveCam?", "Da — gratuit, fără filigran și fără limită de timp. Atingerea publicului multilingv european XLoveCam nu costă software."),
     ]},
    {"slug": "soulcams", "name": "SoulCams",
     "title": "Transmisie pe SoulCams cu SplitCam — Setări OBS",
     "desc": "Transmisie pe SoulCams cu SplitCam gratuit — setări OBS, server RTMP și cheie, scene multi-cameră și overlay-uri.",
     "kw": "soul cams, soulcams, transmisie soulcams, soulcams obs, soulcams rtmp, soulcams broadcast",
     "h1html": 'Cum transmiți pe <span class="accent">SoulCams</span> cu SplitCam',
     "h1short": "Transmisie SoulCams",
     "card": "Setup setări OBS pentru SoulCams.",
     "intro": "SoulCams e o platformă cam ale cărei setări OBS arată <strong style='color:var(--text)'>serverul RTMP și stream key împreună</strong> într-o fereastră. Lipești ambele în <strong style='color:var(--text)'>SplitCam</strong> gratuit pentru a transmite cu scene multi-cameră și overlay-uri.",
     "quick": "Transmisie pe SoulCams cu SplitCam: instalezi SplitCam, construiești scena, pe SoulCams clic Go Online → Settings → OBS, copiezi serverul și cheia, lipești ambele în SplitCam, Go Live."
              "<ol><li>Instalează SplitCam.</li><li>Adaugă cameră + scenă.</li>"
              "<li>Deschide SoulCams Settings → OBS.</li><li>Lipește server + cheie în SplitCam.</li>"
              "<li>Apasă Go Live.</li></ol>",
     "key_how": "Pe SoulCams te loghezi și clic <strong>Go Online</strong>, apoi deschide <strong>Settings</strong> → <strong>OBS</strong>. Fereastra OBS afișează <strong>server RTMP</strong> și <strong>stream key</strong> împreună — copiază ambele în SplitCam.",
     "tips": [
         ("Server și cheie alături", "SoulCams afișează server RTMP și cheie în aceeași fereastră OBS — le iei pe ambele dintr-o singură mișcare."),
         ("Go Online întâi", "Setările OBS apar abia după clic Go Online pe SoulCams — fă asta înainte de a căuta datele encoderului."),
         ("Blochează regiuni nedorite", "SoulCams permite blocare geografică din partea modelului — alegi ce țări nu pot vedea transmisia ta înainte de a apăsa Go Online."),
         _T_ETH, _T_TEST,
     ],
     "faq": [
         ("Unde sunt setările OBS SoulCams?", "Te loghezi, clic Go Online, apoi Settings → OBS — serverul RTMP și stream key sunt afișate împreună."),
         ("Suportă SoulCams encodere externe?", "Da — setările OBS oferă server RTMP și cheie, deci SplitCam funcționează."),
         ("Ce bitrate pentru SoulCams?", "SoulCams nu dă număr oficial — țintește 3.500–6.000 Kbps la 1080p și testează uploadul, pentru că fereastra OBS nu arată îndrumare de bitrate."),
         ("SplitCam e gratuit pentru SoulCams?", "Da — gratuit, fără filigran și fără limită de timp, deci un show complet pe SoulCams cu scene multi-cameră și overlay-uri nu costă nimic la nivelul encoderului."),
     ]},
    {"slug": "imlive", "name": "ImLive",
     "title": "Transmisie pe ImLive cu SplitCam — Cameră virtuală",
     "desc": "Setup Im Live stream cu SplitCam gratuit — ImLive folosește webcam-ul direct (fără RTMP), conectezi SplitCam ca cameră virtuală cu scene.",
     "kw": "im live stream, imlive splitcam, transmisie imlive, imlive cameră virtuală, imlive webcam, im live cam",
     "h1html": 'Cum folosești <span class="accent">ImLive</span> cu SplitCam',
     "h1short": "SplitCam pe ImLive",
     "card": "Setup cameră virtuală pentru ImLive — fără RTMP.",
     "intro": "ImLive folosește webcam-ul direct în browser — nu există <strong style='color:var(--text)'>nici RTMP, nici stream key</strong>. <strong style='color:var(--text)'>SplitCam</strong> gratuit conectează ca <strong style='color:var(--text)'>cameră virtuală</strong>: construiești scena în SplitCam, apoi alegi SplitCam ca cameră în ImLive.",
     "quick": "Folosirea SplitCam cu ImLive: instalezi SplitCam, construiești scena cu straturi media, deschizi ImLive și începi un video chat, în setările ImLive selectezi SplitCam ca webcam și microfon."
              "<ol><li>Instalează SplitCam.</li><li>Construiește scena în SplitCam.</li>"
              "<li>Începe video chat pe ImLive.</li>"
              "<li>Alege SplitCam ca cameră ImLive.</li><li>Începe chat-ul.</li></ol>",
     "steps": [
         ("Instalează SplitCam",
          "SplitCam e software gratuit pentru Windows și macOS. Instalează — fără filigran, fără cont. Pentru ImLive funcționează ca <strong>cameră virtuală</strong>, nu encoder RTMP."),
         ("Construiește scena în SplitCam",
          "Deschide SplitCam și folosește <strong>Media Layers +</strong> pentru a adăuga webcam-ul plus orice overlay-uri, text, filtre sau fundal AI. Această scenă compusă e ceea ce ImLive va vedea drept camera ta."),
         ("Începe un video chat pe ImLive",
          "Loghează-te pe site-ul ImLive și clic <strong>Start Video Chat</strong>, apoi deschide <strong>Go To Settings</strong> pentru a ajunge la opțiunile de cameră și microfon."),
         ("Alege SplitCam ca cameră",
          "În setările ImLive alegi <strong>SplitCam</strong> drept webcam ȘI drept microfon. ImLive afișează acum scena ta SplitCam completă în loc de o webcam simplă."),
         ("Începe Free Live Chat",
          "Clic <strong>Free Live Chat</strong> pe ImLive pentru a intra live. Pentru a schimba aspectul în mijlocul sesiunii, editezi scena în SplitCam — ImLive actualizează instant."),
     ],
     "tips": [
         ("Nu e nevoie de stream key", "ImLive nu are RTMP — nu căuta URL de server sau cheie. SplitCam e doar selectat ca dispozitiv de cameră."),
         ("Setează SplitCam și ca mic", "Alege SplitCam pentru microfon pe lângă cameră, ca mixul audio și suprimarea zgomotului să treacă și ele în live."),
         ("Construiește scena înainte de live", "ImLive afișează ce emite SplitCam — aranjează straturile înainte de a începe chat-ul."),
         _T_TEST,
     ],
     "faq": [
         ("ImLive folosește RTMP sau stream key?", "Nu — ImLive folosește webcam-ul direct prin browser. SplitCam conectează ca cameră virtuală, nu există cheie de copiat."),
         ("Cum aleg SplitCam pe ImLive?", "Start Video Chat → Go To Settings → alegi SplitCam ca webcam și microfon."),
         ("Pot folosi overlay-uri pe ImLive?", "Da — le construiești în scena SplitCam; ImLive afișează rezultatul compus."),
         ("SplitCam e gratuit pentru ImLive?", "Da — gratuit, fără filigran și fără limită de timp. Ca cameră virtuală pentru ImLive nu adaugă cost sau branding la video chat-ul tău."),
     ]},
    {"slug": "vxlive", "name": "VXLive",
     "title": "Transmisie pe VXLive cu SplitCam — Suport oficial",
     "desc": "Transmisie pe VXLive (VXModels / VISIT-X) cu SplitCam gratuit — preset VISIT-X oficial, server și cheie, scene. Fără filigran.",
     "kw": "vxlive, visit-x, vxmodels splitcam, transmisie vxlive, visit-x stream, vxlive rtmp",
     "h1html": 'Cum transmiți pe <span class="accent">VXLive</span> cu SplitCam',
     "h1short": "Transmisie VXLive",
     "card": "VXLive suportă SplitCam oficial (preset VISIT-X).",
     "intro": "VXLive (VXModels / VISIT-X) e o platformă cam de pe piața germană — și una dintre puținele care <strong style='color:var(--text)'>suportă SplitCam oficial pe nume</strong>. VXModels are un articol de ajutor dedicat pentru conectarea <strong style='color:var(--text)'>SplitCam</strong> la VXLive, iar SplitCam livrează VISIT-X ca preset de canal gata făcut.",
     "quick": "Transmisie pe VXLive cu SplitCam: instalezi SplitCam, construiești scena, pe VXLive alegi «Stream with third-party software», copiezi URL-ul serverului și cheia, în SplitCam alegi presetul VISIT-X și lipești, Go Live în SplitCam, apoi GO ONLINE pe VXLive."
              "<ol><li>Instalează SplitCam.</li><li>Adaugă cameră + scenă.</li>"
              "<li>Ia URL server + cheie de la VXLive.</li>"
              "<li>Alege presetul VISIT-X în SplitCam, lipește.</li>"
              "<li>Go Live, apoi GO ONLINE pe VXLive.</li></ol>",
     "key_how": "Pe VXLive alege <strong>Stream with third-party software</strong> și selectează opțiunea pentru <strong>OBS, SplitCam sau XSplit</strong>. VXLive oferă un <strong>URL de server</strong> și o <strong>stream key</strong>. În SplitCam alegi <strong>VISIT-X</strong> ca platformă de streaming, lipești ambele, apeși <strong>Go Live</strong> în SplitCam, apoi <strong>GO ONLINE</strong> pe VXLive.",
     "tips": [
         ("VISIT-X e preset integrat", "Nu tasta URL RTMP brut — SplitCam are VISIT-X în lista de platforme; doar selectezi și lipești URL serverului și cheia."),
         ("Go-live în doi pași", "Pe VXLive apeși Go Live în SplitCam întâi, apoi GO ONLINE pe VXLive — ambele, în această ordine."),
         ("Piața germană", "Publicul VXLive e predominant germanofon — un overlay text sau titlu în germană te ajută să te conectezi cu spectatorii."),
         _T_ETH,
     ],
     "faq": [
         ("Suportă VXLive SplitCam oficial?", "Da — VXModels (VXLive) are un articol de ajutor oficial dedicat configurării SplitCam și listează SplitCam alături de OBS și XSplit ca software de broadcasting suportat."),
         ("Cum conectez SplitCam la VXLive?", "Pe VXLive alegi «Stream with third-party software», apoi în SplitCam selectezi presetul VISIT-X și lipești URL serverului și stream key oferite de VXLive."),
         ("Intru live în SplitCam sau pe VXLive?", "Ambele — întâi Go Live în SplitCam, apoi GO ONLINE pe VXLive."),
         ("De ce recomandă VXModels SplitCam?", "Articolul oficial de ajutor VXModels recomandă SplitCam specific pentru a elimina artefactele de imagine și pixelarea webcam-ului și a stabiliza conexiunea — nu doar ca encoder generic."),
     ]},
    {"slug": "virtwish", "name": "VirtWish",
     "title": "Transmisie pe VirtWish cu SplitCam — URL stream & cheie",
     "desc": "Transmisie pe VirtWish cu SplitCam gratuit — Profile → Start Broadcast secțiunea OBS, URL stream și cheie, scene și overlay-uri.",
     "kw": "virtwish, transmisie virtwish, virtwish broadcasting software, virtwish rtmp, virtwish stream key, virtwish obs",
     "h1html": 'Cum transmiți pe <span class="accent">VirtWish</span> cu SplitCam',
     "h1short": "Transmisie VirtWish",
     "card": "Setup URL stream + cheie pentru VirtWish.",
     "intro": "VirtWish e o platformă cam interactivă. Setările de transmisie îți dau un <strong style='color:var(--text)'>URL stream și o stream key separată</strong> într-o secțiune OBS — <strong style='color:var(--text)'>SplitCam</strong> gratuit le ia pe ambele și rulează show-ul cu scene și overlay-uri.",
     "quick": "Transmisie pe VirtWish cu SplitCam: instalezi SplitCam, construiești scena, pe VirtWish deschizi <em>Profile → Start Broadcast</em> până la secțiunea OBS, copiezi linkul și cheia, lipești ambele în SplitCam, Go Live."
              "<ol><li>Instalează SplitCam.</li><li>Adaugă cameră + scenă.</li>"
              "<li>Ia URL + cheia de la VirtWish.</li><li>Lipește ambele în SplitCam.</li>"
              "<li>Apasă Go Live.</li></ol>",
     "key_how": "Pe VirtWish clic pe iconița din colțul dreapta sus → <strong>Profile</strong> → <strong>Start Broadcast</strong>, apoi <strong>Start Broadcast</strong> din nou pentru a ajunge la secțiunea OBS. <strong>Copiază linkul de pe primul rând</strong> în câmpul Stream URL al SplitCam, iar <strong>Stream Key</strong> separat în câmpul cheii.",
     "tips": [
         ("Link pe primul rând", "Secțiunea OBS VirtWish pune URL-ul streamului pe primul rând — copiezi în Stream URL SplitCam, apoi cheia separată."),
         ("Două click-uri pe Start Broadcast", "Apeși Start Broadcast de două ori pe VirtWish pentru a ajunge la secțiunea OBS — e așteptat, nu bug."),
         _T_ETH, _T_TEST,
     ],
     "faq": [
         ("Unde sunt datele RTMP VirtWish?", "Iconița dreapta sus → Profile → Start Broadcast de două ori → secțiunea OBS afișează linkul și stream key."),
         ("Suportă VirtWish encodere externe?", "Da — secțiunea OBS oferă URL stream și cheie, deci SplitCam funcționează."),
         ("Ce bitrate pentru VirtWish?", "VirtWish nu publică plafon oficial; 3.500–6.000 Kbps la 1080p e sigur. Potrivește rezoluția SplitCam cu cea setată pe VirtWish pentru a evita rescaling."),
         ("SplitCam e gratuit pentru VirtWish?", "Da — gratuit, fără filigran și fără limită de timp. Setup-ul URL-și-cheie VirtWish costă doar minutele necesare."),
     ]},
    {"slug": "xmodels", "name": "XModels",
     "title": "Transmisie pe XModels cu SplitCam — Ghid gratuit",
     "desc": "Transmisie pe XModels cu SplitCam gratuit — opțiune encoder extern în setările contului model, cheie RTMP, scene și overlay-uri.",
     "kw": "xmodels, transmisie xmodels, xmodels broadcasting software, xmodels rtmp, xmodels external encoder",
     "h1html": 'Cum transmiți pe <span class="accent">XModels</span> cu SplitCam',
     "h1short": "Transmisie XModels",
     "card": "Setup encoder extern pentru transmisii XModels.",
     "intro": "XModels e o platformă cam-streaming cu o <strong style='color:var(--text)'>opțiune de encoder extern</strong> integrată în setările contului model. <strong style='color:var(--text)'>SplitCam</strong> gratuit transmite acolo cu scene multi-cameră, overlay-uri și filtre în loc de o singură cameră simplă.",
     "quick": "Transmisie pe XModels cu SplitCam: instalezi SplitCam, construiești scena, în contul model XModels activezi opțiunea de encoder extern, copiezi URL-ul serverului și stream key-ul, lipești în SplitCam, Go Live."
              "<ol><li>Instalează SplitCam.</li><li>Adaugă cameră + scenă.</li>"
              "<li>Activează encoder extern în setările XModels.</li>"
              "<li>Lipește URL + cheia în SplitCam.</li><li>Apasă Go Live.</li></ol>",
     "key_how": "În <strong>setările contului model</strong> XModels, activezi opțiunea <strong>broadcast prin encoder extern</strong>. XModels oferă o <strong>stream key</strong> — copiezi în SplitCam. Dacă opțiunea nu e unde te aștepți, suportul XModels e prin chat FAQ pe site și <strong>info@xmodels.com</strong>; video-ul de mai sus o arată și el.",
     "tips": [
         ("E în setările contului", "XModels pune opțiunea encoder extern în setările contului model, nu pe un ecran de transmisie separat."),
         ("Suport: chat + email", "XModels nu are un centru de ajutor public mare — chat-ul FAQ pe site și info@xmodels.com sunt canalele oficiale de suport."),
         ("Suprapune overlay-uri în SplitCam", "Obiective de tip, nume și handle-uri social ca straturi de scenă — camera de bază XModels nu le adaugă."),
         _T_ETH,
     ],
     "faq": [
         ("Suportă XModels encodere externe?", "Da — setările contului model includ o opțiune de transmisie prin encoder extern care oferă o stream key, deci SplitCam funcționează."),
         ("Unde caut ajutor XModels?", "Suportul XModels e prin chat FAQ pe site și emailul info@xmodels.com — nu există centru de ajutor public mare."),
         ("Ce bitrate pentru XModels?", "XModels nu documentează număr oficial — folosește 3.500–6.000 Kbps la 1080p și rulează testul de viteză SplitCam, pentru că suportul XModels e doar chat și email."),
         ("SplitCam e gratuit pentru XModels?", "Da — gratuit, fără filigran și fără limită de timp, deci transmisia către rețeaua europeană XModels nu adaugă cost de software."),
     ]},
    {"slug": "flirt4free", "name": "Flirt4Free",
     "title": "Transmisie pe Flirt for Free cam cu SplitCam — Ghid gratuit",
     "desc": "Transmisie pe Flirt for Free cam cu SplitCam gratuit — External Broadcast Form, RTMP URL și Stream Name, scene și overlay-uri.",
     "kw": "flirt for free cam, flirt 4 free cam, flirt4free, transmisie flirt4free, flirt4free external broadcast, flirt4free rtmp",
     "h1html": 'Cum transmiți pe <span class="accent">Flirt4Free</span> cu SplitCam',
     "h1short": "Transmisie Flirt4Free",
     "card": "Setup External Broadcast Form pentru Flirt4Free.",
     "intro": "Flirt4Free e una dintre cele mai vechi platforme cam, în aer din anii '90. Suportă transmisia externă oficial printr-un <strong style='color:var(--text)'>External Broadcast Form</strong> — <strong style='color:var(--text)'>SplitCam</strong> gratuit trimite streamul în timp ce formularul setează rezoluția și bitrate-ul.",
     "quick": "Transmisie pe Flirt4Free cu SplitCam: instalezi SplitCam, construiești scena, deschizi External Broadcast Form Flirt4Free, copiezi RTMP URL și Stream Name și setezi rezoluție/bitrate, lipești în SplitCam, Go Live."
              "<ol><li>Instalează SplitCam.</li><li>Adaugă cameră + scenă.</li>"
              "<li>Deschide External Broadcast Form Flirt4Free.</li>"
              "<li>Lipește RTMP URL + Stream Name în SplitCam.</li>"
              "<li>Apasă Go Live.</li></ol>",
     "key_how": "În aria modelului Flirt4Free deschide <strong>External Broadcast Form</strong>. Spre deosebire de majoritatea cam-site-urilor, Flirt4Free îți dă un <strong>RTMP URL</strong> și un <strong>Stream Name</strong> (nu o «cheie»), plus câmpuri de rezoluție și bitrate pe care le completezi în formular. Copiezi URL și Stream Name în câmpurile server și cheie ale SplitCam.",
     "tips": [
         ("E Stream Name, nu cheie", "Flirt4Free numește credențialul Stream Name. Îl lipești în câmpul stream key SplitCam — îndeplinește același rol."),
         ("Setează rezoluția/bitrate în formular", "External Broadcast Form Flirt4Free are câmpuri proprii de rezoluție și bitrate — aliniază cu setările SplitCam ca imaginea să nu fie rescalată."),
         ("Platformă istorică", "Flirt4Free rulează din anii '90 — uneltele pentru modele sunt mature, iar External Broadcast Form e parte documentată din ele."),
         _T_ETH,
     ],
     "faq": [
         ("Suportă Flirt4Free encodere externe?", "Da — oficial, prin External Broadcast Form, care oferă RTMP URL și Stream Name. SplitCam funcționează ca encoder."),
         ("Unde iau datele RTMP Flirt4Free?", "Din External Broadcast Form în aria modelului — afișează RTMP URL, Stream Name și câmpuri de rezoluție/bitrate."),
         ("Ce bitrate pentru Flirt4Free?", "3.500–6.000 Kbps la 1080p — setează aceeași valoare în External Broadcast Form și în SplitCam."),
         ("SplitCam e gratuit pentru Flirt4Free?", "Da — gratuit, fără filigran și fără limită de timp, ceea ce se potrivește unei platforme istorice ca Flirt4Free, unde show-urile pot fi lungi."),
     ]},
    {"slug": "mfc-alerts", "name": "MFC Alerts",
     "title": "Adaugă MFC Alerts la streamul tău cu SplitCam",
     "desc": "Afișează tip alerts animate în streamul MyFreeCams — URL mfcalerts.com ca strat Browser în SplitCam gratuit, deasupra webcam-ului.",
     "kw": "mfc alerts, myfreecams alerts, adaugă mfc alerts, mfcalerts splitcam, myfreecams tip alerts, myfreecams alerts overlay",
     "h1html": 'Cum adaugi <span class="accent">MFC Alerts</span> la streamul tău',
     "h1short": "Adaugă MFC Alerts",
     "card": "Afișează tip alerts animate în streamul MyFreeCams.",
     "intro": "MFC Alerts afișează efecte animate în streamul MyFreeCams ori de câte ori un spectator trimite un tip. Rulează ca <strong style='color:var(--text)'>strat Browser</strong> în <strong style='color:var(--text)'>SplitCam</strong> gratuit — îl setezi o dată și tip-urile declanșează reacții pe ecran live.",
     "quick": "Adăugarea MFC Alerts cu SplitCam: instalezi SplitCam, adaugi webcam-ul, deschizi tab-ul Browser și încarci mfcalerts.com, copiezi URL-ul alerts, adaugi ca strat Browser deasupra webcam-ului, apoi testezi cu un tip de test."
              "<ol><li>Instalează SplitCam.</li><li>Adaugă webcam-ul.</li>"
              "<li>Ia URL-ul de pe mfcalerts.com.</li>"
              "<li>Adaugă ca strat Browser deasupra webcam-ului.</li>"
              "<li>Trimite un tip de test.</li></ol>",
     "steps": [
         ("Instalează SplitCam și adaugă webcam-ul",
          "Instalează SplitCam gratuit pentru Windows sau macOS, apoi adaugă <strong>webcam-ul</strong> ca sursă. MFC Alerts stă ca strat deasupra acestei camere."),
         ("Deschide tab-ul Browser și mergi la mfcalerts.com",
          "În SplitCam deschide tab-ul <strong>Browser</strong> și navighează la <strong>www.mfcalerts.com</strong>. Loghează-te sau înregistrează-te dacă nu ai cont mfcalerts.com încă."),
         ("Copiază URL-ul tău de alerts",
          "Pe mfcalerts.com folosește <strong>Copy to clipboard</strong> pentru a copia URL-ul personal de alerts — e pagina care randează animațiile de tip."),
         ("Adaugă URL-ul ca strat Browser — deasupra webcam-ului",
          "Lipește URL-ul în fereastra Browser SplitCam și clic <strong>Add</strong>. Apoi reorganizează lista de surse ca <strong>MFC Alerts să fie deasupra webcam-ului</strong> (meniu 3 puncte → Move Up). Dacă stă dedesubt, efectele rămân ascunse."),
         ("Testează cu un tip de test",
          "Deschide <strong>Settings → Send test tip</strong> și confirmă că efectul de alert apare peste camera ta. Apoi transmite normal pe MyFreeCams — tip-urile reale declanșează acum animațiile."),
     ],
     "tips": [
         ("MFC Alerts trebuie deasupra webcam-ului", "Greșeala cea mai frecventă: dacă stratul MFC Alerts e dedesubtul webcam-ului în lista de surse, efectele rămân ascunse. Urcă-l."),
         ("Cont mfcalerts.com necesar", "URL-ul de alerts e personal — înregistrează-te pe mfcalerts.com întâi dacă nu ai cont."),
         ("Trimite tip de test înainte de live", "Folosește Settings → Send test tip pentru a confirma că overlay-ul funcționează — nu descoperi greșeala în mijlocul show-ului."),
         _T_ETH,
     ],
     "faq": [
         ("Ce e MFC Alerts?", "Un sistem de notificări pentru MyFreeCams care afișează efecte video în streamul tău când spectatorii trimit tip-uri — adăugat ca overlay Browser în SplitCam."),
         ("De ce nu apar MFC Alerts?", "Aproape întotdeauna ordinea straturilor — stratul Browser MFC Alerts trebuie să fie deasupra webcam-ului în lista de surse SplitCam."),
         ("Am nevoie de cont pentru MFC Alerts?", "Da — înregistrează-te pe mfcalerts.com pentru a obține URL-ul tău personal de alerts."),
         ("SplitCam e gratuit pentru asta?", "Da — SplitCam e gratuit, fără filigran și fără limită de timp, iar overlay-ul browser MFC Alerts rulează în el fără cost suplimentar."),
     ]},
    {"slug": "lovense", "name": "Lovense",
     "title": "Adaugă un toy Lovense la streamul tău cu SplitCam",
     "desc": "Conectează un toy interactiv Lovense la streamul cam cu SplitCam gratuit — Lovense SplitCam Toolset, alerts de tip pe ecran, reacții.",
     "kw": "adaugă lovense la stream, lovense cam stream, lovense splitcam, lovense splitcam toolset, lovense interactive toy streaming",
     "h1html": 'Cum adaugi un <span class="accent">toy Lovense</span> la streamul tău',
     "h1short": "Adaugă toy Lovense",
     "card": "Conectează un toy interactiv Lovense la streamul cam.",
     "intro": "Rulezi streamul cam prin <strong style='color:var(--text)'>SplitCam</strong> gratuit și împerechezi un toy <strong style='color:var(--text)'>Lovense</strong> care reacționează la tokeni. Lovense documentează un <strong style='color:var(--text)'>Lovense SplitCam Toolset</strong> oficial, iar SplitCam livrează un plugin Lovense oficial — integrarea e suportată de ambele părți.",
     "quick": "Pentru a adăuga un toy Lovense la stream: instalezi SplitCam și software-ul Lovense, împerechezi toy-ul, legi Lovense la platforma cam, adaugi statusul Lovense ca strat Browser în SplitCam, apoi transmiți normal."
              "<ol><li>Instalează SplitCam.</li><li>Instalează software Lovense și împerechează toy-ul.</li>"
              "<li>Leagă Lovense la cam-site-ul tău.</li>"
              "<li>Adaugă overlay Lovense în SplitCam.</li><li>Apasă Go Live.</li></ol>",
     "steps": [
         ("Instalează SplitCam",
          "SplitCam e software de streaming gratuit pentru Windows și macOS — encoderul care îți trimite videoul către platforma cam. Instalează; fără filigran."),
         ("Instalează software-ul Lovense și împerechează toy-ul",
          "Instalează Lovense Connect / Lovense Stream (aplicația desktop oficială). Pornește toy-ul și împerechează prin Bluetooth ca aplicația să arate conectat."),
         ("Leagă Lovense la platforma cam",
          "În aplicația Lovense conectezi contul cam ca toy-ul să reacționeze la tokenii / tip-urile spectatorilor. Majoritatea platformelor cam mari sunt suportate."),
         ("Adaugă overlay-ul Lovense în SplitCam",
          "Lovense oferă un URL de overlay / widget. Adaugă ca strat <strong>Browser</strong> în scena SplitCam ca spectatorii să vadă statusul toy-ului și tip-urile recente pe ecran."),
         ("Construiește scena și Go Live",
          "Adaugă camera și celelalte overlay-uri, lipește cheia RTMP a platformei cam în SplitCam și clic <strong>Go Live</strong>. Toy-ul reacționează la tip-uri în timp real."),
     ],
     "tips": [
         ("Folosește Lovense SplitCam Toolset oficial", "Lovense publică un toolset specific pentru SplitCam cu propriul ghid de instalare — adaugă overlay-ul de activitate al toy-ului și alerts de tip făcute pentru SplitCam."),
         ("Actualizează Lovense Cam Extension", "Toolset-ul cere o Lovense Cam Extension recentă (30.1.4 sau mai nouă) — actualizează înainte de live."),
         ("Ține toy-ul încărcat", "O baterie aproape goală în mijlocul show-ului ucide partea interactivă — încarcă complet înainte de live."),
         ("Testează reacția la tokeni", "Trimite un mic tip de test pentru a confirma că toy-ul reacționează înainte să deschizi camera."),
         ("Verifică cerințele de versiune", "Lovense SplitCam Toolset cere SplitCam 10.4.5 sau mai nou. Lovense Cam Extension acoperă oficial Chaturbate, Stripchat, BongaCams, MyFreeCams și CamSoda — pentru orice alt site, folosește integrarea Generic URL Lovense."),
     ],
     "faq": [
         ("Suportă Lovense SplitCam oficial?", "Da — Lovense documentează un «Lovense SplitCam Toolset» oficial cu propriul ghid de instalare, iar SplitCam livrează un plugin Lovense oficial. Integrarea e suportată de ambele părți."),
         ("Toy-ul se conectează direct la SplitCam?", "Nu — toy-ul împerechează cu aplicația Lovense; SplitCam afișează overlay-ul Lovense și transmite camera."),
         ("Ce cam-site-uri suportă Lovense?", "Cam Extension Lovense suportă oficial Chaturbate, Stripchat, BongaCams, MyFreeCams și CamSoda, cu suport variabil pentru altele — verifică lista actuală în aplicația Lovense."),
         ("Pot afișa tip-uri recente pe ecran?", "Da — adaugă URL-ul widget-ului Lovense ca strat Browser în SplitCam."),
     ]},
    {"slug": "multistream-cams", "name": "Mai multe cam-site-uri",
     "title": "Transmisie pe mai multe cam-site-uri simultan cu SplitCam",
     "desc": "Transmisie pe MyFreeCams, Chaturbate, BongaCams, CAM4, Stripchat și mai multe simultan cu multistreaming gratuit SplitCam. Un click, fără filigran.",
     "kw": "transmisie pe mai multe cam-site-uri, multistream cam sites, transmisie pe chaturbate și bongacams simultan, software multistream cam",
     "h1html": 'Cum transmiți pe <span class="accent">mai multe cam-site-uri</span> simultan',
     "h1short": "Multistreaming cam",
     "card": "Transmisie pe mai multe cam-site-uri simultan.",
     "intro": "<strong style='color:var(--text)'>SplitCam</strong> gratuit poate transmite o codare către <strong style='color:var(--text)'>mai multe cam-site-uri simultan</strong> — MyFreeCams, Chaturbate, BongaCams, CAM4, Stripchat și mai multe. Fără filigran, un click.",
     "quick": "Pentru transmisie pe mai multe cam-site-uri deodată: instalezi SplitCam, construiești scena, iei URL-ul serverului RTMP și stream key-ul fiecărui cam-site, adaugi toate în setările multistreaming SplitCam, clic Go Live o singură dată."
              "<ol><li>Instalează SplitCam.</li><li>Adaugă cameră + scenă.</li>"
              "<li>Ia o cheie RTMP de la fiecare cam-site.</li>"
              "<li>Adaugă toate cheile în multistream SplitCam.</li>"
              "<li>Apasă Go Live o singură dată.</li></ol>",
     "steps": [
         ("Instalează SplitCam",
          "SplitCam e software de streaming gratuit pentru Windows și macOS cu multistreaming integrat. Instalează — fără filigran, fără cont."),
         ("Setează cameră și scenă",
          "Deschide SplitCam, adaugă webcam-ul și construiește scena cu overlay-uri și filtre. O singură scenă alimentează fiecare destinație."),
         ("Ia o cheie RTMP de la fiecare cam-site",
          "Pe fiecare platformă cam activezi broadcasting extern / RTMP și copiezi <strong>URL-ul serverului</strong> și <strong>stream key-ul</strong>. Repetă pentru fiecare site pe care vrei să transmiți — vezi ghidurile individuale ale platformelor pentru rutele exacte."),
         ("Adaugă fiecare destinație în SplitCam",
          "Deschide <strong>Stream Settings</strong> și adaugă fiecare cam-site ca destinație RTMP personalizată — lipește URL serverului și cheia. Bifează tot ce vrei să fie live."),
         ("Clic Go Live o singură dată",
          "Apasă <strong>Go Live</strong>. SplitCam trimite streamul către fiecare cam-site selectat simultan, peer-to-peer, dintr-o singură codare — fără taxă suplimentară."),
     ],
     "tips": [
         ("Urmărește uploadul", "Multistreaming-ul multiplică încărcarea de upload. Fiecare destinație consumă bitrate-ul propriu — asigură-te că conexiunea ta poate susține suma."),
         ("Verifică regulile platformei", "Unele cam-site-uri interzic transmisia simultană în altă parte — confirmă înainte de multistreaming."),
         ("Cablu — drops nu îți permiți aici", "Multistreaming-ul multiplică încărcarea de upload, deci o singură întrerupere wi-fi poate dărâma toate destinațiile simultan. Cablu nu e opțional aici."),
         ("Urmărește monitorul de sănătate", "SplitCam arată statusul per destinație — renunță la un site dacă uploadul nu îl susține."),
     ],
     "faq": [
         ("Multistreaming-ul SplitCam e gratuit?", "Da — multistreaming-ul e integrat și gratuit, fără taxă per destinație, fără filigran."),
         ("Pe câte cam-site-uri pot transmite simultan?", "Câte poate susține banda ta de upload — fiecare destinație consumă bitrate-ul propriu."),
         ("Folosește cloud relay?", "Nu — SplitCam trimite streamurile peer-to-peer direct de pe PC către ingestul fiecărui platformei."),
         ("Multistreaming-ul îmi încetinește PC-ul?", "Codarea se face o dată și se reutilizează; codarea hardware ține CPU-ul jos. Banda de upload e limita reală."),
     ]},
    {"slug": "livejasmin", "name": "LiveJasmin",
     "title": "Transmisie pe LiveJasmin cu SplitCam — Encoder Extern HD",
     "desc": "Transmisie pe LiveJasmin cu SplitCam gratuit — encoder extern Model Center, setup HD 1080p, scene multi-cameră și overlay-uri. Fără filigran, fără înregistrare.",
     "kw": "transmisie livejasmin, livejasmin obs, livejasmin external encoder, livejasmin rtmp, livejasmin stream key, livejasmin model setup",
     "h1html": 'Cum transmiți pe <span class="accent">LiveJasmin</span> cu SplitCam',
     "h1short": "Transmisie LiveJasmin",
     "card": "Setup cu encoder extern pentru Model Center-ul HD-only LiveJasmin.",
     "intro": "LiveJasmin e nava amiral a Docler Holding — una dintre cele mai mari rețele cam din lume și o platformă HD-only. Broadcasterul preferat e clientul proprietar <strong>JasminCAM</strong>, dar Model Center expune și o cale standard de <strong>External Encoder</strong> la care se conectează <strong style='color:var(--text)'>SplitCam</strong> gratuit — și transmiți cu scene multi-cameră, filtre de beauty și overlay-uri pe același stream HD.",
     "quick": "Transmisie pe LiveJasmin cu SplitCam: instalezi SplitCam, construiești scena HD, în Model Center mergi la <em>Settings → Broadcast → External Encoder</em>, copiezi URL-ul serverului și stream key-ul, le lipești în SplitCam, Go Live."
              "<ol><li>Instalează SplitCam.</li><li>Adaugă cameră + scenă HD.</li>"
              "<li>Obține URL-ul și stream key-ul din Model Center.</li><li>Lipește în SplitCam.</li>"
              "<li>Apasă Go Live.</li></ol>",
     "key_how": "Loghează-te pe <strong>modelcenter.livejasmin.com</strong>, deschide <strong>Settings → Broadcast → External Encoder</strong>. Model Center afișează un <strong>URL server</strong> și o <strong>stream key</strong> legate de contul tău — copiază ambele în câmpurile RTMP custom ale SplitCam. <strong>Notă:</strong> conturile noi trebuie aprobate (48–72 ore) înainte ca opțiunea External Encoder să apară, iar platforma impune output HD-only.",
     "tips": [
         ("HD sau ești retrogradat", "LiveJasmin e HD-only — orice sub 1280×720 riscă să fie afișat doar pe listele cu plată mică, orice sub 1080p pierde eligibilitatea «Premium». Trage 1920×1080 la 30 fps, 4.000–6.000 Kbps."),
         ("JasminCAM vs encoder extern", "Clientul propriu JasminCAM al Docler dă cea mai curată conformitate HD, dar encoderele externe (OBS, SplitCam, vMix) sunt oficial suportate odată ce contul tău e aprobat — deblochează scene multi-cameră și overlay-uri pe care JasminCAM nu le poate face."),
         ("Free chat ≠ private show", "Free chat e doar preview — fără nuditate. Private și Gold show-urile sunt unde modelul câștigă. Planifică-ți scena să arate puternic îmbrăcată ȘI în modul show."),
         _T_ETH,
     ],
     "faq": [
         ("Suportă LiveJasmin oficial encodere externe ca SplitCam?", "Da — Model Center include opțiunea External Encoder în Settings → Broadcast. JasminCAM e clientul recomandat, dar OBS, SplitCam și alte encodere RTMP sunt explicit listate ca suportate odată ce contul tău de model e aprobat."),
         ("Unde îmi iau stream key-ul LiveJasmin?", "În Model Center: Settings → Broadcast → External Encoder. Atât URL-ul serverului, cât și stream key-ul unic apar acolo — copiază ambele în câmpurile RTMP custom ale SplitCam. Cheia e legată de contul tău; tratează ca o parolă."),
         ("Ce bitrate folosesc pentru LiveJasmin?", "LiveJasmin e HD-only — țintește 1920×1080 la 30 fps, 4.000–6.000 Kbps cu interval keyframe de 2 secunde. Orice vizibil sub atât pierde eticheta Premium și e retrogradat."),
         ("SplitCam e gratuit pentru LiveJasmin?", "Da — SplitCam e gratuit, fără filigran și fără limită de timp. Singurul cost e îndeplinirea cerințelor HD ale LiveJasmin, lucru pe care SplitCam îl gestionează nativ cu compoziția de scenă 1080p și filtrele de beauty."),
     ],
     "steps": [
         ("Descarcă și instalează SplitCam", "SplitCam e software gratuit de live-streaming pentru Windows și macOS — fără înregistrare, fără card, fără filigran. E encoderul care trimite video HD către LiveJasmin."),
         ("Construiește scena HD", "Deschide SplitCam și adaugă webcam-ul în modul 1080p. Pune deasupra overlay-uri, text, o a doua cameră sau telefonul, filtre de beauty sau un fundal AI — LiveJasmin cere calitate HD, iar scena ta compusă trebuie să arate premium atât în free chat, CÂT ȘI în private show-uri."),
         ("Obține URL-ul LiveJasmin și stream key-ul", "Loghează-te pe <strong>modelcenter.livejasmin.com</strong> (contul tău trebuie aprobat întâi — tipic 48–72 ore după înscriere). Deschide <strong>Settings → Broadcast → External Encoder</strong>. Pagina afișează un <strong>URL server</strong> și o <strong>stream key</strong> unică. Copiază ambele."),
         ("Conectează SplitCam la LiveJasmin", "În SplitCam deschide <strong>Stream Settings</strong>, lipește URL-ul serverului LiveJasmin și stream key-ul în câmpurile RTMP custom. Setează bitrate-ul la 4.000–6.000 Kbps la 1920×1080, 30 fps, cu keyframe la 2 secunde. Rulează mai întâi speed test-ul integrat — streamurile HD sunt pretențioase."),
         ("Apasă Go Live", "Apasă <strong>Go Live</strong> în SplitCam, apoi du-te online în Model Center LiveJasmin. În ~10 secunde feed-ul tău HD ajunge în rețeaua LiveJasmin. Transmisiile următoare sunt un singur clic — deschizi SplitCam, Go Live, apoi online pe LiveJasmin."),
     ],
    },
]
