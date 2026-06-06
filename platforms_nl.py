# -*- coding: utf-8 -*-
"""Dutch (nl) content for cam-streaming-guides. One dict per platform, written
natively for Dutch and Flemish audiences."""

_T_ETH = ("Gebruik een bekabelde verbinding", "Ethernet verslaat wifi tijdens een lange "
          "stream — een verloren frame is een gemiste tip. Trek een kabel naar je stream-pc.")
_T_TEST = ("Doe eerst een privé-test", "Run een korte teststream om camera, audio, framing "
           "en overlays te checken voordat je de room voor publiek opent.")

PLATFORMS_NL = [
    {
        "slug": "chaturbate", "name": "Chaturbate",
        "title": "Streamen op Chaturbate met SplitCam — Token & RTMP",
        "desc": "Streamen op Chaturbate met gratis SplitCam — broadcast-token, RTMP, multi-camera scènes en overlays. Geen watermerk, geen registratie.",
        "kw": "chaturbate streamen, chaturbate broadcast token, chaturbate rtmp obs, chaturbate external encoder, chaturbate live",
        "h1html": 'Hoe je <span class="accent">Chaturbate</span> streamt met SplitCam',
        "h1short": "Streamen op Chaturbate",
        "card": "Token-gebaseerde setup met externe encoder op Chaturbate.",
        "intro": "Chaturbate is een van de grootste cam-platforms en draait op een token-economie. De browser-broadcaster is een vlakke single-camera tool — door over te schakelen naar de <strong style='color:var(--text)'>externe encoder</strong> met gratis <strong style='color:var(--text)'>SplitCam</strong> krijg je multi-camera scènes, overlays en filters op diezelfde token-stream.",
        "quick": "Streamen op Chaturbate met SplitCam: SplitCam installeren, scène opbouwen, op Chaturbate naar <em>Broadcast Yourself → My Broadcast</em>, broadcast-token kopiëren, in SplitCam plakken, Go Live."
                 "<ol><li>SplitCam installeren.</li><li>Camera + scène toevoegen.</li>"
                 "<li>Broadcast-token van Chaturbate kopiëren.</li><li>In SplitCam plakken.</li>"
                 "<li>Go Live drukken.</li></ol>",
        "key_how": "Op Chaturbate klik <strong>Broadcast Yourself</strong> om de pagina <strong>My Broadcast</strong> te openen, dan <strong>View RTMP/OBS broadcast information and stream key</strong>. De sleutel verschijnt als je <strong>broadcast-token</strong> — kopieer die. Behandel hem als wachtwoord; nooit publiek delen.",
        "tips": [
            ("Token is de sleutel", "Chaturbate gebruikt je broadcast-token in plaats van een generieke stream key. Behandel hem als wachtwoord en reset bij lekken."),
            ("Veel headroom", "Chaturbate's RTMP ingest accepteert tot 4K, 60 fps en hoge bitrate — je upload is de limiet, niet het platform. Keyframe elke 2 seconden."),
            _T_ETH, _T_TEST,
        ],
        "faq": [
            ("Staat Chaturbate OBS / externe encoders toe?", "Ja — Chaturbate ondersteunt externe encoders officieel en heeft een eigen «How do I set up OBS?»-artikel. Activeer met «Use External Encoder to Broadcast» in de broadcast-instellingen."),
            ("Waar is mijn Chaturbate stream key?", "Broadcast Yourself → My Broadcast → View RTMP/OBS broadcast information and stream key. De sleutel is je broadcast-token."),
            ("Welke bitrate voor Chaturbate?", "3.500–6.000 Kbps op 1080p is ruim genoeg. Chaturbate's plafond is hoog — de echte limiet is je upload; draai eerst de snelheidstest van SplitCam."),
            ("Is SplitCam gratis voor Chaturbate?", "Ja — volledig gratis, geen watermerk en geen tijdslimiet, dus de encoder vreet niet aan je token-verdiensten."),
        ],
    },
    {
        "slug": "cam4", "name": "CAM4",
        "title": "Streamen op CAM4 met SplitCam — External Encoder",
        "desc": "Streamen op CAM4 met gratis SplitCam — External Encoder, stream key, geo-blokkering en overlays. Geen watermerk, gratis gids.",
        "kw": "cam4 streamen, cam4.com, cam4 external encoder, cam4 stream key, cam4 rtmp obs",
        "h1html": 'Hoe je <span class="accent">CAM4</span> streamt met SplitCam',
        "h1short": "Streamen op CAM4",
        "card": "External Encoder op CAM4 met geo-controles.",
        "intro": "CAM4 is een wereldwijd cam-and-earn-platform met ingebouwde geo-controles — je kunt je stream in geselecteerde landen verbergen. Streamen via gratis <strong style='color:var(--text)'>SplitCam</strong> als externe encoder opent scènewissels en overlays die de basis-broadcaster niet doet.",
        "quick": "Streamen op CAM4 met SplitCam: SplitCam installeren, scène opbouwen, op CAM4 naar <em>Broadcast &amp; Earn Money → Start Broadcast → External Encoder</em>, Get Stream Key, in SplitCam plakken, Go Live."
                 "<ol><li>SplitCam installeren.</li><li>Camera + scène toevoegen.</li>"
                 "<li>Stream key van CAM4 ophalen.</li><li>In SplitCam plakken.</li>"
                 "<li>Go Live drukken.</li></ol>",
        "key_how": "Op CAM4 klik <strong>Broadcast</strong> → <strong>Broadcast &amp; Earn Money</strong> → <strong>Start Broadcast</strong>, dan <strong>External Encoder</strong> bovenaan. Vul geboortedatum, geslacht en land in, gebruik <strong>Get Stream Key</strong> en kopieer. Een groene slider in SplitCam's Stream Settings bevestigt de verbinding.",
        "tips": [
            ("Stel geo-restricties in", "CAM4 staat toe je stream in specifieke landen en regio's te verbergen — stel dit aan de CAM4-kant in vóór go-live."),
            ("Let op de groene slider", "CAM4's setup toont een groene slider in SplitCam's Stream Settings zodra de sleutel klopt — rood betekent: sleutel opnieuw checken."),
            ("Lagere bitrate dan gewoonlijk", "CAM4's ingest beperkt videobitrate tot ongeveer 3.000 Kbps — lager dan de meeste cam-sites. Duw niet hoger."),
            _T_ETH,
        ],
        "faq": [
            ("Ondersteunt CAM4 OBS / externe encoders officieel?", "Ja — CAM4 heeft een officiële OBS Guide op de support-site en raadt External Encoder aan voor de beste ervaring. SplitCam gebruikt dezelfde RTMP-route."),
            ("Kan ik mijn CAM4-stream geo-blokkeren?", "Ja — CAM4 heeft ingebouwde geo-restrictie om je stream in bepaalde landen te verbergen. Stel in op CAM4, niet in SplitCam."),
            ("Waar is mijn CAM4 stream key?", "Broadcast → Broadcast & Earn Money → Start Broadcast → External Encoder → Get Stream Key."),
            ("Welke bitrate voor CAM4?", "Lager dan gemiddeld — CAM4's ingest beperkt op ~3.000 Kbps bij 30 fps met 1-seconde keyframe. De officiële snelheidstest-tabel adviseert niet boven ~3.000 te gaan."),
        ],
    },
    {
        "slug": "bongacams", "name": "BongaCams",
        "title": "Streamen op BongaCams met SplitCam — External Encoder",
        "desc": "Streamen op BongaCams met gratis SplitCam — External Encoder, multi-camera scènes, overlays en AI-achtergrond. Geen watermerk.",
        "kw": "bongacams, bongcams, bongacams streamen, bongacams external encoder, bongacams rtmp obs",
        "h1html": 'Hoe je <span class="accent">BongaCams</span> streamt met SplitCam',
        "h1short": "Streamen op BongaCams",
        "card": "External Encoder-setup voor BongaCams.",
        "intro": "BongaCams is een wereldwijd cam-platform. Externe encoder-streaming staat niet altijd standaard aan — eenmaal ingeschakeld voert gratis <strong style='color:var(--text)'>SplitCam</strong> de stream met multi-camera scènes, overlays en AI-achtergrond.",
        "quick": "Streamen op BongaCams met SplitCam: SplitCam installeren, scène opbouwen, op BongaCams naar <em>Options → Broadcast settings → Select Encoder → External Encoder</em>, URL en sleutel kopiëren, in SplitCam plakken, Go Live."
                 "<ol><li>SplitCam installeren.</li><li>Camera + scène toevoegen.</li>"
                 "<li>URL en sleutel van BongaCams ophalen.</li><li>In SplitCam plakken.</li>"
                 "<li>Go Live drukken.</li></ol>",
        "key_how": "Op BongaCams open <strong>Options</strong> → <strong>Broadcast settings</strong> → <strong>Select Encoder</strong> → <strong>External Encoder</strong> en kopieer de getoonde server-URL en stream key. <strong>Als de External Encoder-knop niet verschijnt</strong>, neem contact op met BongaCams-support en vraag om externe codering op je account in te schakelen.",
        "tips": [
            ("Geen External Encoder-knop? Support", "BongaCams schakelt externe codering per account in — als de optie niet in Broadcast settings staat, activeert de support hem."),
            ("Match de resolutie", "BongaCams raadt aan dat de resolutie van je webcam en je stream gelijk zijn — bijvoorbeeld beide 1280×720."),
            _T_ETH, _T_TEST,
        ],
        "faq": [
            ("Waarom verschijnt de External Encoder-knop niet op BongaCams?", "Externe codering staat niet standaard aan op elk account — neem contact op met BongaCams-support om hem te activeren; daarna verschijnt de knop in Broadcast settings."),
            ("Moet ik mijn BongaCams-account verifiëren?", "Ja — streamen vereist 18+, een officieel ID voor leeftijdscontrole en account-goedkeuring voordat je live gaat."),
            ("Welke bitrate voor BongaCams?", "BongaCams' RTMP ingest beperkt videobitrate tot ongeveer 6.000 Kbps met 2-seconde keyframe — 3.500–6.000 op 1080p is de sweet spot; test je upload vooraf."),
            ("Is SplitCam gratis voor BongaCams?", "Ja — volledig gratis, geen watermerk en geen tijdslimiet, dus de encoder vreet niet aan je token-inkomsten op BongaCams."),
        ],
    },
    {
        "slug": "stripchat", "name": "Stripchat",
        "title": "Streamen op Stripchat met SplitCam — Strip Cam Setup",
        "desc": "Streamen op Stripchat — het strip-cam-platform — met gratis SplitCam. Externe software, token-sleutel, scènes en overlays.",
        "kw": "strip cam, stripchat live stream, stripchat streamen, stripchat external software, stripchat stream key, stripchat rtmp obs",
        "h1html": 'Hoe je <span class="accent">Stripchat</span> streamt met SplitCam',
        "h1short": "Streamen op Stripchat",
        "card": "External software-setup voor Stripchat-streams.",
        "intro": "Stripchat is een groot cam-platform met focus op interactiviteit. De <em>external software</em>-modus geeft je een token-gebaseerde sleutel — gooi die in gratis <strong style='color:var(--text)'>SplitCam</strong> om met scènes, overlays en filters te streamen in plaats van een vlakke camera.",
        "quick": "Streamen op Stripchat met SplitCam: SplitCam installeren, scène opbouwen, op Stripchat <em>Switch to external software</em> kiezen, stream key kopiëren, in SplitCam plakken, Go Live."
                 "<ol><li>SplitCam installeren.</li><li>Camera + scène toevoegen.</li>"
                 "<li>Stream key van Stripchat ophalen.</li><li>In SplitCam plakken.</li>"
                 "<li>Go Live drukken.</li></ol>",
        "key_how": "Op Stripchat kies <strong>Switch to external software</strong>, dan <strong>Show external software settings for the stream</strong>. Kopieer de stream key — Stripchat toont hem als token. Houd hem privé.",
        "tips": [
            ("Match resolutie met site", "Stripchat's FAQ waarschuwt: de resolutie in je software moet exact die van de site matchen, anders pixelt video. Stel beide gelijk in."),
            ("Let op de 2 Mbps-ondergrens", "Stripchat noemt 2 Mbps upload als minimum — en zegt zelf dat dat niet genoeg is voor OBS-streaming of multistreaming. Mik flink hoger."),
            ("De sleutel is een token", "De stream key van Stripchat is een token — kopieer exact, deel nooit, reset bij lekken."),
            _T_ETH,
        ],
        "faq": [
            ("Raadt Stripchat OBS / externe software aan?", "Ja — Stripchat's officiële FAQ raadt externe broadcast-software zoals OBS aan «om de beste video- en audiokwaliteit te bereiken». SplitCam werkt op dezelfde manier."),
            ("Hoe schakel ik Stripchat over op externe software?", "In het Broadcast Center kies Switch to External Broadcast Software (OBS), dan open je external software settings om de stream key (token) te onthullen."),
            ("Welke bitrate voor Stripchat?", "RTMP ingest accepteert tot ~6.000 Kbps met 2-seconde keyframe. 3.500–6.000 op 1080p is ideaal — maar moet ruim boven de 2 Mbps-minimum zitten, vooral voor OBS-streaming."),
            ("Is SplitCam gratis voor Stripchat?", "Ja — geen licentiekosten, geen watermerk, geen tijdslimiet: zelfs lange interactieve Stripchat-shows kosten niets aan de encoder-kant."),
        ],
    },
    {
        "slug": "onlyfans", "name": "OnlyFans",
        "title": "Live gaan op OnlyFans met SplitCam — Authorisatie of sleutel",
        "desc": "Live gaan op OnlyFans met gratis SplitCam — login via authorisatie of OBS Key, multi-camera scènes, overlays. Geen watermerk.",
        "kw": "live gaan op onlyfans, onlyfans live stream, onlyfans authorisatie splitcam, onlyfans obs key, onlyfans streaming software",
        "h1html": 'Hoe je <span class="accent">OnlyFans</span> live gaat met SplitCam',
        "h1short": "OnlyFans live",
        "card": "Authoriseer een keer of plak de sleutel — live op OnlyFans.",
        "intro": "OnlyFans live is voor je abonnees. SplitCam verbindt op <strong style='color:var(--text)'>twee manieren</strong> — log één keer in met je OnlyFans-account zodat SplitCam de stream key automatisch ophaalt en gesynchroniseerd houdt, of plak handmatig de OBS Key. Hoe dan ook stream je met multi-camera scènes, overlays en filters.",
        "quick": "Live op OnlyFans met SplitCam: SplitCam installeren, scène opbouwen, Stream Settings &rarr; Add Channel &rarr; OnlyFans openen en <em>Authorisatie</em> kiezen — inloggen met OnlyFans-account, SplitCam haalt de sleutel automatisch — en Go Live klikken. Met de gekoppelde account stel je OnlyFans-streamparameters in SplitCam in zonder de OnlyFans-site te openen.",
        "steps": [
            ("Download en installeer SplitCam",
             "SplitCam is gratis streaming-software voor Windows en macOS — geen registratie, geen creditcard, geen watermerk. Het is de encoder die je video naar OnlyFans stuurt."),
            ("Stel camera en scène in",
             "Open SplitCam en voeg je webcam toe. Bouw de scène die kijkers zien — overlays, tekst, tweede camera, beauty-filters of AI-achtergrond, live toegepast."),
            ("Verbinding — Methode 1: Authorisatie (aanbevolen)",
             "In SplitCam open <strong>Stream Settings</strong> &rarr; <strong>Add Channel</strong> &rarr; <strong>OnlyFans</strong> en kies <strong>Authorisatie</strong>. Log in met je OnlyFans-e-mail en wachtwoord. SplitCam koppelt je account, haalt de stream key automatisch op en houdt hem gesynchroniseerd — en laat je OnlyFans live-parameters binnen SplitCam beheren, ook tijdens of na de stream, zonder de OnlyFans-site te bezoeken."),
            ("Verbinding — Methode 2: Stream Key (handmatig)",
             "Liever niet inloggen? Gebruik de sleutel. Op OnlyFans ga naar <strong>Profile</strong> &rarr; <strong>Settings</strong> &rarr; sectie <strong>Other</strong> en kopieer de <strong>OBS Key</strong>. In SplitCam, Add Channel &rarr; OnlyFans, plak in het sleutelveld. Deze sleutel is statisch — om instellingen later te wijzigen ga je terug naar de OnlyFans-site."),
            ("Go Live",
             "Welke methode ook, druk in SplitCam op <strong>Go Live</strong>. Met Methode 1 kun je OnlyFans-parameters in realtime blijven aanpassen vanuit SplitCam; met Methode 2 blijft de sleutel zoals je hem hebt ingesteld."),
        ],
        "tips": [
            ("Authorisatie vs Stream Key", "Twee manieren om te verbinden: <strong>Authorisatie</strong> (één keer inloggen, sleutel wordt opgehaald en gesynchroniseerd — gemakkelijkste route) of <strong>Stream Key</strong> (kopieer de OBS Key op OnlyFans → Profile → Settings → Other en plak). Authorisatie scheelt het handmatige kopiëren."),
            ("Instellingen wijzigen zonder SplitCam te verlaten", "Met authorisatie blijft je account gekoppeld, dus pas OnlyFans live-parameters aan binnen SplitCam tijdens of na de stream — zonder via de OnlyFans-site te gaan."),
            ("Houd de bitrate bescheiden", "OnlyFans' RTMP ingest beperkt videobitrate tot ongeveer 2.500 Kbps — krapper dan de meeste cam-sites. Mik op 720p–1080p bij ~2.000–2.500."),
            _T_ETH,
        ],
        "faq": [
            ("Hoe verbind ik OnlyFans met SplitCam?", "Twee manieren. <strong>Authorisatie</strong> — Stream Settings → Add Channel → OnlyFans → inloggen met je OnlyFans-account, SplitCam haalt de sleutel automatisch op. Of <strong>Stream Key</strong> — kopieer de OBS Key op OnlyFans → Profile → Settings → Other en plak."),
            ("Kan ik OnlyFans live-instellingen wijzigen zonder de site te openen?", "Ja — met de authorisatie-methode blijft SplitCam gekoppeld aan je OnlyFans-account, zodat sleutel en instellingen automatisch synchroniseren. Wijzig alles binnen SplitCam tijdens of na de stream, zonder onlyfans.com te bezoeken."),
            ("Welke bitrate voor OnlyFans?", "Bescheiden — OnlyFans' RTMP ingest beperkt bitrate tot ongeveer 2.500 Kbps, krapper dan andere cam-platforms. Mik op 720p–1080p rond 2.000–2.500 Kbps."),
            ("Is SplitCam gratis voor OnlyFans live?", "Ja — gratis, geen watermerk en geen tijdslimiet. Geen kosten aan de encoder-kant."),
        ],
    },
    {
        "slug": "camplace", "name": "CamPlace",
        "title": "Streamen op CamPlace met SplitCam — Gratis gids",
        "desc": "Streamen op CamPlace met gratis SplitCam — externe encoder, RTMP-sleutel, scènes en overlays. Stap-voor-stap, geen watermerk.",
        "kw": "camplace streamen, camplace broadcasting software, camplace rtmp, camplace external encoder, camplace stream key",
        "h1html": 'Hoe je <span class="accent">CamPlace</span> streamt met SplitCam',
        "h1short": "Streamen op CamPlace",
        "card": "Externe encoder-setup voor CamPlace-streams.",
        "intro": "CamPlace is een cam-streamingplatform. Er is geen publiek OBS-artikel, dus de <strong style='color:var(--text)'>videogids hierboven</strong> is je referentie — gratis <strong style='color:var(--text)'>SplitCam</strong> verbindt via standaard RTMP en voegt scènes, overlays en AI-achtergrond toe die de basiscamera niet biedt.",
        "quick": "Streamen op CamPlace met SplitCam: SplitCam installeren, scène opbouwen, externe/RTMP-broadcasting op CamPlace activeren, server-URL en stream key kopiëren, in SplitCam plakken, Go Live. Volg de video hierboven voor de actuele route."
                 "<ol><li>SplitCam installeren.</li><li>Camera + scène toevoegen.</li>"
                 "<li>RTMP-sleutel van CamPlace ophalen.</li><li>In SplitCam plakken.</li>"
                 "<li>Go Live drukken.</li></ol>",
        "key_how": "Log in op CamPlace en open je broadcasting-instellingen. Schakel over op externe encoder / RTMP / OBS om <strong>server-URL</strong> en <strong>stream key</strong> te onthullen, kopieer beide. CamPlace publiceert geen officiële OBS-documentatie — de <strong>video hierboven</strong> is de meest betrouwbare stap-voor-stap-route door de huidige interface.",
        "tips": [
            ("Geen officiële OBS-gids — gebruik video", "CamPlace heeft geen publiek artikel over externe encoders; de video hierboven is de referentie voor de actuele route."),
            ("Standaard RTMP werkt", "Hoewel ongedocumenteerd, accepteert CamPlace standaard RTMP-server-URL en sleutel — SplitCam verbindt als custom RTMP-bestemming."),
            ("Stapel overlays in SplitCam", "Tip-doelen, naam en social handles als scènelagen — CamPlace's basiscamera voegt zoiets niet toe."),
            _T_ETH,
        ],
        "faq": [
            ("Heeft CamPlace een officiële OBS-gids?", "Geen publiek artikel over externe encoders gevonden. CamPlace accepteert standaard RTMP-URL en sleutel, dus SplitCam werkt — volg de video hierboven."),
            ("Ondersteunt CamPlace externe encoders?", "Ja — het accepteert een standaard RTMP stream key, dus SplitCam verbindt als custom RTMP-bestemming."),
            ("Welke bitrate voor CamPlace?", "CamPlace publiceert geen officieel getal — gebruik 3.500–6.000 Kbps op 1080p als veilige range en laat SplitCam's snelheidstest je echte plafond vastleggen."),
            ("Is SplitCam gratis voor CamPlace?", "Ja — gratis, geen watermerk en geen tijdslimiet. Omdat CamPlace geen eigen encoder levert, doet een gratis RTMP-tool het werk."),
        ],
    },
    {
        "slug": "camsoda", "name": "CamSoda",
        "title": "CamSoda live met SplitCam — Gratis setup",
        "desc": "CamSoda live met gratis SplitCam — Use OBS Broadcaster, regionale servers, scènes en overlays. Geen watermerk, gratis gids.",
        "kw": "camsoda live, camsoda streamen, camsoda obs broadcaster, camsoda rtmp obs, camsoda live broadcast",
        "h1html": 'Hoe je <span class="accent">CamSoda</span> streamt met SplitCam',
        "h1short": "Streamen op CamSoda",
        "card": "Use OBS Broadcaster-setup op CamSoda.",
        "intro": "CamSoda is een Amerikaans cam-platform bekend om interactieve, ongewone showformats. Het ondersteunt OBS-streaming officieel — er is een <strong style='color:var(--text)'>Use OBS Broadcaster</strong>-knop op de Go Live-pagina en een officiële OBS-gids op de CamSoda-wiki. Gratis <strong style='color:var(--text)'>SplitCam</strong> werkt op dezelfde manier.",
        "quick": "Streamen op CamSoda met SplitCam: SplitCam installeren, scène opbouwen, Use OBS Broadcaster klikken op CamSoda's Go Live-pagina, server-URL en stream key kopiëren, in SplitCam plakken, Go Live."
                 "<ol><li>SplitCam installeren.</li><li>Camera + scène toevoegen.</li>"
                 "<li>Use OBS Broadcaster op CamSoda klikken.</li>"
                 "<li>Server-URL + sleutel in SplitCam plakken.</li><li>Go Live drukken.</li></ol>",
        "key_how": "Op CamSoda's <strong>Go Live</strong>-pagina klik <strong>Use OBS Broadcaster</strong>. CamSoda toont de RTMP-server-URL en stream key — kopieer beide. Kies de regionale server (Noord-Amerika, Europa, Azië enz.) die het dichtst bij je staat. CamSoda's wiki heeft een volledige OBS-gids voor de details.",
        "tips": [
            ("Verifieer voor tips", "Op CamSoda kan iedereen streamen, maar om tips te ontvangen moet je CamSoda's verificatie afronden."),
            ("Kies de dichtstbijzijnde regionale server", "CamSoda biedt regionale ingest-servers — de dichtstbijzijnde (NA / Europa / Azië / Zuid-Amerika / Oceanië) verlaagt latency en dropped frames."),
            ("Plafond bij 1080p / 30 fps", "CamSoda's ingest gaat tot ongeveer 1080p, 30 fps en ~6.000 Kbps — niet hoger duwen."),
            _T_ETH,
        ],
        "faq": [
            ("Ondersteunt CamSoda OBS / externe encoders?", "Ja — officieel. Er is een Use OBS Broadcaster-knop op de Go Live-pagina en een OBS-gids op CamSoda's wiki, dus SplitCam werkt."),
            ("Moet ik mij verifiëren op CamSoda?", "Om te streamen, nee. Om tips te ontvangen, ja — CamSoda vereist eerst hun verificatieproces."),
            ("Welke resolutie ondersteunt CamSoda?", "Tot 1920×1080 bij 30 fps, ongeveer 6.000 Kbps maximum op RTMP ingest."),
            ("Is SplitCam gratis voor CamSoda?", "Ja — gratis, geen watermerk en geen tijdslimiet. Werkt met CamSoda's gratis Use OBS Broadcaster-modus, dus de hele chain is kosteloos."),
        ],
    },
    {
        "slug": "streamate", "name": "Streamate",
        "title": "Streamen op Streamate met SplitCam — Geïntegreerd kanaal",
        "desc": "Streamen op Streamate met gratis SplitCam — geïntegreerd kanaal, SM Connect-sleutel, scènes en overlays. Geen watermerk, snelle setup.",
        "kw": "streamate, streamate sm connect, streamate streamen, streamate broadcasting software, streamate rtmp",
        "h1html": 'Hoe je <span class="accent">Streamate</span> streamt met SplitCam',
        "h1short": "Streamen op Streamate",
        "card": "Streamate is een geïntegreerd kanaal in SplitCam — snelle setup.",
        "intro": "Streamate is een gevestigd cam-platform — en het is een van de <strong style='color:var(--text)'>voorgeconfigureerde bestemmingen</strong> in SplitCam's kanalenlijst, dus setup is sneller dan handmatige RTMP-invoer: kies Streamate, plak je sleutel, klaar.",
        "quick": "Streamen op Streamate met SplitCam: SplitCam installeren, scène opbouwen, op Streamate <em>SM Connect → Start Show</em> en sleutel kopiëren, dan in SplitCam <em>Stream Settings → Add Channel → Streamate</em> openen en plakken."
                 "<ol><li>SplitCam installeren.</li><li>Camera + scène toevoegen.</li>"
                 "<li>Sleutel via Streamate's SM Connect ophalen.</li>"
                 "<li>Add Channel → Streamate in SplitCam.</li><li>Go Live drukken.</li></ol>",
        "key_how": "Op Streamate open <strong>SM Connect</strong>, accepteer de voorwaarden, klik <strong>Start Show</strong> links en sluit het venster dat opent — kopieer dan je streaming-sleutel. In SplitCam open <strong>Stream Settings</strong> → <strong>Add Channel</strong>, kies <strong>Streamate</strong> uit de lijst en plak de sleutel. Een groene slider bevestigt de verbinding.",
        "tips": [
            ("Streamate is geïntegreerd", "Geen handmatige RTMP-URL — SplitCam heeft Streamate in de Add Channel-lijst; alleen selecteren en sleutel plakken."),
            ("Sluit het SM Connect-popup", "Na Start Show opent Streamate een venster — sluiten; het was er alleen om de streaming key zichtbaar te maken."),
            ("Fix resolutie op 1080p", "Het Video Resolution-veld in SM Connect kan stilletjes naar 1440 springen, wat niet daadwerkelijk wordt geleverd en je kwaliteit zonder waarschuwing verlaagt — zet handmatig op 1080p. Bitrate dat zakt bij een statisch beeld is normaal: Streamate's stream is adaptief."),
            _T_ETH, _T_TEST,
        ],
        "faq": [
            ("Is Streamate in SplitCam geïntegreerd?", "Ja — Streamate staat in SplitCam's Add Channel-lijst; je selecteert het in plaats van handmatig een RTMP-URL in te typen."),
            ("Waar is mijn Streamate streaming-sleutel?", "SM Connect → voorwaarden accepteren → Start Show → popup sluiten → sleutel kopiëren."),
            ("Welke bitrate voor Streamate?", "Streamate stelt geen hard plafond — 3.500–6.000 Kbps op 1080p werkt goed. De stream is adaptief, dus lagere bitrate bij statisch beeld is normaal, geen bug."),
            ("Is SplitCam gratis voor Streamate?", "Ja — gratis, geen watermerk en geen tijdslimiet; en omdat Streamate een geïntegreerd kanaal in SplitCam is, is er ook geen aparte encoder-kost."),
        ],
    },
    {
        "slug": "streamray", "name": "StreamRay",
        "title": "Streamen op StreamRay cam met SplitCam — Chat-URL",
        "desc": "Streamen op StreamRay cam met gratis SplitCam — URL in chat gepost, OBS Broadcaster-modus, scènes en overlays. Geen watermerk.",
        "kw": "streamray, streamray cam, streamray streamen, streamray obs broadcaster, streamray rtmp",
        "h1html": 'Hoe je <span class="accent">StreamRay</span> streamt met SplitCam',
        "h1short": "Streamen op StreamRay",
        "card": "Chat-URL externe encoder-setup voor StreamRay.",
        "intro": "StreamRay heeft een ongewone externe encoder-setup — het levert de stream-URL af in het <strong style='color:var(--text)'>chatvenster van de broadcast</strong> en gebruikt geen aparte stream key. Gratis <strong style='color:var(--text)'>SplitCam</strong> handelt deze URL-only flow af.",
        "quick": "Streamen op StreamRay met SplitCam: SplitCam installeren, scène opbouwen, op StreamRay OBS Broadcaster activeren, stream-URL uit het chatvenster kopiëren, in SplitCam plakken (sleutelveld leeg laten), Go Live."
                 "<ol><li>SplitCam installeren.</li><li>Camera + scène toevoegen.</li>"
                 "<li>StreamRay-URL uit chat kopiëren.</li>"
                 "<li>URL in SplitCam plakken.</li><li>Go Live drukken.</li></ol>",
        "key_how": "Op StreamRay dubbelklik <strong>Broadcast Now</strong>, open het <strong>Other</strong>-menu, kies <strong>OBS Broadcaster</strong> en <strong>Save and Close</strong>. StreamRay post dan je <strong>stream-URL in het chatvenster</strong> — kopieer daar. Laat SplitCam's stream key-veld <strong>leeg</strong>; StreamRay authenticeert puur via URL.",
        "tips": [
            ("URL is in chat", "StreamRay toont de stream-URL niet in een settings-vakje — het wordt gepost in het broadcast-chatvenster. Daar kopiëren."),
            ("Sleutelveld leeg laten", "StreamRay gebruikt geen aparte sleutel — alleen de URL. Niets in SplitCam's sleutelveld zetten."),
            _T_ETH, _T_TEST,
        ],
        "faq": [
            ("Waar is mijn StreamRay stream-URL?", "Na het activeren van OBS Broadcaster post StreamRay de URL in het chatvenster — uit chat kopiëren."),
            ("Waarom geen stream key op StreamRay?", "StreamRay authenticeert puur via URL — laat SplitCam's sleutelveld leeg."),
            ("Welke bitrate voor StreamRay?", "StreamRay noemt geen officieel plafond — mik op 3.500–6.000 Kbps op 1080p en draai SplitCam's snelheidstest, aangezien de URL-only flow geen bitrate-feedback geeft."),
            ("Is SplitCam gratis voor StreamRay?", "Ja — gratis, geen watermerk en geen tijdslimiet, wat past bij StreamRay's URL-only flow: één link plakken en je bent live."),
        ],
    },
    {
        "slug": "xlovecam", "name": "XLoveCam",
        "title": "Streamen op XLoveCam met SplitCam — RTMP-link & sleutel",
        "desc": "Streamen op XLoveCam met gratis SplitCam — RTMP-link en sleutel, regionale servers, scènes en overlays. Geen watermerk, gratis gids.",
        "kw": "xlovecam, x love cam, xlovecam streamen, xlovecam rtmp link, xlovecam stream key",
        "h1html": 'Hoe je <span class="accent">XLoveCam</span> streamt met SplitCam',
        "h1short": "Streamen op XLoveCam",
        "card": "RTMP-link + sleutel-setup voor XLoveCam.",
        "intro": "XLoveCam is een Europees meertalig cam-platform. De accountinstellingen tonen zowel een <strong style='color:var(--text)'>RTMP-link</strong> als een <strong style='color:var(--text)'>stream key</strong> — gratis <strong style='color:var(--text)'>SplitCam</strong> pakt beide en streamt met scènes en overlays.",
        "quick": "Streamen op XLoveCam met SplitCam: SplitCam installeren, scène opbouwen, op XLoveCam <em>My Account → settings</em> openen, RTMP-link en stream key kopiëren, beide in SplitCam plakken, show starten."
                 "<ol><li>SplitCam installeren.</li><li>Camera + scène toevoegen.</li>"
                 "<li>RTMP-link + sleutel van XLoveCam kopiëren.</li><li>Beide in SplitCam plakken.</li>"
                 "<li>Go Live drukken.</li></ol>",
        "key_how": "Op XLoveCam open <strong>My Account</strong> → <strong>settings</strong>. De settings tonen zowel een <strong>RTMP-link</strong> als een <strong>stream key</strong> — kopieer beide in SplitCam's server-URL en sleutelvelden, dan <strong>Start your show</strong> op XLoveCam.",
        "tips": [
            ("Kopieer link EN sleutel", "XLoveCam geeft je een RTMP-link EN een aparte stream key — beide nodig in SplitCam, niet één."),
            ("Meertalig publiek", "XLoveCam is Europees en meertalig — een duidelijke tekst-overlay in je taal helpt kijkers je te vinden."),
            ("Kies de dichtstbijzijnde server", "XLoveCam biedt regionale RTMP-servers — Europa, Noord-Amerika, Zuid-Amerika en Azië. De dichtstbijzijnde verlaagt latency en dropped frames."),
            _T_ETH,
        ],
        "faq": [
            ("Waar zijn XLoveCam's RTMP-gegevens?", "My Account → settings — toont zowel de RTMP-link als de sleutel."),
            ("Ondersteunt XLoveCam externe encoders?", "Ja — het levert een RTMP-link en een sleutel, dus SplitCam werkt als encoder."),
            ("Welke bitrate voor XLoveCam?", "XLoveCam publiceert geen vaste limiet; 3.500–6.000 Kbps op 1080p is ideaal. De dichtstbijzijnde regionale server kiezen telt evenveel als het getal — vermindert dropped frames."),
            ("Is SplitCam gratis voor XLoveCam?", "Ja — gratis, geen watermerk en geen tijdslimiet. XLoveCam's Europese meertalige publiek bereiken kost geen software-fee."),
        ],
    },
    {
        "slug": "soulcams", "name": "SoulCams",
        "title": "Streamen op SoulCams met SplitCam — OBS-instellingen",
        "desc": "Streamen op SoulCams met gratis SplitCam — OBS-instellingen, RTMP-server en sleutel, multi-camera scènes en overlays.",
        "kw": "soul cams, soulcams, soulcams streamen, soulcams obs, soulcams rtmp, soulcams broadcast",
        "h1html": 'Hoe je <span class="accent">SoulCams</span> streamt met SplitCam',
        "h1short": "Streamen op SoulCams",
        "card": "OBS-instellingen-setup voor SoulCams.",
        "intro": "SoulCams is een cam-platform waarvan de OBS-instellingen <strong style='color:var(--text)'>RTMP-server en stream key samen</strong> in één venster tonen. Plak beide in gratis <strong style='color:var(--text)'>SplitCam</strong> om met multi-camera scènes en overlays te streamen.",
        "quick": "Streamen op SoulCams met SplitCam: SplitCam installeren, scène opbouwen, op SoulCams Go Online → Settings → OBS klikken, server en sleutel kopiëren, beide in SplitCam plakken, Go Live."
                 "<ol><li>SplitCam installeren.</li><li>Camera + scène toevoegen.</li>"
                 "<li>SoulCams Settings → OBS openen.</li><li>Server + sleutel in SplitCam plakken.</li>"
                 "<li>Go Live drukken.</li></ol>",
        "key_how": "Op SoulCams log in en klik <strong>Go Online</strong>, dan open <strong>Settings</strong> → <strong>OBS</strong>. Het OBS-venster toont <strong>RTMP-server</strong> en <strong>stream key</strong> samen — beide in SplitCam kopiëren.",
        "tips": [
            ("Server en sleutel naast elkaar", "SoulCams toont RTMP-server en sleutel in hetzelfde OBS-venster — beide in één keer pakken."),
            ("Eerst Go Online", "OBS-instellingen verschijnen pas na klikken op Go Online op SoulCams — doe dat voordat je naar encoder-gegevens zoekt."),
            ("Blokkeer ongewenste regio's", "SoulCams staat geo-blokkering aan de model-kant toe — kies welke landen je stream niet kunnen zien voordat je op Go Online klikt."),
            _T_ETH, _T_TEST,
        ],
        "faq": [
            ("Waar zijn SoulCams' OBS-instellingen?", "Inloggen, Go Online klikken, dan Settings → OBS — RTMP-server en stream key worden samen getoond."),
            ("Ondersteunt SoulCams externe encoders?", "Ja — de OBS-instellingen geven RTMP-server en sleutel, dus SplitCam werkt."),
            ("Welke bitrate voor SoulCams?", "SoulCams noemt geen officieel getal — mik op 3.500–6.000 Kbps op 1080p en test je upload, want het OBS-venster toont geen bitrate-aanwijzing."),
            ("Is SplitCam gratis voor SoulCams?", "Ja — gratis, geen watermerk en geen tijdslimiet, dus een volledige SoulCams-show met multi-camera scènes en overlays kost niets aan de encoder-kant."),
        ],
    },
    {
        "slug": "imlive", "name": "ImLive",
        "title": "Streamen op ImLive met SplitCam — Virtuele camera",
        "desc": "Im Live stream-setup met gratis SplitCam — ImLive gebruikt je webcam direct (geen RTMP), verbind SplitCam als virtuele camera met scènes.",
        "kw": "im live stream, imlive splitcam, imlive streamen, imlive virtuele camera, imlive webcam, im live cam",
        "h1html": 'Hoe je <span class="accent">ImLive</span> gebruikt met SplitCam',
        "h1short": "SplitCam op ImLive",
        "card": "Virtuele camera-setup voor ImLive — geen RTMP.",
        "intro": "ImLive gebruikt je webcam direct in de browser — er is <strong style='color:var(--text)'>geen RTMP en geen stream key</strong>. Gratis <strong style='color:var(--text)'>SplitCam</strong> verbindt als <strong style='color:var(--text)'>virtuele camera</strong>: bouw je scène in SplitCam, kies dan SplitCam als camera in ImLive.",
        "quick": "SplitCam op ImLive gebruiken: SplitCam installeren, scène met media-lagen opbouwen, ImLive openen en video chat starten, in ImLive-instellingen SplitCam als webcam en microfoon kiezen."
                 "<ol><li>SplitCam installeren.</li><li>Scène opbouwen in SplitCam.</li>"
                 "<li>Video chat starten op ImLive.</li>"
                 "<li>SplitCam kiezen als ImLive-camera.</li><li>Chat starten.</li></ol>",
        "steps": [
            ("SplitCam installeren",
             "SplitCam is gratis software voor Windows en macOS. Installeren — geen watermerk, geen registratie. Voor ImLive werkt het als <strong>virtuele camera</strong>, niet als RTMP-encoder."),
            ("Scène opbouwen in SplitCam",
             "Open SplitCam en gebruik <strong>Media Layers +</strong> om je webcam plus overlays, tekst, filters of AI-achtergrond toe te voegen. Deze samengestelde scène is wat ImLive als je camera ziet."),
            ("Video chat starten op ImLive",
             "Log in op de ImLive-site en klik <strong>Start Video Chat</strong>, dan open <strong>Go To Settings</strong> om bij camera- en microfoon-opties te komen."),
            ("SplitCam als camera kiezen",
             "Kies in ImLive-instellingen <strong>SplitCam</strong> als webcam EN als microfoon. ImLive toont nu je volledige SplitCam-scène in plaats van een vlakke webcam."),
            ("Start Free Live Chat",
             "Klik <strong>Free Live Chat</strong> op ImLive om live te gaan. Om de look midden in de sessie te wijzigen, bewerk de scène in SplitCam — ImLive update direct."),
        ],
        "tips": [
            ("Geen stream key nodig", "ImLive heeft geen RTMP — niet naar server-URL of sleutel zoeken. SplitCam wordt alleen als camera-apparaat geselecteerd."),
            ("Stel SplitCam ook in als mic", "Kies SplitCam voor de microfoon naast de camera, zodat je audiomix en ruisonderdrukking ook live komen."),
            ("Bouw de scène vóór go-live", "ImLive toont wat SplitCam uitstuurt — schik je lagen voordat je de chat start."),
            _T_TEST,
        ],
        "faq": [
            ("Gebruikt ImLive RTMP of stream key?", "Nee — ImLive gebruikt je webcam rechtstreeks via de browser. SplitCam verbindt als virtuele camera, er is geen sleutel om te kopiëren."),
            ("Hoe kies ik SplitCam in ImLive?", "Start Video Chat → Go To Settings → kies SplitCam als webcam en microfoon."),
            ("Kan ik overlays gebruiken in ImLive?", "Ja — bouw ze in SplitCam's scène; ImLive toont het samengestelde resultaat."),
            ("Is SplitCam gratis voor ImLive?", "Ja — gratis, geen watermerk en geen tijdslimiet. Als virtuele camera voor ImLive voegt het geen kosten of branding aan je video chat toe."),
        ],
    },
    {
        "slug": "vxlive", "name": "VXLive",
        "title": "Streamen op VXLive met SplitCam — Officiële support",
        "desc": "Streamen op VXLive (VXModels / VISIT-X) met gratis SplitCam — officiële VISIT-X preset, server en sleutel, scènes. Geen watermerk.",
        "kw": "vxlive, visit-x, vxmodels splitcam, vxlive streamen, visit-x stream, vxlive rtmp",
        "h1html": 'Hoe je <span class="accent">VXLive</span> streamt met SplitCam',
        "h1short": "Streamen op VXLive",
        "card": "VXLive ondersteunt SplitCam officieel (VISIT-X preset).",
        "intro": "VXLive (VXModels / VISIT-X) is een cam-platform van de Duitse markt — en een van de weinige die <strong style='color:var(--text)'>SplitCam officieel bij naam ondersteunt</strong>. VXModels heeft een gewijd help-artikel voor het verbinden van <strong style='color:var(--text)'>SplitCam</strong> aan VXLive, en SplitCam levert VISIT-X als kant-en-klaar kanaal-preset.",
        "quick": "Streamen op VXLive met SplitCam: SplitCam installeren, scène opbouwen, op VXLive «Stream with third-party software» kiezen, server-URL en sleutel kopiëren, in SplitCam de VISIT-X preset kiezen en plakken, Go Live in SplitCam, dan GO ONLINE op VXLive."
                 "<ol><li>SplitCam installeren.</li><li>Camera + scène toevoegen.</li>"
                 "<li>Server-URL + sleutel van VXLive ophalen.</li>"
                 "<li>VISIT-X preset in SplitCam kiezen, plakken.</li>"
                 "<li>Go Live, dan GO ONLINE op VXLive.</li></ol>",
        "key_how": "Op VXLive kies <strong>Stream with third-party software</strong> en selecteer de optie voor <strong>OBS, SplitCam of XSplit</strong>. VXLive levert een <strong>server-URL</strong> en een <strong>stream key</strong>. In SplitCam kies <strong>VISIT-X</strong> als streamingplatform, plak beide, druk <strong>Go Live</strong> in SplitCam, dan <strong>GO ONLINE</strong> op VXLive.",
        "tips": [
            ("VISIT-X is geïntegreerde preset", "Geen ruwe RTMP-URL invoeren — SplitCam heeft VISIT-X in de platformenlijst; alleen selecteren en server-URL + sleutel plakken."),
            ("Twee-staps go-live", "Op VXLive eerst Go Live in SplitCam, dan GO ONLINE op VXLive — beide, in die volgorde."),
            ("Duitse markt", "VXLive's publiek is overwegend Duitstalig — een Duitse tekst-overlay of titel helpt verbinding maken met kijkers."),
            _T_ETH,
        ],
        "faq": [
            ("Ondersteunt VXLive SplitCam officieel?", "Ja — VXModels (VXLive) heeft een officieel help-artikel gewijd aan SplitCam-setup en noemt SplitCam naast OBS en XSplit als ondersteunde broadcasting-software."),
            ("Hoe verbind ik SplitCam met VXLive?", "Op VXLive kies «Stream with third-party software», dan in SplitCam selecteer de VISIT-X preset en plak de server-URL en stream key die VXLive heeft gegeven."),
            ("Ga ik live in SplitCam of op VXLive?", "Beide — eerst Go Live in SplitCam, dan GO ONLINE op VXLive."),
            ("Waarom raadt VXModels SplitCam aan?", "Het officiële VXModels-help-artikel raadt SplitCam specifiek aan om webcam-beeldartefacten en pixelatie te elimineren en de verbinding te stabiliseren — niet alleen als generieke encoder."),
        ],
    },
    {
        "slug": "virtwish", "name": "VirtWish",
        "title": "Streamen op VirtWish met SplitCam — Stream-URL & sleutel",
        "desc": "Streamen op VirtWish met gratis SplitCam — Profile → Start Broadcast OBS-sectie, stream-URL en sleutel, scènes en overlays.",
        "kw": "virtwish, virtwish streamen, virtwish broadcasting software, virtwish rtmp, virtwish stream key, virtwish obs",
        "h1html": 'Hoe je <span class="accent">VirtWish</span> streamt met SplitCam',
        "h1short": "Streamen op VirtWish",
        "card": "Stream-URL + sleutel-setup voor VirtWish.",
        "intro": "VirtWish is een interactief cam-platform. De broadcast-instellingen geven je een <strong style='color:var(--text)'>stream-URL en een aparte stream key</strong> in een OBS-sectie — gratis <strong style='color:var(--text)'>SplitCam</strong> neemt beide en draait de show met scènes en overlays.",
        "quick": "Streamen op VirtWish met SplitCam: SplitCam installeren, scène opbouwen, op VirtWish <em>Profile → Start Broadcast</em> openen tot de OBS-sectie, link en sleutel kopiëren, beide in SplitCam plakken, Go Live."
                 "<ol><li>SplitCam installeren.</li><li>Camera + scène toevoegen.</li>"
                 "<li>URL + sleutel van VirtWish ophalen.</li><li>Beide in SplitCam plakken.</li>"
                 "<li>Go Live drukken.</li></ol>",
        "key_how": "Op VirtWish klik op het icoon rechtsboven → <strong>Profile</strong> → <strong>Start Broadcast</strong>, dan <strong>Start Broadcast</strong> opnieuw om bij de OBS-sectie te komen. <strong>Kopieer de link op de eerste regel</strong> in SplitCam's Stream URL-veld, en de <strong>Stream Key</strong> apart in het sleutelveld.",
        "tips": [
            ("Link op de eerste regel", "VirtWish's OBS-sectie zet de stream-URL op de eerste regel — die in SplitCam's Stream URL kopiëren, dan de aparte sleutel."),
            ("Twee keer Start Broadcast klikken", "Je klikt Start Broadcast tweemaal op VirtWish om bij de OBS-sectie te komen — dit is verwacht, geen bug."),
            _T_ETH, _T_TEST,
        ],
        "faq": [
            ("Waar zijn VirtWish' RTMP-gegevens?", "Icoon rechtsboven → Profile → Start Broadcast twee keer → de OBS-sectie toont link en stream key."),
            ("Ondersteunt VirtWish externe encoders?", "Ja — de OBS-sectie levert stream-URL en sleutel, dus SplitCam werkt."),
            ("Welke bitrate voor VirtWish?", "VirtWish publiceert geen officieel plafond; 3.500–6.000 Kbps op 1080p is veilig. Match SplitCam's resolutie met die op VirtWish om rescaling te vermijden."),
            ("Is SplitCam gratis voor VirtWish?", "Ja — gratis, geen watermerk en geen tijdslimiet. VirtWish's URL-en-sleutel-setup kost alleen de paar minuten die je nodig hebt."),
        ],
    },
    {
        "slug": "xmodels", "name": "XModels",
        "title": "Streamen op XModels met SplitCam — Gratis gids",
        "desc": "Streamen op XModels met gratis SplitCam — externe encoder-optie in model-accountinstellingen, RTMP-sleutel, scènes en overlays.",
        "kw": "xmodels, xmodels streamen, xmodels broadcasting software, xmodels rtmp, xmodels external encoder",
        "h1html": 'Hoe je <span class="accent">XModels</span> streamt met SplitCam',
        "h1short": "Streamen op XModels",
        "card": "Externe encoder-setup voor XModels-streams.",
        "intro": "XModels is een cam-streamingplatform met een ingebouwde <strong style='color:var(--text)'>externe encoder-optie</strong> in model-accountinstellingen. Gratis <strong style='color:var(--text)'>SplitCam</strong> streamt daarin met multi-camera scènes, overlays en filters in plaats van een enkele vlakke camera.",
        "quick": "Streamen op XModels met SplitCam: SplitCam installeren, scène opbouwen, externe encoder-optie in XModels-modelaccount aanzetten, server-URL en stream key kopiëren, in SplitCam plakken, Go Live."
                 "<ol><li>SplitCam installeren.</li><li>Camera + scène toevoegen.</li>"
                 "<li>Externe encoder in XModels-instellingen activeren.</li>"
                 "<li>Server-URL + sleutel in SplitCam plakken.</li><li>Go Live drukken.</li></ol>",
        "key_how": "In je XModels-<strong>modelaccountinstellingen</strong>, activeer de optie <strong>broadcasten via externe encoder</strong>. XModels levert een <strong>stream key</strong> — naar SplitCam kopiëren. Als de optie niet staat waar je verwacht, is XModels' support via FAQ-chat op de site en <strong>info@xmodels.com</strong>; de video hierboven loopt het ook door.",
        "tips": [
            ("Het zit in accountinstellingen", "XModels plaatst de externe encoder-optie in modelaccountinstellingen, niet op een aparte broadcast-pagina."),
            ("Support: chat + e-mail", "XModels heeft geen groot publiek help-center — FAQ-chat op de site en info@xmodels.com zijn de officiële supportkanalen."),
            ("Stapel overlays in SplitCam", "Tip-doelen, naam en social handles als scènelagen — XModels' basiscamera voegt zoiets niet toe."),
            _T_ETH,
        ],
        "faq": [
            ("Ondersteunt XModels externe encoders?", "Ja — modelaccountinstellingen bevatten een externe-encoder broadcast-optie die een stream key levert, dus SplitCam werkt."),
            ("Waar krijg ik XModels-hulp?", "XModels' support is via FAQ-chat op de site en info@xmodels.com e-mail — er is geen groot publiek help-center."),
            ("Welke bitrate voor XModels?", "XModels documenteert geen officieel getal — gebruik 3.500–6.000 Kbps op 1080p en draai SplitCam's snelheidstest, want XModels-support is alleen chat en e-mail."),
            ("Is SplitCam gratis voor XModels?", "Ja — gratis, geen watermerk en geen tijdslimiet, dus streamen naar XModels' Europese netwerk voegt geen software-kosten toe."),
        ],
    },
    {
        "slug": "flirt4free", "name": "Flirt4Free",
        "title": "Streamen op Flirt for Free cam met SplitCam — Gratis gids",
        "desc": "Streamen op Flirt for Free cam met gratis SplitCam — External Broadcast Form, RTMP URL en Stream Name, scènes en overlays.",
        "kw": "flirt for free cam, flirt 4 free cam, flirt4free, flirt4free streamen, flirt4free external broadcast, flirt4free rtmp",
        "h1html": 'Hoe je <span class="accent">Flirt4Free</span> streamt met SplitCam',
        "h1short": "Streamen op Flirt4Free",
        "card": "External Broadcast Form-setup voor Flirt4Free.",
        "intro": "Flirt4Free is een van de oudste cam-platforms, actief sinds de jaren '90. Het ondersteunt externe streaming officieel via een <strong style='color:var(--text)'>External Broadcast Form</strong> — gratis <strong style='color:var(--text)'>SplitCam</strong> verzendt de stream terwijl het formulier resolutie en bitrate vastlegt.",
        "quick": "Streamen op Flirt4Free met SplitCam: SplitCam installeren, scène opbouwen, Flirt4Free's External Broadcast Form openen, RTMP URL en Stream Name kopiëren en resolutie/bitrate instellen, in SplitCam plakken, Go Live."
                 "<ol><li>SplitCam installeren.</li><li>Camera + scène toevoegen.</li>"
                 "<li>Flirt4Free's External Broadcast Form openen.</li>"
                 "<li>RTMP URL + Stream Name in SplitCam plakken.</li>"
                 "<li>Go Live drukken.</li></ol>",
        "key_how": "In je Flirt4Free model area open het <strong>External Broadcast Form</strong>. Anders dan de meeste cam-sites geeft Flirt4Free je een <strong>RTMP URL</strong> en een <strong>Stream Name</strong> (geen «sleutel»), plus resolutie- en bitrate-velden die je in het formulier zelf invult. Kopieer URL en Stream Name in SplitCam's server- en sleutelvelden.",
        "tips": [
            ("Het is Stream Name, geen sleutel", "Flirt4Free noemt de credential Stream Name. In SplitCam's stream key-veld plakken — vervult dezelfde rol."),
            ("Stel resolutie/bitrate in het formulier in", "Flirt4Free's External Broadcast Form heeft eigen resolutie- en bitrate-velden — align met SplitCam's instellingen zodat het beeld niet wordt herschaald."),
            ("Historisch platform", "Flirt4Free draait sinds de jaren '90 — model-tools zijn volwassen en het External Broadcast Form is daar een gedocumenteerd onderdeel van."),
            _T_ETH,
        ],
        "faq": [
            ("Ondersteunt Flirt4Free externe encoders?", "Ja — officieel, via het External Broadcast Form dat RTMP URL en Stream Name levert. SplitCam werkt als encoder."),
            ("Waar krijg ik Flirt4Free's RTMP-gegevens?", "Uit het External Broadcast Form in de model area — toont RTMP URL, Stream Name en resolutie/bitrate-velden."),
            ("Welke bitrate voor Flirt4Free?", "3.500–6.000 Kbps op 1080p — stel dezelfde waarde in het External Broadcast Form als in SplitCam."),
            ("Is SplitCam gratis voor Flirt4Free?", "Ja — gratis, geen watermerk en geen tijdslimiet, wat goed past bij een historisch platform als Flirt4Free waar shows lang kunnen duren."),
        ],
    },
    {
        "slug": "mfc-alerts", "name": "MFC Alerts",
        "title": "MFC Alerts toevoegen aan je stream met SplitCam",
        "desc": "Toon geanimeerde tip-alerts in je MyFreeCams-stream — mfcalerts.com-URL als Browser-laag in gratis SplitCam, boven je webcam.",
        "kw": "mfc alerts, myfreecams alerts, mfc alerts toevoegen, mfcalerts splitcam, myfreecams tip alerts, myfreecams alerts overlay",
        "h1html": 'Hoe je <span class="accent">MFC Alerts</span> aan je stream toevoegt',
        "h1short": "MFC Alerts toevoegen",
        "card": "Toon geanimeerde tip-alerts in je MyFreeCams-stream.",
        "intro": "MFC Alerts toont geanimeerde effecten in je MyFreeCams-stream telkens als een kijker tipt. Het draait als <strong style='color:var(--text)'>Browser-laag</strong> in gratis <strong style='color:var(--text)'>SplitCam</strong> — één keer instellen en tips triggeren on-screen reacties live.",
        "quick": "MFC Alerts toevoegen met SplitCam: SplitCam installeren, webcam toevoegen, Browser-tab openen en mfcalerts.com laden, je alerts-URL kopiëren, als Browser-laag boven de webcam toevoegen, dan testen met een test-tip."
                 "<ol><li>SplitCam installeren.</li><li>Webcam toevoegen.</li>"
                 "<li>URL ophalen op mfcalerts.com.</li>"
                 "<li>Als Browser-laag boven webcam toevoegen.</li>"
                 "<li>Test-tip sturen.</li></ol>",
        "steps": [
            ("SplitCam installeren en webcam toevoegen",
             "Installeer gratis SplitCam voor Windows of macOS, voeg dan je <strong>webcam</strong> toe als bron. MFC Alerts ligt als laag boven deze camera."),
            ("Browser-tab openen en naar mfcalerts.com",
             "In SplitCam open de <strong>Browser</strong>-tab en navigeer naar <strong>www.mfcalerts.com</strong>. Log in, of meld je aan als je nog geen mfcalerts.com-account hebt."),
            ("Je alerts-URL kopiëren",
             "Op mfcalerts.com gebruik <strong>Copy to clipboard</strong> om je persoonlijke alerts-URL te kopiëren — dat is de pagina die de tip-animaties rendert."),
            ("URL als Browser-laag toevoegen — boven de webcam",
             "Plak de URL in SplitCam's Browser-venster en klik <strong>Add</strong>. Herschik dan je bronnenlijst zodat de <strong>MFC Alerts-laag boven je webcam</strong> staat (3-puntsmenu → Move Up). Als hij onder zit, blijven effecten verborgen."),
            ("Testen met een test-tip",
             "Open <strong>Settings → Send test tip</strong> en bevestig dat het alert-effect over je camera verschijnt. Stream dan normaal naar MyFreeCams — echte tips triggeren nu animaties."),
        ],
        "tips": [
            ("MFC Alerts moet boven webcam staan", "Veelgemaakte fout: als de MFC Alerts-laag onder de webcam in de bronnenlijst staat, blijven effecten verborgen. Naar boven verplaatsen."),
            ("mfcalerts.com-account vereist", "De alerts-URL is persoonlijk — meld je eerst aan op mfcalerts.com als je geen account hebt."),
            ("Stuur test-tip vóór go-live", "Gebruik Settings → Send test tip om te bevestigen dat de overlay werkt — niet pas midden in de show ontdekken."),
            _T_ETH,
        ],
        "faq": [
            ("Wat is MFC Alerts?", "Een meldingssysteem voor MyFreeCams dat video-effecten in je stream toont als kijkers tippen — als Browser-overlay in SplitCam toegevoegd."),
            ("Waarom verschijnen mijn MFC Alerts niet?", "Bijna altijd laag-volgorde — de MFC Alerts Browser-laag moet boven de webcam in SplitCam's bronnenlijst staan."),
            ("Heb ik een account nodig voor MFC Alerts?", "Ja — meld je aan op mfcalerts.com om je persoonlijke alerts-URL te krijgen."),
            ("Is SplitCam gratis hiervoor?", "Ja — SplitCam is gratis, geen watermerk en geen tijdslimiet, en de MFC Alerts browser-overlay draait erin zonder extra kosten."),
        ],
    },
    {
        "slug": "lovense", "name": "Lovense",
        "title": "Lovense-toy aan je stream toevoegen met SplitCam",
        "desc": "Interactieve Lovense-toy met je cam-stream verbinden met gratis SplitCam — Lovense SplitCam Toolset, on-screen tip-alerts, reacties.",
        "kw": "lovense aan stream toevoegen, lovense cam stream, lovense splitcam, lovense splitcam toolset, lovense interactive toy streaming",
        "h1html": 'Hoe je een <span class="accent">Lovense-toy</span> aan je stream toevoegt',
        "h1short": "Lovense-toy toevoegen",
        "card": "Verbind een interactieve Lovense-toy met je cam-stream.",
        "intro": "Draai je cam-stream via gratis <strong style='color:var(--text)'>SplitCam</strong> en koppel een <strong style='color:var(--text)'>Lovense</strong>-toy die op tokens reageert. Lovense documenteert een officieel <strong style='color:var(--text)'>Lovense SplitCam Toolset</strong>, en SplitCam levert een officiële Lovense-plugin — de integratie wordt aan beide kanten ondersteund.",
        "quick": "Om een Lovense-toy aan je stream toe te voegen: SplitCam en Lovense-software installeren, toy koppelen, Lovense aan je cam-platform linken, Lovense-status als Browser-laag in SplitCam toevoegen, dan normaal streamen."
                 "<ol><li>SplitCam installeren.</li><li>Lovense-software installeren en toy koppelen.</li>"
                 "<li>Lovense aan je cam-site linken.</li>"
                 "<li>Lovense-overlay in SplitCam toevoegen.</li><li>Go Live drukken.</li></ol>",
        "steps": [
            ("SplitCam installeren",
             "SplitCam is gratis streaming-software voor Windows en macOS — de encoder die je video naar je cam-platform stuurt. Installeren; geen watermerk."),
            ("Lovense-software installeren en toy koppelen",
             "Installeer Lovense Connect / Lovense Stream (de officiële desktop-app). Zet je toy aan en koppel via Bluetooth zodat de app verbonden toont."),
            ("Lovense aan je cam-platform linken",
             "Verbind in de Lovense-app je cam-account zodat de toy reageert op kijker-tokens / tips. De meeste grote cam-platforms worden ondersteund."),
            ("Lovense-overlay in SplitCam toevoegen",
             "Lovense levert een overlay/widget-URL. Voeg toe als <strong>Browser</strong>-laag in je SplitCam-scène zodat kijkers de toy-status en recente tips op scherm zien."),
            ("Scène bouwen en Go Live",
             "Voeg je camera en andere overlays toe, plak de RTMP-sleutel van je cam-platform in SplitCam, en klik <strong>Go Live</strong>. Toy reageert real-time op tips."),
        ],
        "tips": [
            ("Gebruik de officiële Lovense SplitCam Toolset", "Lovense publiceert een SplitCam-specifieke toolset met eigen installatiegids — het voegt toy-activiteits-overlay en tip-alerts toe die speciaal voor SplitCam zijn gemaakt."),
            ("Werk Lovense Cam Extension bij", "De toolset heeft een recente Lovense Cam Extension nodig (30.1.4 of nieuwer) — werk bij vóór go-live."),
            ("Houd toy opgeladen", "Een bijna-lege batterij midden in een show doodt de interactieve kant — laad volledig op vóór live."),
            ("Test reactie op tokens", "Stuur een kleine test-tip om te bevestigen dat de toy reageert voordat je je room opent."),
            ("Check versie-vereisten", "Lovense SplitCam Toolset vereist SplitCam 10.4.5 of nieuwer. Lovense Cam Extension dekt officieel Chaturbate, Stripchat, BongaCams, MyFreeCams en CamSoda — voor andere sites gebruik Lovense's Generic URL-integratie."),
        ],
        "faq": [
            ("Ondersteunt Lovense SplitCam officieel?", "Ja — Lovense documenteert een officiële «Lovense SplitCam Toolset» met eigen installatiegids, en SplitCam levert een officiële Lovense-plugin. De integratie wordt aan beide kanten ondersteund."),
            ("Verbindt de toy direct met SplitCam?", "Nee — de toy koppelt met de Lovense-app; SplitCam toont de Lovense-overlay en streamt je camera."),
            ("Welke cam-sites ondersteunen Lovense?", "Lovense's Cam Extension ondersteunt officieel Chaturbate, Stripchat, BongaCams, MyFreeCams en CamSoda, met wisselende ondersteuning voor andere — bekijk de actuele lijst in de Lovense-app."),
            ("Kan ik recente tips on-screen tonen?", "Ja — voeg Lovense's widget-URL toe als Browser-laag in SplitCam."),
        ],
    },
    {
        "slug": "multistream-cams", "name": "Meerdere cam-sites",
        "title": "Naar meerdere cam-sites tegelijk streamen met SplitCam",
        "desc": "Naar MyFreeCams, Chaturbate, BongaCams, CAM4, Stripchat en meer tegelijk streamen met SplitCam's gratis multistreaming. Eén klik, geen watermerk.",
        "kw": "naar meerdere cam-sites streamen, multistream cam sites, naar chaturbate en bongacams tegelijk streamen, multistream cam software",
        "h1html": 'Hoe je naar <span class="accent">meerdere cam-sites</span> tegelijk streamt',
        "h1short": "Cam-multistreaming",
        "card": "Naar meerdere cam-sites tegelijk streamen.",
        "intro": "Gratis <strong style='color:var(--text)'>SplitCam</strong> kan één encode naar <strong style='color:var(--text)'>meerdere cam-sites tegelijk</strong> streamen — MyFreeCams, Chaturbate, BongaCams, CAM4, Stripchat en meer. Geen watermerk, één klik.",
        "quick": "Om naar meerdere cam-sites tegelijk te streamen: SplitCam installeren, scène opbouwen, van elke cam-site de RTMP-server-URL en stream key ophalen, alle in SplitCam's multistreaming-instellingen toevoegen, één keer Go Live klikken."
                 "<ol><li>SplitCam installeren.</li><li>Camera + scène toevoegen.</li>"
                 "<li>RTMP-sleutel ophalen van elke cam-site.</li>"
                 "<li>Alle sleutels in SplitCam's multistream toevoegen.</li>"
                 "<li>Eén keer Go Live drukken.</li></ol>",
        "steps": [
            ("SplitCam installeren",
             "SplitCam is gratis streaming-software voor Windows en macOS met ingebouwde multistreaming. Installeren — geen watermerk, geen registratie."),
            ("Camera en scène opzetten",
             "Open SplitCam, voeg je webcam toe en bouw je scène met overlays en filters. Eén scène voedt elke bestemming."),
            ("RTMP-sleutel ophalen van elke cam-site",
             "Op elke cam-platform activeer externe/RTMP-broadcasting en kopieer <strong>server-URL</strong> en <strong>stream key</strong>. Herhaal voor elke site waar je wilt streamen — zie individuele platform-gidsen voor exacte routes."),
            ("Elke bestemming in SplitCam toevoegen",
             "Open <strong>Stream Settings</strong> en voeg elke cam-site toe als custom RTMP-bestemming — plak server-URL en sleutel. Vink alles aan wat live moet."),
            ("Één keer Go Live klikken",
             "Druk op <strong>Go Live</strong>. SplitCam stuurt je stream tegelijk naar elke geselecteerde cam-site, peer-to-peer, vanuit één enkele encode — zonder extra fee."),
        ],
        "tips": [
            ("Let op je upload", "Multistreaming vermenigvuldigt upload-load. Elke bestemming gebruikt zijn eigen bitrate — zorg dat je verbinding de som aankan."),
            ("Check platform-regels", "Sommige cam-sites verbieden gelijktijdig elders streamen — bevestig vóór multistreaming."),
            ("Bekabeld — drops kun je je hier niet veroorloven", "Multistreaming vermenigvuldigt upload-load, dus één wifi-drop kan alle bestemmingen tegelijk doen vallen. Bekabeld is hier niet optioneel."),
            ("Bekijk gezondheidsmonitor", "SplitCam toont status per bestemming — drop een site als je upload het niet trekt."),
        ],
        "faq": [
            ("Is SplitCam-multistreaming gratis?", "Ja — multistreaming is ingebouwd en gratis, geen fee per bestemming, geen watermerk."),
            ("Hoeveel cam-sites kan ik tegelijk streamen?", "Zoveel als je upload-bandbreedte aankan — elke bestemming gebruikt zijn eigen bitrate."),
            ("Gebruikt het cloud-relay?", "Nee — SplitCam stuurt streams peer-to-peer rechtstreeks van je pc naar elk platform's ingest."),
            ("Vertraagt multistreaming mijn pc?", "Codering gebeurt één keer en wordt hergebruikt; hardware-codering houdt CPU-load laag. Upload-bandbreedte is de echte limiet."),
        ],
    },
    {
        "slug": "livejasmin", "name": "LiveJasmin",
        "title": "Streamen op LiveJasmin met SplitCam — HD External Encoder",
        "desc": "Streamen op LiveJasmin met gratis SplitCam — Model Center External Encoder, HD 1080p-setup, multi-camera scènes en overlays. Geen watermerk, geen registratie.",
        "kw": "livejasmin streamen, livejasmin obs, livejasmin external encoder, livejasmin rtmp, livejasmin stream key, livejasmin model setup",
        "h1html": 'Hoe je <span class="accent">LiveJasmin</span> streamt met SplitCam',
        "h1short": "Streamen op LiveJasmin",
        "card": "External-encoder-setup voor het HD-only Model Center van LiveJasmin.",
        "intro": "LiveJasmin is het vlaggenschip van Docler Holding — een van de grootste cam-netwerken ter wereld en een HD-only platform. De voorkeursbroadcaster is de eigen <strong>JasminCAM</strong>-client, maar het Model Center biedt ook een officiële <strong>External Encoder</strong>-route waar gratis <strong style='color:var(--text)'>SplitCam</strong> direct op aansluit — voor multi-camera scènes, beauty-filters en overlays op dezelfde HD-stream.",
        "quick": "Streamen op LiveJasmin met SplitCam: SplitCam installeren, HD-scène opbouwen, in het Model Center naar <em>Settings → Broadcast → External Encoder</em>, server-URL en stream key kopiëren, in SplitCam plakken, Go Live."
                 "<ol><li>SplitCam installeren.</li><li>Camera + HD-scène toevoegen.</li>"
                 "<li>URL en stream key uit het Model Center halen.</li><li>In SplitCam plakken.</li>"
                 "<li>Go Live drukken.</li></ol>",
        "key_how": "Log in op <strong>modelcenter.livejasmin.com</strong> en open <strong>Settings → Broadcast → External Encoder</strong>. Het Model Center toont een aan je account gekoppelde <strong>server-URL</strong> en <strong>stream key</strong> — kopieer beide in de custom RTMP-velden van SplitCam. <strong>Let op:</strong> nieuwe accounts moeten eerst goedgekeurd worden (48–72 uur) voordat de External Encoder-optie verschijnt, en het platform forceert HD-only output.",
        "tips": [
            ("HD of je verliest je ranking", "LiveJasmin is HD-only — alles onder 1280×720 verschijnt alleen nog op de laag-betalende lijsten, en alles onder 1080p verliest het «Premium»-label. Mik op 1920×1080 bij 30 fps, 4.000–6.000 Kbps."),
            ("JasminCAM vs. external encoder", "De eigen JasminCAM-client van Docler levert de schoonste HD-compliance, maar externe encoders (OBS, SplitCam, vMix) zijn na accountgoedkeuring officieel ondersteund — alleen daarmee krijg je multi-camera scènes en overlays die JasminCAM niet kan."),
            ("Free chat ≠ private show", "Free chat is alleen preview — geen naakt. Private en Gold shows zijn waar de model verdient. Bouw je scène zo op dat hij sterk oogt zowel aangekleed als in show-modus."),
            _T_ETH,
        ],
        "faq": [
            ("Ondersteunt LiveJasmin externe encoders zoals SplitCam officieel?", "Ja — het Model Center heeft onder Settings → Broadcast de optie External Encoder. JasminCAM is de aanbevolen client, maar OBS, SplitCam en andere RTMP-encoders staan na goedkeuring van je modelaccount expliciet als ondersteund vermeld."),
            ("Waar haal ik mijn LiveJasmin stream key?", "In het Model Center: Settings → Broadcast → External Encoder. Daar verschijnen zowel de server-URL als een unieke stream key — beide plakken in de custom RTMP-velden van SplitCam. De key is aan je account gekoppeld; behandel hem als wachtwoord."),
            ("Welke bitrate voor LiveJasmin?", "LiveJasmin is HD-only — mik op 1920×1080 bij 30 fps, 4.000–6.000 Kbps met een keyframe-interval van 2 seconden. Merkbaar daaronder verlies je het Premium-label en raakt je ranking achterop."),
            ("Is SplitCam gratis te gebruiken met LiveJasmin?", "Ja — SplitCam is gratis, zonder watermerk en zonder tijdslimiet. De enige drempel zijn de HD-eisen van LiveJasmin, en die dekt SplitCam native af met 1080p-scènecompositie en beauty-filters."),
        ],
        "steps": [
            ("SplitCam downloaden en installeren", "SplitCam is gratis live-stream-software voor Windows en macOS — geen registratie, geen creditcard, geen watermerk. Het is de encoder die je HD-video naar LiveJasmin verstuurt."),
            ("HD-scène opbouwen", "Open SplitCam en voeg je webcam toe in 1080p-modus. Leg er overlays, tekst, een tweede camera of je telefoon overheen, beauty-filters of een AI-achtergrond — LiveJasmin eist HD-kwaliteit en je samengestelde scène moet er premium uitzien zowel in free chat als in private shows."),
            ("LiveJasmin-URL en stream key ophalen", "Log in op <strong>modelcenter.livejasmin.com</strong> (je account moet eerst goedgekeurd zijn — normaal 48–72 uur na aanmelden). Open <strong>Settings → Broadcast → External Encoder</strong>. De pagina toont een <strong>server-URL</strong> en een unieke <strong>stream key</strong>. Kopieer beide."),
            ("SplitCam koppelen aan LiveJasmin", "Open in SplitCam <strong>Stream Settings</strong>, plak de server-URL en stream key van LiveJasmin in de custom RTMP-velden. Zet bitrate op 4.000–6.000 Kbps bij 1920×1080, 30 fps en 2 seconden keyframe. Draai eerst de ingebouwde snelheidstest — HD-streams zijn veeleisend."),
            ("Klik Go Live", "Druk in SplitCam op <strong>Go Live</strong>, ga dan online in het LiveJasmin Model Center. Binnen ~10 seconden bereikt je HD-feed het netwerk van LiveJasmin. Volgende uitzendingen zijn één klik — SplitCam openen, Go Live, daarna online op LiveJasmin."),
        ],
    },
    {
        "slug": "myfreecams", "name": "MyFreeCams",
        "title": "Streamen op MyFreeCams (MFC) met SplitCam — Model Web Broadcaster omzeilen",
        "desc": "Streamen op MyFreeCams met gratis SplitCam — Model Admin External Broadcaster, MFC-token-economie, multi-camera scènes, overlays. Geen watermerk, geen registratie.",
        "kw": "myfreecams streamen, mfc external broadcaster, myfreecams obs, mfc rtmp, mfc stream key, model admin, mfc token",
        "h1html": 'Hoe je <span class="accent">MyFreeCams</span> streamt met SplitCam',
        "h1short": "Streamen op MyFreeCams",
        "card": "External-broadcaster-setup voor het token-gebaseerde Model Admin van MFC.",
        "intro": "MyFreeCams (MFC) is een van de oudste cam-platforms — pure token-economie, geen modelgoedkeurings-marathon en een trouwe Premium-member-basis. De standaard <em>Model Web Broadcaster</em> is een single-camera browser-tool, maar Model Admin biedt ook een <strong>External Broadcaster</strong>-optie waarmee gratis <strong style='color:var(--text)'>SplitCam</strong> verbindt — wat multi-camera scènes, overlays en filters op dezelfde tokenstream ontgrendelt.",
        "quick": "Streamen op MyFreeCams met SplitCam: SplitCam installeren, scène opbouwen, in <em>Model Admin → Broadcaster</em> overschakelen van Web Broadcaster naar External Broadcaster, server-URL en stream key kopiëren, in SplitCam plakken, Go Live."
                 "<ol><li>SplitCam installeren.</li><li>Camera + scène toevoegen.</li>"
                 "<li>URL en stream key uit Model Admin halen.</li><li>In SplitCam plakken.</li>"
                 "<li>Go Live drukken.</li></ol>",
        "key_how": "Log in op MyFreeCams, open <strong>Model Admin → Broadcaster</strong> en schakel over van <em>Web Broadcaster</em> naar <strong>External Broadcaster</strong>. De pagina toont een <strong>server-URL</strong> (rtmp://publish.myfreecams.com…) en een aan je model-account gekoppelde <strong>stream key</strong> — kopieer beide in de custom RTMP-velden van SplitCam. De key zit vast aan je account; behandel hem als wachtwoord en reset hem bij lekkage.",
        "tips": [
            ("MFC = tokens, geen abonnementen", "MFC draait puur op tipping en tokens — Premium-members kunnen private gaan, maar de bulk van het inkomen komt uit tips in free chat. Bouw een scène die ook aangekleed en casual verdient, niet alleen in de naaktshow."),
            ("Web Broadcaster vs. External — kies één keer", "De standaard Web Broadcaster is single-camera, single-source. External Broadcaster ontgrendelt multi-scène, overlays en beauty-filters via SplitCam/OBS. Schakel vóór het Go Live om in Model Admin → Broadcaster."),
            ("MFC Alerts-integratie", "Geanimeerde tip-alerts komen van mfcalerts.com — voeg de alert-URL als Browser-laag in SplitCam toe boven de camera. Volledige overlay-setup staat in onze MFC Alerts-gids."),
            _T_ETH,
        ],
        "faq": [
            ("Ondersteunt MyFreeCams externe broadcasters zoals SplitCam officieel?", "Ja — Model Admin heeft een External Broadcaster-optie die een standaard RTMP-server-URL en stream key levert. OBS, SplitCam, vMix en andere RTMP-encoders werken allemaal."),
            ("Waar haal ik mijn MFC stream key?", "Model Admin → Broadcaster → omschakelen naar External Broadcaster. Zowel de server-URL (rtmp://publish.myfreecams.com…) als de stream key verschijnen daar. Beide plakken in de custom RTMP-velden van SplitCam."),
            ("Welke bitrate voor MyFreeCams?", "MFC accepteert tot ~6.000 Kbps met een keyframe-interval van 2 seconden. Mik op 1920×1080 bij 30 fps, 3.500–6.000 Kbps — je upload is de echte limiet."),
            ("Is SplitCam gratis te gebruiken met MyFreeCams?", "Ja — SplitCam is gratis, zonder watermerk en zonder tijdslimiet. Ook de External Broadcaster-optie in Model Admin is gratis. Totale broadcaster-kosten: nul."),
        ],
        "steps": [
            ("SplitCam downloaden en installeren", "SplitCam is gratis live-stream-software voor Windows en macOS — geen registratie, geen creditcard, geen watermerk. Het is de encoder die je video naar MyFreeCams verstuurt."),
            ("Scène opbouwen", "Open SplitCam en voeg je webcam toe. Leg er overlays, tekst, een tweede camera of je telefoon overheen, beauty-filters of een AI-achtergrond. Voor geanimeerde tip-alerts: voeg de mfcalerts.com-URL als Browser-laag toe."),
            ("In Model Admin omschakelen naar External Broadcaster", "Log in op MyFreeCams. Open <strong>Model Admin → Broadcaster</strong>. Schakel om van <em>Web Broadcaster</em> naar <strong>External Broadcaster</strong>. De pagina toont een <strong>server-URL</strong> en een unieke <strong>stream key</strong>. Kopieer beide."),
            ("SplitCam koppelen aan MyFreeCams", "Open in SplitCam <strong>Stream Settings</strong>, plak de MFC-server-URL en stream key in de custom RTMP-velden. Zet bitrate op 3.500–6.000 Kbps bij 1920×1080, 30 fps en 2 seconden keyframe-interval."),
            ("Klik Go Live", "Druk in SplitCam op <strong>Go Live</strong>. Binnen ~10 seconden bereikt je stream MyFreeCams. Volgende uitzendingen zijn één klik."),
        ],
    },
    {
        "slug": "cherry-tv", "name": "Cherry.tv",
        "title": "Streamen op Cherry.tv met SplitCam — Web3-vriendelijke external encoder",
        "desc": "Streamen op Cherry.tv met gratis SplitCam — Streamer Dashboard external encoder, crypto-vriendelijk cam-platform, multi-camera scènes. Geen watermerk, geen registratie.",
        "kw": "cherry tv streamen, cherry.tv obs, cherry tv external encoder, cherry.tv rtmp, cherry.tv stream key, cherry tv streamer, web3 cam",
        "h1html": 'Hoe je <span class="accent">Cherry.tv</span> streamt met SplitCam',
        "h1short": "Streamen op Cherry.tv",
        "card": "External-encoder-setup voor het Streamer Dashboard van Cherry.tv.",
        "intro": "Cherry.tv is een nieuwer, snelgroeiend cam-platform met een Web3-insteek — crypto-vriendelijke uitbetalingen en een lagere instapdrempel dan oudere netwerken zoals LiveJasmin. De standaard broadcaster werkt in de browser, maar het <strong>Streamer Dashboard</strong> biedt ook een standaardpad voor een <strong>external encoder</strong> waar gratis <strong style='color:var(--text)'>SplitCam</strong> op aansluit — zodat je streamt met multi-camera scènes, overlays en filters.",
        "quick": "Streamen op Cherry.tv met SplitCam: SplitCam installeren, scène opbouwen, in het Streamer Dashboard <em>Broadcast Settings → External Encoder</em> openen, server-URL en stream key kopiëren, in SplitCam plakken, Go Live."
                 "<ol><li>SplitCam installeren.</li><li>Camera + scène toevoegen.</li>"
                 "<li>URL en stream key uit het Streamer Dashboard halen.</li><li>In SplitCam plakken.</li>"
                 "<li>Go Live drukken.</li></ol>",
        "key_how": "Log in op je Cherry.tv-streamer-account, open het <strong>Streamer Dashboard</strong> en navigeer naar <strong>Broadcast Settings → External Encoder</strong>. De pagina toont een aan je account gekoppelde <strong>server-URL</strong> en <strong>stream key</strong> — kopieer beide in de custom RTMP-velden van SplitCam. Nieuwe streamer-accounts moeten eerst een korte basisverificatie afronden voordat de external encoder-optie volledig actief is.",
        "tips": [
            ("Lagere instap, groeiend verkeer", "Cherry.tv onboardt sneller dan de oudere platforms (geen Docler-achtige 72-uurs review). Goede early-mover-plek om een volgers-basis op te bouwen."),
            ("Crypto-uitbetalingen beschikbaar", "Cherry.tv ondersteunt naast standaard fiat ook crypto-uitbetaling — handig in regio's waar klassieke cam-netwerk-uitbetalingen traag of beperkt zijn."),
            ("Browser-broadcaster vs. external", "De browser-broadcaster is handig maar single-source. SplitCam via External Encoder ontgrendelt multi-camera scènes, overlays, beauty-filters en AI-achtergrond."),
            _T_ETH,
        ],
        "faq": [
            ("Ondersteunt Cherry.tv externe encoders zoals SplitCam officieel?", "Ja — het Streamer Dashboard heeft onder Broadcast Settings de optie External Encoder. Standaard RTMP-server-URL en stream key; OBS, SplitCam, vMix sluiten allemaal aan."),
            ("Waar haal ik mijn Cherry.tv stream key?", "Streamer Dashboard → Broadcast Settings → External Encoder. Zowel de server-URL als de stream key verschijnen daar."),
            ("Welke bitrate voor Cherry.tv?", "Mik op 1920×1080 bij 30 fps, 3.500–6.000 Kbps met 2 seconden keyframe. Draai eerst de ingebouwde snelheidstest van SplitCam."),
            ("Is SplitCam gratis te gebruiken met Cherry.tv?", "Ja — SplitCam is gratis, zonder watermerk en zonder tijdslimiet."),
        ],
        "steps": [
            ("SplitCam downloaden en installeren", "SplitCam is gratis live-stream-software voor Windows en macOS — geen registratie, geen creditcard, geen watermerk."),
            ("Scène opbouwen", "Open SplitCam en voeg je webcam toe. Leg er overlays, tekst, een tweede camera, beauty-filters of een AI-achtergrond overheen. Het Cherry.tv-publiek is jonger en platform-vaardig."),
            ("Cherry.tv-URL en stream key ophalen", "Log in op je Cherry.tv-streamer-account, open het <strong>Streamer Dashboard</strong>, navigeer naar <strong>Broadcast Settings → External Encoder</strong>. Kopieer beide."),
            ("SplitCam koppelen aan Cherry.tv", "Open in SplitCam <strong>Stream Settings</strong>, plak de Cherry.tv-server-URL en stream key in de custom RTMP-velden. Zet bitrate op 3.500–6.000 Kbps bij 1920×1080, 30 fps."),
            ("Klik Go Live", "Druk in SplitCam op <strong>Go Live</strong>, ga dan online vanuit het Streamer Dashboard op Cherry.tv."),
        ],
    },
]
