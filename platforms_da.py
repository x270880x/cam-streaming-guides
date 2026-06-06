# -*- coding: utf-8 -*-
"""Danish (da) content for cam-streaming-guides."""

_T_ETH = ("Brug kabelforbindelse", "Ethernet slår Wi-Fi i en lang stream — en mistet frame er "
          "en mistet tip. Træk et kabel til stream-pc'en.")
_T_TEST = ("Lav først en privat test", "Kør en kort testudsendelse for kamera, lyd, framing "
           "og overlays, før du åbner rummet for publikum.")

PLATFORMS_DA = [
    {"slug": "chaturbate", "name": "Chaturbate",
     "title": "Udsend på Chaturbate med SplitCam — Token & RTMP",
     "desc": "Udsend på Chaturbate med gratis SplitCam — broadcast token, RTMP, multi-kamera scener og overlays. Intet vandmærke.",
     "kw": "chaturbate udsend, chaturbate broadcast token, chaturbate rtmp obs, chaturbate external encoder, chaturbate live",
     "h1html": 'Sådan udsender du på <span class="accent">Chaturbate</span> med SplitCam',
     "h1short": "Udsend Chaturbate",
     "card": "Token-baseret opsætning med ekstern encoder på Chaturbate.",
     "intro": "Chaturbate er en af de største cam-platforme, bygget på token-økonomi. Browser-broadcasteren er et fladt et-kameras værktøj — at skifte til <strong style='color:var(--text)'>ekstern encoder</strong> med gratis <strong style='color:var(--text)'>SplitCam</strong> åbner multi-kamera scener, overlays og filtre på samme token-baserede stream.",
     "quick": "Udsend på Chaturbate med SplitCam: installér SplitCam, byg scenen, på Chaturbate åbn <em>Broadcast Yourself → My Broadcast</em>, kopiér broadcast token, indsæt i SplitCam, Go Live."
              "<ol><li>Installér SplitCam.</li><li>Tilføj kamera + scene.</li>"
              "<li>Kopiér broadcast token fra Chaturbate.</li><li>Indsæt i SplitCam.</li>"
              "<li>Tryk Go Live.</li></ol>",
     "key_how": "På Chaturbate klik <strong>Broadcast Yourself</strong> for siden <strong>My Broadcast</strong>, derefter <strong>View RTMP/OBS broadcast information and stream key</strong>. Nøglen vises som <strong>broadcast token</strong> — kopiér. Behandl som adgangskode; aldrig offentligt.",
     "tips": [
         ("Token er nøglen", "Chaturbate bruger din broadcast token i stedet for en generisk stream key. Behandl som adgangskode og nulstil ved lækage."),
         ("Meget plads", "Chaturbate's RTMP ingest accepterer op til 4K, 60 fps og høj bitrate — grænsen er dit upload, ikke platformen. Keyframe hver 2 sekunder."),
         _T_ETH, _T_TEST,
     ],
     "faq": [
         ("Tillader Chaturbate OBS / eksterne encodere?", "Ja — Chaturbate understøtter eksterne encodere officielt med sin egen «How do I set up OBS?» artikel. Aktivér med «Use External Encoder to Broadcast» i broadcast-indstillingerne."),
         ("Hvor er min Chaturbate stream key?", "Broadcast Yourself → My Broadcast → View RTMP/OBS broadcast information and stream key. Nøglen er din broadcast token."),
         ("Hvilken bitrate til Chaturbate?", "3.500–6.000 Kbps ved 1080p er rigeligt. Chaturbate's loft er højt — den reelle grænse er dit upload; kør først SplitCam's hastighedstest."),
         ("Er SplitCam gratis til Chaturbate?", "Ja — helt gratis, uden vandmærke og uden tidsbegrænsning: encoderen spiser ikke dine token-indtægter."),
     ]},
    {"slug": "cam4", "name": "CAM4",
     "title": "Udsend på CAM4 med SplitCam — External Encoder",
     "desc": "Udsend på CAM4 med gratis SplitCam — External Encoder, stream key, geo-blokering og overlays. Intet vandmærke.",
     "kw": "cam4 udsend, cam4.com, cam4 external encoder, cam4 stream key, cam4 rtmp obs",
     "h1html": 'Sådan udsender du på <span class="accent">CAM4</span> med SplitCam',
     "h1short": "Udsend CAM4",
     "card": "External Encoder på CAM4 med geo-kontroller.",
     "intro": "CAM4 er en global cam-and-earn-platform med indbyggede geo-kontroller — du kan skjule udsendelsen i udvalgte lande. Udsendelse via gratis <strong style='color:var(--text)'>SplitCam</strong> som ekstern encoder åbner sceneskift og overlays, som basis-broadcasteren ikke gør.",
     "quick": "Udsend på CAM4 med SplitCam: installér SplitCam, byg scenen, på CAM4 gå til <em>Broadcast &amp; Earn Money → Start Broadcast → External Encoder</em>, Get Stream Key, indsæt i SplitCam, Go Live."
              "<ol><li>Installér SplitCam.</li><li>Tilføj kamera + scene.</li>"
              "<li>Hent stream key fra CAM4.</li><li>Indsæt i SplitCam.</li>"
              "<li>Tryk Go Live.</li></ol>",
     "key_how": "På CAM4 klik <strong>Broadcast</strong> → <strong>Broadcast &amp; Earn Money</strong> → <strong>Start Broadcast</strong>, derefter <strong>External Encoder</strong> øverst. Udfyld fødselsdato, køn og land, brug <strong>Get Stream Key</strong> og kopiér. En grøn slider i SplitCam's Stream Settings bekræfter forbindelsen.",
     "tips": [
         ("Indstil geo-restriktioner", "CAM4 tillader skjul af udsendelsen i specifikke lande og regioner — opsæt på CAM4-siden før go-live."),
         ("Følg den grønne slider", "CAM4's opsætning viser en grøn slider i SplitCam's Stream Settings, når nøglen er accepteret — rød = tjek nøglen."),
         ("Lavere bitrate end normalt", "CAM4's ingest begrænser video-bitrate til omkring 3.000 Kbps — lavere end de fleste cam-sites. Tving ikke højere."),
         _T_ETH,
     ],
     "faq": [
         ("Understøtter CAM4 OBS / eksterne encodere officielt?", "Ja — CAM4 har en officiel OBS Guide på support-sitet og anbefaler External Encoder til den bedste oplevelse. SplitCam bruger samme RTMP-rute."),
         ("Kan jeg geo-blokere min CAM4-stream?", "Ja — CAM4 har indbygget geo-begrænsning til at skjule udsendelsen i visse lande. Indstil på CAM4, ikke i SplitCam."),
         ("Hvor er CAM4's stream key?", "Broadcast → Broadcast & Earn Money → Start Broadcast → External Encoder → Get Stream Key."),
         ("Hvilken bitrate til CAM4?", "Lavere end gennemsnittet — CAM4's ingest begrænser ved ~3.000 Kbps ved 30 fps med 1-sekunds keyframe. Den officielle tabel anbefaler ikke at overskride ~3.000."),
     ]},
    {"slug": "bongacams", "name": "BongaCams",
     "title": "Udsend på BongaCams med SplitCam — External Encoder",
     "desc": "Udsend på BongaCams med gratis SplitCam — External Encoder, multi-kamera scener, overlays og AI-baggrund. Intet vandmærke.",
     "kw": "bongacams, bongcams, bongacams udsend, bongacams external encoder, bongacams rtmp obs",
     "h1html": 'Sådan udsender du på <span class="accent">BongaCams</span> med SplitCam',
     "h1short": "Udsend BongaCams",
     "card": "External Encoder-opsætning til BongaCams.",
     "intro": "BongaCams er en global cam-platform. Ekstern encoder-udsendelse er ikke altid aktiveret — når aktiveret, fører gratis <strong style='color:var(--text)'>SplitCam</strong> udsendelsen med multi-kamera scener, overlays og AI-baggrund.",
     "quick": "Udsend på BongaCams med SplitCam: installér SplitCam, byg scenen, på BongaCams gå til <em>Options → Broadcast settings → Select Encoder → External Encoder</em>, kopiér URL og nøgle, indsæt i SplitCam, Go Live."
              "<ol><li>Installér SplitCam.</li><li>Tilføj kamera + scene.</li>"
              "<li>Hent URL og nøgle fra BongaCams.</li><li>Indsæt i SplitCam.</li>"
              "<li>Tryk Go Live.</li></ol>",
     "key_how": "På BongaCams åbn <strong>Options</strong> → <strong>Broadcast settings</strong> → <strong>Select Encoder</strong> → <strong>External Encoder</strong> og kopiér den viste server-URL og stream key. <strong>Hvis External Encoder-knappen mangler</strong>, kontakt BongaCams-support og bed om aktivering af ekstern kodning på din konto.",
     "tips": [
         ("Ingen External Encoder-knap? Support", "BongaCams aktiverer ekstern kodning per konto — hvis muligheden mangler i Broadcast settings, aktiverer supporten den."),
         ("Match opløsningen", "BongaCams anbefaler, at webkameraets opløsning og udsendelsens opløsning matcher — fx begge 1280×720."),
         _T_ETH, _T_TEST,
     ],
     "faq": [
         ("Hvorfor vises External Encoder-knappen ikke på BongaCams?", "Ekstern kodning er ikke aktiv som standard på hver konto — kontakt BongaCams-support for at aktivere den, og knappen vises i Broadcast settings."),
         ("Skal jeg verificere min BongaCams-konto?", "Ja — udsendelse kræver 18+, officielt ID til aldersverificering og konto-godkendelse før live."),
         ("Hvilken bitrate til BongaCams?", "BongaCams' RTMP ingest begrænser video-bitrate til omkring 6.000 Kbps med 2-sekunds keyframe — 3.500–6.000 ved 1080p er den ideelle zone; test upload først."),
         ("Er SplitCam gratis til BongaCams?", "Ja — helt gratis, uden vandmærke og uden tidsbegrænsning, så encoderen ikke reducerer dine token-indtægter på BongaCams."),
     ]},
    {"slug": "stripchat", "name": "Stripchat",
     "title": "Udsend på Stripchat med SplitCam — Strip Cam Setup",
     "desc": "Udsend på Stripchat — strip cam-platformen — med gratis SplitCam. Ekstern software, token-nøgle, scener og overlays.",
     "kw": "strip cam, stripchat live stream, stripchat udsend, stripchat external software, stripchat stream key, stripchat rtmp obs",
     "h1html": 'Sådan udsender du på <span class="accent">Stripchat</span> med SplitCam',
     "h1short": "Udsend Stripchat",
     "card": "Ekstern software-opsætning til Stripchat-streams.",
     "intro": "Stripchat er en stor cam-platform med fokus på interaktivitet. <em>External software</em>-tilstand giver dig en token-baseret nøgle — putter den i gratis <strong style='color:var(--text)'>SplitCam</strong> for at udsende med scener, overlays og filtre i stedet for et fladt kamera.",
     "quick": "Udsend på Stripchat med SplitCam: installér SplitCam, byg scenen, på Stripchat vælg <em>Switch to external software</em>, kopiér stream key, indsæt i SplitCam, Go Live."
              "<ol><li>Installér SplitCam.</li><li>Tilføj kamera + scene.</li>"
              "<li>Hent stream key fra Stripchat.</li><li>Indsæt i SplitCam.</li>"
              "<li>Tryk Go Live.</li></ol>",
     "key_how": "På Stripchat vælg <strong>Switch to external software</strong>, derefter <strong>Show external software settings for the stream</strong>. Kopiér stream key — Stripchat viser den som token. Hold privat.",
     "tips": [
         ("Match opløsning med sitet", "Stripchat's FAQ advarer: opløsningen i din software skal matche sitets præcist, ellers pixelerer videoen. Indstil begge ens."),
         ("Pas på 2 Mbps minimum", "Stripchat angiver 2 Mbps upload som minimum — og siger direkte, det ikke er nok til OBS-streaming eller multistreaming. Sigt meget højere."),
         ("Nøglen er en token", "Stripchat's stream key er en token — kopiér præcist, del aldrig, nulstil ved lækage."),
         _T_ETH,
     ],
     "faq": [
         ("Anbefaler Stripchat OBS / ekstern software?", "Ja — Stripchat's officielle FAQ anbefaler ekstern broadcast-software som OBS «for at opnå den bedste video- og lydkvalitet». SplitCam virker på samme måde."),
         ("Hvordan skifter jeg Stripchat til ekstern software?", "I Broadcast Center vælg Switch to External Broadcast Software (OBS), åbn derefter external software settings for at afsløre stream key (token)."),
         ("Hvilken bitrate til Stripchat?", "RTMP ingest accepterer op til ~6.000 Kbps med 2-sekunds keyframe. 3.500–6.000 ved 1080p er ideelt — men skal være godt over 2 Mbps-minimum, især til OBS-streaming."),
         ("Er SplitCam gratis til Stripchat?", "Ja — ingen licensafgift, intet vandmærke, ingen tidsbegrænsning: selv lange interaktive Stripchat-shows koster intet på encoder-siden."),
     ]},
    {"slug": "onlyfans", "name": "OnlyFans",
     "title": "Gå live på OnlyFans med SplitCam — Autorisation eller nøgle",
     "desc": "Gå live på OnlyFans med gratis SplitCam — login via autorisation eller OBS Key, multi-kamera scener, overlays. Intet vandmærke.",
     "kw": "live onlyfans, onlyfans live stream, onlyfans autorisation splitcam, onlyfans obs key, onlyfans streaming software",
     "h1html": 'Sådan går du live på <span class="accent">OnlyFans</span> med SplitCam',
     "h1short": "Live OnlyFans",
     "card": "Autorisér én gang eller indsæt nøglen — live på OnlyFans.",
     "intro": "OnlyFans live er til dine abonnenter. SplitCam forbinder på <strong style='color:var(--text)'>to måder</strong> — du logger ind én gang med OnlyFans-kontoen, og SplitCam henter stream key automatisk og holder den synkroniseret, eller du indsætter OBS Key manuelt. I begge tilfælde udsender du med multi-kamera scener, overlays og filtre.",
     "quick": "Live på OnlyFans med SplitCam: installér SplitCam, byg scenen, åbn Stream Settings &rarr; Add Channel &rarr; OnlyFans og vælg <em>Autorisation</em> — log ind med OnlyFans-konto, SplitCam henter nøglen automatisk — og tryk Go Live. Med tilknyttet konto kan du ændre OnlyFans stream-parametre i SplitCam, uden at åbne OnlyFans-sitet.",
     "steps": [
         ("Download og installér SplitCam",
          "SplitCam er gratis streaming-software til Windows og macOS — uden tilmelding, kort eller vandmærke. Det er encoderen, der sender din video til OnlyFans."),
         ("Opsæt kamera og scene",
          "Åbn SplitCam og tilføj webkameraet. Byg scenen, som seerne skal se den — overlays, tekst, et andet kamera, beauty-filtre eller AI-baggrund, alt anvendt live."),
         ("Forbindelse — Metode 1: Autorisation (anbefalet)",
          "I SplitCam åbn <strong>Stream Settings</strong> &rarr; <strong>Add Channel</strong> &rarr; <strong>OnlyFans</strong> og vælg <strong>Autorisation</strong>. Log ind med OnlyFans email og adgangskode. SplitCam tilknytter kontoen, henter stream key automatisk og holder den synkroniseret — og lader dig administrere OnlyFans live-parametre i SplitCam, ændre dem under eller efter udsendelsen uden at åbne OnlyFans-sitet."),
         ("Forbindelse — Metode 2: Stream Key (manuelt)",
          "Foretrækker du ikke at logge ind? Brug nøglen. På OnlyFans gå til <strong>Profile</strong> &rarr; <strong>Settings</strong> &rarr; <strong>Other</strong>-sektionen og kopiér <strong>OBS Key</strong>. I SplitCam, Add Channel &rarr; OnlyFans, indsæt i nøglefeltet. Denne nøgle er statisk — for at ændre indstillinger senere går du tilbage til OnlyFans-sitet."),
         ("Go Live",
          "Uanset metode, tryk <strong>Go Live</strong> i SplitCam. Med Metode 1 kan du fortsætte med at justere OnlyFans-parametre fra SplitCam i realtid; med Metode 2 forbliver nøglen præcis, som du har sat den."),
     ],
     "tips": [
         ("Autorisation vs Stream Key", "To måder at forbinde på: <strong>Autorisation</strong> (log ind én gang, nøglen hentes og synkroniseres — den nemmeste rute) eller <strong>Stream Key</strong> (kopiér OBS Key på OnlyFans → Profile → Settings → Other og indsæt). Autorisation sparer manuel kopi-indsæt."),
         ("Ændr indstillinger uden at forlade SplitCam", "Med autorisation forbliver kontoen tilknyttet, så du justerer OnlyFans live-parametre fra SplitCam under eller efter udsendelsen — uden at gå via OnlyFans-sitet."),
         ("Beskeden bitrate", "OnlyFans' RTMP ingest begrænser video-bitrate til omkring 2.500 Kbps — strammere end de fleste cam-sites. Sigt mod 720p–1080p ved ~2.000–2.500."),
         _T_ETH,
     ],
     "faq": [
         ("Hvordan forbinder jeg OnlyFans til SplitCam?", "På to måder. <strong>Autorisation</strong> — Stream Settings → Add Channel → OnlyFans → log ind med OnlyFans-konto, og SplitCam henter nøglen automatisk. Eller <strong>Stream Key</strong> — kopiér OBS Key på OnlyFans → Profile → Settings → Other og indsæt."),
         ("Kan jeg ændre OnlyFans live-indstillinger uden at åbne sitet?", "Ja — med Autorisations-metoden forbliver SplitCam tilknyttet din OnlyFans-konto, så nøgle og indstillinger synkroniserer automatisk. Du ændrer alt fra SplitCam under eller efter udsendelsen uden at besøge onlyfans.com."),
         ("Hvilken bitrate til OnlyFans?", "Beskeden — OnlyFans' RTMP ingest begrænser bitrate til omkring 2.500 Kbps, meget strammere end andre cam-platforme. Sigt mod 720p–1080p omkring 2.000–2.500 Kbps."),
         ("Er SplitCam gratis til OnlyFans live?", "Ja — gratis, uden vandmærke og uden tidsbegrænsning. Ingen omkostninger på encoder-siden."),
     ]},
    {"slug": "camplace", "name": "CamPlace",
     "title": "Udsend på CamPlace med SplitCam — Gratis guide",
     "desc": "Udsend på CamPlace med gratis SplitCam — ekstern encoder, RTMP-nøgle, scener og overlays. Trin for trin, intet vandmærke.",
     "kw": "camplace udsend, camplace broadcasting software, camplace rtmp, camplace external encoder, camplace stream key",
     "h1html": 'Sådan udsender du på <span class="accent">CamPlace</span> med SplitCam',
     "h1short": "Udsend CamPlace",
     "card": "Ekstern encoder-opsætning til CamPlace-streams.",
     "intro": "CamPlace er en cam-streaming-platform. Der er ingen offentlig OBS-artikel, så <strong style='color:var(--text)'>videoguiden ovenover</strong> er din reference — gratis <strong style='color:var(--text)'>SplitCam</strong> forbinder via standard-RTMP og tilføjer scener, overlays og AI-baggrund, som basis-kameraet ikke gør.",
     "quick": "Udsend på CamPlace med SplitCam: installér SplitCam, byg scenen, aktivér ekstern/RTMP-broadcasting på CamPlace, kopiér server-URL og stream key, indsæt i SplitCam, Go Live. Følg videoen for den aktuelle rute."
              "<ol><li>Installér SplitCam.</li><li>Tilføj kamera + scene.</li>"
              "<li>Hent RTMP-nøgle fra CamPlace.</li><li>Indsæt i SplitCam.</li>"
              "<li>Tryk Go Live.</li></ol>",
     "key_how": "Log ind på CamPlace og åbn broadcasting-indstillingerne. Skift til ekstern encoder / RTMP / OBS-mulighed for at afsløre <strong>server-URL</strong> og <strong>stream key</strong>, kopiér begge. CamPlace udgiver ikke officiel OBS-dokumentation — <strong>videoen ovenover</strong> er den mest pålidelige trin-for-trin rute gennem den aktuelle grænseflade.",
     "tips": [
         ("Ingen officiel OBS-guide — brug videoen", "CamPlace har ingen offentlig artikel om eksterne encodere; videoen ovenover er reference for den aktuelle rute."),
         ("Standard-RTMP virker", "Selvom udokumenteret, accepterer CamPlace standard-RTMP server-URL og nøgle — SplitCam forbinder som tilpasset RTMP-destination."),
         ("Stak overlays i SplitCam", "Tip-mål, navn og social-handles som scene-lag — CamPlace's basis-kamera tilføjer ikke sådanne."),
         _T_ETH,
     ],
     "faq": [
         ("Har CamPlace en officiel OBS-guide?", "Ingen offentlig artikel om eksterne encodere fundet. CamPlace accepterer standard-RTMP URL og nøgle, så SplitCam virker — følg videoen."),
         ("Understøtter CamPlace eksterne encodere?", "Ja — det accepterer en standard-RTMP stream key, så SplitCam forbinder som tilpasset RTMP-destination."),
         ("Hvilken bitrate til CamPlace?", "CamPlace udgiver ikke et officielt tal — brug 3.500–6.000 Kbps ved 1080p som sikker rækkevidde og lad SplitCam's hastighedstest fastsætte dit reelle loft."),
         ("Er SplitCam gratis til CamPlace?", "Ja — gratis, uden vandmærke og uden tidsbegrænsning. Da CamPlace ikke kommer med egen encoder, gør et gratis RTMP-værktøj arbejdet."),
     ]},
    {"slug": "camsoda", "name": "CamSoda",
     "title": "CamSoda live med SplitCam — Gratis opsætning",
     "desc": "CamSoda live med gratis SplitCam — Use OBS Broadcaster, regionale servere, scener og overlays. Intet vandmærke.",
     "kw": "camsoda live, camsoda udsend, camsoda obs broadcaster, camsoda rtmp obs, camsoda live broadcast",
     "h1html": 'Sådan udsender du på <span class="accent">CamSoda</span> med SplitCam',
     "h1short": "Udsend CamSoda",
     "card": "Use OBS Broadcaster-opsætning på CamSoda.",
     "intro": "CamSoda er en amerikansk cam-platform kendt for interaktive og usædvanlige show-formater. Det understøtter OBS-streaming officielt — der er en <strong style='color:var(--text)'>Use OBS Broadcaster</strong>-knap på Go Live-siden og en officiel OBS-guide på CamSoda-wikien. Gratis <strong style='color:var(--text)'>SplitCam</strong> virker på samme måde.",
     "quick": "Udsend på CamSoda med SplitCam: installér SplitCam, byg scenen, klik Use OBS Broadcaster på CamSoda Go Live-siden, kopiér server-URL og stream key, indsæt i SplitCam, Go Live."
              "<ol><li>Installér SplitCam.</li><li>Tilføj kamera + scene.</li>"
              "<li>Klik Use OBS Broadcaster på CamSoda.</li>"
              "<li>Indsæt server-URL + nøgle i SplitCam.</li><li>Tryk Go Live.</li></ol>",
     "key_how": "På CamSoda's <strong>Go Live</strong>-side klik <strong>Use OBS Broadcaster</strong>. CamSoda viser RTMP-server-URL og stream key — kopiér begge. Vælg den regionale server (Nordamerika, Europa, Asien osv.), der er nærmest. CamSoda-wikien har en fuld OBS-guide til detaljer.",
     "tips": [
         ("Verificér for tips", "På CamSoda kan alle udsende, men for at modtage tips skal du gennemføre CamSoda's verificeringsproces."),
         ("Vælg den nærmeste regionale server", "CamSoda tilbyder regionale ingest-servere — den nærmeste (NA / Europa / Asien / Sydamerika / Oceanien) reducerer latens og mistede frames."),
         ("Loft ved 1080p / 30 fps", "CamSoda's ingest går op til omkring 1080p, 30 fps og ~6.000 Kbps — tving ikke højere."),
         _T_ETH,
     ],
     "faq": [
         ("Understøtter CamSoda OBS / eksterne encodere?", "Ja — officielt. Der er en Use OBS Broadcaster-knap på Go Live-siden og en OBS-guide på CamSoda-wikien, så SplitCam virker."),
         ("Skal jeg verificere mig på CamSoda?", "For at udsende, nej. For at modtage tips, ja — CamSoda kræver først verificeringsprocessen gennemført."),
         ("Hvilken opløsning understøtter CamSoda?", "Op til 1920×1080 ved 30 fps, omkring 6.000 Kbps maksimum på RTMP ingest."),
         ("Er SplitCam gratis til CamSoda?", "Ja — gratis, uden vandmærke og uden tidsbegrænsning. Virker med CamSoda's gratis Use OBS Broadcaster-tilstand, så hele kæden koster intet."),
     ]},
    {"slug": "streamate", "name": "Streamate",
     "title": "Udsend på Streamate med SplitCam — Integreret kanal",
     "desc": "Udsend på Streamate med gratis SplitCam — integreret kanal, SM Connect-nøgle, scener og overlays. Intet vandmærke.",
     "kw": "streamate, streamate sm connect, streamate udsend, streamate broadcasting software, streamate rtmp",
     "h1html": 'Sådan udsender du på <span class="accent">Streamate</span> med SplitCam',
     "h1short": "Udsend Streamate",
     "card": "Streamate er en integreret kanal i SplitCam — hurtig opsætning.",
     "intro": "Streamate er en etableret cam-platform — og er en af de <strong style='color:var(--text)'>forkonfigurerede destinationer i SplitCam</strong>, i kanallisten, så opsætningen er hurtigere end manuel RTMP-indtastning: du vælger Streamate, indsætter nøglen, færdig.",
     "quick": "Udsend på Streamate med SplitCam: installér SplitCam, byg scenen, på Streamate brug <em>SM Connect → Start Show</em> og kopiér nøglen, derefter i SplitCam åbn <em>Stream Settings → Add Channel → Streamate</em> og indsæt."
              "<ol><li>Installér SplitCam.</li><li>Tilføj kamera + scene.</li>"
              "<li>Hent Streamate-nøgle via SM Connect.</li>"
              "<li>Add Channel → Streamate i SplitCam.</li><li>Tryk Go Live.</li></ol>",
     "key_how": "På Streamate åbn <strong>SM Connect</strong>, acceptér vilkårene, klik <strong>Start Show</strong> til venstre og luk det åbnede vindue — kopiér derefter streaming-nøglen. I SplitCam åbn <strong>Stream Settings</strong> → <strong>Add Channel</strong>, vælg <strong>Streamate</strong> fra listen og indsæt nøglen. En grøn slider bekræfter forbindelsen.",
     "tips": [
         ("Streamate er integreret", "Ingen manuel RTMP-URL — SplitCam har Streamate i Add Channel-listen; bare vælg og indsæt nøglen."),
         ("Luk SM Connect-popup", "Efter Start Show åbner Streamate et vindue — luk det; det var kun til at afsløre streaming-nøglen."),
         ("Lås opløsning til 1080p", "Video Resolution-feltet i SM Connect kan stille hoppe til 1440, hvilket faktisk ikke leveres og sænker din kvalitet lydløst — indstil manuelt til 1080p. Bitrate, der falder ved statisk billede, er normalt: Streamate's stream er adaptiv."),
         _T_ETH, _T_TEST,
     ],
     "faq": [
         ("Er Streamate integreret i SplitCam?", "Ja — Streamate vises i SplitCam's Add Channel-liste; du vælger i stedet for at indtaste en RTMP-URL manuelt."),
         ("Hvor er Streamate streaming-nøglen?", "SM Connect → acceptér vilkår → Start Show → luk popup → kopiér nøgle."),
         ("Hvilken bitrate til Streamate?", "Streamate sætter ikke et hårdt loft — 3.500–6.000 Kbps ved 1080p virker godt. Streamen er adaptiv, så lavere bitrate ved statisk billede er normalt, ikke en fejl."),
         ("Er SplitCam gratis til Streamate?", "Ja — gratis, uden vandmærke og uden tidsbegrænsning; og fordi Streamate er en integreret kanal i SplitCam, er der heller ingen separat encoder-omkostning."),
     ]},
    {"slug": "streamray", "name": "StreamRay",
     "title": "Udsend på StreamRay cam med SplitCam — Chat-URL",
     "desc": "Udsend på StreamRay cam med gratis SplitCam — URL postet i chat, OBS Broadcaster-tilstand, scener og overlays. Intet vandmærke.",
     "kw": "streamray, streamray cam, streamray udsend, streamray obs broadcaster, streamray rtmp",
     "h1html": 'Sådan udsender du på <span class="accent">StreamRay</span> med SplitCam',
     "h1short": "Udsend StreamRay",
     "card": "URL-i-chat ekstern encoder-opsætning til StreamRay.",
     "intro": "StreamRay har en usædvanlig ekstern encoder-opsætning — den leverer stream-URL'en i <strong style='color:var(--text)'>chat-vinduet for udsendelsen</strong> og bruger ikke en separat stream key. Gratis <strong style='color:var(--text)'>SplitCam</strong> håndterer denne kun-URL flow.",
     "quick": "Udsend på StreamRay med SplitCam: installér SplitCam, byg scenen, på StreamRay aktivér OBS Broadcaster, kopiér stream-URL fra chat-vinduet, indsæt i SplitCam (efterlad nøglefelt tomt), Go Live."
              "<ol><li>Installér SplitCam.</li><li>Tilføj kamera + scene.</li>"
              "<li>Kopiér StreamRay-URL fra chat.</li>"
              "<li>Indsæt URL i SplitCam.</li><li>Tryk Go Live.</li></ol>",
     "key_how": "På StreamRay dobbeltklik <strong>Broadcast Now</strong>, åbn <strong>Other</strong>-menuen, vælg <strong>OBS Broadcaster</strong> og <strong>Save and Close</strong>. StreamRay poster derefter <strong>stream-URL i chat-vinduet</strong> — kopiér derfra. Efterlad SplitCam's stream key-felt <strong>tomt</strong>; StreamRay autentificerer kun via URL.",
     "tips": [
         ("URL er i chatten", "StreamRay viser ikke stream-URL i en indstillingsboks — den postes i chat-vinduet for udsendelsen. Kopiér derfra."),
         ("Efterlad nøglefelt tomt", "StreamRay bruger ikke separat nøgle — kun URL. Skriv intet i SplitCam's nøglefelt."),
         _T_ETH, _T_TEST,
     ],
     "faq": [
         ("Hvor er StreamRay stream-URL?", "Efter aktivering af OBS Broadcaster poster StreamRay URL'en i chat-vinduet — kopiér fra chat."),
         ("Hvorfor er der ingen stream key på StreamRay?", "StreamRay autentificerer kun via URL — efterlad SplitCam's nøglefelt tomt."),
         ("Hvilken bitrate til StreamRay?", "StreamRay angiver ikke et officielt loft — sigt mod 3.500–6.000 Kbps ved 1080p og kør SplitCam's hastighedstest, da kun-URL flow ikke giver bitrate-feedback."),
         ("Er SplitCam gratis til StreamRay?", "Ja — gratis, uden vandmærke og uden tidsbegrænsning, hvilket passer til StreamRay's kun-URL flow: indsæt et link, og du er live."),
     ]},
    {"slug": "xlovecam", "name": "XLoveCam",
     "title": "Udsend på XLoveCam med SplitCam — RTMP-link & nøgle",
     "desc": "Udsend på XLoveCam med gratis SplitCam — RTMP-link og nøgle, regionale servere, scener og overlays. Intet vandmærke.",
     "kw": "xlovecam, x love cam, xlovecam udsend, xlovecam rtmp link, xlovecam stream key",
     "h1html": 'Sådan udsender du på <span class="accent">XLoveCam</span> med SplitCam',
     "h1short": "Udsend XLoveCam",
     "card": "RTMP-link + nøgle-opsætning til XLoveCam.",
     "intro": "XLoveCam er en europæisk flersproget cam-platform. Konto-indstillingerne viser både et <strong style='color:var(--text)'>RTMP-link</strong> og en <strong style='color:var(--text)'>stream key</strong> — gratis <strong style='color:var(--text)'>SplitCam</strong> tager begge og udsender med fulde scener og overlays.",
     "quick": "Udsend på XLoveCam med SplitCam: installér SplitCam, byg scenen, på XLoveCam åbn <em>My Account → settings</em>, kopiér RTMP-link og stream key, indsæt begge i SplitCam, start showet."
              "<ol><li>Installér SplitCam.</li><li>Tilføj kamera + scene.</li>"
              "<li>Kopiér RTMP-link + nøgle fra XLoveCam.</li><li>Indsæt begge i SplitCam.</li>"
              "<li>Tryk Go Live.</li></ol>",
     "key_how": "På XLoveCam åbn <strong>My Account</strong> → <strong>settings</strong>. Indstillingerne viser både et <strong>RTMP-link</strong> og en <strong>stream key</strong> — kopiér begge i SplitCam's server-URL- og nøglefelter, derefter <strong>Start your show</strong> på XLoveCam.",
     "tips": [
         ("Kopiér link OG nøgle", "XLoveCam giver dig et RTMP-link OG en separat stream key — du har brug for begge i SplitCam, ikke kun én."),
         ("Flersproget publikum", "XLoveCam er europæisk og flersproget — en klar tekst-overlay på dit sprog hjælper seerne med at finde dig."),
         ("Vælg den nærmeste server", "XLoveCam tilbyder regionale RTMP-servere — Europa, Nordamerika, Sydamerika og Asien. Den nærmeste reducerer latens og mistede frames."),
         _T_ETH,
     ],
     "faq": [
         ("Hvor er XLoveCam's RTMP-data?", "My Account → settings — viser både RTMP-link og nøgle."),
         ("Understøtter XLoveCam eksterne encodere?", "Ja — det leverer RTMP-link og nøgle, så SplitCam virker som encoder."),
         ("Hvilken bitrate til XLoveCam?", "XLoveCam udgiver ikke fast grænse; 3.500–6.000 Kbps ved 1080p er ideelt. At vælge den nærmeste regionale server tæller lige så meget — reducerer mistede frames."),
         ("Er SplitCam gratis til XLoveCam?", "Ja — gratis, uden vandmærke og uden tidsbegrænsning. At nå XLoveCam's flersprogede europæiske publikum koster ingen software."),
     ]},
    {"slug": "soulcams", "name": "SoulCams",
     "title": "Udsend på SoulCams med SplitCam — OBS-indstillinger",
     "desc": "Udsend på SoulCams med gratis SplitCam — OBS-indstillinger, RTMP-server og nøgle, multi-kamera scener og overlays.",
     "kw": "soul cams, soulcams, soulcams udsend, soulcams obs, soulcams rtmp, soulcams broadcast",
     "h1html": 'Sådan udsender du på <span class="accent">SoulCams</span> med SplitCam',
     "h1short": "Udsend SoulCams",
     "card": "OBS-indstillinger til SoulCams.",
     "intro": "SoulCams er en cam-platform, hvis OBS-indstillinger viser <strong style='color:var(--text)'>RTMP-server og stream key sammen</strong> i et vindue. Indsæt begge i gratis <strong style='color:var(--text)'>SplitCam</strong> for at udsende med multi-kamera scener og overlays.",
     "quick": "Udsend på SoulCams med SplitCam: installér SplitCam, byg scenen, på SoulCams klik Go Online → Settings → OBS, kopiér serveren og nøglen, indsæt begge i SplitCam, Go Live."
              "<ol><li>Installér SplitCam.</li><li>Tilføj kamera + scene.</li>"
              "<li>Åbn SoulCams Settings → OBS.</li><li>Indsæt server + nøgle i SplitCam.</li>"
              "<li>Tryk Go Live.</li></ol>",
     "key_how": "På SoulCams log ind og klik <strong>Go Online</strong>, åbn derefter <strong>Settings</strong> → <strong>OBS</strong>. OBS-vinduet viser <strong>RTMP-server</strong> og <strong>stream key</strong> sammen — kopiér begge i SplitCam.",
     "tips": [
         ("Server og nøgle side om side", "SoulCams viser RTMP-server og nøgle i samme OBS-vindue — du tager begge i ét hug."),
         ("Go Online først", "OBS-indstillinger vises først efter at have klikket Go Online på SoulCams — gør det, før du leder efter encoder-data."),
         ("Bloker uønskede regioner", "SoulCams tillader geo-blokering fra modellens side — vælg, hvilke lande der ikke kan se streamen, før du trykker Go Online."),
         _T_ETH, _T_TEST,
     ],
     "faq": [
         ("Hvor er SoulCams' OBS-indstillinger?", "Log ind, klik Go Online, derefter Settings → OBS — RTMP-server og stream key vises sammen."),
         ("Understøtter SoulCams eksterne encodere?", "Ja — OBS-indstillinger giver RTMP-server og nøgle, så SplitCam virker."),
         ("Hvilken bitrate til SoulCams?", "SoulCams giver ikke et officielt tal — sigt mod 3.500–6.000 Kbps ved 1080p og test upload, da OBS-vinduet ikke viser bitrate-vejledning."),
         ("Er SplitCam gratis til SoulCams?", "Ja — gratis, uden vandmærke og uden tidsbegrænsning, så et fuldt SoulCams-show med multi-kamera scener og overlays koster intet på encoder-siden."),
     ]},
    {"slug": "imlive", "name": "ImLive",
     "title": "Udsend på ImLive med SplitCam — Virtuelt kamera",
     "desc": "Im Live stream-opsætning med gratis SplitCam — ImLive bruger webkameraet direkte (ingen RTMP), forbind SplitCam som virtuelt kamera med scener.",
     "kw": "im live stream, imlive splitcam, imlive udsend, imlive virtuelt kamera, imlive webcam, im live cam",
     "h1html": 'Sådan bruger du <span class="accent">ImLive</span> med SplitCam',
     "h1short": "SplitCam på ImLive",
     "card": "Virtuelt kamera til ImLive — ingen RTMP.",
     "intro": "ImLive bruger webkameraet direkte i browseren — <strong style='color:var(--text)'>ingen RTMP og ingen stream key</strong>. Gratis <strong style='color:var(--text)'>SplitCam</strong> forbinder som <strong style='color:var(--text)'>virtuelt kamera</strong>: du bygger scenen i SplitCam, derefter vælger SplitCam som kamera i ImLive.",
     "quick": "Brug af SplitCam med ImLive: installér SplitCam, byg scenen med medie-lag, åbn ImLive og start videochat, i ImLive-indstillinger vælg SplitCam som webkamera og mikrofon."
              "<ol><li>Installér SplitCam.</li><li>Byg scene i SplitCam.</li>"
              "<li>Start videochat på ImLive.</li>"
              "<li>Vælg SplitCam som ImLive-kamera.</li><li>Start chatten.</li></ol>",
     "steps": [
         ("Installér SplitCam",
          "SplitCam er gratis software til Windows og macOS. Installér — uden vandmærke, uden tilmelding. Til ImLive virker det som <strong>virtuelt kamera</strong>, ikke RTMP-encoder."),
         ("Byg scene i SplitCam",
          "Åbn SplitCam og brug <strong>Media Layers +</strong> til at tilføje webkameraet plus eventuelle overlays, tekst, filtre eller AI-baggrund. Denne sammensatte scene er, hvad ImLive vil se som dit kamera."),
         ("Start videochat på ImLive",
          "Log ind på ImLive-sitet og klik <strong>Start Video Chat</strong>, åbn derefter <strong>Go To Settings</strong> for at nå kamera- og mikrofon-muligheder."),
         ("Vælg SplitCam som kamera",
          "I ImLive-indstillinger vælg <strong>SplitCam</strong> som webkamera OG som mikrofon. ImLive viser nu din fulde SplitCam-scene i stedet for et fladt webkamera."),
         ("Start Free Live Chat",
          "Klik <strong>Free Live Chat</strong> på ImLive for at gå live. For at ændre udseendet midt i sessionen, redigér scenen i SplitCam — ImLive opdateres øjeblikkeligt."),
     ],
     "tips": [
         ("Ingen stream key nødvendig", "ImLive har ingen RTMP — kig ikke efter server-URL eller nøgle. SplitCam vælges bare som kamera-enhed."),
         ("Indstil SplitCam også som mikrofon", "Vælg SplitCam til mikrofon ud over kamera, så dit lydmix og støjundertrykkelse også kommer i live."),
         ("Byg scenen før live", "ImLive viser, hvad SplitCam sender — arrangér lagene, før du starter chatten."),
         _T_TEST,
     ],
     "faq": [
         ("Bruger ImLive RTMP eller stream key?", "Nej — ImLive bruger webkameraet direkte gennem browseren. SplitCam forbinder som virtuelt kamera, der er ingen nøgle at kopiere."),
         ("Hvordan vælger jeg SplitCam på ImLive?", "Start Video Chat → Go To Settings → vælg SplitCam som webkamera og mikrofon."),
         ("Kan jeg bruge overlays på ImLive?", "Ja — byg dem i SplitCam-scenen; ImLive viser det sammensatte resultat."),
         ("Er SplitCam gratis til ImLive?", "Ja — gratis, uden vandmærke og uden tidsbegrænsning. Som virtuelt kamera til ImLive tilføjer det hverken omkostninger eller branding til din videochat."),
     ]},
    {"slug": "vxlive", "name": "VXLive",
     "title": "Udsend på VXLive med SplitCam — Officiel support",
     "desc": "Udsend på VXLive (VXModels / VISIT-X) med gratis SplitCam — officiel VISIT-X preset, server og nøgle, scener. Intet vandmærke.",
     "kw": "vxlive, visit-x, vxmodels splitcam, vxlive udsend, visit-x stream, vxlive rtmp",
     "h1html": 'Sådan udsender du på <span class="accent">VXLive</span> med SplitCam',
     "h1short": "Udsend VXLive",
     "card": "VXLive understøtter SplitCam officielt (VISIT-X preset).",
     "intro": "VXLive (VXModels / VISIT-X) er en cam-platform fra det tyske marked — og en af de få, der <strong style='color:var(--text)'>understøtter SplitCam officielt ved navn</strong>. VXModels har en dedikeret hjælpeartikel til at forbinde <strong style='color:var(--text)'>SplitCam</strong> til VXLive, og SplitCam leverer VISIT-X som færdig kanal-preset.",
     "quick": "Udsend på VXLive med SplitCam: installér SplitCam, byg scenen, på VXLive vælg «Stream with third-party software», kopiér server-URL og nøgle, i SplitCam vælg VISIT-X preset og indsæt, Go Live i SplitCam, derefter GO ONLINE på VXLive."
              "<ol><li>Installér SplitCam.</li><li>Tilføj kamera + scene.</li>"
              "<li>Hent server-URL + nøgle fra VXLive.</li>"
              "<li>Vælg VISIT-X preset i SplitCam, indsæt.</li>"
              "<li>Go Live, derefter GO ONLINE på VXLive.</li></ol>",
     "key_how": "På VXLive vælg <strong>Stream with third-party software</strong> og vælg mulighed for <strong>OBS, SplitCam eller XSplit</strong>. VXLive leverer <strong>server-URL</strong> og <strong>stream key</strong>. I SplitCam vælg <strong>VISIT-X</strong> som streaming-platform, indsæt begge, tryk <strong>Go Live</strong> i SplitCam, derefter <strong>GO ONLINE</strong> på VXLive.",
     "tips": [
         ("VISIT-X er integreret preset", "Indtast ikke rå RTMP-URL — SplitCam har VISIT-X i platform-listen; bare vælg og indsæt server-URL og nøgle."),
         ("To-trins go-live", "På VXLive tryk Go Live i SplitCam først, derefter GO ONLINE på VXLive — begge, i den rækkefølge."),
         ("Tysk marked", "VXLive's publikum er overvejende tysktalende — en tysk tekst-overlay eller titel hjælper med at forbinde med seerne."),
         _T_ETH,
     ],
     "faq": [
         ("Understøtter VXLive SplitCam officielt?", "Ja — VXModels (VXLive) opretholder en dedikeret officiel hjælpeartikel til SplitCam-opsætning og lister SplitCam ved siden af OBS og XSplit som understøttet broadcasting-software."),
         ("Hvordan forbinder jeg SplitCam til VXLive?", "På VXLive vælger du «Stream with third-party software», derefter i SplitCam vælger du VISIT-X preset og indsætter server-URL og stream key fra VXLive."),
         ("Går jeg live i SplitCam eller på VXLive?", "Begge — først Go Live i SplitCam, derefter GO ONLINE på VXLive."),
         ("Hvorfor anbefaler VXModels SplitCam?", "VXModels' officielle hjælpeartikel anbefaler SplitCam specifikt til at eliminere webkamera-billedartefakter og pixelering og stabilisere forbindelsen — ikke kun som generisk encoder."),
     ]},
    {"slug": "virtwish", "name": "VirtWish",
     "title": "Udsend på VirtWish med SplitCam — Stream-URL & nøgle",
     "desc": "Udsend på VirtWish med gratis SplitCam — Profile → Start Broadcast OBS-sektion, stream-URL og nøgle, scener og overlays.",
     "kw": "virtwish, virtwish udsend, virtwish broadcasting software, virtwish rtmp, virtwish stream key, virtwish obs",
     "h1html": 'Sådan udsender du på <span class="accent">VirtWish</span> med SplitCam',
     "h1short": "Udsend VirtWish",
     "card": "Stream-URL + nøgle til VirtWish.",
     "intro": "VirtWish er en interaktiv cam-platform. Broadcast-indstillingerne giver dig <strong style='color:var(--text)'>stream-URL og en separat stream key</strong> i en OBS-sektion — gratis <strong style='color:var(--text)'>SplitCam</strong> tager begge og kører showet med scener og overlays.",
     "quick": "Udsend på VirtWish med SplitCam: installér SplitCam, byg scenen, på VirtWish åbn <em>Profile → Start Broadcast</em> indtil OBS-sektionen, kopiér link og nøgle, indsæt begge i SplitCam, Go Live."
              "<ol><li>Installér SplitCam.</li><li>Tilføj kamera + scene.</li>"
              "<li>Hent URL + nøgle fra VirtWish.</li><li>Indsæt begge i SplitCam.</li>"
              "<li>Tryk Go Live.</li></ol>",
     "key_how": "På VirtWish klik på ikonet i øverste højre hjørne → <strong>Profile</strong> → <strong>Start Broadcast</strong>, derefter <strong>Start Broadcast</strong> igen for at nå OBS-sektionen. <strong>Kopiér linket på første linje</strong> til SplitCam's Stream URL-felt, og <strong>Stream Key</strong> separat i nøglefeltet.",
     "tips": [
         ("Link på første linje", "VirtWish's OBS-sektion sætter stream-URL på første linje — kopiér til SplitCam Stream URL, derefter den separate nøgle."),
         ("To klik på Start Broadcast", "Du klikker Start Broadcast to gange på VirtWish for at nå OBS-sektionen — forventet, ikke en fejl."),
         _T_ETH, _T_TEST,
     ],
     "faq": [
         ("Hvor er VirtWish's RTMP-data?", "Ikon øverst højre → Profile → Start Broadcast to gange → OBS-sektionen viser linket og stream key."),
         ("Understøtter VirtWish eksterne encodere?", "Ja — OBS-sektionen leverer stream-URL og nøgle, så SplitCam virker."),
         ("Hvilken bitrate til VirtWish?", "VirtWish udgiver ikke officielt loft; 3.500–6.000 Kbps ved 1080p er sikkert. Match SplitCam's opløsning med den, der er sat på VirtWish, for at undgå rescaling."),
         ("Er SplitCam gratis til VirtWish?", "Ja — gratis, uden vandmærke og uden tidsbegrænsning. VirtWish's URL-og-nøgle-opsætning koster kun de minutter, der kræves."),
     ]},
    {"slug": "xmodels", "name": "XModels",
     "title": "Udsend på XModels med SplitCam — Gratis guide",
     "desc": "Udsend på XModels med gratis SplitCam — ekstern encoder-mulighed i model-konto-indstillinger, RTMP-nøgle, scener og overlays.",
     "kw": "xmodels, xmodels udsend, xmodels broadcasting software, xmodels rtmp, xmodels external encoder",
     "h1html": 'Sådan udsender du på <span class="accent">XModels</span> med SplitCam',
     "h1short": "Udsend XModels",
     "card": "Ekstern encoder til XModels-streams.",
     "intro": "XModels er en cam-streaming-platform med en indbygget <strong style='color:var(--text)'>ekstern encoder-mulighed</strong> i model-konto-indstillinger. Gratis <strong style='color:var(--text)'>SplitCam</strong> udsender der med multi-kamera scener, overlays og filtre i stedet for et enkelt fladt kamera.",
     "quick": "Udsend på XModels med SplitCam: installér SplitCam, byg scenen, i XModels-modelkonto aktivér ekstern encoder-mulighed, kopiér server-URL og stream key, indsæt i SplitCam, Go Live."
              "<ol><li>Installér SplitCam.</li><li>Tilføj kamera + scene.</li>"
              "<li>Aktivér ekstern encoder i XModels-indstillinger.</li>"
              "<li>Indsæt server-URL + nøgle i SplitCam.</li><li>Tryk Go Live.</li></ol>",
     "key_how": "I XModels <strong>model-konto-indstillinger</strong> aktivér muligheden <strong>udsendelse via ekstern encoder</strong>. XModels leverer en <strong>stream key</strong> — kopiér til SplitCam. Hvis muligheden ikke er, hvor du forventer, er XModels-support via FAQ-chat på sitet og <strong>info@xmodels.com</strong>; videoen ovenover viser det også.",
     "tips": [
         ("Det er i konto-indstillinger", "XModels placerer den eksterne encoder-mulighed i model-konto-indstillinger, ikke på en separat broadcast-skærm."),
         ("Support: chat + email", "XModels har ikke et stort offentligt hjælpecenter — site FAQ-chat og info@xmodels.com er de officielle supportkanaler."),
         ("Stak overlays i SplitCam", "Tip-mål, navn og social-handles som scene-lag — XModels' basis-kamera tilføjer ikke sådanne."),
         _T_ETH,
     ],
     "faq": [
         ("Understøtter XModels eksterne encodere?", "Ja — model-konto-indstillinger inkluderer en ekstern encoder-broadcast-mulighed, der leverer en stream key, så SplitCam virker."),
         ("Hvor får jeg XModels-hjælp?", "XModels-support er via FAQ-chat på sitet og email info@xmodels.com — der er intet stort offentligt hjælpecenter."),
         ("Hvilken bitrate til XModels?", "XModels dokumenterer ikke et officielt tal — brug 3.500–6.000 Kbps ved 1080p og kør SplitCam's hastighedstest, da XModels-support kun er chat og email."),
         ("Er SplitCam gratis til XModels?", "Ja — gratis, uden vandmærke og uden tidsbegrænsning, så udsendelse til XModels' europæiske netværk tilføjer ingen software-omkostninger."),
     ]},
    {"slug": "flirt4free", "name": "Flirt4Free",
     "title": "Udsend på Flirt for Free cam med SplitCam — Gratis guide",
     "desc": "Udsend på Flirt for Free cam med gratis SplitCam — External Broadcast Form, RTMP URL og Stream Name, scener og overlays.",
     "kw": "flirt for free cam, flirt 4 free cam, flirt4free, flirt4free udsend, flirt4free external broadcast, flirt4free rtmp",
     "h1html": 'Sådan udsender du på <span class="accent">Flirt4Free</span> med SplitCam',
     "h1short": "Udsend Flirt4Free",
     "card": "External Broadcast Form til Flirt4Free.",
     "intro": "Flirt4Free er en af de ældste cam-platforme, i æteren siden 90'erne. Det understøtter ekstern udsendelse officielt via en <strong style='color:var(--text)'>External Broadcast Form</strong> — gratis <strong style='color:var(--text)'>SplitCam</strong> sender streamen, mens formularen sætter opløsning og bitrate.",
     "quick": "Udsend på Flirt4Free med SplitCam: installér SplitCam, byg scenen, åbn Flirt4Free External Broadcast Form, kopiér RTMP URL og Stream Name og indstil opløsning/bitrate, indsæt i SplitCam, Go Live."
              "<ol><li>Installér SplitCam.</li><li>Tilføj kamera + scene.</li>"
              "<li>Åbn Flirt4Free External Broadcast Form.</li>"
              "<li>Indsæt RTMP URL + Stream Name i SplitCam.</li>"
              "<li>Tryk Go Live.</li></ol>",
     "key_how": "I Flirt4Free-modelområdet åbn <strong>External Broadcast Form</strong>. I modsætning til de fleste cam-sites giver Flirt4Free dig en <strong>RTMP URL</strong> og et <strong>Stream Name</strong> (ikke en «nøgle»), plus opløsnings- og bitrate-felter, du udfylder i selve formularen. Kopiér URL og Stream Name til SplitCam's server- og nøglefelter.",
     "tips": [
         ("Det er Stream Name, ikke nøgle", "Flirt4Free kalder legitimationsoplysningen Stream Name. Du indsætter den i SplitCam's stream key-felt — samme rolle."),
         ("Indstil opløsning/bitrate i formularen", "Flirt4Free's External Broadcast Form har egne opløsnings- og bitrate-felter — afstem med SplitCam's indstillinger, så billedet ikke rescales."),
         ("Historisk platform", "Flirt4Free har kørt siden 90'erne — modelværktøjer er modne, og External Broadcast Form er en dokumenteret del af dem."),
         _T_ETH,
     ],
     "faq": [
         ("Understøtter Flirt4Free eksterne encodere?", "Ja — officielt, via External Broadcast Form, som leverer RTMP URL og Stream Name. SplitCam virker som encoder."),
         ("Hvor får jeg Flirt4Free's RTMP-data?", "Fra External Broadcast Form i modelområdet — viser RTMP URL, Stream Name og opløsnings/bitrate-felter."),
         ("Hvilken bitrate til Flirt4Free?", "3.500–6.000 Kbps ved 1080p — indstil samme værdi i External Broadcast Form og i SplitCam."),
         ("Er SplitCam gratis til Flirt4Free?", "Ja — gratis, uden vandmærke og uden tidsbegrænsning, hvilket passer til en historisk platform som Flirt4Free, hvor shows kan være lange."),
     ]},
    {"slug": "mfc-alerts", "name": "MFC Alerts",
     "title": "Tilføj MFC Alerts til streamen med SplitCam",
     "desc": "Vis animerede tip alerts i MyFreeCams-stream — mfcalerts.com-URL som Browser-lag i gratis SplitCam, over webkameraet.",
     "kw": "mfc alerts, myfreecams alerts, tilføj mfc alerts, mfcalerts splitcam, myfreecams tip alerts, myfreecams alerts overlay",
     "h1html": 'Sådan tilføjer du <span class="accent">MFC Alerts</span> til din stream',
     "h1short": "Tilføj MFC Alerts",
     "card": "Vis animerede tip alerts i MyFreeCams-streamen.",
     "intro": "MFC Alerts viser animerede effekter i din MyFreeCams-stream, hver gang en seer sender en tip. Kører som <strong style='color:var(--text)'>Browser-lag</strong> i gratis <strong style='color:var(--text)'>SplitCam</strong> — du opsætter én gang, og tips udløser skærmreaktioner live.",
     "quick": "Tilføjelse af MFC Alerts med SplitCam: installér SplitCam, tilføj webkameraet, åbn Browser-fanen og indlæs mfcalerts.com, kopiér alerts-URL, tilføj som Browser-lag over webkameraet, test derefter med test-tip."
              "<ol><li>Installér SplitCam.</li><li>Tilføj webkameraet.</li>"
              "<li>Hent URL på mfcalerts.com.</li>"
              "<li>Tilføj som Browser-lag over webkameraet.</li>"
              "<li>Send test-tip.</li></ol>",
     "steps": [
         ("Installér SplitCam og tilføj webkameraet",
          "Installér gratis SplitCam til Windows eller macOS, tilføj derefter <strong>webkameraet</strong> som kilde. MFC Alerts sidder som lag over dette kamera."),
         ("Åbn Browser-fanen og gå til mfcalerts.com",
          "I SplitCam åbn <strong>Browser</strong>-fanen og naviger til <strong>www.mfcalerts.com</strong>. Log ind, eller registrér dig, hvis du ikke har en mfcalerts.com-konto endnu."),
         ("Kopiér din alerts-URL",
          "På mfcalerts.com brug <strong>Copy to clipboard</strong> til at kopiere din personlige alerts-URL — det er siden, der renderer tip-animationer."),
         ("Tilføj URL som Browser-lag — over webkameraet",
          "Indsæt URL'en i SplitCam's Browser-vindue og klik <strong>Add</strong>. Omarranger derefter kildelisten, så <strong>MFC Alerts er over webkameraet</strong> (3-prikket menu → Move Up). Hvis det sidder under, forbliver effekterne skjult."),
         ("Test med test-tip",
          "Åbn <strong>Settings → Send test tip</strong> og bekræft, at alert-effekten vises over kameraet. Udsend derefter normalt på MyFreeCams — rigtige tips udløser nu animationerne."),
     ],
     "tips": [
         ("MFC Alerts skal være over webkameraet", "Den mest almindelige fejl: hvis MFC Alerts-laget er under webkameraet på kildelisten, forbliver effekterne skjult. Flyt op."),
         ("Mfcalerts.com-konto påkrævet", "Alerts-URL er personlig — registrér dig på mfcalerts.com først, hvis du ikke har en konto."),
         ("Send test-tip før live", "Brug Settings → Send test tip til at bekræfte, at overlay'et virker — opdag ikke fejlen midt i showet."),
         _T_ETH,
     ],
     "faq": [
         ("Hvad er MFC Alerts?", "Et notifikationssystem til MyFreeCams, der viser videoeffekter i din stream, når seere sender tips — tilføjet som Browser-overlay i SplitCam."),
         ("Hvorfor vises mine MFC Alerts ikke?", "Næsten altid lagorden — MFC Alerts Browser-laget skal være over webkameraet på SplitCam's kildeliste."),
         ("Skal jeg have en konto til MFC Alerts?", "Ja — registrér dig på mfcalerts.com for at få din personlige alerts-URL."),
         ("Er SplitCam gratis til dette?", "Ja — SplitCam er gratis, uden vandmærke og uden tidsbegrænsning, og MFC Alerts browser-overlay kører i den uden ekstra omkostninger."),
     ]},
    {"slug": "lovense", "name": "Lovense",
     "title": "Tilføj et Lovense-legetøj til streamen med SplitCam",
     "desc": "Forbind et interaktivt Lovense-legetøj til cam-stream med gratis SplitCam — Lovense SplitCam Toolset, skærm-tip alerts, reaktioner.",
     "kw": "tilføj lovense til stream, lovense cam stream, lovense splitcam, lovense splitcam toolset, lovense interactive toy streaming",
     "h1html": 'Sådan tilføjer du et <span class="accent">Lovense-legetøj</span> til din stream',
     "h1short": "Tilføj Lovense-legetøj",
     "card": "Forbind et interaktivt Lovense-legetøj til cam-streamen.",
     "intro": "Du kører cam-streamen via gratis <strong style='color:var(--text)'>SplitCam</strong> og parrer et <strong style='color:var(--text)'>Lovense</strong>-legetøj, der reagerer på tokens. Lovense dokumenterer et officielt <strong style='color:var(--text)'>Lovense SplitCam Toolset</strong>, og SplitCam leverer en officiel Lovense-plugin — integrationen er understøttet fra begge sider.",
     "quick": "For at tilføje et Lovense-legetøj til streamen: installér SplitCam og Lovense-software, par legetøjet, link Lovense til cam-platformen, tilføj Lovense-status som Browser-lag i SplitCam, udsend derefter normalt."
              "<ol><li>Installér SplitCam.</li><li>Installér Lovense-software og par legetøj.</li>"
              "<li>Link Lovense til cam-sitet.</li>"
              "<li>Tilføj Lovense-overlay i SplitCam.</li><li>Tryk Go Live.</li></ol>",
     "steps": [
         ("Installér SplitCam",
          "SplitCam er gratis streaming-software til Windows og macOS — encoderen, der sender din video til cam-platformen. Installér; uden vandmærke."),
         ("Installér Lovense-software og par legetøjet",
          "Installér Lovense Connect / Lovense Stream (officiel desktop-app). Tænd legetøjet og par via Bluetooth, så appen viser forbundet."),
         ("Link Lovense til cam-platformen",
          "I Lovense-appen link din cam-konto, så legetøjet reagerer på seer-tokens / tips. De fleste store cam-platforme understøttes."),
         ("Tilføj Lovense-overlay i SplitCam",
          "Lovense leverer en overlay/widget-URL. Tilføj som <strong>Browser</strong>-lag i SplitCam-scenen, så seerne ser legetøjets status og seneste tips på skærmen."),
         ("Byg scene og Go Live",
          "Tilføj kameraet og andre overlays, indsæt cam-platformens RTMP-nøgle i SplitCam og klik <strong>Go Live</strong>. Legetøjet reagerer på tips i realtid."),
     ],
     "tips": [
         ("Brug det officielle Lovense SplitCam Toolset", "Lovense udgiver et SplitCam-specifikt toolset med egen installationsguide — det tilføjer legetøjs-aktivitets-overlay og tip alerts lavet til SplitCam."),
         ("Opdater Lovense Cam Extension", "Toolset'et kræver en nylig Lovense Cam Extension (30.1.4 eller nyere) — opdater før live."),
         ("Hold legetøjet opladet", "Næsten tomt batteri midt i showet dræber den interaktive side — oplad fuldt før live."),
         ("Test token-reaktion", "Send en lille test-tip for at bekræfte, at legetøjet reagerer, før du åbner rummet."),
         ("Tjek versions-krav", "Lovense SplitCam Toolset kræver SplitCam 10.4.5 eller nyere. Lovense Cam Extension dækker officielt Chaturbate, Stripchat, BongaCams, MyFreeCams og CamSoda — for andre sites brug Lovense's Generic URL-integration."),
     ],
     "faq": [
         ("Understøtter Lovense SplitCam officielt?", "Ja — Lovense dokumenterer et officielt «Lovense SplitCam Toolset» med egen installationsguide, og SplitCam leverer en officiel Lovense-plugin. Integrationen er understøttet fra begge sider."),
         ("Forbinder legetøjet direkte til SplitCam?", "Nej — legetøjet parres med Lovense-appen; SplitCam viser Lovense-overlay og udsender kameraet."),
         ("Hvilke cam-sites understøtter Lovense?", "Lovense Cam Extension understøtter officielt Chaturbate, Stripchat, BongaCams, MyFreeCams og CamSoda, med varierende understøttelse for andre — tjek den aktuelle liste i Lovense-appen."),
         ("Kan jeg vise seneste tips på skærmen?", "Ja — tilføj Lovense widget-URL som Browser-lag i SplitCam."),
     ]},
    {"slug": "multistream-cams", "name": "Flere cam-sites",
     "title": "Udsend til flere cam-sites samtidigt med SplitCam",
     "desc": "Udsend til MyFreeCams, Chaturbate, BongaCams, CAM4, Stripchat og flere samtidigt med SplitCam's gratis multistreaming. Ét klik, intet vandmærke.",
     "kw": "udsend til flere cam-sites, multistream cam sites, udsend til chaturbate og bongacams samtidigt, multistream cam software",
     "h1html": 'Sådan udsender du til <span class="accent">flere cam-sites</span> samtidigt',
     "h1short": "Cam-multistreaming",
     "card": "Udsend til flere cam-sites samtidigt.",
     "intro": "Gratis <strong style='color:var(--text)'>SplitCam</strong> kan udsende én kodning til <strong style='color:var(--text)'>flere cam-sites samtidigt</strong> — MyFreeCams, Chaturbate, BongaCams, CAM4, Stripchat og flere. Intet vandmærke, ét klik.",
     "quick": "For at udsende til flere cam-sites på én gang: installér SplitCam, byg scenen, hent RTMP-server-URL og stream key fra hvert cam-site, tilføj alle i SplitCam's multistreaming-indstillinger, klik Go Live én gang."
              "<ol><li>Installér SplitCam.</li><li>Tilføj kamera + scene.</li>"
              "<li>Hent en RTMP-nøgle fra hvert cam-site.</li>"
              "<li>Tilføj alle nøgler i SplitCam multistream.</li>"
              "<li>Tryk Go Live én gang.</li></ol>",
     "steps": [
         ("Installér SplitCam",
          "SplitCam er gratis streaming-software til Windows og macOS med indbygget multistreaming. Installér — uden vandmærke, uden tilmelding."),
         ("Opsæt kamera og scene",
          "Åbn SplitCam, tilføj webkameraet og byg scenen med overlays og filtre. Én scene fodrer hver destination."),
         ("Hent en RTMP-nøgle fra hvert cam-site",
          "På hver cam-platform aktivér ekstern / RTMP-broadcasting og kopiér <strong>server-URL</strong> og <strong>stream key</strong>. Gentag for hvert site, du vil udsende til — se de enkelte platform-guides for præcise ruter."),
         ("Tilføj hver destination i SplitCam",
          "Åbn <strong>Stream Settings</strong> og tilføj hvert cam-site som tilpasset RTMP-destination — indsæt server-URL og nøgle. Markér alt, du vil have live."),
         ("Klik Go Live én gang",
          "Tryk <strong>Go Live</strong>. SplitCam sender streamen til hvert valgt cam-site samtidigt, peer-to-peer, fra én kodning — uden ekstra gebyr."),
     ],
     "tips": [
         ("Følg dit upload", "Multistreaming multiplicerer upload-belastningen. Hver destination forbruger sin egen bitrate — sørg for, at din forbindelse kan klare summen."),
         ("Tjek platform-regler", "Nogle cam-sites forbyder samtidig udsendelse andre steder — bekræft før multistreaming."),
         ("Kabel — drops kan du ikke tillade her", "Multistreaming multiplicerer upload-belastningen, så et enkelt wi-fi-drop kan vælte alle destinationer på én gang. Kabel er ikke valgfrit her."),
         ("Følg sundhedsmonitoren", "SplitCam viser status per destination — drop et site, hvis upload ikke kan klare det."),
     ],
     "faq": [
         ("Er SplitCam multistreaming gratis?", "Ja — multistreaming er indbygget og gratis, intet gebyr per destination, intet vandmærke."),
         ("Til hvor mange cam-sites kan jeg udsende samtidigt?", "Så mange som din upload-båndbredde kan klare — hver destination forbruger sin egen bitrate."),
         ("Bruger den cloud-relay?", "Nej — SplitCam sender streams peer-to-peer direkte fra pc'en til hver platforms ingest."),
         ("Sænker multistreaming min pc?", "Kodning sker én gang og genbruges; hardware-kodning holder CPU-belastningen lav. Upload-båndbredde er den reelle grænse."),
     ]},
    {"slug": "livejasmin", "name": "LiveJasmin",
     "title": "Udsend på LiveJasmin med SplitCam — HD External Encoder",
     "desc": "Udsend på LiveJasmin med gratis SplitCam — Model Center External Encoder, HD 1080p-opsætning, multi-kamera scener og overlays. Intet vandmærke.",
     "kw": "livejasmin udsend, livejasmin obs, livejasmin external encoder, livejasmin rtmp, livejasmin stream key, livejasmin model setup",
     "h1html": 'Sådan udsender du på <span class="accent">LiveJasmin</span> med SplitCam',
     "h1short": "Udsend LiveJasmin",
     "card": "External-encoder-opsætning til LiveJasmins HD-only Model Center.",
     "intro": "LiveJasmin er flagskibet i Docler Holding — et af verdens største cam-netværk og en HD-only-platform. Den foretrukne broadcaster er deres egen <strong>JasminCAM</strong>-klient, men Model Center har også en officiel <strong>External Encoder</strong>-vej, som gratis <strong style='color:var(--text)'>SplitCam</strong> kobler direkte på — for multi-kamera scener, beauty-filtre og overlays på den samme HD-stream.",
     "quick": "Udsend på LiveJasmin med SplitCam: installér SplitCam, byg HD-scenen, i Model Center åbn <em>Settings → Broadcast → External Encoder</em>, kopiér server-URL og stream key, indsæt i SplitCam, Go Live."
              "<ol><li>Installér SplitCam.</li><li>Tilføj kamera + HD-scene.</li>"
              "<li>Hent URL og stream key fra Model Center.</li><li>Indsæt i SplitCam.</li>"
              "<li>Tryk Go Live.</li></ol>",
     "key_how": "Log ind på <strong>modelcenter.livejasmin.com</strong>, åbn <strong>Settings → Broadcast → External Encoder</strong>. Model Center viser en <strong>server-URL</strong> og en <strong>stream key</strong> bundet til din konto — kopiér begge ind i SplitCams custom RTMP-felter. <strong>Bemærk:</strong> Nye konti skal godkendes (48–72 timer), før External Encoder-valget dukker op, og platformen tvinger HD-only output igennem.",
     "tips": [
         ("HD eller du falder i ranking", "LiveJasmin er HD-only — alt under 1280×720 risikerer kun at blive vist på de lavtbetalende lister, og alt under 1080p mister «Premium»-status. Sigt efter 1920×1080 ved 30 fps, 4.000–6.000 Kbps."),
         ("JasminCAM vs. external encoder", "Doclers egen JasminCAM-klient giver den reneste HD-compliance, men eksterne encodere (OBS, SplitCam, vMix) er officielt understøttet, når kontoen er godkendt — og kun derigennem får du multi-kamera scener og overlays, som JasminCAM ikke kan."),
         ("Free chat ≠ private show", "Free chat er kun preview — ingen nøgenhed. Private og Gold shows er der, hvor modellen tjener. Byg scenen, så den ser stærk ud både påklædt OG i show-tilstand."),
         _T_ETH,
     ],
     "faq": [
         ("Understøtter LiveJasmin officielt eksterne encodere som SplitCam?", "Ja — Model Center har External Encoder-valget under Settings → Broadcast. JasminCAM er den anbefalede klient, men OBS, SplitCam og andre RTMP-encodere er udtrykkeligt nævnt som understøttede, når din model-konto er godkendt."),
         ("Hvor finder jeg min LiveJasmin stream key?", "Inde i Model Center: Settings → Broadcast → External Encoder. Både server-URL og en unik stream key dukker op der — kopiér begge ind i SplitCams custom RTMP-felter. Nøglen er bundet til din konto; behandl den som en adgangskode."),
         ("Hvilken bitrate til LiveJasmin?", "LiveJasmin er HD-only — sigt efter 1920×1080 ved 30 fps, 4.000–6.000 Kbps og keyframe hver 2. sekund. Mærkbart under det mister du Premium-mærket og falder i ranking."),
         ("Er SplitCam gratis at bruge med LiveJasmin?", "Ja — SplitCam er gratis, uden vandmærke og uden tidsbegrænsning. Det eneste, du skal levere, er at ramme LiveJasmins HD-krav, og dem klarer SplitCam nativt med 1080p-scenekomposition og beauty-filtre."),
     ],
     "steps": [
         ("Download og installér SplitCam", "SplitCam er gratis live-streaming-software til Windows og macOS — ingen tilmelding, intet kort, intet vandmærke. Det er den encoder, der sender din HD-video til LiveJasmin."),
         ("Byg HD-scenen", "Åbn SplitCam og tilføj webkameraet i 1080p-tilstand. Læg overlays, tekst, et ekstra kamera eller telefonen, beauty-filtre eller en AI-baggrund ovenpå — LiveJasmin kræver HD-kvalitet, og din komponerede scene skal se premium ud både i free chat OG i private shows."),
         ("Hent LiveJasmin-URL og stream key", "Log ind på <strong>modelcenter.livejasmin.com</strong> (kontoen skal være godkendt først — typisk 48–72 timer efter tilmelding). Åbn <strong>Settings → Broadcast → External Encoder</strong>. Siden viser en <strong>server-URL</strong> og en unik <strong>stream key</strong>. Kopiér begge."),
         ("Forbind SplitCam med LiveJasmin", "I SplitCam åbn <strong>Stream Settings</strong>, indsæt LiveJasmins server-URL og stream key i custom RTMP-felterne. Sæt bitrate til 4.000–6.000 Kbps ved 1920×1080, 30 fps, med 2 sekunders keyframe. Kør først den indbyggede hastighedstest — HD-streams er krævende."),
         ("Klik Go Live", "Tryk <strong>Go Live</strong> i SplitCam, og gå derefter online i LiveJasmin Model Center. Inden for ~10 sekunder når dit HD-feed LiveJasmins netværk. Næste gang er det ét klik — åbn SplitCam, Go Live, og gå online på LiveJasmin."),
     ]},
    {"slug": "myfreecams", "name": "MyFreeCams",
     "title": "Udsend på MyFreeCams (MFC) med SplitCam — uden om Model Web Broadcaster",
     "desc": "Udsend på MyFreeCams med gratis SplitCam — Model Admin External Broadcaster, MFC-token-økonomi, multi-kamera scener, overlays. Intet vandmærke, ingen tilmelding.",
     "kw": "myfreecams udsend, mfc external broadcaster, myfreecams obs, mfc rtmp, mfc stream key, model admin, mfc token",
     "h1html": 'Sådan udsender du på <span class="accent">MyFreeCams</span> med SplitCam',
     "h1short": "Udsend MyFreeCams",
     "card": "External-broadcaster-opsætning til MFC's tokenbaserede Model Admin.",
     "intro": "MyFreeCams (MFC) er en af de ældste cam-platforme — ren token-økonomi, ingen lang model-godkendelsesproces og en loyal Premium-medlemsbase. Standard-<em>Model Web Broadcaster</em> er et single-kamera browserværktøj, men Model Admin har også en <strong>External Broadcaster</strong>-mulighed, som gratis <strong style='color:var(--text)'>SplitCam</strong> kobler sig på — og åbner for multi-kamera scener, overlays og filtre på samme token-stream.",
     "quick": "Udsend på MyFreeCams med SplitCam: installér SplitCam, byg scenen, i <em>Model Admin → Broadcaster</em> skift fra Web Broadcaster til External Broadcaster, kopiér server-URL og stream key, indsæt i SplitCam, Go Live."
              "<ol><li>Installér SplitCam.</li><li>Tilføj kamera + scene.</li>"
              "<li>Hent URL og stream key fra Model Admin.</li><li>Indsæt i SplitCam.</li>"
              "<li>Tryk Go Live.</li></ol>",
     "key_how": "Log ind på MyFreeCams, åbn <strong>Model Admin → Broadcaster</strong>, og skift fra <em>Web Broadcaster</em> til <strong>External Broadcaster</strong>. Siden viser en <strong>server-URL</strong> (rtmp://publish.myfreecams.com…) og en <strong>stream key</strong> bundet til din model-konto — kopiér begge ind i SplitCams custom RTMP-felter. Nøglen er bundet til kontoen; behandl den som en adgangskode og nulstil, hvis den lækker.",
     "tips": [
         ("MFC = tokens, ikke abonnementer", "MFC er ren tipping- og token-økonomi — Premium-medlemmer kan tage private, men hovedindtægten kommer fra tips i free chat. Planlæg en scene, der tjener både påklædt og casual, ikke kun i nøgenshowet."),
         ("Web Broadcaster vs. External — vælg én gang", "Standard Web Broadcaster er single-kamera, single-kilde. External Broadcaster åbner for multi-scene, overlays og beauty-filtre via SplitCam/OBS. Skift i Model Admin → Broadcaster, før du går live."),
         ("MFC Alerts-integration", "Animerede tip-alerts kommer fra mfcalerts.com — tilføj alert-URL'en som Browser-lag i SplitCam over kameraet. Fuld overlay-opsætning står i vores MFC Alerts-guide."),
         _T_ETH,
     ],
     "faq": [
         ("Understøtter MyFreeCams officielt eksterne broadcastere som SplitCam?", "Ja — Model Admin har en External Broadcaster-mulighed, der leverer en standard RTMP-server-URL og stream key. OBS, SplitCam, vMix og andre RTMP-encodere fungerer alle."),
         ("Hvor finder jeg min MFC stream key?", "Model Admin → Broadcaster → skift til External Broadcaster. Både server-URL (rtmp://publish.myfreecams.com…) og stream key dukker op der. Kopiér begge ind i SplitCams custom RTMP-felter."),
         ("Hvilken bitrate til MyFreeCams?", "MFC accepterer op til ~6.000 Kbps med 2 sekunders keyframe-interval. Sigt efter 1920×1080 ved 30 fps, 3.500–6.000 Kbps — din upload er den reelle grænse."),
         ("Er SplitCam gratis at bruge med MyFreeCams?", "Ja — SplitCam er gratis, uden vandmærke og uden tidsbegrænsning. External Broadcaster-mulighed i Model Admin er også gratis. Samlede broadcaster-omkostninger: nul."),
     ],
     "steps": [
         ("Download og installér SplitCam", "SplitCam er gratis live-streaming-software til Windows og macOS — ingen tilmelding, intet kort, intet vandmærke. Det er den encoder, der sender din video til MyFreeCams."),
         ("Byg scenen", "Åbn SplitCam og tilføj webkameraet. Læg overlays, tekst, et ekstra kamera eller telefonen, beauty-filtre eller en AI-baggrund ovenpå. Tilføj mfcalerts.com-URL'en som Browser-lag for animerede tip-alerts."),
         ("Skift til External Broadcaster i Model Admin", "Log ind på MyFreeCams. Åbn <strong>Model Admin → Broadcaster</strong>. Skift fra <em>Web Broadcaster</em> til <strong>External Broadcaster</strong>. Siden viser en <strong>server-URL</strong> og en unik <strong>stream key</strong>. Kopiér begge."),
         ("Forbind SplitCam med MyFreeCams", "I SplitCam åbn <strong>Stream Settings</strong>, indsæt MFC server-URL og stream key i custom RTMP-felterne. Sæt bitrate til 3.500–6.000 Kbps ved 1920×1080, 30 fps, med 2 sekunders keyframe-interval."),
         ("Klik Go Live", "Tryk <strong>Go Live</strong> i SplitCam. Inden for ~10 sekunder når din stream MyFreeCams. Næste gang er det ét klik."),
     ]},
    {"slug": "cherry-tv", "name": "Cherry.tv",
     "title": "Udsend på Cherry.tv med SplitCam — Web3-venlig External Encoder",
     "desc": "Udsend på Cherry.tv med gratis SplitCam — Streamer Dashboard external encoder, krypto-venlig cam-platform, multi-kamera scener. Intet vandmærke, ingen tilmelding.",
     "kw": "cherry tv udsend, cherry.tv obs, cherry tv external encoder, cherry.tv rtmp, cherry.tv stream key, cherry tv streamer, web3 cam",
     "h1html": 'Sådan udsender du på <span class="accent">Cherry.tv</span> med SplitCam',
     "h1short": "Udsend Cherry.tv",
     "card": "External-encoder-opsætning til Cherry.tv's Streamer Dashboard.",
     "intro": "Cherry.tv er en nyere, hurtigtvoksende cam-platform med en Web3-vinkel — krypto-venlige udbetalinger og lavere adgangsbarriere end ældre netværk som LiveJasmin. Standardbroadcasteren er browserbaseret, men <strong>Streamer Dashboard</strong> har også en standard <strong>external encoder</strong>-vej, som gratis <strong style='color:var(--text)'>SplitCam</strong> kobler sig på — så du kan streame med multi-kamera scener, overlays og filtre.",
     "quick": "Udsend på Cherry.tv med SplitCam: installér SplitCam, byg scenen, i Streamer Dashboard åbn <em>Broadcast Settings → External Encoder</em>, kopiér server-URL og stream key, indsæt i SplitCam, Go Live."
              "<ol><li>Installér SplitCam.</li><li>Tilføj kamera + scene.</li>"
              "<li>Hent URL og stream key fra Streamer Dashboard.</li><li>Indsæt i SplitCam.</li>"
              "<li>Tryk Go Live.</li></ol>",
     "key_how": "Log ind på din Cherry.tv-streamer-konto, åbn <strong>Streamer Dashboard</strong> og naviger til <strong>Broadcast Settings → External Encoder</strong>. Siden viser en <strong>server-URL</strong> og <strong>stream key</strong> bundet til din konto — kopiér begge ind i SplitCams custom RTMP-felter. Nye streamer-konti skal gennemføre en kort basisverifikation, før external encoder-muligheden er fuldt aktiv.",
     "tips": [
         ("Lettere indgang, voksende trafik", "Cherry.tv onboarder hurtigere end ældre platforme (ingen 72-timers Docler-prøvning). Godt early-mover-spot til at bygge en følgerbase."),
         ("Krypto-udbetalinger tilgængelige", "Cherry.tv understøtter krypto-udbetaling ved siden af klassisk fiat — nyttigt i regioner, hvor traditionelle cam-netværks-udbetalinger er langsomme eller begrænsede."),
         ("Browser-broadcaster vs. external", "Browser-broadcasteren er bekvem, men single-kilde. SplitCam via External Encoder åbner for multi-kamera scener, overlays, beauty-filtre og AI-baggrund."),
         _T_ETH,
     ],
     "faq": [
         ("Understøtter Cherry.tv officielt eksterne encodere som SplitCam?", "Ja — Streamer Dashboard har External Encoder under Broadcast Settings. Standard RTMP-server-URL og stream key; OBS, SplitCam, vMix kan alle forbinde."),
         ("Hvor får jeg min Cherry.tv stream key?", "Streamer Dashboard → Broadcast Settings → External Encoder. Både server-URL og stream key dukker op der."),
         ("Hvilken bitrate til Cherry.tv?", "Sigt efter 1920×1080 ved 30 fps, 3.500–6.000 Kbps med 2 sekunders keyframe. Kør først SplitCams indbyggede hastighedstest."),
         ("Er SplitCam gratis at bruge med Cherry.tv?", "Ja — SplitCam er gratis, uden vandmærke og uden tidsbegrænsning."),
     ],
     "steps": [
         ("Download og installér SplitCam", "SplitCam er gratis live-streaming-software til Windows og macOS — ingen tilmelding, intet kort, intet vandmærke."),
         ("Byg scenen", "Åbn SplitCam og tilføj webkameraet. Læg overlays, tekst, et ekstra kamera, beauty-filtre eller en AI-baggrund ovenpå. Cherry.tv's publikum er yngre og platform-stærkt."),
         ("Hent Cherry.tv-URL og stream key", "Log ind på din Cherry.tv-streamer-konto, åbn <strong>Streamer Dashboard</strong>, naviger til <strong>Broadcast Settings → External Encoder</strong>. Kopiér begge."),
         ("Forbind SplitCam med Cherry.tv", "I SplitCam åbn <strong>Stream Settings</strong>, indsæt Cherry.tv server-URL og stream key i custom RTMP-felterne. Sæt bitrate til 3.500–6.000 Kbps ved 1920×1080, 30 fps."),
         ("Klik Go Live", "Tryk <strong>Go Live</strong> i SplitCam, og gå derefter online fra Streamer Dashboard på Cherry.tv."),
     ]},
]
