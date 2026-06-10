# -*- coding: utf-8 -*-
"""Romanian (ro) content for cam-streaming-guides."""

_T_ETH = ("Folosește conexiune prin cablu", "Ethernet bate Wi-Fi într-un stream lung — un frame "
          "pierdut e un tip pierdut. Trage un cablu până la PC-ul de stream.")
_T_TEST = ("Fă mai întâi un test privat", "Rulează o transmisiune scurtă de test pentru cameră, "
           "audio, încadrare și overlay-uri înainte să deschizi camera publicului.")

PLATFORMS_RO = [
    {"slug": "chaturbate", "name": "Chaturbate",
     "title": "Cum transmiți pe Chaturbate cu SplitCam — token & RTMP",
     "desc": "Transmite pe Chaturbate cu SplitCam gratuit — broadcast token, encoder extern RTMP, scene multi-cameră și overlay-uri. Fără filigran.",
     "kw": "cum transmiți pe chaturbate, chaturbate, chaturbate broadcast, chaturbate broadcast token, chaturbate obs, chaturbate external encoder, chaturbate rtmp",
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
     "title": "Cum transmiți pe CAM4 cu SplitCam — encoder extern",
     "desc": "Transmite pe CAM4 cu SplitCam gratuit — External Encoder, stream key, geo-blocare, scene și overlay-uri. Fără filigran.",
     "kw": "cum transmiți pe cam4, cam4, cam4 broadcast, cam4 obs, cam4 external encoder, cam4 rtmp, cam4 stream key",
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
     "title": "Cum transmiți pe BongaCams cu SplitCam — encoder extern",
     "desc": "Transmite pe BongaCams cu SplitCam gratuit — External Encoder, scene multi-cameră, overlay-uri și fundal AI. Fără filigran.",
     "kw": "cum transmiți pe bongacams, bongacams, bongacams broadcast, bongacams obs, bongacams external encoder, bongacams rtmp, bongacams stream key",
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
     "title": "Cum transmiți pe Stripchat cu SplitCam — software extern",
     "desc": "Transmite pe Stripchat cu SplitCam gratuit — software extern, cheie-token RTMP, scene multi-cameră și overlay-uri. Fără filigran.",
     "kw": "cum transmiți pe stripchat, stripchat, stripchat broadcast, stripchat obs, stripchat external software, stripchat rtmp, stripchat stream key",
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
     "title": "Cum intri live pe OnlyFans cu SplitCam — cheie sau login",
     "desc": "Intră live pe OnlyFans cu SplitCam gratuit — autorizare sau OBS Key, scene multi-cameră și overlay-uri. Fără filigran.",
     "kw": "cum transmiți pe onlyfans, onlyfans, onlyfans live, onlyfans obs, onlyfans obs key, onlyfans stream key, onlyfans rtmp",
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
     "title": "Cum transmiți pe CamPlace cu SplitCam — encoder extern",
     "desc": "Transmite pe CamPlace cu SplitCam gratuit — encoder extern, cheie RTMP, scene multi-cameră și overlay-uri. Pas cu pas, fără filigran.",
     "kw": "cum transmiți pe camplace, camplace, camplace broadcast, camplace obs, camplace external encoder, camplace rtmp, camplace stream key",
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
     "title": "Cum transmiți pe CamSoda cu SplitCam — OBS Broadcaster",
     "desc": "Transmite pe CamSoda cu SplitCam gratuit — Use OBS Broadcaster, servere regionale, scene multi-cameră și overlay-uri. Fără filigran.",
     "kw": "cum transmiți pe camsoda, camsoda, camsoda broadcast, camsoda obs, camsoda obs broadcaster, camsoda rtmp, camsoda stream key",
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
     "title": "Cum transmiți pe Streamate cu SplitCam — SM Connect",
     "desc": "Transmite pe Streamate cu SplitCam gratuit — canal integrat, cheie SM Connect, scene multi-cameră și overlay-uri. Fără filigran.",
     "kw": "cum transmiți pe streamate, streamate, streamate broadcast, streamate sm connect, streamate obs, streamate rtmp, streamate stream key",
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
     "title": "Cum transmiți pe StreamRay cu SplitCam — OBS Broadcaster",
     "desc": "Transmite pe StreamRay cu SplitCam gratuit — URL postat în chat, OBS Broadcaster, scene multi-cameră și overlay-uri. Fără filigran.",
     "kw": "cum transmiți pe streamray, streamray, streamray broadcast, streamray obs, streamray obs broadcaster, streamray rtmp, streamray cam",
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
     "title": "Cum transmiți pe XLoveCam cu SplitCam — link RTMP & cheie",
     "desc": "Transmite pe XLoveCam cu SplitCam gratuit — link RTMP și cheie, servere regionale, scene multi-cameră și overlay-uri. Fără filigran.",
     "kw": "cum transmiți pe xlovecam, xlovecam, xlovecam broadcast, xlovecam obs, xlovecam external encoder, xlovecam rtmp, xlovecam stream key",
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
     "title": "Cum transmiți pe SoulCams cu SplitCam — setări OBS",
     "desc": "Transmite pe SoulCams cu SplitCam gratuit — setări OBS, server RTMP și cheie, scene multi-cameră și overlay-uri. Fără filigran.",
     "kw": "cum transmiți pe soulcams, soulcams, soulcams broadcast, soulcams obs, soulcams external encoder, soulcams rtmp, soulcams stream key",
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
     "title": "Cum folosești ImLive cu SplitCam — cameră virtuală",
     "desc": "Folosește ImLive cu SplitCam gratuit ca cameră virtuală — ImLive merge direct prin webcam (fără RTMP), cu scene multi-cameră și overlay-uri. Fără filigran.",
     "kw": "cum folosești imlive, imlive, imlive splitcam, imlive virtual camera, imlive cameră virtuală, imlive webcam, im live cam",
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
     "title": "Cum transmiți pe VXLive cu SplitCam — preset VISIT-X",
     "desc": "Transmite pe VXLive (VISIT-X) cu SplitCam gratuit — preset VISIT-X oficial, server și cheie, scene multi-cameră și overlay-uri. Fără filigran.",
     "kw": "cum transmiți pe vxlive, vxlive, visit-x, vxmodels, vxlive broadcast, vxlive obs, vxlive rtmp, vxlive stream key",
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
     "title": "Cum transmiți pe VirtWish cu SplitCam — URL stream & cheie",
     "desc": "Transmite pe VirtWish cu SplitCam gratuit — secțiunea OBS cu URL stream și cheie, scene multi-cameră și overlay-uri. Fără filigran.",
     "kw": "cum transmiți pe virtwish, virtwish, virtwish broadcast, virtwish obs, virtwish external encoder, virtwish rtmp, virtwish stream key",
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
     "title": "Cum transmiți pe XModels cu SplitCam — encoder extern",
     "desc": "Transmite pe XModels cu SplitCam gratuit — encoder extern în setările contului model, cheie RTMP, scene multi-cameră și overlay-uri. Fără filigran.",
     "kw": "cum transmiți pe xmodels, xmodels, xmodels broadcast, xmodels obs, xmodels external encoder, xmodels rtmp, xmodels stream key",
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
     "title": "Cum transmiți pe Flirt4Free cu SplitCam — encoder extern",
     "desc": "Transmite pe Flirt4Free cu SplitCam gratuit — External Broadcast Form cu RTMP URL și Stream Name, scene multi-cameră și overlay-uri. Fără filigran.",
     "kw": "cum transmiți pe flirt4free, flirt4free, flirt for free, flirt4free broadcast, flirt4free obs, flirt4free external encoder, flirt4free rtmp",
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
     "title": "Cum adaugi MFC Alerts în stream cu SplitCam",
     "desc": "Adaugă tip alerts animate în streamul MyFreeCams cu SplitCam gratuit — URL mfcalerts.com ca strat Browser, deasupra webcam-ului. Fără filigran.",
     "kw": "cum adaugi mfc alerts, mfc alerts, myfreecams, myfreecams alerts, mfcalerts, myfreecams tip alerts, mfc alerts overlay",
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
     "title": "Cum adaugi un toy Lovense în stream cu SplitCam",
     "desc": "Adaugă un toy interactiv Lovense în streamul cam cu SplitCam gratuit — Lovense SplitCam Toolset, alerts de tip pe ecran și reacții. Fără filigran.",
     "kw": "cum adaugi lovense în stream, lovense, lovense splitcam, lovense splitcam toolset, lovense cam, lovense toy, lovense interactive toy",
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
     "title": "Cum transmiți pe mai multe cam-site-uri simultan cu SplitCam",
     "desc": "Transmite simultan pe Chaturbate, BongaCams, CAM4, Stripchat și altele cu multistreaming gratuit SplitCam — un click, fără filigran.",
     "kw": "transmisie pe mai multe cam-site-uri, multistream cam, software multistream cam, transmisie pe chaturbate și bongacams simultan, multistreaming cam",
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
     "title": "Cum transmiți pe LiveJasmin cu SplitCam — encoder extern",
     "desc": "Transmite pe LiveJasmin cu SplitCam gratuit — encoder extern Model Center, setup HD 1080p, scene multi-cameră și overlay-uri. Fără filigran.",
     "kw": "cum transmiți pe livejasmin, livejasmin, livejasmin broadcast, livejasmin obs, livejasmin external encoder, livejasmin rtmp, livejasmin stream key",
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
    {"slug": "myfreecams", "name": "MyFreeCams",
     "title": "Cum transmiți pe MyFreeCams cu SplitCam — encoder extern",
     "desc": "Transmite pe MyFreeCams cu SplitCam gratuit — Model Admin External Broadcaster, scene multi-cameră și overlay-uri. Fără filigran.",
     "kw": "cum transmiți pe myfreecams, myfreecams, mfc external broadcaster, myfreecams obs, mfc rtmp, mfc stream key, mfc token",
     "h1html": 'Cum transmiți pe <span class="accent">MyFreeCams</span> cu SplitCam',
     "h1short": "Transmisie MyFreeCams",
     "card": "Setup cu external broadcaster pentru Model Admin-ul pe tokens al MFC.",
     "intro": "MyFreeCams (MFC) e una dintre cele mai vechi platforme cam — economie pură pe tokens, fără filtru sufocant de aprobare a modelelor și o bază loială de Premium members. Model Web Broadcaster-ul implicit e un tool de browser cu o singură cameră, dar <strong>Model Admin</strong> expune și o opțiune <strong>External Broadcaster</strong> la care se conectează <strong style='color:var(--text)'>SplitCam</strong> gratuit — deblocând scene multi-cameră, overlay-uri și filtre pe același stream pe tokens.",
     "quick": "Transmisie pe MyFreeCams cu SplitCam: instalezi SplitCam, construiești scena, în Model Admin → Broadcaster comuți de la Web Broadcaster la External Broadcaster, copiezi URL-ul serverului și stream key-ul, le lipești în SplitCam, Go Live."
              "<ol><li>Instalează SplitCam.</li><li>Adaugă cameră + scenă.</li>"
              "<li>Comută în Model Admin pe External Broadcaster.</li><li>Lipește URL+key în SplitCam.</li>"
              "<li>Apasă Go Live.</li></ol>",
     "key_how": "Loghează-te pe MyFreeCams, deschide <strong>Model Admin → Broadcaster</strong> și comută de la <strong>Web Broadcaster</strong> la <strong>External Broadcaster</strong>. Pagina dezvăluie un <strong>URL server</strong> (rtmp://publish.myfreecams.com…) și o <strong>stream key</strong> legate de contul tău de model — copiază ambele în câmpurile RTMP custom ale SplitCam.",
     "tips": [
         ("Tokens MFC, nu abonamente", "MFC e economie pură de tipping/tokens — Premium members pot intra în private, dar pâinea ta de zi cu zi rămân bacșișurile în free chat. Optimizează scena pentru tip menu vizibil și reacții live."),
         ("Web vs External Broadcaster", "Implicitul e single-source, doar webcam din browser; External Broadcaster deblochează scene multi-cameră, overlay-uri și beauty filters din SplitCam pe același stream."),
         ("Integrare MFC Alerts", "Adaugă URL-ul de alerte de la mfcalerts.com ca strat Browser deasupra camerei — primești alerte animate de tips care îi împing pe viewers spre tokens noi."),
         _T_ETH,
     ],
     "faq": [
         ("Suportă MFC broadcasteri externi?", "Da — Model Admin are opțiunea External Broadcaster, RTMP standard, OBS/SplitCam/vMix funcționează cu toate. Web Broadcaster-ul implicit e doar varianta rapidă din browser."),
         ("Unde îmi iau stream key-ul pentru MFC?", "Model Admin → Broadcaster → External Broadcaster afișează URL-ul serverului (rtmp://publish.myfreecams.com…) și stream key-ul tău unic. Copiază ambele în câmpurile RTMP custom ale SplitCam."),
         ("Ce bitrate folosesc pentru MyFreeCams?", "Până la ~6.000 Kbps cu keyframe de 2 secunde; trage 1920×1080 la 30 fps, 3.500–6.000 Kbps. MFC nu impune HD strict, dar Premium members văd diferența imediat."),
         ("SplitCam e gratuit pentru MFC?", "Da — SplitCam e gratuit, fără filigran și fără limită de timp. Nu există taxă de broadcaster din partea MFC pentru folosirea External Broadcaster — doar te conectezi prin RTMP."),
     ],
     "steps": [
         ("Descarcă și instalează SplitCam", "SplitCam e software gratuit de live-streaming pentru Windows și macOS — fără înregistrare, fără card, fără filigran. E encoderul care trimite video către MyFreeCams."),
         ("Construiește scena", "Deschide SplitCam și adaugă webcam-ul. Pune deasupra overlay-uri, text, o a doua cameră sau telefonul, filtre de beauty sau un fundal AI. Adaugă URL-ul de la mfcalerts.com ca strat Browser pentru alerte animate de tips în timp ce streamezi."),
         ("Comută pe External Broadcaster", "Loghează-te în Model Admin → <strong>Broadcaster</strong> și comută de la <strong>Web Broadcaster</strong> la <strong>External Broadcaster</strong>. Pagina afișează un URL server (rtmp://publish.myfreecams.com…) și o stream key unică. Copiază ambele."),
         ("Conectează SplitCam la MFC", "În SplitCam deschide <strong>Stream Settings</strong>, lipește URL-ul serverului MFC și stream key-ul în câmpurile RTMP custom. Setează bitrate-ul la 3.500–6.000 Kbps la 1920×1080, 30 fps, cu keyframe la 2 secunde."),
         ("Apasă Go Live", "Apasă <strong>Go Live</strong> în SplitCam — în câteva secunde apari în lista MyFreeCams. Transmisiile următoare sunt un singur clic: deschizi SplitCam, Go Live."),
     ],
    },
    {"slug": "cherry-tv", "name": "Cherry.tv",
     "title": "Cum transmiți pe Cherry.tv cu SplitCam — encoder extern",
     "desc": "Transmite pe Cherry.tv cu SplitCam gratuit — Streamer Dashboard cu encoder extern, scene multi-cameră și overlay-uri. Fără filigran.",
     "kw": "cum transmiți pe cherry.tv, cherry.tv, cherry.tv broadcast, cherry.tv obs, cherry.tv external encoder, cherry.tv rtmp, cherry.tv stream key",
     "h1html": 'Cum transmiți pe <span class="accent">Cherry.tv</span> cu SplitCam',
     "h1short": "Transmisie Cherry.tv",
     "card": "Setup cu encoder extern pentru Streamer Dashboard-ul Cherry.tv.",
     "intro": "Cherry.tv e o platformă cam mai nouă, în creștere rapidă, cu un unghi Web3 — payout-uri prietenoase cu cripto și o barieră de intrare mai joasă decât rețelele vechi precum LiveJasmin. Broadcasterul implicit e bazat pe browser, dar <strong>Streamer Dashboard</strong> expune calea standard de <strong>External Encoder</strong> la care se conectează <strong style='color:var(--text)'>SplitCam</strong> gratuit.",
     "quick": "Transmisie pe Cherry.tv cu SplitCam: instalezi SplitCam, construiești scena, în Streamer Dashboard → Broadcast Settings → External Encoder copiezi URL-ul și stream key-ul, le lipești în SplitCam, Go Live."
              "<ol><li>Instalează SplitCam.</li><li>Adaugă cameră + scenă.</li>"
              "<li>Obține URL și stream key din Streamer Dashboard.</li><li>Lipește în SplitCam.</li>"
              "<li>Apasă Go Live.</li></ol>",
     "key_how": "Loghează-te în contul tău de streamer Cherry.tv, deschide <strong>Streamer Dashboard → Broadcast Settings → External Encoder</strong>. Apar un <strong>URL server</strong> și o <strong>stream key</strong> — copiază ambele. Conturile noi trec mai întâi printr-o verificare de bază (rapidă).",
     "tips": [
         ("Intrare mai ușoară, trafic în creștere", "Fără review de 72 de ore în stil Docler — Cherry.tv aprobă mult mai rapid și e un spot bun de early mover, cu audiență tânără și platform-savvy."),
         ("Payout-uri în cripto disponibile", "Cherry.tv oferă plăți în cripto alături de fiat standard — util dacă vrei să eviți frecușul bancar sau să încasezi mai discret."),
         ("Browser broadcaster e single-source", "Broadcasterul implicit din browser e o singură cameră; SplitCam prin External Encoder deblochează multi-cameră, overlay-uri și beauty filters pe același stream."),
         _T_ETH,
     ],
     "faq": [
         ("Suportă Cherry.tv encodere externe?", "Da — Streamer Dashboard include opțiunea External Encoder, RTMP standard. OBS, SplitCam și vMix funcționează imediat după verificarea contului."),
         ("Unde îmi iau stream key-ul pentru Cherry.tv?", "Streamer Dashboard → Broadcast Settings → External Encoder. Atât URL-ul serverului, cât și stream key-ul unic apar acolo — copiază ambele în câmpurile RTMP custom ale SplitCam."),
         ("Ce bitrate folosesc pentru Cherry.tv?", "3.500–6.000 Kbps la 1920×1080, 30 fps, cu keyframe la 2 secunde. Audiența Cherry.tv e tânără și obișnuită cu calitate bună — nu trișa la rezoluție."),
         ("SplitCam e gratuit pentru Cherry.tv?", "Da — SplitCam e gratuit, fără filigran și fără limită de timp. Cherry.tv nu taxează separat folosirea unui encoder extern."),
     ],
     "steps": [
         ("Descarcă și instalează SplitCam", "SplitCam e software gratuit de live-streaming pentru Windows și macOS — fără înregistrare, fără card, fără filigran. E encoderul care trimite video către Cherry.tv."),
         ("Construiește scena", "Deschide SplitCam și adaugă webcam-ul. Pune deasupra overlay-uri, text, o a doua cameră sau telefonul, filtre de beauty sau un fundal AI — audiența Cherry.tv e tânără și platform-savvy, scena trebuie să arate modern."),
         ("Obține URL și stream key", "În contul de streamer deschide <strong>Streamer Dashboard → Broadcast Settings → External Encoder</strong>. Copiază URL-ul serverului și stream key-ul unic."),
         ("Conectează SplitCam la Cherry.tv", "În SplitCam deschide <strong>Stream Settings</strong>, lipește URL-ul serverului Cherry.tv și stream key-ul în câmpurile RTMP custom. Bitrate 3.500–6.000 Kbps la 1920×1080, 30 fps, keyframe la 2 secunde."),
         ("Apasă Go Live", "Apasă <strong>Go Live</strong> în SplitCam, apoi du-te online din Streamer Dashboard. În câteva secunde apari în listele Cherry.tv. Transmisiile următoare sunt un singur clic."),
     ],
    },
    {"slug": "amateurtv", "name": "AmateurTV",
     "title": "Cum transmiți pe AmateurTV cu SplitCam — encoder extern",
     "desc": "Transmite pe AmateurTV cu SplitCam gratuit — Model Panel cu encoder extern, scene multi-cameră și overlay-uri. Fără filigran.",
     "kw": "cum transmiți pe amateurtv, amateurtv, amateurtv broadcast, amateurtv obs, amateurtv external encoder, amateurtv rtmp, amateurtv stream key",
     "h1html": 'Cum transmiți pe <span class="accent">AmateurTV</span> cu SplitCam',
     "h1short": "Transmisie AmateurTV",
     "card": "Setup cu encoder extern pentru rețeaua de limbă spaniolă AmateurTV.",
     "intro": "AmateurTV e rețeaua cam lider în spațiul hispanofon — audiență puternică în Spania, Mexic, Argentina și prin toată America Latină. Broadcasterul implicit din Model Panel merge în browser, dar expune și calea standard de <strong>external encoder</strong>, la care se conectează <strong style='color:var(--text)'>SplitCam</strong> gratuit — astfel transmiți cu scene multi-cameră, beauty filters și overlay-uri către o audiență hispanofonă pe care rețelele US-centric nu o servesc bine.",
     "quick": "Transmisie pe AmateurTV cu SplitCam: instalezi SplitCam, construiești scena, în Model Panel deschizi <em>Broadcast Settings → External Encoder</em>, copiezi URL-ul și stream key-ul, le lipești în SplitCam, Go Live."
              "<ol><li>Instalează SplitCam.</li><li>Adaugă cameră + scenă.</li>"
              "<li>Obține URL și stream key din Model Panel.</li><li>Lipește în SplitCam.</li>"
              "<li>Apasă Go Live.</li></ol>",
     "key_how": "Loghează-te în contul tău de model AmateurTV, deschide <strong>Model Panel → Broadcast Settings → External Encoder</strong>. Apar un <strong>URL server</strong> și o <strong>stream key</strong> legate de cont — copiază-le în câmpurile RTMP custom ale SplitCam. Conturile noi trec mai întâi prin verificarea ID-ului înainte de a transmite.",
     "tips": [
         ("Audiența hispanofonă pe primul loc", "Traficul AmateurTV e covârșitor de limbă spaniolă — Spania pe timpul zilei, LatAm pe seara orei US. Titlurile, textul din scenă și overlay-urile în spaniolă bat clar varianta doar-în-engleză pe această rețea."),
         ("Fusul LatAm e prime time-ul tău", "Vârful de trafic corelează cu serile LatAm (UTC-3 la UTC-6). Dacă ești flexibil, transmisia târziu seara CET / dimineața devreme oră asiatică prinde și vârful Spaniei și pe cel LatAm."),
         ("Payout-uri mid-tier stabile", "Nu cel mai mare RPM din industrie, dar stabil — AmateurTV plătește constant, iar nișa hispanofonă are concurență mai mică decât rețelele top US."),
         _T_ETH,
     ],
     "faq": [
         ("Suportă AmateurTV oficial encodere externe precum SplitCam?", "Da — Model Panel include opțiunea External Encoder sub Broadcast Settings. AmateurTV furnizează URL server RTMP standard și stream key; OBS, SplitCam, vMix și alte encodere RTMP se conectează."),
         ("Unde îmi iau stream key-ul pentru AmateurTV?", "Model Panel → Broadcast Settings → External Encoder. Atât URL-ul serverului, cât și stream key-ul apar acolo. Copiază ambele în câmpurile RTMP custom ale SplitCam. Cheia e legată de cont."),
         ("Ce bitrate folosesc pentru AmateurTV?", "Setări standard de cam-quality — împinge 1920×1080 la 30 fps, 3.500–6.000 Kbps cu keyframe la 2 secunde. Rulează întâi speed test-ul integrat din SplitCam."),
         ("SplitCam e gratuit pentru AmateurTV?", "Da — SplitCam e gratuit, fără filigran și fără limită de timp. Opțiunea External Encoder a AmateurTV se activează gratuit."),
     ],
     "steps": [
         ("Descarcă și instalează SplitCam", "SplitCam e software gratuit de live-streaming pentru Windows și macOS — fără înregistrare, fără card, fără filigran. E encoderul care trimite video către AmateurTV."),
         ("Construiește scena", "Deschide SplitCam și adaugă webcam-ul. Pune deasupra overlay-uri, text, o a doua cameră sau telefonul, filtre de beauty sau un fundal AI. Folosește text în spaniolă pe overlay-uri pentru audiența hispanofonă a AmateurTV."),
         ("Obține URL și stream key AmateurTV", "În contul tău de model deschide <strong>Model Panel → Broadcast Settings → External Encoder</strong>. Copiază URL-ul serverului și stream key-ul unic."),
         ("Conectează SplitCam la AmateurTV", "În SplitCam deschide <strong>Stream Settings</strong>, lipește URL-ul serverului AmateurTV și stream key-ul în câmpurile RTMP custom. Bitrate 3.500–6.000 Kbps la 1920×1080, 30 fps, keyframe la 2 secunde. Rulează întâi speed test-ul integrat."),
         ("Apasă Go Live", "Apasă <strong>Go Live</strong> în SplitCam, apoi du-te online din Model Panel pe AmateurTV. În ~10 secunde stream-ul ajunge la rețea. Transmisiile următoare sunt un singur clic — deschizi SplitCam, Go Live."),
     ],
    },
    {"slug": "camster", "name": "Camster",
     "title": "Cum transmiți pe Camster cu SplitCam — encoder extern",
     "desc": "Transmite pe Camster cu SplitCam gratuit — Model Hub cu encoder extern, scene multi-cameră și overlay-uri. Fără filigran.",
     "kw": "cum transmiți pe camster, camster, camster broadcast, camster obs, camster external encoder, camster rtmp, camster stream key",
     "h1html": 'Cum transmiți pe <span class="accent">Camster</span> cu SplitCam',
     "h1short": "Transmisie Camster",
     "card": "Setup cu encoder extern pentru Model Hub-ul Camster.",
     "intro": "Camster e o platformă cam mid-tier consacrată — mai mică decât Chaturbate sau LiveJasmin, dar cu o bază loială de utilizatori și payout-uri corecte. Broadcasterul implicit din Model Hub merge în browser, dar expune și calea standard de <strong>external encoder</strong>, la care se conectează <strong style='color:var(--text)'>SplitCam</strong> gratuit — astfel transmiți cu scene multi-cameră, overlay-uri și filtre pe care broadcasterul integrat nu le poate livra.",
     "quick": "Transmisie pe Camster cu SplitCam: instalezi SplitCam, construiești scena, în Model Hub deschizi <em>Broadcast Settings → External Encoder</em>, copiezi URL-ul și stream key-ul, le lipești în SplitCam, Go Live."
              "<ol><li>Instalează SplitCam.</li><li>Adaugă cameră + scenă.</li>"
              "<li>Obține URL și stream key din Model Hub.</li><li>Lipește în SplitCam.</li>"
              "<li>Apasă Go Live.</li></ol>",
     "key_how": "Loghează-te în contul tău de model Camster, deschide <strong>Model Hub → Broadcast Settings → External Encoder</strong>. Apar un <strong>URL server</strong> și o <strong>stream key</strong> legate de cont — copiază-le în câmpurile RTMP custom ale SplitCam. Cheia e legată de cont; tratează-o ca pe o parolă.",
     "tips": [
         ("Mid-tier înseamnă mai puțină concurență", "Camster are trafic stabil, dar mai puțini broadcasteri decât rețelele top — mai ușor să ajungi pe prima pagină cu o scenă îngrijită și un program constant."),
         ("Browser broadcaster vs extern", "Broadcasterul implicit din browser e single-source. SplitCam prin External Encoder deblochează scene multi-cameră, overlay-uri, beauty filters și fundal AI."),
         ("Payout-uri stabile, split-uri corecte", "Split-ul de venit al Camster e corect pentru nivelul mid-tier — nu cel mai mare din industrie, dar payout-uri lunare fiabile și puține plângeri de la modele despre întârzieri de plată."),
         _T_ETH,
     ],
     "faq": [
         ("Suportă Camster oficial encodere externe precum SplitCam?", "Da — Model Hub include opțiunea External Encoder sub Broadcast Settings. URL server RTMP standard și stream key; OBS, SplitCam și alte encodere RTMP se conectează."),
         ("Unde îmi iau stream key-ul pentru Camster?", "Model Hub → Broadcast Settings → External Encoder. Atât URL-ul serverului, cât și stream key-ul apar acolo. Copiază ambele în câmpurile RTMP custom ale SplitCam."),
         ("Ce bitrate folosesc pentru Camster?", "Setări standard de cam-quality — împinge 1920×1080 la 30 fps, 3.500–6.000 Kbps cu keyframe la 2 secunde. Rulează întâi speed test-ul integrat din SplitCam."),
         ("SplitCam e gratuit pentru Camster?", "Da — SplitCam e gratuit, fără filigran și fără limită de timp. Opțiunea External Encoder a Camster e gratuită."),
     ],
     "steps": [
         ("Descarcă și instalează SplitCam", "SplitCam e software gratuit de live-streaming pentru Windows și macOS — fără înregistrare, fără card, fără filigran."),
         ("Construiește scena", "Deschide SplitCam și adaugă webcam-ul. Pune deasupra overlay-uri, text, o a doua cameră sau telefonul, filtre de beauty sau un fundal AI — toate aplicate live."),
         ("Obține URL și stream key Camster", "În contul tău de model deschide <strong>Model Hub → Broadcast Settings → External Encoder</strong>. Copiază URL-ul serverului și stream key-ul unic."),
         ("Conectează SplitCam la Camster", "În SplitCam deschide <strong>Stream Settings</strong>, lipește URL-ul serverului Camster și stream key-ul în câmpurile RTMP custom. Bitrate 3.500–6.000 Kbps la 1920×1080, 30 fps, keyframe la 2 secunde. Rulează întâi speed test-ul integrat."),
         ("Apasă Go Live", "Apasă <strong>Go Live</strong> în SplitCam, apoi du-te online din Model Hub pe Camster. În ~10 secunde stream-ul ajunge la Camster."),
     ],
    },
    {"slug": "camversity", "name": "Camversity",
     "title": "Cum transmiți pe Camversity cu SplitCam — encoder extern",
     "desc": "Transmite pe Camversity cu SplitCam gratuit — Performer Dashboard cu encoder extern, scene multi-cameră și overlay-uri. Fără filigran.",
     "kw": "cum transmiți pe camversity, camversity, camversity broadcast, camversity obs, camversity external encoder, camversity rtmp, camversity stream key",
     "h1html": 'Cum transmiți pe <span class="accent">Camversity</span> cu SplitCam',
     "h1short": "Transmisie Camversity",
     "card": "Setup cu encoder extern pentru Performer Dashboard-ul Camversity.",
     "intro": "Camversity e o platformă cam independentă în creștere, axată pe unelte prietenoase cu performerii și rate de comision mai mici decât rețelele moștenite. Broadcasterul implicit din Performer Dashboard merge în browser, dar expune și calea standard de <strong>external encoder</strong>, la care se conectează <strong style='color:var(--text)'>SplitCam</strong> gratuit — astfel transmiți cu scene multi-cameră, overlay-uri și filtre.",
     "quick": "Transmisie pe Camversity cu SplitCam: instalezi SplitCam, construiești scena, în Performer Dashboard deschizi <em>Stream Settings → External Encoder</em>, copiezi URL-ul și stream key-ul, le lipești în SplitCam, Go Live."
              "<ol><li>Instalează SplitCam.</li><li>Adaugă cameră + scenă.</li>"
              "<li>Obține URL și stream key din Performer Dashboard.</li><li>Lipește în SplitCam.</li>"
              "<li>Apasă Go Live.</li></ol>",
     "key_how": "Loghează-te în contul tău de performer Camversity, deschide <strong>Performer Dashboard → Stream Settings → External Encoder</strong>. Apar un <strong>URL server</strong> și o <strong>stream key</strong> legate de cont — copiază-le în câmpurile RTMP custom ale SplitCam. Conturile noi trec prin verificarea ID-ului standard înainte de a transmite.",
     "tips": [
         ("Split-uri prietenoase cu performerii", "Split-ul de venit al Camversity e mai favorabil performerilor decât la rețelele moștenite — merită comparat cu platforma ta principală actuală dacă ești la început în cariera cam."),
         ("Onboarding mai ușor decât Docler", "Verificarea Camversity e mai rapidă decât aprobarea de 48–72h a LiveJasmin, dar rămâne legitimă (fără modele random / neverificate). Un middle ground bun."),
         ("Construiește o scenă, nu doar un webcam", "Broadcasterul implicit din Performer Dashboard al Camversity e single-source. SplitCam prin External Encoder deblochează multi-cameră, overlay-uri, beauty filters."),
         _T_ETH,
     ],
     "faq": [
         ("Suportă Camversity oficial encodere externe precum SplitCam?", "Da — Performer Dashboard include opțiunea External Encoder sub Stream Settings. URL server RTMP standard și stream key; OBS, SplitCam, vMix se conectează."),
         ("Unde îmi iau stream key-ul pentru Camversity?", "Performer Dashboard → Stream Settings → External Encoder. Atât URL-ul serverului, cât și stream key-ul apar acolo."),
         ("Ce bitrate folosesc pentru Camversity?", "Împinge 1920×1080 la 30 fps, 3.500–6.000 Kbps cu keyframe la 2 secunde. Rulează întâi speed test-ul integrat din SplitCam."),
         ("SplitCam e gratuit pentru Camversity?", "Da — SplitCam e gratuit, fără filigran și fără limită de timp. Opțiunea External Encoder a Camversity e gratuită."),
     ],
     "steps": [
         ("Descarcă și instalează SplitCam", "SplitCam e software gratuit de live-streaming pentru Windows și macOS — fără înregistrare, fără card, fără filigran."),
         ("Construiește scena", "Deschide SplitCam și adaugă webcam-ul. Pune deasupra overlay-uri, text, o a doua cameră sau telefonul, filtre de beauty sau un fundal AI."),
         ("Obține URL și stream key Camversity", "În contul tău de performer deschide <strong>Performer Dashboard → Stream Settings → External Encoder</strong>. Copiază URL-ul serverului și stream key-ul unic."),
         ("Conectează SplitCam la Camversity", "În SplitCam deschide <strong>Stream Settings</strong>, lipește URL-ul serverului Camversity și stream key-ul în câmpurile RTMP custom. Bitrate 3.500–6.000 Kbps la 1920×1080, 30 fps, keyframe la 2 secunde."),
         ("Apasă Go Live", "Apasă <strong>Go Live</strong> în SplitCam, apoi du-te online din Performer Dashboard. În ~10 secunde stream-ul ajunge la Camversity."),
     ],
    },
    {"slug": "skyprivate", "name": "SkyPrivate",
     "title": "Cum folosești SkyPrivate cu SplitCam — cameră virtuală",
     "desc": "Folosește SkyPrivate cu SplitCam gratuit ca cameră virtuală în apelurile Skype — scene multi-cameră, overlay-uri și beauty filters. Fără filigran.",
     "kw": "cum folosești skyprivate, skyprivate, skyprivate splitcam, skyprivate virtual camera, skyprivate skype, sky private cam, cam plată pe minut",
     "h1html": 'Cum folosești <span class="accent">SkyPrivate</span> cu SplitCam',
     "h1short": "SplitCam pe SkyPrivate",
     "card": "Setup virtual camera pentru apelurile cam prin Skype ale SkyPrivate.",
     "intro": "SkyPrivate e o platformă cam aparte — în loc de transmisie RTMP, monetizează <strong>apeluri cam private prin Skype, cu plată pe minut</strong>. Clienții rezervă și plătesc pe minut în marketplace-ul SkyPrivate, apoi apelul video efectiv rulează prin Skype. <strong style='color:var(--text)'>SplitCam</strong> gratuit se conectează ca <strong>virtual camera</strong>: îți construiești scena în SplitCam, apoi alegi SplitCam ca cameră în Skype înainte să răspunzi unui apel rezervat prin SkyPrivate.",
     "quick": "Folosește SkyPrivate cu SplitCam: instalezi SplitCam, construiești scena, instalezi Skype cu add-on-ul SkyPrivate, în <em>Video Settings</em> din Skype selectezi SplitCam ca cameră și microfon, apoi răspunzi apelurilor rezervate prin SkyPrivate — Skype livrează clientului scena compusă."
              "<ol><li>Instalează SplitCam.</li><li>Construiește scena în SplitCam.</li>"
              "<li>Instalează Skype + add-on SkyPrivate.</li><li>Selectează SplitCam ca cameră în Skype.</li>"
              "<li>Răspunde apelurilor.</li></ol>",
     "key_how": "SkyPrivate nu folosește RTMP sau stream key — folosește Skype ca transport video cu un add-on de facturare pe minut. Instalează Skype, instalează add-on-ul de browser/desktop SkyPrivate, apoi în Skype deschide <strong>Settings → Audio &amp; Video → Camera</strong> și selectează <strong>SplitCam</strong> în locul webcam-ului. Scena compusă în SplitCam (overlay-uri, multi-cameră, beauty filters) devine ce vede clientul SkyPrivate prin Skype.",
     "tips": [
         ("Fără RTMP — flux de virtual camera", "Nu căuta URL server sau stream key. SkyPrivate rulează prin Skype, iar Skype vede SplitCam doar ca un webcam. Construiește scena în SplitCam, apoi alege SplitCam în setările camerei din Skype."),
         ("Setează SplitCam și ca microfon", "În setările Audio din Skype selectează SplitCam și ca microfon, nu doar ca cameră — așa noise-suppression, audio mixat și muzica de intro ajung toate la client."),
         ("Adaugă un test de apel prin Skype", "Înainte de primul apel SkyPrivate plătit, fă un apel gratuit de test prin Skype (Echo / Sound Test Service) ca să confirmi că SplitCam e camera activă și că scena ta e compusă corect."),
         _T_TEST,
     ],
     "faq": [
         ("Folosește SkyPrivate RTMP sau stream key?", "Niciuna. SkyPrivate gestionează facturarea și rezervările; video-ul efectiv rulează prin Skype. Nu ai nevoie de URL server RTMP sau stream key — doar configurezi SplitCam ca cameră în Skype."),
         ("Cum selectez SplitCam în Skype pentru SkyPrivate?", "Deschide Skype Settings → Audio &amp; Video → Camera, alege SplitCam din listă. Fă la fel pentru Microphone. Apelurile SkyPrivate ajung apoi ca apeluri Skype normale, cu scena ta din SplitCam ca feed de cameră."),
         ("Pot folosi overlay-uri și beauty filters cu SkyPrivate?", "Da — construiește-le în scena ta din SplitCam. Skype primește doar rezultatul compus ca un singur feed de cameră, deci tot ce compune SplitCam (overlay-uri, beauty filters, fundal AI, scene multi-cameră) e vizibil pentru clientul SkyPrivate."),
         ("SplitCam e gratuit pentru SkyPrivate?", "Da — SplitCam e gratuit, fără filigran și fără limită de timp. Ca virtual camera pentru apeluri SkyPrivate prin Skype, nu adaugă cost sau branding la apel."),
     ],
     "steps": [
         ("Instalează SplitCam", "SplitCam e gratuit pentru Windows și macOS — fără înregistrare, fără card, fără filigran. Pentru SkyPrivate, funcționează ca <strong>virtual camera</strong> pe care Skype o vede ca pe orice webcam."),
         ("Construiește scena în SplitCam", "Deschide SplitCam și folosește <strong>Media Layers +</strong> pentru a adăuga webcam-ul plus orice overlay-uri, text, beauty filters sau fundal AI. Această scenă compusă e ce Skype va livra clientului SkyPrivate."),
         ("Instalează Skype și add-on-ul SkyPrivate", "Instalează Skype pe același PC, autentifică-te, apoi instalează add-on-ul / aplicația desktop SkyPrivate urmând onboarding-ul SkyPrivate. Add-on-ul gestionează facturarea pe minut pe partea SkyPrivate."),
         ("Selectează SplitCam ca cameră și mic în Skype", "În Skype deschide <strong>Settings → Audio &amp; Video</strong>. Setează <strong>Camera = SplitCam</strong> și <strong>Microphone = SplitCam</strong>. Rulează un apel rapid de test prin Skype (Echo / Sound Test Service) ca să confirmi că scena arată și sună corect."),
         ("Răspunde la apeluri SkyPrivate", "Când un client SkyPrivate rezervă un apel plătit, acesta ajunge ca apel Skype — răspunde. Clientul vede scena ta compusă în SplitCam; SkyPrivate facturează pe minut. Ajustează scena în timpul apelului editând-o în SplitCam — Skype actualizează instant."),
     ],
    },
    {"slug": "manyvids", "name": "ManyVids",
     "title": "Cum intri live pe ManyVids (MV Live) cu SplitCam",
     "desc": "Intră live pe MV Live de la ManyVids cu SplitCam gratuit — Creator Studio cu encoder extern, scene multi-cameră și overlay-uri. Fără filigran.",
     "kw": "cum transmiți pe manyvids, manyvids, mv live, manyvids live, manyvids obs, manyvids external encoder, manyvids rtmp, manyvids stream key",
     "h1html": 'Cum transmiți pe <span class="accent">MV Live</span> cu SplitCam',
     "h1short": "Transmisie pe MV Live",
     "card": "Setup cu encoder extern pentru Creator Studio MV Live de la ManyVids.",
     "intro": "ManyVids e o platformă de tip creator-economy — vânzări de clipuri, video-uri custom, abonamente fan club și produsul de live-streaming <strong>MV Live</strong>. Broadcasterul implicit din Creator Studio rulează în browser, dar expune și o cale standard de <strong>external encoder</strong> la care se conectează <strong style='color:var(--text)'>SplitCam</strong> gratuit — astfel transmiți cu scene multi-cameră, overlay-uri și filtre pe aceeași platformă prietenoasă cu creatorii.",
     "quick": "Transmisie pe MV Live cu SplitCam: instalezi SplitCam, construiești scena, în Creator Studio deschizi <em>MV Live → Broadcast Settings → External Encoder</em>, copiezi URL-ul serverului și stream key-ul, le lipești în SplitCam, Go Live."
              "<ol><li>Instalează SplitCam.</li><li>Adaugă cameră + scenă.</li>"
              "<li>Obține URL și stream key din Creator Studio.</li><li>Lipește în SplitCam.</li>"
              "<li>Apasă Go Live.</li></ol>",
     "key_how": "Loghează-te în contul tău de creator ManyVids, deschide <strong>Creator Studio</strong> și mergi la <strong>MV Live → Broadcast Settings → External Encoder</strong>. Pagina dezvăluie un <strong>URL server</strong> și o <strong>stream key</strong> legate de cont — copiază-le în câmpurile RTMP custom ale SplitCam. Conturile de creator trebuie să fie complet verificate (ID + taxe) înainte ca MV Live să fie disponibil.",
     "tips": [
         ("Creator-economy, nu doar live", "ManyVids nu e o platformă cam pură — MV Live e doar o sursă de venit alături de vânzări de clipuri, video-uri custom și abonamente fan club. Folosește stream-urile live pentru a aduce vizitatori spre celelalte forme de monetizare."),
         ("Tipping cu tokeni în MV Live", "MV Live are propriul sistem de tipping cu tokeni în camera live. Planifică meniuri de obiective și reward triggers similar cu Chaturbate / Stripchat — convertesc bine cu audiența existentă ManyVids."),
         ("Browser vs encoder extern", "Broadcasterul integrat în browser din Creator Studio e single-cameră. SplitCam prin External Encoder deblochează scene multi-cameră, overlay-uri și filtre."),
         _T_ETH,
     ],
     "faq": [
         ("Suportă MV Live (ManyVids) encodere externe precum SplitCam?", "Da — secțiunea MV Live din Creator Studio include opțiunea External Encoder sub Broadcast Settings. URL server RTMP standard și stream key; OBS, SplitCam, vMix se conectează."),
         ("Unde îmi iau stream key-ul pentru MV Live?", "Creator Studio → MV Live → Broadcast Settings → External Encoder. Atât URL-ul serverului, cât și stream key-ul apar acolo — copiază ambele în câmpurile RTMP custom ale SplitCam."),
         ("Ce bitrate folosesc pentru MV Live?", "Împinge 1920×1080 la 30 fps, 3.500–6.000 Kbps cu keyframe la 2 secunde. Rulează întâi speed test-ul integrat din SplitCam."),
         ("SplitCam e gratuit pentru MV Live?", "Da — SplitCam e gratuit, fără filigran și fără limită de timp. Opțiunea External Encoder de la ManyVids e gratuită în Creator Studio."),
     ],
     "steps": [
         ("Descarcă și instalează SplitCam", "SplitCam e software gratuit de live-streaming pentru Windows și macOS — fără înregistrare, fără card, fără filigran."),
         ("Construiește scena", "Deschide SplitCam și adaugă webcam-ul. Pune deasupra overlay-uri, text, o a doua cameră sau telefonul, filtre de beauty sau fundal AI — perfect pentru build-uri MV Live cu goal-reveal și reward triggers."),
         ("Obține URL și stream key MV Live", "Loghează-te în contul tău de creator ManyVids, deschide <strong>Creator Studio</strong>, navighează la <strong>MV Live → Broadcast Settings → External Encoder</strong>. Pagina dezvăluie un <strong>URL server</strong> și o <strong>stream key</strong> unică. Copiază ambele."),
         ("Conectează SplitCam la MV Live", "În SplitCam deschide <strong>Stream Settings</strong>, lipește URL-ul serverului MV Live și stream key-ul în câmpurile RTMP custom. Setează bitrate la 3.500–6.000 Kbps la 1920×1080, 30 fps, cu keyframe la 2 secunde."),
         ("Apasă Go Live", "Apasă <strong>Go Live</strong> în SplitCam, apoi pornește transmisia MV Live din Creator Studio. În ~10 secunde stream-ul tău ajunge la audiența MV Live."),
     ],
    },
    {"slug": "fansly", "name": "Fansly",
     "title": "Cum intri live pe Fansly cu SplitCam — encoder extern",
     "desc": "Intră live pe Fansly cu SplitCam gratuit — Creator Dashboard cu encoder extern, scene multi-cameră și overlay-uri. Fără filigran.",
     "kw": "cum transmiți pe fansly, fansly, fansly live, fansly obs, fansly external encoder, fansly rtmp, fansly stream key",
     "h1html": 'Cum transmiți pe <span class="accent">Fansly Live</span> cu SplitCam',
     "h1short": "Transmisie pe Fansly",
     "card": "Setup cu encoder extern pentru Creator Dashboard-ul Fansly.",
     "intro": "Fansly e un competitor direct al OnlyFans, cu reguli de conținut mai relaxate și o bază de creatori în creștere — abonamente, conținut pay-per-view și produsul de live-streaming <strong>Fansly Live</strong>. Broadcasterul implicit merge în browser, dar <strong>Creator Dashboard</strong> expune și o cale standard de <strong>external encoder</strong>, la care se conectează <strong style='color:var(--text)'>SplitCam</strong> gratuit — astfel transmiți cu scene multi-cameră, overlay-uri și filtre către baza ta de abonați.",
     "quick": "Transmisie pe Fansly Live cu SplitCam: instalezi SplitCam, construiești scena, în Creator Dashboard deschizi <em>Live → Broadcast Settings → External Encoder</em>, copiezi URL-ul serverului și stream key-ul, le lipești în SplitCam, Go Live."
              "<ol><li>Instalează SplitCam.</li><li>Adaugă cameră + scenă.</li>"
              "<li>Obține URL și stream key din Creator Dashboard.</li><li>Lipește în SplitCam.</li>"
              "<li>Apasă Go Live.</li></ol>",
     "key_how": "Loghează-te în contul tău de creator Fansly, deschide <strong>Creator Dashboard</strong> și navighează la <strong>Live → Broadcast Settings → External Encoder</strong>. Pagina dezvăluie un <strong>URL server</strong> și o <strong>stream key</strong> legate de cont — copiază-le în câmpurile RTMP custom ale SplitCam. Conturile de creator au nevoie de verificare ID înainte ca Fansly Live să fie activat.",
     "tips": [
         ("Audiență subscriber-first", "Audiența Fansly e bazată pe abonament — stream-ul tău live ajunge la oameni care deja te plătesc lunar. Planifică conținut care răsplătește loialitatea (Q&amp;A exclusiv, behind-the-scenes, obiective de tip custom) în loc să vânezi metrici din camere publice."),
         ("Tip-uri alături de abonamente", "Fansly Live suportă tipping în stream în plus față de abonamentele de bază. Venitul combinat poate depăși tipping-ul de pe platformele cam pure pentru creatorii consacrați."),
         ("Browser broadcaster vs extern", "Broadcasterul implicit din browser e single-source. SplitCam prin External Encoder deblochează multi-cameră, overlay-uri, beauty filters și fundal AI care se ridică la nivelul conținutului premium pentru abonați."),
         _T_ETH,
     ],
     "faq": [
         ("Suportă Fansly Live encodere externe precum SplitCam?", "Da — secțiunea Live din Creator Dashboard include opțiunea External Encoder sub Broadcast Settings. URL server RTMP standard și stream key; OBS, SplitCam, vMix se conectează."),
         ("Unde îmi iau stream key-ul pentru Fansly?", "Creator Dashboard → Live → Broadcast Settings → External Encoder. Atât URL-ul serverului, cât și stream key-ul apar acolo. Copiază ambele în câmpurile RTMP custom ale SplitCam."),
         ("Ce bitrate folosesc pentru Fansly Live?", "Împinge 1920×1080 la 30 fps, 3.500–6.000 Kbps cu keyframe la 2 secunde. Rulează întâi speed test-ul integrat din SplitCam."),
         ("SplitCam e gratuit pentru Fansly?", "Da — SplitCam e gratuit, fără filigran și fără limită de timp. Opțiunea External Encoder de la Fansly e gratuită în Creator Dashboard."),
     ],
     "steps": [
         ("Descarcă și instalează SplitCam", "SplitCam e software gratuit de live-streaming pentru Windows și macOS — fără înregistrare, fără card, fără filigran."),
         ("Construiește scena", "Deschide SplitCam și adaugă webcam-ul. Pune deasupra overlay-uri, text, o a doua cameră sau telefonul, filtre de beauty sau un fundal AI — scene îngrijite care se potrivesc cu așteptările premium ale abonaților."),
         ("Obține URL și stream key Fansly", "Loghează-te în contul tău de creator Fansly, deschide <strong>Creator Dashboard</strong>, navighează la <strong>Live → Broadcast Settings → External Encoder</strong>. Pagina dezvăluie un <strong>URL server</strong> și o <strong>stream key</strong> unică. Copiază ambele."),
         ("Conectează SplitCam la Fansly", "În SplitCam deschide <strong>Stream Settings</strong>, lipește URL-ul serverului Fansly și stream key-ul în câmpurile RTMP custom. Setează bitrate la 3.500–6.000 Kbps la 1920×1080, 30 fps, cu keyframe la 2 secunde."),
         ("Apasă Go Live", "Apasă <strong>Go Live</strong> în SplitCam, apoi pornește transmisia Fansly Live din Creator Dashboard. În ~10 secunde stream-ul tău ajunge la abonații Fansly."),
     ],
    },
    {"slug": "ifriends", "name": "iFriends",
     "title": "Cum transmiți pe iFriends cu SplitCam — encoder extern",
     "desc": "Transmite pe iFriends cu SplitCam gratuit — Model Center cu encoder extern, scene multi-cameră și overlay-uri. Fără filigran.",
     "kw": "cum transmiți pe ifriends, ifriends, ifriends broadcast, ifriends obs, ifriends external encoder, ifriends rtmp, ifriends stream key",
     "h1html": 'Cum transmiți pe <span class="accent">iFriends</span> cu SplitCam',
     "h1short": "Transmisie pe iFriends",
     "card": "Setup cu encoder extern pentru Model Center-ul matur al iFriends.",
     "intro": "iFriends (WebPower) e una dintre cele mai longevive rețele cam independente — discret profitabilă, cu o bază loială de utilizatori și un Model Center matur, construit înainte ca broadcasterele de browser să devină comune. Platforma suportă o cale standard de <strong>external encoder</strong> din Model Center la care se conectează <strong style='color:var(--text)'>SplitCam</strong> gratuit — astfel transmiți cu scene multi-cameră moderne, overlay-uri și filtre pe această rețea consacrată.",
     "quick": "Transmisie pe iFriends cu SplitCam: instalezi SplitCam, construiești scena, în Model Center deschizi <em>Broadcast Settings → External Encoder</em>, copiezi URL-ul serverului și stream key-ul, le lipești în SplitCam, Go Live."
              "<ol><li>Instalează SplitCam.</li><li>Adaugă cameră + scenă.</li>"
              "<li>Obține URL și stream key din Model Center.</li><li>Lipește în SplitCam.</li>"
              "<li>Apasă Go Live.</li></ol>",
     "key_how": "Loghează-te în contul tău de model iFriends, deschide <strong>Model Center</strong> și navighează la <strong>Broadcast Settings → External Encoder</strong>. Pagina dezvăluie un <strong>URL server</strong> și o <strong>stream key</strong> legate de cont — copiază-le în câmpurile RTMP custom ale SplitCam. Aprobarea iFriends pentru conturile noi de model e riguroasă, dar legitimă; odată verificat, opțiunea External Encoder rămâne disponibilă pe termen nelimitat.",
     "tips": [
         ("Audiență long-tail, rețea matură", "iFriends funcționează de la sfârșitul anilor '90, cu o bază loială de utilizatori — mulți sunt abonați pe termen lung, nu vizitatori la prima vizită. Venit stabil pentru modele consacrate, creștere mai lentă pentru începători."),
         ("Browser broadcaster vs encoder extern", "Broadcasterul vechi din iFriends a fost construit înainte de UX-ul modern multi-cameră. Trecerea la SplitCam prin External Encoder e un upgrade vizibil — scene multi-cameră, overlay-uri și beauty filters pe care tool-ul vechi nu le poate livra."),
         ("Plăți constante, mai puține surprize", "Compania-mamă a iFriends (WebPower) plătește modelele constant de decenii — programe de plată mai lente decât platformele noi crypto-friendly, dar foarte puține istorii de groază."),
         _T_ETH,
     ],
     "faq": [
         ("iFriends suportă oficial encodere externe precum SplitCam?", "Da — Model Center include o opțiune External Encoder sub Broadcast Settings. URL server RTMP standard și stream key; OBS, SplitCam, vMix se conectează odată ce contul tău e aprobat."),
         ("Unde îmi iau stream key-ul iFriends?", "Model Center → Broadcast Settings → External Encoder. Atât URL-ul serverului, cât și stream key-ul apar acolo — copiază ambele în câmpurile RTMP custom ale SplitCam."),
         ("Ce bitrate folosesc pentru iFriends?", "Împinge 1920×1080 la 30 fps, 3.500–6.000 Kbps cu keyframe la 2 secunde. Rulează întâi speed test-ul integrat din SplitCam."),
         ("SplitCam e gratuit pentru iFriends?", "Da — SplitCam e gratuit, fără filigran și fără limită de timp. Opțiunea External Encoder de la iFriends e gratuită în Model Center."),
     ],
     "steps": [
         ("Descarcă și instalează SplitCam", "SplitCam e software gratuit de live-streaming pentru Windows și macOS — fără înregistrare, fără card, fără filigran."),
         ("Construiește scena", "Deschide SplitCam și adaugă webcam-ul. Pune deasupra overlay-uri, text, o a doua cameră sau telefonul, filtre de beauty sau fundal AI — scenele moderne și îngrijite ies în evidență pe această rețea matură."),
         ("Obține URL și stream key iFriends", "Loghează-te în contul tău de model iFriends, deschide <strong>Model Center</strong>, navighează la <strong>Broadcast Settings → External Encoder</strong>. Pagina dezvăluie un <strong>URL server</strong> și o <strong>stream key</strong> unică. Copiază ambele."),
         ("Conectează SplitCam la iFriends", "În SplitCam deschide <strong>Stream Settings</strong>, lipește URL-ul serverului iFriends și stream key-ul în câmpurile RTMP custom. Setează bitrate la 3.500–6.000 Kbps la 1920×1080, 30 fps, cu keyframe la 2 secunde."),
         ("Apasă Go Live", "Apasă <strong>Go Live</strong> în SplitCam, apoi treci online din Model Center-ul iFriends. În ~10 secunde stream-ul tău ajunge în rețea."),
     ],
    },
    {"slug": "babestation", "name": "Babestation",
     "title": "Cum transmiți pe Babestation cu SplitCam — encoder extern",
     "desc": "Transmite pe Babestation cu SplitCam gratuit — Performer Hub cu encoder extern, scene multi-cameră și overlay-uri. Fără filigran.",
     "kw": "cum transmiți pe babestation, babestation, babestation broadcast, babestation obs, babestation external encoder, babestation rtmp, babestation stream key",
     "h1html": 'Cum transmiți pe <span class="accent">Babestation</span> cu SplitCam',
     "h1short": "Transmisie pe Babestation",
     "card": "Setup cu encoder extern pentru Performer Hub-ul UK de la Babestation.",
     "intro": "Babestation e principala rețea UK de adult TV / cam — un hibrid între canale TV broadcast și un produs cam live alimentat de performerii logați în Performer Hub. Platforma suportă o cale standard de <strong>external encoder</strong> din Performer Hub, la care se conectează <strong style='color:var(--text)'>SplitCam</strong> gratuit — astfel performerii UK independenți transmit cu scene multi-cameră, overlay-uri și beauty filters care depășesc broadcasterul implicit, de tip studio TV.",
     "quick": "Transmisie pe Babestation cu SplitCam: instalezi SplitCam, construiești scena, în Performer Hub deschizi <em>Broadcast Settings → External Encoder</em>, copiezi URL-ul serverului și stream key-ul, le lipești în SplitCam, Go Live."
              "<ol><li>Instalează SplitCam.</li><li>Adaugă cameră + scenă.</li>"
              "<li>Obține URL și stream key din Performer Hub.</li><li>Lipește în SplitCam.</li>"
              "<li>Apasă Go Live.</li></ol>",
     "key_how": "Loghează-te în contul tău de performer Babestation, deschide <strong>Performer Hub</strong> și navighează la <strong>Broadcast Settings → External Encoder</strong>. Pagina dezvăluie un <strong>URL server</strong> și o <strong>stream key</strong> legate de cont — copiază-le în câmpurile RTMP custom ale SplitCam. Onboarding-ul Babestation pentru performerii UK include verificarea ID-ului conform reglementărilor britanice de verificare a vârstei.",
     "tips": [
         ("Audiență UK-first și timing", "Traficul de vârf al Babestation e seara / noaptea UK (GMT/BST). Dacă ești în alt fus orar, transmisia târziu în noaptea UK depășește semnificativ timingul de prime-time local pe această rețea."),
         ("Se așteaptă polish de studio TV", "Brandul Babestation e legat de canalele sale TV — privitorii se așteaptă la seturi și iluminat mai produse decât un stream webcam tipic. Scenele SplitCam (overlay-uri, text branduit, fundal AI) ajută să te aliniezi cu estetica polish a platformei."),
         ("Performeri independenți vs studio", "Babestation lucrează atât cu studiouri UK, cât și cu performeri independenți. Broadcasterii independenți conectați prin External Encoder primesc același model de payout ca și camerele alimentate de studio."),
         _T_ETH,
     ],
     "faq": [
         ("Babestation suportă encodere externe precum SplitCam?", "Da — Performer Hub include o opțiune External Encoder sub Broadcast Settings. URL server RTMP standard și stream key; OBS, SplitCam, vMix se conectează după ce verificarea performerului e completă."),
         ("Unde îmi iau stream key-ul Babestation?", "Performer Hub → Broadcast Settings → External Encoder. Atât URL-ul serverului, cât și stream key-ul apar acolo — copiază ambele în câmpurile RTMP custom ale SplitCam."),
         ("Ce bitrate folosesc pentru Babestation?", "Împinge 1920×1080 la 30 fps, 3.500–6.000 Kbps cu keyframe la 2 secunde. Banda de upload din UK e în general bună, dar rulează întâi speed test-ul din SplitCam."),
         ("SplitCam e gratuit pentru Babestation?", "Da — SplitCam e gratuit, fără filigran și fără limită de timp. Opțiunea External Encoder de la Babestation e gratuită în Performer Hub."),
     ],
     "steps": [
         ("Descarcă și instalează SplitCam", "SplitCam e software gratuit de live-streaming pentru Windows și macOS — fără înregistrare, fără card, fără filigran."),
         ("Construiește scena", "Deschide SplitCam și adaugă webcam-ul. Pune deasupra overlay-uri, text, o a doua cameră sau telefonul, filtre de beauty sau un fundal AI — aliniază-te cu polish-ul de producție de studio TV al Babestation ca să ieși în evidență."),
         ("Obține URL și stream key Babestation", "Loghează-te în contul tău de performer Babestation, deschide <strong>Performer Hub</strong>, navighează la <strong>Broadcast Settings → External Encoder</strong>. Pagina dezvăluie un <strong>URL server</strong> și o <strong>stream key</strong> unică. Copiază ambele."),
         ("Conectează SplitCam la Babestation", "În SplitCam deschide <strong>Stream Settings</strong>, lipește URL-ul serverului Babestation și stream key-ul în câmpurile RTMP custom. Setează bitrate la 3.500–6.000 Kbps la 1920×1080, 30 fps, cu keyframe la 2 secunde."),
         ("Apasă Go Live", "Apasă <strong>Go Live</strong> în SplitCam, apoi treci online din Performer Hub. În ~10 secunde stream-ul tău ajunge la audiența UK a Babestation."),
     ],
    },
    {"slug": "adultwork", "name": "AdultWork",
     "title": "Cum transmiți pe AdultWork cu SplitCam — encoder extern",
     "desc": "Transmite pe AdultWork cu SplitCam gratuit — Members Area cu encoder extern, scene multi-cameră și overlay-uri. Fără filigran.",
     "kw": "cum transmiți pe adultwork, adultwork, adultwork broadcast, adultwork obs, adultwork external encoder, adultwork rtmp, adultwork stream key",
     "h1html": 'Cum transmiți pe <span class="accent">AdultWork</span> cu SplitCam',
     "h1short": "Transmisie pe AdultWork",
     "card": "Setup cu encoder extern pentru funcția cam din Members Area UK al AdultWork.",
     "intro": "AdultWork e marketplace-ul UK consacrat pentru servicii adult — cunoscut în principal pentru rezervări de escortă, vânzări de foto / video și servicii telefonice, cu o funcție <strong>webcam</strong> live alături. Platforma suportă o cale standard de <strong>external encoder</strong> din Members Area, la care se conectează <strong style='color:var(--text)'>SplitCam</strong> gratuit — astfel performerii UK independenți adaugă venit din cam live cu scene multi-cameră, overlay-uri și filtre.",
     "quick": "Transmisie pe AdultWork cu SplitCam: instalezi SplitCam, construiești scena, în Members Area deschizi <em>Members → Broadcasting → External Encoder</em>, copiezi URL-ul serverului și stream key-ul, le lipești în SplitCam, Go Live."
              "<ol><li>Instalează SplitCam.</li><li>Adaugă cameră + scenă.</li>"
              "<li>Obține URL și stream key din Members Area.</li><li>Lipește în SplitCam.</li>"
              "<li>Apasă Go Live.</li></ol>",
     "key_how": "Loghează-te în contul tău de performer AdultWork, deschide <strong>Members Area</strong> și navighează la <strong>Members → Broadcasting → External Encoder</strong>. Pagina dezvăluie un <strong>URL server</strong> și o <strong>stream key</strong> legate de cont — copiază-le în câmpurile RTMP custom ale SplitCam. Verificarea AdultWork e obligatorie pentru funcția cam live și acoperă conformitatea cu regulile UK de verificare a vârstei.",
     "tips": [
         ("Cross-sell din celelalte servicii AdultWork", "Forța AdultWork e baza existentă de clienți — privitorii pot deja să-ți rezerve serviciile de foto / video / telefon. Folosește stream-urile live ca să faci cross-sell către clienții care încă n-au încercat cam-ul tău, nu ca să vânezi străini."),
         ("Members Area e punctul de intrare", "Nu căuta broadcasterul pe site-ul public — totul pentru performer e în Members Area. Setări de broadcasting, payouts, gestionarea conținutului — toate stau acolo."),
         ("UK-centric, dar payouts internaționale", "Cel mai mult trafic e UK/EU. Payouts funcționează internațional prin transfer bancar standard / e-wallet, cu programe săptămânale comune pe platformă."),
         _T_ETH,
     ],
     "faq": [
         ("AdultWork suportă encodere externe precum SplitCam?", "Da — Members Area include o opțiune External Encoder sub Broadcasting. URL server RTMP standard și stream key; OBS, SplitCam, vMix se conectează după verificarea performerului."),
         ("Unde îmi iau stream key-ul AdultWork?", "Members Area → Members → Broadcasting → External Encoder. Atât URL-ul serverului, cât și stream key-ul apar acolo — copiază ambele în câmpurile RTMP custom ale SplitCam."),
         ("Ce bitrate folosesc pentru AdultWork?", "Împinge 1920×1080 la 30 fps, 3.500–6.000 Kbps cu keyframe la 2 secunde. Rulează întâi speed test-ul integrat din SplitCam."),
         ("SplitCam e gratuit pentru AdultWork?", "Da — SplitCam e gratuit, fără filigran și fără limită de timp. Opțiunea External Encoder de la AdultWork e gratuită în Members Area."),
     ],
     "steps": [
         ("Descarcă și instalează SplitCam", "SplitCam e software gratuit de live-streaming pentru Windows și macOS — fără înregistrare, fără card, fără filigran."),
         ("Construiește scena", "Deschide SplitCam și adaugă webcam-ul. Pune deasupra overlay-uri, text, o a doua cameră sau telefonul, filtre de beauty sau fundal AI — folosește overlay-urile ca să-ți promovezi conținutul AdultWork / serviciile telefonice și să faci cross-sell în timpul live-ului."),
         ("Obține URL și stream key AdultWork", "Loghează-te în contul tău de performer AdultWork, deschide <strong>Members Area</strong>, navighează la <strong>Members → Broadcasting → External Encoder</strong>. Pagina dezvăluie un <strong>URL server</strong> și o <strong>stream key</strong> unică. Copiază ambele."),
         ("Conectează SplitCam la AdultWork", "În SplitCam deschide <strong>Stream Settings</strong>, lipește URL-ul serverului AdultWork și stream key-ul în câmpurile RTMP custom. Setează bitrate la 3.500–6.000 Kbps la 1920×1080, 30 fps, cu keyframe la 2 secunde."),
         ("Apasă Go Live", "Apasă <strong>Go Live</strong> în SplitCam, apoi treci online din Members Area. În ~10 secunde stream-ul tău ajunge la audiența AdultWork."),
     ],
    },
    {
        "slug": "jerkmate", "name": "Jerkmate",
        "title": "Cum transmiți pe Jerkmate cu SplitCam — prin Streamate",
        "desc": "Transmite pe Jerkmate cu SplitCam gratuit — Jerkmate își ia modelele din Streamate, deci transmiți prin SM Connect, cu scene și overlay-uri. Fără filigran.",
        "kw": "cum transmiți pe jerkmate, jerkmate, jerkmate broadcast, jerkmate streamate, jerkmate sm connect, jerkmate obs, jerkmate stream key",
        "h1html": 'Cum transmiți pe <span class="accent">Jerkmate</span> cu SplitCam',
        "h1short": "Transmisie pe Jerkmate",
        "card": "Jerkmate își ia modelele din rețeaua Streamate — transmiți prin SM Connect + SplitCam.",
        "intro": "Jerkmate e unul dintre cele mai căutate branduri cam, cunoscut pentru AI-ul care îmbină privitorii cu performeri live. Nu are broadcaster propriu — Jerkmate <strong>își ia modelele live din rețeaua Streamate</strong>. Transmiți ca model în rețeaua Streamate, iar show-ul tău e distribuit pe Jerkmate și pe site-urile partenere. Pentru că Streamate e <strong style='color:var(--text)'>preconfigurat în lista de canale</strong> a SplitCam, <strong style='color:var(--text)'>SplitCam</strong> gratuit îți lasă să adaugi scene multi-cameră, overlay-uri și filtre fără să introduci manual vreun URL RTMP.",
        "quick": "Transmisie pe Jerkmate cu SplitCam: instalezi SplitCam, construiești scena, te înscrii ca model în rețeaua Streamate care alimentează Jerkmate, deschizi <em>SM Connect → Start Show</em> și copiezi cheia, apoi în SplitCam deschizi <em>Stream Settings → Add Channel → Streamate</em>, o lipești și apeși Go Live."
                 "<ol><li>Instalează SplitCam.</li><li>Adaugă cameră + scenă.</li>"
                 "<li>Înscrie-te ca model în rețeaua Streamate.</li>"
                 "<li>Ia cheia prin SM Connect.</li>"
                 "<li>Add Channel → Streamate, Go Live.</li></ol>",
        "key_how": "Camerele live de pe Jerkmate vin din <strong>rețeaua de broadcasting Streamate</strong> — nu există un \"Jerkmate encoder\" separat. Înregistrează-te prin programul de modele Jerkmate sau direct în rețeaua Streamate, deschide <strong>SM Connect</strong>, acceptă termenii, clic <strong>Start Show</strong> și copiază streaming key-ul. În SplitCam deschide <strong>Stream Settings → Add Channel</strong>, alegi <strong>Streamate</strong> din lista integrată și lipești cheia. Stream-ul tău ajunge atunci simultan pe Jerkmate și pe site-urile partenere ale rețelei.",
        "tips": [
            ("Sub capotă e rețeaua Streamate", "Nu căuta un broadcaster specific Jerkmate — transmiți pe Streamate, iar Jerkmate redistribuie. Orice merge pentru Streamate (SM Connect, canalul integrat din SplitCam) merge și pentru Jerkmate."),
            ("Convertește traficul potrivit de AI", "AI-ul matchmaker al Jerkmate trimite privitorii către modelele care le corespund preferințelor — o scenă SplitCam îngrijită, cu overlay-uri și o încadrare bună, convertește acei privitori potriviți mult mai bine decât o webcam plată."),
            ("Un singur flux, mai multe site-uri", "Transmisia către rețeaua Streamate te pune simultan pe Jerkmate și pe site-urile sale partenere — acoperire mai largă dintr-un singur stream SplitCam, fără setup în plus."),
            _T_ETH,
        ],
        "faq": [
            ("Are Jerkmate broadcaster propriu sau stream key?", "Nu — Jerkmate își ia modelele live din rețeaua Streamate. Transmiți ca model în rețeaua Streamate prin SM Connect, iar show-ul tău apare automat pe Jerkmate."),
            ("Cum îmi iau stream key-ul pentru Jerkmate?", "Prin SM Connect, pe partea de model din rețeaua Streamate: acceptă termenii → Start Show → copiază cheia. O lipești în canalul Streamate integrat din SplitCam — fără URL RTMP manual."),
            ("Ce bitrate folosesc pentru Jerkmate?", "Fixează 1080p la 30 fps. Fluxul rețelei e adaptiv, deci un bitrate mai mic pe o imagine statică e normal. Rulează speed test-ul din SplitCam și folosește conexiune prin cablu."),
            ("SplitCam e gratuit pentru Jerkmate?", "Da — SplitCam e gratuit, fără filigran și fără limită de timp. Streamate (care alimentează Jerkmate) e un canal integrat în SplitCam, deci nu există un cost separat de encoder."),
        ],
        "steps": [
            ("Descarcă și instalează SplitCam", "SplitCam e software gratuit de live-streaming pentru Windows și macOS — fără înregistrare, fără card, fără filigran."),
            ("Construiește scena", "Deschide SplitCam și adaugă webcam-ul. Pune deasupra overlay-uri, text, o a doua cameră sau telefonul, filtre de beauty sau un fundal AI — o scenă puternică convertește privitorii potriviți de AI ai Jerkmate."),
            ("Înscrie-te ca model și ia-ți cheia", "Înregistrează-te prin programul de modele Jerkmate sau direct în <strong>rețeaua Streamate</strong> care îl alimentează. Deschide <strong>SM Connect</strong>, acceptă termenii, clic <strong>Start Show</strong> și copiază streaming key-ul."),
            ("Adaugă Streamate ca un canal în SplitCam", "Deschide <strong>Stream Settings → Add Channel</strong>, alegi <strong>Streamate</strong> din lista integrată și lipești cheia — fără URL RTMP manual. Fixează rezoluția la 1080p."),
            ("Apasă Go Live", "Apasă <strong>Go Live</strong> în SplitCam — un slider verde confirmă conexiunea. Show-ul tău iese în rețeaua Streamate și apare pe Jerkmate."),
        ],
    },
    {
        "slug": "justforfans", "name": "JustForFans",
        "title": "Cum intri live pe JustForFans cu SplitCam — cameră virtuală",
        "desc": "Intră live pe JustForFans cu SplitCam gratuit — cameră virtuală în broadcasterul JFF, scene multi-cameră și overlay-uri. Fără filigran.",
        "kw": "cum transmiți pe justforfans, justforfans, justforfans live, justforfans obs, justforfans virtual camera, justforfans external encoder, justforfans broadcast",
        "h1html": 'Cum intri live pe <span class="accent">JustForFans</span> cu SplitCam',
        "h1short": "Live pe JustForFans",
        "card": "Folosește SplitCam ca o cameră virtuală în broadcasterul live al JustForFans.",
        "intro": "JustForFans (JFF) e o platformă de abonamente deținută de creatori — o alternativă longevivă la OnlyFans, fondată de performeri, cu abonamente, conținut pay-per-view și o funcție live în browser. Broadcasterul ei live arată o singură webcam simplă; îndreptat spre <strong style='color:var(--text)'>SplitCam</strong> gratuit ca o <strong>cameră virtuală</strong>, deblochează scene multi-cameră, overlay-uri și filtre. Dacă în Creator Dashboard ai și o opțiune de external encoder / stream key, SplitCam se conectează în schimb prin RTMP.",
        "quick": "Intră live pe JustForFans cu SplitCam: instalezi SplitCam, construiești scena, pornești o transmisie live pe JFF, iar în selectorul de cameră al broadcasterului alegi <em>SplitCam</em> ca webcam — apoi intri live."
                 "<ol><li>Instalează SplitCam.</li><li>Adaugă cameră + scenă.</li>"
                 "<li>Pornește o transmisie live pe JFF.</li>"
                 "<li>Alege SplitCam din lista de camere.</li>"
                 "<li>Apasă Go Live.</li></ol>",
        "key_how": "Live-ul JustForFans merge în browser. Construiește scena în SplitCam — apare ca o webcam de sistem numită <strong>\"SplitCam Video Driver\"</strong> — apoi deschide broadcasterul live JFF și, în lista de camere, alege <strong>SplitCam</strong> în loc de webcam-ul tău brut. Scena ta compusă înlocuiește camera plată. Dacă în Creator Dashboard-ul JFF apare o opțiune de <strong>external encoder / stream key</strong>, lipești în schimb cheia în câmpurile RTMP custom ale SplitCam.",
        "tips": [
            ("Camera virtuală merge peste tot", "Chiar și când live-ul unei platforme e doar în browser, SplitCam apare ca o webcam selectabilă — așa că scena ta multi-cameră, overlay-urile și filtrele merg pe JFF fără nicio stream key."),
            ("Deținută de creatori, prietenoasă cu performerii", "JFF e condusă de performeri și păstrează o bază loială de abonați. Overlay-urile care fac cross-sell la PPV sau abonamentul tău convertesc bine la o audiență care deja plătește."),
            ("Dă browserului permisiunea de cameră", "Dacă SplitCam nu apare în lista de camere a JFF, asigură-te mai întâi că SplitCam rulează și că browserul are permisiunea de cameră — apoi reîncarcă broadcasterul."),
            _T_TEST,
        ],
        "faq": [
            ("Cum se conectează SplitCam la JustForFans?", "Live-ul JFF e în browser, deci SplitCam se conectează ca o cameră virtuală: alegi SplitCam în selectorul de cameră al broadcasterului JFF. Nu e nevoie de stream key."),
            ("Pot folosi overlay-uri și mai multe camere pe JFF?", "Da — construiești scena în SplitCam (a doua cameră, overlay-uri, filtre de beauty sau fundal AI), iar JFF vede scena finită ca o singură webcam."),
            ("JustForFans suportă OBS sau encodere externe?", "Live-ul JFF e în primul rând bazat pe browser / webcam. Dacă în Creator Dashboard apare o opțiune de external encoder sau stream key, o lipești în câmpurile RTMP custom ale SplitCam; altfel folosești metoda cu camera virtuală."),
            ("SplitCam e gratuit pentru JustForFans?", "Da — SplitCam e gratuit, fără filigran și fără limită de timp."),
        ],
        "steps": [
            ("Descarcă și instalează SplitCam", "SplitCam e software gratuit de live-streaming pentru Windows și macOS — fără înregistrare, fără card, fără filigran. Instalează o cameră virtuală pe care browserul o poate selecta."),
            ("Construiește scena", "Deschide SplitCam și adaugă webcam-ul. Pune deasupra overlay-uri, text, o a doua cameră sau telefonul, filtre de beauty sau un fundal AI — totul aplicat live."),
            ("Pornește o transmisie live pe JFF", "Loghează-te în contul tău de creator JustForFans și deschide broadcasterul live pentru a porni un stream pentru abonații tăi."),
            ("Alege SplitCam ca cameră", "În lista de camere a broadcasterului JFF, alegi <strong>SplitCam</strong> în loc de webcam-ul tău brut — scena ta compusă înlocuiește camera plată. (Sau, dacă e disponibilă, lipești cheia de external encoder a JFF în câmpurile RTMP custom ale SplitCam.)"),
            ("Apasă Go Live", "Pornește transmisia — scena ta SplitCam, overlay-urile și filtrele ajung la abonații tăi de pe JustForFans."),
        ],
    },
    {
        "slug": "fanvue", "name": "Fanvue",
        "title": "Cum intri live pe Fanvue cu SplitCam — cameră virtuală",
        "desc": "Intră live pe Fanvue cu SplitCam gratuit ca o cameră virtuală — scene multi-cameră, overlay-uri și filtre pentru abonații tăi. Fără filigran, fără cont.",
        "kw": "cum intri live pe fanvue, fanvue, fanvue live, fanvue obs, fanvue cameră virtuală, fanvue creator, fanvue broadcast",
        "h1html": 'Cum intri live pe <span class="accent">Fanvue</span> cu SplitCam',
        "h1short": "Live pe Fanvue",
        "card": "Folosește SplitCam ca o cameră virtuală pentru live-ul de pe Fanvue.",
        "intro": "Fanvue e o platformă de abonamente deținută de creatori, cu creștere rapidă în UK — o alternativă la OnlyFans, cunoscută ca prietenoasă cu creatorii și cu AI-ul, cu abonamente, pay-per-view și transmisie live. Broadcasterul ei live merge în browser, așa că îndreptat spre <strong style='color:var(--text)'>SplitCam</strong> gratuit ca o <strong>cameră virtuală</strong> deblochează scene multi-cameră, overlay-uri și filtre. Dacă în Creator Dashboard ai și o opțiune de external encoder / stream key, SplitCam se conectează în schimb prin RTMP.",
        "quick": "Intră live pe Fanvue cu SplitCam: instalezi SplitCam, construiești scena, pornești o transmisie live pe Fanvue, iar în selectorul de cameră al broadcasterului alegi <em>SplitCam</em> — apoi intri live."
                 "<ol><li>Instalează SplitCam.</li><li>Adaugă cameră + scenă.</li>"
                 "<li>Pornește o transmisie live pe Fanvue.</li>"
                 "<li>Alege SplitCam din lista de camere.</li>"
                 "<li>Apasă Go Live.</li></ol>",
        "key_how": "Live-ul Fanvue merge în browser. Construiește scena în SplitCam — apare ca o webcam de sistem numită <strong>\"SplitCam Video Driver\"</strong> — apoi deschide broadcasterul live Fanvue și, în lista de camere, alege <strong>SplitCam</strong> în loc de webcam-ul tău brut. Dacă în Creator Dashboard apare o opțiune de <strong>external encoder / stream key</strong>, lipești în schimb cheia în câmpurile RTMP custom ale SplitCam.",
        "tips": [
            ("Camera virtuală merge peste tot", "Chiar și când live-ul unei platforme e doar în browser, SplitCam apare ca o webcam selectabilă — așa că scena ta multi-cameră, overlay-urile și filtrele merg pe Fanvue fără nicio stream key."),
            ("Prietenoasă cu creatorii și cu AI-ul", "Fanvue primește bine creatorii AI și plătește curat. Overlay-urile care fac cross-sell la abonamentul sau PPV-ul tău convertesc bine la o audiență care deja plătește."),
            ("Dă browserului permisiunea de cameră", "Dacă SplitCam nu apare în lista de camere a Fanvue, asigură-te mai întâi că SplitCam rulează și că browserul are permisiunea de cameră — apoi reîncarcă pagina."),
            _T_TEST,
        ],
        "faq": [
            ("Cum se conectează SplitCam la Fanvue?", "Live-ul Fanvue e în browser, deci SplitCam se conectează ca o cameră virtuală: alegi SplitCam în selectorul de cameră. Nu e nevoie de stream key."),
            ("Pot folosi overlay-uri și mai multe camere pe Fanvue?", "Da — construiești scena în SplitCam (a doua cameră, overlay-uri, filtre de beauty sau fundal AI), iar Fanvue vede scena finită ca o singură webcam."),
            ("Fanvue suportă OBS sau encodere externe?", "Live-ul Fanvue e în primul rând bazat pe browser / webcam. Dacă în dashboard apare o opțiune de external encoder sau stream key, o lipești în câmpurile RTMP custom ale SplitCam; altfel folosești metoda cu camera virtuală."),
            ("SplitCam e gratuit pentru Fanvue?", "Da — SplitCam e gratuit, fără filigran și fără limită de timp."),
        ],
        "steps": [
            ("Descarcă și instalează SplitCam", "SplitCam e software gratuit de live-streaming pentru Windows și macOS — fără înregistrare, fără card, fără filigran. Instalează o cameră virtuală pe care browserul o poate selecta."),
            ("Construiește scena", "Deschide SplitCam și adaugă webcam-ul. Pune deasupra overlay-uri, text, o a doua cameră sau telefonul, filtre de beauty sau un fundal AI — totul aplicat live."),
            ("Pornește o transmisie live pe Fanvue", "Loghează-te în contul tău de creator Fanvue și deschide broadcasterul live pentru a porni un stream pentru abonații tăi."),
            ("Alege SplitCam ca cameră", "În lista de camere a broadcasterului Fanvue, alegi <strong>SplitCam</strong> în loc de webcam-ul tău brut — scena ta compusă înlocuiește camera plată. (Sau, dacă e disponibilă, lipești cheia de external encoder în câmpurile RTMP custom ale SplitCam.)"),
            ("Apasă Go Live", "Pornește transmisia — scena ta SplitCam, overlay-urile și filtrele ajung la abonații tăi de pe Fanvue."),
        ],
    },
    {
        "slug": "loyalfans", "name": "LoyalFans",
        "title": "Cum intri live pe LoyalFans cu SplitCam — cameră virtuală",
        "desc": "Intră live pe LoyalFans cu SplitCam gratuit ca o cameră virtuală — scene multi-cameră, overlay-uri și filtre pentru abonați și tipperi. Fără filigran.",
        "kw": "cum intri live pe loyalfans, loyalfans, loyalfans live, loyalfans obs, loyalfans cameră virtuală, loyalfans broadcast, loyal fans",
        "h1html": 'Cum intri live pe <span class="accent">LoyalFans</span> cu SplitCam',
        "h1short": "Live pe LoyalFans",
        "card": "Folosește SplitCam ca o cameră virtuală pentru live-ul de pe LoyalFans.",
        "intro": "LoyalFans e o platformă de abonamente deținută de creatori, cu abonamente, pay-per-view, tipping și o funcție <strong>live cam</strong> integrată. Broadcasterul live merge în browser, așa că prin conectarea <strong style='color:var(--text)'>SplitCam</strong> gratuit ca o <strong>cameră virtuală</strong> adaugi scene multi-cameră, overlay-uri și filtre peste webcam-ul standard. Dacă în dashboard ai și o opțiune de external encoder / stream key, SplitCam se conectează în schimb prin RTMP.",
        "quick": "Intră live pe LoyalFans cu SplitCam: instalezi SplitCam, construiești scena, pornești o transmisie live pe LoyalFans, iar în selectorul de cameră al broadcasterului alegi <em>SplitCam</em> — apoi intri live."
                 "<ol><li>Instalează SplitCam.</li><li>Adaugă cameră + scenă.</li>"
                 "<li>Pornește o transmisie live pe LoyalFans.</li>"
                 "<li>Alege SplitCam din lista de camere.</li>"
                 "<li>Apasă Go Live.</li></ol>",
        "key_how": "Live-ul LoyalFans merge în browser. Construiește scena în SplitCam — apare ca o webcam de sistem numită <strong>\"SplitCam Video Driver\"</strong> — apoi deschide broadcasterul live LoyalFans și, în lista de camere, alege <strong>SplitCam</strong>. Dacă în Creator Dashboard apare o opțiune de <strong>stream key / external encoder</strong>, lipești în schimb cheia în câmpurile RTMP custom ale SplitCam.",
        "tips": [
            ("Cameră virtuală, fără cheie", "Live-ul în browser primește tot scena ta SplitCam — overlay-uri, a doua cameră și filtre — doar selectând SplitCam ca webcam."),
            ("Tip-urile răsplătesc producția", "LoyalFans se sprijină pe tipping; overlay-urile cu tip-goal pe ecran și o scenă îngrijită împing tipperii mai mult decât o webcam plată."),
            ("Dă browserului permisiunea de cameră", "Dacă SplitCam nu e în lista de camere a LoyalFans, pornește mai întâi SplitCam, permite accesul la cameră în browser, apoi reîncarcă broadcasterul."),
            _T_TEST,
        ],
        "faq": [
            ("Cum se conectează SplitCam la LoyalFans?", "Live-ul LoyalFans e în browser, deci SplitCam se conectează ca o cameră virtuală — alegi SplitCam în selectorul de cameră. Nu e nevoie de stream key."),
            ("Pot folosi overlay-uri și mai multe camere pe LoyalFans?", "Da — compui scena în SplitCam (a doua cameră, overlay-uri, filtre de beauty sau fundal AI); LoyalFans o vede ca o singură webcam."),
            ("LoyalFans suportă OBS sau encodere externe?", "Live-ul ei e în primul rând bazat pe browser / webcam. Dacă în dashboard apare o opțiune de stream key, o lipești în câmpurile RTMP custom ale SplitCam; altfel folosești metoda cu camera virtuală."),
            ("SplitCam e gratuit pentru LoyalFans?", "Da — gratuit, fără filigran și fără limită de timp."),
        ],
        "steps": [
            ("Descarcă și instalează SplitCam", "SplitCam e software gratuit de live-streaming pentru Windows și macOS — fără înregistrare, fără card, fără filigran. Instalează o cameră virtuală pe care browserul o poate selecta."),
            ("Construiește scena", "Deschide SplitCam și adaugă webcam-ul. Pune deasupra overlay-uri, text cu tip-goal, o a doua cameră sau telefonul, filtre de beauty sau un fundal AI."),
            ("Pornește o transmisie live pe LoyalFans", "Loghează-te în contul tău LoyalFans și deschide broadcasterul live pentru a intra live pentru abonații tăi."),
            ("Alege SplitCam ca cameră", "În lista de camere a LoyalFans, alegi <strong>SplitCam</strong> în loc de webcam-ul tău brut — scena ta înlocuiește camera plată. (Sau, dacă e disponibilă, lipești o stream key în câmpurile RTMP custom ale SplitCam.)"),
            ("Apasă Go Live", "Pornește transmisia — scena ta SplitCam ajunge la audiența ta de pe LoyalFans."),
        ],
    },
    {
        "slug": "fancentro", "name": "FanCentro",
        "title": "Cum intri live pe FanCentro cu SplitCam — cameră virtuală",
        "desc": "Intră live pe FanCentro cu SplitCam gratuit ca o cameră virtuală — scene multi-cameră, overlay-uri și filtre pentru abonații tăi. Fără filigran, fără cont.",
        "kw": "cum intri live pe fancentro, fancentro, fancentro live, fancentro obs, fancentro cameră virtuală, fancentro broadcast, fan centro",
        "h1html": 'Cum intri live pe <span class="accent">FanCentro</span> cu SplitCam',
        "h1short": "Live pe FanCentro",
        "card": "Folosește SplitCam ca o cameră virtuală pentru live-ul de pe FanCentro.",
        "intro": "FanCentro e o platformă longevivă de monetizare pentru creatori — abonamente, mesaje pay-per-view, conținut și transmisie live. Live-ul ei merge în browser, așa că prin conectarea <strong style='color:var(--text)'>SplitCam</strong> gratuit ca o <strong>cameră virtuală</strong> adaugi scene multi-cameră, overlay-uri și filtre dincolo de webcam-ul simplu. Dacă în dashboard ai și o opțiune de external encoder / stream key, SplitCam se conectează în schimb prin RTMP.",
        "quick": "Intră live pe FanCentro cu SplitCam: instalezi SplitCam, construiești scena, pornești o transmisie live pe FanCentro, iar în selectorul de cameră al broadcasterului alegi <em>SplitCam</em> — apoi intri live."
                 "<ol><li>Instalează SplitCam.</li><li>Adaugă cameră + scenă.</li>"
                 "<li>Pornește o transmisie live pe FanCentro.</li>"
                 "<li>Alege SplitCam din lista de camere.</li>"
                 "<li>Apasă Go Live.</li></ol>",
        "key_how": "Live-ul FanCentro merge în browser. Construiește scena în SplitCam — apare ca o webcam de sistem numită <strong>\"SplitCam Video Driver\"</strong> — apoi deschide broadcasterul live FanCentro și, în lista de camere, alege <strong>SplitCam</strong>. Dacă e oferită o opțiune de <strong>stream key / external encoder</strong>, lipești în schimb cheia în câmpurile RTMP custom ale SplitCam.",
        "tips": [
            ("Camera virtuală merge peste tot", "Live-ul doar în browser primește tot scena ta SplitCam — overlay-uri, a doua cameră și filtre — selectând SplitCam ca webcam."),
            ("Cross-sell în funnelul tău", "FanCentro e construită în jurul funnelurilor de creator și al PPV. Overlay-urile care îți promovează abonamentul sau mesajele plătite îți transformă privitorii live în cumpărători."),
            ("Dă browserului permisiunea de cameră", "Dacă SplitCam nu apare în listă, rulează mai întâi SplitCam, permite accesul la cameră în browser, apoi reîncarcă broadcasterul."),
            _T_TEST,
        ],
        "faq": [
            ("Cum se conectează SplitCam la FanCentro?", "Live-ul FanCentro e în browser, deci SplitCam se conectează ca o cameră virtuală — alegi SplitCam în selectorul de cameră. Nu e nevoie de stream key."),
            ("Pot folosi overlay-uri și mai multe camere pe FanCentro?", "Da — construiești scena în SplitCam; FanCentro vede scena finită ca o singură webcam."),
            ("FanCentro suportă OBS sau encodere externe?", "Live-ul ei e în primul rând bazat pe browser / webcam. Dacă în dashboard apare o opțiune de stream key, o lipești în câmpurile RTMP custom ale SplitCam; altfel folosești metoda cu camera virtuală."),
            ("SplitCam e gratuit pentru FanCentro?", "Da — gratuit, fără filigran și fără limită de timp."),
        ],
        "steps": [
            ("Descarcă și instalează SplitCam", "SplitCam e software gratuit de live-streaming pentru Windows și macOS — fără înregistrare, fără card, fără filigran. Instalează o cameră virtuală pe care browserul o poate selecta."),
            ("Construiește scena", "Deschide SplitCam și adaugă webcam-ul. Pune deasupra overlay-uri, text, o a doua cameră sau telefonul, filtre de beauty sau un fundal AI."),
            ("Pornește o transmisie live pe FanCentro", "Loghează-te în contul tău FanCentro și deschide broadcasterul live pentru a intra live pentru abonații tăi."),
            ("Alege SplitCam ca cameră", "În lista de camere a FanCentro, alegi <strong>SplitCam</strong> în loc de webcam-ul tău brut. (Sau, dacă e disponibilă, lipești o stream key în câmpurile RTMP custom ale SplitCam.)"),
            ("Apasă Go Live", "Pornește transmisia — scena ta SplitCam ajunge la abonații tăi de pe FanCentro."),
        ],
    },
    {
        "slug": "ismygirl", "name": "IsMyGirl",
        "title": "Cum intri live pe IsMyGirl cu SplitCam — cameră virtuală",
        "desc": "Intră live pe IsMyGirl cu SplitCam gratuit ca o cameră virtuală — scene multi-cameră, overlay-uri și filtre pentru abonații tăi. Fără filigran, fără cont.",
        "kw": "cum intri live pe ismygirl, ismygirl, ismygirl live, ismygirl obs, ismygirl cameră virtuală, ismygirl broadcast, is my girl",
        "h1html": 'Cum intri live pe <span class="accent">IsMyGirl</span> cu SplitCam',
        "h1short": "Live pe IsMyGirl",
        "card": "Folosește SplitCam ca o cameră virtuală pentru live-ul de pe IsMyGirl.",
        "intro": "IsMyGirl e o platformă de abonamente deținută de creatori — o alternativă la OnlyFans cu abonamente, conținut plătit și transmisie live, cunoscută pentru suportul atent pentru creatori. Broadcasterul live merge în browser, așa că prin conectarea <strong style='color:var(--text)'>SplitCam</strong> gratuit ca o <strong>cameră virtuală</strong> aduci scene multi-cameră, overlay-uri și filtre. Dacă în dashboard ai și o opțiune de external encoder / stream key, SplitCam se conectează în schimb prin RTMP.",
        "quick": "Intră live pe IsMyGirl cu SplitCam: instalezi SplitCam, construiești scena, pornești o transmisie live pe IsMyGirl, iar în selectorul de cameră al broadcasterului alegi <em>SplitCam</em> — apoi intri live."
                 "<ol><li>Instalează SplitCam.</li><li>Adaugă cameră + scenă.</li>"
                 "<li>Pornește o transmisie live pe IsMyGirl.</li>"
                 "<li>Alege SplitCam din lista de camere.</li>"
                 "<li>Apasă Go Live.</li></ol>",
        "key_how": "Live-ul IsMyGirl merge în browser. Construiește scena în SplitCam — apare ca o webcam de sistem numită <strong>\"SplitCam Video Driver\"</strong> — apoi deschide broadcasterul live IsMyGirl și, în lista de camere, alege <strong>SplitCam</strong>. Dacă apare o opțiune de <strong>stream key / external encoder</strong>, lipești în schimb cheia în câmpurile RTMP custom ale SplitCam.",
        "tips": [
            ("Cameră virtuală, fără cheie", "Live-ul doar în browser primește tot scena ta SplitCam — overlay-uri, a doua cameră și filtre — selectând SplitCam ca webcam."),
            ("Profită de suportul pentru creatori", "IsMyGirl își promovează suportul puternic și promovarea creatorilor. O scenă SplitCam îngrijită plus overlay-uri de cross-sell valorifică la maximum traficul pe care ți-l trimit."),
            ("Dă browserului permisiunea de cameră", "Dacă SplitCam nu apare în listă, rulează mai întâi SplitCam, permite accesul la cameră, apoi reîncarcă broadcasterul."),
            _T_TEST,
        ],
        "faq": [
            ("Cum se conectează SplitCam la IsMyGirl?", "Live-ul IsMyGirl e în browser, deci SplitCam se conectează ca o cameră virtuală — alegi SplitCam în selectorul de cameră. Nu e nevoie de stream key."),
            ("Pot folosi overlay-uri și mai multe camere pe IsMyGirl?", "Da — compui scena în SplitCam; IsMyGirl o vede ca o singură webcam."),
            ("IsMyGirl suportă OBS sau encodere externe?", "Live-ul ei e în primul rând bazat pe browser / webcam. Dacă apare o opțiune de stream key, o lipești în câmpurile RTMP custom ale SplitCam; altfel folosești metoda cu camera virtuală."),
            ("SplitCam e gratuit pentru IsMyGirl?", "Da — gratuit, fără filigran și fără limită de timp."),
        ],
        "steps": [
            ("Descarcă și instalează SplitCam", "SplitCam e software gratuit de live-streaming pentru Windows și macOS — fără înregistrare, fără card, fără filigran. Instalează o cameră virtuală pe care browserul o poate selecta."),
            ("Construiește scena", "Deschide SplitCam și adaugă webcam-ul. Pune deasupra overlay-uri, text, o a doua cameră sau telefonul, filtre de beauty sau un fundal AI."),
            ("Pornește o transmisie live pe IsMyGirl", "Loghează-te în contul tău IsMyGirl și deschide broadcasterul live pentru a intra live pentru abonații tăi."),
            ("Alege SplitCam ca cameră", "În lista de camere a IsMyGirl, alegi <strong>SplitCam</strong> în loc de webcam-ul tău brut. (Sau, dacă e disponibilă, lipești o stream key în câmpurile RTMP custom ale SplitCam.)"),
            ("Apasă Go Live", "Pornește transmisia — scena ta SplitCam ajunge la abonații tăi de pe IsMyGirl."),
        ],
    },
    {
        "slug": "dxlive", "name": "DXLive",
        "title": "Cum transmiți pe DXLive cu SplitCam — encoder extern",
        "desc": "Transmite pe DXLive cu SplitCam gratuit — encoder extern pentru rețeaua cam premium japoneză, scene multi-cameră și overlay-uri. Fără filigran.",
        "kw": "cum transmiți pe dxlive, dxlive, dxlive broadcast, dxlive obs, dxlive external encoder, dxlive rtmp, dxlive performer",
        "h1html": 'Cum transmiți pe <span class="accent">DXLive</span> cu SplitCam',
        "h1short": "Transmisie pe DXLive",
        "card": "Setup cu encoder extern pentru rețeaua cam premium DXLive.",
        "intro": "DXLive e o rețea webcam premium consacrată, populară în Japonia și în toată Asia, construită pe un model pay-per-minute cu o audiență loială. Zona de performer suportă o cale standard de <strong>external encoder</strong> la care se conectează <strong style='color:var(--text)'>SplitCam</strong> gratuit — astfel transmiți cu scene multi-cameră, overlay-uri și beauty filters în loc de o singură webcam plată.",
        "quick": "Transmisie pe DXLive cu SplitCam: instalezi SplitCam, construiești scena, în zona de performer deschizi setările <em>external encoder / broadcast</em>, copiezi URL-ul serverului și stream key-ul, le lipești în SplitCam, Go Live."
                 "<ol><li>Instalează SplitCam.</li><li>Adaugă cameră + scenă.</li>"
                 "<li>Obține URL și stream key din zona de performer.</li><li>Lipește în SplitCam.</li>"
                 "<li>Apasă Go Live.</li></ol>",
        "key_how": "Loghează-te în contul tău de performer DXLive și deschide setările <strong>broadcast / external encoder</strong> din zona de performer. Pagina dezvăluie un <strong>URL server</strong> și o <strong>stream key</strong> legate de cont — copiază-le în câmpurile RTMP custom ale SplitCam. Verificarea DXLive e obligatorie înainte ca funcția de live cam să fie activată.",
        "tips": [
            ("Construit pentru piața asiatică", "Audiența DXLive înclină spre Japonia / Asia și plătește pe minut. Programează-ți show-urile pentru serile JST și baza loială și plătitoare convertește bine."),
            ("Polish-ul bate webcam-ul brut", "O scenă SplitCam curată cu overlay-uri și beauty filters iese în evidență pe o rețea premium pay-per-minute unde privitorii se așteaptă la calitate."),
            ("Folosește encoderul extern, nu doar webcam-ul", "Trecerea prin RTMP-ul SplitCam, nu prin camera de browser de bază, e ceea ce deblochează scenele multi-cameră și filtrele."),
            _T_ETH,
        ],
        "faq": [
            ("DXLive suportă encodere externe precum SplitCam?", "Da — zona de performer expune o cale standard de external encoder / RTMP. Copiază URL-ul serverului și stream key-ul în SplitCam după verificare."),
            ("Unde îmi iau stream key-ul DXLive?", "În setările broadcast / external encoder din zona de performer — atât URL-ul serverului, cât și stream key-ul apar acolo. Lipește ambele în câmpurile RTMP custom ale SplitCam."),
            ("Ce bitrate folosesc pentru DXLive?", "Împinge 1920×1080 la 30 fps, 3.500–6.000 Kbps cu keyframe la 2 secunde. Rulează întâi speed test-ul integrat din SplitCam."),
            ("SplitCam e gratuit pentru DXLive?", "Da — SplitCam e gratuit, fără filigran și fără limită de timp. Opțiunea de external encoder de la DXLive e gratuită în zona de performer."),
        ],
        "steps": [
            ("Descarcă și instalează SplitCam", "SplitCam e software gratuit de live-streaming pentru Windows și macOS — fără înregistrare, fără card, fără filigran."),
            ("Construiește scena", "Deschide SplitCam și adaugă webcam-ul. Pune deasupra overlay-uri, text, o a doua cameră sau telefonul, filtre de beauty sau un fundal AI."),
            ("Obține URL și stream key DXLive", "Loghează-te în contul tău de performer DXLive și deschide setările <strong>broadcast / external encoder</strong>. Copiază <strong>URL-ul serverului</strong> și <strong>stream key-ul</strong>."),
            ("Conectează SplitCam la DXLive", "În SplitCam deschide <strong>Stream Settings</strong>, lipește URL-ul serverului DXLive și stream key-ul în câmpurile RTMP custom. Setează 3.500–6.000 Kbps la 1920×1080, 30 fps, cu keyframe la 2 secunde."),
            ("Apasă Go Live", "Apasă <strong>Go Live</strong> în SplitCam, apoi treci online din zona de performer. În ~10 secunde stream-ul tău ajunge la audiența DXLive."),
        ],
    },
    {
        "slug": "streamen", "name": "Streamen",
        "title": "Cum transmiți pe Streamen cu SplitCam — encoder extern",
        "desc": "Transmite pe Streamen cu SplitCam gratuit — setup cu encoder extern, scene multi-cameră, overlay-uri și beauty filters. Fără filigran, fără cont.",
        "kw": "cum transmiți pe streamen, streamen, streamen broadcast, streamen obs, streamen external encoder, streamen rtmp, streamen.tv",
        "h1html": 'Cum transmiți pe <span class="accent">Streamen</span> cu SplitCam',
        "h1short": "Transmisie pe Streamen",
        "card": "Setup cu encoder extern pentru platforma cam Streamen.",
        "intro": "Streamen e o platformă live cam unde modelele transmit către o audiență condusă de tipping. Setările ei de broadcast expun o cale standard de <strong>external encoder</strong> la care se conectează <strong style='color:var(--text)'>SplitCam</strong> gratuit — astfel transmiți cu scene multi-cameră, overlay-uri și filtre în loc de o singură webcam simplă.",
        "quick": "Transmisie pe Streamen cu SplitCam: instalezi SplitCam, construiești scena, în dashboardul de model deschizi <em>broadcast settings → external encoder</em>, copiezi URL-ul serverului și stream key-ul, le lipești în SplitCam, Go Live."
                 "<ol><li>Instalează SplitCam.</li><li>Adaugă cameră + scenă.</li>"
                 "<li>Obține URL și stream key din dashboard.</li><li>Lipește în SplitCam.</li>"
                 "<li>Apasă Go Live.</li></ol>",
        "key_how": "Loghează-te în contul tău de model Streamen și deschide secțiunea <strong>broadcast settings / external encoder</strong>. Aceasta dezvăluie un <strong>URL server</strong> și o <strong>stream key</strong> legate de cont — copiază-le în câmpurile RTMP custom ale SplitCam. Verificarea modelului e obligatorie înainte ca transmisia să fie activată.",
        "tips": [
            ("Audiență condusă de tip-uri", "Privitorii Streamen dau tip-uri — tip-goal-urile pe ecran și o scenă îngrijită împing mai multe tip-uri decât o webcam plată."),
            ("Encoderul extern deblochează scenele", "Trecerea prin RTMP-ul SplitCam, nu prin camera de browser de bază, e ceea ce activează layout-urile multi-cameră, overlay-urile și filtrele."),
            ("Fixează rezoluția", "Setează 1080p manual ca fluxul să nu scadă pe tăcute calitatea; un bitrate care coboară pe o imagine statică e normal pe fluxurile adaptive."),
            _T_ETH,
        ],
        "faq": [
            ("Streamen suportă encodere externe precum SplitCam?", "Da — setările de broadcast expun o cale standard de external encoder / RTMP. Copiază URL-ul serverului și stream key-ul în SplitCam după verificare."),
            ("Unde îmi iau stream key-ul Streamen?", "În setările broadcast / external encoder din dashboardul de model — atât URL-ul serverului, cât și stream key-ul apar acolo. Lipește ambele în câmpurile RTMP custom ale SplitCam."),
            ("Ce bitrate folosesc pentru Streamen?", "Împinge 1920×1080 la 30 fps, 3.500–6.000 Kbps cu keyframe la 2 secunde. Rulează întâi speed test-ul din SplitCam."),
            ("SplitCam e gratuit pentru Streamen?", "Da — SplitCam e gratuit, fără filigran și fără limită de timp. Opțiunea de external encoder de la Streamen e gratuită în dashboard."),
        ],
        "steps": [
            ("Descarcă și instalează SplitCam", "SplitCam e software gratuit de live-streaming pentru Windows și macOS — fără înregistrare, fără card, fără filigran."),
            ("Construiește scena", "Deschide SplitCam și adaugă webcam-ul. Pune deasupra overlay-uri, text cu tip-goal, o a doua cameră sau telefonul, filtre de beauty sau un fundal AI."),
            ("Obține URL și stream key Streamen", "Loghează-te în contul tău de model Streamen, deschide <strong>broadcast settings → external encoder</strong> și copiază <strong>URL-ul serverului</strong> și <strong>stream key-ul</strong>."),
            ("Conectează SplitCam la Streamen", "În SplitCam deschide <strong>Stream Settings</strong>, lipește URL-ul serverului Streamen și stream key-ul în câmpurile RTMP custom. Setează 3.500–6.000 Kbps la 1920×1080, 30 fps, cu keyframe la 2 secunde."),
            ("Apasă Go Live", "Apasă <strong>Go Live</strong> în SplitCam, apoi treci online din dashboard. În ~10 secunde stream-ul tău ajunge la audiența Streamen."),
        ],
    },
    {
        "slug": "xcams", "name": "XCams",
        "title": "Cum transmiți pe XCams cu SplitCam — encoder extern",
        "desc": "Transmite pe XCams cu SplitCam gratuit — encoder extern pentru comunitatea cam europeană, scene multi-cameră, overlay-uri și filtre. Fără filigran.",
        "kw": "cum transmiți pe xcams, xcams, xcams broadcast, xcams obs, xcams external encoder, xcams rtmp, x cams",
        "h1html": 'Cum transmiți pe <span class="accent">XCams</span> cu SplitCam',
        "h1short": "Transmisie pe XCams",
        "card": "Setup cu encoder extern pentru comunitatea europeană XCams.",
        "intro": "XCams e o comunitate europeană de live cam — puternică în Italia, Franța și Spania — construită în jurul show-urilor live și al unei economii de tipping / private show. Zona de model suportă o cale standard de <strong>external encoder</strong> la care se conectează <strong style='color:var(--text)'>SplitCam</strong> gratuit, astfel încât transmiți cu scene multi-cameră, overlay-uri și beauty filters.",
        "quick": "Transmisie pe XCams cu SplitCam: instalezi SplitCam, construiești scena, în zona de model deschizi <em>broadcast / external encoder</em>, copiezi URL-ul serverului și stream key-ul, le lipești în SplitCam, Go Live."
                 "<ol><li>Instalează SplitCam.</li><li>Adaugă cameră + scenă.</li>"
                 "<li>Obține URL și stream key din zona de model.</li><li>Lipește în SplitCam.</li>"
                 "<li>Apasă Go Live.</li></ol>",
        "key_how": "Loghează-te în contul tău de model XCams și deschide setările <strong>broadcast / external encoder</strong> din zona de model. Pagina dezvăluie un <strong>URL server</strong> și o <strong>stream key</strong> legate de cont — copiază-le în câmpurile RTMP custom ale SplitCam. Verificarea XCams e obligatorie înainte de transmisie.",
        "tips": [
            ("Prime-time european", "Traficul XCams atinge vârful în serile UE (CET). Transmisia în acele ore depășește semnificativ orele moarte pe această comunitate."),
            ("Private show-urile răsplătesc calitatea", "XCams funcționează pe private / spy show — o scenă SplitCam îngrijită cu overlay-uri convertește vizitatorii în private-uri plătite."),
            ("Encoderul extern deblochează scenele", "Trecerea prin RTMP-ul SplitCam, nu prin camera de browser, activează layout-urile multi-cameră, overlay-urile și filtrele."),
            _T_ETH,
        ],
        "faq": [
            ("XCams suportă encodere externe precum SplitCam?", "Da — zona de model expune o cale standard de external encoder / RTMP. Copiază URL-ul serverului și stream key-ul în SplitCam după verificare."),
            ("Unde îmi iau stream key-ul XCams?", "În setările broadcast / external encoder din zona de model — atât URL-ul serverului, cât și stream key-ul apar acolo. Lipește ambele în câmpurile RTMP custom ale SplitCam."),
            ("Ce bitrate folosesc pentru XCams?", "Împinge 1920×1080 la 30 fps, 3.500–6.000 Kbps cu keyframe la 2 secunde. Rulează întâi speed test-ul din SplitCam."),
            ("SplitCam e gratuit pentru XCams?", "Da — SplitCam e gratuit, fără filigran și fără limită de timp. Opțiunea de external encoder de la XCams e gratuită în zona de model."),
        ],
        "steps": [
            ("Descarcă și instalează SplitCam", "SplitCam e software gratuit de live-streaming pentru Windows și macOS — fără înregistrare, fără card, fără filigran."),
            ("Construiește scena", "Deschide SplitCam și adaugă webcam-ul. Pune deasupra overlay-uri, text, o a doua cameră sau telefonul, filtre de beauty sau un fundal AI."),
            ("Obține URL și stream key XCams", "Loghează-te în contul tău de model XCams, deschide <strong>broadcast / external encoder</strong> și copiază <strong>URL-ul serverului</strong> și <strong>stream key-ul</strong>."),
            ("Conectează SplitCam la XCams", "În SplitCam deschide <strong>Stream Settings</strong>, lipește URL-ul serverului XCams și stream key-ul în câmpurile RTMP custom. Setează 3.500–6.000 Kbps la 1920×1080, 30 fps, cu keyframe la 2 secunde."),
            ("Apasă Go Live", "Apasă <strong>Go Live</strong> în SplitCam, apoi treci online din zona de model. În ~10 secunde stream-ul tău ajunge la audiența XCams."),
        ],
    },
    {
        "slug": "camcontacts", "name": "CamContacts",
        "title": "Cum transmiți pe CamContacts cu SplitCam — encoder extern",
        "desc": "Transmite pe CamContacts cu SplitCam gratuit — encoder extern pentru cam-site-ul longeviv pay-per-minute, scene multi-cameră și overlay-uri. Fără filigran.",
        "kw": "cum transmiți pe camcontacts, camcontacts, camcontacts broadcast, camcontacts obs, camcontacts external encoder, camcontacts rtmp, cam contacts",
        "h1html": 'Cum transmiți pe <span class="accent">CamContacts</span> cu SplitCam',
        "h1short": "Transmisie pe CamContacts",
        "card": "Setup cu encoder extern pentru cam-ul pay-per-minute al CamContacts.",
        "intro": "CamContacts e unul dintre cele mai longevive cam-site-uri independente — un model pay-per-minute cu o audiență matură, loială și o reputație de plăți constante. Zona de performer suportă o cale standard de <strong>external encoder</strong> la care se conectează <strong style='color:var(--text)'>SplitCam</strong> gratuit, astfel încât transmiți cu scene multi-cameră, overlay-uri și beauty filters.",
        "quick": "Transmisie pe CamContacts cu SplitCam: instalezi SplitCam, construiești scena, în zona de performer deschizi setările <em>external encoder / broadcast</em>, copiezi URL-ul serverului și stream key-ul, le lipești în SplitCam, Go Live."
                 "<ol><li>Instalează SplitCam.</li><li>Adaugă cameră + scenă.</li>"
                 "<li>Obține URL și stream key din zona de performer.</li><li>Lipește în SplitCam.</li>"
                 "<li>Apasă Go Live.</li></ol>",
        "key_how": "Loghează-te în contul tău de performer CamContacts și deschide setările <strong>broadcast / external encoder</strong> din zona de performer. Pagina dezvăluie un <strong>URL server</strong> și o <strong>stream key</strong> legate de cont — copiază-le în câmpurile RTMP custom ale SplitCam. Verificarea CamContacts e obligatorie pentru funcția de live cam.",
        "tips": [
            ("Audiență matură, loială", "CamContacts funcționează de decenii, cu membri pe termen lung — obișnuiți mai stabili și mai plătitori decât pe un site gratuit cu churn mare, dar creștere mai lentă pentru începători."),
            ("Pay-per-minute răsplătește retenția", "Ține privitorii în timp plătit cu o scenă îngrijită și overlay-uri; valoarea de producție prelungește sesiunile pe un model pe minut."),
            ("Encoderul extern deblochează scenele", "Trecerea prin RTMP-ul SplitCam, nu prin camera de bază, activează layout-urile multi-cameră, overlay-urile și filtrele."),
            _T_ETH,
        ],
        "faq": [
            ("CamContacts suportă encodere externe precum SplitCam?", "Da — zona de performer expune o cale standard de external encoder / RTMP. Copiază URL-ul serverului și stream key-ul în SplitCam după verificare."),
            ("Unde îmi iau stream key-ul CamContacts?", "În setările broadcast / external encoder din zona de performer — atât URL-ul serverului, cât și stream key-ul apar acolo. Lipește ambele în câmpurile RTMP custom ale SplitCam."),
            ("Ce bitrate folosesc pentru CamContacts?", "Împinge 1920×1080 la 30 fps, 3.500–6.000 Kbps cu keyframe la 2 secunde. Rulează întâi speed test-ul din SplitCam."),
            ("SplitCam e gratuit pentru CamContacts?", "Da — SplitCam e gratuit, fără filigran și fără limită de timp. Opțiunea de external encoder de la CamContacts e gratuită în zona de performer."),
        ],
        "steps": [
            ("Descarcă și instalează SplitCam", "SplitCam e software gratuit de live-streaming pentru Windows și macOS — fără înregistrare, fără card, fără filigran."),
            ("Construiește scena", "Deschide SplitCam și adaugă webcam-ul. Pune deasupra overlay-uri, text, o a doua cameră sau telefonul, filtre de beauty sau un fundal AI."),
            ("Obține URL și stream key CamContacts", "Loghează-te în contul tău de performer CamContacts, deschide setările <strong>broadcast / external encoder</strong> și copiază <strong>URL-ul serverului</strong> și <strong>stream key-ul</strong>."),
            ("Conectează SplitCam la CamContacts", "În SplitCam deschide <strong>Stream Settings</strong>, lipește URL-ul serverului CamContacts și stream key-ul în câmpurile RTMP custom. Setează 3.500–6.000 Kbps la 1920×1080, 30 fps, cu keyframe la 2 secunde."),
            ("Apasă Go Live", "Apasă <strong>Go Live</strong> în SplitCam, apoi treci online din zona de performer. În ~10 secunde stream-ul tău ajunge la audiența CamContacts."),
        ],
    },
    {
        "slug": "royalcams", "name": "RoyalCams",
        "title": "Cum transmiți pe RoyalCams cu SplitCam — encoder extern",
        "desc": "Transmite pe RoyalCams cu SplitCam gratuit — encoder extern pentru cam-site-ul gratuit pe tokeni, scene multi-cameră, overlay-uri și filtre. Fără filigran.",
        "kw": "cum transmiți pe royalcams, royalcams, royalcams broadcast, royalcams obs, royalcams external encoder, royalcams rtmp, royal cams",
        "h1html": 'Cum transmiți pe <span class="accent">RoyalCams</span> cu SplitCam',
        "h1short": "Transmisie pe RoyalCams",
        "card": "Setup cu encoder extern pentru cam-site-ul pe tokeni RoyalCams.",
        "intro": "RoyalCams e un cam-site gratuit bazat pe tokeni — camere publice deschise, finanțate din tip-uri, cu private show-uri deasupra. Setările de broadcast suportă o cale standard de <strong>external encoder</strong> la care se conectează <strong style='color:var(--text)'>SplitCam</strong> gratuit, astfel încât transmiți cu scene multi-cameră, overlay-uri și beauty filters în loc de o singură webcam plată.",
        "quick": "Transmisie pe RoyalCams cu SplitCam: instalezi SplitCam, construiești scena, în dashboardul de model deschizi <em>broadcast settings → external encoder</em>, copiezi URL-ul serverului și stream key-ul, le lipești în SplitCam, Go Live."
                 "<ol><li>Instalează SplitCam.</li><li>Adaugă cameră + scenă.</li>"
                 "<li>Obține URL și stream key din dashboard.</li><li>Lipește în SplitCam.</li>"
                 "<li>Apasă Go Live.</li></ol>",
        "key_how": "Loghează-te în contul tău de model RoyalCams și deschide secțiunea <strong>broadcast settings / external encoder</strong>. Aceasta dezvăluie un <strong>URL server</strong> și o <strong>stream key</strong> legate de cont — copiază-le în câmpurile RTMP custom ale SplitCam. Verificarea modelului e obligatorie înainte de transmisie.",
        "tips": [
            ("Camerele pe tokeni răsplătesc producția", "Camerele publice RoyalCams funcționează pe tip-uri — tip-goal-urile și o scenă îngrijită convertesc spectatorii tăcuți în tipperi și private show-uri."),
            ("Convertește spre private show-uri", "Folosește o scenă publică puternică pentru a face upsell la private show-uri, unde stau câștigurile reale pe cam-site-urile pe tokeni."),
            ("Encoderul extern deblochează scenele", "Trecerea prin RTMP-ul SplitCam, nu prin camera de browser, activează layout-urile multi-cameră, overlay-urile și filtrele."),
            _T_ETH,
        ],
        "faq": [
            ("RoyalCams suportă encodere externe precum SplitCam?", "Da — setările de broadcast expun o cale standard de external encoder / RTMP. Copiază URL-ul serverului și stream key-ul în SplitCam după verificare."),
            ("Unde îmi iau stream key-ul RoyalCams?", "În setările broadcast / external encoder din dashboardul de model — atât URL-ul serverului, cât și stream key-ul apar acolo. Lipește ambele în câmpurile RTMP custom ale SplitCam."),
            ("Ce bitrate folosesc pentru RoyalCams?", "Împinge 1920×1080 la 30 fps, 3.500–6.000 Kbps cu keyframe la 2 secunde. Rulează întâi speed test-ul din SplitCam."),
            ("SplitCam e gratuit pentru RoyalCams?", "Da — SplitCam e gratuit, fără filigran și fără limită de timp. Opțiunea de external encoder de la RoyalCams e gratuită în dashboard."),
        ],
        "steps": [
            ("Descarcă și instalează SplitCam", "SplitCam e software gratuit de live-streaming pentru Windows și macOS — fără înregistrare, fără card, fără filigran."),
            ("Construiește scena", "Deschide SplitCam și adaugă webcam-ul. Pune deasupra overlay-uri, text cu tip-goal, o a doua cameră sau telefonul, filtre de beauty sau un fundal AI."),
            ("Obține URL și stream key RoyalCams", "Loghează-te în contul tău de model RoyalCams, deschide <strong>broadcast settings → external encoder</strong> și copiază <strong>URL-ul serverului</strong> și <strong>stream key-ul</strong>."),
            ("Conectează SplitCam la RoyalCams", "În SplitCam deschide <strong>Stream Settings</strong>, lipește URL-ul serverului RoyalCams și stream key-ul în câmpurile RTMP custom. Setează 3.500–6.000 Kbps la 1920×1080, 30 fps, cu keyframe la 2 secunde."),
            ("Apasă Go Live", "Apasă <strong>Go Live</strong> în SplitCam, apoi treci online din dashboard. În ~10 secunde stream-ul tău ajunge la audiența RoyalCams."),
        ],
    },
    {
        "slug": "modelhub", "name": "Modelhub",
        "title": "Cum transmiți pe Modelhub cu SplitCam — encoder extern",
        "desc": "Transmite pe Modelhub Live cu SplitCam gratuit — encoder extern pentru platforma de creatori Pornhub, scene multi-cameră și overlay-uri. Fără filigran.",
        "kw": "cum transmiți pe modelhub, modelhub, modelhub live, modelhub obs, modelhub external encoder, modelhub rtmp, modelhub cam",
        "h1html": 'Cum transmiți pe <span class="accent">Modelhub</span> cu SplitCam',
        "h1short": "Transmisie pe Modelhub",
        "card": "Setup cu encoder extern pentru Modelhub Live (Pornhub).",
        "intro": "Modelhub e platforma de creatori a Pornhub — vânzări video, abonamente de fani și un produs <strong>live cam</strong> cu trafic masiv în vârful de funnel din rețeaua Pornhub. Dashboardul de model suportă o cale standard de <strong>external encoder</strong> la care se conectează <strong style='color:var(--text)'>SplitCam</strong> gratuit, astfel încât transmiți cu scene multi-cameră, overlay-uri și beauty filters.",
        "quick": "Transmisie pe Modelhub cu SplitCam: instalezi SplitCam, construiești scena, în dashboardul de model deschizi <em>Live → broadcast / external encoder</em>, copiezi URL-ul serverului și stream key-ul, le lipești în SplitCam, Go Live."
                 "<ol><li>Instalează SplitCam.</li><li>Adaugă cameră + scenă.</li>"
                 "<li>Obține URL și stream key din dashboard.</li><li>Lipește în SplitCam.</li>"
                 "<li>Apasă Go Live.</li></ol>",
        "key_how": "Loghează-te în contul tău de model Modelhub și deschide setările <strong>Live / broadcast / external encoder</strong> din dashboard. Pagina dezvăluie un <strong>URL server</strong> și o <strong>stream key</strong> legate de cont — copiază-le în câmpurile RTMP custom ale SplitCam. Verificarea modelului în rețea e obligatorie înainte de live.",
        "tips": [
            ("Trafic uriaș în vârful de funnel", "Modelhub atrage privitori din rețeaua Pornhub — o scenă SplitCam îngrijită convertește acea audiență mare și ocazională în privitori live și abonați plătitori."),
            ("Cross-sell la videoclipurile tale", "Folosește overlay-uri ca să-ți îndrumi privitorii live spre videoclipurile și abonamentul tău de pe Modelhub — platforma e construită pentru acel funnel."),
            ("Encoderul extern deblochează scenele", "Trecerea prin RTMP-ul SplitCam, nu prin camera de bază, activează layout-urile multi-cameră, overlay-urile și filtrele."),
            _T_ETH,
        ],
        "faq": [
            ("Modelhub suportă encodere externe precum SplitCam?", "Da — dashboardul de model expune o cale standard de external encoder / RTMP pentru Modelhub Live. Copiază URL-ul serverului și stream key-ul în SplitCam după verificare."),
            ("Unde îmi iau stream key-ul Modelhub?", "În setările Live / broadcast / external encoder din dashboard — atât URL-ul serverului, cât și stream key-ul apar acolo. Lipește ambele în câmpurile RTMP custom ale SplitCam."),
            ("Ce bitrate folosesc pentru Modelhub?", "Împinge 1920×1080 la 30 fps, 3.500–6.000 Kbps cu keyframe la 2 secunde. Rulează întâi speed test-ul din SplitCam."),
            ("SplitCam e gratuit pentru Modelhub?", "Da — SplitCam e gratuit, fără filigran și fără limită de timp. Opțiunea de external encoder de la Modelhub e gratuită în dashboard."),
        ],
        "steps": [
            ("Descarcă și instalează SplitCam", "SplitCam e software gratuit de live-streaming pentru Windows și macOS — fără înregistrare, fără card, fără filigran."),
            ("Construiește scena", "Deschide SplitCam și adaugă webcam-ul. Pune deasupra overlay-uri, text, o a doua cameră sau telefonul, filtre de beauty sau un fundal AI."),
            ("Obține URL și stream key Modelhub", "Loghează-te în contul tău de model Modelhub, deschide <strong>Live → broadcast / external encoder</strong> și copiază <strong>URL-ul serverului</strong> și <strong>stream key-ul</strong>."),
            ("Conectează SplitCam la Modelhub", "În SplitCam deschide <strong>Stream Settings</strong>, lipește URL-ul serverului Modelhub și stream key-ul în câmpurile RTMP custom. Setează 3.500–6.000 Kbps la 1920×1080, 30 fps, cu keyframe la 2 secunde."),
            ("Apasă Go Live", "Apasă <strong>Go Live</strong> în SplitCam, apoi treci online din dashboard. În ~10 secunde stream-ul tău ajunge la audiența Modelhub."),
        ],
    },
    {
        "slug": "xhamsterlive", "name": "xHamsterLive",
        "title": "Cum transmiți pe xHamsterLive cu SplitCam (RTMP/OBS)",
        "desc": "Transmite pe xHamsterLive cu SplitCam gratuit prin RTMP — scene multi-cameră, overlay-uri și filtre. Trafic mainstream xHamster, fără filigran.",
        "kw": "cum transmiți pe xhamsterlive, xhamsterlive obs, xhamsterlive rtmp, xhamsterlive broadcast, xhamsterlive model, xhamster live cam, xhamsterlive studio, xhamster live stream key",
        "h1html": 'Cum transmiți pe <span class="accent">xHamsterLive</span> cu SplitCam',
        "h1short": "Transmisie xHamsterLive",
        "card": "SplitCam gratuit → transmisie RTMP/OBS spre xHamsterLive.",
        "intro": "xHamsterLive e brațul live-cam al xHamster — aceeași tehnologie de broadcaster ca Stripchat, dar canalizată prin traficul mainstream al xHamster, una dintre cele mai mari baze de privitori din industria adult. Modelele transmit prin <strong>Studio</strong>-ul xHamsterLive, care suportă atât broadcasterul din browser, cât și un <strong>encoder extern prin RTMP</strong>. Cu <strong style='color:var(--text)'>SplitCam</strong> gratuit transmiți ca encoder extern pentru scene multi-cameră complete, overlay-uri și filtre — sau, dacă transmiți din browser, setezi xHamsterLive să folosească SplitCam drept <strong>cameră virtuală</strong>, cu același efect.",
        "quick": "Transmisie pe xHamsterLive cu SplitCam: instalezi SplitCam, construiești scena, copiezi URL-ul serverului și stream key-ul din Studio-ul xHamsterLive, le lipești în setările RTMP ale SplitCam, apasă Go Live."
                 "<ol><li>Instalează SplitCam.</li><li>Adaugă cameră + scenă.</li>"
                 "<li>Copiază URL + stream key din Studio xHamsterLive → External Encoder.</li>"
                 "<li>Lipește în RTMP custom SplitCam.</li><li>Apasă Go Live.</li></ol>",
        "key_how": "Studio-ul xHamsterLive afișează broadcasterilor un tab <strong>external encoder</strong> cu URL de server și stream key. Lipește ambele în <strong>Stream Settings → Custom RTMP</strong> din SplitCam; alege 4.000–6.000 Kbps la 1920×1080, 30 fps, keyframe la 2 secunde. Apasă <strong>Go Live</strong> în SplitCam, apoi treci online din Studio. Dacă preferi broadcasterul din browser, deschide-l și alege <strong>SplitCam</strong> din dropdown-ul de cameră — scena ta compusă înlocuiește webcam-ul brut.",
        "tips": [
            ("Trafic xHamster, motor Stripchat", "Aceleași unelte de broadcaster ca Stripchat (panou Studio, meniu de tip-uri, Lovense), dar cu funnelul mainstream al xHamster — un mix diferit de audiență ajunge în camera ta."),
            ("Folosește encoder extern dacă poți", "RTMP din SplitCam îți dă bitrate stabil și scene multi-cameră/overlay-uri complete; broadcasterul din browser e ok, dar limitează opțiunile de compoziție."),
            ("Meniurile de tip-uri convertesc audiența mainstream", "Mulți vizitatori xHamster sunt noi la cam — un meniu de tip-uri clar pe ecran și un goal bar setează așteptările și cresc conversia pe sesiune."),
            _T_TEST,
        ],
        "faq": [
            ("xHamsterLive e același lucru cu Stripchat?", "Rulează pe motorul de broadcaster al Stripchat, dar brandul și sursa de trafic diferă — xHamster canalizează audiența sa mainstream aici, deci profilul de privitor diferă de un signup direct pe Stripchat."),
            ("De unde iau stream key-ul xHamsterLive?", "În Studio-ul xHamsterLive deschide panoul <em>Broadcast</em> sau <em>External Encoder</em> — vei vedea un URL de server și un stream key. Lipește ambele în câmpurile RTMP custom ale SplitCam."),
            ("Broadcaster din browser sau RTMP?", "Encoderul extern (RTMP) e preferat pentru modelele serioase — bitrate stabil și scene SplitCam complete. Broadcasterul din browser merge și el: alege SplitCam drept webcam."),
            ("SplitCam e gratuit pentru xHamsterLive?", "Da — SplitCam e gratuit, fără filigran și fără limită de timp."),
        ],
        "steps": [
            ("Descarcă și instalează SplitCam", "SplitCam e software gratuit de live-streaming pentru Windows și macOS — fără înregistrare, fără card, fără filigran."),
            ("Construiește scena", "Deschide SplitCam și adaugă webcam-ul. Pune deasupra overlay-uri, un meniu de tip-uri, o a doua cameră sau telefonul, filtre de beauty sau un fundal AI — totul live."),
            ("Obține URL + key din Studio xHamsterLive", "Loghează-te în xHamsterLive, deschide Studio, treci pe <strong>External Encoder</strong> și copiază <strong>URL-ul serverului</strong> și <strong>stream key-ul</strong>."),
            ("Conectează SplitCam la xHamsterLive", "În SplitCam → <strong>Stream Settings → Custom RTMP</strong>, lipește URL-ul și cheia. Setează 4.000–6.000 Kbps la 1920×1080, 30 fps, keyframe la 2 secunde."),
            ("Apasă Go Live", "Apasă <strong>Go Live</strong> în SplitCam, apoi treci online din Studio-ul xHamsterLive. În ~10 secunde stream-ul tău apare pe lista publică."),
        ],
    },
    {
        "slug": "premium-chat", "name": "Premium.Chat",
        "title": "Cum folosești SplitCam pe Premium.Chat — apeluri plătite",
        "desc": "Folosește SplitCam gratuit drept cameră virtuală pe Premium.Chat — apeluri video plătite la minut, scene multi-cameră, overlay-uri, filtre. Fără filigran.",
        "kw": "cum folosești splitcam pe premium chat, premium chat apel video, premium chat cameră virtuală, premium.chat pay per minute, premium chat model, premium chat advisor, premium chat live, platformă apel video splitcam",
        "h1html": 'Cum folosești SplitCam pe <span class="accent">Premium.Chat</span>',
        "h1short": "Premium.Chat cu SplitCam",
        "card": "Folosește SplitCam drept cameră virtuală pentru apeluri plătite Premium.Chat.",
        "intro": "Premium.Chat e o platformă plătită la minut: îți setezi tariful per minut pentru chat, voce sau <strong>apeluri video</strong>, distribui linkul tău personal, iar clienții plătesc ca să discute cu tine. Apelurile rulează în browser, ceea ce înseamnă că <strong style='color:var(--text)'>SplitCam</strong> gratuit se conectează direct ca <strong>cameră virtuală</strong> — scene multi-cameră, overlay-uri, filtre de lumină și un fundal AI ajung la apelant fără să schimbi modul în care funcționează Premium.Chat.",
        "quick": "Folosește SplitCam pe Premium.Chat: instalezi SplitCam, construiești o scenă curată pentru apeluri video, accepți un apel Premium.Chat și în selectorul de cameră al apelului alegi <em>SplitCam</em>."
                 "<ol><li>Instalează SplitCam.</li><li>Configurează scena (lumină bună, overlay opțional).</li>"
                 "<li>Setează tariful pe minut pe Premium.Chat.</li><li>Acceptă apelul video.</li>"
                 "<li>Alege SplitCam drept cameră.</li></ol>",
        "key_how": "Apelurile Premium.Chat se desfășoară în browser. SplitCam instalează un webcam virtual numit <strong>„SplitCam Video Driver”</strong> — când începe apelul, clic pe meniul cu iconița de cameră din fereastra Premium.Chat și schimbă de pe webcam-ul integrat pe <strong>SplitCam</strong>. Scena ta compusă (cameră reală + overlay-uri + filtre) devine ceea ce vede apelantul.",
        "tips": [
            ("Premium.Chat e per minut, nu streaming", "Spre deosebire de camerele de tip Chaturbate cu tip-uri, ești plătit la minut. Lumină moale, audio clar și un fundal AI arată mai degrabă a consultație premium decât a cam public."),
            ("Promovează linkul, nu un profil", "Premium.Chat îți dă un link personal pe care îl poți pune pe rețele sociale, în bio-ul OnlyFans sau pe un Linktree — așa te găsesc apelanții."),
            ("Overlay-uri doar dacă sunt utile", "La apeluri 1-on-1, overlay-urile groase distrag. Folosește SplitCam pentru calitatea camerei, lumină și fundal — păstrează ecranul preponderent pe tine."),
            _T_TEST,
        ],
        "faq": [
            ("Cum se conectează SplitCam la Premium.Chat?", "Drept cameră virtuală. Apelurile Premium.Chat rulează în browser; alege SplitCam din selectorul de cameră al apelului — fără stream key, fără RTMP."),
            ("Premium.Chat suportă OBS?", "Premium.Chat e bazat pe browser, deci OBS se conectează la fel ca SplitCam — prin cameră virtuală. SplitCam e varianta mai ușoară, gratuită și fără filigran."),
            ("Pot folosi o a doua cameră sau overlay pe Premium.Chat?", "Da — compune scena în SplitCam (a doua cameră, overlay-uri, filtre) și Premium.Chat vede un singur webcam. Folosește cu moderație în 1-on-1."),
            ("SplitCam e gratuit?", "Da — gratuit, fără filigran și fără limită de timp."),
        ],
        "steps": [
            ("Descarcă și instalează SplitCam", "SplitCam e software gratuit de live-streaming pentru Windows și macOS — fără înregistrare, fără card, fără filigran. Instalează o cameră virtuală pe care o poate folosi browserul."),
            ("Configurează scena pentru apeluri", "Deschide SplitCam, adaugă webcam-ul, pune-ți lumina, eventual adaugă un fundal AI sau un overlay discret. Păstrează încadrarea curată — e un apel plătit, nu o scenă."),
            ("Setează tariful pe Premium.Chat", "Loghează-te pe Premium.Chat, setează tariful per minut pentru apeluri video și copiază linkul tău personal. Distribuie-l pe rețele sociale sau în bio."),
            ("Acceptă apelul video", "Când un client plătește pentru timp, vine cererea de apel. Acceptă din dashboardul Premium.Chat."),
            ("Alege SplitCam drept cameră", "În meniul cu iconița de cameră al ferestrei de apel, schimbă de pe webcam-ul integrat pe <strong>SplitCam</strong>. Scena ta compusă ajunge acum la apelant."),
        ],
    },
    {
        "slug": "arousr", "name": "Arousr",
        "title": "Cum folosești SplitCam pe Arousr — sexting și apel video",
        "desc": "Folosește SplitCam gratuit drept cameră virtuală pe apelurile video Arousr — scene multi-cameră, overlay-uri și filtre pentru sexting plătit.",
        "kw": "cum folosești splitcam pe arousr, arousr apel video, arousr cameră virtuală, arousr cam girl, arousr model, platformă sexting splitcam, arousr live, arousr broadcast",
        "h1html": 'Cum folosești SplitCam pe <span class="accent">Arousr</span>',
        "h1short": "Arousr cu SplitCam",
        "card": "Folosește SplitCam drept cameră virtuală pentru apeluri video Arousr.",
        "intro": "Arousr e o platformă plătită de <strong>sexting + voce + apel video</strong> — clienții cumpără credite ca să scrie, să vorbească sau să facă apel video cu modelele, iar tu ești plătit pe sesiune. Partea de video rulează în browser (sau în aplicația mobilă Arousr pe telefoane), ceea ce înseamnă că <strong style='color:var(--text)'>SplitCam</strong> gratuit se conectează drept <strong>cameră virtuală</strong> pe desktop: scene multi-cameră, overlay-uri, filtre de lumină și un fundal AI ajung direct la client.",
        "quick": "Folosește SplitCam pe Arousr: instalezi SplitCam, construiești scena, accepți o cerere de video Arousr, iar în selectorul de cameră alegi <em>SplitCam</em>."
                 "<ol><li>Instalează SplitCam.</li><li>Configurează scena + lumina.</li>"
                 "<li>Setează tarifele de sexting/video pe Arousr.</li><li>Acceptă cererea video.</li>"
                 "<li>Alege SplitCam din dropdown-ul de cameră.</li></ol>",
        "key_how": "Partea de video web Arousr rulează în browser. SplitCam instalează un webcam virtual numit <strong>„SplitCam Video Driver”</strong> — când începe o sesiune video în dashboardul Arousr, schimbă camera din fereastra sesiunii pe <strong>SplitCam</strong>. Scena compusă (cameră + overlay-uri + filtre) devine ceea ce vede clientul. În aplicația mobilă Arousr, camerele virtuale nu sunt disponibile — folosește acolo o cameră reală de telefon și rezervă SplitCam pentru sesiunile de pe desktop.",
        "tips": [
            ("Sesiunile sunt plătite la timp", "Clienții cumpără credite per minut (sau per mesaj pentru text). Video îngrijit — lumină bună, fundal AI, beauty filter — se amortizează prin sesiuni mai lungi."),
            ("Sexting întâi, upsell la video", "Cea mai mare parte din venitul Arousr e text. Un scurt preview video în timpul unui chat de sexting face upsell la o sesiune video completă — acolo intră tariful per minut."),
            ("Sesiuni în app mobile ≠ desktop", "Camerele virtuale funcționează în video-ul din browser pe desktop. Aplicația mobilă Arousr folosește direct camera telefonului — același flux, alt instrument."),
            _T_TEST,
        ],
        "faq": [
            ("Cum se conectează SplitCam la Arousr?", "Drept cameră virtuală. Apelurile video Arousr rulează în browser pe desktop — alege SplitCam din selectorul de cameră. Nu e nevoie de stream key."),
            ("Arousr suportă OBS?", "Arousr e bazat pe browser, deci OBS se conectează la fel ca SplitCam — prin cameră virtuală. SplitCam e opțiunea gratuită, fără filigran."),
            ("Pot folosi overlay-uri într-o sesiune de sexting + video?", "Da — compune scena în SplitCam (lumină, overlay, a doua cameră) și Arousr vede un singur webcam. Păstrează overlay-urile discrete în 1-on-1."),
            ("SplitCam e gratuit pentru Arousr?", "Da — gratuit, fără filigran și fără limită de timp."),
        ],
        "steps": [
            ("Descarcă și instalează SplitCam", "SplitCam e software gratuit de live-streaming pentru Windows și macOS — fără înregistrare, fără card, fără filigran. Instalează o cameră virtuală pe care o poate alege browserul."),
            ("Construiește scena", "Deschide SplitCam, adaugă webcam-ul, ajustează lumina, adaugă opțional un fundal AI sau un beauty filter. Păstrează un ton intim — e o sesiune 1-on-1 plătită, nu o scenă publică."),
            ("Setează tarifele pe Arousr", "Loghează-te pe Arousr, setează tariful per mesaj și tariful video per minut și asigură-te că profilul tău e aprobat ca să poată intra cereri."),
            ("Acceptă cererea video", "Când un client inițiază o sesiune video din sexting sau direct, acceptă din dashboardul Arousr."),
            ("Alege SplitCam drept cameră", "În dropdown-ul de cameră al ferestrei de sesiune, schimbă de pe webcam-ul integrat pe <strong>SplitCam</strong>. Scena ta compusă ajunge acum la client."),
        ],
    },
    {
        "slug": "cams-com", "name": "Cams.com",
        "title": "Cum transmiți pe Cams.com cu SplitCam (RTMP/OBS)",
        "desc": "Transmite pe Cams.com cu SplitCam gratuit prin RTMP — scene multi-cameră, overlay-uri și filtre. Acces la baza de cheltuitori AFF. Fără filigran.",
        "kw": "cum transmiți pe cams.com, cams.com obs, cams.com rtmp, cams.com model, cams.com broadcaster, cams.com stream key, adult friend finder cams, cams.com live, cams com model signup",
        "h1html": 'Cum transmiți pe <span class="accent">Cams.com</span> cu SplitCam',
        "h1short": "Transmisie Cams.com",
        "card": "SplitCam gratuit → stream RTMP spre rețeaua Cams.com / AFF.",
        "intro": "Cams.com e brațul cam al rețelei AdultFriendFinder — unul dintre cele mai vechi ecosisteme dating + cam online, cu o bază consistentă de <strong>membri care plătesc deja</strong> ce migrează din AFF, AmateurMatch și alte proprietăți FriendFinder. Modelele transmit din <strong>Model Center</strong>-ul Cams.com, care suportă atât broadcasterul din browser, cât și un <strong>encoder extern prin RTMP</strong>. <strong style='color:var(--text)'>SplitCam</strong> gratuit transmite prin RTMP pentru scene multi-cameră complete, overlay-uri și filtre — sau, în broadcasterul din browser, se înregistrează drept <strong>cameră virtuală</strong> pentru același rezultat.",
        "quick": "Transmisie pe Cams.com: instalezi SplitCam, construiești scena, iei URL-ul de server RTMP și stream key-ul Cams.com din Model Center, le lipești în SplitCam, apasă Go Live."
                 "<ol><li>Instalează SplitCam.</li><li>Adaugă cameră + scenă.</li>"
                 "<li>Copiază URL server + key din Model Center Cams.com → External Encoder.</li>"
                 "<li>Lipește în RTMP custom SplitCam.</li><li>Apasă Go Live.</li></ol>",
        "key_how": "Model Center-ul Cams.com are un tab <strong>External Encoder / OBS</strong> cu URL de server și stream key. Lipește ambele în <strong>Stream Settings → Custom RTMP</strong> din SplitCam; alege 3.500–5.000 Kbps la 1920×1080, 30 fps, keyframe la 2 secunde. Apasă <strong>Go Live</strong> în SplitCam, apoi pornește show-ul din Model Center. Dacă preferi broadcasterul din browser, alege <strong>SplitCam</strong> din dropdown-ul de cameră.",
        "tips": [
            ("Cross-trafic AFF = membri plătitori", "Cams.com aduce privitori din conturi AdultFriendFinder care au deja o metodă de plată salvată — diferit de o audiență fresh de signup. Conversia la private și tip-urile tind să fie mai mari."),
            ("Encoderul extern bate browserul", "RTMP din SplitCam îți dă bitrate curat și permite scene multi-cameră cu overlay-uri; broadcasterul din browser merge, dar limitează producția."),
            ("Folosește uneltele de private show", "Cams.com mizează pe sesiunile private/exclusive. Un meniu de tip-uri și un drum clar spre private (în overlay) ridică sensibil venitul per privitor."),
            _T_TEST,
        ],
        "faq": [
            ("Cams.com e același lucru cu AdultFriendFinder?", "Aceeași rețea-mamă. Cams.com e brandul de broadcasting cam; privitorii pot ajunge prin AFF, AmateurMatch și alte site-uri FriendFinder, ceea ce reprezintă o mare parte din traficul său."),
            ("De unde iau stream key-ul Cams.com?", "În Model Center-ul Cams.com, deschide tabul <em>External Encoder</em> sau <em>OBS</em> — vei vedea un URL de server și un stream key. Lipește ambele în câmpurile RTMP custom ale SplitCam."),
            ("Broadcaster din browser sau RTMP?", "RTMP (encoder extern) e preferat — bitrate stabil, scene SplitCam complete. Broadcasterul din browser merge ca fallback: alege SplitCam drept webcam."),
            ("SplitCam e gratuit pentru Cams.com?", "Da — SplitCam e gratuit, fără filigran și fără limită de timp."),
        ],
        "steps": [
            ("Descarcă și instalează SplitCam", "SplitCam e software gratuit de live-streaming pentru Windows și macOS — fără înregistrare, fără card, fără filigran."),
            ("Construiește scena", "Deschide SplitCam și adaugă webcam-ul. Pune deasupra overlay-uri, un meniu de tip-uri, o a doua cameră sau telefonul, filtre de beauty sau un fundal AI — totul live."),
            ("Obține URL + stream key Cams.com", "Loghează-te în Model Center-ul Cams.com, deschide tabul <strong>External Encoder / OBS</strong> și copiază <strong>URL-ul serverului</strong> și <strong>stream key-ul</strong>."),
            ("Conectează SplitCam la Cams.com", "În SplitCam → <strong>Stream Settings → Custom RTMP</strong>, lipește URL-ul și cheia. Setează 3.500–5.000 Kbps la 1920×1080, 30 fps, keyframe la 2 secunde."),
            ("Apasă Go Live", "Apasă <strong>Go Live</strong> în SplitCam, apoi treci online din Model Center. Stream-ul tău aterizează în rețeaua Cams.com / AFF în ~10 secunde."),
        ],
    },
    {
        "slug": "stripcamfun", "name": "StripCamFun",
        "title": "Cum transmiți pe StripCamFun cu SplitCam (RTMP/OBS)",
        "desc": "Transmite pe StripCamFun cu SplitCam gratuit prin RTMP — scene multi-cameră, overlay-uri și filtre pentru o audiență indie. Fără filigran.",
        "kw": "cum transmiți pe stripcamfun, stripcamfun obs, stripcamfun rtmp, stripcamfun model, stripcamfun broadcast, strip cam fun model signup, stripcamfun stream key, site cam indie obs",
        "h1html": 'Cum transmiți pe <span class="accent">StripCamFun</span> cu SplitCam',
        "h1short": "Transmisie StripCamFun",
        "card": "SplitCam gratuit → transmisie RTMP/OBS spre StripCamFun.",
        "intro": "StripCamFun e un site live-cam independent — mai mic decât giganții de nivel Chaturbate, dar cu o audiență reală, mai puțin saturată, și sensibil mai puțină concurență pe nișă între broadcasteri. Modelele transmit din panoul de model StripCamFun, care expune o opțiune de <strong>encoder extern / RTMP</strong>. <strong style='color:var(--text)'>SplitCam</strong> gratuit se conectează prin RTMP pentru scene multi-cameră complete, overlay-uri și filtre — iar acolo unde e oferit un broadcaster din browser, SplitCam se înregistrează și ca <strong>cameră virtuală</strong>.",
        "quick": "Transmisie pe StripCamFun: instalezi SplitCam, construiești scena, copiezi URL-ul de server StripCamFun și stream key-ul, le lipești în setările RTMP ale SplitCam, apasă Go Live."
                 "<ol><li>Instalează SplitCam.</li><li>Adaugă cameră + scenă.</li>"
                 "<li>Copiază URL + stream key din panoul de model StripCamFun → External Encoder.</li>"
                 "<li>Lipește în RTMP custom SplitCam.</li><li>Apasă Go Live.</li></ol>",
        "key_how": "Deschide dashboardul de model StripCamFun și secțiunea <strong>External Encoder / OBS</strong>. Copiază URL-ul serverului și stream key-ul în <strong>Stream Settings → Custom RTMP</strong> din SplitCam; setează 3.500–5.000 Kbps la 1920×1080, 30 fps, keyframe la 2 secunde. Apasă <strong>Go Live</strong> în SplitCam, apoi treci online din dashboard.",
        "tips": [
            ("Bazin mai mic, vizibilitate mai ușoară", "Pe un site Tier-1 ești unul din mii online; pe StripCamFun lista de broadcasteri e scurtă — o scenă SplitCam îngrijită iese în evidență mai repede pe homepage."),
            ("Cross-broadcast pentru reach", "Site-urile cam indie merg bine cu multi-streaming. Folosește SplitCam ca să transmiți simultan pe StripCamFun și pe un site mai mare, ca să prinzi tipperi din ambele bazine."),
            ("Mizează pe tagging-ul de nișă", "Audiențele indie caută după nișă mai mult decât după nume mare. Tag-uri specifice + un overlay de scenă care numește nișa atrag privitorii de pe listă."),
            _T_TEST,
        ],
        "faq": [
            ("De unde iau stream key-ul StripCamFun?", "În dashboardul de model, deschide tabul <em>External Encoder / OBS</em> — vei vedea un URL de server și un stream key. Lipește ambele în câmpurile RTMP custom ale SplitCam."),
            ("E sigur să transmiți pe StripCamFun?", "Ca pe orice site cam indie, verifică acordul de model și termenii de plată înainte să mergi live. Folosește un email real și validează-ți întâi metoda de payout."),
            ("Pot face multi-stream pe StripCamFun și alt site cam?", "Da — SplitCam poate trimite simultan către mai multe endpoint-uri RTMP custom. Verifică întâi regulile de exclusivitate ale fiecărui site."),
            ("SplitCam e gratuit pentru StripCamFun?", "Da — gratuit, fără filigran și fără limită de timp."),
        ],
        "steps": [
            ("Descarcă și instalează SplitCam", "SplitCam e software gratuit de live-streaming pentru Windows și macOS — fără înregistrare, fără card, fără filigran."),
            ("Construiește scena", "Deschide SplitCam și adaugă webcam-ul. Pune deasupra overlay-uri, un meniu de tip-uri, o a doua cameră sau telefonul, filtre de beauty sau un fundal AI — totul live."),
            ("Obține URL + stream key StripCamFun", "Loghează-te în dashboardul de model StripCamFun, deschide <strong>External Encoder / OBS</strong> și copiază <strong>URL-ul serverului</strong> și <strong>stream key-ul</strong>."),
            ("Conectează SplitCam la StripCamFun", "În SplitCam → <strong>Stream Settings → Custom RTMP</strong>, lipește URL-ul și cheia. Setează 3.500–5.000 Kbps la 1920×1080, 30 fps, keyframe la 2 secunde."),
            ("Apasă Go Live", "Apasă <strong>Go Live</strong> în SplitCam, apoi treci online în dashboardul StripCamFun. Stream-ul tău apare pe lista publică în ~10 secunde."),
        ],
    },
    {
        "slug": "mym-fans", "name": "MYM.fans",
        "title": "Cum intri live pe MYM.fans cu SplitCam — cameră virtuală",
        "desc": "Intră live pe MYM.fans (alternativa franceză la OnlyFans) cu SplitCam gratuit ca o cameră virtuală — scene, overlay-uri și filtre. Fără filigran.",
        "kw": "cum intri live pe mym, mym.fans live, mym fans cameră virtuală, mym creator, mym france, mym live stream, mym obs, mym fans broadcast, mym influencer",
        "h1html": 'Cum intri live pe <span class="accent">MYM.fans</span> cu SplitCam',
        "h1short": "Live pe MYM.fans",
        "card": "Folosește SplitCam ca o cameră virtuală pentru live-ul de pe MYM.fans.",
        "intro": "MYM.fans e cea mai mare platformă franceză de abonamente pentru creatori — răspunsul Franței la OnlyFans, cu abonamente, pay-per-view, tipping și o funcție <strong>live stream</strong> integrată pentru fani. Broadcasterul ei merge în browser, așa că prin conectarea <strong style='color:var(--text)'>SplitCam</strong> gratuit ca o <strong>cameră virtuală</strong> adaugi scene multi-cameră, overlay-uri și filtre peste webcam-ul standard. Dacă în Creator Dashboard apare o opțiune de external encoder, SplitCam se conectează în schimb prin RTMP.",
        "quick": "Intră live pe MYM.fans cu SplitCam: instalezi SplitCam, construiești scena, pornești o transmisie live pe MYM, iar în selectorul de cameră al broadcasterului alegi <em>SplitCam</em> — apoi intri live."
                 "<ol><li>Instalează SplitCam.</li><li>Adaugă cameră + scenă.</li>"
                 "<li>Pornește o transmisie live pe MYM.fans.</li>"
                 "<li>Alege SplitCam din lista de camere.</li>"
                 "<li>Apasă Go Live.</li></ol>",
        "key_how": "Live-ul MYM.fans merge în browser. Construiește scena în SplitCam — apare ca o webcam de sistem numită <strong>\"SplitCam Video Driver\"</strong> — apoi deschide broadcasterul live MYM și alege <strong>SplitCam</strong> în lista de camere. Dacă în Creator Dashboard apare o opțiune de <strong>stream key / external encoder</strong>, lipești cheia în câmpurile RTMP custom ale SplitCam.",
        "tips": [
            ("Cea mai mare platformă franceză pentru creatori", "MYM e platforma #1 de fani în Franța, cu o audiență FR/EU obișnuită să plătească în EUR. O scenă SplitCam îngrijită cu overlay-uri în franceză convertește mai bine decât o webcam plată."),
            ("Camera virtuală merge fără stream key", "Live-ul doar în browser primește tot scena ta SplitCam — a doua cameră, overlay-uri, filtre de beauty sau fundal AI — doar selectând SplitCam ca webcam."),
            ("Cross-sell PPV în timpul live-ului", "MYM e construită în jurul conținutului plătit. Overlay-urile pe ecran care îți promovează abonamentul sau deblochează mesajele PPV transformă privitorii live în abonați plătitori."),
            _T_TEST,
        ],
        "faq": [
            ("Cum se conectează SplitCam la MYM.fans?", "Live-ul MYM e în browser, deci SplitCam se conectează ca o cameră virtuală — alegi SplitCam în selectorul de cameră. Nu e nevoie de stream key."),
            ("Pot folosi overlay-uri și mai multe camere pe MYM?", "Da — construiești scena în SplitCam (a doua cameră, overlay-uri, fundal AI); MYM vede scena finită ca o singură webcam."),
            ("MYM.fans suportă OBS sau encodere externe?", "Live-ul ei e în primul rând bazat pe browser / webcam. Dacă în dashboard apare o opțiune de stream key, o lipești în câmpurile RTMP custom ale SplitCam; altfel folosești metoda cu camera virtuală."),
            ("SplitCam e gratuit pentru MYM.fans?", "Da — SplitCam e gratuit, fără filigran și fără limită de timp."),
        ],
        "steps": [
            ("Descarcă și instalează SplitCam", "SplitCam e software gratuit de live-streaming pentru Windows și macOS — fără înregistrare, fără card, fără filigran. Instalează o cameră virtuală pe care browserul o poate selecta."),
            ("Construiește scena", "Deschide SplitCam și adaugă webcam-ul. Pune deasupra overlay-uri, text (în franceză dacă audiența ta e FR), o a doua cameră sau telefonul, filtre de beauty sau un fundal AI."),
            ("Pornește o transmisie live pe MYM.fans", "Loghează-te în contul tău de creator MYM și deschide broadcasterul live pentru a porni o transmisie pentru abonații tăi."),
            ("Alege SplitCam ca cameră", "În lista de camere a MYM, alegi <strong>SplitCam</strong> în loc de webcam-ul tău brut — scena ta compusă înlocuiește camera plată. (Sau, dacă e disponibilă, lipești o stream key în câmpurile RTMP custom ale SplitCam.)"),
            ("Apasă Go Live", "Pornește transmisia — scena ta SplitCam, overlay-urile și filtrele ajung la abonații tăi de pe MYM."),
        ],
    },
    {
        "slug": "fc2-live", "name": "FC2 Live",
        "title": "Cum transmiți pe FC2 Live cu SplitCam (RTMP/OBS)",
        "desc": "Transmite pe FC2 Live (cel mai mare site live-cam din Japonia) cu SplitCam gratuit prin RTMP — scene multi-cameră, overlay-uri și filtre. Fără filigran.",
        "kw": "cum transmiți pe fc2 live, fc2 live obs, fc2 live rtmp, fc2 live broadcast, fc2 live配信, fc2 live stream key, fc2 live model, fc2 live japonia, fc2 ライブ",
        "h1html": 'Cum transmiți pe <span class="accent">FC2 Live</span> cu SplitCam',
        "h1short": "Transmisie FC2 Live",
        "card": "SplitCam gratuit → transmisie RTMP/OBS spre FC2 Live.",
        "intro": "FC2 Live e cea mai mare platformă de live-streaming din Japonia — o bază uriașă de privitori, o secțiune adult dedicată și un flux separat de show-uri plătite care o transformă în una dintre cele mai profitabile piețe cam din Asia. Modelele transmit din panoul de broadcaster FC2, care suportă atât broadcasterul din browser, cât și un <strong>encoder extern prin RTMP</strong>. <strong style='color:var(--text)'>SplitCam</strong> gratuit transmite prin RTMP pentru scene multi-cameră complete, overlay-uri și filtre.",
        "quick": "Transmisie pe FC2 Live cu SplitCam: instalezi SplitCam, construiești scena, copiezi URL-ul de server și stream key-ul din panoul de broadcaster FC2, le lipești în setările RTMP ale SplitCam, apasă Go Live."
                 "<ol><li>Instalează SplitCam.</li><li>Adaugă cameră + scenă.</li>"
                 "<li>Copiază URL + stream key din panoul de broadcaster FC2.</li>"
                 "<li>Lipește în RTMP custom SplitCam.</li><li>Apasă Go Live.</li></ol>",
        "key_how": "Deschide panoul de broadcaster FC2 Live și treci pe <strong>External Encoder / RTMP</strong>. Copiază URL-ul serverului și stream key-ul în <strong>Stream Settings → Custom RTMP</strong> din SplitCam; setează 3.500–5.000 Kbps la 1920×1080, 30 fps, keyframe la 2 secunde. Apasă <strong>Go Live</strong> în SplitCam, apoi pornește show-ul din dashboardul FC2.",
        "tips": [
            ("Audiență japoneză uriașă", "FC2 e Tier 1 în Japonia — privitorii sunt locali, obișnuiți să plătească în JPY și înclină spre show-uri plătite mai lungi. Overlay-urile cu text în japoneză (de exemplu un meniu de tip-uri în 円 / JPY) cresc sensibil conversia."),
            ("Secțiunea adult e separată", "FC2 are atât live-uri generale, cât și adult. Setează corect categoria camerei înainte să intri live — show-urile adult nu pot fi descoperite din secțiunea generală."),
            ("Encoderul extern pentru bitrate stabil", "Audiența japoneză predominant mobilă e sensibilă la frame-urile pierdute. RTMP din SplitCam la 4 Mbps constant bate broadcasterul din browser ca fiabilitate."),
            _T_TEST,
        ],
        "faq": [
            ("De unde iau stream key-ul FC2 Live?", "În panoul de broadcaster FC2 Live, treci pe <em>External Encoder</em> sau <em>OBS</em> — vei vedea un URL de server și un stream key. Lipește ambele în câmpurile RTMP custom ale SplitCam."),
            ("Broadcaster din browser sau RTMP?", "RTMP (encoder extern) e preferat — bitrate stabil, scene SplitCam complete. Broadcasterul din browser merge ca fallback: alege SplitCam drept webcam."),
            ("Am nevoie de cont japonez ca să transmit pe FC2?", "E necesar un cont FC2, iar transmisia adult are pași suplimentari de verificare a vârstei pentru model. Urmează procesul de onboarding FC2."),
            ("SplitCam e gratuit pentru FC2 Live?", "Da — SplitCam e gratuit, fără filigran și fără limită de timp."),
        ],
        "steps": [
            ("Descarcă și instalează SplitCam", "SplitCam e software gratuit de live-streaming pentru Windows și macOS — fără înregistrare, fără card, fără filigran."),
            ("Construiește scena", "Deschide SplitCam și adaugă webcam-ul. Pune deasupra overlay-uri, un meniu de tip-uri în 円 (JPY), o a doua cameră sau telefonul, filtre de beauty sau un fundal AI — totul live."),
            ("Obține URL + stream key FC2 Live", "Loghează-te pe FC2, deschide panoul de broadcaster Live, treci pe <strong>External Encoder</strong> și copiază <strong>URL-ul serverului</strong> și <strong>stream key-ul</strong>."),
            ("Conectează SplitCam la FC2 Live", "În SplitCam → <strong>Stream Settings → Custom RTMP</strong>, lipește URL-ul și cheia. Setează 3.500–5.000 Kbps la 1920×1080, 30 fps, keyframe la 2 secunde."),
            ("Apasă Go Live", "Apasă <strong>Go Live</strong> în SplitCam, apoi pornește show-ul din dashboardul FC2. Stream-ul tău apare pe lista publică în ~10 secunde."),
        ],
    },
    {
        "slug": "boosty", "name": "Boosty",
        "title": "Cum intri live pe Boosty cu SplitCam — cameră virtuală",
        "desc": "Intră live pe Boosty (platforma rusă pentru creatori) cu SplitCam gratuit ca o cameră virtuală — scene, overlay-uri și filtre. Fără filigran.",
        "kw": "cum intri live pe boosty, boosty live, boosty stream, boosty cameră virtuală, boosty creator, бусти прямой эфир, boosty obs, boosty live plătit, boosty abonat",
        "h1html": 'Cum intri live pe <span class="accent">Boosty</span> cu SplitCam',
        "h1short": "Live pe Boosty",
        "card": "Folosește SplitCam ca o cameră virtuală pentru live-ul de pe Boosty.",
        "intro": "Boosty e cea mai mare platformă rusă de monetizare pentru creatori — un serviciu în stilul Patreon cu abonamente, postări plătite, tip-uri și o funcție <strong>live broadcast</strong>, cu o audiență de creatori care include atât creatori adult, cât și mainstream. Live-ul ei merge în browser, așa că prin conectarea <strong style='color:var(--text)'>SplitCam</strong> gratuit ca o <strong>cameră virtuală</strong> adaugi scene multi-cameră, overlay-uri și filtre pe care abonații nu le-ar primi dintr-o webcam plată.",
        "quick": "Intră live pe Boosty cu SplitCam: instalezi SplitCam, construiești scena, pornești o transmisie live pe Boosty și alegi <em>SplitCam</em> în lista de camere a broadcasterului — apoi intri live."
                 "<ol><li>Instalează SplitCam.</li><li>Adaugă cameră + scenă.</li>"
                 "<li>Pornește o transmisie live pe Boosty.</li>"
                 "<li>Alege SplitCam din lista de camere.</li>"
                 "<li>Apasă Go Live.</li></ol>",
        "key_how": "Live-ul Boosty merge în browser. Construiește scena în SplitCam — apare ca o webcam de sistem numită <strong>\"SplitCam Video Driver\"</strong> — apoi deschide broadcasterul live Boosty și alege <strong>SplitCam</strong> în lista de camere în loc de webcam-ul tău brut.",
        "tips": [
            ("Cea mai mare platformă rusă pentru creatori", "Boosty a înlocuit Patreon pentru mulți creatori RU după sancțiuni, așa că audiența e loială și obișnuită să plătească în RUB. O scenă SplitCam îngrijită cu overlay-uri în rusă convertește bine."),
            ("Show-uri live pe nivel de abonat", "Boosty îți permite să restricționezi transmisiile live pe nivel de abonament. SplitCam merge cu toate nivelurile — encoderului nu-i pasă pe ce nivel e privitorul, tu transmiți o singură dată și Boosty gestionează accesul."),
            ("Overlay de tip și pay-per-view", "Boosty suportă deblocări de postări plătite și tip-uri. Un overlay pe ecran care denumește beneficiile nivelului crește conversiile în timpul transmisiilor live."),
            _T_TEST,
        ],
        "faq": [
            ("Cum se conectează SplitCam la Boosty?", "Live-ul Boosty e în browser, deci SplitCam se conectează ca o cameră virtuală — alegi SplitCam în selectorul de cameră. Nu e nevoie de stream key."),
            ("Pot folosi overlay-uri pe un live Boosty?", "Da — compui scena în SplitCam (overlay-uri, a doua cameră, fundal AI); Boosty vede o singură webcam. Abonații primesc scena compusă completă."),
            ("Boosty suportă OBS sau encodere externe?", "Live-ul Boosty e în primul rând bazat pe browser. Dacă în panoul de creator apare o opțiune de stream key, o lipești în câmpurile RTMP custom ale SplitCam; altfel folosești metoda cu camera virtuală."),
            ("SplitCam e gratuit pentru Boosty?", "Da — SplitCam e gratuit, fără filigran și fără limită de timp."),
        ],
        "steps": [
            ("Descarcă și instalează SplitCam", "SplitCam e software gratuit de live-streaming pentru Windows și macOS — fără înregistrare, fără card, fără filigran. Instalează o cameră virtuală pe care browserul o poate selecta."),
            ("Construiește scena", "Deschide SplitCam și adaugă webcam-ul. Pune deasupra overlay-uri (în rusă, pentru audiența ta), o a doua cameră sau telefonul, filtre de beauty sau un fundal AI."),
            ("Pornește o transmisie live pe Boosty", "Loghează-te în contul tău de creator Boosty și deschide broadcasterul live. Setează restricția de nivel dacă vrei ca live-ul să fie după un nivel plătit."),
            ("Alege SplitCam ca cameră", "În lista de camere a Boosty, alegi <strong>SplitCam</strong> în loc de webcam-ul tău brut — scena ta compusă înlocuiește camera plată."),
            ("Apasă Go Live", "Pornește transmisia — scena ta SplitCam, overlay-urile și filtrele ajung la abonații tăi de pe Boosty."),
        ],
    },
    {
        "slug": "amateurcommunity", "name": "AmateurCommunity",
        "title": "Cum transmiți pe AmateurCommunity cu SplitCam (RTMP)",
        "desc": "Transmite pe AmateurCommunity (cel mai mare site cam amator din Germania) cu SplitCam gratuit prin RTMP — scene, overlay-uri și filtre. Fără filigran.",
        "kw": "cum transmiți pe amateurcommunity, amateurcommunity obs, amateurcommunity rtmp, amateur community deutschland, amateurcommunity model, ac community broadcast, amateurcommunity live, amateur cam deutschland",
        "h1html": 'Cum transmiți pe <span class="accent">AmateurCommunity</span> cu SplitCam',
        "h1short": "Transmisie AmateurCommunity",
        "card": "SplitCam gratuit → transmisie RTMP spre AmateurCommunity (DE).",
        "intro": "AmateurCommunity e cel mai mare site amator de cam și comunitate de conținut din Germania — funcționează încă de la începutul anilor 2000 cu o audiență germanofonă profund loială, obișnuită să plătească pentru conținut și show-uri live. Modelele transmit din panoul de model AC, care suportă atât un <strong>encoder extern prin RTMP</strong>, cât și broadcasterul din browser. <strong style='color:var(--text)'>SplitCam</strong> gratuit transmite prin RTMP pentru scene multi-cameră complete, overlay-uri și filtre — overlay-urile în germană vorbesc direct audienței locale.",
        "quick": "Transmisie pe AmateurCommunity: instalezi SplitCam, construiești scena, copiezi URL-ul de server AC și stream key-ul din panoul de model, le lipești în setările RTMP ale SplitCam, apasă Go Live."
                 "<ol><li>Instalează SplitCam.</li><li>Adaugă cameră + scenă.</li>"
                 "<li>Copiază URL + stream key din panoul de model AC.</li>"
                 "<li>Lipește în RTMP custom SplitCam.</li><li>Apasă Go Live.</li></ol>",
        "key_how": "Deschide panoul de model AmateurCommunity și tabul <strong>External Encoder / OBS</strong>. Copiază URL-ul serverului și stream key-ul în <strong>Stream Settings → Custom RTMP</strong> din SplitCam; setează 3.500–5.000 Kbps la 1920×1080, 30 fps, keyframe la 2 secunde. Apasă <strong>Go Live</strong> în SplitCam, apoi treci online din panou.",
        "tips": [
            ("Audiență germanofonă care plătește în germană", "Audiența AmateurCommunity e covârșitor DACH (DE/AT/CH) și plătește în EUR — overlay-urile, meniul de tip-uri și chatul live în germană convertesc sensibil mai bine decât în engleză."),
            ("Combo PPV premium + live", "AC îți permite să vinzi conținut PPV alături de live. Un show live care teasează PPV-ul (cu un overlay pe ecran) tinde să crească vânzările PPV în timpul și după transmisie."),
            ("Encoder extern pentru calitate stabilă", "Audiența AC așteaptă producție înaltă; RTMP la 4 Mbps constant din SplitCam bate bitrate-ul variabil al broadcasterului din browser."),
            _T_TEST,
        ],
        "faq": [
            ("De unde iau stream key-ul AmateurCommunity?", "În panoul de model AC, deschide tabul <em>External Encoder</em> sau <em>OBS</em> — vei vedea un URL de server și un stream key. Lipește ambele în câmpurile RTMP custom ale SplitCam."),
            ("Broadcaster din browser sau RTMP?", "RTMP (encoder extern) e preferat pentru modele serioase — bitrate stabil, scene SplitCam complete. Broadcasterul din browser merge ca fallback: alege SplitCam drept webcam."),
            ("Trebuie să fiu în Germania ca să transmit pe AC?", "Nu, dar audiența e germanofonă. Modelele de oriunde se pot înregistra — pasul principal e trecerea verificării de model + a formularelor fiscale."),
            ("SplitCam e gratuit pentru AmateurCommunity?", "Da — SplitCam e gratuit, fără filigran și fără limită de timp."),
        ],
        "steps": [
            ("Descarcă și instalează SplitCam", "SplitCam e software gratuit de live-streaming pentru Windows și macOS — fără înregistrare, fără card, fără filigran."),
            ("Construiește scena", "Deschide SplitCam și adaugă webcam-ul. Pune deasupra overlay-uri (în germană — \"Trinkgeld\" / \"PPV freischalten\"), o a doua cameră sau telefonul, filtre de beauty sau un fundal AI — totul live."),
            ("Obține URL + stream key AmateurCommunity", "Loghează-te în panoul de model AC, deschide <strong>External Encoder / OBS</strong> și copiază <strong>URL-ul serverului</strong> și <strong>stream key-ul</strong>."),
            ("Conectează SplitCam la AmateurCommunity", "În SplitCam → <strong>Stream Settings → Custom RTMP</strong>, lipește URL-ul și cheia. Setează 3.500–5.000 Kbps la 1920×1080, 30 fps, keyframe la 2 secunde."),
            ("Apasă Go Live", "Apasă <strong>Go Live</strong> în SplitCam, apoi treci online în panoul de model AC. Stream-ul tău apare pe lista publică în ~10 secunde."),
        ],
    },
    {
        "slug": "myfans-jp", "name": "MyFans.jp",
        "title": "Cum intri live pe MyFans.jp cu SplitCam — cameră virtuală",
        "desc": "Intră live pe MyFans.jp (OnlyFans-ul japonez) cu SplitCam gratuit ca o cameră virtuală — scene multi-cameră, overlay-uri, filtre. Fără filigran.",
        "kw": "cum intri live pe myfans, myfans.jp live, myfans 配信, myfans cameră virtuală, myfans creator, マイファンズ, myfans japonia, myfans broadcast, myfans abonat",
        "h1html": 'Cum intri live pe <span class="accent">MyFans.jp</span> cu SplitCam',
        "h1short": "Live pe MyFans.jp",
        "card": "Folosește SplitCam ca o cameră virtuală pentru live-ul de pe MyFans.jp.",
        "intro": "MyFans.jp e platforma japoneză de top pentru abonamente la creatori — răspunsul Japoniei la OnlyFans, cu abonamente, pay-per-view, tip-uri (投げ銭) și o funcție <strong>live stream</strong> încorporată pentru fani. Broadcasterul ei merge în browser, așa că, îndreptând <strong style='color:var(--text)'>SplitCam</strong> gratuit spre MyFans ca o <strong>cameră virtuală</strong>, adaugi scene multi-cameră, overlay-uri și filtre pe care o webcam plată nu le poate livra. Dacă în dashboardul tău de creator apare opțiunea de encoder extern, SplitCam se poate conecta și prin RTMP.",
        "quick": "Intră live pe MyFans.jp cu SplitCam: instalezi SplitCam, construiești scena, pornești un live pe MyFans și în selectorul de cameră al broadcasterului alegi <em>SplitCam</em> — apoi intri live."
                 "<ol><li>Instalează SplitCam.</li><li>Adaugă cameră + scenă.</li>"
                 "<li>Pornește un live pe MyFans.jp.</li>"
                 "<li>Alege SplitCam din lista de camere.</li>"
                 "<li>Apasă Go Live.</li></ol>",
        "key_how": "Live-ul MyFans.jp merge în browser. Construiește scena în SplitCam — apare ca o webcam de sistem numită <strong>\"SplitCam Video Driver\"</strong> — apoi deschide broadcasterul live MyFans și alege <strong>SplitCam</strong> în lista de camere. Dacă în dashboardul tău de creator apare o opțiune de <strong>stream key / encoder extern</strong>, lipește-o în câmpurile RTMP custom ale SplitCam.",
        "tips": [
            ("Cea mai mare fan-platformă din Japonia", "MyFans e #1 între platformele de abonament pentru creatori din Japonia, cu o audiență JP-nativă care plătește în 円 (JPY). Overlay-urile în japoneză și o scenă SplitCam îngrijită convertesc mult mai bine decât o webcam plată."),
            ("Cameră virtuală, fără stream key", "Live-ul doar din browser primește totuși scena ta SplitCam completă — a doua cameră, overlay-uri, filtre de beauty sau fundal AI — alegând SplitCam ca webcam."),
            ("Cross-sell PPV în timpul live-ului", "MyFans e construită în jurul 投げ銭 (tip-uri) și al postărilor plătite. Un overlay pe ecran care denumește pachetul PPV sau ținta de tip-uri crește sensibil veniturile în timpul unui live."),
            _T_TEST,
        ],
        "faq": [
            ("Cum se conectează SplitCam la MyFans.jp?", "Live-ul MyFans e în browser, deci SplitCam se conectează ca o cameră virtuală — alegi SplitCam în selectorul de cameră. Nu e nevoie de stream key."),
            ("Pot folosi overlay-uri și mai multe camere pe MyFans?", "Da — compui scena în SplitCam (a doua cameră, overlay-uri, fundal AI); MyFans vede scena finală ca pe o singură webcam."),
            ("MyFans.jp suportă OBS sau encodere externe?", "Live-ul ei e în primul rând bazat pe browser/webcam. Dacă în dashboard apare o opțiune de stream key, o lipești în câmpurile RTMP custom ale SplitCam; altfel folosești metoda cu camera virtuală."),
            ("SplitCam e gratuit pentru MyFans.jp?", "Da — SplitCam e gratuit, fără filigran și fără limită de timp."),
        ],
        "steps": [
            ("Descarcă și instalează SplitCam", "SplitCam e software gratuit de live-streaming pentru Windows și macOS — fără înregistrare, fără card, fără filigran. Instalează o cameră virtuală pe care browserul o poate selecta."),
            ("Construiește scena", "Deschide SplitCam și adaugă webcam-ul. Pune deasupra overlay-uri (în japoneză — 「投げ銭」「PPV解放」 pentru audiența ta), o a doua cameră sau telefonul, filtre de beauty sau un fundal AI."),
            ("Pornește un live pe MyFans.jp", "Loghează-te în contul tău de creator MyFans și deschide broadcasterul live (配信) ca să pornești o transmisie pentru abonații tăi."),
            ("Alege SplitCam ca cameră", "În lista de camere a MyFans, alegi <strong>SplitCam</strong> în loc de webcam-ul tău brut — scena ta compusă înlocuiește camera plată. (Sau lipești un stream key în câmpurile RTMP custom ale SplitCam, dacă e disponibil.)"),
            ("Apasă Go Live", "Pornește transmisia — scena ta SplitCam, overlay-urile și filtrele ajung la abonații tăi de pe MyFans."),
        ],
    },
    {
        "slug": "privacy-com-br", "name": "Privacy.com.br",
        "title": "Cum intri live pe Privacy.com.br cu SplitCam",
        "desc": "Intră ao vivo pe Privacy.com.br (OnlyFans-ul Braziliei) cu SplitCam gratuit ca o cameră virtuală — scene multi-cameră, overlay-uri, filtre. Fără filigran.",
        "kw": "cum intri live pe privacy, privacy.com.br ao vivo, privacy live, privacy brasil, privacy cameră virtuală, privacy creator, privacy broadcast, privacy br criadora, privacy assinante",
        "h1html": 'Cum intri live pe <span class="accent">Privacy.com.br</span> cu SplitCam',
        "h1short": "Live pe Privacy.com.br",
        "card": "Folosește SplitCam ca o cameră virtuală pentru ao vivo pe Privacy.com.br.",
        "intro": "Privacy.com.br e platforma braziliană de top pentru abonamente la creatori — răspunsul Braziliei la OnlyFans, cu assinaturas, pay-per-view, gorjetas și o funcție <strong>ao vivo</strong> (live stream) încorporată pentru fãs. Broadcasterul ei merge în browser, așa că, îndreptând <strong style='color:var(--text)'>SplitCam</strong> gratuit spre Privacy ca o <strong>cameră virtuală</strong>, adaugi scene multi-cameră, overlay-uri și filtre pe care o webcam plată nu le poate livra. Dacă în dashboardul tău de creator apare opțiunea de encoder extern, SplitCam se poate conecta și prin RTMP.",
        "quick": "Intră live pe Privacy.com.br cu SplitCam: instalezi SplitCam, construiești scena, pornești un ao vivo pe Privacy și în selectorul de cameră al broadcasterului alegi <em>SplitCam</em> — apoi intri live."
                 "<ol><li>Instalează SplitCam.</li><li>Adaugă cameră + scenă.</li>"
                 "<li>Pornește un ao vivo pe Privacy.com.br.</li>"
                 "<li>Alege SplitCam din lista de camere.</li>"
                 "<li>Apasă Go Live.</li></ol>",
        "key_how": "Ao vivo de pe Privacy.com.br merge în browser. Construiește scena în SplitCam — apare ca o webcam de sistem numită <strong>\"SplitCam Video Driver\"</strong> — apoi deschide broadcasterul live Privacy și alege <strong>SplitCam</strong> în lista de camere. Dacă apare o opțiune de <strong>stream key / encoder extern</strong>, o lipești în câmpurile RTMP custom ale SplitCam.",
        "tips": [
            ("Cea mai mare fan-platformă din Brazilia", "Privacy e #1 între platformele de abonament pentru creatori din Brazilia, cu o audiență vorbitoare de portugheză obișnuită să plătească în BRL prin PIX. Overlay-urile în portugheză plus o scenă SplitCam îngrijită convertesc mult mai bine decât o webcam plată."),
            ("Cameră virtuală, fără stream key", "Live-ul doar din browser primește totuși scena ta SplitCam completă — a doua cameră, overlay-uri, filtre de beauty sau fundal AI — alegând SplitCam ca webcam."),
            ("Meniuri de tip + PPV în timpul ao vivo", "Privacy suportă gorjetas (tip-uri) și postări plătite. Un overlay pe ecran care denumește pachetul PPV sau meta-de-gorjeta crește veniturile în timpul unui live."),
            _T_TEST,
        ],
        "faq": [
            ("Cum se conectează SplitCam la Privacy.com.br?", "Ao vivo de pe Privacy e în browser, deci SplitCam se conectează ca o cameră virtuală — alegi SplitCam în selectorul de cameră. Nu e nevoie de stream key."),
            ("Pot folosi overlay-uri și mai multe camere pe Privacy?", "Da — compui scena în SplitCam (a doua cameră, overlay-uri, fundal AI); Privacy vede scena finală ca pe o singură webcam."),
            ("Privacy.com.br suportă OBS sau encodere externe?", "Ao vivo de pe ea e în primul rând bazat pe browser/webcam. Dacă în dashboard apare o opțiune de stream key, o lipești în câmpurile RTMP custom ale SplitCam; altfel folosești metoda cu camera virtuală."),
            ("SplitCam e gratuit pentru Privacy.com.br?", "Da — SplitCam e gratuit, fără filigran și fără limită de timp."),
        ],
        "steps": [
            ("Descarcă și instalează SplitCam", "SplitCam e software gratuit de live-streaming pentru Windows și macOS — fără înregistrare, fără card, fără filigran. Instalează o cameră virtuală pe care browserul o poate selecta."),
            ("Construiește scena", "Deschide SplitCam și adaugă webcam-ul. Pune deasupra overlay-uri în portugheză (\"gorjeta\", \"desbloquear PPV\"), o a doua cameră sau telefonul, filtre de beauty sau un fundal AI."),
            ("Pornește un ao vivo pe Privacy.com.br", "Loghează-te în contul tău de creator Privacy și deschide broadcasterul de ao vivo ca să pornești un live pentru abonații tăi."),
            ("Alege SplitCam ca cameră", "În lista de camere a Privacy, alegi <strong>SplitCam</strong> în loc de webcam-ul tău brut — scena ta compusă înlocuiește camera plată. (Sau lipești un stream key în câmpurile RTMP custom ale SplitCam, dacă e disponibil.)"),
            ("Apasă Go Live", "Pornește transmisia — scena ta SplitCam, overlay-urile și filtrele ajung la abonații tăi de pe Privacy.com.br."),
        ],
    },
]
