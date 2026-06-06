# -*- coding: utf-8 -*-
"""German content for cam-streaming-guides. One dict per platform, written natively
for German-speaking audiences (DACH market)."""

_T_ETH = ("Kabelverbindung", "Ethernet ist bei langen Streams zuverlässiger als WLAN — "
          "ein verlorenes Frame ist ein verlorener Tipp. Zieh ein Kabel zum Streaming-PC.")
_T_TEST = ("Erst privat testen", "Mach einen kurzen Test-Stream, um Kamera, Ton, Bildaus"
           "schnitt und Overlays zu prüfen, bevor du den Raum öffentlich machst.")

PLATFORMS_DE = [
    {
        "slug": "chaturbate", "name": "Chaturbate",
        "title": "Auf Chaturbate streamen mit SplitCam — Token & RTMP",
        "desc": "Auf Chaturbate senden mit kostenlosem SplitCam — Broadcast-Token, RTMP, Multi-Cam-Szenen und Overlays. Ohne Wasserzeichen, ohne Registrierung.",
        "kw": "auf chaturbate streamen, chaturbate broadcast token, chaturbate rtmp obs, chaturbate external encoder, chaturbate live",
        "h1html": 'So streamst du auf <span class="accent">Chaturbate</span> mit SplitCam',
        "h1short": "Auf Chaturbate streamen",
        "card": "Token-Setup für Chaturbate über externen Encoder.",
        "intro": "Chaturbate ist eine der größten Cam-Plattformen mit Token-Ökonomie. Der Browser-Broadcaster zeigt nur eine flache Kamera — der Weg über den <strong style='color:var(--text)'>externen Encoder</strong> mit kostenlosem <strong style='color:var(--text)'>SplitCam</strong> bringt Multi-Cam-Szenen, Overlays und Filter auf denselben Token-Stream.",
        "quick": "Auf Chaturbate mit SplitCam senden: SplitCam installieren, Szene bauen, auf Chaturbate <em>Broadcast Yourself → My Broadcast</em> öffnen, Broadcast-Token kopieren, in SplitCam einfügen, Go Live."
                 "<ol><li>SplitCam installieren.</li><li>Kamera + Szene hinzufügen.</li>"
                 "<li>Chaturbate-Broadcast-Token kopieren.</li><li>In SplitCam einfügen.</li>"
                 "<li>Go Live drücken.</li></ol>",
        "key_how": "Auf Chaturbate auf <strong>Broadcast Yourself</strong> klicken, dann auf der <strong>My Broadcast</strong>-Seite <strong>View RTMP/OBS broadcast information and stream key</strong>. Der Key wird als <strong>Broadcast-Token</strong> angezeigt — kopieren. Behandle ihn wie ein Passwort, niemals öffentlich posten.",
        "tips": [
            ("Dein Token ist der Schlüssel", "Chaturbate verwendet deinen Broadcast-Token statt eines generischen Stream-Keys. Wie ein Passwort behandeln, bei Leak zurücksetzen."),
            ("Viel Reserve", "Der RTMP-Ingest akzeptiert bis zu 4K, 60 fps und sehr hohe Bitraten — die Grenze ist dein Upload, nicht die Plattform. Keyframe-Intervall 2 Sekunden."),
            _T_ETH, _T_TEST,
        ],
        "faq": [
            ("Erlaubt Chaturbate OBS / externe Encoder?", "Ja — Chaturbate unterstützt externe Encoder offiziell und hat einen eigenen «How do I set up OBS?»-Hilfeartikel. Aktivierung über «Use External Encoder to Broadcast» in den Broadcast-Einstellungen."),
            ("Wo finde ich meinen Chaturbate-Stream-Key?", "Broadcast Yourself → My Broadcast → View RTMP/OBS broadcast information and stream key. Der Key ist dein Broadcast-Token."),
            ("Welche Bitrate für Chaturbate?", "3.500–6.000 Kbps bei 1080p sind reichlich. Die Decke ist hoch — der Upload ist der Engpass; teste ihn zuerst mit dem SplitCam-Speedtest."),
            ("Ist SplitCam kostenlos für Chaturbate?", "Ja — vollständig kostenlos, ohne Wasserzeichen und ohne Zeitlimit, sodass der Encoder dir keinen Token wegnimmt."),
        ],
    },
    {
        "slug": "cam4", "name": "CAM4",
        "title": "Auf CAM4 streamen mit SplitCam — External Encoder",
        "desc": "Auf CAM4 senden mit kostenlosem SplitCam — External Encoder, Stream-Key, Geo-Blocking und Szenen-Overlays. Ohne Wasserzeichen, kostenlose Anleitung.",
        "kw": "auf cam4 streamen, cam4.com, cam4 external encoder, cam4 stream key, cam4 rtmp obs",
        "h1html": 'So streamst du auf <span class="accent">CAM4</span> mit SplitCam',
        "h1short": "Auf CAM4 streamen",
        "card": "External Encoder bei CAM4 mit Geo-Kontrollen.",
        "intro": "CAM4 ist eine globale Cam-and-Earn-Plattform mit eingebauten Geo-Kontrollen — du kannst deinen Stream in ausgewählten Ländern verstecken. Der Weg über kostenloses <strong style='color:var(--text)'>SplitCam</strong> als externen Encoder bringt Szenenwechsel und Overlays, die der einfache Broadcaster nicht kann.",
        "quick": "Auf CAM4 mit SplitCam senden: SplitCam installieren, Szene bauen, auf CAM4 <em>Broadcast &amp; Earn Money → Start Broadcast → External Encoder</em> öffnen, Get Stream Key, in SplitCam einfügen, Go Live."
                 "<ol><li>SplitCam installieren.</li><li>Kamera + Szene hinzufügen.</li>"
                 "<li>CAM4-Stream-Key holen.</li><li>In SplitCam einfügen.</li>"
                 "<li>Go Live drücken.</li></ol>",
        "key_how": "Auf CAM4 auf <strong>Broadcast</strong> → <strong>Broadcast &amp; Earn Money</strong> → <strong>Start Broadcast</strong> klicken, dann oben auf <strong>External Encoder</strong>. Geburtsdatum, Geschlecht und Land ausfüllen, mit <strong>Get Stream Key</strong> den Key holen und kopieren. Ein grüner Slider in den SplitCam Stream Settings bestätigt die Verbindung.",
        "tips": [
            ("Geo-Beschränkungen einstellen", "CAM4 lässt dich den Stream in bestimmten Ländern und Regionen verstecken — auf CAM4-Seite vor dem Go Live einstellen, wenn nötig."),
            ("Achte auf den grünen Slider", "Beim CAM4-Setup erscheint in den SplitCam Stream Settings ein grüner Slider, sobald der Key akzeptiert ist — Rot heißt: Key prüfen."),
            ("Strengere Bitrate", "Der CAM4-Ingest deckelt die Videobitrate bei ~3.000 Kbps — niedriger als die meisten Cam-Seiten. Nicht höher drehen."),
            _T_ETH,
        ],
        "faq": [
            ("Unterstützt CAM4 OBS / externe Encoder offiziell?", "Ja — CAM4 hat einen offiziellen OBS Guide auf seiner Support-Seite und empfiehlt die External-Encoder-Option für beste Qualität. SplitCam nutzt denselben RTMP-Pfad."),
            ("Kann ich meinen CAM4-Stream geo-blockieren?", "Ja — CAM4 hat eingebaute Geo-Restriktion, um deinen Stream in bestimmten Ländern zu verstecken. Einstellung auf CAM4, nicht in SplitCam."),
            ("Wo ist der CAM4-Stream-Key?", "Broadcast → Broadcast & Earn Money → Start Broadcast → External Encoder → Get Stream Key."),
            ("Welche Bitrate für CAM4?", "Niedriger als bei den meisten — der CAM4-Ingest deckelt bei ~3.000 Kbps, 30 fps, 1-Sekunden-Keyframe. Die offizielle OBS-Tabelle empfiehlt nicht über 3.000."),
        ],
    },
    {
        "slug": "bongacams", "name": "BongaCams",
        "title": "Auf BongaCams streamen mit SplitCam — External Encoder",
        "desc": "Auf BongaCams senden mit kostenlosem SplitCam — External Encoder, Multi-Cam-Szenen, Overlays und KI-Hintergrund. Ohne Wasserzeichen.",
        "kw": "bongacams, bongcams, auf bongacams streamen, bongacams external encoder, bongacams rtmp obs",
        "h1html": 'So streamst du auf <span class="accent">BongaCams</span> mit SplitCam',
        "h1short": "Auf BongaCams streamen",
        "card": "External-Encoder-Setup für BongaCams.",
        "intro": "BongaCams ist eine globale Cam-Plattform. Externer-Encoder-Streaming ist nicht standardmäßig aktiviert — nach Freischaltung steuert kostenloses <strong style='color:var(--text)'>SplitCam</strong> den Stream mit Multi-Cam-Szenen, Overlays und KI-Hintergrund.",
        "quick": "Auf BongaCams mit SplitCam senden: SplitCam installieren, Szene bauen, auf BongaCams <em>Options → Broadcast settings → Select Encoder → External Encoder</em>, URL und Key kopieren, in SplitCam einfügen, Go Live."
                 "<ol><li>SplitCam installieren.</li><li>Kamera + Szene hinzufügen.</li>"
                 "<li>BongaCams-URL und -Key holen.</li><li>In SplitCam einfügen.</li>"
                 "<li>Go Live drücken.</li></ol>",
        "key_how": "Auf BongaCams <strong>Options</strong> → <strong>Broadcast settings</strong> → <strong>Select Encoder</strong> → <strong>External Encoder</strong> öffnen, Server-URL und Stream-Key kopieren. <strong>Fehlt die External-Encoder-Schaltfläche</strong>, beim BongaCams-Support anfragen, externe Kodierung für dein Konto freizuschalten.",
        "tips": [
            ("Kein External-Encoder-Button? Support fragen", "BongaCams schaltet externe Kodierung pro Konto frei — wenn die Option in den Broadcast-Einstellungen fehlt, muss der Support sie aktivieren."),
            ("Auflösung angleichen", "BongaCams empfiehlt, Webcam- und Stream-Auflösung gleich einzustellen — etwa beide auf 1280×720."),
            _T_ETH, _T_TEST,
        ],
        "faq": [
            ("Warum fehlt der External-Encoder-Button bei BongaCams?", "Externe Kodierung ist nicht für jedes Konto standardmäßig aktiv — Support kontaktieren, dann erscheint der Button in den Broadcast-Einstellungen."),
            ("Muss ich mein Konto verifizieren?", "Ja — fürs Senden musst du 18+ sein, einen gültigen amtlichen Ausweis zur Altersprüfung haben und die Konto-Freigabe abwarten."),
            ("Welche Bitrate für BongaCams?", "Der RTMP-Ingest deckelt die Videobitrate bei ~6.000 Kbps mit 2-Sekunden-Keyframe — 3.500–6.000 bei 1080p ist optimal; Upload zuerst testen."),
            ("Ist SplitCam kostenlos für BongaCams?", "Ja — komplett kostenlos, ohne Wasserzeichen und ohne Zeitlimit, sodass der Encoder dir keine BongaCams-Tokens wegnimmt."),
        ],
    },
    {
        "slug": "stripchat", "name": "Stripchat",
        "title": "Auf Stripchat streamen mit SplitCam — Strip-Cam-Setup",
        "desc": "Auf Stripchat — der Strip-Cam-Plattform — mit kostenlosem SplitCam senden. Externe Software, Token-Key, Szenen und Overlays.",
        "kw": "strip cam, stripchat live stream, auf stripchat streamen, stripchat external software, stripchat stream key, stripchat rtmp obs",
        "h1html": 'So streamst du auf <span class="accent">Stripchat</span> mit SplitCam',
        "h1short": "Auf Stripchat streamen",
        "card": "External-Software-Setup für Stripchat-Streams.",
        "intro": "Stripchat ist eine große, interaktiv ausgerichtete Cam-Plattform. Der <em>external software</em>-Modus gibt dir einen tokenbasierten Key — gib ihn in kostenloses <strong style='color:var(--text)'>SplitCam</strong> und sende mit Szenen, Overlays und Filtern statt nur einer flachen Kamera.",
        "quick": "Auf Stripchat mit SplitCam senden: SplitCam installieren, Szene bauen, auf Stripchat <em>Switch to external software</em> wählen, Stream-Key kopieren, in SplitCam einfügen, Go Live."
                 "<ol><li>SplitCam installieren.</li><li>Kamera + Szene hinzufügen.</li>"
                 "<li>Stripchat-Stream-Key holen.</li><li>In SplitCam einfügen.</li>"
                 "<li>Go Live drücken.</li></ol>",
        "key_how": "Auf Stripchat <strong>Switch to external software</strong> wählen, dann <strong>Show external software settings for the stream</strong> öffnen. Stream-Key kopieren — Stripchat zeigt ihn als Token. Privat halten.",
        "tips": [
            ("Auflösung exakt mit der Seite abgleichen", "Stripchats FAQ warnt: Die Auflösung deiner Software muss exakt der auf der Seite entsprechen — sonst pixelt das Video. Beide gleich einstellen."),
            ("Auf das 2-Mbps-Minimum achten", "Stripchat nennt 2 Mbps Upload als Minimum — explizit nicht ausreichend für OBS-Streaming oder Multi-Plattform. Deutlich darüber zielen."),
            ("Der Key ist ein Token", "Der Stripchat-Stream-Key ist ein Token — exakt kopieren, nie teilen, bei Leak zurücksetzen."),
            _T_ETH,
        ],
        "faq": [
            ("Empfiehlt Stripchat OBS / externe Software?", "Ja — Stripchats eigenes FAQ rät zu externer Broadcast-Software wie OBS «to achieve better video and audio quality». SplitCam funktioniert genauso."),
            ("Wie schalte ich Stripchat auf externe Software um?", "Im Broadcast Center «Switch to External Broadcast Software (OBS)» wählen, dann die externen Software-Einstellungen öffnen, um den Stream-Key (Token) anzuzeigen."),
            ("Welche Bitrate für Stripchat?", "Der RTMP-Ingest akzeptiert bis ~6.000 Kbps mit 2-Sekunden-Keyframe. 3.500–6.000 bei 1080p ist ideal — aber deutlich über dem 2-Mbps-Minimum bleiben, besonders bei OBS-Streaming."),
            ("Ist SplitCam kostenlos für Stripchat?", "Ja — keine Lizenzgebühr, kein Wasserzeichen, kein Zeitlimit, sodass auch lange interaktive Stripchat-Shows beim Encoder nichts kosten."),
        ],
    },
    {
        "slug": "onlyfans", "name": "OnlyFans",
        "title": "Auf OnlyFans live gehen mit SplitCam — Autorisierung oder Key",
        "desc": "Auf OnlyFans live gehen mit kostenlosem SplitCam — Autorisierungs-Login oder OBS Key, Multi-Cam-Szenen, Overlays. Ohne Wasserzeichen.",
        "kw": "auf onlyfans live gehen, onlyfans live stream, onlyfans autorisierung splitcam, onlyfans obs key, onlyfans streaming software",
        "h1html": 'So gehst du auf <span class="accent">OnlyFans</span> live mit SplitCam',
        "h1short": "Auf OnlyFans live gehen",
        "card": "Einmal autorisieren oder Key einfügen — auf OnlyFans live gehen.",
        "intro": "OnlyFans-Livestreaming läuft für deine Abonnenten. SplitCam verbindet sich auf <strong style='color:var(--text)'>zwei Wegen</strong> — einmal mit OnlyFans-Login anmelden, dann holt sich SplitCam den Stream-Key und hält ihn synchron; oder OBS Key manuell einfügen. So oder so sendest du mit Multi-Cam-Szenen, Overlays und Filtern.",
        "quick": "Auf OnlyFans mit SplitCam live: SplitCam installieren, Szene bauen, Stream Settings &rarr; Add Channel &rarr; OnlyFans und <em>Autorisierung</em> wählen — mit OnlyFans-Login anmelden, SplitCam zieht den Stream-Key automatisch — dann Go Live. Mit verbundenem Konto kannst du die OnlyFans-Stream-Einstellungen direkt in SplitCam ändern, ohne die OnlyFans-Seite zu öffnen.",
        "steps": [
            ("SplitCam herunterladen und installieren",
             "SplitCam ist kostenlose Streaming-Software für Windows und macOS — keine Registrierung, keine Karte, kein Wasserzeichen. Es ist der Encoder, der dein Video an OnlyFans sendet."),
            ("Kamera und Szene einrichten",
             "Öffne SplitCam und füge deine Webcam hinzu. Baue die Szene für deine Zuschauer — Overlays, Text, zweite Kamera, Beauty-Filter oder KI-Hintergrund, alles live."),
            ("Verbindung — Methode 1: Autorisierung (empfohlen)",
             "In SplitCam <strong>Stream Settings</strong> &rarr; <strong>Add Channel</strong> &rarr; <strong>OnlyFans</strong> öffnen und <strong>Autorisierung</strong> wählen. Mit OnlyFans-E-Mail und -Passwort anmelden. SplitCam verbindet dein Konto, holt den Stream-Key automatisch und hält ihn synchron — und du kannst die OnlyFans-Stream-Einstellungen direkt in SplitCam während oder nach dem Stream ändern, ohne onlyfans.com zu öffnen."),
            ("Verbindung — Methode 2: Stream Key (manuell)",
             "Lieber nicht anmelden? Dann den Key. Auf OnlyFans <strong>Profile</strong> &rarr; <strong>Settings</strong> &rarr; Bereich <strong>Other</strong> und den <strong>OBS Key</strong> kopieren. In SplitCam Add Channel &rarr; OnlyFans, in das Stream-Key-Feld einfügen. Dieser Key ist statisch — um Einstellungen später zu ändern, zurück auf die OnlyFans-Seite."),
            ("Go Live",
             "Egal welche Methode, in SplitCam <strong>Go Live</strong> drücken. Mit Methode 1 kannst du die OnlyFans-Einstellungen weiter aus SplitCam anpassen; mit Methode 2 bleibt der Key exakt, wie du ihn gesetzt hast."),
        ],
        "tips": [
            ("Autorisierung vs Stream Key", "Zwei Wege zur Verbindung: <strong>Autorisierung</strong> (einmal anmelden, Key wird geholt und synchron gehalten — am einfachsten) oder <strong>Stream Key</strong> (OBS Key auf OnlyFans → Profile → Settings → Other kopieren und einfügen). Autorisierung erspart das manuelle Kopieren."),
            ("Einstellungen ohne SplitCam zu verlassen ändern", "Mit Autorisierung bleibt das Konto verbunden, du kannst die OnlyFans-Stream-Einstellungen direkt in SplitCam mitten im Stream oder danach anpassen — kein Abstecher auf die OnlyFans-Seite."),
            ("Bitrate moderat halten", "Der OnlyFans-RTMP-Ingest deckelt die Videobitrate bei ~2.500 Kbps — strenger als die meisten Cam-Seiten. Ziel: 720p–1080p bei ~2.000–2.500."),
            _T_ETH,
        ],
        "faq": [
            ("Wie verbinde ich OnlyFans mit SplitCam?", "Zwei Wege. <strong>Autorisierung</strong> — Stream Settings → Add Channel → OnlyFans → mit OnlyFans-Login anmelden, SplitCam holt den Stream-Key automatisch. Oder <strong>Stream Key</strong> — OBS Key auf OnlyFans → Profile → Settings → Other kopieren und einfügen."),
            ("Kann ich OnlyFans-Stream-Einstellungen ändern, ohne die Seite zu öffnen?", "Ja — bei Autorisierung bleibt SplitCam mit deinem OnlyFans-Konto verbunden, Key und Einstellungen synchronisieren sich automatisch. Du kannst sie in SplitCam während oder nach dem Stream ändern, ohne onlyfans.com zu besuchen."),
            ("Welche Bitrate für OnlyFans?", "Moderat halten — der OnlyFans-RTMP-Ingest deckelt die Videobitrate bei ~2.500 Kbps, deutlich strenger als die meisten Cam-Plattformen. Ziel: 720p–1080p bei rund 2.000–2.500 Kbps."),
            ("Ist SplitCam kostenlos für OnlyFans-Livestreams?", "Ja — kostenlos, kein Wasserzeichen, kein Zeitlimit. Bezahlt wird also nichts auf der Encoder-Seite."),
        ],
    },
    {
        "slug": "camplace", "name": "CamPlace",
        "title": "Auf CamPlace streamen mit SplitCam — kostenlose Anleitung",
        "desc": "Auf CamPlace senden mit kostenlosem SplitCam — externer Encoder, RTMP-Key, Szenen und Overlays. Schritt-für-Schritt-Anleitung, ohne Wasserzeichen.",
        "kw": "auf camplace streamen, camplace broadcasting software, camplace rtmp, camplace external encoder, camplace stream key",
        "h1html": 'So streamst du auf <span class="accent">CamPlace</span> mit SplitCam',
        "h1short": "Auf CamPlace streamen",
        "card": "External-Encoder-Setup für CamPlace-Streams.",
        "intro": "CamPlace ist eine Cam-Streaming-Plattform ohne öffentlichen OBS-Hilfeartikel — der <strong style='color:var(--text)'>Video-Guide oben</strong> ist die Referenz. Kostenloses <strong style='color:var(--text)'>SplitCam</strong> verbindet sich über Standard-RTMP und fügt Szenen, Overlays und KI-Hintergrund hinzu, die die einfache Kamera nicht kann.",
        "quick": "Auf CamPlace mit SplitCam senden: SplitCam installieren, Szene bauen, externes/RTMP-Streaming in CamPlace aktivieren, Server-URL und Stream-Key kopieren, in SplitCam einfügen, Go Live. Folge dem Video-Guide oben für den aktuellen Pfad."
                 "<ol><li>SplitCam installieren.</li><li>Kamera + Szene hinzufügen.</li>"
                 "<li>CamPlace-RTMP-Key holen.</li><li>In SplitCam einfügen.</li>"
                 "<li>Go Live drücken.</li></ol>",
        "key_how": "Auf CamPlace anmelden und die Broadcast-Einstellungen öffnen. Zur Option für externen Encoder / RTMP / OBS wechseln, um <strong>Server-URL</strong> und <strong>Stream-Key</strong> einzublenden, beide kopieren. CamPlace veröffentlicht keine offizielle OBS-Dokumentation — der <strong>Video-Guide oben</strong> ist die zuverlässigste Anleitung zur aktuellen Oberfläche.",
        "tips": [
            ("Kein offizieller OBS-Guide — Video nutzen", "CamPlace hat keinen öffentlichen Hilfeartikel zu externen Encodern; der Video-Guide oben ist die Referenz für den aktuellen Pfad."),
            ("Standard-RTMP funktioniert", "Auch ohne Doku akzeptiert CamPlace eine Standard-RTMP-Server-URL und einen Key — SplitCam verbindet sich als normales Custom-RTMP-Ziel."),
            ("Overlays in SplitCam schichten", "Tipp-Ziele, Name und Social-Handles als Szenenebenen — die einfache CamPlace-Kamera kann das nicht."),
            _T_ETH,
        ],
        "faq": [
            ("Hat CamPlace einen offiziellen OBS-Guide?", "Kein öffentlicher Hilfeartikel zu externen Encodern gefunden. CamPlace akzeptiert eine Standard-RTMP-URL und einen Key, also funktioniert SplitCam — folge dem Video-Guide oben."),
            ("Unterstützt CamPlace externe Encoder?", "Ja — es akzeptiert einen Standard-RTMP-Stream-Key, sodass SplitCam sich als Custom-RTMP-Ziel verbindet."),
            ("Welche Bitrate für CamPlace?", "CamPlace veröffentlicht keine offizielle Zahl — 3.500–6.000 Kbps bei 1080p als sicheren Bereich nehmen und den SplitCam-Speedtest deine echte Obergrenze festlegen lassen."),
            ("Ist SplitCam kostenlos für CamPlace?", "Ja — kostenlos, ohne Wasserzeichen und ohne Zeitlimit. Da CamPlace keinen eigenen Encoder mitliefert, reicht ein kostenloses RTMP-Tool völlig aus."),
        ],
    },
    {
        "slug": "camsoda", "name": "CamSoda",
        "title": "CamSoda live mit SplitCam — kostenloses Setup",
        "desc": "CamSoda live mit kostenlosem SplitCam — Use OBS Broadcaster, regionale Server, Szenen und Overlays. Ohne Wasserzeichen, kostenlose Anleitung.",
        "kw": "camsoda live, auf camsoda streamen, camsoda obs broadcaster, camsoda rtmp obs, camsoda live broadcast",
        "h1html": 'So streamst du auf <span class="accent">CamSoda</span> mit SplitCam',
        "h1short": "Auf CamSoda live",
        "card": "Use-OBS-Broadcaster-Setup für CamSoda.",
        "intro": "CamSoda ist eine US-Cam-Plattform, bekannt für interaktive Show-Formate. Sie unterstützt OBS-Streaming offiziell — auf der Go-Live-Seite gibt es einen <strong style='color:var(--text)'>Use OBS Broadcaster</strong>-Button und ein offizielles OBS-Guide im CamSoda-Wiki. Kostenloses <strong style='color:var(--text)'>SplitCam</strong> funktioniert genauso.",
        "quick": "Auf CamSoda mit SplitCam senden: SplitCam installieren, Szene bauen, auf CamSodas Go-Live-Seite Use OBS Broadcaster klicken, Server-URL und Stream-Key kopieren, in SplitCam einfügen, Go Live."
                 "<ol><li>SplitCam installieren.</li><li>Kamera + Szene hinzufügen.</li>"
                 "<li>Auf CamSoda Use OBS Broadcaster klicken.</li>"
                 "<li>Server-URL + Key in SplitCam einfügen.</li><li>Go Live drücken.</li></ol>",
        "key_how": "Auf CamSodas <strong>Go Live</strong>-Seite <strong>Use OBS Broadcaster</strong> klicken. CamSoda zeigt RTMP-Server-URL und Stream-Key — beide kopieren. Den regionalen Server (Nordamerika, Europa, Asien usw.) am nächsten zu dir wählen. Das offizielle CamSoda-Wiki hat einen vollständigen OBS-Guide, falls du Details brauchst.",
        "tips": [
            ("Verifizierung für Tipps", "Bei CamSoda kann jeder senden, aber für Tipps musst du die CamSoda-Verifizierung abschließen."),
            ("Nächstgelegenen regionalen Server wählen", "CamSoda bietet regionale Ingest-Server — den nächstgelegenen (NA / Europa / Asien / Südamerika / Ozeanien) wählen, das senkt Lag und verlorene Frames."),
            ("Bei 1080p / 30 fps deckeln", "Der CamSoda-Ingest reicht bis 1080p, 30 fps und ~6.000 Kbps — nicht höher drehen."),
            _T_ETH,
        ],
        "faq": [
            ("Unterstützt CamSoda OBS / externe Encoder?", "Ja — offiziell. Es gibt einen Use-OBS-Broadcaster-Button auf der Go-Live-Seite und ein OBS-Guide im CamSoda-Wiki, also funktioniert SplitCam."),
            ("Muss ich mich bei CamSoda verifizieren?", "Zum Senden nicht. Für Tipps ja — CamSoda verlangt zuerst den Abschluss der Verifizierungs-Application."),
            ("Welche Auflösung unterstützt CamSoda?", "Bis 1920×1080 bei 30 fps, etwa 6.000 Kbps Maximum auf dem RTMP-Ingest."),
            ("Ist SplitCam kostenlos für CamSoda?", "Ja — kostenlos, ohne Wasserzeichen und ohne Zeitlimit. Funktioniert neben CamSodas eigenem kostenlosen OBS-Broadcaster-Modus, die ganze Kette kostet nichts."),
        ],
    },
    {
        "slug": "streamate", "name": "Streamate",
        "title": "Auf Streamate streamen mit SplitCam — eingebauter Kanal",
        "desc": "Auf Streamate senden mit kostenlosem SplitCam — eingebauter Kanal, SM-Connect-Key, Szenen und Overlays. Ohne Wasserzeichen, schnelles Setup.",
        "kw": "streamate, streamate sm connect, auf streamate streamen, streamate broadcasting software, streamate rtmp",
        "h1html": 'So streamst du auf <span class="accent">Streamate</span> mit SplitCam',
        "h1short": "Auf Streamate streamen",
        "card": "Streamate ist ein eingebauter SplitCam-Kanal — schnelles Setup.",
        "intro": "Streamate ist eine etablierte Cam-Plattform — und eines der Ziele, die <strong style='color:var(--text)'>in SplitCams</strong> Kanalliste vorinstalliert sind, daher ist das Setup schneller als eine manuelle RTMP-Eingabe: Streamate wählen, Key einfügen, fertig.",
        "quick": "Auf Streamate mit SplitCam senden: SplitCam installieren, Szene bauen, auf Streamate über <em>SM Connect → Start Show</em> den Key kopieren, dann in SplitCam <em>Stream Settings → Add Channel → Streamate</em> öffnen und einfügen."
                 "<ol><li>SplitCam installieren.</li><li>Kamera + Szene hinzufügen.</li>"
                 "<li>Streamate-Key über SM Connect holen.</li>"
                 "<li>Add Channel → Streamate in SplitCam.</li><li>Go Live drücken.</li></ol>",
        "key_how": "Auf Streamate <strong>SM Connect</strong> öffnen, Bedingungen akzeptieren, links <strong>Start Show</strong> klicken und das aufgehende Fenster schließen — dann den Streaming-Key kopieren. In SplitCam <strong>Stream Settings</strong> → <strong>Add Channel</strong> öffnen, <strong>Streamate</strong> aus der Liste wählen und den Key einfügen. Ein grüner Slider bestätigt die Verbindung.",
        "tips": [
            ("Streamate ist ein eingebauter Kanal", "Du brauchst keine manuelle RTMP-URL — SplitCam hat Streamate in seiner Add-Channel-Liste, einfach auswählen und Key einfügen."),
            ("SM-Connect-Fenster schließen", "Nach Start Show öffnet Streamate ein Fenster — schließen; es war nur da, um den Streaming-Key zu zeigen."),
            ("Auflösung auf 1080p fixieren", "Das Video-Resolution-Feld in SM Connect kann auf 1440 springen, das real nicht ausgeliefert wird und still deine Qualität senkt — von Hand auf 1080p setzen. Fallende Bitrate bei Standbild ist normal: Streamates Feed ist adaptiv."),
            _T_ETH, _T_TEST,
        ],
        "faq": [
            ("Ist Streamate in SplitCam eingebaut?", "Ja — Streamate erscheint in SplitCams Add-Channel-Liste, du wählst es statt eine RTMP-URL manuell einzugeben."),
            ("Wo ist der Streamate-Streaming-Key?", "SM Connect → Bedingungen akzeptieren → Start Show → Pop-up-Fenster schließen → Key kopieren."),
            ("Welche Bitrate für Streamate?", "Streamate setzt keinen harten Deckel — 3.500–6.000 Kbps bei 1080p funktionieren gut. Der Feed ist adaptiv, eine niedrigere Bitrate bei Standbildern ist normal, kein Fehler."),
            ("Ist SplitCam kostenlos für Streamate?", "Ja — kostenlos, ohne Wasserzeichen und ohne Zeitlimit; und weil Streamate ein eingebauter SplitCam-Kanal ist, fallen auch keine separaten Encoder-Kosten an."),
        ],
    },
    {
        "slug": "streamray", "name": "StreamRay",
        "title": "Auf StreamRay Cam streamen mit SplitCam — URL aus dem Chat",
        "desc": "Auf StreamRay Cam senden mit kostenlosem SplitCam — URL aus dem Chat-Fenster, OBS-Broadcaster-Modus, Szenen und Overlays. Ohne Wasserzeichen.",
        "kw": "streamray, streamray cam, auf streamray streamen, streamray obs broadcaster, streamray rtmp",
        "h1html": 'So streamst du auf <span class="accent">StreamRay</span> mit SplitCam',
        "h1short": "Auf StreamRay streamen",
        "card": "URL-aus-Chat-Setup für StreamRay.",
        "intro": "StreamRay hat ein ungewöhnliches External-Encoder-Setup — die Stream-URL kommt ins <strong style='color:var(--text)'>Broadcast-Chat-Fenster</strong> und es gibt keinen separaten Stream-Key. Kostenloses <strong style='color:var(--text)'>SplitCam</strong> kommt mit diesem Nur-URL-Workflow gut zurecht.",
        "quick": "Auf StreamRay mit SplitCam senden: SplitCam installieren, Szene bauen, auf StreamRay den OBS Broadcaster aktivieren, Stream-URL aus dem Chat-Fenster kopieren, in SplitCam einfügen (Key-Feld leer lassen), Go Live."
                 "<ol><li>SplitCam installieren.</li><li>Kamera + Szene hinzufügen.</li>"
                 "<li>StreamRay-URL aus dem Chat kopieren.</li>"
                 "<li>URL in SplitCam einfügen.</li><li>Go Live drücken.</li></ol>",
        "key_how": "Auf StreamRay zweimal auf <strong>Broadcast Now</strong> klicken, das <strong>Other</strong>-Menü öffnen, <strong>OBS Broadcaster</strong> und <strong>Save and Close</strong> wählen. StreamRay postet deine <strong>Stream-URL ins Chat-Fenster</strong> — von dort kopieren. Das Stream-Key-Feld in SplitCam <strong>leer</strong> lassen; StreamRay authentifiziert nur über die URL.",
        "tips": [
            ("Die URL ist im Chat", "StreamRay zeigt die Stream-URL nicht in einem Einstellungsfeld — sie wird ins Broadcast-Chat-Fenster gepostet. Dort kopieren."),
            ("Stream-Key leer lassen", "StreamRay verwendet keinen separaten Key — nur die URL. Das Key-Feld in SplitCam nicht ausfüllen."),
            _T_ETH, _T_TEST,
        ],
        "faq": [
            ("Wo ist die StreamRay-Stream-URL?", "Nach Aktivierung des OBS Broadcasters postet StreamRay die Stream-URL ins Chat-Fenster — von dort kopieren."),
            ("Warum gibt es keinen StreamRay-Stream-Key?", "StreamRay authentifiziert nur über die URL — SplitCams Stream-Key-Feld leer lassen."),
            ("Welche Bitrate für StreamRay?", "StreamRay nennt keine offizielle Obergrenze — 3.500–6.000 Kbps bei 1080p anvisieren und den SplitCam-Speedtest laufen lassen, da der URL-only-Aufbau kein Bitrate-Feedback gibt."),
            ("Ist SplitCam kostenlos für StreamRay?", "Ja — kostenlos, ohne Wasserzeichen und ohne Zeitlimit, was zum URL-only-Workflow von StreamRay passt: einen Link einfügen und senden."),
        ],
    },
    {
        "slug": "xlovecam", "name": "XLoveCam",
        "title": "Auf XLoveCam streamen mit SplitCam — RTMP-Link & Key",
        "desc": "Auf XLoveCam senden mit kostenlosem SplitCam — RTMP-Link und Key, regionale Server, Szenen und Overlays. Ohne Wasserzeichen, kostenlose Anleitung.",
        "kw": "xlovecam, x love cam, auf xlovecam streamen, xlovecam rtmp link, xlovecam stream key",
        "h1html": 'So streamst du auf <span class="accent">XLoveCam</span> mit SplitCam',
        "h1short": "Auf XLoveCam streamen",
        "card": "RTMP-Link- und Key-Setup für XLoveCam.",
        "intro": "XLoveCam ist eine europäische, mehrsprachige Cam-Plattform. Die Konto-Einstellungen zeigen sowohl einen <strong style='color:var(--text)'>RTMP-Link</strong> als auch einen <strong style='color:var(--text)'>Stream-Key</strong> — kostenloses <strong style='color:var(--text)'>SplitCam</strong> nimmt beide und sendet mit vollen Szenen und Overlays.",
        "quick": "Auf XLoveCam mit SplitCam senden: SplitCam installieren, Szene bauen, auf XLoveCam <em>My Account → settings</em> öffnen, RTMP-Link und Stream-Key kopieren, beides in SplitCam einfügen, Show starten."
                 "<ol><li>SplitCam installieren.</li><li>Kamera + Szene hinzufügen.</li>"
                 "<li>XLoveCam-RTMP-Link + Key kopieren.</li><li>Beides in SplitCam einfügen.</li>"
                 "<li>Go Live drücken.</li></ol>",
        "key_how": "Auf XLoveCam <strong>My Account</strong> → <strong>settings</strong> öffnen. Die Einstellungen enthalten sowohl einen <strong>RTMP-Link</strong> als auch einen <strong>Stream-Key</strong> — beide in die Server-URL- und Key-Felder von SplitCam kopieren, dann auf XLoveCam <strong>Start your show</strong> nutzen.",
        "tips": [
            ("Link UND Key kopieren", "XLoveCam gibt dir einen RTMP-Link UND einen separaten Stream-Key — du brauchst beide in SplitCam, nicht nur einen."),
            ("Mehrsprachiges Publikum", "XLoveCam ist europäisch und mehrsprachig — ein klares Text-Overlay in deiner Sprache hilft den Zuschauern, dich zu finden."),
            ("Nächstgelegenen Server wählen", "XLoveCam betreibt regionale RTMP-Server — Europa, Nordamerika, Südamerika und Asien. Den nächstgelegenen wählen, das senkt Lag und verlorene Frames."),
            _T_ETH,
        ],
        "faq": [
            ("Wo sind die XLoveCam-RTMP-Daten?", "My Account → settings — dort werden sowohl RTMP-Link als auch Stream-Key angezeigt."),
            ("Unterstützt XLoveCam externe Encoder?", "Ja — es liefert einen RTMP-Link und einen Key, sodass SplitCam als Encoder funktioniert."),
            ("Welche Bitrate für XLoveCam?", "XLoveCam veröffentlicht kein festes Limit; 3.500–6.000 Kbps bei 1080p sind ideal. Die Wahl des nächstgelegenen regionalen Servers ist genauso wichtig wie die Zahl — sie reduziert verlorene Frames."),
            ("Ist SplitCam kostenlos für XLoveCam?", "Ja — kostenlos, ohne Wasserzeichen und ohne Zeitlimit, sodass das Erreichen des mehrsprachigen europäischen XLoveCam-Publikums keine Software-Kosten verursacht."),
        ],
    },
    {
        "slug": "soulcams", "name": "SoulCams",
        "title": "Auf SoulCams streamen mit SplitCam — OBS-Settings-Setup",
        "desc": "Auf SoulCams senden mit kostenlosem SplitCam — OBS-Settings-Setup, RTMP-Server und Key, Multi-Cam-Szenen und Overlays.",
        "kw": "soul cams, soulcams, auf soulcams streamen, soulcams obs, soulcams rtmp, soulcams broadcast",
        "h1html": 'So streamst du auf <span class="accent">SoulCams</span> mit SplitCam',
        "h1short": "Auf SoulCams streamen",
        "card": "OBS-Settings-Setup für SoulCams-Streams.",
        "intro": "SoulCams ist eine Cam-Plattform, deren OBS-Einstellungen <strong style='color:var(--text)'>RTMP-Server und Stream-Key gemeinsam</strong> in einem Fenster anzeigen. Beide in kostenloses <strong style='color:var(--text)'>SplitCam</strong> einfügen und mit Multi-Cam-Szenen und Overlays senden.",
        "quick": "Auf SoulCams mit SplitCam senden: SplitCam installieren, Szene bauen, auf SoulCams Go Online → Settings → OBS klicken, Server und Key kopieren, beides in SplitCam einfügen, Go Live."
                 "<ol><li>SplitCam installieren.</li><li>Kamera + Szene hinzufügen.</li>"
                 "<li>SoulCams Settings → OBS öffnen.</li><li>Server + Key in SplitCam einfügen.</li>"
                 "<li>Go Live drücken.</li></ol>",
        "key_how": "Auf SoulCams anmelden und <strong>Go Online</strong> klicken, dann <strong>Settings</strong> → <strong>OBS</strong> öffnen. Das OBS-Fenster zeigt <strong>RTMP-Server</strong> und <strong>Stream-Key</strong> zusammen — beide in SplitCam kopieren.",
        "tips": [
            ("Server und Key nebeneinander", "SoulCams zeigt RTMP-Server und Key im selben OBS-Fenster — beide in einem Rutsch holen."),
            ("Erst Go Online", "Die OBS-Einstellungen erscheinen erst, nachdem du auf SoulCams Go Online geklickt hast — vor der Suche nach den Encoder-Daten tun."),
            ("Unerwünschte Regionen blockieren", "SoulCams unterstützt Länderblockierung auf Modellseite — vor dem Klick auf Go Online wählen, welche Länder deinen Stream nicht sehen können."),
            _T_ETH, _T_TEST,
        ],
        "faq": [
            ("Wo sind die SoulCams-OBS-Einstellungen?", "Anmelden, Go Online klicken, dann Settings → OBS — RTMP-Server und Stream-Key werden zusammen angezeigt."),
            ("Unterstützt SoulCams externe Encoder?", "Ja — die OBS-Einstellungen liefern einen RTMP-Server und einen Key, also funktioniert SplitCam."),
            ("Welche Bitrate für SoulCams?", "SoulCams gibt keine offizielle Zahl an — 3.500–6.000 Kbps bei 1080p anvisieren und den Upload zuerst testen, da das OBS-Fenster keine Bitrate-Hinweise zeigt."),
            ("Ist SplitCam kostenlos für SoulCams?", "Ja — kostenlos, ohne Wasserzeichen und ohne Zeitlimit, sodass eine volle SoulCams-Show mit Multi-Cam-Szenen und Overlays auf der Encoder-Seite nichts kostet."),
        ],
    },
    {
        "slug": "imlive", "name": "ImLive",
        "title": "Auf ImLive streamen mit SplitCam — Virtual-Camera-Setup",
        "desc": "Im-Live-Stream-Setup mit kostenlosem SplitCam — ImLive nutzt die Webcam direkt (kein RTMP), SplitCam als virtuelle Kamera mit Szenen anbinden.",
        "kw": "im live stream, imlive splitcam, auf imlive streamen, imlive virtuelle kamera, imlive webcam, im live cam",
        "h1html": 'So nutzt du <span class="accent">ImLive</span> mit SplitCam',
        "h1short": "SplitCam auf ImLive",
        "card": "Virtual-Camera-Setup für ImLive — kein RTMP nötig.",
        "intro": "ImLive nutzt deine Webcam direkt im Browser — es gibt <strong style='color:var(--text)'>kein RTMP und keinen Stream-Key</strong>. Kostenloses <strong style='color:var(--text)'>SplitCam</strong> verbindet sich als <strong style='color:var(--text)'>virtuelle Kamera</strong>: Szene in SplitCam bauen, dann in ImLive SplitCam als Kamera wählen.",
        "quick": "SplitCam mit ImLive nutzen: SplitCam installieren, Szene mit Medien-Layern bauen, ImLive öffnen und einen Videochat starten, in ImLive-Einstellungen SplitCam als Webcam und Mikrofon wählen."
                 "<ol><li>SplitCam installieren.</li><li>Szene in SplitCam bauen.</li>"
                 "<li>Videochat auf ImLive starten.</li>"
                 "<li>SplitCam als ImLive-Kamera wählen.</li><li>Chat starten.</li></ol>",
        "steps": [
            ("SplitCam installieren",
             "SplitCam ist kostenlose Software für Windows und macOS. Installieren — kein Wasserzeichen, keine Anmeldung. Auf ImLive arbeitet es als <strong>virtuelle Kamera</strong>, nicht als RTMP-Encoder."),
            ("Szene in SplitCam bauen",
             "Öffne SplitCam und nutze <strong>Media Layers +</strong>, um deine Webcam plus Overlays, Text, Filter oder KI-Hintergrund hinzuzufügen. Diese komponierte Szene sieht ImLive als deine Kamera."),
            ("Videochat auf ImLive starten",
             "Auf die ImLive-Seite gehen und <strong>Start Video Chat</strong> klicken, dann <strong>Go To Settings</strong> öffnen, um zu den Kamera- und Mikrofonoptionen zu gelangen."),
            ("SplitCam als Kamera wählen",
             "In den ImLive-Einstellungen <strong>SplitCam</strong> als Webcam UND als Mikrofon wählen. ImLive zeigt jetzt deine volle SplitCam-Szene statt einer einfachen Webcam."),
            ("Free Live Chat starten",
             "Auf ImLive <strong>Free Live Chat</strong> klicken, um live zu gehen. Um dein Aussehen mitten in der Session zu ändern, bearbeite die Szene in SplitCam — ImLive aktualisiert sich sofort."),
        ],
        "tips": [
            ("Kein Stream-Key nötig", "ImLive hat kein RTMP — such keine Server-URL oder Key. SplitCam wird einfach als Kamera-Gerät ausgewählt."),
            ("SplitCam auch als Mikro setzen", "SplitCam auch als Mikrofon wählen, damit dein Audio-Mix und die Rauschunterdrückung mit übertragen werden."),
            ("Szene vor dem Live-Gehen bauen", "ImLive zeigt, was SplitCam ausgibt — die Layer vor dem Chat-Start anordnen."),
            _T_TEST,
        ],
        "faq": [
            ("Nutzt ImLive RTMP oder einen Stream-Key?", "Nein — ImLive nutzt deine Webcam direkt über den Browser. SplitCam verbindet sich als virtuelle Kamera, es gibt keinen Key zu kopieren."),
            ("Wie wähle ich SplitCam auf ImLive?", "Start Video Chat → Go To Settings → SplitCam als Webcam und Mikrofon wählen."),
            ("Kann ich Overlays auf ImLive nutzen?", "Ja — sie in die SplitCam-Szene einbauen; ImLive zeigt das komponierte Ergebnis."),
            ("Ist SplitCam kostenlos für ImLive?", "Ja — kostenlos, ohne Wasserzeichen und ohne Zeitlimit. Als virtuelle Kamera für ImLive bringt es weder Kosten noch Branding in deinen Videochat."),
        ],
    },
    {
        "slug": "vxlive", "name": "VXLive",
        "title": "Auf VXLive streamen mit SplitCam — offizielle Unterstützung",
        "desc": "Auf VXLive (VXModels / VISIT-X) mit kostenlosem SplitCam — offizielles VISIT-X-Preset, Server und Key, Szenen. Ohne Wasserzeichen.",
        "kw": "vxlive, visit-x, vxmodels splitcam, auf vxlive streamen, visit-x stream, vxlive rtmp",
        "h1html": 'So streamst du auf <span class="accent">VXLive</span> mit SplitCam',
        "h1short": "Auf VXLive streamen",
        "card": "VXLive unterstützt SplitCam offiziell (VISIT-X-Preset).",
        "intro": "VXLive (VXModels / VISIT-X) ist eine Cam-Plattform für den deutschen Markt — und eine der wenigen, die <strong style='color:var(--text)'>SplitCam offiziell unter eigenem Namen unterstützt</strong>. VXModels hat einen eigenen Hilfeartikel zur Anbindung von <strong style='color:var(--text)'>SplitCam</strong> an VXLive, und SplitCam liefert VISIT-X als fertiges Kanal-Preset.",
        "quick": "Auf VXLive mit SplitCam senden: SplitCam installieren, Szene bauen, in VXLive «Stream with third-party software» wählen, Server-URL und Key kopieren, in SplitCam das VISIT-X-Preset wählen und einfügen, in SplitCam Go Live, dann in VXLive GO ONLINE."
                 "<ol><li>SplitCam installieren.</li><li>Kamera + Szene hinzufügen.</li>"
                 "<li>VXLive-Server-URL + Key holen.</li>"
                 "<li>VISIT-X-Preset in SplitCam wählen, einfügen.</li>"
                 "<li>Go Live, dann GO ONLINE in VXLive.</li></ol>",
        "key_how": "In VXLive <strong>Stream with third-party software</strong> wählen und die Option für <strong>OBS, SplitCam oder XSplit</strong> nutzen. VXLive liefert eine <strong>Server-URL</strong> und einen <strong>Stream-Key</strong>. In SplitCam <strong>VISIT-X</strong> als Streaming-Plattform wählen, beide einfügen, in SplitCam <strong>Go Live</strong> drücken und dann in VXLive <strong>GO ONLINE</strong>.",
        "tips": [
            ("VISIT-X ist ein eingebautes Preset", "Du gibst keine rohe RTMP-URL ein — SplitCam hat VISIT-X in der Plattformliste, einfach auswählen und Server-URL plus Key einfügen."),
            ("Zwei-Schritt-Go-Live", "Auf VXLive zuerst in SplitCam Go Live, dann in VXLive GO ONLINE — beide, in dieser Reihenfolge."),
            ("Deutscher Markt", "VXLive-Publikum ist überwiegend deutschsprachig — ein deutsches Text-Overlay oder Titel hilft beim Zuschauerkontakt."),
            _T_ETH,
        ],
        "faq": [
            ("Unterstützt VXLive SplitCam offiziell?", "Ja — VXModels (VXLive) hat einen eigenen offiziellen Hilfeartikel zur Einrichtung von SplitCam und listet SplitCam neben OBS und XSplit als unterstützte Broadcasting-Software."),
            ("Wie verbinde ich SplitCam mit VXLive?", "In VXLive «Stream with third-party software» wählen, dann in SplitCam das VISIT-X-Preset wählen und die Server-URL und den Stream-Key einfügen, die VXLive liefert."),
            ("Drücke ich Go Live in SplitCam oder VXLive?", "Beides — zuerst in SplitCam Go Live, dann in VXLive GO ONLINE."),
            ("Warum empfiehlt VXModels SplitCam?", "Der offizielle VXModels-Hilfeartikel empfiehlt SplitCam gezielt, um Bildartefakte und Pixelung der Webcam zu beseitigen und die Verbindung zu stabilisieren — nicht nur als generischen Encoder."),
        ],
    },
    {
        "slug": "virtwish", "name": "VirtWish",
        "title": "Auf VirtWish streamen mit SplitCam — Stream-URL & Key",
        "desc": "Auf VirtWish senden mit kostenlosem SplitCam — Profile → Start Broadcast → OBS-Bereich, Stream-URL und Key, Szenen und Overlays.",
        "kw": "virtwish, auf virtwish streamen, virtwish broadcasting software, virtwish rtmp, virtwish stream key, virtwish obs",
        "h1html": 'So streamst du auf <span class="accent">VirtWish</span> mit SplitCam',
        "h1short": "Auf VirtWish streamen",
        "card": "Stream-URL- und Key-Setup für VirtWish.",
        "intro": "VirtWish ist eine interaktive Cam-Plattform. Ihre Broadcast-Einstellungen geben dir eine <strong style='color:var(--text)'>Stream-URL und einen separaten Stream-Key</strong> in einem OBS-Bereich — kostenloses <strong style='color:var(--text)'>SplitCam</strong> nimmt beide und führt die Show mit Szenen und Overlays.",
        "quick": "Auf VirtWish mit SplitCam senden: SplitCam installieren, Szene bauen, auf VirtWish <em>Profile → Start Broadcast</em> bis zum OBS-Bereich öffnen, Link und Key kopieren, beides in SplitCam einfügen, Go Live."
                 "<ol><li>SplitCam installieren.</li><li>Kamera + Szene hinzufügen.</li>"
                 "<li>VirtWish-URL + Key holen.</li><li>Beides in SplitCam einfügen.</li>"
                 "<li>Go Live drücken.</li></ol>",
        "key_how": "Auf VirtWish oben rechts auf das Icon klicken → <strong>Profile</strong> → <strong>Start Broadcast</strong>, dann erneut <strong>Start Broadcast</strong>, um zum OBS-Bereich zu kommen. <strong>Den Link in der ersten Zeile</strong> in das Stream-URL-Feld von SplitCam kopieren und den <strong>Stream Key</strong> separat in das Key-Feld.",
        "tips": [
            ("Link in der ersten Zeile", "Der OBS-Bereich von VirtWish setzt die Stream-URL in die erste Zeile — diese in SplitCams Stream URL kopieren, dann den Key separat."),
            ("Zwei Klicks auf Start Broadcast", "Du klickst Start Broadcast zweimal auf VirtWish, um zum OBS-Bereich zu gelangen — das ist erwartet, kein Glitch."),
            _T_ETH, _T_TEST,
        ],
        "faq": [
            ("Wo sind die VirtWish-RTMP-Daten?", "Icon oben rechts → Profile → Start Broadcast zweimal → der OBS-Bereich zeigt Link und Stream-Key."),
            ("Unterstützt VirtWish externe Encoder?", "Ja — der OBS-Bereich liefert eine Stream-URL und einen Key, sodass SplitCam funktioniert."),
            ("Welche Bitrate für VirtWish?", "VirtWish veröffentlicht keinen offiziellen Deckel; 3.500–6.000 Kbps bei 1080p sind ein sicherer Bereich. SplitCams Auflösung an die auf VirtWish gesetzte angleichen, um Rescaling zu vermeiden."),
            ("Ist SplitCam kostenlos für VirtWish?", "Ja — kostenlos, ohne Wasserzeichen und ohne Zeitlimit, sodass das URL-und-Key-Setup von VirtWish nur die paar Minuten Einrichtung kostet."),
        ],
    },
    {
        "slug": "xmodels", "name": "XModels",
        "title": "Auf XModels streamen mit SplitCam — kostenlose Anleitung",
        "desc": "Auf XModels senden mit kostenlosem SplitCam — Option für externen Encoder in den Model-Konto-Einstellungen, RTMP-Key, Szenen und Overlays.",
        "kw": "xmodels, auf xmodels streamen, xmodels broadcasting software, xmodels rtmp, xmodels external encoder",
        "h1html": 'So streamst du auf <span class="accent">XModels</span> mit SplitCam',
        "h1short": "Auf XModels streamen",
        "card": "External-Encoder-Setup für XModels-Streams.",
        "intro": "XModels ist eine Cam-Streaming-Plattform mit einer in-Produkt-Option für <strong style='color:var(--text)'>externe Encoder</strong> in den Model-Konto-Einstellungen. Kostenloses <strong style='color:var(--text)'>SplitCam</strong> sendet dorthin mit Multi-Cam-Szenen, Overlays und Filtern statt nur einer einfachen Kamera.",
        "quick": "Auf XModels mit SplitCam senden: SplitCam installieren, Szene bauen, im XModels-Model-Konto die External-Encoder-Option aktivieren, Server-URL und Stream-Key kopieren, in SplitCam einfügen, Go Live."
                 "<ol><li>SplitCam installieren.</li><li>Kamera + Szene hinzufügen.</li>"
                 "<li>External Encoder in den XModels-Konto-Einstellungen aktivieren.</li>"
                 "<li>Server-URL + Key in SplitCam einfügen.</li><li>Go Live drücken.</li></ol>",
        "key_how": "In den <strong>Model-Konto-Einstellungen</strong> von XModels die Option <strong>Senden über externen Encoder</strong> aktivieren. XModels liefert einen <strong>Stream-Key</strong> — diesen in SplitCam einfügen. Wenn die Option nicht an erwarteter Stelle ist, läuft der XModels-Support über In-Site-FAQ-Chat und <strong>info@xmodels.com</strong>; der Video-Guide oben zeigt es ebenfalls.",
        "tips": [
            ("In den Konto-Einstellungen", "XModels legt die External-Encoder-Option in die Model-Konto-Einstellungen, nicht auf einen separaten Broadcast-Bildschirm."),
            ("Support ist Chat + E-Mail", "XModels hat kein großes öffentliches Hilfecenter — der On-Site-FAQ-Chat und info@xmodels.com sind die offiziellen Support-Wege."),
            ("Overlays in SplitCam schichten", "Tipp-Ziele, dein Name und Social-Handles als Szenenebenen — die einfache XModels-Kamera kann das nicht."),
            _T_ETH,
        ],
        "faq": [
            ("Unterstützt XModels externe Encoder?", "Ja — die Model-Konto-Einstellungen enthalten eine Option «Senden über externen Encoder», die einen Stream-Key liefert, sodass SplitCam funktioniert."),
            ("Wo bekomme ich Hilfe zu XModels?", "XModels-Support läuft über den On-Site-FAQ-Chat und die E-Mail info@xmodels.com — es gibt kein großes öffentliches Hilfecenter."),
            ("Welche Bitrate für XModels?", "XModels nennt keine offizielle Zahl — 3.500–6.000 Kbps bei 1080p nutzen und den SplitCam-Speedtest laufen lassen, da der XModels-Support nur per Chat und E-Mail erreichbar ist."),
            ("Ist SplitCam kostenlos für XModels?", "Ja — kostenlos, ohne Wasserzeichen und ohne Zeitlimit, sodass das Senden ins europäische XModels-Netzwerk keine Software-Kosten verursacht."),
        ],
    },
    {
        "slug": "flirt4free", "name": "Flirt4Free",
        "title": "Auf Flirt4Free streamen mit SplitCam — External Broadcast Form",
        "desc": "Auf Flirt for Free Cam mit kostenlosem SplitCam — External Broadcast Form, RTMP-URL und Stream-Name, Szenen und Overlays.",
        "kw": "flirt for free cam, flirt 4 free cam, flirt4free, auf flirt4free streamen, flirt4free external broadcast, flirt4free rtmp",
        "h1html": 'So streamst du auf <span class="accent">Flirt4Free</span> mit SplitCam',
        "h1short": "Auf Flirt4Free streamen",
        "card": "External-Broadcast-Form-Setup für Flirt4Free.",
        "intro": "Flirt4Free ist eine der ältesten Cam-Plattformen, online seit den 1990ern. Sie unterstützt externes Broadcasting offiziell über ein <strong style='color:var(--text)'>External Broadcast Form</strong> — kostenloses <strong style='color:var(--text)'>SplitCam</strong> sendet den Stream, während das Formular Auflösung und Bitrate festlegt.",
        "quick": "Auf Flirt4Free mit SplitCam senden: SplitCam installieren, Szene bauen, Flirt4Frees External Broadcast Form öffnen, RTMP-URL und Stream-Namen kopieren und Auflösung/Bitrate setzen, in SplitCam einfügen, Go Live."
                 "<ol><li>SplitCam installieren.</li><li>Kamera + Szene hinzufügen.</li>"
                 "<li>Flirt4Frees External Broadcast Form öffnen.</li>"
                 "<li>RTMP URL + Stream Name in SplitCam einfügen.</li>"
                 "<li>Go Live drücken.</li></ol>",
        "key_how": "Im Flirt4Free-Modelbereich das <strong>External Broadcast Form</strong> öffnen. Anders als die meisten Cam-Seiten gibt Flirt4Free dir eine <strong>RTMP-URL</strong> und einen <strong>Stream-Namen</strong> (keinen «Key»), plus Auflösungs- und Bitrate-Felder, die du im Formular selbst ausfüllst. URL und Stream-Namen in die Server- und Key-Felder von SplitCam kopieren.",
        "tips": [
            ("Stream Name, nicht Key", "Flirt4Free nennt die Anmeldedaten Stream Name. In SplitCams Stream-Key-Feld einfügen — er erfüllt dieselbe Rolle."),
            ("Auflösung/Bitrate im Formular setzen", "Das External Broadcast Form von Flirt4Free hat eigene Auflösungs- und Bitrate-Felder — an deine SplitCam-Einstellungen angleichen, damit das Bild nicht skaliert wird."),
            ("Etablierte Plattform", "Flirt4Free läuft seit den 1990ern — die Model-Tools sind ausgereift und das External Broadcast Form ist ein dokumentierter Teil davon."),
            _T_ETH,
        ],
        "faq": [
            ("Unterstützt Flirt4Free externe Encoder?", "Ja — offiziell, über das External Broadcast Form, das eine RTMP-URL und einen Stream-Namen liefert. SplitCam funktioniert als Encoder."),
            ("Wo bekomme ich die Flirt4Free-RTMP-Daten?", "Aus dem External Broadcast Form im Modelbereich — es zeigt RTMP-URL, Stream-Namen und Auflösungs-/Bitrate-Felder."),
            ("Welche Bitrate für Flirt4Free?", "3.500–6.000 Kbps bei 1080p — denselben Wert im External Broadcast Form und in SplitCam setzen."),
            ("Ist SplitCam kostenlos für Flirt4Free?", "Ja — kostenlos, ohne Wasserzeichen und ohne Zeitlimit, was zu einer altgedienten Plattform wie Flirt4Free passt, bei der die Shows lang sein können."),
        ],
    },
    {
        "slug": "mfc-alerts", "name": "MFC Alerts",
        "title": "MFC Alerts zum Stream hinzufügen mit SplitCam",
        "desc": "Animierte Tipp-Alerts auf deinem MyFreeCams-Stream zeigen — mfcalerts.com-URL als Browser-Layer in kostenlosem SplitCam, immer über der Webcam.",
        "kw": "mfc alerts, myfreecams alerts, mfc alerts hinzufügen, mfcalerts splitcam, myfreecams tip alerts, myfreecams alerts overlay",
        "h1html": 'So fügst du <span class="accent">MFC Alerts</span> zu deinem Stream hinzu',
        "h1short": "MFC Alerts hinzufügen",
        "card": "Animierte Tipp-Alerts auf deinem MyFreeCams-Stream.",
        "intro": "MFC Alerts zeigt animierte Effekte auf deinem MyFreeCams-Stream, sobald ein Zuschauer tippt. Es läuft als <strong style='color:var(--text)'>Browser-Layer</strong> in kostenlosem <strong style='color:var(--text)'>SplitCam</strong> — einmal einrichten und Tipps lösen live On-Screen-Reaktionen aus.",
        "quick": "MFC Alerts mit SplitCam hinzufügen: SplitCam installieren, Webcam hinzufügen, Browser-Tab öffnen und mfcalerts.com laden, deine Alert-URL kopieren, als Browser-Layer über der Webcam hinzufügen, dann mit einem Test-Tipp prüfen."
                 "<ol><li>SplitCam installieren.</li><li>Webcam hinzufügen.</li>"
                 "<li>URL von mfcalerts.com holen.</li>"
                 "<li>Als Browser-Layer über der Webcam hinzufügen.</li>"
                 "<li>Test-Tipp senden.</li></ol>",
        "steps": [
            ("SplitCam installieren und Webcam hinzufügen",
             "Kostenloses SplitCam für Windows oder macOS installieren, dann die <strong>Webcam</strong> als Quelle hinzufügen. MFC Alerts wird als Layer über dieser Kamera sitzen."),
            ("Browser-Tab öffnen und auf mfcalerts.com gehen",
             "In SplitCam den <strong>Browser</strong>-Tab öffnen und zu <strong>www.mfcalerts.com</strong> navigieren. Anmelden, oder registrieren, falls noch kein mfcalerts.com-Konto."),
            ("Deine Alert-URL kopieren",
             "Auf mfcalerts.com <strong>Copy to clipboard</strong> nutzen, um deine persönliche Alert-URL zu kopieren — das ist die Seite, die die Tipp-Animationen rendert."),
            ("URL als Browser-Layer einfügen — über der Webcam",
             "Die URL in SplitCams Browser-Fenster einfügen und auf <strong>Add</strong> klicken. Dann die Quellenliste so umsortieren, dass <strong>MFC Alerts über deiner Webcam liegt</strong> (3-Punkte-Menü → Move Up). Liegt es darunter, sind die Effekte verdeckt."),
            ("Mit einem Test-Tipp prüfen",
             "<strong>Settings → Send test tip</strong> öffnen und prüfen, dass der Alert-Effekt über deiner Kamera erscheint. Dann wie gewohnt zu MyFreeCams senden — echte Tipps lösen jetzt die Animationen aus."),
        ],
        "tips": [
            ("MFC Alerts muss über der Webcam liegen", "Der häufigste Fehler: Liegt der MFC-Alerts-Layer unter der Webcam in der Quellenliste, sind die Effekte verdeckt. Nach oben verschieben."),
            ("Du brauchst ein mfcalerts.com-Konto", "Die Alert-URL ist persönlich — auf mfcalerts.com registrieren, falls noch kein Konto."),
            ("Vor dem Live-Gehen Test-Tipp senden", "Über Settings → Send test tip prüfen, dass das Overlay funktioniert — keine Überraschung mitten in der Show."),
            _T_ETH,
        ],
        "faq": [
            ("Was ist MFC Alerts?", "Ein Benachrichtigungssystem für MyFreeCams, das Video-Effekte auf deinem Stream zeigt, wenn Zuschauer tippen — als Browser-Overlay in SplitCam eingefügt."),
            ("Warum erscheinen meine MFC Alerts nicht?", "Fast immer die Layer-Reihenfolge — der MFC-Alerts-Browser-Layer muss in SplitCams Quellenliste über der Webcam liegen."),
            ("Brauche ich ein Konto für MFC Alerts?", "Ja — auf mfcalerts.com registrieren, um deine persönliche Alert-URL zu bekommen."),
            ("Ist SplitCam dafür kostenlos?", "Ja — SplitCam ist kostenlos, ohne Wasserzeichen und ohne Zeitlimit, und das MFC-Alerts-Browser-Overlay läuft darin ohne Zusatzkosten."),
        ],
    },
    {
        "slug": "lovense", "name": "Lovense",
        "title": "Lovense-Toy zum Stream hinzufügen mit SplitCam",
        "desc": "Lovense-Spielzeug interaktiv zum Cam-Stream hinzufügen mit kostenlosem SplitCam — Lovense SplitCam Toolset, On-Screen-Tipp-Alerts, Reaktionen.",
        "kw": "lovense zum stream hinzufügen, lovense cam stream, lovense splitcam, lovense splitcam toolset, lovense interaktives spielzeug streaming",
        "h1html": 'So fügst du ein <span class="accent">Lovense-Toy</span> zu deinem Stream hinzu',
        "h1short": "Lovense-Toy hinzufügen",
        "card": "Interaktives Lovense-Spielzeug an deinen Cam-Stream koppeln.",
        "intro": "Führe deinen Cam-Stream über kostenloses <strong style='color:var(--text)'>SplitCam</strong> und koppele ein <strong style='color:var(--text)'>Lovense</strong>-Spielzeug, das auf Tokens reagiert. Lovense dokumentiert ein eigenes <strong style='color:var(--text)'>Lovense SplitCam Toolset</strong>, und SplitCam liefert ein offizielles Lovense-Plugin — die Integration wird von beiden Seiten unterstützt.",
        "quick": "Lovense zum Stream hinzufügen: SplitCam und Lovense-Software installieren, Toy koppeln, Lovense mit deiner Cam-Plattform verknüpfen, den Lovense-Status als Browser-Layer in SplitCam einfügen, dann wie gewohnt senden."
                 "<ol><li>SplitCam installieren.</li><li>Lovense-Software installieren &amp; koppeln.</li>"
                 "<li>Lovense mit deiner Cam-Seite verknüpfen.</li>"
                 "<li>Lovense-Overlay in SplitCam einfügen.</li><li>Go Live drücken.</li></ol>",
        "steps": [
            ("SplitCam installieren",
             "SplitCam ist kostenlose Streaming-Software für Windows und macOS — der Encoder, der dein Video an deine Cam-Plattform sendet. Installieren; kein Wasserzeichen."),
            ("Lovense-Software installieren und koppeln",
             "Lovense Connect / Lovense Stream (die offizielle Desktop-App) installieren. Toy einschalten und per Bluetooth koppeln, sodass die App es als verbunden anzeigt."),
            ("Lovense mit deiner Cam-Plattform verknüpfen",
             "In der Lovense-App dein Cam-Konto verbinden, damit das Toy auf Tokens / Tipps der Zuschauer reagiert. Lovense unterstützt die meisten großen Cam-Plattformen."),
            ("Lovense-Overlay in SplitCam einfügen",
             "Lovense liefert eine Overlay-/Widget-URL. Diese als <strong>Browser</strong>-Layer in deine SplitCam-Szene einfügen, sodass Zuschauer Toy-Status und aktuelle Tipps am Bildschirm sehen."),
            ("Szene bauen und Go Live",
             "Kamera und andere Overlays hinzufügen, den RTMP-Key deiner Cam-Plattform in SplitCam einfügen und <strong>Go Live</strong> drücken. Das Toy reagiert in Echtzeit auf Tipps."),
        ],
        "tips": [
            ("Offizielles Lovense SplitCam Toolset nutzen", "Lovense veröffentlicht ein SplitCam-spezifisches Toolset mit eigener Installationsanleitung — es bringt das Toy-Aktivitäts- und Tipp-Alert-Overlay, das für SplitCam gemacht ist."),
            ("Lovense Cam Extension aktualisieren", "Das Toolset braucht eine aktuelle Lovense Cam Extension (30.1.4 oder neuer) — vor dem Live-Gehen updaten."),
            ("Toy geladen halten", "Eine leere Batterie mitten in der Show beendet den interaktiven Teil — vor dem Live-Gehen voll laden."),
            ("Token-Reaktion testen", "Einen kleinen Test-Tipp senden, um vor dem Öffnen des Raums zu prüfen, dass das Toy reagiert."),
            ("Versionsanforderungen beachten", "Das Lovense SplitCam Toolset benötigt SplitCam 10.4.5 oder neuer. Die Lovense Cam Extension deckt offiziell Chaturbate, Stripchat, BongaCams, MyFreeCams und CamSoda ab — für andere Seiten Lovenses Generic-URL-Integration nutzen."),
        ],
        "faq": [
            ("Unterstützt Lovense SplitCam offiziell?", "Ja — Lovense dokumentiert ein offizielles «Lovense SplitCam Toolset» mit eigener Installationsanleitung, und SplitCam liefert ein offizielles Lovense-Plugin. Die Integration wird beidseitig unterstützt."),
            ("Verbindet sich das Toy direkt mit SplitCam?", "Nein — das Toy koppelt sich mit der Lovense-App; SplitCam zeigt das Lovense-Overlay an und überträgt deine Kamera."),
            ("Welche Cam-Seiten unterstützen Lovense?", "Lovenses Cam Extension unterstützt offiziell Chaturbate, Stripchat, BongaCams, MyFreeCams und CamSoda, mit unterschiedlicher Unterstützung für andere — aktuelle Liste in der Lovense-App."),
            ("Kann ich aktuelle Tipps am Bildschirm zeigen?", "Ja — die Lovense-Widget-URL als Browser-Layer in SplitCam einfügen."),
        ],
    },
    {
        "slug": "multistream-cams", "name": "Mehrere Cam-Seiten",
        "title": "Auf mehrere Cam-Seiten gleichzeitig streamen mit SplitCam",
        "desc": "Auf MyFreeCams, Chaturbate, BongaCams, CAM4, Stripchat und mehr gleichzeitig mit kostenlosem SplitCam-Multistreaming. Ein Klick, ohne Wasserzeichen.",
        "kw": "auf mehrere cam-seiten senden, multistream cam sites, gleichzeitig auf chaturbate und bongacams streamen, cam multistreaming software",
        "h1html": 'So sendest du auf <span class="accent">mehrere Cam-Seiten</span> gleichzeitig',
        "h1short": "Multistream Cam-Seiten",
        "card": "Auf mehrere Cam-Seiten gleichzeitig senden.",
        "intro": "Kostenloses <strong style='color:var(--text)'>SplitCam</strong> kann eine Codierung an <strong style='color:var(--text)'>mehrere Cam-Seiten gleichzeitig</strong> senden — MyFreeCams, Chaturbate, BongaCams, CAM4, Stripchat und mehr. Kein Wasserzeichen, ein Klick.",
        "quick": "Auf mehrere Cam-Seiten gleichzeitig senden: SplitCam installieren, Szene bauen, von jeder Cam-Seite die RTMP-Server-URL und den Stream-Key holen, alle in SplitCams Multistream-Einstellungen einfügen, einmal Go Live klicken."
                 "<ol><li>SplitCam installieren.</li><li>Kamera + Szene hinzufügen.</li>"
                 "<li>RTMP-Key von jeder Cam-Seite holen.</li>"
                 "<li>Alle Keys in SplitCam-Multistream hinzufügen.</li>"
                 "<li>Einmal Go Live drücken.</li></ol>",
        "steps": [
            ("SplitCam installieren",
             "SplitCam ist kostenlose Streaming-Software für Windows und macOS mit eingebautem Multistreaming. Installieren — kein Wasserzeichen, keine Anmeldung."),
            ("Kamera und Szene einrichten",
             "SplitCam öffnen, Webcam hinzufügen und Szene mit Overlays und Filtern bauen. Eine Szene speist alle Ziele."),
            ("RTMP-Key von jeder Cam-Seite holen",
             "Auf jeder Cam-Plattform externes / RTMP-Streaming aktivieren und ihre <strong>Server-URL</strong> und <strong>Stream-Key</strong> kopieren. Für jede Seite wiederholen — siehe die einzelnen Plattform-Guides für genaue Pfade."),
            ("Jedes Ziel in SplitCam hinzufügen",
             "<strong>Stream Settings</strong> öffnen und jede Cam-Seite als Custom-RTMP-Ziel hinzufügen — Server-URL und Key einfügen. Alle gewünschten aktivieren."),
            ("Einmal Go Live klicken",
             "<strong>Go Live</strong> drücken. SplitCam sendet deinen Stream gleichzeitig peer-to-peer aus einer Codierung an jede ausgewählte Cam-Seite — ohne Zusatzgebühr."),
        ],
        "tips": [
            ("Auf deinen Upload achten", "Multistreaming verdielfältigt die Upload-Last. Jedes Ziel braucht seine eigene Bitrate — stell sicher, dass deine Verbindung die Summe trägt."),
            ("Regeln jeder Plattform prüfen", "Manche Cam-Seiten verbieten gleichzeitiges Senden anderswo — vor dem Multistreaming klären."),
            ("Kabel — Aussetzer kannst du dir hier nicht leisten", "Multistreaming vervielfacht die Upload-Last, sodass ein einzelner Wi-Fi-Einbruch alle Ziele gleichzeitig zum Stillstand bringen kann. Kabel ist hier nicht optional."),
            ("Health-Monitor beobachten", "SplitCam zeigt den Status pro Ziel — eine Seite abschalten, wenn dein Upload nicht mithält."),
        ],
        "faq": [
            ("Ist Multistreaming in SplitCam kostenlos?", "Ja — Multistreaming ist eingebaut und kostenlos, keine Gebühr pro Ziel, kein Wasserzeichen."),
            ("Auf wie viele Cam-Seiten kann ich gleichzeitig senden?", "So viele, wie dein Upload trägt — jedes Ziel verbraucht seine eigene Bitrate."),
            ("Nutzt das einen Cloud-Relay?", "Nein — SplitCam sendet Streams peer-to-peer direkt von deinem PC an jeden Plattform-Ingest-Server."),
            ("Verlangsamt Multistreaming meinen PC?", "Die Kodierung erfolgt einmal und wird wiederverwendet; Hardware-Encoding hält die CPU-Last gering. Upload-Bandbreite ist die echte Grenze."),
        ],
    },
    {
        "slug": "livejasmin", "name": "LiveJasmin",
        "title": "Auf LiveJasmin senden mit SplitCam — HD External Encoder",
        "desc": "Auf LiveJasmin senden mit kostenlosem SplitCam — Model Center External Encoder, HD-1080p-Setup, Multi-Cam-Szenen und Overlays. Ohne Wasserzeichen, ohne Registrierung.",
        "kw": "auf livejasmin senden, livejasmin obs, livejasmin external encoder, livejasmin rtmp, livejasmin stream key, livejasmin model setup",
        "h1html": 'So sendest du auf <span class="accent">LiveJasmin</span> mit SplitCam',
        "h1short": "Auf LiveJasmin senden",
        "card": "External-Encoder-Setup für das HD-only Model Center von LiveJasmin.",
        "intro": "LiveJasmin ist das Flaggschiff von Docler Holding — eines der größten Cam-Netzwerke der Welt und eine HD-only-Plattform. Der bevorzugte Broadcaster ist der hauseigene <strong>JasminCAM</strong>-Client, doch das Model Center bietet zusätzlich einen offiziellen Pfad über einen <strong>External Encoder</strong>, mit dem sich kostenloses <strong style='color:var(--text)'>SplitCam</strong> verbinden lässt — für Multi-Cam-Szenen, Beauty-Filter und Overlays auf demselben HD-Stream.",
        "quick": "Auf LiveJasmin mit SplitCam senden: SplitCam installieren, HD-Szene bauen, im Model Center <em>Settings → Broadcast → External Encoder</em> öffnen, Server-URL und Stream Key kopieren, in SplitCam einfügen, Go Live."
                 "<ol><li>SplitCam installieren.</li><li>Kamera + HD-Szene hinzufügen.</li>"
                 "<li>URL und Stream Key aus dem Model Center holen.</li><li>In SplitCam einfügen.</li>"
                 "<li>Go Live drücken.</li></ol>",
        "key_how": "Bei <strong>modelcenter.livejasmin.com</strong> anmelden, dann <strong>Settings → Broadcast → External Encoder</strong> öffnen. Das Model Center zeigt eine an dein Konto gebundene <strong>Server-URL</strong> und einen <strong>Stream Key</strong> — beides in die Custom-RTMP-Felder von SplitCam kopieren. <strong>Hinweis:</strong> Neue Accounts müssen zuerst freigeschaltet werden (48–72 Stunden), bevor die External-Encoder-Option erscheint, und die Plattform erzwingt HD-only-Output.",
        "tips": [
            ("HD oder Ranking weg", "LiveJasmin ist HD-only — alles unter 1280×720 läuft nur noch auf den schlecht zahlenden Listen, alles unter 1080p verliert den «Premium»-Status. Ziel: 1920×1080 bei 30 fps, 4.000–6.000 Kbps."),
            ("JasminCAM vs. External Encoder", "Doclers eigener JasminCAM-Client liefert die sauberste HD-Konformität, aber externe Encoder (OBS, SplitCam, vMix) sind nach Account-Freigabe offiziell unterstützt — und nur darüber bekommst du Multi-Cam-Szenen und Overlays, die JasminCAM nicht kann."),
            ("Free Chat ≠ Private Show", "Free Chat ist Vorschau-Modus — keine Nacktheit. Verdient wird in Private und Gold Show. Plane deine Szene so, dass sie angezogen UND im Show-Modus stark wirkt."),
            _T_ETH,
        ],
        "faq": [
            ("Unterstützt LiveJasmin externe Encoder wie SplitCam offiziell?", "Ja — das Model Center hat unter Settings → Broadcast die Option External Encoder. JasminCAM ist der empfohlene Client, aber OBS, SplitCam und andere RTMP-Encoder sind nach Freischaltung des Modell-Accounts ausdrücklich als unterstützt gelistet."),
            ("Wo bekomme ich meinen LiveJasmin-Stream-Key?", "Im Model Center: Settings → Broadcast → External Encoder. Dort erscheinen Server-URL und ein eindeutiger Stream Key — beides in die Custom-RTMP-Felder von SplitCam kopieren. Der Key gehört zu deinem Account; wie ein Passwort behandeln."),
            ("Welche Bitrate für LiveJasmin?", "LiveJasmin ist HD-only — anpeilen: 1920×1080 bei 30 fps, 4.000–6.000 Kbps und 2 Sekunden Keyframe-Intervall. Deutlich darunter kostet das Premium-Label und führt zu De-Ranking."),
            ("Ist SplitCam bei LiveJasmin kostenlos nutzbar?", "Ja — SplitCam ist kostenlos, ohne Wasserzeichen und ohne Zeitlimit. Der einzige Aufwand sind die HD-Anforderungen von LiveJasmin, und die deckt SplitCam mit 1080p-Szenenkomposition und Beauty-Filtern nativ ab."),
        ],
        "steps": [
            ("SplitCam herunterladen und installieren", "SplitCam ist kostenlose Live-Streaming-Software für Windows und macOS — ohne Registrierung, ohne Kreditkarte, ohne Wasserzeichen. Es ist der Encoder, der dein HD-Video an LiveJasmin schickt."),
            ("HD-Szene aufbauen", "SplitCam öffnen und die Webcam im 1080p-Modus hinzufügen. Overlays, Text, eine zweite Kamera oder das Smartphone, Beauty-Filter oder einen KI-Hintergrund einbauen — LiveJasmin verlangt HD-Qualität, und deine Szene muss sowohl im Free Chat als auch in Private Shows premium aussehen."),
            ("LiveJasmin-URL und Stream-Key holen", "Bei <strong>modelcenter.livejasmin.com</strong> anmelden (Account muss zuerst freigeschaltet sein — meist 48–72 Stunden nach Registrierung). <strong>Settings → Broadcast → External Encoder</strong> öffnen. Die Seite zeigt eine <strong>Server-URL</strong> und einen eindeutigen <strong>Stream Key</strong>. Beides kopieren."),
            ("SplitCam mit LiveJasmin verbinden", "In SplitCam <strong>Stream Settings</strong> öffnen, Server-URL und Stream Key in die Custom-RTMP-Felder einfügen. Bitrate auf 4.000–6.000 Kbps bei 1920×1080, 30 fps und 2 Sekunden Keyframe stellen. Vorher den eingebauten Speedtest laufen lassen — HD-Streams sind anspruchsvoll."),
            ("Go Live drücken", "In SplitCam auf <strong>Go Live</strong> klicken und im LiveJasmin Model Center online gehen. Innerhalb von ~10 Sekunden erreicht dein HD-Feed das Netzwerk von LiveJasmin. Spätere Sendungen sind ein Klick — SplitCam öffnen, Go Live, dann auf LiveJasmin online gehen."),
        ],
    },
    {
        "slug": "myfreecams", "name": "MyFreeCams",
        "title": "Auf MyFreeCams (MFC) senden mit SplitCam — Model Web Broadcaster umgehen",
        "desc": "Auf MyFreeCams senden mit kostenlosem SplitCam — Model Admin External Broadcaster, MFC-Token-Ökonomie, Multi-Cam-Szenen, Overlays. Ohne Wasserzeichen, ohne Registrierung.",
        "kw": "myfreecams senden, mfc external broadcaster, myfreecams obs, mfc rtmp, mfc stream key, model admin, mfc token",
        "h1html": 'So sendest du auf <span class="accent">MyFreeCams</span> mit SplitCam',
        "h1short": "Auf MyFreeCams senden",
        "card": "External-Broadcaster-Setup für das tokenbasierte Model Admin von MFC.",
        "intro": "MyFreeCams (MFC) ist eine der ältesten Cam-Plattformen — reine Token-Ökonomie, kein Modell-Freischalt-Marathon und eine treue Premium-Member-Basis. Der Standard-<em>Model Web Broadcaster</em> ist ein Single-Cam-Browser-Tool, doch Model Admin bietet zusätzlich eine <strong>External Broadcaster</strong>-Option, mit der sich kostenloses <strong style='color:var(--text)'>SplitCam</strong> verbindet — und so Multi-Cam-Szenen, Overlays und Filter auf demselben Token-Stream freischaltet.",
        "quick": "Auf MyFreeCams mit SplitCam senden: SplitCam installieren, Szene bauen, in <em>Model Admin → Broadcaster</em> vom Web Broadcaster auf External Broadcaster umstellen, Server-URL und Stream Key kopieren, in SplitCam einfügen, Go Live."
                 "<ol><li>SplitCam installieren.</li><li>Kamera + Szene hinzufügen.</li>"
                 "<li>URL und Stream Key aus Model Admin holen.</li><li>In SplitCam einfügen.</li>"
                 "<li>Go Live drücken.</li></ol>",
        "key_how": "Bei MyFreeCams anmelden, <strong>Model Admin → Broadcaster</strong> öffnen und vom <em>Web Broadcaster</em> auf <strong>External Broadcaster</strong> umstellen. Die Seite zeigt eine <strong>Server-URL</strong> (rtmp://publish.myfreecams.com…) und einen an dein Modell-Konto gebundenen <strong>Stream Key</strong> — beides in die Custom-RTMP-Felder von SplitCam kopieren. Der Key gehört zum Account; wie ein Passwort behandeln und bei Leak sofort zurücksetzen.",
        "tips": [
            ("MFC = Tokens, keine Abos", "MFC ist reine Tipping- bzw. Token-Ökonomie — Premium-Member können Private starten, aber das Hauptgeschäft sind Tips im Free Chat. Plane eine Szene, die angezogen und casual verdient, nicht nur in der Nacktshow."),
            ("Web Broadcaster vs. External — einmal entscheiden", "Der Standard-Web-Broadcaster ist Single-Cam, Single-Source. External Broadcaster schaltet Multi-Szene, Overlays und Beauty-Filter über SplitCam/OBS frei. Vor dem Go Live in Model Admin → Broadcaster umschalten."),
            ("MFC-Alerts-Integration", "Animierte Tip-Alerts kommen von mfcalerts.com — die Alert-URL als Browser-Layer in SplitCam über die Kamera legen. Vollständiges Overlay-Setup steht in unserem MFC-Alerts-Guide."),
            _T_ETH,
        ],
        "faq": [
            ("Unterstützt MyFreeCams externe Broadcaster wie SplitCam offiziell?", "Ja — Model Admin hat eine External-Broadcaster-Option, die eine Standard-RTMP-Server-URL und einen Stream Key liefert. OBS, SplitCam, vMix und andere RTMP-Encoder funktionieren alle."),
            ("Wo finde ich meinen MFC-Stream-Key?", "Model Admin → Broadcaster → auf External Broadcaster umschalten. Dort erscheinen Server-URL (rtmp://publish.myfreecams.com…) und Stream Key. Beides in die Custom-RTMP-Felder von SplitCam kopieren."),
            ("Welche Bitrate für MyFreeCams?", "MFC akzeptiert bis zu ~6.000 Kbps bei 2 Sekunden Keyframe-Intervall. Anpeilen: 1920×1080 bei 30 fps, 3.500–6.000 Kbps — dein Upload ist die echte Grenze."),
            ("Ist SplitCam bei MyFreeCams kostenlos nutzbar?", "Ja — SplitCam ist kostenlos, ohne Wasserzeichen und ohne Zeitlimit. Auch die External-Broadcaster-Option in Model Admin kostet nichts. Gesamtkosten für den Broadcaster: null."),
        ],
        "steps": [
            ("SplitCam herunterladen und installieren", "SplitCam ist kostenlose Live-Streaming-Software für Windows und macOS — ohne Registrierung, ohne Kreditkarte, ohne Wasserzeichen. Es ist der Encoder, der dein Video an MyFreeCams sendet."),
            ("Szene aufbauen", "SplitCam öffnen und die Webcam hinzufügen. Overlays, Text, eine zweite Kamera oder das Smartphone, Beauty-Filter oder einen KI-Hintergrund einbauen. Für animierte Tip-Alerts die mfcalerts.com-URL als Browser-Layer einbinden."),
            ("In Model Admin auf External Broadcaster umschalten", "Bei MyFreeCams anmelden. <strong>Model Admin → Broadcaster</strong> öffnen. Vom <em>Web Broadcaster</em> auf <strong>External Broadcaster</strong> umstellen. Die Seite zeigt eine <strong>Server-URL</strong> und einen eindeutigen <strong>Stream Key</strong>. Beides kopieren."),
            ("SplitCam mit MyFreeCams verbinden", "In SplitCam <strong>Stream Settings</strong> öffnen, MFC-Server-URL und Stream Key in die Custom-RTMP-Felder einfügen. Bitrate auf 3.500–6.000 Kbps bei 1920×1080, 30 fps und 2 Sekunden Keyframe-Intervall stellen."),
            ("Go Live drücken", "In SplitCam auf <strong>Go Live</strong> klicken. Innerhalb von ~10 Sekunden erreicht dein Stream MyFreeCams. Spätere Sendungen sind ein Klick."),
        ],
    },
    {
        "slug": "cherry-tv", "name": "Cherry.tv",
        "title": "Auf Cherry.tv senden mit SplitCam — Web3-freundlicher External Encoder",
        "desc": "Auf Cherry.tv senden mit kostenlosem SplitCam — Streamer Dashboard External Encoder, krypto-freundliche Cam-Plattform, Multi-Cam-Szenen. Ohne Wasserzeichen, ohne Registrierung.",
        "kw": "cherry tv senden, cherry.tv obs, cherry tv external encoder, cherry.tv rtmp, cherry.tv stream key, cherry tv streamer, web3 cam",
        "h1html": 'So sendest du auf <span class="accent">Cherry.tv</span> mit SplitCam',
        "h1short": "Auf Cherry.tv senden",
        "card": "External-Encoder-Setup für das Streamer Dashboard von Cherry.tv.",
        "intro": "Cherry.tv ist eine neuere, schnell wachsende Cam-Plattform mit Web3-Ausrichtung — krypto-freundliche Auszahlungen und niedrigere Einstiegshürden als alteingesessene Netzwerke wie LiveJasmin. Der Standard-Broadcaster läuft im Browser, doch das <strong>Streamer Dashboard</strong> bietet zusätzlich einen Standardpfad für einen <strong>External Encoder</strong>, an den sich kostenloses <strong style='color:var(--text)'>SplitCam</strong> verbinden lässt — für Streams mit Multi-Cam-Szenen, Overlays und Filtern.",
        "quick": "Auf Cherry.tv mit SplitCam senden: SplitCam installieren, Szene bauen, im Streamer Dashboard <em>Broadcast Settings → External Encoder</em> öffnen, Server-URL und Stream Key kopieren, in SplitCam einfügen, Go Live."
                 "<ol><li>SplitCam installieren.</li><li>Kamera + Szene hinzufügen.</li>"
                 "<li>URL und Stream Key aus dem Streamer Dashboard holen.</li><li>In SplitCam einfügen.</li>"
                 "<li>Go Live drücken.</li></ol>",
        "key_how": "Im Cherry.tv-Streamer-Account anmelden, das <strong>Streamer Dashboard</strong> öffnen und zu <strong>Broadcast Settings → External Encoder</strong> navigieren. Die Seite zeigt eine an dein Konto gebundene <strong>Server-URL</strong> und einen <strong>Stream Key</strong> — beides in die Custom-RTMP-Felder von SplitCam kopieren. Neue Streamer-Accounts müssen zuerst eine kurze Basis-Verifizierung abschließen, bevor die External-Encoder-Option vollständig aktiv ist.",
        "tips": [
            ("Niedrigere Einstiegshürde, wachsender Traffic", "Cherry.tv hat ein schnelleres Onboarding als alteingesessene Plattformen (keine 72-Stunden-Docler-Prüfung). Guter Early-Mover-Spot, um eine Follower-Basis aufzubauen."),
            ("Krypto-Auszahlungen verfügbar", "Cherry.tv unterstützt neben Standard-Fiat auch Krypto-Auszahlungen — praktisch in Regionen, wo klassische Cam-Netzwerk-Auszahlungen langsam oder eingeschränkt sind."),
            ("Browser-Broadcaster vs. External", "Der Browser-Broadcaster ist bequem, aber Single-Source. SplitCam über External Encoder schaltet Multi-Cam-Szenen, Overlays, Beauty-Filter und KI-Hintergrund frei."),
            _T_ETH,
        ],
        "faq": [
            ("Unterstützt Cherry.tv externe Encoder wie SplitCam offiziell?", "Ja — das Streamer Dashboard hat unter Broadcast Settings die Option External Encoder. Standard-RTMP-Server-URL und Stream Key; OBS, SplitCam, vMix lassen sich alle verbinden."),
            ("Wo bekomme ich meinen Cherry.tv-Stream-Key?", "Streamer Dashboard → Broadcast Settings → External Encoder. Server-URL und Stream Key erscheinen dort."),
            ("Welche Bitrate für Cherry.tv?", "Anpeilen: 1920×1080 bei 30 fps, 3.500–6.000 Kbps und 2 Sekunden Keyframe. Vorher den eingebauten Speedtest von SplitCam laufen lassen."),
            ("Ist SplitCam bei Cherry.tv kostenlos nutzbar?", "Ja — SplitCam ist kostenlos, ohne Wasserzeichen und ohne Zeitlimit."),
        ],
        "steps": [
            ("SplitCam herunterladen und installieren", "SplitCam ist kostenlose Live-Streaming-Software für Windows und macOS — ohne Registrierung, ohne Kreditkarte, ohne Wasserzeichen."),
            ("Szene aufbauen", "SplitCam öffnen und die Webcam hinzufügen. Overlays, Text, eine zweite Kamera, Beauty-Filter oder einen KI-Hintergrund einbauen. Das Cherry.tv-Publikum ist jünger und plattform-affin."),
            ("Cherry.tv-URL und Stream-Key holen", "Im Cherry.tv-Streamer-Account anmelden, das <strong>Streamer Dashboard</strong> öffnen und zu <strong>Broadcast Settings → External Encoder</strong> navigieren. Beides kopieren."),
            ("SplitCam mit Cherry.tv verbinden", "In SplitCam <strong>Stream Settings</strong> öffnen, Cherry.tv-Server-URL und Stream Key in die Custom-RTMP-Felder einfügen. Bitrate auf 3.500–6.000 Kbps bei 1920×1080, 30 fps stellen."),
            ("Go Live drücken", "In SplitCam auf <strong>Go Live</strong> klicken und anschließend im Streamer Dashboard auf Cherry.tv online gehen."),
        ],
    },
    {
        "slug": "amateurtv", "name": "AmateurTV",
        "title": "Auf AmateurTV senden mit SplitCam — spanischsprachiges Cam-Netzwerk",
        "desc": "Auf AmateurTV senden mit kostenlosem SplitCam — Model Panel External Encoder, spanischsprachiges Cam-Netzwerk für Spanien und LatAm, Multi-Cam-Szenen. Ohne Wasserzeichen, ohne Registrierung.",
        "kw": "auf amateurtv senden, amateur.tv obs, amateurtv external encoder, amateurtv rtmp, amateurtv stream key, modelos amateur tv",
        "h1html": 'So sendest du auf <span class="accent">AmateurTV</span> mit SplitCam',
        "h1short": "Auf AmateurTV senden",
        "card": "External-Encoder-Setup für das spanischsprachige Netzwerk AmateurTV.",
        "intro": "AmateurTV ist das führende spanischsprachige Cam-Netzwerk — starkes Publikum in Spanien, Mexiko, Argentinien und in ganz LatAm. Der Standard-Broadcaster im Model Panel läuft im Browser, doch die Plattform bietet zusätzlich einen offiziellen Pfad über einen <strong>External Encoder</strong>, an den sich kostenloses <strong style='color:var(--text)'>SplitCam</strong> verbindet — und so Multi-Cam-Szenen, Beauty-Filter und Overlays für ein hispanophones Publikum freischaltet, das von US-zentrierten Netzwerken kaum bedient wird.",
        "quick": "Auf AmateurTV mit SplitCam senden: SplitCam installieren, Szene bauen, im Model Panel <em>Broadcast Settings → External Encoder</em> öffnen, Server-URL und Stream Key kopieren, in SplitCam einfügen, Go Live."
                 "<ol><li>SplitCam installieren.</li><li>Kamera + Szene hinzufügen.</li>"
                 "<li>URL und Stream Key aus dem Model Panel holen.</li><li>In SplitCam einfügen.</li>"
                 "<li>Go Live drücken.</li></ol>",
        "key_how": "Im AmateurTV-Modell-Account anmelden, das <strong>Model Panel</strong> öffnen und zu <strong>Broadcast Settings → External Encoder</strong> navigieren. Die Seite zeigt eine an dein Konto gebundene <strong>Server-URL</strong> und einen <strong>Stream Key</strong> — beides in die Custom-RTMP-Felder von SplitCam kopieren. Neue Modell-Accounts müssen vor dem Go Live eine ID-Verifizierung abschließen.",
        "tips": [
            ("Hispanophones Publikum zuerst", "Der Traffic auf AmateurTV ist überwiegend spanischsprachig — tagsüber Spanien, abends US-Zeit LatAm. Stream-Titel, Szenentexte und Overlays auf Spanisch performen deutlich besser als reines Englisch."),
            ("LatAm-Zeitzone ist Prime Time", "Die Peak-Zeiten korrelieren mit dem LatAm-Abend (UTC-3 bis UTC-6). Wer flexibel ist, trifft mit spätem CET-Abend / frühem Asien-Morgen sowohl Spanien- als auch LatAm-Spitzen."),
            ("Solide Mid-Tier-Auszahlungen", "Nicht die höchsten RPMs der Branche, aber stabil — AmateurTV zahlt zuverlässig und die hispanophone Nische hat weniger Konkurrenz als die Top-US-Netzwerke."),
            _T_ETH,
        ],
        "faq": [
            ("Unterstützt AmateurTV externe Encoder wie SplitCam offiziell?", "Ja — das Model Panel hat unter Broadcast Settings die Option External Encoder. AmateurTV liefert eine Standard-RTMP-Server-URL und einen Stream Key; OBS, SplitCam, vMix und andere RTMP-Encoder lassen sich alle verbinden."),
            ("Wo bekomme ich meinen AmateurTV-Stream-Key?", "Model Panel → Broadcast Settings → External Encoder. Server-URL und Stream Key erscheinen dort. Beides in die Custom-RTMP-Felder von SplitCam kopieren. Der Key gehört zum Account."),
            ("Welche Bitrate für AmateurTV?", "Standard-Cam-Qualität — anpeilen: 1920×1080 bei 30 fps, 3.500–6.000 Kbps und 2 Sekunden Keyframe-Intervall. Vorher den eingebauten Speedtest von SplitCam laufen lassen."),
            ("Ist SplitCam bei AmateurTV kostenlos nutzbar?", "Ja — SplitCam ist kostenlos, ohne Wasserzeichen und ohne Zeitlimit. Die External-Encoder-Option bei AmateurTV ist kostenlos aktivierbar."),
        ],
        "steps": [
            ("SplitCam herunterladen und installieren", "SplitCam ist kostenlose Live-Streaming-Software für Windows und macOS — ohne Registrierung, ohne Kreditkarte, ohne Wasserzeichen. Es ist der Encoder, der dein Video an AmateurTV schickt."),
            ("Szene aufbauen", "SplitCam öffnen und die Webcam hinzufügen. Overlays, Text, eine zweite Kamera oder das Smartphone, Beauty-Filter oder einen KI-Hintergrund einbauen. Für das hispanophone Publikum von AmateurTV Overlays auf Spanisch verwenden."),
            ("AmateurTV-URL und Stream-Key holen", "Im AmateurTV-Modell-Account anmelden, das <strong>Model Panel</strong> öffnen und zu <strong>Broadcast Settings → External Encoder</strong> navigieren. Die Seite zeigt eine <strong>Server-URL</strong> und einen eindeutigen <strong>Stream Key</strong>. Beides kopieren."),
            ("SplitCam mit AmateurTV verbinden", "In SplitCam <strong>Stream Settings</strong> öffnen, die AmateurTV-Server-URL und den Stream Key in die Custom-RTMP-Felder einfügen. Bitrate auf 3.500–6.000 Kbps bei 1920×1080, 30 fps und 2 Sekunden Keyframe stellen. Vorher den eingebauten Speedtest laufen lassen."),
            ("Go Live drücken", "In SplitCam auf <strong>Go Live</strong> klicken, dann im Model Panel auf AmateurTV online gehen. Innerhalb von ~10 Sekunden erreicht dein Stream das Netzwerk. Spätere Sendungen sind ein Klick — SplitCam öffnen, Go Live."),
        ],
    },
    {
        "slug": "camster", "name": "Camster",
        "title": "Auf Camster senden mit SplitCam — Model Hub External Encoder",
        "desc": "Auf Camster senden mit kostenlosem SplitCam — Model Hub External Encoder, etablierte Mid-Tier-Cam-Plattform, Multi-Cam-Szenen und Overlays. Ohne Wasserzeichen, ohne Registrierung.",
        "kw": "auf camster senden, camster.com obs, camster external encoder, camster rtmp, camster stream key, camster model hub",
        "h1html": 'So sendest du auf <span class="accent">Camster</span> mit SplitCam',
        "h1short": "Auf Camster senden",
        "card": "External-Encoder-Setup für Camsters Model Hub.",
        "intro": "Camster ist eine etablierte Mid-Tier-Cam-Plattform — kleiner als Chaturbate oder LiveJasmin, aber mit treuer Nutzerbasis und fairen Auszahlungen. Der Standard-Broadcaster im Model Hub läuft im Browser, doch die Plattform bietet zusätzlich einen offiziellen Pfad über einen <strong>External Encoder</strong>, an den sich kostenloses <strong style='color:var(--text)'>SplitCam</strong> verbindet — für Multi-Cam-Szenen, Overlays und Filter, die der eingebaute Broadcaster nicht liefern kann.",
        "quick": "Auf Camster mit SplitCam senden: SplitCam installieren, Szene bauen, im Model Hub <em>Broadcast Settings → External Encoder</em> öffnen, Server-URL und Stream Key kopieren, in SplitCam einfügen, Go Live."
                 "<ol><li>SplitCam installieren.</li><li>Kamera + Szene hinzufügen.</li>"
                 "<li>URL und Stream Key aus dem Model Hub holen.</li><li>In SplitCam einfügen.</li>"
                 "<li>Go Live drücken.</li></ol>",
        "key_how": "Im Camster-Modell-Account anmelden, den <strong>Model Hub</strong> öffnen und zu <strong>Broadcast Settings → External Encoder</strong> navigieren. Die Seite zeigt eine an dein Konto gebundene <strong>Server-URL</strong> und einen <strong>Stream Key</strong> — beides in die Custom-RTMP-Felder von SplitCam kopieren. Der Key gehört zum Account; wie ein Passwort behandeln.",
        "tips": [
            ("Mid-Tier heißt weniger Konkurrenz", "Camster hat stabilen Traffic, aber weniger Broadcaster als die Top-Netzwerke — mit einer polierten Szene und konstantem Sendeplan kommt man hier leichter auf die Startseite."),
            ("Browser-Broadcaster vs. External", "Der Standard-Browser-Broadcaster ist Single-Source. SplitCam über External Encoder schaltet Multi-Cam-Szenen, Overlays, Beauty-Filter und KI-Hintergrund frei."),
            ("Stabile Auszahlungen, faire Splits", "Camsters Revenue-Split ist für die Mid-Tier fair — nicht die höchsten in der Branche, aber zuverlässige monatliche Auszahlungen und kaum Modellbeschwerden über Zahlungsverzögerungen."),
            _T_ETH,
        ],
        "faq": [
            ("Unterstützt Camster externe Encoder wie SplitCam offiziell?", "Ja — der Model Hub hat unter Broadcast Settings die Option External Encoder. Standard-RTMP-Server-URL und Stream Key; OBS, SplitCam und andere RTMP-Encoder lassen sich alle verbinden."),
            ("Wo bekomme ich meinen Camster-Stream-Key?", "Model Hub → Broadcast Settings → External Encoder. Server-URL und Stream Key erscheinen dort. Beides in die Custom-RTMP-Felder von SplitCam kopieren."),
            ("Welche Bitrate für Camster?", "Standard-Cam-Qualität — anpeilen: 1920×1080 bei 30 fps, 3.500–6.000 Kbps und 2 Sekunden Keyframe-Intervall. Vorher den eingebauten Speedtest von SplitCam laufen lassen."),
            ("Ist SplitCam bei Camster kostenlos nutzbar?", "Ja — SplitCam ist kostenlos, ohne Wasserzeichen und ohne Zeitlimit. Die External-Encoder-Option bei Camster ist kostenlos."),
        ],
        "steps": [
            ("SplitCam herunterladen und installieren", "SplitCam ist kostenlose Live-Streaming-Software für Windows und macOS — ohne Registrierung, ohne Kreditkarte, ohne Wasserzeichen."),
            ("Szene aufbauen", "SplitCam öffnen und die Webcam hinzufügen. Overlays, Text, eine zweite Kamera oder das Smartphone, Beauty-Filter oder einen KI-Hintergrund einbauen — alles live anwendbar."),
            ("Camster-URL und Stream-Key holen", "Im Camster-Modell-Account anmelden, den <strong>Model Hub</strong> öffnen und zu <strong>Broadcast Settings → External Encoder</strong> navigieren. Die Seite zeigt eine <strong>Server-URL</strong> und einen eindeutigen <strong>Stream Key</strong>. Beides kopieren."),
            ("SplitCam mit Camster verbinden", "In SplitCam <strong>Stream Settings</strong> öffnen, die Camster-Server-URL und den Stream Key in die Custom-RTMP-Felder einfügen. Bitrate auf 3.500–6.000 Kbps bei 1920×1080, 30 fps und 2 Sekunden Keyframe stellen. Vorher den eingebauten Speedtest laufen lassen."),
            ("Go Live drücken", "In SplitCam auf <strong>Go Live</strong> klicken, dann im Model Hub auf Camster online gehen. Innerhalb von ~10 Sekunden erreicht dein Stream Camster."),
        ],
    },
    {
        "slug": "camversity", "name": "Camversity",
        "title": "Auf Camversity senden mit SplitCam — Performer Dashboard External Encoder",
        "desc": "Auf Camversity senden mit kostenlosem SplitCam — Performer Dashboard External Encoder, wachsende unabhängige Cam-Plattform, Multi-Cam-Szenen. Ohne Wasserzeichen, ohne Registrierung.",
        "kw": "auf camversity senden, camversity obs, camversity external encoder, camversity rtmp, camversity stream key, camversity performer",
        "h1html": 'So sendest du auf <span class="accent">Camversity</span> mit SplitCam',
        "h1short": "Auf Camversity senden",
        "card": "External-Encoder-Setup für Camversitys Performer Dashboard.",
        "intro": "Camversity ist eine wachsende unabhängige Cam-Plattform mit Fokus auf performer-freundliche Tools und niedrigere Provisionen als die Legacy-Netzwerke. Der Standard-Broadcaster im Performer Dashboard läuft im Browser, doch die Plattform bietet zusätzlich einen offiziellen Pfad über einen <strong>External Encoder</strong>, an den sich kostenloses <strong style='color:var(--text)'>SplitCam</strong> verbindet — für Multi-Cam-Szenen, Overlays und Filter.",
        "quick": "Auf Camversity mit SplitCam senden: SplitCam installieren, Szene bauen, im Performer Dashboard <em>Stream Settings → External Encoder</em> öffnen, Server-URL und Stream Key kopieren, in SplitCam einfügen, Go Live."
                 "<ol><li>SplitCam installieren.</li><li>Kamera + Szene hinzufügen.</li>"
                 "<li>URL und Stream Key aus dem Performer Dashboard holen.</li><li>In SplitCam einfügen.</li>"
                 "<li>Go Live drücken.</li></ol>",
        "key_how": "Im Camversity-Performer-Account anmelden, das <strong>Performer Dashboard</strong> öffnen und zu <strong>Stream Settings → External Encoder</strong> navigieren. Die Seite zeigt eine an dein Konto gebundene <strong>Server-URL</strong> und einen <strong>Stream Key</strong> — beides in die Custom-RTMP-Felder von SplitCam kopieren. Neue Accounts müssen vor dem Go Live eine Standard-ID-Verifizierung abschließen.",
        "tips": [
            ("Performer-freundliche Splits", "Camversitys Revenue-Split ist für Performer günstiger als bei den Legacy-Netzwerken — ein Vergleich mit deinem aktuellen Hauptplattform lohnt sich, wenn du noch am Anfang deiner Cam-Karriere stehst."),
            ("Leichteres Onboarding als bei Docler", "Die Verifizierung bei Camversity ist schneller als der 48–72-Stunden-Approval-Prozess bei LiveJasmin und trotzdem seriös (keine zufälligen / unverifizierten Modelle). Guter Mittelweg."),
            ("Eine Szene bauen, nicht nur eine Webcam", "Der Standard-Broadcaster im Performer Dashboard ist Single-Source. SplitCam über External Encoder schaltet Multi-Cam, Overlays und Beauty-Filter frei."),
            _T_ETH,
        ],
        "faq": [
            ("Unterstützt Camversity externe Encoder wie SplitCam offiziell?", "Ja — das Performer Dashboard hat unter Stream Settings die Option External Encoder. Standard-RTMP-Server-URL und Stream Key; OBS, SplitCam, vMix lassen sich alle verbinden."),
            ("Wo bekomme ich meinen Camversity-Stream-Key?", "Performer Dashboard → Stream Settings → External Encoder. Server-URL und Stream Key erscheinen dort."),
            ("Welche Bitrate für Camversity?", "Anpeilen: 1920×1080 bei 30 fps, 3.500–6.000 Kbps und 2 Sekunden Keyframe-Intervall. Vorher den eingebauten Speedtest von SplitCam laufen lassen."),
            ("Ist SplitCam bei Camversity kostenlos nutzbar?", "Ja — SplitCam ist kostenlos, ohne Wasserzeichen und ohne Zeitlimit. Die External-Encoder-Option bei Camversity ist kostenlos."),
        ],
        "steps": [
            ("SplitCam herunterladen und installieren", "SplitCam ist kostenlose Live-Streaming-Software für Windows und macOS — ohne Registrierung, ohne Kreditkarte, ohne Wasserzeichen."),
            ("Szene aufbauen", "SplitCam öffnen und die Webcam hinzufügen. Overlays, Text, eine zweite Kamera oder das Smartphone, Beauty-Filter oder einen KI-Hintergrund einbauen."),
            ("Camversity-URL und Stream-Key holen", "Im Camversity-Performer-Account anmelden, das <strong>Performer Dashboard</strong> öffnen und zu <strong>Stream Settings → External Encoder</strong> navigieren. Die Seite zeigt eine <strong>Server-URL</strong> und einen eindeutigen <strong>Stream Key</strong>. Beides kopieren."),
            ("SplitCam mit Camversity verbinden", "In SplitCam <strong>Stream Settings</strong> öffnen, die Camversity-Server-URL und den Stream Key in die Custom-RTMP-Felder einfügen. Bitrate auf 3.500–6.000 Kbps bei 1920×1080, 30 fps und 2 Sekunden Keyframe stellen."),
            ("Go Live drücken", "In SplitCam auf <strong>Go Live</strong> klicken, dann im Performer Dashboard online gehen. Innerhalb von ~10 Sekunden erreicht dein Stream Camversity."),
        ],
    },
]
