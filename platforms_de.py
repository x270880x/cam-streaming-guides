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
        "kw": "auf chaturbate streamen, chaturbate, chaturbate broadcast, chaturbate obs, chaturbate external encoder, chaturbate rtmp, chaturbate broadcast token",
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
        "kw": "auf cam4 streamen, cam4, cam4 broadcast, cam4 obs, cam4 external encoder, cam4 rtmp, cam4 stream key",
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
        "kw": "auf bongacams streamen, bongacams, bongacams broadcast, bongacams obs, bongacams external encoder, bongacams rtmp, bongacams stream key",
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
        "kw": "auf stripchat streamen, stripchat, stripchat broadcast, stripchat obs, stripchat external software, stripchat rtmp, stripchat stream key",
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
        "title": "Auf OnlyFans live gehen mit SplitCam — OBS Key",
        "desc": "Auf OnlyFans live gehen mit kostenlosem SplitCam — Autorisierungs-Login oder OBS Key, Multi-Cam-Szenen, Overlays. Ohne Wasserzeichen.",
        "kw": "auf onlyfans live gehen, onlyfans, onlyfans live, onlyfans broadcast, onlyfans obs key, onlyfans stream key, onlyfans streaming software",
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
        "title": "Auf CamPlace streamen mit SplitCam — External Encoder",
        "desc": "Auf CamPlace senden mit kostenlosem SplitCam — externer Encoder, RTMP-Key, Szenen und Overlays. Schritt-für-Schritt-Anleitung, ohne Wasserzeichen.",
        "kw": "auf camplace streamen, camplace, camplace broadcast, camplace obs, camplace external encoder, camplace rtmp, camplace stream key",
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
        "kw": "auf camsoda streamen, camsoda, camsoda broadcast, camsoda obs broadcaster, camsoda external encoder, camsoda rtmp, camsoda stream key",
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
        "kw": "auf streamate streamen, streamate, streamate broadcast, streamate sm connect, streamate obs, streamate external encoder, streamate rtmp",
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
        "kw": "auf streamray streamen, streamray, streamray broadcast, streamray obs broadcaster, streamray external encoder, streamray rtmp, streamray cam",
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
        "kw": "auf xlovecam streamen, xlovecam, xlovecam broadcast, xlovecam obs, xlovecam external encoder, xlovecam rtmp, xlovecam stream key",
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
        "kw": "auf soulcams streamen, soulcams, soulcams broadcast, soulcams obs, soulcams external encoder, soulcams rtmp, soulcams stream key",
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
        "kw": "auf imlive streamen, imlive, imlive virtual camera, imlive virtuelle kamera, imlive webcam, imlive splitcam, im live cam",
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
        "kw": "auf vxlive streamen, vxlive, vxlive broadcast, vxlive obs, vxlive external encoder, vxlive rtmp, visit-x, vxmodels",
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
        "kw": "auf virtwish streamen, virtwish, virtwish broadcast, virtwish obs, virtwish external encoder, virtwish rtmp, virtwish stream key",
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
        "title": "Auf XModels streamen mit SplitCam — External Encoder",
        "desc": "Auf XModels senden mit kostenlosem SplitCam — Option für externen Encoder in den Model-Konto-Einstellungen, RTMP-Key, Szenen und Overlays.",
        "kw": "auf xmodels streamen, xmodels, xmodels broadcast, xmodels obs, xmodels external encoder, xmodels rtmp, xmodels stream key",
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
        "title": "Auf Flirt4Free streamen mit SplitCam — External Encoder",
        "desc": "Auf Flirt for Free Cam mit kostenlosem SplitCam — External Broadcast Form, RTMP-URL und Stream-Name, Szenen und Overlays.",
        "kw": "auf flirt4free streamen, flirt4free, flirt4free broadcast, flirt4free obs, flirt4free external broadcast, flirt4free rtmp, flirt for free cam",
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
        "kw": "mfc alerts hinzufügen, mfc alerts, myfreecams, myfreecams alerts, mfcalerts splitcam, myfreecams tip alerts, myfreecams alerts overlay",
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
        "desc": "Lovense-Toy zum SplitCam-Stream hinzufügen — Lovense Remote App + Cam Extension (integrierte SplitCam-Unterstützung), Tipp-Alerts im Bild.",
        "kw": "lovense zum stream hinzufügen, lovense, lovense cam stream, lovense splitcam, lovense splitcam toolset, lovense toy stream, lovense interaktives spielzeug",
        "h1html": 'So fügst du ein <span class="accent">Lovense-Toy</span> zu deinem Stream hinzu',
        "h1short": "Lovense-Toy hinzufügen",
        "card": "Interaktives Lovense-Spielzeug an deinen Cam-Stream koppeln.",
        "intro": "Sende deinen Cam-Stream über kostenloses <strong style='color:var(--text)'>SplitCam</strong> "
                 "und koppele ein interaktives <strong style='color:var(--text)'>Lovense</strong>-Spielzeug, "
                 "das auf Tipps reagiert. Du installierst drei Dinge: <strong>SplitCam</strong> (den Encoder), "
                 "die <strong>Lovense Remote</strong> App (die Bluetooth-Brücke zum Toy) und die "
                 "<strong>Lovense Cam Extension</strong> für Chrome/Edge (sie liest Trinkgelder und liefert "
                 "das Overlay im Bild). Die SplitCam-Unterstützung ist in die Cam Extension (Version 30.1.4 "
                 "oder neuer) integriert — SplitCam steht direkt in der Video Feedback-Liste der Erweiterung, "
                 "du brauchst also kein separates Plugin.",
        "quick": "Lovense-Toy zum Stream hinzufügen: SplitCam, die Lovense Remote App und die Lovense Cam "
                 "Extension installieren, das Toy koppeln, die Extension mit deiner Cam-Seite verknüpfen, das "
                 "Lovense-Overlay als Browser-Layer in SplitCam einfügen, dann wie gewohnt senden."
                 "<ol><li>SplitCam installieren.</li>"
                 "<li>Lovense Remote installieren &amp; Toy koppeln.</li>"
                 "<li>Lovense Cam Extension installieren (Chrome/Edge).</li>"
                 "<li>Extension mit Cam-Seite verknüpfen + Overlay in SplitCam einfügen.</li>"
                 "<li>Go Live drücken.</li></ol>",
        "key_how": "Das Toy spricht nie direkt mit SplitCam. Die Kette lautet: ein Zuschauer gibt auf deiner "
                   "Cam-Seite ein Trinkgeld &rarr; die <strong>Lovense Cam Extension</strong> in deinem Browser "
                   "erkennt es &rarr; sie sendet einen Befehl an die <strong>Lovense Remote</strong> App auf "
                   "localhost &rarr; Remote steuert das Toy über Bluetooth. SplitCams einzige Aufgabe ist es, "
                   "das <strong>Lovense-Overlay</strong> (Toy-Status + aktuelle Tipps) als Browser-Layer "
                   "anzuzeigen und deine Kamera zu übertragen. Es gibt keine eigene «Lovense Browser»-App — es "
                   "ist eine Browser-<em>Erweiterung</em> für Chrome oder Edge.",
        "steps": [
            ("SplitCam installieren",
             "SplitCam ist kostenlose Live-Streaming-Software für Windows und macOS — der Encoder, der dein "
             "Video an deine Cam-Plattform sendet. Installieren; kein Wasserzeichen, keine Anmeldung."),
            ("Lovense Remote installieren und Toy koppeln",
             "Installiere die <strong>Lovense Remote</strong> App — als Desktop-Version (Windows / Mac) oder "
             "als mobile App auf deinem Handy. Das ist die Brücke, die über Bluetooth mit dem Toy spricht. "
             "Schalte das Toy ein und koppele es, bis die App es als verbunden anzeigt."),
            ("Lovense Cam Extension installieren",
             "Füge die <strong>Lovense Cam Extension</strong> zu Chrome oder Edge hinzu (Version 30.1.4 oder "
             "neuer) und melde dich mit deinem Lovense-Konto an. Es gibt keinen eigenständigen «Lovense "
             "Browser» — diese Erweiterung liest die Trinkgelder und treibt das Overlay an. <strong>Die "
             "SplitCam-Unterstützung ist integriert</strong>: SplitCam steht in der Video Feedback-Liste "
             "der Erweiterung, du brauchst also kein separates SplitCam-Plugin."),
            ("Extension mit deiner Cam-Seite verknüpfen und Overlay in SplitCam einfügen",
             "Klicke in der Cam Extension auf <strong>+</strong>, um deine Cam-Seite hinzuzufügen (Chaturbate, "
             "Stripchat usw.), lege deine Tipp-Stufen fest, öffne dann den Tab <strong>Video Feedback</strong> "
             "und wähle <strong>SplitCam</strong>. Kopiere die angezeigte Overlay-URL und füge sie als "
             "<strong>Browser</strong>-Layer in deine SplitCam-Szene ein, sodass Zuschauer Toy-Status und "
             "aktuelle Tipps sehen."),
            ("Szene bauen und Go Live",
             "Kamera und weitere Overlays hinzufügen, den RTMP-Key deiner Cam-Plattform in SplitCam einfügen "
             "und <strong>Go Live</strong> klicken. Das Toy reagiert nun in Echtzeit auf Tipps."),
        ],
        "tips": [
            ("Drei Installationen, in dieser Reihenfolge", "SplitCam (Encoder) + Lovense Remote "
             "(Bluetooth-Brücke) + Lovense Cam Extension (Tipp-Leser / Overlay). Fehlt eine davon, reagiert "
             "das Toy im Stream nicht."),
            ("Eine Erweiterung, kein Browser", "Es gibt keinen separaten «Lovense Browser» zum Herunterladen — "
             "die Lovense Cam Extension installiert sich in Chrome oder Edge. Halte sie aktuell (30.1.4 oder "
             "neuer), sonst lädt das SplitCam-Overlay eventuell nicht."),
            ("Toy geladen halten", "Eine leere Batterie mitten in der Show beendet den interaktiven Teil — "
             "vor dem Live-Gehen voll laden."),
            ("Tipp-Reaktion testen", "Einen kleinen Test-Tipp senden, um vor dem Öffnen des Raums zu prüfen, "
             "dass das Toy reagiert."),
            ("Welche Cam-Seiten abgedeckt sind", "Die Cam Extension deckt offiziell Chaturbate, Stripchat, "
             "BongaCams, MyFreeCams und CamSoda ab — für jede andere Seite Lovenses Generic-URL-Integration "
             "nutzen. SplitCam funktioniert als Overlay-Layer mit allen."),
        ],
        "faq": [
            ("Was muss ich für Lovense auf SplitCam installieren?", "Drei Dinge: <strong>SplitCam</strong> "
             "(den Encoder), die <strong>Lovense Remote</strong> App (verbindet das Toy über Bluetooth) und "
             "die <strong>Lovense Cam Extension</strong> für Chrome/Edge (liest Trinkgelder und liefert das "
             "Overlay). Kein separates SplitCam-Plugin — die SplitCam-Unterstützung ist in die Cam Extension integriert."),
            ("Funktioniert die Cam Extension 30.1.4+ direkt mit SplitCam?", "Ja — die SplitCam-Unterstützung "
             "ist integriert. Öffne den Tab <strong>Video Feedback</strong> der Erweiterung, wähle "
             "<strong>SplitCam</strong>, kopiere die Overlay-URL und füge sie als Browser-Layer in SplitCam "
             "ein. Kein zusätzliches Plugin, nur diese einmalige Verknüpfung."),
            ("Muss ich einen «Lovense Browser» herunterladen?", "Nein. Es gibt keinen eigenständigen "
             "Lovense-Browser — es ist die <strong>Lovense Cam Extension</strong>, die sich in Chrome oder "
             "Edge installiert. Das Koppeln des Toys übernimmt die separate App Lovense Remote (Desktop oder mobil)."),
            ("Verbindet sich das Toy direkt mit SplitCam?", "Nein — das Toy koppelt sich über Bluetooth mit "
             "der Lovense Remote App; die Cam Extension liest die Trinkgelder, und SplitCam zeigt nur das "
             "Overlay an und überträgt deine Kamera."),
            ("Welche Cam-Seiten unterstützen Lovense?", "Lovenses Cam Extension unterstützt offiziell "
             "Chaturbate, Stripchat, BongaCams, MyFreeCams und CamSoda, mit unterschiedlicher Unterstützung "
             "für andere — aktuelle Liste in der Lovense-App."),
            ("Kann ich aktuelle Tipps am Bildschirm zeigen?", "Ja — die Cam Extension liefert dir eine "
             "Overlay-URL; füge sie als Browser-Layer in SplitCam ein, und Zuschauer sehen Toy-Status und "
             "aktuelle Tipps."),
        ],
    },
    {
        "slug": "multistream-cams", "name": "Mehrere Cam-Seiten",
        "title": "Auf mehrere Cam-Seiten gleichzeitig streamen mit SplitCam",
        "desc": "Auf MyFreeCams, Chaturbate, BongaCams, CAM4, Stripchat und mehr gleichzeitig mit kostenlosem SplitCam-Multistreaming. Ein Klick, ohne Wasserzeichen.",
        "kw": "auf mehrere cam-seiten streamen, multistream cam sites, gleichzeitig auf mehrere cam-seiten senden, cam multistreaming software, multistream chaturbate bongacams",
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
        "desc": "Auf LiveJasmin senden mit kostenlosem SplitCam — Model Center External Encoder, HD-1080p, Multi-Cam-Szenen und Overlays. Ohne Wasserzeichen.",
        "kw": "auf livejasmin senden, livejasmin, livejasmin broadcast, livejasmin obs, livejasmin external encoder, livejasmin rtmp, livejasmin stream key",
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
        "title": "Auf MyFreeCams senden mit SplitCam — External Broadcaster",
        "desc": "Auf MyFreeCams senden mit kostenlosem SplitCam — Model Admin External Broadcaster, MFC-Token, Multi-Cam-Szenen und Overlays. Ohne Wasserzeichen.",
        "kw": "auf myfreecams senden, myfreecams, mfc broadcast, myfreecams obs, mfc external broadcaster, mfc rtmp, mfc stream key",
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
        "title": "Auf Cherry.tv senden mit SplitCam — External Encoder",
        "desc": "Auf Cherry.tv senden mit kostenlosem SplitCam — Streamer Dashboard External Encoder, Multi-Cam-Szenen und Overlays. Ohne Wasserzeichen.",
        "kw": "auf cherry.tv senden, cherry.tv, cherry.tv broadcast, cherry.tv obs, cherry.tv external encoder, cherry.tv rtmp, cherry.tv stream key",
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
        "title": "Auf AmateurTV senden mit SplitCam — External Encoder",
        "desc": "Auf AmateurTV senden mit kostenlosem SplitCam — Model Panel External Encoder, spanischsprachiges Cam-Netzwerk, Multi-Cam-Szenen. Ohne Wasserzeichen.",
        "kw": "auf amateurtv senden, amateurtv, amateurtv broadcast, amateurtv obs, amateurtv external encoder, amateurtv rtmp, amateurtv stream key",
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
        "title": "Auf Camster senden mit SplitCam — External Encoder",
        "desc": "Auf Camster senden mit kostenlosem SplitCam — Model Hub External Encoder, Multi-Cam-Szenen und Overlays. Ohne Wasserzeichen, kostenlose Anleitung.",
        "kw": "auf camster senden, camster, camster broadcast, camster obs, camster external encoder, camster rtmp, camster stream key",
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
        "title": "Auf Camversity senden mit SplitCam — External Encoder",
        "desc": "Auf Camversity senden mit kostenlosem SplitCam — Performer Dashboard External Encoder, Multi-Cam-Szenen und Overlays. Ohne Wasserzeichen.",
        "kw": "auf camversity senden, camversity, camversity broadcast, camversity obs, camversity external encoder, camversity rtmp, camversity stream key",
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
    {
        "slug": "skyprivate", "name": "SkyPrivate",
        "title": "SkyPrivate mit SplitCam nutzen — virtuelle Kamera für Skype",
        "desc": "SkyPrivate mit kostenlosem SplitCam als virtuelle Kamera nutzen — Pay-per-Minute-Skype-Cam-Calls, Multi-Cam-Szenen, Beauty-Filter. Ohne Wasserzeichen.",
        "kw": "skyprivate mit splitcam, skyprivate, skyprivate virtual camera, skyprivate virtuelle kamera, skyprivate splitcam, sky private cam, pay-per-minute cam",
        "h1html": 'So nutzt du <span class="accent">SkyPrivate</span> mit SplitCam',
        "h1short": "SplitCam bei SkyPrivate",
        "card": "Virtual-Camera-Setup für SkyPrivates Skype-basierte Cam-Calls.",
        "intro": "SkyPrivate ist eine besondere Cam-Plattform — statt RTMP-Broadcast werden <strong>Pay-per-Minute-Private-Cam-Calls über Skype</strong> abgerechnet. Kunden buchen und zahlen pro Minute im SkyPrivate-Marketplace, der eigentliche Video-Call läuft anschließend über Skype. Kostenloses <strong style='color:var(--text)'>SplitCam</strong> klinkt sich als <strong>virtuelle Kamera</strong> ein: Szene in SplitCam bauen, dann in Skype SplitCam als Kamera auswählen, bevor du einen über SkyPrivate gebuchten Call annimmst.",
        "quick": "SkyPrivate mit SplitCam nutzen: SplitCam installieren, Szene bauen, Skype mit dem SkyPrivate-Add-on installieren, in Skypes <em>Video-Einstellungen</em> SplitCam als Kamera und Mikrofon wählen, dann SkyPrivate-Buchungen annehmen — Skype liefert deine komponierte Szene an den Kunden."
                 "<ol><li>SplitCam installieren.</li><li>Szene in SplitCam bauen.</li><li>Skype + SkyPrivate-Add-on installieren.</li><li>SplitCam in Skype als Kamera wählen.</li><li>Calls annehmen.</li></ol>",
        "key_how": "SkyPrivate verwendet weder RTMP noch einen Stream Key — Skype dient als Video-Transport, das SkyPrivate-Add-on übernimmt die Minutenabrechnung. Skype installieren, das SkyPrivate-Browser-/Desktop-Add-on installieren, dann in Skype <strong>Einstellungen → Audio &amp; Video → Kamera</strong> öffnen und <strong>SplitCam</strong> statt der Webcam wählen. Die komponierte SplitCam-Szene (Overlays, Multi-Cam, Beauty-Filter) ist genau das, was der SkyPrivate-Kunde über Skype sieht.",
        "tips": [
            ("Kein RTMP — Virtual-Camera-Flow", "Such nicht nach Server-URL oder Stream Key. SkyPrivate läuft über Skype, und Skype erkennt SplitCam einfach als Webcam-Gerät. Szene in SplitCam bauen, dann in Skypes Kamera-Einstellungen SplitCam auswählen."),
            ("SplitCam auch als Mikrofon setzen", "In den Audio-Einstellungen von Skype zusätzlich SplitCam als Mikrofon wählen — so erreichen Rauschunterdrückung, gemischtes Audio und Intro-Musik den Kunden mit."),
            ("Test-Call in Skype vorab", "Vor dem ersten bezahlten SkyPrivate-Call einen kostenlosen Skype-Testcall machen (Echo / Sound Test Service), um zu prüfen, dass SplitCam als Kamera aktiv ist und die Szene sauber komponiert ist."),
            _T_TEST,
        ],
        "faq": [
            ("Nutzt SkyPrivate RTMP oder einen Stream Key?", "Weder noch. SkyPrivate übernimmt Abrechnung und Buchung; der eigentliche Video-Call läuft über Skype. Es gibt keine RTMP-Server-URL und keinen Stream Key — du konfigurierst SplitCam einfach als Kamera in Skype."),
            ("Wie wähle ich SplitCam für SkyPrivate in Skype aus?", "Skype-Einstellungen → Audio &amp; Video → Kamera öffnen und SplitCam aus der Liste auswählen. Beim Mikrofon dasselbe. SkyPrivate-Calls kommen dann als normale Skype-Anrufe rein, mit deiner SplitCam-Szene als Kamerabild."),
            ("Funktionieren Overlays und Beauty-Filter mit SkyPrivate?", "Ja — die werden in der SplitCam-Szene zusammengestellt. Skype bekommt nur das fertig komponierte Bild als ein Kamera-Feed, also ist alles aus SplitCam (Overlays, Beauty-Filter, KI-Hintergrund, Multi-Cam-Szenen) für den SkyPrivate-Kunden sichtbar."),
            ("Ist SplitCam für SkyPrivate kostenlos?", "Ja — SplitCam ist kostenlos, ohne Wasserzeichen und ohne Zeitlimit. Als virtuelle Kamera für Skype-basierte SkyPrivate-Calls fallen keine zusätzlichen Kosten an und es wird kein Branding eingeblendet."),
        ],
        "steps": [
            ("SplitCam installieren", "SplitCam ist kostenlos für Windows und macOS — ohne Registrierung, ohne Kreditkarte, ohne Wasserzeichen. Für SkyPrivate fungiert es als <strong>virtuelle Kamera</strong>, die Skype wie jede andere Webcam erkennt."),
            ("Szene in SplitCam bauen", "SplitCam öffnen und über <strong>Media Layers +</strong> die Webcam plus Overlays, Text, Beauty-Filter oder KI-Hintergrund hinzufügen. Genau diese Szene liefert Skype später an den SkyPrivate-Kunden."),
            ("Skype und SkyPrivate-Add-on installieren", "Skype auf demselben PC installieren, anmelden, dann das SkyPrivate-Add-on / die Desktop-App gemäß SkyPrivates Onboarding einrichten. Das Add-on regelt die Minutenabrechnung auf SkyPrivate-Seite."),
            ("In Skype SplitCam als Kamera und Mikrofon wählen", "In Skype <strong>Einstellungen → Audio &amp; Video</strong> öffnen. <strong>Kamera = SplitCam</strong> und <strong>Mikrofon = SplitCam</strong> setzen. Schnellen Skype-Testcall (Echo / Sound Test Service) machen, um Bild und Ton zu prüfen."),
            ("SkyPrivate-Calls annehmen", "Bucht ein SkyPrivate-Kunde einen bezahlten Call, kommt er als Skype-Anruf rein — einfach annehmen. Der Kunde sieht deine komponierte SplitCam-Szene; SkyPrivate rechnet pro Minute ab. Szene mitten im Call ändern? Direkt in SplitCam anpassen — Skype zeigt das sofort."),
        ],
    },
    {
        "slug": "manyvids", "name": "ManyVids",
        "title": "Auf MV Live (ManyVids) live gehen mit SplitCam",
        "desc": "Auf ManyVids' MV Live live gehen mit kostenlosem SplitCam — Creator Studio External Encoder, Multi-Cam-Szenen und Overlays. Ohne Wasserzeichen.",
        "kw": "auf manyvids live gehen, manyvids, manyvids live, mv live, manyvids obs, mv live external encoder, manyvids stream key",
        "h1html": 'So sendest du auf <span class="accent">MV Live</span> mit SplitCam',
        "h1short": "Auf MV Live senden",
        "card": "External-Encoder-Setup für ManyVids' MV Live im Creator Studio.",
        "intro": "ManyVids ist eine Creator-Economy-Plattform — Clip-Verkäufe, Custom Videos, Fan-Club-Abos und das Live-Streaming-Produkt <strong>MV Live</strong>. Der Standard-Broadcaster im Creator Studio läuft im Browser, daneben gibt es einen klassischen <strong>External Encoder</strong>-Pfad, an den sich kostenloses <strong style='color:var(--text)'>SplitCam</strong> anschließt — für Multi-Cam-Szenen, Overlays und Filter auf derselben creator-freundlichen Plattform.",
        "quick": "Auf MV Live mit SplitCam senden: SplitCam installieren, Szene bauen, im Creator Studio <em>MV Live → Broadcast Settings → External Encoder</em> öffnen, Server-URL und Stream Key kopieren, in SplitCam einfügen, Go Live."
                 "<ol><li>SplitCam installieren.</li><li>Kamera + Szene hinzufügen.</li><li>URL und Stream Key aus dem Creator Studio holen.</li><li>In SplitCam einfügen.</li><li>Go Live drücken.</li></ol>",
        "key_how": "Im ManyVids-Creator-Account anmelden, das <strong>Creator Studio</strong> öffnen und zu <strong>MV Live → Broadcast Settings → External Encoder</strong> navigieren. Die Seite zeigt eine an deinen Account gebundene <strong>Server-URL</strong> und einen <strong>Stream Key</strong> — beides in die Custom-RTMP-Felder von SplitCam kopieren. Creator-Accounts müssen vollständig verifiziert sein (ID + Steuer), bevor MV Live verfügbar ist.",
        "tips": [
            ("Creator Economy, nicht nur Live", "ManyVids ist keine reine Cam-Plattform — MV Live ist eine von mehreren Einnahmequellen neben Clip-Verkäufen, Custom Videos und Fan-Club-Abos. Live-Streams gezielt nutzen, um Zuschauer zu deinen anderen Monetarisierungen zu führen."),
            ("Token-Tipping in MV Live", "MV Live hat ein eigenes Token-Tipping-System im Live-Room. Goal-Menüs und Reward-Trigger ähnlich wie bei Chaturbate / Stripchat planen — funktionieren beim ManyVids-Publikum gut."),
            ("Browser vs. External Encoder", "Der eingebaute Browser-Broadcaster im Creator Studio ist Single-Cam. SplitCam über External Encoder schaltet Multi-Cam-Szenen, Overlays und Filter frei."),
            _T_ETH,
        ],
        "faq": [
            ("Unterstützt MV Live (ManyVids) externe Encoder wie SplitCam?", "Ja — der MV-Live-Bereich im Creator Studio hat unter Broadcast Settings die Option External Encoder. Standard-RTMP-Server-URL und Stream Key; OBS, SplitCam und vMix verbinden sich problemlos."),
            ("Wo bekomme ich meinen MV-Live-Stream-Key?", "Creator Studio → MV Live → Broadcast Settings → External Encoder. Server-URL und Stream Key erscheinen dort — beides in die Custom-RTMP-Felder von SplitCam kopieren."),
            ("Welche Bitrate für MV Live?", "Anpeilen: 1920×1080 bei 30 fps, 3.500–6.000 Kbps und 2 Sekunden Keyframe-Intervall. Vorher den eingebauten Speedtest von SplitCam laufen lassen."),
            ("Ist SplitCam bei MV Live kostenlos nutzbar?", "Ja — SplitCam ist kostenlos, ohne Wasserzeichen und ohne Zeitlimit. Die External-Encoder-Option von ManyVids ist im Creator Studio kostenlos."),
        ],
        "steps": [
            ("SplitCam herunterladen und installieren", "SplitCam ist kostenlose Live-Streaming-Software für Windows und macOS — ohne Registrierung, ohne Kreditkarte, ohne Wasserzeichen."),
            ("Szene aufbauen", "SplitCam öffnen und die Webcam hinzufügen. Overlays, Text, eine zweite Kamera oder das Smartphone, Beauty-Filter oder einen KI-Hintergrund einbauen — perfekt für MV-Live-Goal-Reveals und Reward-Trigger."),
            ("MV-Live-URL und Stream-Key holen", "Im ManyVids-Creator-Account anmelden, das <strong>Creator Studio</strong> öffnen und zu <strong>MV Live → Broadcast Settings → External Encoder</strong> navigieren. Die Seite zeigt eine <strong>Server-URL</strong> und einen eindeutigen <strong>Stream Key</strong>. Beides kopieren."),
            ("SplitCam mit MV Live verbinden", "In SplitCam <strong>Stream Settings</strong> öffnen, die MV-Live-Server-URL und den Stream Key in die Custom-RTMP-Felder einfügen. Bitrate auf 3.500–6.000 Kbps bei 1920×1080, 30 fps und 2 Sekunden Keyframe stellen."),
            ("Go Live drücken", "In SplitCam auf <strong>Go Live</strong> klicken, dann im Creator Studio den MV-Live-Broadcast starten. Innerhalb von ~10 Sekunden erreicht dein Stream das MV-Live-Publikum."),
        ],
    },
    {
        "slug": "fansly", "name": "Fansly",
        "title": "Auf Fansly Live live gehen mit SplitCam — External Encoder",
        "desc": "Auf Fansly Live live gehen mit kostenlosem SplitCam — Creator Dashboard External Encoder, Multi-Cam-Szenen und Overlays. Ohne Wasserzeichen.",
        "kw": "auf fansly live gehen, fansly, fansly live, fansly broadcast, fansly obs, fansly external encoder, fansly rtmp, fansly stream key",
        "h1html": 'So sendest du auf <span class="accent">Fansly Live</span> mit SplitCam',
        "h1short": "Auf Fansly senden",
        "card": "External-Encoder-Setup für Fansly's Creator Dashboard.",
        "intro": "Fansly ist ein direkter OnlyFans-Konkurrent mit lockereren Content-Regeln und einer wachsenden Creator-Basis — Abos, Pay-per-View-Inhalte und das Live-Streaming-Produkt <strong>Fansly Live</strong>. Der Standard-Broadcaster läuft im Browser, doch das <strong>Creator Dashboard</strong> bietet zusätzlich einen klassischen <strong>External Encoder</strong>-Pfad, an den sich kostenloses <strong style='color:var(--text)'>SplitCam</strong> anschließt — für Multi-Cam-Szenen, Overlays und Filter direkt an deine Abonnenten.",
        "quick": "Auf Fansly Live mit SplitCam senden: SplitCam installieren, Szene bauen, im Creator Dashboard <em>Live → Broadcast Settings → External Encoder</em> öffnen, Server-URL und Stream Key kopieren, in SplitCam einfügen, Go Live."
                 "<ol><li>SplitCam installieren.</li><li>Kamera + Szene hinzufügen.</li><li>URL und Stream Key aus dem Creator Dashboard holen.</li><li>In SplitCam einfügen.</li><li>Go Live drücken.</li></ol>",
        "key_how": "Im Fansly-Creator-Account anmelden, das <strong>Creator Dashboard</strong> öffnen und zu <strong>Live → Broadcast Settings → External Encoder</strong> navigieren. Die Seite zeigt eine an deinen Account gebundene <strong>Server-URL</strong> und einen <strong>Stream Key</strong> — beides in die Custom-RTMP-Felder von SplitCam kopieren. Creator-Accounts brauchen eine ID-Verifizierung, bevor Fansly Live freigeschaltet wird.",
        "tips": [
            ("Abonnenten-fokussiertes Publikum", "Fanslys Publikum ist abo-basiert — dein Live-Stream erreicht Leute, die dich ohnehin schon monatlich bezahlen. Content auf Treue ausrichten (exklusive Q&amp;A, Behind-the-Scenes, individuelle Tip-Goals) statt auf Public-Room-Metriken zu jagen."),
            ("Tips zusätzlich zu Abos", "Fansly Live unterstützt In-Stream-Tipping zusätzlich zum Grund-Abo. Die kombinierten Einnahmen können bei etablierten Creators reines Cam-Plattform-Tipping übertreffen."),
            ("Browser-Broadcaster vs. External", "Der Standard-Browser-Broadcaster ist Single-Source. SplitCam über External Encoder schaltet Multi-Cam, Overlays, Beauty-Filter und KI-Hintergrund frei — passend zum Premium-Anspruch von Abo-Content."),
            _T_ETH,
        ],
        "faq": [
            ("Unterstützt Fansly Live externe Encoder wie SplitCam?", "Ja — der Live-Bereich im Creator Dashboard hat unter Broadcast Settings die Option External Encoder. Standard-RTMP-Server-URL und Stream Key; OBS, SplitCam und vMix verbinden sich problemlos."),
            ("Wo bekomme ich meinen Fansly-Stream-Key?", "Creator Dashboard → Live → Broadcast Settings → External Encoder. Server-URL und Stream Key erscheinen dort. Beides in die Custom-RTMP-Felder von SplitCam kopieren."),
            ("Welche Bitrate für Fansly Live?", "Anpeilen: 1920×1080 bei 30 fps, 3.500–6.000 Kbps und 2 Sekunden Keyframe-Intervall. Vorher den eingebauten Speedtest von SplitCam laufen lassen."),
            ("Ist SplitCam bei Fansly kostenlos nutzbar?", "Ja — SplitCam ist kostenlos, ohne Wasserzeichen und ohne Zeitlimit. Die External-Encoder-Option von Fansly ist im Creator Dashboard kostenlos."),
        ],
        "steps": [
            ("SplitCam herunterladen und installieren", "SplitCam ist kostenlose Live-Streaming-Software für Windows und macOS — ohne Registrierung, ohne Kreditkarte, ohne Wasserzeichen."),
            ("Szene aufbauen", "SplitCam öffnen und die Webcam hinzufügen. Overlays, Text, eine zweite Kamera oder das Smartphone, Beauty-Filter oder einen KI-Hintergrund einbauen — polierte Szenen passen zum Premium-Erwartungswert zahlender Abonnenten."),
            ("Fansly-URL und Stream-Key holen", "Im Fansly-Creator-Account anmelden, das <strong>Creator Dashboard</strong> öffnen und zu <strong>Live → Broadcast Settings → External Encoder</strong> navigieren. Die Seite zeigt eine <strong>Server-URL</strong> und einen eindeutigen <strong>Stream Key</strong>. Beides kopieren."),
            ("SplitCam mit Fansly verbinden", "In SplitCam <strong>Stream Settings</strong> öffnen, die Fansly-Server-URL und den Stream Key in die Custom-RTMP-Felder einfügen. Bitrate auf 3.500–6.000 Kbps bei 1920×1080, 30 fps und 2 Sekunden Keyframe stellen."),
            ("Go Live drücken", "In SplitCam auf <strong>Go Live</strong> klicken, dann im Creator Dashboard den Fansly-Live-Broadcast starten. Innerhalb von ~10 Sekunden erreicht dein Stream deine Fansly-Abonnenten."),
        ],
    },
    {
        "slug": "ifriends", "name": "iFriends",
        "title": "Auf iFriends senden mit SplitCam — External Encoder",
        "desc": "Auf iFriends senden mit kostenlosem SplitCam — Model Center External Encoder, Multi-Cam-Szenen und Overlays. Ohne Wasserzeichen, kostenlose Anleitung.",
        "kw": "auf ifriends senden, ifriends, ifriends broadcast, ifriends obs, ifriends external encoder, ifriends rtmp, ifriends stream key",
        "h1html": 'So sendest du auf <span class="accent">iFriends</span> mit SplitCam',
        "h1short": "Auf iFriends senden",
        "card": "External-Encoder-Setup für das gereifte Model Center von iFriends.",
        "intro": "iFriends (WebPower) ist eines der am längsten betriebenen unabhängigen Cam-Netzwerke — leise profitabel, loyale Nutzerbasis und ein gereiftes Model Center, das vor dem Aufkommen der Browser-Broadcaster gebaut wurde. Die Plattform unterstützt einen Standard-<strong>External Encoder</strong>-Pfad aus dem Model Center, an den sich kostenloses <strong style='color:var(--text)'>SplitCam</strong> anschließt — für moderne Multi-Cam-Szenen, Overlays und Filter in diesem etablierten Netzwerk.",
        "quick": "Auf iFriends mit SplitCam senden: SplitCam installieren, Szene bauen, im Model Center <em>Broadcast Settings → External Encoder</em> öffnen, Server-URL und Stream Key kopieren, in SplitCam einfügen, Go Live."
                 "<ol><li>SplitCam installieren.</li><li>Kamera + Szene hinzufügen.</li><li>URL und Stream Key aus dem Model Center holen.</li><li>In SplitCam einfügen.</li><li>Go Live drücken.</li></ol>",
        "key_how": "Im iFriends-Model-Account anmelden, das <strong>Model Center</strong> öffnen und zu <strong>Broadcast Settings → External Encoder</strong> navigieren. Die Seite zeigt eine an den Account gebundene <strong>Server-URL</strong> und einen <strong>Stream Key</strong> — beides in die Custom-RTMP-Felder von SplitCam kopieren. Die iFriends-Freigabe für neue Model-Accounts ist streng, aber seriös; nach der Verifizierung bleibt die External-Encoder-Option dauerhaft verfügbar.",
        "tips": [
            ("Long-Tail-Publikum, gereiftes Netzwerk", "iFriends läuft seit Ende der 1990er mit treuer Nutzerbasis — viele Nutzer sind langjährige Abonnenten, keine Erstbesucher. Stabiles Einkommen für etablierte Models, langsameres Wachstum für Neueinsteiger."),
            ("Browser-Broadcaster vs. External", "Der Legacy-Broadcaster von iFriends entstand vor moderner Multi-Cam-UX. Der Wechsel zu SplitCam über External Encoder ist ein spürbares Upgrade — Multi-Cam-Szenen, Overlays und Beauty-Filter, die das alte Tool nicht liefern kann."),
            ("Verlässliche Auszahlungen, wenig Überraschungen", "Die Mutter (WebPower) zahlt Models seit Jahrzehnten zuverlässig — langsamere Auszahlungszyklen als bei neueren krypto-freundlichen Plattformen, dafür sehr wenige Horrorstorys."),
            _T_ETH,
        ],
        "faq": [
            ("Unterstützt iFriends offiziell externe Encoder wie SplitCam?", "Ja — das Model Center hat unter Broadcast Settings die Option External Encoder. Standard-RTMP-Server-URL und Stream Key; OBS, SplitCam und vMix verbinden sich, sobald der Account freigegeben ist."),
            ("Wo bekomme ich meinen iFriends-Stream-Key?", "Model Center → Broadcast Settings → External Encoder. Server-URL und Stream Key erscheinen dort — beides in die Custom-RTMP-Felder von SplitCam kopieren."),
            ("Welche Bitrate für iFriends?", "Anpeilen: 1920×1080 bei 30 fps, 3.500–6.000 Kbps und 2 Sekunden Keyframe-Intervall. Vorher den eingebauten Speedtest von SplitCam laufen lassen."),
            ("Ist SplitCam bei iFriends kostenlos nutzbar?", "Ja — SplitCam ist kostenlos, ohne Wasserzeichen und ohne Zeitlimit. Die External-Encoder-Option von iFriends ist im Model Center kostenlos."),
        ],
        "steps": [
            ("SplitCam herunterladen und installieren", "SplitCam ist kostenlose Live-Streaming-Software für Windows und macOS — ohne Registrierung, ohne Kreditkarte, ohne Wasserzeichen."),
            ("Szene aufbauen", "SplitCam öffnen und die Webcam hinzufügen. Overlays, Text, eine zweite Kamera oder das Smartphone, Beauty-Filter oder einen KI-Hintergrund einbauen — polierte moderne Szenen heben sich in diesem gereiften Netzwerk ab."),
            ("iFriends-URL und Stream-Key holen", "Im iFriends-Model-Account anmelden, das <strong>Model Center</strong> öffnen und zu <strong>Broadcast Settings → External Encoder</strong> navigieren. Die Seite zeigt eine <strong>Server-URL</strong> und einen eindeutigen <strong>Stream Key</strong>. Beides kopieren."),
            ("SplitCam mit iFriends verbinden", "In SplitCam <strong>Stream Settings</strong> öffnen, die iFriends-Server-URL und den Stream Key in die Custom-RTMP-Felder einfügen. Bitrate auf 3.500–6.000 Kbps bei 1920×1080, 30 fps und 2 Sekunden Keyframe stellen."),
            ("Go Live drücken", "In SplitCam auf <strong>Go Live</strong> klicken, dann im iFriends Model Center online gehen. Innerhalb von ~10 Sekunden erreicht dein Stream das Netzwerk."),
        ],
    },
    {
        "slug": "babestation", "name": "Babestation",
        "title": "Auf Babestation senden mit SplitCam — UK-Cam-Netzwerk-Setup",
        "desc": "Auf Babestation senden mit kostenlosem SplitCam — Performer Hub External Encoder, Multi-Cam-Szenen und Overlays. Ohne Wasserzeichen, kostenlose Anleitung.",
        "kw": "auf babestation senden, babestation, babestation broadcast, babestation obs, babestation external encoder, babestation rtmp, babestation cam",
        "h1html": 'So sendest du auf <span class="accent">Babestation</span> mit SplitCam',
        "h1short": "Auf Babestation senden",
        "card": "External-Encoder-Setup für den britischen Performer Hub von Babestation.",
        "intro": "Babestation ist das führende britische Adult-TV-/Cam-Netzwerk — ein Hybrid aus Broadcast-TV-Kanälen und einem Live-Cam-Produkt, das von Performern im Performer Hub gespeist wird. Die Plattform unterstützt einen Standard-<strong>External Encoder</strong>-Pfad aus dem Performer Hub, an den sich kostenloses <strong style='color:var(--text)'>SplitCam</strong> anschließt — damit unabhängige UK-Performer mit Multi-Cam-Szenen, Overlays und Beauty-Filtern senden können, die über Babestations TV-Studio-Standard-Broadcaster hinausgehen.",
        "quick": "Auf Babestation mit SplitCam senden: SplitCam installieren, Szene bauen, im Performer Hub <em>Broadcast Settings → External Encoder</em> öffnen, Server-URL und Stream Key kopieren, in SplitCam einfügen, Go Live."
                 "<ol><li>SplitCam installieren.</li><li>Kamera + Szene hinzufügen.</li><li>URL und Stream Key aus dem Performer Hub holen.</li><li>In SplitCam einfügen.</li><li>Go Live drücken.</li></ol>",
        "key_how": "Im Babestation-Performer-Account anmelden, den <strong>Performer Hub</strong> öffnen und zu <strong>Broadcast Settings → External Encoder</strong> navigieren. Die Seite zeigt eine an den Account gebundene <strong>Server-URL</strong> und einen <strong>Stream Key</strong> — beides in die Custom-RTMP-Felder von SplitCam kopieren. Das UK-Performer-Onboarding bei Babestation beinhaltet eine ID-Verifizierung gemäß britischer Altersnachweispflicht.",
        "tips": [
            ("UK-zentriertes Publikum und Timing", "Babestations Prime-Traffic liegt am UK-Abend / in der UK-Nacht (GMT/BST). Aus anderen Zeitzonen schlägt eine Sendung zur britischen Nachtzeit das lokale Prime-Time deutlich."),
            ("TV-Studio-Politur wird erwartet", "Die Marke Babestation hängt eng an ihren TV-Kanälen — Zuschauer erwarten produzierter wirkende Sets und Beleuchtung als bei einem typischen Webcam-Stream. SplitCam-Szenen (Overlays, Markentext, KI-Hintergrund) treffen die polierte Ästhetik der Plattform."),
            ("Unabhängige vs. Studio-Performer", "Babestation arbeitet sowohl mit britischen Studios als auch mit unabhängigen Performern. Wer als Independent über External Encoder einspeist, bekommt das gleiche Auszahlungsmodell wie Studio-Kameras."),
            _T_ETH,
        ],
        "faq": [
            ("Unterstützt Babestation externe Encoder wie SplitCam?", "Ja — der Performer Hub hat unter Broadcast Settings die Option External Encoder. Standard-RTMP-Server-URL und Stream Key; OBS, SplitCam und vMix verbinden sich, sobald die Performer-Verifizierung abgeschlossen ist."),
            ("Wo bekomme ich meinen Babestation-Stream-Key?", "Performer Hub → Broadcast Settings → External Encoder. Server-URL und Stream Key erscheinen dort — beides in die Custom-RTMP-Felder von SplitCam kopieren."),
            ("Welche Bitrate für Babestation?", "Anpeilen: 1920×1080 bei 30 fps, 3.500–6.000 Kbps und 2 Sekunden Keyframe-Intervall. Die UK-Upload-Bandbreite ist meist stark, vorher trotzdem den SplitCam-Speedtest laufen lassen."),
            ("Ist SplitCam bei Babestation kostenlos nutzbar?", "Ja — SplitCam ist kostenlos, ohne Wasserzeichen und ohne Zeitlimit. Die External-Encoder-Option von Babestation ist im Performer Hub kostenlos."),
        ],
        "steps": [
            ("SplitCam herunterladen und installieren", "SplitCam ist kostenlose Live-Streaming-Software für Windows und macOS — ohne Registrierung, ohne Kreditkarte, ohne Wasserzeichen."),
            ("Szene aufbauen", "SplitCam öffnen und die Webcam hinzufügen. Overlays, Text, eine zweite Kamera oder das Smartphone, Beauty-Filter oder einen KI-Hintergrund einbauen — der Babestation-TV-Studio-Politur entsprechen, um aufzufallen."),
            ("Babestation-URL und Stream-Key holen", "Im Babestation-Performer-Account anmelden, den <strong>Performer Hub</strong> öffnen und zu <strong>Broadcast Settings → External Encoder</strong> navigieren. Die Seite zeigt eine <strong>Server-URL</strong> und einen eindeutigen <strong>Stream Key</strong>. Beides kopieren."),
            ("SplitCam mit Babestation verbinden", "In SplitCam <strong>Stream Settings</strong> öffnen, die Babestation-Server-URL und den Stream Key in die Custom-RTMP-Felder einfügen. Bitrate auf 3.500–6.000 Kbps bei 1920×1080, 30 fps und 2 Sekunden Keyframe stellen."),
            ("Go Live drücken", "In SplitCam auf <strong>Go Live</strong> klicken, dann im Performer Hub online gehen. Innerhalb von ~10 Sekunden erreicht dein Stream Babestations UK-Publikum."),
        ],
    },
    {
        "slug": "adultwork", "name": "AdultWork",
        "title": "Auf AdultWork senden mit SplitCam — External Encoder",
        "desc": "Auf AdultWork senden mit kostenlosem SplitCam — Members Area External Encoder, Multi-Cam-Szenen und Overlays. Ohne Wasserzeichen, kostenlose Anleitung.",
        "kw": "auf adultwork senden, adultwork, adultwork broadcast, adultwork obs, adultwork external encoder, adultwork rtmp, adultwork cam",
        "h1html": 'So sendest du auf <span class="accent">AdultWork</span> mit SplitCam',
        "h1short": "Auf AdultWork senden",
        "card": "External-Encoder-Setup für das Cam-Feature im britischen Members Area von AdultWork.",
        "intro": "AdultWork ist der etablierte britische Adult-Service-Marktplatz — primär bekannt für Escort-Buchungen, Foto-/Videoverkauf und Telefonservices, mit einem zusätzlichen Live-<strong>Webcam-Feature</strong>. Die Plattform unterstützt einen Standard-<strong>External Encoder</strong>-Pfad aus der Members Area, an den sich kostenloses <strong style='color:var(--text)'>SplitCam</strong> anschließt — damit unabhängige UK-Performer Live-Cam-Umsätze mit Multi-Cam-Szenen, Overlays und Filtern dazunehmen.",
        "quick": "Auf AdultWork mit SplitCam senden: SplitCam installieren, Szene bauen, in der Members Area <em>Members → Broadcasting → External Encoder</em> öffnen, Server-URL und Stream Key kopieren, in SplitCam einfügen, Go Live."
                 "<ol><li>SplitCam installieren.</li><li>Kamera + Szene hinzufügen.</li><li>URL und Stream Key aus der Members Area holen.</li><li>In SplitCam einfügen.</li><li>Go Live drücken.</li></ol>",
        "key_how": "Im AdultWork-Performer-Account anmelden, die <strong>Members Area</strong> öffnen und zu <strong>Members → Broadcasting → External Encoder</strong> navigieren. Die Seite zeigt eine an den Account gebundene <strong>Server-URL</strong> und einen <strong>Stream Key</strong> — beides in die Custom-RTMP-Felder von SplitCam kopieren. Die AdultWork-Verifizierung ist für das Live-Cam-Feature Pflicht und deckt die britische Altersnachweispflicht ab.",
        "tips": [
            ("Cross-Sell aus den übrigen AdultWork-Services", "Die Stärke von AdultWork ist die vorhandene Kundenbasis — Zuschauer buchen bei dir vielleicht schon Foto-/Video-/Telefonservices. Live-Cam-Streams gezielt zum Cross-Sell an Kunden nutzen, die deinen Cam noch nicht kennen, statt Fremden hinterherzujagen."),
            ("Members Area ist der Einstieg", "Den Broadcaster nicht auf der öffentlichen Seite suchen — alles Performer-seitige sitzt in der Members Area. Sendeeinstellungen, Auszahlungen, Content-Verwaltung — alles dort."),
            ("UK-zentriert, aber internationale Auszahlungen", "Der Großteil des Traffics ist UK/EU. Auszahlungen laufen international via Standard-Banküberweisung / E-Wallet, oft im Wochenrhythmus."),
            _T_ETH,
        ],
        "faq": [
            ("Unterstützt AdultWork externe Encoder wie SplitCam?", "Ja — die Members Area hat unter Broadcasting die Option External Encoder. Standard-RTMP-Server-URL und Stream Key; OBS, SplitCam und vMix verbinden sich nach der Performer-Verifizierung."),
            ("Wo bekomme ich meinen AdultWork-Stream-Key?", "Members Area → Members → Broadcasting → External Encoder. Server-URL und Stream Key erscheinen dort — beides in die Custom-RTMP-Felder von SplitCam kopieren."),
            ("Welche Bitrate für AdultWork?", "Anpeilen: 1920×1080 bei 30 fps, 3.500–6.000 Kbps und 2 Sekunden Keyframe-Intervall. Vorher den eingebauten Speedtest von SplitCam laufen lassen."),
            ("Ist SplitCam bei AdultWork kostenlos nutzbar?", "Ja — SplitCam ist kostenlos, ohne Wasserzeichen und ohne Zeitlimit. Die External-Encoder-Option von AdultWork ist in der Members Area kostenlos."),
        ],
        "steps": [
            ("SplitCam herunterladen und installieren", "SplitCam ist kostenlose Live-Streaming-Software für Windows und macOS — ohne Registrierung, ohne Kreditkarte, ohne Wasserzeichen."),
            ("Szene aufbauen", "SplitCam öffnen und die Webcam hinzufügen. Overlays, Text, eine zweite Kamera oder das Smartphone, Beauty-Filter oder einen KI-Hintergrund einbauen — Overlays gezielt nutzen, um deine AdultWork-Inhalte / Telefondienste zu bewerben und während des Lives cross-zusellen."),
            ("AdultWork-URL und Stream-Key holen", "Im AdultWork-Performer-Account anmelden, die <strong>Members Area</strong> öffnen und zu <strong>Members → Broadcasting → External Encoder</strong> navigieren. Die Seite zeigt eine <strong>Server-URL</strong> und einen eindeutigen <strong>Stream Key</strong>. Beides kopieren."),
            ("SplitCam mit AdultWork verbinden", "In SplitCam <strong>Stream Settings</strong> öffnen, die AdultWork-Server-URL und den Stream Key in die Custom-RTMP-Felder einfügen. Bitrate auf 3.500–6.000 Kbps bei 1920×1080, 30 fps und 2 Sekunden Keyframe stellen."),
            ("Go Live drücken", "In SplitCam auf <strong>Go Live</strong> klicken, dann in der Members Area online gehen. Innerhalb von ~10 Sekunden erreicht dein Stream das AdultWork-Publikum."),
        ],
    },
    {
        "slug": "jerkmate", "name": "Jerkmate",
        "title": "Auf Jerkmate senden mit SplitCam — Streamate-Netzwerk-Setup",
        "desc": "Auf Jerkmate senden mit kostenlosem SplitCam — Jerkmate zieht Models aus dem Streamate-Netzwerk, du sendest über SM Connect. Multi-Cam, ohne Wasserzeichen.",
        "kw": "auf jerkmate senden, jerkmate, jerkmate broadcast, jerkmate sm connect, jerkmate streamate, jerkmate obs, jerkmate model werden",
        "h1html": 'So sendest du auf <span class="accent">Jerkmate</span> mit SplitCam',
        "h1short": "Auf Jerkmate senden",
        "card": "Jerkmate zieht Models aus dem Streamate-Netzwerk — Senden über SM Connect + SplitCam.",
        "intro": "Jerkmate ist eine der meistgesuchten Cam-Marken, bekannt für seinen KI-Matchmaker, der Zuschauer mit Live-Performern zusammenbringt. Einen eigenen Broadcaster betreibt Jerkmate nicht — die Plattform <strong>bezieht ihre Live-Models aus dem Streamate-Netzwerk</strong>. Du sendest als Model im Streamate-Netzwerk, und deine Show wird an Jerkmate und dessen Partnerseiten verteilt. Weil Streamate in <strong style='color:var(--text)'>SplitCams</strong> Kanalliste vorinstalliert ist, kannst du mit kostenlosem <strong style='color:var(--text)'>SplitCam</strong> Multi-Cam-Szenen, Overlays und Filter hinzufügen, ganz ohne manuelle RTMP-Eingabe.",
        "quick": "Auf Jerkmate mit SplitCam senden: SplitCam installieren, Szene bauen, als Model im Streamate-Netzwerk anmelden, das Jerkmate speist, über <em>SM Connect → Start Show</em> den Key kopieren, dann in SplitCam <em>Stream Settings → Add Channel → Streamate</em> öffnen, einfügen und Go Live."
                 "<ol><li>SplitCam installieren.</li><li>Kamera + Szene hinzufügen.</li>"
                 "<li>Als Model im Streamate-Netzwerk anmelden.</li>"
                 "<li>Key über SM Connect holen.</li>"
                 "<li>Add Channel → Streamate, Go Live.</li></ol>",
        "key_how": "Jerkmates Live-Cams kommen aus dem <strong>Streamate-Broadcasting-Netzwerk</strong> — einen separaten «Jerkmate-Encoder» gibt es nicht. Über Jerkmates Model-Programm oder direkt im Streamate-Netzwerk registrieren, <strong>SM Connect</strong> öffnen, die Bedingungen akzeptieren, <strong>Start Show</strong> klicken und den Streaming-Key kopieren. In SplitCam <strong>Stream Settings → Add Channel</strong> öffnen, <strong>Streamate</strong> aus der eingebauten Liste wählen und den Key einfügen. Dein Stream erreicht dann Jerkmate und die Partnerseiten des Netzwerks gleichzeitig.",
        "tips": [
            ("Darunter steckt das Streamate-Netzwerk", "Such keinen Jerkmate-eigenen Broadcaster — du sendest auf Streamate, und Jerkmate verteilt es weiter. Alles, was für Streamate funktioniert (SM Connect, der eingebaute SplitCam-Kanal), funktioniert auch für Jerkmate."),
            ("Den KI-gematchten Traffic umwandeln", "Jerkmates Matchmaker leitet Zuschauer zu Models, die zu ihren Vorlieben passen — eine polierte SplitCam-Szene mit Overlays und gutem Bildausschnitt wandelt diese gematchten Zuschauer weit besser um als eine flache Webcam."),
            ("Ein Feed, viele Seiten", "Senden ins Streamate-Netzwerk bringt dich gleichzeitig auf Jerkmate plus dessen Partnerseiten — größere Reichweite aus einem einzigen SplitCam-Stream, ohne Zusatzaufwand."),
            _T_ETH,
        ],
        "faq": [
            ("Hat Jerkmate einen eigenen Broadcaster oder Stream-Key?", "Nein — Jerkmate bezieht seine Live-Models aus dem Streamate-Netzwerk. Du sendest als Model im Streamate-Netzwerk über SM Connect, und deine Show erscheint automatisch auf Jerkmate."),
            ("Wie bekomme ich meinen Jerkmate-Stream-Key?", "Über SM Connect auf der Model-Seite des Streamate-Netzwerks: Bedingungen akzeptieren → Start Show → Key kopieren. In den eingebauten Streamate-Kanal von SplitCam einfügen — keine manuelle RTMP-URL nötig."),
            ("Welche Bitrate für Jerkmate?", "1080p bei 30 fps fixieren. Der Netzwerk-Feed ist adaptiv, eine niedrigere Bitrate bei Standbildern ist also normal. Den SplitCam-Speedtest laufen lassen und eine Kabelverbindung nutzen."),
            ("Ist SplitCam kostenlos für Jerkmate?", "Ja — SplitCam ist kostenlos, ohne Wasserzeichen und ohne Zeitlimit. Streamate (das Jerkmate speist) ist ein eingebauter SplitCam-Kanal, es fallen also keine separaten Encoder-Kosten an."),
        ],
        "steps": [
            ("SplitCam herunterladen und installieren", "SplitCam ist kostenlose Live-Streaming-Software für Windows und macOS — ohne Registrierung, ohne Kreditkarte, ohne Wasserzeichen."),
            ("Szene aufbauen", "SplitCam öffnen und die Webcam hinzufügen. Overlays, Text, eine zweite Kamera oder das Smartphone, Beauty-Filter oder einen KI-Hintergrund einbauen — eine starke Szene wandelt Jerkmates gematchte Zuschauer um."),
            ("Als Model anmelden und Key holen", "Über Jerkmates Model-Programm oder direkt im <strong>Streamate-Netzwerk</strong>, das es speist, registrieren. <strong>SM Connect</strong> öffnen, die Bedingungen akzeptieren, <strong>Start Show</strong> klicken und den Streaming-Key kopieren."),
            ("Streamate als Kanal in SplitCam hinzufügen", "In SplitCam <strong>Stream Settings → Add Channel</strong> öffnen, <strong>Streamate</strong> aus der eingebauten Liste wählen und den Key einfügen — keine manuelle RTMP-URL. Die Auflösung auf 1080p fixieren."),
            ("Go Live drücken", "In SplitCam <strong>Go Live</strong> drücken — ein grüner Slider bestätigt die Verbindung. Deine Show geht übers Streamate-Netzwerk raus und erscheint auf Jerkmate."),
        ],
    },
    {
        "slug": "justforfans", "name": "JustForFans",
        "title": "Auf JustForFans live gehen mit SplitCam — virtuelle Kamera",
        "desc": "Auf JustForFans (JFF) live gehen mit kostenlosem SplitCam als virtuelle Kamera — Multi-Cam-Szenen, Overlays und Filter. Ohne Wasserzeichen.",
        "kw": "auf justforfans live gehen, justforfans, justforfans live, justforfans virtual camera, justforfans virtuelle kamera, justforfans obs, jff live stream",
        "h1html": 'So gehst du auf <span class="accent">JustForFans</span> live mit SplitCam',
        "h1short": "Auf JustForFans live gehen",
        "card": "SplitCam als virtuelle Kamera im Live-Broadcaster von JustForFans nutzen.",
        "intro": "JustForFans (JFF) ist eine creator-eigene Abo-Plattform — eine langjährige, von Performern gegründete OnlyFans-Alternative mit Abos, Pay-per-View und einem browserbasierten Live-Feature. Der Live-Broadcaster zeigt nur eine schlichte Webcam; richtest du ihn auf kostenloses <strong style='color:var(--text)'>SplitCam</strong> als <strong>virtuelle Kamera</strong>, schaltest du Multi-Cam-Szenen, Overlays und Filter frei. Bietet dein Creator-Dashboard zusätzlich eine External-Encoder- / Stream-Key-Option, verbindet sich SplitCam stattdessen über RTMP.",
        "quick": "Auf JustForFans mit SplitCam live: SplitCam installieren, Szene bauen, auf JFF einen Live-Broadcast starten und im Kamera-Auswahlmenü des Broadcasters <em>SplitCam</em> als Webcam wählen — dann live gehen."
                 "<ol><li>SplitCam installieren.</li><li>Kamera + Szene hinzufügen.</li>"
                 "<li>Live-Broadcast auf JFF starten.</li>"
                 "<li>SplitCam im Kamera-Dropdown wählen.</li><li>Go Live drücken.</li></ol>",
        "key_how": "Der Live-Modus von JustForFans läuft im Browser. Baue deine Szene in SplitCam — es registriert sich als System-Webcam namens <strong>«SplitCam Video Driver»</strong> — öffne dann den JFF-Live-Broadcaster und wähle im Kamera-Dropdown <strong>SplitCam</strong> statt deiner rohen Webcam. Deine komponierte Szene ersetzt die flache Kamera. Bietet JFFs Creator-Dashboard eine <strong>External-Encoder- / Stream-Key</strong>-Option, fügst du diesen Key stattdessen in die Custom-RTMP-Felder von SplitCam ein.",
        "tips": [
            ("Virtuelle Kamera funktioniert überall", "Auch wenn der Live-Modus einer Plattform nur im Browser läuft, erscheint SplitCam als auswählbare Webcam — deine Multi-Cam-Szene, Overlays und Filter funktionieren auf JFF also ganz ohne Stream-Key."),
            ("Creator-eigen, performer-freundlich", "JFF wird von Performern betrieben und hat eine treue Abonnentenbasis. Overlays, die dein PPV oder Abo bewerben, wandeln bei einem Publikum gut, das ohnehin schon zahlt."),
            ("Dem Browser die Kamera-Berechtigung geben", "Erscheint SplitCam nicht in JFFs Kameraliste, stell sicher, dass SplitCam zuerst läuft und der Browser die Kamera-Berechtigung hat — dann den Broadcaster neu laden."),
            _T_TEST,
        ],
        "faq": [
            ("Wie verbindet sich SplitCam mit JustForFans?", "Der JFF-Live-Modus ist browserbasiert, SplitCam verbindet sich also als virtuelle Kamera: im Kamera-Auswahlmenü des JFF-Broadcasters SplitCam wählen. Kein Stream-Key nötig."),
            ("Kann ich Overlays und mehrere Kameras auf JFF nutzen?", "Ja — bau die Szene in SplitCam (zweite Kamera, Overlays, Beauty- oder KI-Hintergrund-Filter), und JFF sieht die fertige Szene als eine einzige Webcam."),
            ("Unterstützt JustForFans OBS oder externe Encoder?", "Der JFF-Live-Modus ist primär browser-/webcam-basiert. Zeigt dein Creator-Dashboard eine External-Encoder- oder Stream-Key-Option, fügst du sie in die Custom-RTMP-Felder von SplitCam ein; sonst die Virtual-Camera-Methode nutzen."),
            ("Ist SplitCam kostenlos für JustForFans?", "Ja — SplitCam ist kostenlos, ohne Wasserzeichen und ohne Zeitlimit."),
        ],
        "steps": [
            ("SplitCam herunterladen und installieren", "SplitCam ist kostenlose Live-Streaming-Software für Windows und macOS — ohne Registrierung, ohne Kreditkarte, ohne Wasserzeichen. Es installiert eine virtuelle Kamera, die der Browser auswählen kann."),
            ("Szene aufbauen", "SplitCam öffnen und die Webcam hinzufügen. Overlays, Text, eine zweite Kamera oder das Smartphone, Beauty-Filter oder einen KI-Hintergrund einbauen — alles live."),
            ("Live-Broadcast auf JFF starten", "In deinen JustForFans-Creator-Account einloggen und den Live-Broadcaster öffnen, um einen Stream für deine Abonnenten zu starten."),
            ("SplitCam als Kamera wählen", "Im Kamera-Dropdown des JFF-Broadcasters <strong>SplitCam</strong> statt deiner rohen Webcam wählen — deine komponierte Szene ersetzt die flache Kamera. (Oder, falls verfügbar, JFFs External-Encoder-Key in die Custom-RTMP-Felder von SplitCam einfügen.)"),
            ("Go Live drücken", "Den Broadcast starten — deine SplitCam-Szene, Overlays und Filter erreichen deine JustForFans-Abonnenten."),
        ],
    },
    {
        "slug": "fanvue", "name": "Fanvue",
        "title": "Auf Fanvue live gehen mit SplitCam — virtuelle Kamera",
        "desc": "Auf Fanvue live gehen mit kostenlosem SplitCam als virtuelle Kamera — Multi-Cam-Szenen, Overlays und Filter für deine Abonnenten. Ohne Wasserzeichen.",
        "kw": "auf fanvue live gehen, fanvue, fanvue live, fanvue stream, fanvue virtuelle kamera, fanvue virtual camera, fanvue obs, fanvue creator",
        "h1html": 'So gehst du auf <span class="accent">Fanvue</span> live mit SplitCam',
        "h1short": "Auf Fanvue live gehen",
        "card": "SplitCam als virtuelle Kamera im Live-Modus von Fanvue nutzen.",
        "intro": "Fanvue ist eine schnell wachsende britische Creator-Abo-Plattform — eine OnlyFans-Alternative, die als creator- und KI-freundlich gilt, mit Abos, Pay-per-View und Live-Streaming. Der Live-Broadcaster läuft im Browser; richtest du ihn auf kostenloses <strong style='color:var(--text)'>SplitCam</strong> als <strong>virtuelle Kamera</strong>, schaltest du Multi-Cam-Szenen, Overlays und Filter frei. Bietet dein Creator-Dashboard eine External-Encoder- / Stream-Key-Option, verbindet sich SplitCam stattdessen über RTMP.",
        "quick": "Auf Fanvue mit SplitCam live: SplitCam installieren, Szene bauen, auf Fanvue einen Live-Broadcast starten und im Kamera-Auswahlmenü des Broadcasters <em>SplitCam</em> wählen — dann live gehen."
                 "<ol><li>SplitCam installieren.</li><li>Kamera + Szene hinzufügen.</li>"
                 "<li>Live-Broadcast auf Fanvue starten.</li>"
                 "<li>SplitCam im Kamera-Dropdown wählen.</li><li>Go Live drücken.</li></ol>",
        "key_how": "Der Live-Modus von Fanvue läuft im Browser. Baue deine Szene in SplitCam — es registriert sich als Webcam namens <strong>«SplitCam Video Driver»</strong> — öffne dann den Fanvue-Live-Broadcaster und wähle im Kamera-Dropdown <strong>SplitCam</strong> statt deiner rohen Webcam. Bietet dein Creator-Dashboard eine <strong>External-Encoder- / Stream-Key</strong>-Option, fügst du diesen Key stattdessen in die Custom-RTMP-Felder von SplitCam ein.",
        "tips": [
            ("Virtuelle Kamera funktioniert überall", "Auch wenn der Live-Modus einer Plattform nur im Browser läuft, erscheint SplitCam als auswählbare Webcam — Multi-Cam-Szenen, Overlays und Filter funktionieren auf Fanvue ganz ohne Stream-Key."),
            ("Creator- und KI-freundlich", "Fanvue heißt KI-Creator willkommen und zahlt sauber aus. Overlays, die dein Abo oder PPV bewerben, wandeln gut bei einem Publikum, das ohnehin schon zahlt."),
            ("Dem Browser die Kamera-Berechtigung geben", "Erscheint SplitCam nicht in Fanvues Kameraliste, stell sicher, dass SplitCam zuerst läuft und der Browser die Kamera-Berechtigung hat — dann neu laden."),
            _T_TEST,
        ],
        "faq": [
            ("Wie verbindet sich SplitCam mit Fanvue?", "Der Fanvue-Live-Modus ist browserbasiert, SplitCam verbindet sich also als virtuelle Kamera: im Kamera-Auswahlmenü SplitCam wählen. Kein Stream-Key nötig."),
            ("Kann ich Overlays und mehrere Kameras auf Fanvue nutzen?", "Ja — bau die Szene in SplitCam (zweite Kamera, Overlays, Beauty- oder KI-Hintergrund-Filter), und Fanvue sieht die fertige Szene als eine einzige Webcam."),
            ("Unterstützt Fanvue OBS oder externe Encoder?", "Der Fanvue-Live-Modus ist primär browser-/webcam-basiert. Zeigt dein Dashboard eine External-Encoder- oder Stream-Key-Option, fügst du sie in die Custom-RTMP-Felder von SplitCam ein; sonst die Virtual-Camera-Methode nutzen."),
            ("Ist SplitCam kostenlos für Fanvue?", "Ja — SplitCam ist kostenlos, ohne Wasserzeichen und ohne Zeitlimit."),
        ],
        "steps": [
            ("SplitCam herunterladen und installieren", "SplitCam ist kostenlose Live-Streaming-Software für Windows und macOS — ohne Registrierung, ohne Kreditkarte, ohne Wasserzeichen. Es installiert eine virtuelle Kamera, die der Browser auswählen kann."),
            ("Szene aufbauen", "SplitCam öffnen und die Webcam hinzufügen. Overlays, Text, eine zweite Kamera oder das Smartphone, Beauty-Filter oder einen KI-Hintergrund einbauen — alles live."),
            ("Live-Broadcast auf Fanvue starten", "In deinen Fanvue-Creator-Account einloggen und den Live-Broadcaster öffnen, um einen Stream für deine Abonnenten zu starten."),
            ("SplitCam als Kamera wählen", "Im Kamera-Dropdown von Fanvue <strong>SplitCam</strong> statt deiner rohen Webcam wählen — deine komponierte Szene ersetzt die flache Kamera. (Oder, falls verfügbar, einen Stream-Key in die Custom-RTMP-Felder von SplitCam einfügen.)"),
            ("Go Live drücken", "Den Broadcast starten — deine SplitCam-Szene, Overlays und Filter erreichen deine Fanvue-Abonnenten."),
        ],
    },
    {
        "slug": "loyalfans", "name": "LoyalFans",
        "title": "Auf LoyalFans live gehen mit SplitCam — virtuelle Kamera",
        "desc": "Auf LoyalFans live gehen mit kostenlosem SplitCam als virtuelle Kamera — Multi-Cam-Szenen, Overlays und Filter für Abonnenten. Ohne Wasserzeichen.",
        "kw": "auf loyalfans live gehen, loyalfans, loyalfans live, loyalfans stream, loyalfans virtuelle kamera, loyalfans virtual camera, loyalfans obs, loyal fans",
        "h1html": 'So gehst du auf <span class="accent">LoyalFans</span> live mit SplitCam',
        "h1short": "Auf LoyalFans live gehen",
        "card": "SplitCam als virtuelle Kamera im Live-Modus von LoyalFans nutzen.",
        "intro": "LoyalFans ist eine Creator-Abo-Plattform mit Abos, Pay-per-View, Trinkgeldern und einem eingebauten <strong>Live-Cam</strong>-Feature. Der Live-Broadcaster läuft im Browser; verbindest du kostenloses <strong style='color:var(--text)'>SplitCam</strong> als <strong>virtuelle Kamera</strong>, kommen Multi-Cam-Szenen, Overlays und Filter über die Standard-Webcam dazu. Bietet dein Dashboard eine External-Encoder- / Stream-Key-Option, verbindet sich SplitCam stattdessen über RTMP.",
        "quick": "Auf LoyalFans mit SplitCam live: SplitCam installieren, Szene bauen, auf LoyalFans einen Live-Broadcast starten und im Kamera-Auswahlmenü des Broadcasters <em>SplitCam</em> wählen — dann live gehen."
                 "<ol><li>SplitCam installieren.</li><li>Kamera + Szene hinzufügen.</li>"
                 "<li>Live-Broadcast auf LoyalFans starten.</li>"
                 "<li>SplitCam im Kamera-Dropdown wählen.</li><li>Go Live drücken.</li></ol>",
        "key_how": "Der Live-Modus von LoyalFans läuft im Browser. Baue deine Szene in SplitCam — es registriert sich als Webcam namens <strong>«SplitCam Video Driver»</strong> — öffne dann den LoyalFans-Live-Broadcaster und wähle im Kamera-Dropdown <strong>SplitCam</strong>. Erscheint in deinem Creator-Dashboard eine <strong>Stream-Key- / External-Encoder</strong>-Option, fügst du sie stattdessen in die Custom-RTMP-Felder von SplitCam ein.",
        "tips": [
            ("Virtuelle Kamera, kein Key nötig", "Auch browserbasierter Live-Modus bekommt deine volle SplitCam-Szene — Overlays, zweite Kamera und Filter — einfach dadurch, dass du SplitCam als Webcam wählst."),
            ("Trinkgelder belohnen Produktion", "LoyalFans setzt stark auf Trinkgelder; eingeblendete Tip-Goal-Overlays und eine polierte Szene treiben Tipper mehr an als eine flache Webcam."),
            ("Dem Browser die Kamera-Berechtigung geben", "Steht SplitCam nicht in LoyalFans' Kameraliste, SplitCam zuerst starten, im Browser den Kamerazugriff erlauben, dann den Broadcaster neu laden."),
            _T_TEST,
        ],
        "faq": [
            ("Wie verbindet sich SplitCam mit LoyalFans?", "Der LoyalFans-Live-Modus ist browserbasiert, SplitCam verbindet sich also als virtuelle Kamera — im Kamera-Auswahlmenü SplitCam wählen. Kein Stream-Key nötig."),
            ("Kann ich Overlays und mehrere Kameras auf LoyalFans nutzen?", "Ja — komponiere die Szene in SplitCam (zweite Kamera, Overlays, Beauty- oder KI-Hintergrund-Filter); LoyalFans sieht sie als eine Webcam."),
            ("Unterstützt LoyalFans OBS oder externe Encoder?", "Der Live-Modus ist primär browser-/webcam-basiert. Zeigt dein Dashboard eine Stream-Key-Option, fügst du sie in die Custom-RTMP-Felder von SplitCam ein; sonst die Virtual-Camera-Methode nutzen."),
            ("Ist SplitCam kostenlos für LoyalFans?", "Ja — kostenlos, ohne Wasserzeichen und ohne Zeitlimit."),
        ],
        "steps": [
            ("SplitCam herunterladen und installieren", "SplitCam ist kostenlose Live-Streaming-Software für Windows und macOS — ohne Registrierung, ohne Kreditkarte, ohne Wasserzeichen. Es installiert eine virtuelle Kamera, die der Browser auswählen kann."),
            ("Szene aufbauen", "SplitCam öffnen und die Webcam hinzufügen. Overlays, Tip-Goal-Text, eine zweite Kamera oder das Smartphone, Beauty-Filter oder einen KI-Hintergrund einbauen."),
            ("Live-Broadcast auf LoyalFans starten", "In deinen LoyalFans-Account einloggen und den Live-Broadcaster öffnen, um für deine Abonnenten live zu gehen."),
            ("SplitCam als Kamera wählen", "Im Kamera-Dropdown von LoyalFans <strong>SplitCam</strong> statt deiner rohen Webcam wählen — deine Szene ersetzt die flache Kamera. (Oder, falls verfügbar, einen Stream-Key in die Custom-RTMP-Felder von SplitCam einfügen.)"),
            ("Go Live drücken", "Den Broadcast starten — deine SplitCam-Szene erreicht dein LoyalFans-Publikum."),
        ],
    },
    {
        "slug": "fancentro", "name": "FanCentro",
        "title": "Auf FanCentro live gehen mit SplitCam — virtuelle Kamera",
        "desc": "Auf FanCentro live gehen mit kostenlosem SplitCam als virtuelle Kamera — Multi-Cam-Szenen, Overlays und Filter für deine Abonnenten. Ohne Wasserzeichen.",
        "kw": "auf fancentro live gehen, fancentro, fancentro live, fancentro stream, fancentro virtuelle kamera, fancentro virtual camera, fancentro obs, fan centro",
        "h1html": 'So gehst du auf <span class="accent">FanCentro</span> live mit SplitCam',
        "h1short": "Auf FanCentro live gehen",
        "card": "SplitCam als virtuelle Kamera im Live-Modus von FanCentro nutzen.",
        "intro": "FanCentro ist eine langjährige Creator-Monetarisierungs-Plattform — Abos, Pay-per-View-Nachrichten, Content und Live-Streaming. Der Live-Modus läuft im Browser; verbindest du kostenloses <strong style='color:var(--text)'>SplitCam</strong> als <strong>virtuelle Kamera</strong>, kommen Multi-Cam-Szenen, Overlays und Filter über die schlichte Webcam hinaus dazu. Bietet dein Dashboard eine External-Encoder- / Stream-Key-Option, verbindet sich SplitCam stattdessen über RTMP.",
        "quick": "Auf FanCentro mit SplitCam live: SplitCam installieren, Szene bauen, auf FanCentro einen Live-Broadcast starten und im Kamera-Auswahlmenü des Broadcasters <em>SplitCam</em> wählen — dann live gehen."
                 "<ol><li>SplitCam installieren.</li><li>Kamera + Szene hinzufügen.</li>"
                 "<li>Live-Broadcast auf FanCentro starten.</li>"
                 "<li>SplitCam im Kamera-Dropdown wählen.</li><li>Go Live drücken.</li></ol>",
        "key_how": "Der Live-Modus von FanCentro läuft im Browser. Baue deine Szene in SplitCam — es registriert sich als Webcam namens <strong>«SplitCam Video Driver»</strong> — öffne dann den FanCentro-Live-Broadcaster und wähle im Kamera-Dropdown <strong>SplitCam</strong>. Wird eine <strong>Stream-Key- / External-Encoder</strong>-Option angeboten, fügst du sie stattdessen in die Custom-RTMP-Felder von SplitCam ein.",
        "tips": [
            ("Virtuelle Kamera funktioniert überall", "Auch ein reiner Browser-Live-Modus bekommt deine volle SplitCam-Szene — Overlays, zweite Kamera und Filter — indem du SplitCam als Webcam wählst."),
            ("Cross-Sell deines Funnels", "FanCentro ist rund um Creator-Funnels und PPV gebaut. Overlays, die dein Abo oder bezahlte Nachrichten bewerben, machen aus Live-Zuschauern Käufer."),
            ("Dem Browser die Kamera-Berechtigung geben", "Wird SplitCam nicht gelistet, SplitCam zuerst starten, im Browser den Kamerazugriff erlauben, dann den Broadcaster neu laden."),
            _T_TEST,
        ],
        "faq": [
            ("Wie verbindet sich SplitCam mit FanCentro?", "Der FanCentro-Live-Modus ist browserbasiert, SplitCam verbindet sich also als virtuelle Kamera — im Kamera-Auswahlmenü SplitCam wählen. Kein Stream-Key nötig."),
            ("Kann ich Overlays und mehrere Kameras auf FanCentro nutzen?", "Ja — bau die Szene in SplitCam; FanCentro sieht die fertige Szene als eine einzige Webcam."),
            ("Unterstützt FanCentro OBS oder externe Encoder?", "Der Live-Modus ist primär browser-/webcam-basiert. Erscheint in deinem Dashboard eine Stream-Key-Option, fügst du sie in die Custom-RTMP-Felder von SplitCam ein; sonst die Virtual-Camera-Methode nutzen."),
            ("Ist SplitCam kostenlos für FanCentro?", "Ja — kostenlos, ohne Wasserzeichen und ohne Zeitlimit."),
        ],
        "steps": [
            ("SplitCam herunterladen und installieren", "SplitCam ist kostenlose Live-Streaming-Software für Windows und macOS — ohne Registrierung, ohne Kreditkarte, ohne Wasserzeichen. Es installiert eine virtuelle Kamera, die der Browser auswählen kann."),
            ("Szene aufbauen", "SplitCam öffnen und die Webcam hinzufügen. Overlays, Text, eine zweite Kamera oder das Smartphone, Beauty-Filter oder einen KI-Hintergrund einbauen."),
            ("Live-Broadcast auf FanCentro starten", "In deinen FanCentro-Account einloggen und den Live-Broadcaster öffnen, um für deine Abonnenten live zu gehen."),
            ("SplitCam als Kamera wählen", "Im Kamera-Dropdown von FanCentro <strong>SplitCam</strong> statt deiner rohen Webcam wählen. (Oder, falls verfügbar, einen Stream-Key in die Custom-RTMP-Felder von SplitCam einfügen.)"),
            ("Go Live drücken", "Den Broadcast starten — deine SplitCam-Szene erreicht deine FanCentro-Abonnenten."),
        ],
    },
    {
        "slug": "ismygirl", "name": "IsMyGirl",
        "title": "Auf IsMyGirl live gehen mit SplitCam — virtuelle Kamera",
        "desc": "Auf IsMyGirl live gehen mit kostenlosem SplitCam als virtuelle Kamera — Multi-Cam-Szenen, Overlays und Filter für deine Abonnenten. Ohne Wasserzeichen.",
        "kw": "auf ismygirl live gehen, ismygirl, ismygirl live, ismygirl stream, ismygirl virtuelle kamera, ismygirl virtual camera, ismygirl obs, is my girl",
        "h1html": 'So gehst du auf <span class="accent">IsMyGirl</span> live mit SplitCam',
        "h1short": "Auf IsMyGirl live gehen",
        "card": "SplitCam als virtuelle Kamera im Live-Modus von IsMyGirl nutzen.",
        "intro": "IsMyGirl ist eine Creator-Abo-Plattform — eine OnlyFans-Alternative mit Abos, bezahltem Content und Live-Streaming, bekannt für engen Creator-Support. Der Live-Broadcaster läuft im Browser; verbindest du kostenloses <strong style='color:var(--text)'>SplitCam</strong> als <strong>virtuelle Kamera</strong>, kommen Multi-Cam-Szenen, Overlays und Filter dazu. Bietet dein Dashboard eine External-Encoder- / Stream-Key-Option, verbindet sich SplitCam stattdessen über RTMP.",
        "quick": "Auf IsMyGirl mit SplitCam live: SplitCam installieren, Szene bauen, auf IsMyGirl einen Live-Broadcast starten und im Kamera-Auswahlmenü des Broadcasters <em>SplitCam</em> wählen — dann live gehen."
                 "<ol><li>SplitCam installieren.</li><li>Kamera + Szene hinzufügen.</li>"
                 "<li>Live-Broadcast auf IsMyGirl starten.</li>"
                 "<li>SplitCam im Kamera-Dropdown wählen.</li><li>Go Live drücken.</li></ol>",
        "key_how": "Der Live-Modus von IsMyGirl läuft im Browser. Baue deine Szene in SplitCam — es registriert sich als Webcam namens <strong>«SplitCam Video Driver»</strong> — öffne dann den IsMyGirl-Live-Broadcaster und wähle im Kamera-Dropdown <strong>SplitCam</strong>. Erscheint eine <strong>Stream-Key- / External-Encoder</strong>-Option, fügst du sie stattdessen in die Custom-RTMP-Felder von SplitCam ein.",
        "tips": [
            ("Virtuelle Kamera, kein Key nötig", "Auch ein reiner Browser-Live-Modus bekommt deine volle SplitCam-Szene — Overlays, zweite Kamera und Filter — indem du SplitCam als Webcam wählst."),
            ("Den Creator-Support nutzen", "IsMyGirl wirbt mit starkem Creator-Support und Promotion. Eine polierte SplitCam-Szene plus Cross-Sell-Overlays holen das Maximum aus dem Traffic, den sie dir schicken."),
            ("Dem Browser die Kamera-Berechtigung geben", "Wird SplitCam nicht gelistet, SplitCam zuerst starten, den Kamerazugriff erlauben, dann den Broadcaster neu laden."),
            _T_TEST,
        ],
        "faq": [
            ("Wie verbindet sich SplitCam mit IsMyGirl?", "Der IsMyGirl-Live-Modus ist browserbasiert, SplitCam verbindet sich also als virtuelle Kamera — im Kamera-Auswahlmenü SplitCam wählen. Kein Stream-Key nötig."),
            ("Kann ich Overlays und mehrere Kameras auf IsMyGirl nutzen?", "Ja — komponiere die Szene in SplitCam; IsMyGirl sieht sie als eine Webcam."),
            ("Unterstützt IsMyGirl OBS oder externe Encoder?", "Der Live-Modus ist primär browser-/webcam-basiert. Erscheint eine Stream-Key-Option, fügst du sie in die Custom-RTMP-Felder von SplitCam ein; sonst die Virtual-Camera-Methode nutzen."),
            ("Ist SplitCam kostenlos für IsMyGirl?", "Ja — kostenlos, ohne Wasserzeichen und ohne Zeitlimit."),
        ],
        "steps": [
            ("SplitCam herunterladen und installieren", "SplitCam ist kostenlose Live-Streaming-Software für Windows und macOS — ohne Registrierung, ohne Kreditkarte, ohne Wasserzeichen. Es installiert eine virtuelle Kamera, die der Browser auswählen kann."),
            ("Szene aufbauen", "SplitCam öffnen und die Webcam hinzufügen. Overlays, Text, eine zweite Kamera oder das Smartphone, Beauty-Filter oder einen KI-Hintergrund einbauen."),
            ("Live-Broadcast auf IsMyGirl starten", "In deinen IsMyGirl-Account einloggen und den Live-Broadcaster öffnen, um für deine Abonnenten live zu gehen."),
            ("SplitCam als Kamera wählen", "Im Kamera-Dropdown von IsMyGirl <strong>SplitCam</strong> statt deiner rohen Webcam wählen. (Oder, falls verfügbar, einen Stream-Key in die Custom-RTMP-Felder von SplitCam einfügen.)"),
            ("Go Live drücken", "Den Broadcast starten — deine SplitCam-Szene erreicht deine IsMyGirl-Abonnenten."),
        ],
    },
    {
        "slug": "dxlive", "name": "DXLive",
        "title": "Auf DXLive senden mit SplitCam — External Encoder",
        "desc": "Auf DXLive senden mit kostenlosem SplitCam — External Encoder für das japanische Premium-Cam-Netzwerk, Multi-Cam-Szenen und Overlays. Ohne Wasserzeichen.",
        "kw": "auf dxlive senden, dxlive, dxlive broadcast, dxlive obs, dxlive external encoder, dxlive rtmp, dxlive performer",
        "h1html": 'So sendest du auf <span class="accent">DXLive</span> mit SplitCam',
        "h1short": "Auf DXLive senden",
        "card": "External-Encoder-Setup für das Premium-Cam-Netzwerk DXLive.",
        "intro": "DXLive ist ein etabliertes Premium-Webcam-Netzwerk, beliebt in Japan und ganz Asien, mit einem Pay-per-Minute-Modell und treuem Publikum. Der Performer-Bereich unterstützt einen Standard-<strong>External Encoder</strong>-Pfad, an den sich kostenloses <strong style='color:var(--text)'>SplitCam</strong> anschließt — damit du mit Multi-Cam-Szenen, Overlays und Beauty-Filtern sendest statt mit einer einzigen flachen Webcam.",
        "quick": "Auf DXLive mit SplitCam senden: SplitCam installieren, Szene bauen, im Performer-Bereich die <em>External-Encoder- / Broadcast</em>-Einstellungen öffnen, Server-URL und Stream Key kopieren, in SplitCam einfügen, Go Live."
                 "<ol><li>SplitCam installieren.</li><li>Kamera + Szene hinzufügen.</li><li>URL + Stream Key aus dem Performer-Bereich holen.</li><li>In SplitCam einfügen.</li><li>Go Live drücken.</li></ol>",
        "key_how": "Im DXLive-Performer-Account anmelden und im Performer-Bereich die <strong>Broadcast- / External-Encoder</strong>-Einstellungen öffnen. Die Seite zeigt eine an den Account gebundene <strong>Server-URL</strong> und einen <strong>Stream Key</strong> — beides in die Custom-RTMP-Felder von SplitCam kopieren. Die DXLive-Verifizierung ist Pflicht, bevor das Live-Cam-Feature freigeschaltet wird.",
        "tips": [
            ("Gebaut für den asiatischen Markt", "DXLives Publikum kommt überwiegend aus Japan/Asien und zahlt pro Minute. Legst du deine Shows auf die Abendstunden in JST, wandelt die treue, zahlende Basis gut."),
            ("Politur schlägt rohe Webcam", "Eine saubere SplitCam-Szene mit Overlays und Beauty-Filtern hebt sich in einem Premium-Pay-per-Minute-Netzwerk ab, wo Zuschauer Qualität erwarten."),
            ("External Encoder statt nur Webcam nutzen", "Der Weg über SplitCams RTMP statt der einfachen Browser-Cam schaltet Multi-Cam-Szenen und Filter erst frei."),
            _T_ETH,
        ],
        "faq": [
            ("Unterstützt DXLive externe Encoder wie SplitCam?", "Ja — der Performer-Bereich bietet einen Standard-External-Encoder- / RTMP-Pfad. Server-URL und Stream Key nach der Verifizierung in SplitCam kopieren."),
            ("Wo bekomme ich meinen DXLive-Stream-Key?", "In den Broadcast- / External-Encoder-Einstellungen im Performer-Bereich — Server-URL und Stream Key erscheinen dort. Beides in die Custom-RTMP-Felder von SplitCam einfügen."),
            ("Welche Bitrate für DXLive?", "Anpeilen: 1920×1080 bei 30 fps, 3.500–6.000 Kbps und 2 Sekunden Keyframe-Intervall. Vorher den eingebauten Speedtest von SplitCam laufen lassen."),
            ("Ist SplitCam bei DXLive kostenlos nutzbar?", "Ja — SplitCam ist kostenlos, ohne Wasserzeichen und ohne Zeitlimit. Die External-Encoder-Option von DXLive ist im Performer-Bereich kostenlos."),
        ],
        "steps": [
            ("SplitCam herunterladen und installieren", "SplitCam ist kostenlose Live-Streaming-Software für Windows und macOS — ohne Registrierung, ohne Kreditkarte, ohne Wasserzeichen."),
            ("Szene aufbauen", "SplitCam öffnen und die Webcam hinzufügen. Overlays, Text, eine zweite Kamera oder das Smartphone, Beauty-Filter oder einen KI-Hintergrund einbauen."),
            ("DXLive-URL und Stream-Key holen", "Im DXLive-Performer-Account anmelden und die <strong>Broadcast- / External-Encoder</strong>-Einstellungen öffnen. <strong>Server-URL</strong> und <strong>Stream Key</strong> kopieren."),
            ("SplitCam mit DXLive verbinden", "In SplitCam <strong>Stream Settings</strong> öffnen, die DXLive-Server-URL und den Stream Key in die Custom-RTMP-Felder einfügen. 3.500–6.000 Kbps bei 1920×1080, 30 fps und 2 Sekunden Keyframe einstellen."),
            ("Go Live drücken", "In SplitCam auf <strong>Go Live</strong> klicken, dann aus dem Performer-Bereich online gehen. Innerhalb von ~10 Sekunden erreicht dein Stream DXLives Publikum."),
        ],
    },
    {
        "slug": "streamen", "name": "Streamen",
        "title": "Auf Streamen senden mit SplitCam — External Encoder",
        "desc": "Auf Streamen senden mit kostenlosem SplitCam — External-Encoder-Setup, Multi-Cam-Szenen, Overlays und Beauty-Filter. Ohne Wasserzeichen.",
        "kw": "auf streamen senden, streamen broadcast, streamen cam, streamen obs, streamen external encoder, streamen rtmp, streamen.tv",
        "h1html": 'So sendest du auf <span class="accent">Streamen</span> mit SplitCam',
        "h1short": "Auf Streamen senden",
        "card": "External-Encoder-Setup für die Cam-Plattform Streamen.",
        "intro": "Streamen ist eine Live-Cam-Plattform, auf der Models an ein trinkgeld-getriebenes Publikum senden. Die Broadcast-Einstellungen bieten einen Standard-<strong>External Encoder</strong>-Pfad, an den sich kostenloses <strong style='color:var(--text)'>SplitCam</strong> anschließt — damit du mit Multi-Cam-Szenen, Overlays und Filtern streamst statt mit einer einzigen schlichten Webcam.",
        "quick": "Auf Streamen mit SplitCam senden: SplitCam installieren, Szene bauen, im Model-Dashboard <em>Broadcast Settings → External Encoder</em> öffnen, Server-URL und Stream Key kopieren, in SplitCam einfügen, Go Live."
                 "<ol><li>SplitCam installieren.</li><li>Kamera + Szene hinzufügen.</li><li>URL + Stream Key aus dem Dashboard holen.</li><li>In SplitCam einfügen.</li><li>Go Live drücken.</li></ol>",
        "key_how": "Im Streamen-Model-Account anmelden und den Bereich <strong>Broadcast Settings / External Encoder</strong> öffnen. Er zeigt eine an den Account gebundene <strong>Server-URL</strong> und einen <strong>Stream Key</strong> — beides in die Custom-RTMP-Felder von SplitCam kopieren. Die Model-Verifizierung ist Pflicht, bevor das Senden freigeschaltet wird.",
        "tips": [
            ("Trinkgeld-getriebenes Publikum", "Streamen-Zuschauer geben Trinkgeld — eingeblendete Tip-Goals und eine polierte Szene treiben mehr Trinkgeld als eine flache Webcam."),
            ("External Encoder schaltet Szenen frei", "Der Weg über SplitCams RTMP statt der einfachen Browser-Cam ermöglicht Multi-Cam-Layouts, Overlays und Filter."),
            ("Auflösung festlegen", "1080p von Hand setzen, damit der Feed nicht heimlich die Qualität drosselt; dass die Bitrate bei einem ruhigen Bild absackt, ist bei adaptiven Feeds normal."),
            _T_ETH,
        ],
        "faq": [
            ("Unterstützt Streamen externe Encoder wie SplitCam?", "Ja — die Broadcast-Einstellungen bieten einen Standard-External-Encoder- / RTMP-Pfad. Server-URL und Stream Key nach der Verifizierung in SplitCam kopieren."),
            ("Wo bekomme ich meinen Streamen-Stream-Key?", "In den Broadcast- / External-Encoder-Einstellungen deines Model-Dashboards — Server-URL und Stream Key erscheinen dort. Beides in die Custom-RTMP-Felder von SplitCam einfügen."),
            ("Welche Bitrate für Streamen?", "Anpeilen: 1920×1080 bei 30 fps, 3.500–6.000 Kbps und 2 Sekunden Keyframe-Intervall. Vorher den SplitCam-Speedtest laufen lassen."),
            ("Ist SplitCam bei Streamen kostenlos nutzbar?", "Ja — SplitCam ist kostenlos, ohne Wasserzeichen und ohne Zeitlimit. Die External-Encoder-Option von Streamen ist im Dashboard kostenlos."),
        ],
        "steps": [
            ("SplitCam herunterladen und installieren", "SplitCam ist kostenlose Live-Streaming-Software für Windows und macOS — ohne Registrierung, ohne Kreditkarte, ohne Wasserzeichen."),
            ("Szene aufbauen", "SplitCam öffnen und die Webcam hinzufügen. Overlays, Tip-Goal-Text, eine zweite Kamera oder das Smartphone, Beauty-Filter oder einen KI-Hintergrund einbauen."),
            ("Streamen-URL und Stream-Key holen", "Im Streamen-Model-Account anmelden, <strong>Broadcast Settings → External Encoder</strong> öffnen und <strong>Server-URL</strong> und <strong>Stream Key</strong> kopieren."),
            ("SplitCam mit Streamen verbinden", "In SplitCam <strong>Stream Settings</strong> öffnen, die Streamen-Server-URL und den Stream Key in die Custom-RTMP-Felder einfügen. 3.500–6.000 Kbps bei 1920×1080, 30 fps und 2 Sekunden Keyframe einstellen."),
            ("Go Live drücken", "In SplitCam auf <strong>Go Live</strong> klicken, dann aus deinem Dashboard online gehen. Innerhalb von ~10 Sekunden erreicht dein Stream Streamens Publikum."),
        ],
    },
    {
        "slug": "xcams", "name": "XCams",
        "title": "Auf XCams senden mit SplitCam — External Encoder",
        "desc": "Auf XCams senden mit kostenlosem SplitCam — External Encoder für die europäische Cam-Community, Multi-Cam-Szenen, Overlays und Filter. Ohne Wasserzeichen.",
        "kw": "auf xcams senden, xcams, xcams broadcast, xcams obs, xcams external encoder, xcams rtmp, x cams",
        "h1html": 'So sendest du auf <span class="accent">XCams</span> mit SplitCam',
        "h1short": "Auf XCams senden",
        "card": "External-Encoder-Setup für die europäische XCams-Community.",
        "intro": "XCams ist eine europäische Live-Cam-Community — stark in Italien, Frankreich und Spanien — aufgebaut rund um Live-Shows und eine Trinkgeld-/Privatshow-Ökonomie. Der Model-Bereich unterstützt einen Standard-<strong>External Encoder</strong>-Pfad, an den sich kostenloses <strong style='color:var(--text)'>SplitCam</strong> anschließt — damit du mit Multi-Cam-Szenen, Overlays und Beauty-Filtern sendest.",
        "quick": "Auf XCams mit SplitCam senden: SplitCam installieren, Szene bauen, im Model-Bereich <em>Broadcast / External Encoder</em> öffnen, Server-URL und Stream Key kopieren, in SplitCam einfügen, Go Live."
                 "<ol><li>SplitCam installieren.</li><li>Kamera + Szene hinzufügen.</li><li>URL + Stream Key aus dem Model-Bereich holen.</li><li>In SplitCam einfügen.</li><li>Go Live drücken.</li></ol>",
        "key_how": "Im XCams-Model-Account anmelden und im Model-Bereich die <strong>Broadcast- / External-Encoder</strong>-Einstellungen öffnen. Die Seite zeigt eine an den Account gebundene <strong>Server-URL</strong> und einen <strong>Stream Key</strong> — beides in die Custom-RTMP-Felder von SplitCam kopieren. Die XCams-Verifizierung ist vor dem Senden Pflicht.",
        "tips": [
            ("Europäische Prime Time", "XCams-Traffic erreicht abends in der EU (MEZ) seinen Höhepunkt. In diesen Stunden zu senden übertrifft die Nebenzeiten in dieser Community deutlich."),
            ("Privatshows belohnen Qualität", "XCams lebt von Privat-/Spy-Shows — eine polierte SplitCam-Szene mit Overlays macht aus Stöberern bezahlte Privatshows."),
            ("External Encoder schaltet Szenen frei", "Der Weg über SplitCams RTMP statt der Browser-Cam ermöglicht Multi-Cam-Layouts, Overlays und Filter."),
            _T_ETH,
        ],
        "faq": [
            ("Unterstützt XCams externe Encoder wie SplitCam?", "Ja — der Model-Bereich bietet einen Standard-External-Encoder- / RTMP-Pfad. Server-URL und Stream Key nach der Verifizierung in SplitCam kopieren."),
            ("Wo bekomme ich meinen XCams-Stream-Key?", "In den Broadcast- / External-Encoder-Einstellungen im Model-Bereich — Server-URL und Stream Key erscheinen dort. Beides in die Custom-RTMP-Felder von SplitCam einfügen."),
            ("Welche Bitrate für XCams?", "Anpeilen: 1920×1080 bei 30 fps, 3.500–6.000 Kbps und 2 Sekunden Keyframe-Intervall. Vorher den SplitCam-Speedtest laufen lassen."),
            ("Ist SplitCam bei XCams kostenlos nutzbar?", "Ja — SplitCam ist kostenlos, ohne Wasserzeichen und ohne Zeitlimit. Die External-Encoder-Option von XCams ist im Model-Bereich kostenlos."),
        ],
        "steps": [
            ("SplitCam herunterladen und installieren", "SplitCam ist kostenlose Live-Streaming-Software für Windows und macOS — ohne Registrierung, ohne Kreditkarte, ohne Wasserzeichen."),
            ("Szene aufbauen", "SplitCam öffnen und die Webcam hinzufügen. Overlays, Text, eine zweite Kamera oder das Smartphone, Beauty-Filter oder einen KI-Hintergrund einbauen."),
            ("XCams-URL und Stream-Key holen", "Im XCams-Model-Account anmelden, <strong>Broadcast / External Encoder</strong> öffnen und <strong>Server-URL</strong> und <strong>Stream Key</strong> kopieren."),
            ("SplitCam mit XCams verbinden", "In SplitCam <strong>Stream Settings</strong> öffnen, die XCams-Server-URL und den Stream Key in die Custom-RTMP-Felder einfügen. 3.500–6.000 Kbps bei 1920×1080, 30 fps und 2 Sekunden Keyframe einstellen."),
            ("Go Live drücken", "In SplitCam auf <strong>Go Live</strong> klicken, dann aus dem Model-Bereich online gehen. Innerhalb von ~10 Sekunden erreicht dein Stream XCams' Publikum."),
        ],
    },
    {
        "slug": "camcontacts", "name": "CamContacts",
        "title": "Auf CamContacts senden mit SplitCam — External Encoder",
        "desc": "Auf CamContacts senden mit kostenlosem SplitCam — External Encoder für die Pay-per-Minute-Cam-Seite, Multi-Cam-Szenen und Overlays. Ohne Wasserzeichen.",
        "kw": "auf camcontacts senden, camcontacts, camcontacts broadcast, camcontacts obs, camcontacts external encoder, camcontacts rtmp, cam contacts",
        "h1html": 'So sendest du auf <span class="accent">CamContacts</span> mit SplitCam',
        "h1short": "Auf CamContacts senden",
        "card": "External-Encoder-Setup für die Pay-per-Minute-Cam von CamContacts.",
        "intro": "CamContacts ist eine der am längsten betriebenen unabhängigen Cam-Seiten — ein Pay-per-Minute-Modell mit einem gereiften, treuen Publikum und dem Ruf für verlässliche Auszahlungen. Der Performer-Bereich unterstützt einen Standard-<strong>External Encoder</strong>-Pfad, an den sich kostenloses <strong style='color:var(--text)'>SplitCam</strong> anschließt — damit du mit Multi-Cam-Szenen, Overlays und Beauty-Filtern sendest.",
        "quick": "Auf CamContacts mit SplitCam senden: SplitCam installieren, Szene bauen, im Performer-Bereich die <em>External-Encoder- / Broadcast</em>-Einstellungen öffnen, Server-URL und Stream Key kopieren, in SplitCam einfügen, Go Live."
                 "<ol><li>SplitCam installieren.</li><li>Kamera + Szene hinzufügen.</li><li>URL + Stream Key aus dem Performer-Bereich holen.</li><li>In SplitCam einfügen.</li><li>Go Live drücken.</li></ol>",
        "key_how": "Im CamContacts-Performer-Account anmelden und im Performer-Bereich die <strong>Broadcast- / External-Encoder</strong>-Einstellungen öffnen. Die Seite zeigt eine an den Account gebundene <strong>Server-URL</strong> und einen <strong>Stream Key</strong> — beides in die Custom-RTMP-Felder von SplitCam kopieren. Die CamContacts-Verifizierung ist für das Live-Cam-Feature Pflicht.",
        "tips": [
            ("Gereiftes, treues Publikum", "CamContacts läuft seit Jahrzehnten mit langjährigen Mitgliedern — stabilere, besser zahlende Stammgäste als eine churn-lastige Gratis-Seite, dafür langsameres Wachstum für Neulinge."),
            ("Pay-per-Minute belohnt Bindung", "Halte Zuschauer mit einer polierten Szene und Overlays in der bezahlten Zeit; Produktionswert verlängert Sessions im Minutenmodell."),
            ("External Encoder schaltet Szenen frei", "Der Weg über SplitCams RTMP statt der einfachen Cam ermöglicht Multi-Cam-Layouts, Overlays und Filter."),
            _T_ETH,
        ],
        "faq": [
            ("Unterstützt CamContacts externe Encoder wie SplitCam?", "Ja — der Performer-Bereich bietet einen Standard-External-Encoder- / RTMP-Pfad. Server-URL und Stream Key nach der Verifizierung in SplitCam kopieren."),
            ("Wo bekomme ich meinen CamContacts-Stream-Key?", "In den Broadcast- / External-Encoder-Einstellungen im Performer-Bereich — Server-URL und Stream Key erscheinen dort. Beides in die Custom-RTMP-Felder von SplitCam einfügen."),
            ("Welche Bitrate für CamContacts?", "Anpeilen: 1920×1080 bei 30 fps, 3.500–6.000 Kbps und 2 Sekunden Keyframe-Intervall. Vorher den SplitCam-Speedtest laufen lassen."),
            ("Ist SplitCam bei CamContacts kostenlos nutzbar?", "Ja — SplitCam ist kostenlos, ohne Wasserzeichen und ohne Zeitlimit. Die External-Encoder-Option von CamContacts ist im Performer-Bereich kostenlos."),
        ],
        "steps": [
            ("SplitCam herunterladen und installieren", "SplitCam ist kostenlose Live-Streaming-Software für Windows und macOS — ohne Registrierung, ohne Kreditkarte, ohne Wasserzeichen."),
            ("Szene aufbauen", "SplitCam öffnen und die Webcam hinzufügen. Overlays, Text, eine zweite Kamera oder das Smartphone, Beauty-Filter oder einen KI-Hintergrund einbauen."),
            ("CamContacts-URL und Stream-Key holen", "Im CamContacts-Performer-Account anmelden, die <strong>Broadcast- / External-Encoder</strong>-Einstellungen öffnen und <strong>Server-URL</strong> und <strong>Stream Key</strong> kopieren."),
            ("SplitCam mit CamContacts verbinden", "In SplitCam <strong>Stream Settings</strong> öffnen, die CamContacts-Server-URL und den Stream Key in die Custom-RTMP-Felder einfügen. 3.500–6.000 Kbps bei 1920×1080, 30 fps und 2 Sekunden Keyframe einstellen."),
            ("Go Live drücken", "In SplitCam auf <strong>Go Live</strong> klicken, dann aus dem Performer-Bereich online gehen. Innerhalb von ~10 Sekunden erreicht dein Stream CamContacts' Publikum."),
        ],
    },
    {
        "slug": "royalcams", "name": "RoyalCams",
        "title": "Auf RoyalCams senden mit SplitCam — External Encoder",
        "desc": "Auf RoyalCams senden mit kostenlosem SplitCam — External Encoder für die Token-Cam-Seite, Multi-Cam-Szenen, Overlays und Filter. Ohne Wasserzeichen.",
        "kw": "auf royalcams senden, royalcams, royalcams broadcast, royalcams obs, royalcams external encoder, royalcams rtmp, royal cams",
        "h1html": 'So sendest du auf <span class="accent">RoyalCams</span> mit SplitCam',
        "h1short": "Auf RoyalCams senden",
        "card": "External-Encoder-Setup für die Token-Cam-Seite RoyalCams.",
        "intro": "RoyalCams ist eine token-basierte Gratis-Cam-Seite — offene öffentliche Räume, finanziert durch Trinkgeld, mit Privatshows obendrauf. Die Broadcast-Einstellungen unterstützen einen Standard-<strong>External Encoder</strong>-Pfad, an den sich kostenloses <strong style='color:var(--text)'>SplitCam</strong> anschließt — damit du mit Multi-Cam-Szenen, Overlays und Beauty-Filtern streamst statt mit einer einzigen flachen Webcam.",
        "quick": "Auf RoyalCams mit SplitCam senden: SplitCam installieren, Szene bauen, im Model-Dashboard <em>Broadcast Settings → External Encoder</em> öffnen, Server-URL und Stream Key kopieren, in SplitCam einfügen, Go Live."
                 "<ol><li>SplitCam installieren.</li><li>Kamera + Szene hinzufügen.</li><li>URL + Stream Key aus dem Dashboard holen.</li><li>In SplitCam einfügen.</li><li>Go Live drücken.</li></ol>",
        "key_how": "Im RoyalCams-Model-Account anmelden und den Bereich <strong>Broadcast Settings / External Encoder</strong> öffnen. Er zeigt eine an den Account gebundene <strong>Server-URL</strong> und einen <strong>Stream Key</strong> — beides in die Custom-RTMP-Felder von SplitCam kopieren. Die Model-Verifizierung ist vor dem Senden Pflicht.",
        "tips": [
            ("Token-Räume belohnen Produktion", "RoyalCams' öffentliche Räume laufen über Trinkgeld — Tip-Goal-Overlays und eine polierte Szene machen aus Lurkern Tipper und Privatshows."),
            ("In Privatshows umwandeln", "Nutze eine starke öffentliche Szene, um Privatshows hochzuverkaufen — dort steckt der eigentliche Verdienst auf Token-Cam-Seiten."),
            ("External Encoder schaltet Szenen frei", "Der Weg über SplitCams RTMP statt der Browser-Cam ermöglicht Multi-Cam-Layouts, Overlays und Filter."),
            _T_ETH,
        ],
        "faq": [
            ("Unterstützt RoyalCams externe Encoder wie SplitCam?", "Ja — die Broadcast-Einstellungen bieten einen Standard-External-Encoder- / RTMP-Pfad. Server-URL und Stream Key nach der Verifizierung in SplitCam kopieren."),
            ("Wo bekomme ich meinen RoyalCams-Stream-Key?", "In den Broadcast- / External-Encoder-Einstellungen deines Model-Dashboards — Server-URL und Stream Key erscheinen dort. Beides in die Custom-RTMP-Felder von SplitCam einfügen."),
            ("Welche Bitrate für RoyalCams?", "Anpeilen: 1920×1080 bei 30 fps, 3.500–6.000 Kbps und 2 Sekunden Keyframe-Intervall. Vorher den SplitCam-Speedtest laufen lassen."),
            ("Ist SplitCam bei RoyalCams kostenlos nutzbar?", "Ja — SplitCam ist kostenlos, ohne Wasserzeichen und ohne Zeitlimit. Die External-Encoder-Option von RoyalCams ist im Dashboard kostenlos."),
        ],
        "steps": [
            ("SplitCam herunterladen und installieren", "SplitCam ist kostenlose Live-Streaming-Software für Windows und macOS — ohne Registrierung, ohne Kreditkarte, ohne Wasserzeichen."),
            ("Szene aufbauen", "SplitCam öffnen und die Webcam hinzufügen. Overlays, Tip-Goal-Text, eine zweite Kamera oder das Smartphone, Beauty-Filter oder einen KI-Hintergrund einbauen."),
            ("RoyalCams-URL und Stream-Key holen", "Im RoyalCams-Model-Account anmelden, <strong>Broadcast Settings → External Encoder</strong> öffnen und <strong>Server-URL</strong> und <strong>Stream Key</strong> kopieren."),
            ("SplitCam mit RoyalCams verbinden", "In SplitCam <strong>Stream Settings</strong> öffnen, die RoyalCams-Server-URL und den Stream Key in die Custom-RTMP-Felder einfügen. 3.500–6.000 Kbps bei 1920×1080, 30 fps und 2 Sekunden Keyframe einstellen."),
            ("Go Live drücken", "In SplitCam auf <strong>Go Live</strong> klicken, dann aus deinem Dashboard online gehen. Innerhalb von ~10 Sekunden erreicht dein Stream RoyalCams' Publikum."),
        ],
    },
    {
        "slug": "modelhub", "name": "Modelhub",
        "title": "Auf Modelhub senden mit SplitCam — External Encoder",
        "desc": "Auf Modelhub Live senden mit kostenlosem SplitCam — External Encoder für Pornhubs Creator-Plattform, Multi-Cam-Szenen und Overlays. Ohne Wasserzeichen.",
        "kw": "auf modelhub senden, modelhub, modelhub live, modelhub broadcast, modelhub obs, modelhub external encoder, modelhub rtmp, modelhub cam",
        "h1html": 'So sendest du auf <span class="accent">Modelhub</span> mit SplitCam',
        "h1short": "Auf Modelhub senden",
        "card": "External-Encoder-Setup für Modelhub Live (Pornhub).",
        "intro": "Modelhub ist Pornhubs Creator-Plattform — Videoverkauf, Fan-Abos und ein <strong>Live-Cam</strong>-Produkt mit enormem Top-of-Funnel-Traffic aus dem Pornhub-Netzwerk. Das Model-Dashboard unterstützt einen Standard-<strong>External Encoder</strong>-Pfad, an den sich kostenloses <strong style='color:var(--text)'>SplitCam</strong> anschließt — damit du mit Multi-Cam-Szenen, Overlays und Beauty-Filtern sendest.",
        "quick": "Auf Modelhub mit SplitCam senden: SplitCam installieren, Szene bauen, im Model-Dashboard <em>Live → Broadcast / External Encoder</em> öffnen, Server-URL und Stream Key kopieren, in SplitCam einfügen, Go Live."
                 "<ol><li>SplitCam installieren.</li><li>Kamera + Szene hinzufügen.</li><li>URL + Stream Key aus dem Dashboard holen.</li><li>In SplitCam einfügen.</li><li>Go Live drücken.</li></ol>",
        "key_how": "Im Modelhub-Model-Account anmelden und im Dashboard die <strong>Live- / Broadcast- / External-Encoder</strong>-Einstellungen öffnen. Die Seite zeigt eine an den Account gebundene <strong>Server-URL</strong> und einen <strong>Stream Key</strong> — beides in die Custom-RTMP-Felder von SplitCam kopieren. Eine Model-Verifizierung beim Netzwerk ist Pflicht, bevor du live gehst.",
        "tips": [
            ("Riesiger Top-of-Funnel-Traffic", "Modelhub zieht Zuschauer aus dem Pornhub-Netzwerk — eine polierte SplitCam-Szene macht aus diesem großen, beiläufigen Publikum zahlende Live-Zuschauer und Abonnenten."),
            ("Deine Videos cross-sellen", "Nutze Overlays, um Live-Zuschauer auf deine Modelhub-Videos und dein Abo zu lenken — die Plattform ist genau für diesen Funnel gebaut."),
            ("External Encoder schaltet Szenen frei", "Der Weg über SplitCams RTMP statt der einfachen Cam ermöglicht Multi-Cam-Layouts, Overlays und Filter."),
            _T_ETH,
        ],
        "faq": [
            ("Unterstützt Modelhub externe Encoder wie SplitCam?", "Ja — das Model-Dashboard bietet für Modelhub Live einen Standard-External-Encoder- / RTMP-Pfad. Server-URL und Stream Key nach der Verifizierung in SplitCam kopieren."),
            ("Wo bekomme ich meinen Modelhub-Stream-Key?", "In den Live- / Broadcast- / External-Encoder-Einstellungen des Dashboards — Server-URL und Stream Key erscheinen dort. Beides in die Custom-RTMP-Felder von SplitCam einfügen."),
            ("Welche Bitrate für Modelhub?", "Anpeilen: 1920×1080 bei 30 fps, 3.500–6.000 Kbps und 2 Sekunden Keyframe-Intervall. Vorher den SplitCam-Speedtest laufen lassen."),
            ("Ist SplitCam bei Modelhub kostenlos nutzbar?", "Ja — SplitCam ist kostenlos, ohne Wasserzeichen und ohne Zeitlimit. Die External-Encoder-Option von Modelhub ist im Dashboard kostenlos."),
        ],
        "steps": [
            ("SplitCam herunterladen und installieren", "SplitCam ist kostenlose Live-Streaming-Software für Windows und macOS — ohne Registrierung, ohne Kreditkarte, ohne Wasserzeichen."),
            ("Szene aufbauen", "SplitCam öffnen und die Webcam hinzufügen. Overlays, Text, eine zweite Kamera oder das Smartphone, Beauty-Filter oder einen KI-Hintergrund einbauen."),
            ("Modelhub-URL und Stream-Key holen", "Im Modelhub-Model-Account anmelden, <strong>Live → Broadcast / External Encoder</strong> öffnen und <strong>Server-URL</strong> und <strong>Stream Key</strong> kopieren."),
            ("SplitCam mit Modelhub verbinden", "In SplitCam <strong>Stream Settings</strong> öffnen, die Modelhub-Server-URL und den Stream Key in die Custom-RTMP-Felder einfügen. 3.500–6.000 Kbps bei 1920×1080, 30 fps und 2 Sekunden Keyframe einstellen."),
            ("Go Live drücken", "In SplitCam auf <strong>Go Live</strong> klicken, dann aus dem Dashboard online gehen. Innerhalb von ~10 Sekunden erreicht dein Stream Modelhubs Publikum."),
        ],
    },
    {
        "slug": "xhamsterlive", "name": "xHamsterLive",
        "title": "Auf xHamsterLive streamen mit SplitCam (RTMP/OBS)",
        "desc": "Auf xHamsterLive senden mit kostenlosem SplitCam über RTMP — Multi-Cam-Szenen, Overlays und Filter. xHamster-Mainstream-Traffic, ohne Wasserzeichen.",
        "kw": "auf xhamsterlive streamen, xhamsterlive, xhamsterlive obs, xhamsterlive rtmp, xhamsterlive broadcast, xhamsterlive model, xhamster live cam, xhamsterlive stream key",
        "h1html": 'So streamst du auf <span class="accent">xHamsterLive</span> mit SplitCam',
        "h1short": "Auf xHamsterLive streamen",
        "card": "Kostenloses SplitCam → RTMP-/OBS-Stream zu xHamsterLive.",
        "intro": "xHamsterLive ist der Live-Cam-Arm von xHamster — gleiche Broadcaster-Technik wie Stripchat, aber gespeist aus xHamsters Mainstream-Traffic, einer der größten Zuschauerbasen im Adult-Bereich. Models senden über das xHamsterLive-<strong>Studio</strong>, das sowohl den Browser-Broadcaster als auch einen <strong>externen Encoder über RTMP</strong> unterstützt. Mit kostenlosem <strong style='color:var(--text)'>SplitCam</strong> sendest du als externer Encoder für vollwertige Multi-Cam-Szenen, Overlays und Filter — oder, wenn du aus dem Browser sendest, wählst du SplitCam in xHamsterLive als <strong>virtuelle Kamera</strong> für denselben Effekt.",
        "quick": "Auf xHamsterLive mit SplitCam senden: SplitCam installieren, Szene bauen, Server-URL und Stream Key aus dem xHamsterLive-Studio kopieren, in die RTMP-Einstellungen von SplitCam einfügen, Go Live drücken."
                 "<ol><li>SplitCam installieren.</li><li>Kamera + Szene hinzufügen.</li><li>URL + Stream Key aus xHamsterLive Studio → External Encoder kopieren.</li><li>In SplitCams Custom-RTMP einfügen.</li><li>Go Live drücken.</li></ol>",
        "key_how": "Das xHamsterLive-Studio zeigt Broadcastern einen <strong>External-Encoder</strong>-Tab mit Server-URL und Stream Key. Beides in SplitCams <strong>Stream Settings → Custom RTMP</strong> einfügen; 4.000–6.000 Kbps bei 1920×1080, 30 fps und 2 Sekunden Keyframe einstellen. In SplitCam auf <strong>Go Live</strong> klicken, dann aus dem Studio online gehen. Möchtest du lieber den Browser-Broadcaster nutzen, öffne ihn und wähle im Kamera-Dropdown stattdessen <strong>SplitCam</strong> — deine komponierte Szene ersetzt die reine Webcam.",
        "tips": [
            ("xHamster-Traffic, Stripchat-Engine", "Gleiche Broadcaster-Tools wie Stripchat (Studio-Panel, Tipper-Menü, Lovense), aber mit xHamsters Mainstream-Funnel — eine andere Zuschauer-Mischung landet in deinem Raum."),
            ("Wenn möglich, externen Encoder nutzen", "RTMP aus SplitCam liefert eine stabile Bitrate und vollwertige Multi-Cam- und Overlay-Szenen; der Browser-Broadcaster funktioniert, deckelt aber die Kompositionsmöglichkeiten."),
            ("Tip-Menüs konvertieren Mainstream-Zuschauer", "Viele xHamster-Besucher sind neu beim Camming — ein klares Tip-Menü und eine Goal-Bar setzen Erwartungen und steigern die Session-Conversion spürbar."),
            _T_TEST,
        ],
        "faq": [
            ("Ist xHamsterLive dasselbe wie Stripchat?", "Es läuft auf Stripchats Broadcaster-Engine, aber Marke und Traffic-Quelle sind anders — xHamster speist sein Mainstream-Publikum hierher ein, sodass das Zuschauerprofil sich von einem reinen Stripchat-Signup unterscheidet."),
            ("Wo bekomme ich den xHamsterLive-Stream-Key?", "Im xHamsterLive-Studio das <em>Broadcast</em>- oder <em>External Encoder</em>-Panel öffnen — dort erscheinen Server-URL und Stream Key. Beides in SplitCams Custom-RTMP-Felder einfügen."),
            ("Browser-Broadcaster oder RTMP?", "External Encoder (RTMP) ist für ernsthafte Models vorzuziehen — stabile Bitrate und vollwertige SplitCam-Szenen. Der Browser-Broadcaster funktioniert auch: einfach SplitCam als Webcam wählen."),
            ("Ist SplitCam für xHamsterLive kostenlos?", "Ja — SplitCam ist kostenlos, ohne Wasserzeichen und ohne Zeitlimit."),
        ],
        "steps": [
            ("SplitCam herunterladen und installieren", "SplitCam ist kostenlose Live-Streaming-Software für Windows und macOS — ohne Registrierung, ohne Kreditkarte, ohne Wasserzeichen."),
            ("Szene aufbauen", "SplitCam öffnen und die Webcam hinzufügen. Overlays, ein Tip-Menü, eine zweite Kamera oder das Smartphone, Beauty-Filter oder einen KI-Hintergrund einbauen — alles live."),
            ("xHamsterLive-Studio-URL und Stream Key holen", "In xHamsterLive anmelden, das Studio öffnen, auf <strong>External Encoder</strong> wechseln und <strong>Server-URL</strong> und <strong>Stream Key</strong> kopieren."),
            ("SplitCam mit xHamsterLive verbinden", "In SplitCam <strong>Stream Settings → Custom RTMP</strong> öffnen, URL und Key einfügen. 4.000–6.000 Kbps bei 1920×1080, 30 fps und 2 Sekunden Keyframe einstellen."),
            ("Go Live drücken", "In SplitCam auf <strong>Go Live</strong> klicken, dann aus dem xHamsterLive-Studio online gehen. Innerhalb von ~10 Sekunden landet dein Stream in der öffentlichen Liste."),
        ],
    },
    {
        "slug": "premium-chat", "name": "Premium.Chat",
        "title": "Premium.Chat mit SplitCam nutzen — bezahlte Videocalls",
        "desc": "Kostenloses SplitCam als virtuelle Kamera auf Premium.Chat — bezahlte Pro-Minute-Videocalls mit Multi-Cam-Szenen, Overlays und Filtern. Ohne Wasserzeichen.",
        "kw": "premium chat mit splitcam, premium chat videocall, premium chat virtuelle kamera, premium.chat pay per minute, premium chat model, premium chat berater, premium chat live, videocall plattform splitcam",
        "h1html": 'So nutzt du SplitCam auf <span class="accent">Premium.Chat</span>',
        "h1short": "Premium.Chat mit SplitCam",
        "card": "SplitCam als virtuelle Kamera für bezahlte Premium.Chat-Calls nutzen.",
        "intro": "Premium.Chat ist eine bezahlte Pro-Minute-Plattform: Du legst deinen Minutenpreis für Chat, Voice oder <strong>Videocalls</strong> fest, teilst deinen persönlichen Link und Kund:innen zahlen, um mit dir zu sprechen. Die Calls laufen im Browser, womit sich kostenloses <strong style='color:var(--text)'>SplitCam</strong> direkt als <strong>virtuelle Kamera</strong> einklinkt — Multi-Cam-Szenen, Overlays, Lichtfilter und ein KI-Hintergrund landen beim Anrufer, ohne dass sich an Premium.Chat etwas ändert.",
        "quick": "SplitCam auf Premium.Chat nutzen: SplitCam installieren, eine saubere Szene für Videocalls bauen, einen eingehenden Premium.Chat-Call annehmen und im Kamera-Selector des Calls <em>SplitCam</em> wählen."
                 "<ol><li>SplitCam installieren.</li><li>Szene einrichten (gutes Licht, optionales Overlay).</li><li>Minutenpreis auf Premium.Chat festlegen.</li><li>Eingehenden Videocall annehmen.</li><li>SplitCam als Kamera auswählen.</li></ol>",
        "key_how": "Premium.Chat-Calls laufen im Browser. SplitCam installiert eine virtuelle Webcam namens <strong>\"SplitCam Video Driver\"</strong> — beim Start eines Calls auf das Kamera-Symbol im Premium.Chat-Call-Fenster klicken und von der integrierten Webcam auf <strong>SplitCam</strong> umstellen. Deine komponierte Szene (echte Kamera + Overlays + Filter) wird das, was der Anrufer sieht.",
        "tips": [
            ("Premium.Chat zahlt pro Minute, nicht pro Stream", "Anders als Tipping-Räume à la Chaturbate wirst du pro Minute bezahlt. Weiches Licht, klarer Ton und ein KI-Hintergrund wirken mehr wie eine Premium-Beratung als eine öffentliche Cam."),
            ("Bewirb deinen Link, nicht ein Profil", "Premium.Chat gibt dir einen persönlichen Link, den du auf Social Media, in der OnlyFans-Bio oder einem Linktree platzieren kannst — so finden dich Kund:innen."),
            ("Overlays nur, wenn sie nützen", "Bei 1-zu-1-Calls lenken schwere Overlays ab. Nutze SplitCam für Kameraqualität, Licht und Hintergrund — und halt den Bildausschnitt überwiegend auf dir."),
            _T_TEST,
        ],
        "faq": [
            ("Wie verbindet sich SplitCam mit Premium.Chat?", "Als virtuelle Kamera. Premium.Chat-Calls laufen im Browser; einfach SplitCam im Kamera-Selector des Calls auswählen — kein Stream Key, kein RTMP."),
            ("Unterstützt Premium.Chat OBS?", "Premium.Chat ist browserbasiert, OBS klinkt sich also genauso ein wie SplitCam — über die virtuelle Kamera. SplitCam ist die leichtere, kostenlose Option ohne Wasserzeichen."),
            ("Kann ich eine zweite Kamera oder Overlays auf Premium.Chat nutzen?", "Ja — Szene in SplitCam komponieren (zweite Kamera, Overlays, Filter), Premium.Chat sieht eine einzige Webcam. Bei 1-zu-1-Calls sparsam einsetzen."),
            ("Ist SplitCam kostenlos?", "Ja — kostenlos, ohne Wasserzeichen und ohne Zeitlimit."),
        ],
        "steps": [
            ("SplitCam herunterladen und installieren", "SplitCam ist kostenlose Live-Streaming-Software für Windows und macOS — ohne Registrierung, ohne Kreditkarte, ohne Wasserzeichen. Es installiert eine virtuelle Kamera, die der Browser nutzen kann."),
            ("Szene für Calls einrichten", "SplitCam öffnen, Webcam hinzufügen, Licht setzen, optional einen KI-Hintergrund oder ein dezentes Overlay ergänzen. Bildausschnitt sauber halten — das ist ein bezahlter Call, keine Bühne."),
            ("Tarif auf Premium.Chat festlegen", "Bei Premium.Chat anmelden, Minutenpreis für Videocalls festlegen und persönlichen Link kopieren. Auf Social Media oder in Bios teilen."),
            ("Eingehenden Videocall annehmen", "Wenn ein:e Kund:in Zeit bezahlt, geht die Call-Anfrage ein. Im Premium.Chat-Dashboard annehmen."),
            ("SplitCam als Kamera auswählen", "Im Kamera-Symbol-Menü des Call-Fensters von der integrierten Webcam auf <strong>SplitCam</strong> umstellen. Deine komponierte Szene erreicht jetzt die andere Seite."),
        ],
    },
    {
        "slug": "arousr", "name": "Arousr",
        "title": "Arousr mit SplitCam nutzen — Sexting & Videochat",
        "desc": "Kostenloses SplitCam als virtuelle Kamera für Arousr — Multi-Cam-Szenen, Overlays und Filter für bezahltes Sexting, Voice und Video. Ohne Wasserzeichen.",
        "kw": "arousr mit splitcam, arousr videochat, arousr virtuelle kamera, arousr cam girl, arousr model, sexting plattform splitcam, arousr live, arousr broadcast",
        "h1html": 'So nutzt du SplitCam auf <span class="accent">Arousr</span>',
        "h1short": "Arousr mit SplitCam",
        "card": "SplitCam als virtuelle Kamera für Arousr-Videochats nutzen.",
        "intro": "Arousr ist eine bezahlte <strong>Sexting-, Voice- und Videochat</strong>-Plattform — Kund:innen kaufen Credits, um Models per Text zu schreiben, anzurufen oder mit ihnen zu video-chatten, und du wirst pro Session bezahlt. Das Video läuft im Browser (oder am Handy in der Arousr-App), wodurch sich kostenloses <strong style='color:var(--text)'>SplitCam</strong> am Desktop als <strong>virtuelle Kamera</strong> einklinkt: Multi-Cam-Szenen, Overlays, Lichtfilter und ein KI-Hintergrund gehen direkt an den Kunden.",
        "quick": "SplitCam auf Arousr nutzen: SplitCam installieren, Szene einrichten, eine eingehende Arousr-Videoanfrage annehmen und im Kamera-Selector <em>SplitCam</em> wählen."
                 "<ol><li>SplitCam installieren.</li><li>Szene und Licht einrichten.</li><li>Sexting-/Video-Tarife auf Arousr festlegen.</li><li>Eingehende Videoanfrage annehmen.</li><li>SplitCam im Kamera-Dropdown auswählen.</li></ol>",
        "key_how": "Arousrs Web-Video läuft im Browser. SplitCam installiert eine virtuelle Webcam namens <strong>\"SplitCam Video Driver\"</strong> — startet im Arousr-Dashboard eine Videosession, im Session-Fenster die Kamera auf <strong>SplitCam</strong> umstellen. Die komponierte Szene (Kamera + Overlays + Filter) wird das, was der Kunde sieht. In der Arousr-Mobile-App sind virtuelle Kameras nicht verfügbar — dort die echte Handykamera nutzen und SplitCam für Desktop-Sessions reservieren.",
        "tips": [
            ("Sessions werden nach Zeit bezahlt", "Kund:innen kaufen Credits pro Minute (oder pro Nachricht für Text). Poliertes Video — gutes Licht, KI-Hintergrund, Beauty-Filter — rechnet sich über längere Sessions schnell."),
            ("Erst Sexting, dann Video als Upsell", "Der größte Teil des Arousr-Umsatzes ist Text. Eine kurze Video-Vorschau während eines Sext-Chats verkauft die Kund:innen in eine vollständige Videosession — dort greift der Minutenpreis."),
            ("Mobile-App-Sessions ≠ Desktop", "Virtuelle Kameras funktionieren beim Browser-Video am Desktop. Die Arousr-Mobile-App nutzt die Handykamera direkt — gleicher Workflow, anderes Werkzeug."),
            _T_TEST,
        ],
        "faq": [
            ("Wie verbindet sich SplitCam mit Arousr?", "Als virtuelle Kamera. Arousrs Videochat läuft am Desktop im Browser — einfach SplitCam im Kamera-Selector wählen. Kein Stream Key nötig."),
            ("Unterstützt Arousr OBS?", "Arousr ist browserbasiert, OBS klinkt sich also genauso ein wie SplitCam — über die virtuelle Kamera. SplitCam ist die kostenlose Option ohne Wasserzeichen."),
            ("Kann ich Overlays in einer Sexting-+-Video-Session nutzen?", "Ja — Szene in SplitCam komponieren (Licht, Overlay, zweite Kamera), Arousr sieht eine einzige Webcam. Bei 1-zu-1 die Overlays dezent halten."),
            ("Ist SplitCam für Arousr kostenlos?", "Ja — kostenlos, ohne Wasserzeichen und ohne Zeitlimit."),
        ],
        "steps": [
            ("SplitCam herunterladen und installieren", "SplitCam ist kostenlose Live-Streaming-Software für Windows und macOS — ohne Registrierung, ohne Kreditkarte, ohne Wasserzeichen. Es installiert eine virtuelle Kamera, die der Browser auswählen kann."),
            ("Szene aufbauen", "SplitCam öffnen, Webcam hinzufügen, Licht justieren, optional einen KI-Hintergrund oder Beauty-Filter ergänzen. Intim halten — das ist eine bezahlte 1-zu-1-Session, keine öffentliche Bühne."),
            ("Tarife auf Arousr festlegen", "Bei Arousr anmelden, Pro-Nachricht- und Pro-Minute-Videotarif festlegen und sicherstellen, dass dein Profil freigegeben ist, damit Anfragen eingehen."),
            ("Eingehende Videoanfrage annehmen", "Startet ein:e Kund:in aus dem Sexting heraus oder direkt eine Videosession, im Arousr-Dashboard annehmen."),
            ("SplitCam als Kamera auswählen", "Im Kamera-Dropdown des Session-Fensters von der integrierten Webcam auf <strong>SplitCam</strong> umstellen. Deine komponierte Szene erreicht jetzt die andere Seite."),
        ],
    },
    {
        "slug": "cams-com", "name": "Cams.com",
        "title": "Auf Cams.com senden mit SplitCam (RTMP/OBS)",
        "desc": "Auf Cams.com senden mit kostenlosem SplitCam über RTMP — Multi-Cam-Szenen, Overlays und Filter. AFFs zahlende Member-Basis. Ohne Wasserzeichen.",
        "kw": "auf cams.com senden, cams.com, cams.com obs, cams.com rtmp, cams.com model, cams.com broadcaster, cams.com stream key, adult friend finder cams, cams.com live",
        "h1html": 'So sendest du auf <span class="accent">Cams.com</span> mit SplitCam',
        "h1short": "Auf Cams.com senden",
        "card": "Kostenloses SplitCam → RTMP-Stream ins Cams.com-/AFF-Netzwerk.",
        "intro": "Cams.com ist der Cam-Arm des AdultFriendFinder-Netzwerks — eines der ältesten Dating- und Cam-Ökosysteme online, mit einer beträchtlichen Basis aus <strong>bereits zahlenden Mitgliedern</strong>, die aus AFF, AmateurMatch und anderen FriendFinder-Properties einfließen. Models senden über das Cams.com-<strong>Model Center</strong>, das sowohl den Browser-Broadcaster als auch einen <strong>externen Encoder über RTMP</strong> unterstützt. Kostenloses <strong style='color:var(--text)'>SplitCam</strong> streamt per RTMP für vollwertige Multi-Cam-Szenen, Overlays und Filter — oder registriert sich im Browser-Broadcaster als <strong>virtuelle Kamera</strong> mit demselben Ergebnis.",
        "quick": "Auf Cams.com senden: SplitCam installieren, Szene bauen, Cams.com-RTMP-Server-URL und Stream Key aus dem Model Center holen, in SplitCam einfügen, Go Live drücken."
                 "<ol><li>SplitCam installieren.</li><li>Kamera + Szene hinzufügen.</li><li>Server-URL + Key aus Cams.com Model Center → External Encoder kopieren.</li><li>In SplitCams Custom-RTMP einfügen.</li><li>Go Live drücken.</li></ol>",
        "key_how": "Das Cams.com Model Center hat einen <strong>External Encoder / OBS</strong>-Tab mit Server-URL und Stream Key. Beides in SplitCams <strong>Stream Settings → Custom RTMP</strong> einfügen; 3.500–5.000 Kbps bei 1920×1080, 30 fps und 2 Sekunden Keyframe einstellen. In SplitCam auf <strong>Go Live</strong> klicken, dann die Show aus dem Model Center starten. Möchtest du lieber den Browser-Broadcaster nutzen, wähle stattdessen <strong>SplitCam</strong> im Kamera-Dropdown.",
        "tips": [
            ("AFF-Cross-Traffic = zahlende Mitglieder", "Cams.com zieht Zuschauer aus AdultFriendFinder-Accounts, die bereits eine Zahlungsmethode hinterlegt haben — anders als ein frisches Signup-Publikum. Die Conversion zu Private und Tipps liegt tendenziell höher."),
            ("External Encoder schlägt Browser", "RTMP aus SplitCam liefert eine saubere Bitrate und erlaubt Multi-Cam-Szenen mit Overlays; der Browser-Broadcaster funktioniert, deckelt aber die Produktion."),
            ("Private-Show-Tools nutzen", "Cams.com setzt stark auf Private- und Exclusive-Sessions. Ein Tip-Menü und ein klarer Weg ins Private (im Overlay) heben den Umsatz pro Zuschauer spürbar."),
            _T_TEST,
        ],
        "faq": [
            ("Ist Cams.com dasselbe wie AdultFriendFinder?", "Selbes Mutternetzwerk. Cams.com ist die Cam-Broadcasting-Marke; Zuschauer kommen über AFF, AmateurMatch und andere FriendFinder-Sites — das macht einen großen Teil des Traffics aus."),
            ("Wo bekomme ich den Cams.com-Stream-Key?", "Im Cams.com Model Center den Tab <em>External Encoder</em> oder <em>OBS</em> öffnen — dort erscheinen Server-URL und Stream Key. Beides in SplitCams Custom-RTMP-Felder einfügen."),
            ("Browser-Broadcaster oder RTMP?", "RTMP (External Encoder) ist vorzuziehen — stabile Bitrate, vollwertige SplitCam-Szenen. Browser-Broadcaster funktioniert als Fallback: einfach SplitCam als Webcam wählen."),
            ("Ist SplitCam für Cams.com kostenlos?", "Ja — SplitCam ist kostenlos, ohne Wasserzeichen und ohne Zeitlimit."),
        ],
        "steps": [
            ("SplitCam herunterladen und installieren", "SplitCam ist kostenlose Live-Streaming-Software für Windows und macOS — ohne Registrierung, ohne Kreditkarte, ohne Wasserzeichen."),
            ("Szene aufbauen", "SplitCam öffnen und die Webcam hinzufügen. Overlays, ein Tip-Menü, eine zweite Kamera oder das Smartphone, Beauty-Filter oder einen KI-Hintergrund einbauen — alles live."),
            ("Cams.com-URL und Stream Key holen", "Beim Cams.com Model Center anmelden, den Tab <strong>External Encoder / OBS</strong> öffnen und <strong>Server-URL</strong> und <strong>Stream Key</strong> kopieren."),
            ("SplitCam mit Cams.com verbinden", "In SplitCam <strong>Stream Settings → Custom RTMP</strong> öffnen, URL und Key einfügen. 3.500–5.000 Kbps bei 1920×1080, 30 fps und 2 Sekunden Keyframe einstellen."),
            ("Go Live drücken", "In SplitCam auf <strong>Go Live</strong> klicken, dann aus dem Model Center online gehen. Dein Stream landet innerhalb von ~10 Sekunden im Cams.com-/AFF-Netzwerk."),
        ],
    },
    {
        "slug": "stripcamfun", "name": "StripCamFun",
        "title": "Auf StripCamFun streamen mit SplitCam (RTMP/OBS)",
        "desc": "Auf StripCamFun senden mit kostenlosem SplitCam über RTMP — Multi-Cam-Szenen, Overlays und Filter für ein Indie-Cam-Publikum. Ohne Wasserzeichen.",
        "kw": "auf stripcamfun streamen, stripcamfun, stripcamfun obs, stripcamfun rtmp, stripcamfun model, stripcamfun broadcast, strip cam fun, stripcamfun stream key",
        "h1html": 'So streamst du auf <span class="accent">StripCamFun</span> mit SplitCam',
        "h1short": "Auf StripCamFun streamen",
        "card": "Kostenloses SplitCam → RTMP-/OBS-Stream zu StripCamFun.",
        "intro": "StripCamFun ist eine unabhängige Live-Cam-Seite — kleiner als die Chaturbate-Tier-Riesen, aber mit einem echten, weniger gesättigten Publikum und deutlich geringerer Broadcaster-Konkurrenz pro Nische. Models senden über das StripCamFun-Model-Panel, das eine <strong>External-Encoder-/RTMP</strong>-Option bietet. Kostenloses <strong style='color:var(--text)'>SplitCam</strong> verbindet sich per RTMP für vollwertige Multi-Cam-Szenen, Overlays und Filter — und wo ein Browser-Broadcaster angeboten wird, registriert sich SplitCam auch als <strong>virtuelle Kamera</strong>.",
        "quick": "Auf StripCamFun senden: SplitCam installieren, Szene bauen, StripCamFun-Server-URL und Stream Key kopieren, in die RTMP-Einstellungen von SplitCam einfügen, Go Live drücken."
                 "<ol><li>SplitCam installieren.</li><li>Kamera + Szene hinzufügen.</li><li>URL + Stream Key aus dem StripCamFun-Model-Panel → External Encoder kopieren.</li><li>In SplitCams Custom-RTMP einfügen.</li><li>Go Live drücken.</li></ol>",
        "key_how": "Das StripCamFun-Model-Dashboard und den Bereich <strong>External Encoder / OBS</strong> öffnen. Server-URL und Stream Key in SplitCams <strong>Stream Settings → Custom RTMP</strong> kopieren; 3.500–5.000 Kbps bei 1920×1080, 30 fps und 2 Sekunden Keyframe einstellen. In SplitCam auf <strong>Go Live</strong> klicken, dann aus dem Dashboard online schalten.",
        "tips": [
            ("Kleinerer Pool, leichtere Sichtbarkeit", "Auf einer Tier-1-Seite bist du eine:r von Tausenden online; auf StripCamFun ist die Broadcaster-Liste kurz — eine polierte SplitCam-Szene fällt auf der Startseite schneller auf."),
            ("Cross-Broadcast für Reichweite", "Indie-Cam-Seiten passen gut zu Multi-Streaming. Nutze SplitCam, um gleichzeitig zu StripCamFun und einer größeren Seite zu senden, und sammle Tipper aus beiden Pools ein."),
            ("Auf Nischen-Tagging setzen", "Indie-Publikum sucht eher nach Nische als nach Star-Power. Spezifische Tags und ein Szenen-Overlay, das die Nische benennt, holt Zuschauer aus der Liste."),
            _T_TEST,
        ],
        "faq": [
            ("Wo bekomme ich den StripCamFun-Stream-Key?", "Im Model-Dashboard den Tab <em>External Encoder / OBS</em> öffnen — dort erscheinen Server-URL und Stream Key. Beides in SplitCams Custom-RTMP-Felder einfügen."),
            ("Ist StripCamFun sicher zum Senden?", "Wie bei jeder Indie-Cam-Seite vorher den Model-Vertrag und die Auszahlungsbedingungen prüfen. Eine echte E-Mail-Adresse nutzen und die Auszahlungsmethode zuerst verifizieren."),
            ("Kann ich gleichzeitig zu StripCamFun und einer anderen Cam-Seite senden?", "Ja — SplitCam kann an mehrere Custom-RTMP-Endpoints gleichzeitig pushen. Vorher die Exklusivitätsregeln jeder Seite prüfen."),
            ("Ist SplitCam für StripCamFun kostenlos?", "Ja — kostenlos, ohne Wasserzeichen und ohne Zeitlimit."),
        ],
        "steps": [
            ("SplitCam herunterladen und installieren", "SplitCam ist kostenlose Live-Streaming-Software für Windows und macOS — ohne Registrierung, ohne Kreditkarte, ohne Wasserzeichen."),
            ("Szene aufbauen", "SplitCam öffnen und die Webcam hinzufügen. Overlays, ein Tip-Menü, eine zweite Kamera oder das Smartphone, Beauty-Filter oder einen KI-Hintergrund einbauen — alles live."),
            ("StripCamFun-URL und Stream Key holen", "Beim StripCamFun-Model-Dashboard anmelden, <strong>External Encoder / OBS</strong> öffnen und <strong>Server-URL</strong> und <strong>Stream Key</strong> kopieren."),
            ("SplitCam mit StripCamFun verbinden", "In SplitCam <strong>Stream Settings → Custom RTMP</strong> öffnen, URL und Key einfügen. 3.500–5.000 Kbps bei 1920×1080, 30 fps und 2 Sekunden Keyframe einstellen."),
            ("Go Live drücken", "In SplitCam auf <strong>Go Live</strong> klicken, dann im StripCamFun-Dashboard online schalten. Dein Stream landet innerhalb von ~10 Sekunden in der öffentlichen Liste."),
        ],
    },
    {
        "slug": "mym-fans", "name": "MYM.fans",
        "title": "Auf MYM.fans live gehen mit SplitCam — virtuelle Kamera",
        "desc": "Auf MYM.fans (Frankreichs OnlyFans-Alternative) live gehen mit SplitCam als virtueller Kamera — Multi-Cam, Overlays, Filter. Ohne Wasserzeichen.",
        "kw": "auf mym live gehen, mym.fans live, mym fans virtuelle kamera, mym creator, mym frankreich, mym live stream, mym obs, mym fans broadcast, mym influencer",
        "h1html": 'So gehst du auf <span class="accent">MYM.fans</span> live mit SplitCam',
        "h1short": "Auf MYM.fans live gehen",
        "card": "Nutze SplitCam als virtuelle Kamera für MYM.fans-Lives.",
        "intro": "MYM.fans ist die führende französische Creator-Abo-Plattform — Frankreichs Antwort auf OnlyFans, mit Abonnements, Pay-per-View, Trinkgeldern und eingebauter <strong>Live-Stream</strong>-Funktion für Fans. Der Broadcaster läuft im Browser, daher fügt kostenloses <strong style='color:var(--text)'>SplitCam</strong> als <strong>virtuelle Kamera</strong> Multi-Cam-Szenen, Overlays und Filter über der normalen Webcam hinzu. Falls dein Creator-Dashboard eine External-Encoder-Option zeigt, kann SplitCam auch per RTMP verbinden.",
        "quick": "Auf MYM.fans live gehen mit SplitCam: SplitCam installieren, Szene bauen, Live auf MYM starten und im Kamera-Dropdown des Broadcasters <em>SplitCam</em> auswählen — dann auf Go Live."
                 "<ol><li>SplitCam installieren.</li><li>Kamera + Szene hinzufügen.</li><li>Live auf MYM.fans starten.</li><li>SplitCam im Kamera-Dropdown auswählen.</li><li>Go Live drücken.</li></ol>",
        "key_how": "MYM.fans-Lives laufen im Browser. Szene in SplitCam aufbauen — sie wird als Webcam namens <strong>\"SplitCam Video Driver\"</strong> erkannt — dann den MYM-Live-Broadcaster öffnen und im Kamera-Dropdown <strong>SplitCam</strong> wählen. Wenn eine <strong>Stream-Key-/External-Encoder</strong>-Option im Creator-Dashboard erscheint, in SplitCams Custom-RTMP-Felder einfügen.",
        "tips": [
            ("Größte französische Creator-Plattform", "MYM ist die Nummer 1 unter den Fan-Plattformen in Frankreich, mit einem französisch-/europäischen Publikum, das in EUR zahlt. Eine polierte SplitCam-Szene mit französischsprachigen Overlays konvertiert besser als eine flache Webcam."),
            ("Virtuelle Kamera funktioniert ohne Stream Key", "Auch der reine Browser-Live bekommt deine komplette SplitCam-Szene — zweite Kamera, Overlays, Beauty-Filter oder KI-Hintergrund — einfach indem SplitCam als Webcam ausgewählt wird."),
            ("Cross-Selling von PPV während des Lives", "MYM ist um Premium-Inhalte herum gebaut. Bildschirm-Overlays, die dein Abo bewerben oder PPV-Nachrichten freischalten, machen aus Live-Zuschauern zahlende Abonnenten."),
            _T_TEST,
        ],
        "faq": [
            ("Wie verbindet sich SplitCam mit MYM.fans?", "Der MYM-Live ist browserbasiert, also verbindet sich SplitCam als virtuelle Kamera — im Kamera-Selector SplitCam wählen. Kein Stream Key nötig."),
            ("Kann ich Overlays und mehrere Kameras auf MYM nutzen?", "Ja — die Szene in SplitCam aufbauen (zweite Kamera, Overlays, KI-Hintergrund); MYM sieht die fertige Szene als eine Webcam."),
            ("Unterstützt MYM.fans OBS oder externe Encoder?", "Der Live ist primär browser-/webcam-basiert. Falls dein Dashboard eine Stream-Key-Option anbietet, in SplitCams Custom-RTMP-Felder einfügen; sonst die Virtuelle-Kamera-Methode nutzen."),
            ("Ist SplitCam für MYM.fans kostenlos?", "Ja — SplitCam ist kostenlos, ohne Wasserzeichen und ohne Zeitlimit."),
        ],
        "steps": [
            ("SplitCam herunterladen und installieren", "SplitCam ist kostenlose Live-Streaming-Software für Windows und macOS — ohne Registrierung, ohne Kreditkarte, ohne Wasserzeichen. Sie installiert eine virtuelle Kamera, die der Browser auswählen kann."),
            ("Szene aufbauen", "SplitCam öffnen und die Webcam hinzufügen. Overlays, Text (auf Französisch, wenn dein Publikum FR ist), eine zweite Kamera oder das Smartphone, Beauty-Filter oder einen KI-Hintergrund einbauen."),
            ("Live auf MYM.fans starten", "Beim MYM-Creator-Konto anmelden und den Live-Broadcaster öffnen, um einen Stream für deine Abonnenten zu starten."),
            ("SplitCam als Kamera auswählen", "Im Kamera-Dropdown von MYM <strong>SplitCam</strong> statt der reinen Webcam wählen — deine komponierte Szene ersetzt das flache Kamerabild. (Oder einen Stream Key in SplitCams Custom-RTMP-Felder einfügen, falls verfügbar.)"),
            ("Go Live", "Sendung starten — deine SplitCam-Szene, Overlays und Filter erreichen deine MYM-Abonnenten."),
        ],
    },
    {
        "slug": "fc2-live", "name": "FC2 Live",
        "title": "Auf FC2 Live streamen mit SplitCam (RTMP/OBS)",
        "desc": "Auf FC2 Live (Japans größter Live-Cam-Seite) senden mit kostenlosem SplitCam über RTMP — Multi-Cam-Szenen, Overlays, Filter. Ohne Wasserzeichen.",
        "kw": "auf fc2 live streamen, fc2 live obs, fc2 live rtmp, fc2 live broadcast, fc2 live配信, fc2 live stream key, fc2 live model, fc2 live japan, fc2 ライブ",
        "h1html": 'So streamst du auf <span class="accent">FC2 Live</span> mit SplitCam',
        "h1short": "Auf FC2 Live streamen",
        "card": "Kostenloses SplitCam → RTMP-/OBS-Stream zu FC2 Live.",
        "intro": "FC2 Live ist Japans größte Live-Streaming-Plattform — riesige Zuschauerbasis, eigene Erwachsenen-Sektion und ein separater Bezahlshow-Flow, der sie zu einem der lukrativsten Cam-Märkte Asiens macht. Models senden über das FC2-Broadcaster-Panel, das sowohl den In-Browser-Broadcaster als auch einen <strong>externen Encoder über RTMP</strong> unterstützt. Kostenloses <strong style='color:var(--text)'>SplitCam</strong> sendet per RTMP für vollwertige Multi-Cam-Szenen, Overlays und Filter.",
        "quick": "Auf FC2 Live senden mit SplitCam: SplitCam installieren, Szene bauen, Server-URL und Stream Key aus dem FC2-Broadcaster kopieren, in SplitCams RTMP-Einstellungen einfügen, Go Live drücken."
                 "<ol><li>SplitCam installieren.</li><li>Kamera + Szene hinzufügen.</li><li>URL + Stream Key aus dem FC2-Broadcaster-Panel kopieren.</li><li>In SplitCams Custom-RTMP einfügen.</li><li>Go Live drücken.</li></ol>",
        "key_how": "Das FC2-Live-Broadcaster-Panel öffnen und auf <strong>External Encoder / RTMP</strong> umschalten. Server-URL und Stream Key in SplitCams <strong>Stream Settings → Custom RTMP</strong> kopieren; 3.500–5.000 Kbps bei 1920×1080, 30 fps und 2 Sekunden Keyframe einstellen. In SplitCam auf <strong>Go Live</strong> klicken, dann die Show aus dem FC2-Dashboard starten.",
        "tips": [
            ("Riesiges japanisches Publikum", "FC2 ist Tier 1 in Japan — die Zuschauer sind lokal, zahlen in JPY und neigen zu längeren Bezahlshows. Japanische Overlay-Texte (z. B. Tip-Menü in 円 / JPY) heben die Conversion deutlich."),
            ("Erwachsenen-Sektion ist getrennt", "FC2 hat sowohl allgemeine als auch Erwachsenen-Lives. Die Raum-Kategorie vor dem Live-Gang korrekt setzen — Adult-Shows sind aus der allgemeinen Sektion nicht auffindbar."),
            ("Externer Encoder für stabile Bitrate", "Japans mobil-lastiges Publikum reagiert empfindlich auf Frame-Drops. RTMP aus SplitCam mit konstanten 4 Mbps schlägt den Browser-Broadcaster bei der Zuverlässigkeit."),
            _T_TEST,
        ],
        "faq": [
            ("Wo bekomme ich den FC2-Live-Stream-Key?", "Im FC2-Live-Broadcaster-Panel auf <em>External Encoder</em> oder <em>OBS</em> umschalten — Server-URL und Stream Key erscheinen. Beides in SplitCams Custom-RTMP-Felder einfügen."),
            ("Browser-Broadcaster oder RTMP?", "RTMP (externer Encoder) ist vorzuziehen — stabile Bitrate, volle SplitCam-Szenen. Der Browser-Broadcaster funktioniert als Fallback: SplitCam als Webcam wählen."),
            ("Brauche ich ein japanisches Konto, um auf FC2 zu senden?", "Ein FC2-Konto ist erforderlich, und Adult-Streaming hat zusätzliche Altersverifizierungs-Schritte für das Model. FC2s Onboarding folgen."),
            ("Ist SplitCam für FC2 Live kostenlos?", "Ja — SplitCam ist kostenlos, ohne Wasserzeichen und ohne Zeitlimit."),
        ],
        "steps": [
            ("SplitCam herunterladen und installieren", "SplitCam ist kostenlose Live-Streaming-Software für Windows und macOS — ohne Registrierung, ohne Kreditkarte, ohne Wasserzeichen."),
            ("Szene aufbauen", "SplitCam öffnen und die Webcam hinzufügen. Overlays, ein Tip-Menü in 円 (JPY), eine zweite Kamera oder das Smartphone, Beauty-Filter oder einen KI-Hintergrund einbauen — alles live."),
            ("FC2-Live-URL und Stream Key holen", "Bei FC2 anmelden, das Live-Broadcaster-Panel öffnen, auf <strong>External Encoder</strong> umschalten und <strong>Server-URL</strong> und <strong>Stream Key</strong> kopieren."),
            ("SplitCam mit FC2 Live verbinden", "In SplitCam <strong>Stream Settings → Custom RTMP</strong> öffnen, URL und Key einfügen. 3.500–5.000 Kbps bei 1920×1080, 30 fps und 2 Sekunden Keyframe einstellen."),
            ("Go Live drücken", "In SplitCam auf <strong>Go Live</strong> klicken, dann die Show aus dem FC2-Dashboard starten. Dein Stream landet innerhalb von ~10 Sekunden in der öffentlichen Liste."),
        ],
    },
    {
        "slug": "boosty", "name": "Boosty",
        "title": "Auf Boosty live gehen mit SplitCam — virtuelle Kamera",
        "desc": "Auf Boosty (Russlands Creator-Plattform) live gehen mit SplitCam als virtueller Kamera — Multi-Cam-Szenen, Overlays, Filter. Ohne Wasserzeichen.",
        "kw": "auf boosty live gehen, boosty live, boosty stream, boosty virtuelle kamera, boosty creator, бусти прямой эфир, boosty obs, boosty paid live, boosty subscriber",
        "h1html": 'So gehst du auf <span class="accent">Boosty</span> live mit SplitCam',
        "h1short": "Auf Boosty live gehen",
        "card": "Nutze SplitCam als virtuelle Kamera für Boosty-Lives.",
        "intro": "Boosty ist Russlands größte Creator-Monetarisierungsplattform — ein Patreon-ähnlicher Dienst mit Abos, Bezahl-Posts, Trinkgeldern und einer <strong>Live-Broadcast</strong>-Funktion, mit einer Creator-Bandbreite, die neben Mainstream-Creators auch Adult-Creators umfasst. Der Live läuft im Browser, also fügt kostenloses <strong style='color:var(--text)'>SplitCam</strong> als <strong>virtuelle Kamera</strong> Multi-Cam-Szenen, Overlays und Filter hinzu, die Abonnenten aus einer einfachen Webcam nicht bekommen würden.",
        "quick": "Auf Boosty live gehen mit SplitCam: SplitCam installieren, Szene bauen, Live auf Boosty starten und im Kamera-Dropdown des Broadcasters <em>SplitCam</em> wählen — dann Go Live."
                 "<ol><li>SplitCam installieren.</li><li>Kamera + Szene hinzufügen.</li><li>Live auf Boosty starten.</li><li>SplitCam im Kamera-Dropdown auswählen.</li><li>Go Live drücken.</li></ol>",
        "key_how": "Boosty-Lives laufen im Browser. Szene in SplitCam aufbauen — sie wird als Webcam namens <strong>\"SplitCam Video Driver\"</strong> erkannt — dann den Boosty-Live-Broadcaster öffnen und im Kamera-Dropdown <strong>SplitCam</strong> statt der reinen Webcam wählen.",
        "tips": [
            ("Russlands größte Creator-Plattform", "Boosty hat Patreon für viele RU-Creator nach Sanktionen ersetzt, das Publikum ist also treu und ans Zahlen in RUB gewöhnt. Eine polierte SplitCam-Szene mit russischsprachigen Overlays konvertiert gut."),
            ("Live-Shows nach Abo-Stufe", "Boosty erlaubt das Gating von Live-Streams nach Abo-Stufe. SplitCam funktioniert mit allen Stufen — der Encoder kümmert sich nicht um die Stufe des Zuschauers, du sendest einmal und Boosty regelt den Zugriff."),
            ("Trinkgeld- und Pay-per-View-Overlay", "Boosty unterstützt Bezahl-Post-Freischaltungen und Trinkgelder. Ein Bildschirm-Overlay, das die Stufen-Vorteile benennt, hebt die Conversions während Live-Streams."),
            _T_TEST,
        ],
        "faq": [
            ("Wie verbindet sich SplitCam mit Boosty?", "Der Boosty-Live ist browserbasiert, also verbindet sich SplitCam als virtuelle Kamera — im Kamera-Selector SplitCam wählen. Kein Stream Key nötig."),
            ("Kann ich Overlays im Boosty-Live nutzen?", "Ja — die Szene in SplitCam komponieren (Overlays, zweite Kamera, KI-Hintergrund); Boosty sieht eine Webcam. Abonnenten bekommen die komplette komponierte Szene."),
            ("Unterstützt Boosty OBS oder externe Encoder?", "Boosty-Lives sind primär browserbasiert. Falls eine Stream-Key-Option im Creator-Panel erscheint, in SplitCams Custom-RTMP-Felder einfügen; sonst die Virtuelle-Kamera-Methode nutzen."),
            ("Ist SplitCam für Boosty kostenlos?", "Ja — SplitCam ist kostenlos, ohne Wasserzeichen und ohne Zeitlimit."),
        ],
        "steps": [
            ("SplitCam herunterladen und installieren", "SplitCam ist kostenlose Live-Streaming-Software für Windows und macOS — ohne Registrierung, ohne Kreditkarte, ohne Wasserzeichen. Sie installiert eine virtuelle Kamera, die der Browser auswählen kann."),
            ("Szene aufbauen", "SplitCam öffnen und die Webcam hinzufügen. Overlays (russischsprachig für dein Publikum), eine zweite Kamera oder das Smartphone, Beauty-Filter oder einen KI-Hintergrund einbauen."),
            ("Live auf Boosty starten", "Beim Boosty-Creator-Konto anmelden und den Live-Broadcaster öffnen. Das Stufen-Gating setzen, falls der Live hinter einer bezahlten Ebene laufen soll."),
            ("SplitCam als Kamera auswählen", "Im Kamera-Dropdown von Boosty <strong>SplitCam</strong> statt der reinen Webcam wählen — deine komponierte Szene ersetzt das flache Kamerabild."),
            ("Go Live", "Sendung starten — deine SplitCam-Szene, Overlays und Filter erreichen deine Boosty-Abonnenten."),
        ],
    },
    {
        "slug": "amateurcommunity", "name": "AmateurCommunity",
        "title": "Auf AmateurCommunity streamen mit SplitCam (RTMP)",
        "desc": "Auf AmateurCommunity (Deutschlands Amateur-Cam-Seite) senden mit kostenlosem SplitCam über RTMP — Multi-Cam-Szenen, Overlays, Filter. Ohne Wasserzeichen.",
        "kw": "auf amateurcommunity streamen, amateurcommunity obs, amateurcommunity rtmp, amateur community deutschland, amateurcommunity model, ac community broadcast, amateurcommunity live, amateur cam deutschland",
        "h1html": 'So streamst du auf <span class="accent">AmateurCommunity</span> mit SplitCam',
        "h1short": "Auf AmateurCommunity streamen",
        "card": "Kostenloses SplitCam → RTMP-Stream zu AmateurCommunity (DE).",
        "intro": "AmateurCommunity ist Deutschlands größte Amateur-Cam- und Content-Community — seit den frühen 2000ern aktiv, mit einem tief loyalen deutschsprachigen Publikum, das ans Zahlen für Premium-Inhalte und Live-Shows gewöhnt ist. Models senden aus dem AC-Model-Panel, das einen <strong>externen Encoder über RTMP</strong> ebenso unterstützt wie den In-Browser-Broadcaster. Kostenloses <strong style='color:var(--text)'>SplitCam</strong> sendet per RTMP für vollwertige Multi-Cam-Szenen, Overlays und Filter — deutschsprachige Overlays sprechen das lokale Publikum direkt an.",
        "quick": "Auf AmateurCommunity senden: SplitCam installieren, Szene bauen, AC-Server-URL und Stream Key aus dem Model-Panel kopieren, in SplitCams RTMP-Einstellungen einfügen, Go Live drücken."
                 "<ol><li>SplitCam installieren.</li><li>Kamera + Szene hinzufügen.</li><li>URL + Stream Key aus dem AC-Model-Panel kopieren.</li><li>In SplitCams Custom-RTMP einfügen.</li><li>Go Live drücken.</li></ol>",
        "key_how": "Das AmateurCommunity-Model-Panel und den Tab <strong>External Encoder / OBS</strong> öffnen. Server-URL und Stream Key in SplitCams <strong>Stream Settings → Custom RTMP</strong> kopieren; 3.500–5.000 Kbps bei 1920×1080, 30 fps und 2 Sekunden Keyframe einstellen. In SplitCam auf <strong>Go Live</strong> klicken, dann aus dem Panel online schalten.",
        "tips": [
            ("Deutschsprachiges, zahlungsbereites Publikum", "AmateurCommunitys Publikum stammt überwiegend aus dem DACH-Raum (DE/AT/CH) und zahlt in EUR — Overlays, Tip-Menü und On-Stream-Chat auf Deutsch konvertieren deutlich besser als Englisch."),
            ("Premium-PPV plus Live-Kombi", "AC erlaubt den Verkauf von PPV-Inhalten zusätzlich zum Live. Eine Live-Show, die das PPV anteasert (mit einem Bildschirm-Overlay), hebt die PPV-Verkäufe während und nach der Sendung."),
            ("Externer Encoder für stabile Qualität", "ACs Publikum erwartet hohe Produktionsqualität; RTMP mit konstanten 4 Mbps aus SplitCam schlägt die schwankende Bitrate des Browser-Broadcasters."),
            _T_TEST,
        ],
        "faq": [
            ("Wo bekomme ich den AmateurCommunity-Stream-Key?", "Im AC-Model-Panel den Tab <em>External Encoder</em> oder <em>OBS</em> öffnen — Server-URL und Stream Key erscheinen. Beides in SplitCams Custom-RTMP-Felder einfügen."),
            ("Browser-Broadcaster oder RTMP?", "RTMP (externer Encoder) ist für ernsthafte Models vorzuziehen — stabile Bitrate, volle SplitCam-Szenen. Der Browser-Broadcaster funktioniert als Fallback: SplitCam als Webcam wählen."),
            ("Muss ich in Deutschland sein, um auf AC zu senden?", "Nein, aber das Publikum ist deutschsprachig. Models von überall können sich registrieren — der zentrale Schritt ist das Bestehen der Model-Verifizierung und der Steuerformulare."),
            ("Ist SplitCam für AmateurCommunity kostenlos?", "Ja — SplitCam ist kostenlos, ohne Wasserzeichen und ohne Zeitlimit."),
        ],
        "steps": [
            ("SplitCam herunterladen und installieren", "SplitCam ist kostenlose Live-Streaming-Software für Windows und macOS — ohne Registrierung, ohne Kreditkarte, ohne Wasserzeichen."),
            ("Szene aufbauen", "SplitCam öffnen und die Webcam hinzufügen. Overlays (auf Deutsch — \"Trinkgeld\" / \"PPV freischalten\"), eine zweite Kamera oder das Smartphone, Beauty-Filter oder einen KI-Hintergrund einbauen — alles live."),
            ("AmateurCommunity-URL und Stream Key holen", "Beim AC-Model-Panel anmelden, <strong>External Encoder / OBS</strong> öffnen und <strong>Server-URL</strong> und <strong>Stream Key</strong> kopieren."),
            ("SplitCam mit AmateurCommunity verbinden", "In SplitCam <strong>Stream Settings → Custom RTMP</strong> öffnen, URL und Key einfügen. 3.500–5.000 Kbps bei 1920×1080, 30 fps und 2 Sekunden Keyframe einstellen."),
            ("Go Live drücken", "In SplitCam auf <strong>Go Live</strong> klicken, dann im AC-Model-Panel online schalten. Dein Stream landet innerhalb von ~10 Sekunden in der öffentlichen Liste."),
        ],
    },
    {
        "slug": "myfans-jp", "name": "MyFans.jp",
        "title": "Auf MyFans.jp live gehen mit SplitCam — virtuelle Kamera",
        "desc": "Auf MyFans.jp (Japans OnlyFans) live gehen mit SplitCam als virtueller Kamera — Multi-Cam-Szenen, Overlays, Filter. Ohne Wasserzeichen.",
        "kw": "auf myfans live gehen, myfans.jp live, myfans 配信, myfans virtuelle kamera, myfans creator, マイファンズ, myfans japan, myfans broadcast, myfans abonnent",
        "h1html": 'So gehst du auf <span class="accent">MyFans.jp</span> live mit SplitCam',
        "h1short": "Auf MyFans.jp live gehen",
        "card": "Nutze SplitCam als virtuelle Kamera für MyFans.jp-Lives.",
        "intro": "MyFans.jp ist Japans führende Creator-Abo-Plattform — die japanische Antwort auf OnlyFans, mit Abos, Pay-per-View, Trinkgeldern (投げ銭) und einer integrierten <strong>Live-Stream</strong>-Funktion für Fans. Der Broadcaster läuft im Browser, also fügt kostenloses <strong style='color:var(--text)'>SplitCam</strong> als <strong>virtuelle Kamera</strong> Multi-Cam-Szenen, Overlays und Filter hinzu, die eine einfache Webcam nicht liefern kann. Falls dein Creator-Dashboard eine Option für externen Encoder bietet, kann SplitCam auch über RTMP verbinden.",
        "quick": "Auf MyFans.jp live gehen mit SplitCam: SplitCam installieren, Szene bauen, Live auf MyFans starten und im Kamera-Dropdown des Broadcasters <em>SplitCam</em> wählen — dann Go Live."
                 "<ol><li>SplitCam installieren.</li><li>Kamera + Szene hinzufügen.</li><li>Live auf MyFans.jp starten.</li><li>SplitCam im Kamera-Dropdown auswählen.</li><li>Go Live drücken.</li></ol>",
        "key_how": "MyFans.jps Live läuft im Browser. Szene in SplitCam aufbauen — sie wird als Webcam namens <strong>\"SplitCam Video Driver\"</strong> erkannt — dann den MyFans-Live-Broadcaster öffnen und im Kamera-Dropdown <strong>SplitCam</strong> wählen. Falls eine <strong>Stream-Key- / Externer-Encoder</strong>-Option im Creator-Dashboard erscheint, diese stattdessen in SplitCams Custom-RTMP-Felder einfügen.",
        "tips": [
            ("Japans größte Fan-Plattform", "MyFans ist die Nummer 1 unter den Creator-Abo-Plattformen in Japan, mit einem JP-nativen Publikum, das in 円 (JPY) zahlt. Japanische Overlays und eine polierte SplitCam-Szene konvertieren weit besser als eine einfache Webcam."),
            ("Virtuelle Kamera, kein Stream Key nötig", "Ein reiner Browser-Live bekommt trotzdem deine komplette SplitCam-Szene — zweite Kamera, Overlays, Beauty-Filter oder KI-Hintergrund — indem du SplitCam als Webcam auswählst."),
            ("PPV-Cross-Sell während des Live", "MyFans dreht sich um 投げ銭 (Trinkgelder) und Bezahl-Posts. Ein Bildschirm-Overlay, das dein PPV-Paket oder dein Tip-Ziel benennt, hebt die Einnahmen während eines Lives spürbar."),
            _T_TEST,
        ],
        "faq": [
            ("Wie verbindet sich SplitCam mit MyFans.jp?", "Der MyFans-Live ist browserbasiert, also verbindet sich SplitCam als virtuelle Kamera — im Kamera-Selector SplitCam wählen. Kein Stream Key nötig."),
            ("Kann ich Overlays und mehrere Kameras auf MyFans nutzen?", "Ja — die Szene in SplitCam aufbauen (zweite Kamera, Overlays, KI-Hintergrund); MyFans sieht die fertige Szene als eine einzige Webcam."),
            ("Unterstützt MyFans.jp OBS oder externe Encoder?", "Der Live ist primär browser-/webcam-basiert. Falls eine Stream-Key-Option im Dashboard erscheint, in SplitCams Custom-RTMP-Felder einfügen; sonst die Virtuelle-Kamera-Methode nutzen."),
            ("Ist SplitCam für MyFans.jp kostenlos?", "Ja — SplitCam ist kostenlos, ohne Wasserzeichen und ohne Zeitlimit."),
        ],
        "steps": [
            ("SplitCam herunterladen und installieren", "SplitCam ist kostenlose Live-Streaming-Software für Windows und macOS — ohne Registrierung, ohne Kreditkarte, ohne Wasserzeichen. Sie installiert eine virtuelle Kamera, die der Browser auswählen kann."),
            ("Szene aufbauen", "SplitCam öffnen und die Webcam hinzufügen. Overlays (auf Japanisch — 「投げ銭」「PPV解放」 für dein Publikum), eine zweite Kamera oder das Smartphone, Beauty-Filter oder einen KI-Hintergrund einbauen."),
            ("Live auf MyFans.jp starten", "Beim MyFans-Creator-Konto anmelden und den Live-Broadcaster (配信) öffnen, um einen Stream für deine Abonnenten zu starten."),
            ("SplitCam als Kamera auswählen", "Im Kamera-Dropdown von MyFans <strong>SplitCam</strong> statt der reinen Webcam wählen — deine komponierte Szene ersetzt das flache Kamerabild. (Oder einen Stream Key in SplitCams Custom-RTMP-Felder einfügen, falls verfügbar.)"),
            ("Go Live", "Sendung starten — deine SplitCam-Szene, Overlays und Filter erreichen deine MyFans-Abonnenten."),
        ],
    },
    {
        "slug": "privacy-com-br", "name": "Privacy.com.br",
        "title": "Auf Privacy.com.br live gehen mit SplitCam",
        "desc": "Auf Privacy.com.br (Brasiliens OnlyFans) live gehen mit SplitCam als virtueller Kamera — Multi-Cam-Szenen, Overlays, Filter. Ohne Wasserzeichen.",
        "kw": "auf privacy live gehen, privacy.com.br ao vivo, privacy live, privacy brasilien, privacy virtuelle kamera, privacy creator, privacy broadcast, privacy br creator, privacy abonnent",
        "h1html": 'So gehst du auf <span class="accent">Privacy.com.br</span> live mit SplitCam',
        "h1short": "Auf Privacy.com.br live gehen",
        "card": "Nutze SplitCam als virtuelle Kamera für Privacy.com.br ao vivo.",
        "intro": "Privacy.com.br ist Brasiliens führende Creator-Abo-Plattform — die brasilianische Antwort auf OnlyFans, mit assinaturas, Pay-per-View, gorjetas und einer integrierten <strong>ao vivo</strong>-Funktion (Live-Stream) für fãs. Der Broadcaster läuft im Browser, also fügt kostenloses <strong style='color:var(--text)'>SplitCam</strong> als <strong>virtuelle Kamera</strong> Multi-Cam-Szenen, Overlays und Filter hinzu, die eine flache Webcam nicht liefern kann. Falls dein Creator-Dashboard eine Option für externen Encoder bietet, kann SplitCam auch über RTMP verbinden.",
        "quick": "Auf Privacy.com.br live gehen mit SplitCam: SplitCam installieren, Szene bauen, ao-vivo auf Privacy starten und im Kamera-Dropdown des Broadcasters <em>SplitCam</em> wählen — dann Go Live."
                 "<ol><li>SplitCam installieren.</li><li>Kamera + Szene hinzufügen.</li><li>Ao vivo auf Privacy.com.br starten.</li><li>SplitCam im Kamera-Dropdown auswählen.</li><li>Go Live drücken.</li></ol>",
        "key_how": "Der ao vivo von Privacy.com.br läuft im Browser. Szene in SplitCam aufbauen — sie wird als Webcam namens <strong>\"SplitCam Video Driver\"</strong> erkannt — dann den Privacy-Live-Broadcaster öffnen und im Kamera-Dropdown <strong>SplitCam</strong> wählen. Falls eine <strong>Stream-Key- / Externer-Encoder</strong>-Option angeboten wird, diese stattdessen in SplitCams Custom-RTMP-Felder einfügen.",
        "tips": [
            ("Brasiliens größte Fan-Plattform", "Privacy ist die Nummer 1 unter den Creator-Abo-Plattformen in Brasilien, mit einem portugiesischsprachigen Publikum, das ans Zahlen in BRL via PIX gewöhnt ist. Portugiesische Overlays plus eine polierte SplitCam-Szene konvertieren viel besser als eine einfache Webcam."),
            ("Virtuelle Kamera, kein Stream Key nötig", "Ein reiner Browser-Live bekommt trotzdem deine komplette SplitCam-Szene — zweite Kamera, Overlays, Beauty-Filter oder KI-Hintergrund — einfach indem du SplitCam als Webcam auswählst."),
            ("Tip-Menüs + PPV während des ao vivo", "Privacy unterstützt gorjetas (Trinkgelder) und Bezahl-Posts. Ein Bildschirm-Overlay, das dein PPV-Paket oder dein meta-de-gorjeta benennt, hebt die Einnahmen während eines Lives."),
            _T_TEST,
        ],
        "faq": [
            ("Wie verbindet sich SplitCam mit Privacy.com.br?", "Der ao vivo von Privacy ist browserbasiert, also verbindet sich SplitCam als virtuelle Kamera — im Kamera-Selector SplitCam wählen. Kein Stream Key nötig."),
            ("Kann ich Overlays und mehrere Kameras auf Privacy nutzen?", "Ja — die Szene in SplitCam aufbauen (zweite Kamera, Overlays, KI-Hintergrund); Privacy sieht die fertige Szene als eine einzige Webcam."),
            ("Unterstützt Privacy.com.br OBS oder externe Encoder?", "Der ao vivo ist primär browser-/webcam-basiert. Falls eine Stream-Key-Option im Dashboard erscheint, in SplitCams Custom-RTMP-Felder einfügen; sonst die Virtuelle-Kamera-Methode nutzen."),
            ("Ist SplitCam für Privacy.com.br kostenlos?", "Ja — SplitCam ist kostenlos, ohne Wasserzeichen und ohne Zeitlimit."),
        ],
        "steps": [
            ("SplitCam herunterladen und installieren", "SplitCam ist kostenlose Live-Streaming-Software für Windows und macOS — ohne Registrierung, ohne Kreditkarte, ohne Wasserzeichen. Sie installiert eine virtuelle Kamera, die der Browser auswählen kann."),
            ("Szene aufbauen", "SplitCam öffnen und die Webcam hinzufügen. Overlays auf Portugiesisch einbauen (\"gorjeta\", \"desbloquear PPV\"), eine zweite Kamera oder das Smartphone, Beauty-Filter oder einen KI-Hintergrund."),
            ("Ao vivo auf Privacy.com.br starten", "Beim Privacy-Creator-Konto anmelden und den ao-vivo-Broadcaster öffnen, um einen Live für deine Abonnenten zu starten."),
            ("SplitCam als Kamera auswählen", "Im Kamera-Dropdown von Privacy <strong>SplitCam</strong> statt der reinen Webcam wählen — deine komponierte Szene ersetzt das flache Kamerabild. (Oder einen Stream Key in SplitCams Custom-RTMP-Felder einfügen, falls verfügbar.)"),
            ("Go Live", "Sendung starten — deine SplitCam-Szene, Overlays und Filter erreichen deine Privacy.com.br-Abonnenten."),
        ],
    },
]
