# -*- coding: utf-8 -*-
"""Finnish (fi) content for cam-streaming-guides."""

_T_ETH = ("Käytä kaapeliyhteyttä", "Ethernet voittaa Wi-Fin pitkässä striimissä — "
          "kadonnut frame on menetetty tip. Vedä kaapeli stream-PC:lle.")
_T_TEST = ("Tee ensin yksityinen testi", "Aja lyhyt testilähetys kameran, äänen, "
           "rajauksen ja overlay-yhteyden tarkistamiseksi ennen huoneen avaamista yleisölle.")

PLATFORMS_FI = [
    {"slug": "chaturbate", "name": "Chaturbate",
     "title": "Lähetys Chaturbatessa SplitCamilla — Token & RTMP",
     "desc": "Lähetys Chaturbatessa ilmaisella SplitCamilla — broadcast token, RTMP, monikamera-näkymät ja overlayt. Ei vesileimaa.",
     "kw": "chaturbate lähetys, chaturbate broadcast token, chaturbate rtmp obs, chaturbate external encoder, chaturbate live",
     "h1html": 'Miten lähetät <span class="accent">Chaturbatessa</span> SplitCamilla',
     "h1short": "Lähetys Chaturbate",
     "card": "Token-pohjainen asetus ulkoisella enkooderilla Chaturbatessa.",
     "intro": "Chaturbate on yksi suurimmista cam-alustoista, rakennettu token-talouden päälle. Selainpohjainen broadcaster on litteä yhden kameran työkalu — siirtyminen <strong style='color:var(--text)'>ulkoiseen enkooderiin</strong> ilmaisella <strong style='color:var(--text)'>SplitCamilla</strong> avaa monikamera-näkymät, overlayt ja suodattimet samaan token-pohjaiseen striimiin.",
     "quick": "Lähetys Chaturbatessa SplitCamilla: asenna SplitCam, rakenna näkymä, Chaturbatessa avaa <em>Broadcast Yourself → My Broadcast</em>, kopioi broadcast token, liitä SplitCamiin, Go Live."
              "<ol><li>Asenna SplitCam.</li><li>Lisää kamera + näkymä.</li>"
              "<li>Kopioi broadcast token Chaturbatesta.</li><li>Liitä SplitCamiin.</li>"
              "<li>Paina Go Live.</li></ol>",
     "key_how": "Chaturbatessa klikkaa <strong>Broadcast Yourself</strong> avataksesi <strong>My Broadcast</strong> -sivun, sitten <strong>View RTMP/OBS broadcast information and stream key</strong>. Avain näkyy <strong>broadcast tokenina</strong> — kopioi. Käsittele kuten salasanaa; ei koskaan julkisesti.",
     "tips": [
         ("Token on avain", "Chaturbate käyttää broadcast tokeniasi yleisen stream keyn sijaan. Käsittele kuten salasanaa ja resetoi vuodettaessa."),
         ("Paljon liikkumavaraa", "Chaturbaten RTMP ingest hyväksyy 4K asti, 60 fps ja korkean bitraten — raja on uploadisi, ei alusta. Keyframe 2 sekunnin välein."),
         _T_ETH, _T_TEST,
     ],
     "faq": [
         ("Sallii Chaturbate OBS:n / ulkoiset enkooderit?", "Kyllä — Chaturbate tukee ulkoisia enkoodereita virallisesti omalla «How do I set up OBS?» -artikkelillaan. Aktivoi «Use External Encoder to Broadcast» -kytkimellä lähetysasetuksissa."),
         ("Missä Chaturbate stream keyni on?", "Broadcast Yourself → My Broadcast → View RTMP/OBS broadcast information and stream key. Avain on broadcast tokenisi."),
         ("Mikä bitrate Chaturbatelle?", "3 500–6 000 Kbps 1080p:ssä riittää reilusti. Chaturbaten katto on korkea — todellinen raja on uploadisi; aja ensin SplitCamin nopeustesti."),
         ("Onko SplitCam ilmainen Chaturbatelle?", "Kyllä — täysin ilmainen, ilman vesileimaa ja ilman aikarajaa: enkooderi ei syö token-tulojasi."),
     ]},
    {"slug": "cam4", "name": "CAM4",
     "title": "Lähetys CAM4:ssä SplitCamilla — External Encoder",
     "desc": "Lähetys CAM4:ssä ilmaisella SplitCamilla — External Encoder, stream key, geo-esto ja overlayt. Ei vesileimaa.",
     "kw": "cam4 lähetys, cam4.com, cam4 external encoder, cam4 stream key, cam4 rtmp obs",
     "h1html": 'Miten lähetät <span class="accent">CAM4</span>:ssä SplitCamilla',
     "h1short": "Lähetys CAM4",
     "card": "External Encoder CAM4:ssä geo-hallinnoilla.",
     "intro": "CAM4 on globaali cam-and-earn-alusta sisäänrakennetuilla geo-hallinnoilla — voit piilottaa lähetyksen valituissa maissa. Lähettäminen ilmaisen <strong style='color:var(--text)'>SplitCamin</strong> kautta ulkoisena enkooderina avaa näkymänvaihdot ja overlayt, joita perus-broadcaster ei tee.",
     "quick": "Lähetys CAM4:ssä SplitCamilla: asenna SplitCam, rakenna näkymä, CAM4:ssä mene <em>Broadcast &amp; Earn Money → Start Broadcast → External Encoder</em>, Get Stream Key, liitä SplitCamiin, Go Live."
              "<ol><li>Asenna SplitCam.</li><li>Lisää kamera + näkymä.</li>"
              "<li>Hanki stream key CAM4:stä.</li><li>Liitä SplitCamiin.</li>"
              "<li>Paina Go Live.</li></ol>",
     "key_how": "CAM4:ssä klikkaa <strong>Broadcast</strong> → <strong>Broadcast &amp; Earn Money</strong> → <strong>Start Broadcast</strong>, sitten <strong>External Encoder</strong> ylhäältä. Täytä syntymäaika, sukupuoli ja maa, käytä <strong>Get Stream Key</strong> ja kopioi. Vihreä slider SplitCamin Stream Settings -valikossa vahvistaa yhteyden.",
     "tips": [
         ("Aseta geo-rajoitukset", "CAM4 sallii lähetyksen piilottamisen tietyissä maissa ja alueilla — määritä CAM4:n puolella ennen go-livea."),
         ("Seuraa vihreää slideria", "CAM4:n asetus näyttää vihreän sliderin SplitCamin Stream Settings -valikossa, kun avain hyväksytään — punainen = tarkista avain."),
         ("Matalampi bitrate kuin tavallisesti", "CAM4:n ingest rajoittaa videon bitraten noin 3 000 Kbps:ään — alempi kuin useimmat cam-sivut. Älä pakota korkeammalle."),
         _T_ETH,
     ],
     "faq": [
         ("Tukeeko CAM4 virallisesti OBS:ää / ulkoisia enkoodereita?", "Kyllä — CAM4:llä on virallinen OBS Guide tuki-sivulla ja se suosittelee External Encoderia parhaaseen kokemukseen. SplitCam käyttää samaa RTMP-reittiä."),
         ("Voinko geo-estää CAM4-streamini?", "Kyllä — CAM4:llä on sisäänrakennettu geo-rajoitus lähetyksen piilottamiseksi tietyissä maissa. Aseta CAM4:ssä, ei SplitCamissa."),
         ("Missä CAM4:n stream key on?", "Broadcast → Broadcast & Earn Money → Start Broadcast → External Encoder → Get Stream Key."),
         ("Mikä bitrate CAM4:lle?", "Matalampi kuin keskimäärin — CAM4:n ingest rajoittaa ~3 000 Kbps:ään 30 fps:llä 1 sekunnin keyframella. Virallinen taulukko suosittelee, ettet ylitä ~3 000:ta."),
     ]},
    {"slug": "bongacams", "name": "BongaCams",
     "title": "Lähetys BongaCamsissä SplitCamilla — External Encoder",
     "desc": "Lähetys BongaCamsissä ilmaisella SplitCamilla — External Encoder, monikamera-näkymät, overlayt ja AI-tausta. Ei vesileimaa.",
     "kw": "bongacams, bongcams, bongacams lähetys, bongacams external encoder, bongacams rtmp obs",
     "h1html": 'Miten lähetät <span class="accent">BongaCamsissä</span> SplitCamilla',
     "h1short": "Lähetys BongaCams",
     "card": "External Encoder -asetus BongaCamsille.",
     "intro": "BongaCams on globaali cam-alusta. Ulkoisen enkooderin lähetys ei aina ole aktiivinen — kun se on aktivoitu, ilmainen <strong style='color:var(--text)'>SplitCam</strong> johtaa lähetyksen monikamera-näkymillä, overlayilla ja AI-taustalla.",
     "quick": "Lähetys BongaCamsissä SplitCamilla: asenna SplitCam, rakenna näkymä, BongaCamsissä mene <em>Options → Broadcast settings → Select Encoder → External Encoder</em>, kopioi URL ja avain, liitä SplitCamiin, Go Live."
              "<ol><li>Asenna SplitCam.</li><li>Lisää kamera + näkymä.</li>"
              "<li>Hanki URL ja avain BongaCamsiltä.</li><li>Liitä SplitCamiin.</li>"
              "<li>Paina Go Live.</li></ol>",
     "key_how": "BongaCamsissä avaa <strong>Options</strong> → <strong>Broadcast settings</strong> → <strong>Select Encoder</strong> → <strong>External Encoder</strong> ja kopioi näytetty palvelin-URL ja stream key. <strong>Jos External Encoder -painike puuttuu</strong>, ota yhteyttä BongaCamsin tukeen ja pyydä ulkoisen koodauksen aktivointia tilillesi.",
     "tips": [
         ("Ei External Encoder -painiketta? Tuki", "BongaCams aktivoi ulkoisen koodauksen tilikohtaisesti — jos vaihtoehto puuttuu Broadcast settingsistä, tuki aktivoi sen."),
         ("Sovita resoluutio", "BongaCams suosittelee, että webkameran ja lähetyksen resoluutiot vastaavat — esim. molemmat 1280×720."),
         _T_ETH, _T_TEST,
     ],
     "faq": [
         ("Miksi External Encoder -painike ei näy BongaCamsissä?", "Ulkoinen koodaus ei ole oletuksena aktiivinen jokaisella tilillä — ota yhteyttä BongaCamsin tukeen aktivoidaksesi sen, ja painike ilmestyy Broadcast settings -valikkoon."),
         ("Pitääkö BongaCams-tilini varmentaa?", "Kyllä — lähetys vaatii 18+ iän, virallisen ID:n iän tarkistukseen ja tilin hyväksynnän ennen livenä menoa."),
         ("Mikä bitrate BongaCamsille?", "BongaCamsin RTMP ingest rajoittaa videon bitraten noin 6 000 Kbps:ään 2 sekunnin keyframella — 3 500–6 000 1080p:ssä on ihanteellinen alue; testaa upload ensin."),
         ("Onko SplitCam ilmainen BongaCamsille?", "Kyllä — täysin ilmainen, ilman vesileimaa ja ilman aikarajaa, joten enkooderi ei vähennä token-tulojasi BongaCamsissä."),
     ]},
    {"slug": "stripchat", "name": "Stripchat",
     "title": "Lähetys Stripchatissä SplitCamilla — Strip Cam Setup",
     "desc": "Lähetys Stripchatissä — strip cam -alustalla — ilmaisella SplitCamilla. Ulkoinen ohjelmisto, token-avain, näkymät ja overlayt.",
     "kw": "strip cam, stripchat live stream, stripchat lähetys, stripchat external software, stripchat stream key, stripchat rtmp obs",
     "h1html": 'Miten lähetät <span class="accent">Stripchatissä</span> SplitCamilla',
     "h1short": "Lähetys Stripchat",
     "card": "Ulkoinen ohjelmisto Stripchat-streameille.",
     "intro": "Stripchat on suuri cam-alusta interaktiivisuuden painotuksella. <em>External software</em> -tila antaa sinulle token-pohjaisen avaimen — laita se ilmaiseen <strong style='color:var(--text)'>SplitCamiin</strong>, jotta voit lähettää näkymillä, overlayilla ja suodattimilla litteän kameran sijaan.",
     "quick": "Lähetys Stripchatissä SplitCamilla: asenna SplitCam, rakenna näkymä, Stripchatissä valitse <em>Switch to external software</em>, kopioi stream key, liitä SplitCamiin, Go Live."
              "<ol><li>Asenna SplitCam.</li><li>Lisää kamera + näkymä.</li>"
              "<li>Hanki stream key Stripchatistä.</li><li>Liitä SplitCamiin.</li>"
              "<li>Paina Go Live.</li></ol>",
     "key_how": "Stripchatissä valitse <strong>Switch to external software</strong>, sitten <strong>Show external software settings for the stream</strong>. Kopioi stream key — Stripchat näyttää sen tokenina. Pidä yksityisenä.",
     "tips": [
         ("Sovita resoluutio sivuston kanssa", "Stripchatin FAQ varoittaa: ohjelmistosi resoluution on vastattava tarkalleen sivuston resoluutiota, muuten video pikselöityy. Aseta molemmat samaksi."),
         ("Huomio 2 Mbps minimissä", "Stripchat ilmoittaa 2 Mbps uploadin minimiksi — ja sanoo suoraan, että se ei riitä OBS-streamingiin tai multistreamingiin. Tähtää paljon korkeammalle."),
         ("Avain on token", "Stripchatin stream key on token — kopioi tarkasti, älä koskaan jaa, resetoi vuodettaessa."),
         _T_ETH,
     ],
     "faq": [
         ("Suositteleeko Stripchat OBS:ää / ulkoista ohjelmistoa?", "Kyllä — Stripchatin virallinen FAQ suosittelee ulkoista broadcast-ohjelmistoa kuten OBS:ää «saavuttaakseen parhaan videon ja äänen laadun». SplitCam toimii samalla tavalla."),
         ("Miten vaihdan Stripchatin ulkoiseen ohjelmistoon?", "Broadcast Centerissä valitse Switch to External Broadcast Software (OBS), sitten avaa external software settings paljastaaksesi stream keyn (tokenin)."),
         ("Mikä bitrate Stripchatille?", "RTMP ingest hyväksyy ~6 000 Kbps asti 2 sekunnin keyframella. 3 500–6 000 1080p:ssä on ihanteellinen — mutta sinun pitää olla reilusti 2 Mbps minimin yläpuolella, erityisesti OBS-streamingissa."),
         ("Onko SplitCam ilmainen Stripchatille?", "Kyllä — ei lisenssimaksua, ei vesileimaa, ei aikarajaa: edes pitkät interaktiiviset Stripchat-shokit eivät maksa mitään enkooderin puolelta."),
     ]},
    {"slug": "onlyfans", "name": "OnlyFans",
     "title": "Live OnlyFansissa SplitCamilla — Valtuutus tai avain",
     "desc": "Live OnlyFansissa ilmaisella SplitCamilla — sisäänkirjautuminen valtuutuksella tai OBS Keylla, monikamera-näkymät, overlayt. Ei vesileimaa.",
     "kw": "live onlyfans, onlyfans live stream, onlyfans valtuutus splitcam, onlyfans obs key, onlyfans streaming software",
     "h1html": 'Miten menet livenä <span class="accent">OnlyFansissa</span> SplitCamilla',
     "h1short": "Live OnlyFans",
     "card": "Valtuuta kerran tai liitä avain — live OnlyFansissa.",
     "intro": "OnlyFans-live on tilaajillesi. SplitCam yhdistää <strong style='color:var(--text)'>kahdella tavalla</strong> — kirjaudut kerran OnlyFans-tilillä ja SplitCam hakee stream keyn automaattisesti ja pitää sen synkronoituna, tai liität OBS Keyn käsin. Molemmissa tapauksissa lähetät monikamera-näkymillä, overlayilla ja suodattimilla.",
     "quick": "Live OnlyFansissa SplitCamilla: asenna SplitCam, rakenna näkymä, avaa Stream Settings &rarr; Add Channel &rarr; OnlyFans ja valitse <em>Valtuutus</em> — kirjaudu OnlyFans-tilillä, SplitCam hakee avaimen automaattisesti — ja paina Go Live. Liitetyllä tilillä voit muuttaa OnlyFans-streamin parametreja SplitCamissa, ilman että avaat OnlyFans-sivustoa.",
     "steps": [
         ("Lataa ja asenna SplitCam",
          "SplitCam on ilmainen streaming-ohjelmisto Windowsille ja macOS:lle — ilman rekisteröintiä, korttia tai vesileimaa. Se on enkooderi, joka lähettää videosi OnlyFansiin."),
         ("Aseta kamera ja näkymä",
          "Avaa SplitCam ja lisää webkamera. Rakenna näkymä, jonka katsojat näkevät — overlayt, teksti, toinen kamera, beauty-suodattimet tai AI-tausta, kaikki sovellettuna livenä."),
         ("Yhdistäminen — Tapa 1: Valtuutus (suositeltu)",
          "SplitCamissa avaa <strong>Stream Settings</strong> &rarr; <strong>Add Channel</strong> &rarr; <strong>OnlyFans</strong> ja valitse <strong>Valtuutus</strong>. Kirjaudu OnlyFans-sähköpostilla ja salasanalla. SplitCam yhdistää tilisi, hakee stream keyn automaattisesti ja pitää sen synkronoituna — ja antaa sinun hallita OnlyFans-liven parametreja SplitCamissa, muuttaen niitä lähetyksen aikana tai sen jälkeen ilman OnlyFans-sivuston avaamista."),
         ("Yhdistäminen — Tapa 2: Stream Key (käsin)",
          "Etkö halua kirjautua? Käytä avainta. OnlyFansissa mene <strong>Profile</strong> &rarr; <strong>Settings</strong> &rarr; <strong>Other</strong>-osio ja kopioi <strong>OBS Key</strong>. SplitCamissa Add Channel &rarr; OnlyFans, liitä avainkenttään. Tämä avain on staattinen — muutoksia varten myöhemmin palaat OnlyFans-sivustolle."),
         ("Go Live",
          "Tavasta riippumatta paina <strong>Go Live</strong> SplitCamissa. Tavalla 1 voit jatkaa OnlyFans-parametrien säätämistä SplitCamista reaaliajassa; Tavalla 2 avain pysyy täsmälleen asetetuissa arvoissa."),
     ],
     "tips": [
         ("Valtuutus vs Stream Key", "Kaksi tapaa yhdistää: <strong>Valtuutus</strong> (kirjaudut kerran, avain haetaan ja synkronoidaan — helpoin reitti) tai <strong>Stream Key</strong> (kopioit OBS Keyn OnlyFans → Profile → Settings → Other -kohdasta ja liität). Valtuutus säästää käsin tehtävää copy-paste-työtä."),
         ("Muuta asetuksia poistumatta SplitCamista", "Valtuutuksella tili pysyy liitettynä, joten säädät OnlyFans-liven parametreja SplitCamissa lähetyksen aikana tai sen jälkeen — ilman OnlyFans-sivuston kautta menoa."),
         ("Kohtuullinen bitrate", "OnlyFansin RTMP ingest rajoittaa videon bitraten noin 2 500 Kbps:ään — tiukempi kuin useimmat cam-sivut. Tähtää 720p–1080p:hen ~2 000–2 500:lla."),
         _T_ETH,
     ],
     "faq": [
         ("Miten yhdistän OnlyFansin SplitCamiin?", "Kahdella tavalla. <strong>Valtuutus</strong> — Stream Settings → Add Channel → OnlyFans → kirjaudu OnlyFans-tilillä ja SplitCam hakee avaimen automaattisesti. Tai <strong>Stream Key</strong> — kopioi OBS Key OnlyFans → Profile → Settings → Other -kohdasta ja liitä."),
         ("Voinko muuttaa OnlyFans-liven asetuksia avaamatta sivustoa?", "Kyllä — Valtuutus-tavalla SplitCam pysyy liitettynä OnlyFans-tiliisi, joten avain ja asetukset synkronoituvat automaattisesti. Muutat kaiken SplitCamissa lähetyksen aikana tai sen jälkeen, käymättä onlyfans.com:issa."),
         ("Mikä bitrate OnlyFansille?", "Kohtuullinen — OnlyFansin RTMP ingest rajoittaa bitraten noin 2 500 Kbps:ään, paljon tiukempi kuin muut cam-alustat. Tähtää 720p–1080p:hen noin 2 000–2 500 Kbps."),
         ("Onko SplitCam ilmainen OnlyFans-liveen?", "Kyllä — ilmainen, ilman vesileimaa ja ilman aikarajaa. Ei kustannuksia enkooderin puolelta."),
     ]},
    {"slug": "camplace", "name": "CamPlace",
     "title": "Lähetys CamPlace:ssä SplitCamilla — Ilmainen opas",
     "desc": "Lähetys CamPlace:ssä ilmaisella SplitCamilla — ulkoinen enkooderi, RTMP-avain, näkymät ja overlayt. Vaihe vaiheelta, ei vesileimaa.",
     "kw": "camplace lähetys, camplace broadcasting software, camplace rtmp, camplace external encoder, camplace stream key",
     "h1html": 'Miten lähetät <span class="accent">CamPlace</span>:ssä SplitCamilla',
     "h1short": "Lähetys CamPlace",
     "card": "Ulkoinen enkooderi CamPlace-streameille.",
     "intro": "CamPlace on cam-streaming-alusta. Julkista OBS-artikkelia ei ole, joten <strong style='color:var(--text)'>yllä oleva video-opas</strong> on viittauksesi — ilmainen <strong style='color:var(--text)'>SplitCam</strong> yhdistää vakio-RTMP:llä ja lisää näkymät, overlayt ja AI-taustan, joita peruskamera ei tee.",
     "quick": "Lähetys CamPlace:ssä SplitCamilla: asenna SplitCam, rakenna näkymä, aktivoi ulkoinen/RTMP-lähetys CamPlace:ssä, kopioi palvelin-URL ja stream key, liitä SplitCamiin, Go Live. Seuraa videota nykyiselle reitille."
              "<ol><li>Asenna SplitCam.</li><li>Lisää kamera + näkymä.</li>"
              "<li>Hanki RTMP-avain CamPlace:stä.</li><li>Liitä SplitCamiin.</li>"
              "<li>Paina Go Live.</li></ol>",
     "key_how": "Kirjaudu CamPlace:hen ja avaa lähetysasetukset. Vaihda ulkoinen enkooderi / RTMP / OBS -vaihtoehtoon paljastaaksesi <strong>palvelin-URL</strong>:n ja <strong>stream keyn</strong>, kopioi molemmat. CamPlace ei julkaise virallista OBS-dokumentaatiota — <strong>yllä oleva video</strong> on luotettavin vaihe vaiheelta -reitti nykyisessä käyttöliittymässä.",
     "tips": [
         ("Ei virallista OBS-opasta — käytä videota", "CamPlace:llä ei ole julkista artikkelia ulkoisista enkoodereista; yllä oleva video on viite nykyiselle reitille."),
         ("Vakio-RTMP toimii", "Vaikka dokumentoimatonta, CamPlace hyväksyy vakio-RTMP-palvelin-URL:n ja avaimen — SplitCam yhdistää mukautettuna RTMP-kohteena."),
         ("Pinota overlayt SplitCamissa", "Tip-tavoitteet, nimi ja sosiaalisen median tunnisteet näkymäkerroksina — CamPlace:n peruskamera ei lisää tällaisia."),
         _T_ETH,
     ],
     "faq": [
         ("Onko CamPlace:llä virallinen OBS-opas?", "Julkista artikkelia ulkoisista enkoodereista ei löytynyt. CamPlace hyväksyy vakio-RTMP-URL:n ja avaimen, joten SplitCam toimii — seuraa videota."),
         ("Tukeeko CamPlace ulkoisia enkoodereita?", "Kyllä — se hyväksyy vakio-RTMP stream keyn, joten SplitCam yhdistää mukautettuna RTMP-kohteena."),
         ("Mikä bitrate CamPlace:lle?", "CamPlace ei julkaise virallista numeroa — käytä 3 500–6 000 Kbps:ää 1080p:ssä turvallisena alueena ja anna SplitCamin nopeustestin määrittää todellinen kattosi."),
         ("Onko SplitCam ilmainen CamPlace:lle?", "Kyllä — ilmainen, ilman vesileimaa ja ilman aikarajaa. Koska CamPlace ei tuo omaa enkooderia, ilmainen RTMP-työkalu hoitaa työn."),
     ]},
    {"slug": "camsoda", "name": "CamSoda",
     "title": "CamSoda live SplitCamilla — Ilmainen asetus",
     "desc": "CamSoda live ilmaisella SplitCamilla — Use OBS Broadcaster, alueelliset palvelimet, näkymät ja overlayt. Ei vesileimaa.",
     "kw": "camsoda live, camsoda lähetys, camsoda obs broadcaster, camsoda rtmp obs, camsoda live broadcast",
     "h1html": 'Miten lähetät <span class="accent">CamSoda</span>ssa SplitCamilla',
     "h1short": "Lähetys CamSoda",
     "card": "Use OBS Broadcaster -asetus CamSoda:ssa.",
     "intro": "CamSoda on yhdysvaltalainen cam-alusta, joka tunnetaan interaktiivisista ja epätavallisista show-muodoista. Se tukee OBS-streamingiä virallisesti — Go Live -sivulla on <strong style='color:var(--text)'>Use OBS Broadcaster</strong> -painike ja virallinen OBS-opas CamSoda-wikissä. Ilmainen <strong style='color:var(--text)'>SplitCam</strong> toimii samalla tavalla.",
     "quick": "Lähetys CamSoda:ssa SplitCamilla: asenna SplitCam, rakenna näkymä, klikkaa Use OBS Broadcaster CamSoda:n Go Live -sivulla, kopioi palvelin-URL ja stream key, liitä SplitCamiin, Go Live."
              "<ol><li>Asenna SplitCam.</li><li>Lisää kamera + näkymä.</li>"
              "<li>Klikkaa Use OBS Broadcaster CamSoda:ssa.</li>"
              "<li>Liitä palvelin-URL + avain SplitCamiin.</li><li>Paina Go Live.</li></ol>",
     "key_how": "CamSoda:n <strong>Go Live</strong> -sivulla klikkaa <strong>Use OBS Broadcaster</strong>. CamSoda näyttää RTMP-palvelin-URL:n ja stream keyn — kopioi molemmat. Valitse alueellinen palvelin (Pohjois-Amerikka, Eurooppa, Aasia jne.), joka on lähimpänä. CamSoda-wikissä on täydellinen OBS-opas yksityiskohtia varten.",
     "tips": [
         ("Varmenna saadaksesi tippejä", "CamSoda:ssa kuka tahansa voi lähettää, mutta tippien saamiseksi sinun on suoritettava CamSoda-varmennusprosessi."),
         ("Valitse lähin alueellinen palvelin", "CamSoda tarjoaa alueellisia ingest-palvelimia — lähin (NA / Eurooppa / Aasia / Etelä-Amerikka / Oseania) vähentää latenssia ja menetettyjä frameja."),
         ("Katto 1080p:ssä / 30 fps:ssä", "CamSoda:n ingest menee ~1080p:hen, 30 fps:ään ja ~6 000 Kbps:ään — älä pakota korkeammalle."),
         _T_ETH,
     ],
     "faq": [
         ("Tukeeko CamSoda OBS:ää / ulkoisia enkoodereita?", "Kyllä — virallisesti. Go Live -sivulla on Use OBS Broadcaster -painike ja OBS-opas CamSoda-wikissä, joten SplitCam toimii."),
         ("Pitääkö CamSoda varmentaa?", "Lähettämistä varten ei. Tippien saamiseksi kyllä — CamSoda vaatii ensin varmennusprosessin suorittamisen."),
         ("Mitä resoluutiota CamSoda tukee?", "1920×1080 asti 30 fps:llä, noin 6 000 Kbps maksimi RTMP ingestissä."),
         ("Onko SplitCam ilmainen CamSoda:lle?", "Kyllä — ilmainen, ilman vesileimaa ja ilman aikarajaa. Toimii CamSoda:n ilmaisen Use OBS Broadcaster -tilan kanssa, joten koko ketju ei maksa mitään."),
     ]},
    {"slug": "streamate", "name": "Streamate",
     "title": "Lähetys Streamate:ssa SplitCamilla — Integroitu kanava",
     "desc": "Lähetys Streamate:ssa ilmaisella SplitCamilla — integroitu kanava, SM Connect -avain, näkymät ja overlayt. Ei vesileimaa.",
     "kw": "streamate, streamate sm connect, streamate lähetys, streamate broadcasting software, streamate rtmp",
     "h1html": 'Miten lähetät <span class="accent">Streamate</span>:ssa SplitCamilla',
     "h1short": "Lähetys Streamate",
     "card": "Streamate on integroitu kanava SplitCamissa — nopea asetus.",
     "intro": "Streamate on vakiintunut cam-alusta — ja se on yksi <strong style='color:var(--text)'>SplitCamiin esiasetetuista kohteista</strong>, kanavaluettelossa, joten asetus on nopeampi kuin manuaalinen RTMP-syöttö: valitset Streamaten, liität avaimen, valmis.",
     "quick": "Lähetys Streamate:ssa SplitCamilla: asenna SplitCam, rakenna näkymä, Streamate:ssa käytä <em>SM Connect → Start Show</em>:ta ja kopioi avain, sitten SplitCamissa avaa <em>Stream Settings → Add Channel → Streamate</em> ja liitä."
              "<ol><li>Asenna SplitCam.</li><li>Lisää kamera + näkymä.</li>"
              "<li>Hanki Streamate-avain SM Connect -kautta.</li>"
              "<li>Add Channel → Streamate SplitCamissa.</li><li>Paina Go Live.</li></ol>",
     "key_how": "Streamate:ssa avaa <strong>SM Connect</strong>, hyväksy ehdot, klikkaa <strong>Start Show</strong> vasemmalla ja sulje aukeava ikkuna — sitten kopioi streaming-avain. SplitCamissa avaa <strong>Stream Settings</strong> → <strong>Add Channel</strong>, valitse <strong>Streamate</strong> listalta ja liitä avain. Vihreä slider vahvistaa yhteyden.",
     "tips": [
         ("Streamate on integroitu", "Ei manuaalista RTMP-URL:ää — SplitCamissa on Streamate Add Channel -listassa; vain valitset ja liität avaimen."),
         ("Sulje SM Connect -popup", "Start Show'n jälkeen Streamate avaa ikkunan — sulje se; se oli vain streaming-avaimen paljastamista varten."),
         ("Lukitse resoluutio 1080p:hen", "SM Connect:in Video Resolution -kenttä voi hiljaisesti hypätä 1440:een, mitä ei käytännössä toimiteta, ja se heikentää laatuasi äänettömästi — aseta manuaalisesti 1080p. Bitrate, joka putoaa staattisessa kuvassa, on normaalia: Streamaten stream on adaptiivinen."),
         _T_ETH, _T_TEST,
     ],
     "faq": [
         ("Onko Streamate integroitu SplitCamiin?", "Kyllä — Streamate näkyy SplitCamin Add Channel -listalla; valitset sen sen sijaan, että kirjoittaisit RTMP-URL:n käsin."),
         ("Missä Streamate streaming-avain on?", "SM Connect → hyväksy ehdot → Start Show → sulje popup → kopioi avain."),
         ("Mikä bitrate Streamate:lle?", "Streamate ei aseta kovaa kattoa — 3 500–6 000 Kbps 1080p:ssä toimii hyvin. Stream on adaptiivinen, joten matalampi bitrate staattisessa kuvassa on normaalia, ei bugi."),
         ("Onko SplitCam ilmainen Streamate:lle?", "Kyllä — ilmainen, ilman vesileimaa ja ilman aikarajaa; ja koska Streamate on integroitu kanava SplitCamissa, ei myöskään ole erillistä enkooderikulua."),
     ]},
    {"slug": "streamray", "name": "StreamRay",
     "title": "Lähetys StreamRay cam:issa SplitCamilla — Chat-URL",
     "desc": "Lähetys StreamRay cam:issa ilmaisella SplitCamilla — URL chattiin postattu, OBS Broadcaster -tila, näkymät ja overlayt. Ei vesileimaa.",
     "kw": "streamray, streamray cam, streamray lähetys, streamray obs broadcaster, streamray rtmp",
     "h1html": 'Miten lähetät <span class="accent">StreamRay</span>:ssä SplitCamilla',
     "h1short": "Lähetys StreamRay",
     "card": "URL-chatissa ulkoinen enkooderi StreamRay:lle.",
     "intro": "StreamRay:llä on epätavallinen ulkoisen enkooderin asetus — se toimittaa stream-URL:n <strong style='color:var(--text)'>lähetyksen chat-ikkunaan</strong> eikä käytä erillistä stream keyä. Ilmainen <strong style='color:var(--text)'>SplitCam</strong> käsittelee tätä vain-URL-virtaa.",
     "quick": "Lähetys StreamRay:ssä SplitCamilla: asenna SplitCam, rakenna näkymä, StreamRay:ssä aktivoi OBS Broadcaster, kopioi stream-URL chat-ikkunasta, liitä SplitCamiin (jätä avainkenttä tyhjäksi), Go Live."
              "<ol><li>Asenna SplitCam.</li><li>Lisää kamera + näkymä.</li>"
              "<li>Kopioi StreamRay-URL chatista.</li>"
              "<li>Liitä URL SplitCamiin.</li><li>Paina Go Live.</li></ol>",
     "key_how": "StreamRay:ssä tuplaklikkaa <strong>Broadcast Now</strong>, avaa <strong>Other</strong>-valikko, valitse <strong>OBS Broadcaster</strong> ja <strong>Save and Close</strong>. StreamRay postaa sitten <strong>stream-URL:n chat-ikkunaan</strong> — kopioi sieltä. Jätä SplitCamin stream key -kenttä <strong>tyhjäksi</strong>; StreamRay todentaa vain URL:lla.",
     "tips": [
         ("URL on chatissa", "StreamRay ei näytä stream-URL:ää asetusruudussa — se postaa sen lähetyksen chat-ikkunaan. Kopioi sieltä."),
         ("Jätä avainkenttä tyhjäksi", "StreamRay ei käytä erillistä avainta — vain URL:n. Älä laita mitään SplitCamin avainkenttään."),
         _T_ETH, _T_TEST,
     ],
     "faq": [
         ("Missä StreamRay stream-URL on?", "OBS Broadcaster -aktivoinnin jälkeen StreamRay postaa URL:n chat-ikkunaan — kopioi chatista."),
         ("Miksi StreamRay:ssä ei ole stream keyä?", "StreamRay todentaa vain URL:lla — jätä SplitCamin avainkenttä tyhjäksi."),
         ("Mikä bitrate StreamRay:lle?", "StreamRay ei ilmoita virallista kattoa — tähtää 3 500–6 000 Kbps:ään 1080p:ssä ja aja SplitCamin nopeustesti, koska vain-URL-virta ei anna bitrate-palautetta."),
         ("Onko SplitCam ilmainen StreamRay:lle?", "Kyllä — ilmainen, ilman vesileimaa ja ilman aikarajaa, mikä sopii StreamRay:n vain-URL-virtaan: liität linkin ja olet livenä."),
     ]},
    {"slug": "xlovecam", "name": "XLoveCam",
     "title": "Lähetys XLoveCam:issa SplitCamilla — RTMP-linkki & avain",
     "desc": "Lähetys XLoveCam:issa ilmaisella SplitCamilla — RTMP-linkki ja avain, alueelliset palvelimet, näkymät ja overlayt. Ei vesileimaa.",
     "kw": "xlovecam, x love cam, xlovecam lähetys, xlovecam rtmp link, xlovecam stream key",
     "h1html": 'Miten lähetät <span class="accent">XLoveCam</span>:issa SplitCamilla',
     "h1short": "Lähetys XLoveCam",
     "card": "RTMP-linkki + avain XLoveCam:ille.",
     "intro": "XLoveCam on eurooppalainen monikielinen cam-alusta. Tiliasetukset näyttävät sekä <strong style='color:var(--text)'>RTMP-linkin</strong> että <strong style='color:var(--text)'>stream keyn</strong> — ilmainen <strong style='color:var(--text)'>SplitCam</strong> ottaa molemmat ja lähettää täysillä näkymillä ja overlayilla.",
     "quick": "Lähetys XLoveCam:issa SplitCamilla: asenna SplitCam, rakenna näkymä, XLoveCam:issa avaa <em>My Account → settings</em>, kopioi RTMP-linkki ja stream key, liitä molemmat SplitCamiin, aloita show."
              "<ol><li>Asenna SplitCam.</li><li>Lisää kamera + näkymä.</li>"
              "<li>Kopioi RTMP-linkki + avain XLoveCam:ista.</li><li>Liitä molemmat SplitCamiin.</li>"
              "<li>Paina Go Live.</li></ol>",
     "key_how": "XLoveCam:issa avaa <strong>My Account</strong> → <strong>settings</strong>. Asetukset näyttävät sekä <strong>RTMP-linkin</strong> että <strong>stream keyn</strong> — kopioi molemmat SplitCamin palvelin-URL- ja avainkenttiin, sitten <strong>Start your show</strong> XLoveCam:issa.",
     "tips": [
         ("Kopioi linkki JA avain", "XLoveCam antaa RTMP-linkin JA erillisen stream keyn — tarvitset molemmat SplitCamissa, et vain yhtä."),
         ("Monikielinen yleisö", "XLoveCam on eurooppalainen ja monikielinen — selkeä tekstioverlay omalla kielelläsi auttaa katsojia löytämään sinut."),
         ("Valitse lähin palvelin", "XLoveCam tarjoaa alueellisia RTMP-palvelimia — Eurooppa, Pohjois-Amerikka, Etelä-Amerikka ja Aasia. Lähin vähentää latenssia ja menetettyjä frameja."),
         _T_ETH,
     ],
     "faq": [
         ("Missä XLoveCam:in RTMP-tiedot ovat?", "My Account → settings — näyttää sekä RTMP-linkin että avaimen."),
         ("Tukeeko XLoveCam ulkoisia enkoodereita?", "Kyllä — se tarjoaa RTMP-linkin ja avaimen, joten SplitCam toimii enkooderina."),
         ("Mikä bitrate XLoveCam:ille?", "XLoveCam ei julkaise kiinteää rajaa; 3 500–6 000 Kbps 1080p:ssä on ihanteellinen. Lähimmän alueellisen palvelimen valinta on yhtä tärkeää — vähentää menetettyjä frameja."),
         ("Onko SplitCam ilmainen XLoveCam:ille?", "Kyllä — ilmainen, ilman vesileimaa ja ilman aikarajaa. XLoveCam:in monikielisen eurooppalaisen yleisön tavoittaminen ei maksa ohjelmistossa."),
     ]},
    {"slug": "soulcams", "name": "SoulCams",
     "title": "Lähetys SoulCams:issa SplitCamilla — OBS-asetukset",
     "desc": "Lähetys SoulCams:issa ilmaisella SplitCamilla — OBS-asetukset, RTMP-palvelin ja avain, monikamera-näkymät ja overlayt.",
     "kw": "soul cams, soulcams, soulcams lähetys, soulcams obs, soulcams rtmp, soulcams broadcast",
     "h1html": 'Miten lähetät <span class="accent">SoulCams</span>:issa SplitCamilla',
     "h1short": "Lähetys SoulCams",
     "card": "OBS-asetukset SoulCams:ille.",
     "intro": "SoulCams on cam-alusta, jonka OBS-asetukset näyttävät <strong style='color:var(--text)'>RTMP-palvelimen ja stream keyn yhdessä</strong> yhdessä ikkunassa. Liitä molemmat ilmaiseen <strong style='color:var(--text)'>SplitCamiin</strong>, jotta voit lähettää monikamera-näkymillä ja overlayilla.",
     "quick": "Lähetys SoulCams:issa SplitCamilla: asenna SplitCam, rakenna näkymä, SoulCams:issa klikkaa Go Online → Settings → OBS, kopioi palvelin ja avain, liitä molemmat SplitCamiin, Go Live."
              "<ol><li>Asenna SplitCam.</li><li>Lisää kamera + näkymä.</li>"
              "<li>Avaa SoulCams Settings → OBS.</li><li>Liitä palvelin + avain SplitCamiin.</li>"
              "<li>Paina Go Live.</li></ol>",
     "key_how": "SoulCams:issa kirjaudu sisään ja klikkaa <strong>Go Online</strong>, sitten avaa <strong>Settings</strong> → <strong>OBS</strong>. OBS-ikkuna näyttää <strong>RTMP-palvelimen</strong> ja <strong>stream keyn</strong> yhdessä — kopioi molemmat SplitCamiin.",
     "tips": [
         ("Palvelin ja avain rinnakkain", "SoulCams näyttää RTMP-palvelimen ja avaimen samassa OBS-ikkunassa — otat molemmat yhdellä kertaa."),
         ("Ensin Go Online", "OBS-asetukset näkyvät vasta Go Online -klikkauksen jälkeen SoulCams:issa — tee se ennen enkooderitietojen etsimistä."),
         ("Estä ei-toivotut alueet", "SoulCams sallii geo-eston mallin puolelta — valitse, mitkä maat eivät voi nähdä lähetystä, ennen kuin painat Go Online."),
         _T_ETH, _T_TEST,
     ],
     "faq": [
         ("Missä SoulCams:in OBS-asetukset ovat?", "Kirjaudu sisään, klikkaa Go Online, sitten Settings → OBS — RTMP-palvelin ja stream key näytetään yhdessä."),
         ("Tukeeko SoulCams ulkoisia enkoodereita?", "Kyllä — OBS-asetukset antavat RTMP-palvelimen ja avaimen, joten SplitCam toimii."),
         ("Mikä bitrate SoulCams:ille?", "SoulCams ei anna virallista numeroa — tähtää 3 500–6 000 Kbps:ään 1080p:ssä ja testaa upload, koska OBS-ikkuna ei näytä bitrate-ohjetta."),
         ("Onko SplitCam ilmainen SoulCams:ille?", "Kyllä — ilmainen, ilman vesileimaa ja ilman aikarajaa, joten täysi SoulCams-show monikamera-näkymillä ja overlayilla ei maksa mitään enkooderin puolelta."),
     ]},
    {"slug": "imlive", "name": "ImLive",
     "title": "Lähetys ImLivessä SplitCamilla — Virtuaalikamera",
     "desc": "Im Live stream -asetus ilmaisella SplitCamilla — ImLive käyttää webkameraa suoraan (ei RTMP), yhdistä SplitCam virtuaalikamerana näkymillä.",
     "kw": "im live stream, imlive splitcam, imlive lähetys, imlive virtuaalikamera, imlive webcam, im live cam",
     "h1html": 'Miten käytät <span class="accent">ImLiveä</span> SplitCamilla',
     "h1short": "SplitCam ImLivessä",
     "card": "Virtuaalikamera ImLivelle — ei RTMP:tä.",
     "intro": "ImLive käyttää webkameraa suoraan selaimessa — <strong style='color:var(--text)'>ei RTMP:tä eikä stream keyä</strong>. Ilmainen <strong style='color:var(--text)'>SplitCam</strong> yhdistää <strong style='color:var(--text)'>virtuaalikamerana</strong>: rakennat näkymän SplitCamissa, sitten valitset SplitCamin kameraksi ImLivessä.",
     "quick": "SplitCam ImLivessä: asenna SplitCam, rakenna näkymä mediakerroksilla, avaa ImLive ja aloita videochat, ImLive-asetuksissa valitse SplitCam webkameraksi ja mikrofoniksi."
              "<ol><li>Asenna SplitCam.</li><li>Rakenna näkymä SplitCamissa.</li>"
              "<li>Aloita videochat ImLivessä.</li>"
              "<li>Valitse SplitCam ImLive-kameraksi.</li><li>Aloita chat.</li></ol>",
     "steps": [
         ("Asenna SplitCam",
          "SplitCam on ilmainen ohjelmisto Windowsille ja macOS:lle. Asenna — ilman vesileimaa, ilman rekisteröintiä. ImLivelle se toimii <strong>virtuaalikamerana</strong>, ei RTMP-enkooderina."),
         ("Rakenna näkymä SplitCamissa",
          "Avaa SplitCam ja käytä <strong>Media Layers +</strong> -toimintoa lisätäksesi webkameran sekä kaikki overlayt, tekstit, suodattimet tai AI-taustan. Tämä yhdistetty näkymä on se, mitä ImLive näkee kamerana."),
         ("Aloita videochat ImLivessä",
          "Kirjaudu ImLive-sivulle ja klikkaa <strong>Start Video Chat</strong>, sitten avaa <strong>Go To Settings</strong> päästäksesi kamera- ja mikrofoniasetuksiin."),
         ("Valitse SplitCam kameraksi",
          "ImLive-asetuksissa valitse <strong>SplitCam</strong> webkameraksi JA mikrofoniksi. ImLive näyttää nyt täyden SplitCam-näkymän litteän webkameran sijaan."),
         ("Aloita Free Live Chat",
          "Klikkaa <strong>Free Live Chat</strong> ImLivessä mennäksesi livenä. Ulkoasun muuttamiseksi keskellä istuntoa muokkaa näkymää SplitCamissa — ImLive päivittyy heti."),
     ],
     "tips": [
         ("Ei stream keyä tarvita", "ImLivellä ei ole RTMP:tä — älä etsi palvelin-URL:ää tai avainta. SplitCam vain valitaan kameralaitteeksi."),
         ("Aseta SplitCam myös mikrofoniksi", "Valitse SplitCam mikrofoniksi kameran lisäksi, jotta audiomix ja kohinanpoisto myös pääsevät liveen."),
         ("Rakenna näkymä ennen liveä", "ImLive näyttää sen, mitä SplitCam lähettää — järjestele kerrokset ennen chatin aloittamista."),
         _T_TEST,
     ],
     "faq": [
         ("Käyttääkö ImLive RTMP:tä vai stream keyä?", "Ei — ImLive käyttää webkameraa suoraan selaimen kautta. SplitCam yhdistää virtuaalikamerana, ei avainta kopioitavaksi."),
         ("Miten valitsen SplitCamin ImLivessä?", "Start Video Chat → Go To Settings → valitse SplitCam webkameraksi ja mikrofoniksi."),
         ("Voinko käyttää overlayitä ImLivessä?", "Kyllä — rakennat ne SplitCam-näkymässä; ImLive näyttää yhdistetyn tuloksen."),
         ("Onko SplitCam ilmainen ImLivelle?", "Kyllä — ilmainen, ilman vesileimaa ja ilman aikarajaa. Virtuaalikamerana ImLivelle se ei lisää kustannuksia tai brändäystä videochat-yhteyteesi."),
     ]},
    {"slug": "vxlive", "name": "VXLive",
     "title": "Lähetys VXLivessä SplitCamilla — Virallinen tuki",
     "desc": "Lähetys VXLivessä (VXModels / VISIT-X) ilmaisella SplitCamilla — virallinen VISIT-X preset, palvelin ja avain, näkymät. Ei vesileimaa.",
     "kw": "vxlive, visit-x, vxmodels splitcam, vxlive lähetys, visit-x stream, vxlive rtmp",
     "h1html": 'Miten lähetät <span class="accent">VXLivessä</span> SplitCamilla',
     "h1short": "Lähetys VXLive",
     "card": "VXLive tukee SplitCamia virallisesti (VISIT-X preset).",
     "intro": "VXLive (VXModels / VISIT-X) on cam-alusta Saksan markkinoilta — ja yksi harvoista, joka <strong style='color:var(--text)'>tukee SplitCamia virallisesti nimeltä</strong>. VXModelsilla on omistettu ohjeartikkeli <strong style='color:var(--text)'>SplitCamin</strong> yhdistämiseen VXLiveen, ja SplitCam tarjoaa VISIT-X:n valmiina kanava-presetinä.",
     "quick": "Lähetys VXLivessä SplitCamilla: asenna SplitCam, rakenna näkymä, VXLivessä valitse «Stream with third-party software», kopioi palvelin-URL ja avain, SplitCamissa valitse VISIT-X preset ja liitä, Go Live SplitCamissa, sitten GO ONLINE VXLivessä."
              "<ol><li>Asenna SplitCam.</li><li>Lisää kamera + näkymä.</li>"
              "<li>Hanki palvelin-URL + avain VXLivestä.</li>"
              "<li>Valitse VISIT-X preset SplitCamissa, liitä.</li>"
              "<li>Go Live, sitten GO ONLINE VXLivessä.</li></ol>",
     "key_how": "VXLivessä valitse <strong>Stream with third-party software</strong> ja valitse vaihtoehto <strong>OBS, SplitCam tai XSplit</strong>. VXLive tarjoaa <strong>palvelin-URL:n</strong> ja <strong>stream keyn</strong>. SplitCamissa valitse <strong>VISIT-X</strong> streaming-alustaksi, liitä molemmat, paina <strong>Go Live</strong> SplitCamissa, sitten <strong>GO ONLINE</strong> VXLivessä.",
     "tips": [
         ("VISIT-X on integroitu preset", "Älä kirjoita raakaa RTMP-URL:ää — SplitCamissa on VISIT-X alustojen luettelossa; vain valitset ja liität palvelin-URL:n ja avaimen."),
         ("Kaksivaiheinen go-live", "VXLivessä paina Go Live SplitCamissa ensin, sitten GO ONLINE VXLivessä — molemmat, tässä järjestyksessä."),
         ("Saksan markkinat", "VXLiven yleisö on enimmäkseen saksankielinen — saksankielinen tekstioverlay tai otsikko auttaa yhteyden luomista katsojiin."),
         _T_ETH,
     ],
     "faq": [
         ("Tukeeko VXLive SplitCamia virallisesti?", "Kyllä — VXModels (VXLive) ylläpitää omistettua virallista ohjeartikkelia SplitCam-asetukselle ja listaa SplitCamin OBS:n ja XSplitin rinnalla tuettuna broadcasting-ohjelmistona."),
         ("Miten yhdistän SplitCamin VXLiveen?", "VXLivessä valitset «Stream with third-party software», sitten SplitCamissa valitset VISIT-X presetin ja liität VXLiven antaman palvelin-URL:n ja stream keyn."),
         ("Menenkö livenä SplitCamissa vai VXLivessä?", "Molemmissa — ensin Go Live SplitCamissa, sitten GO ONLINE VXLivessä."),
         ("Miksi VXModels suosittelee SplitCamia?", "VXModelsin virallinen ohjeartikkeli suosittelee SplitCamia erityisesti webkameran kuva-artefaktien ja pikselöinnin eliminointiin ja yhteyden vakauttamiseen — ei vain yleisenä enkooderina."),
     ]},
    {"slug": "virtwish", "name": "VirtWish",
     "title": "Lähetys VirtWishissä SplitCamilla — Stream-URL & avain",
     "desc": "Lähetys VirtWishissä ilmaisella SplitCamilla — Profile → Start Broadcast OBS-osio, stream-URL ja avain, näkymät ja overlayt.",
     "kw": "virtwish, virtwish lähetys, virtwish broadcasting software, virtwish rtmp, virtwish stream key, virtwish obs",
     "h1html": 'Miten lähetät <span class="accent">VirtWishissä</span> SplitCamilla',
     "h1short": "Lähetys VirtWish",
     "card": "Stream-URL + avain VirtWishille.",
     "intro": "VirtWish on interaktiivinen cam-alusta. Lähetysasetukset antavat sinulle <strong style='color:var(--text)'>stream-URL:n ja erillisen stream keyn</strong> OBS-osiossa — ilmainen <strong style='color:var(--text)'>SplitCam</strong> ottaa molemmat ja pyörittää shown näkymillä ja overlayilla.",
     "quick": "Lähetys VirtWishissä SplitCamilla: asenna SplitCam, rakenna näkymä, VirtWishissä avaa <em>Profile → Start Broadcast</em> OBS-osioon, kopioi linkki ja avain, liitä molemmat SplitCamiin, Go Live."
              "<ol><li>Asenna SplitCam.</li><li>Lisää kamera + näkymä.</li>"
              "<li>Hanki URL + avain VirtWishistä.</li><li>Liitä molemmat SplitCamiin.</li>"
              "<li>Paina Go Live.</li></ol>",
     "key_how": "VirtWishissä klikkaa oikean yläkulman kuvaketta → <strong>Profile</strong> → <strong>Start Broadcast</strong>, sitten <strong>Start Broadcast</strong> uudelleen päästäksesi OBS-osioon. <strong>Kopioi ensimmäisen rivin linkki</strong> SplitCamin Stream URL -kenttään, ja <strong>Stream Key</strong> erikseen avainkenttään.",
     "tips": [
         ("Linkki ensimmäisellä rivillä", "VirtWishin OBS-osio asettaa stream-URL:n ensimmäiselle riville — kopioi SplitCamin Stream URL:iin, sitten erillinen avain."),
         ("Kaksi klikkausta Start Broadcastissa", "Klikkaat Start Broadcast kahdesti VirtWishissä päästäksesi OBS-osioon — odotettu, ei bugi."),
         _T_ETH, _T_TEST,
     ],
     "faq": [
         ("Missä VirtWishin RTMP-tiedot ovat?", "Oikean yläkulman kuvake → Profile → Start Broadcast kahdesti → OBS-osio näyttää linkin ja stream keyn."),
         ("Tukeeko VirtWish ulkoisia enkoodereita?", "Kyllä — OBS-osio tarjoaa stream-URL:n ja avaimen, joten SplitCam toimii."),
         ("Mikä bitrate VirtWishille?", "VirtWish ei julkaise virallista kattoa; 3 500–6 000 Kbps 1080p:ssä on turvallista. Sovita SplitCamin resoluutio VirtWishissä asetettuun välttääksesi rescalingin."),
         ("Onko SplitCam ilmainen VirtWishille?", "Kyllä — ilmainen, ilman vesileimaa ja ilman aikarajaa. VirtWishin URL-ja-avain-asetus maksaa vain siihen tarvittavat minuutit."),
     ]},
    {"slug": "xmodels", "name": "XModels",
     "title": "Lähetys XModelsissa SplitCamilla — Ilmainen opas",
     "desc": "Lähetys XModelsissa ilmaisella SplitCamilla — ulkoisen enkooderin vaihtoehto mallitilin asetuksissa, RTMP-avain, näkymät ja overlayt.",
     "kw": "xmodels, xmodels lähetys, xmodels broadcasting software, xmodels rtmp, xmodels external encoder",
     "h1html": 'Miten lähetät <span class="accent">XModelsissa</span> SplitCamilla',
     "h1short": "Lähetys XModels",
     "card": "Ulkoinen enkooderi XModels-streameille.",
     "intro": "XModels on cam-streaming-alusta sisäänrakennetulla <strong style='color:var(--text)'>ulkoisen enkooderin vaihtoehdolla</strong> mallitilin asetuksissa. Ilmainen <strong style='color:var(--text)'>SplitCam</strong> lähettää siellä monikamera-näkymillä, overlayilla ja suodattimilla yksittäisen litteän kameran sijaan.",
     "quick": "Lähetys XModelsissa SplitCamilla: asenna SplitCam, rakenna näkymä, XModels-mallitilillä aktivoi ulkoisen enkooderin vaihtoehto, kopioi palvelin-URL ja stream key, liitä SplitCamiin, Go Live."
              "<ol><li>Asenna SplitCam.</li><li>Lisää kamera + näkymä.</li>"
              "<li>Aktivoi ulkoinen enkooderi XModels-asetuksissa.</li>"
              "<li>Liitä palvelin-URL + avain SplitCamiin.</li><li>Paina Go Live.</li></ol>",
     "key_how": "XModelsin <strong>mallitilin asetuksissa</strong> aktivoi <strong>ulkoisen enkooderin lähetys</strong> -vaihtoehto. XModels tarjoaa <strong>stream keyn</strong> — kopioi SplitCamiin. Jos vaihtoehto ei ole odottamassasi paikassa, XModelsin tuki on FAQ-chatissa sivustolla ja <strong>info@xmodels.com</strong>:issa; yllä oleva video näyttää sen myös.",
     "tips": [
         ("Se on tilin asetuksissa", "XModels asettaa ulkoisen enkooderin vaihtoehdon mallitilin asetuksiin, ei erilliselle lähetysnäytölle."),
         ("Tuki: chat + sähköposti", "XModelsilla ei ole suurta julkista help-keskusta — sivuston FAQ-chat ja info@xmodels.com ovat viralliset tukikanavat."),
         ("Pinota overlayt SplitCamissa", "Tip-tavoitteet, nimi ja sosiaalisen median tunnisteet näkymäkerroksina — XModelsin peruskamera ei lisää tällaisia."),
         _T_ETH,
     ],
     "faq": [
         ("Tukeeko XModels ulkoisia enkoodereita?", "Kyllä — mallitilin asetukset sisältävät ulkoisen enkooderin lähetysvaihtoehdon, joka tarjoaa stream keyn, joten SplitCam toimii."),
         ("Mistä saan XModels-apua?", "XModelsin tuki on sivuston FAQ-chatissa ja info@xmodels.com-sähköpostissa — ei suurta julkista help-keskusta."),
         ("Mikä bitrate XModelsille?", "XModels ei dokumentoi virallista numeroa — käytä 3 500–6 000 Kbps:ää 1080p:ssä ja aja SplitCamin nopeustesti, koska XModelsin tuki on vain chattia ja sähköpostia."),
         ("Onko SplitCam ilmainen XModelsille?", "Kyllä — ilmainen, ilman vesileimaa ja ilman aikarajaa, joten lähettäminen XModelsin eurooppalaiseen verkkoon ei lisää ohjelmistokustannuksia."),
     ]},
    {"slug": "flirt4free", "name": "Flirt4Free",
     "title": "Lähetys Flirt for Free cam:issa SplitCamilla — Ilmainen opas",
     "desc": "Lähetys Flirt for Free cam:issa ilmaisella SplitCamilla — External Broadcast Form, RTMP URL ja Stream Name, näkymät ja overlayt.",
     "kw": "flirt for free cam, flirt 4 free cam, flirt4free, flirt4free lähetys, flirt4free external broadcast, flirt4free rtmp",
     "h1html": 'Miten lähetät <span class="accent">Flirt4Free</span>:ssa SplitCamilla',
     "h1short": "Lähetys Flirt4Free",
     "card": "External Broadcast Form Flirt4Freelle.",
     "intro": "Flirt4Free on yksi vanhimmista cam-alustoista, lähetyksessä 90-luvulta. Tukee ulkoista lähetystä virallisesti <strong style='color:var(--text)'>External Broadcast Form</strong>:in kautta — ilmainen <strong style='color:var(--text)'>SplitCam</strong> lähettää streamin, kun lomake asettaa resoluution ja bitraten.",
     "quick": "Lähetys Flirt4Freessa SplitCamilla: asenna SplitCam, rakenna näkymä, avaa Flirt4Free External Broadcast Form, kopioi RTMP URL ja Stream Name ja aseta resoluutio/bitrate, liitä SplitCamiin, Go Live."
              "<ol><li>Asenna SplitCam.</li><li>Lisää kamera + näkymä.</li>"
              "<li>Avaa Flirt4Free External Broadcast Form.</li>"
              "<li>Liitä RTMP URL + Stream Name SplitCamiin.</li>"
              "<li>Paina Go Live.</li></ol>",
     "key_how": "Flirt4Freen malli-alueella avaa <strong>External Broadcast Form</strong>. Toisin kuin useimmat cam-sivut, Flirt4Free antaa <strong>RTMP URL</strong>:n ja <strong>Stream Namen</strong> (ei «avainta»), sekä resoluutio- ja bitrate-kentät, jotka täytät itse lomakkeessa. Kopioi URL ja Stream Name SplitCamin palvelin- ja avainkenttiin.",
     "tips": [
         ("Se on Stream Name, ei avain", "Flirt4Free kutsuu kredentiaalia Stream Nameksi. Liität sen SplitCamin stream key -kenttään — sama rooli."),
         ("Aseta resoluutio/bitrate lomakkeessa", "Flirt4Freen External Broadcast Formilla on omat resoluutio- ja bitrate-kentät — kohdista SplitCamin asetusten kanssa, jotta kuvaa ei muunneta uudelleen."),
         ("Historiallinen alusta", "Flirt4Free on toiminut 90-luvulta — mallityökalut ovat kypsiä, ja External Broadcast Form on niiden dokumentoitu osa."),
         _T_ETH,
     ],
     "faq": [
         ("Tukeeko Flirt4Free ulkoisia enkoodereita?", "Kyllä — virallisesti, External Broadcast Form:in kautta, joka tarjoaa RTMP URL:n ja Stream Namen. SplitCam toimii enkooderina."),
         ("Mistä saan Flirt4Freen RTMP-tiedot?", "External Broadcast Form:ista malli-alueella — näyttää RTMP URL:n, Stream Namen ja resoluutio/bitrate-kentät."),
         ("Mikä bitrate Flirt4Freelle?", "3 500–6 000 Kbps 1080p:ssä — aseta sama arvo External Broadcast Form:issa ja SplitCamissa."),
         ("Onko SplitCam ilmainen Flirt4Freelle?", "Kyllä — ilmainen, ilman vesileimaa ja ilman aikarajaa, mikä sopii historialliseen alustaan kuten Flirt4Free, jossa shokit voivat olla pitkiä."),
     ]},
    {"slug": "mfc-alerts", "name": "MFC Alerts",
     "title": "MFC Alertsien lisääminen streamiin SplitCamilla",
     "desc": "Näytä animoidut tip-alertit MyFreeCams-streamissä — mfcalerts.com-URL Browser-kerroksena ilmaisessa SplitCamissa, webkameran päällä.",
     "kw": "mfc alerts, myfreecams alerts, mfc alerts lisääminen, mfcalerts splitcam, myfreecams tip alerts, myfreecams alerts overlay",
     "h1html": 'Miten lisäät <span class="accent">MFC Alertsit</span> streamiisi',
     "h1short": "MFC Alertsit lisätään",
     "card": "Näytä animoidut tip-alertit MyFreeCams-streamissä.",
     "intro": "MFC Alerts näyttää animoidut efektit MyFreeCams-streamissäsi aina, kun katsoja lähettää tipin. Toimii <strong style='color:var(--text)'>Browser-kerroksena</strong> ilmaisessa <strong style='color:var(--text)'>SplitCamissa</strong> — asetat kerran ja tipit laukaisevat näytön reaktioita livenä.",
     "quick": "MFC Alertsien lisääminen SplitCamilla: asenna SplitCam, lisää webkamera, avaa Browser-välilehti ja lataa mfcalerts.com, kopioi alerts-URL, lisää Browser-kerroksena webkameran päälle, sitten testaa testi-tippillä."
              "<ol><li>Asenna SplitCam.</li><li>Lisää webkamera.</li>"
              "<li>Hanki URL mfcalerts.com:ista.</li>"
              "<li>Lisää Browser-kerroksena webkameran päälle.</li>"
              "<li>Lähetä testi-tip.</li></ol>",
     "steps": [
         ("Asenna SplitCam ja lisää webkamera",
          "Asenna ilmainen SplitCam Windowsille tai macOS:lle, sitten lisää <strong>webkamera</strong> lähteeksi. MFC Alerts istuu kerroksena tämän kameran päällä."),
         ("Avaa Browser-välilehti ja mene mfcalerts.com:iin",
          "SplitCamissa avaa <strong>Browser</strong>-välilehti ja navigoi <strong>www.mfcalerts.com</strong>:iin. Kirjaudu sisään tai rekisteröidy, jos sinulla ei vielä ole mfcalerts.com-tiliä."),
         ("Kopioi alerts-URL",
          "Mfcalerts.com:issa käytä <strong>Copy to clipboard</strong>:ia kopioidaksesi henkilökohtainen alerts-URL — se on sivu, joka renderöi tip-animaatiot."),
         ("Lisää URL Browser-kerroksena — webkameran päälle",
          "Liitä URL SplitCamin Browser-ikkunaan ja klikkaa <strong>Add</strong>. Sitten järjestele lähdeluettelo siten, että <strong>MFC Alerts on webkameran päällä</strong> (3-pisteinen valikko → Move Up). Jos se istuu alla, efektit pysyvät piilossa."),
         ("Testaa testi-tipillä",
          "Avaa <strong>Settings → Send test tip</strong> ja vahvista, että alert-efekti ilmestyy kameran päälle. Sitten lähetä normaalisti MyFreeCams:iin — todelliset tipit laukaisevat nyt animaatiot."),
     ],
     "tips": [
         ("MFC Alerts on oltava webkameran päällä", "Yleisin virhe: jos MFC Alerts -kerros on webkameran alla lähdeluettelossa, efektit pysyvät piilossa. Siirrä ylös."),
         ("Mfcalerts.com-tili vaadittu", "Alerts-URL on henkilökohtainen — rekisteröidy mfcalerts.com:iin ensin, jos sinulla ei ole tiliä."),
         ("Lähetä testi-tip ennen liveä", "Käytä Settings → Send test tip vahvistaaksesi, että overlay toimii — älä löydä virhettä show:n keskellä."),
         _T_ETH,
     ],
     "faq": [
         ("Mikä on MFC Alerts?", "Ilmoitusjärjestelmä MyFreeCamsille, joka näyttää videoefektejä streamissäsi, kun katsojat lähettävät tippejä — lisätään Browser-overlaynä SplitCamissa."),
         ("Miksi MFC Alertsini eivät näy?", "Lähes aina kerrosjärjestys — MFC Alerts Browser -kerroksen on oltava webkameran päällä SplitCamin lähdeluettelossa."),
         ("Tarvitsenko tilin MFC Alertsiin?", "Kyllä — rekisteröidy mfcalerts.com:iin saadaksesi henkilökohtainen alerts-URL."),
         ("Onko SplitCam ilmainen tähän?", "Kyllä — SplitCam on ilmainen, ilman vesileimaa ja ilman aikarajaa, ja MFC Alerts browser-overlay toimii siinä ilman lisäkustannuksia."),
     ]},
    {"slug": "lovense", "name": "Lovense",
     "title": "Lovense-lelun lisääminen streamiin SplitCamilla",
     "desc": "Interaktiivisen Lovense-lelun yhdistäminen cam-streamiin ilmaisella SplitCamilla — Lovense SplitCam Toolset, näytön tip-alertit, reaktiot.",
     "kw": "lovense lisääminen stream, lovense cam stream, lovense splitcam, lovense splitcam toolset, lovense interactive toy streaming",
     "h1html": 'Miten lisäät <span class="accent">Lovense-lelun</span> streamiisi',
     "h1short": "Lovense-lelun lisääminen",
     "card": "Yhdistä interaktiivinen Lovense-lelu cam-streamiisi.",
     "intro": "Pyörität cam-streamia ilmaisen <strong style='color:var(--text)'>SplitCamin</strong> kautta ja paritat <strong style='color:var(--text)'>Lovense</strong>-lelun, joka reagoi tokeneihin. Lovense dokumentoi virallisen <strong style='color:var(--text)'>Lovense SplitCam Toolsetin</strong>, ja SplitCam tarjoaa virallisen Lovense-pluginin — integraatio on tuettu molemmilta puolilta.",
     "quick": "Lovense-lelun lisäämiseksi streamiin: asenna SplitCam ja Lovense-ohjelmisto, parita lelu, linkitä Lovense cam-alustaan, lisää Lovense-status Browser-kerroksena SplitCamiin, sitten lähetä normaalisti."
              "<ol><li>Asenna SplitCam.</li><li>Asenna Lovense-ohjelmisto ja parita lelu.</li>"
              "<li>Linkitä Lovense cam-sivulle.</li>"
              "<li>Lisää Lovense-overlay SplitCamiin.</li><li>Paina Go Live.</li></ol>",
     "steps": [
         ("Asenna SplitCam",
          "SplitCam on ilmainen streaming-ohjelmisto Windowsille ja macOS:lle — enkooderi, joka lähettää videosi cam-alustalle. Asenna; ilman vesileimaa."),
         ("Asenna Lovense-ohjelmisto ja parita lelu",
          "Asenna Lovense Connect / Lovense Stream (virallinen pöytäkoneapp). Käynnistä lelu ja parita Bluetoothilla niin että app näyttää yhdistetyn."),
         ("Linkitä Lovense cam-alustaan",
          "Lovense-appissa linkitä cam-tilisi, jotta lelu reagoi katsojien tokeneihin / tippeihin. Useimmat suuret cam-alustat tuetaan."),
         ("Lisää Lovense-overlay SplitCamiin",
          "Lovense tarjoaa overlay-/widget-URL:n. Lisää <strong>Browser</strong>-kerroksena SplitCam-näkymään, jotta katsojat näkevät lelun statuksen ja viimeisimmät tipit ruudulla."),
         ("Rakenna näkymä ja Go Live",
          "Lisää kamera ja muut overlayt, liitä cam-alustan RTMP-avain SplitCamiin ja klikkaa <strong>Go Live</strong>. Lelu reagoi tippeihin reaaliajassa."),
     ],
     "tips": [
         ("Käytä virallista Lovense SplitCam Toolsetia", "Lovense julkaisee SplitCam-spesifisen toolsetin omalla asennusohjeellaan — se lisää lelun aktiivisuus-overlayn ja SplitCamille tehdyt tip-alertit."),
         ("Päivitä Lovense Cam Extension", "Toolset vaatii tuoreen Lovense Cam Extensionin (30.1.4 tai uudempi) — päivitä ennen liveä."),
         ("Pidä lelu ladattuna", "Lähes tyhjä akku show:n keskellä tappaa interaktiivisen puolen — lataa täyteen ennen liveä."),
         ("Testaa reaktio tokeneihin", "Lähetä pieni testi-tip vahvistaaksesi, että lelu reagoi, ennen huoneen avaamista."),
         ("Tarkista versiovaatimukset", "Lovense SplitCam Toolset vaatii SplitCam 10.4.5:n tai uudemman. Lovense Cam Extension kattaa virallisesti Chaturbaten, Stripchatin, BongaCamsin, MyFreeCamsin ja CamSoda:n — muiden sivustojen kohdalla käytä Lovensen Generic URL -integraatiota."),
     ],
     "faq": [
         ("Tukeeko Lovense SplitCamia virallisesti?", "Kyllä — Lovense dokumentoi virallisen «Lovense SplitCam Toolsetin» omalla asennusohjeellaan, ja SplitCam tarjoaa virallisen Lovense-pluginin. Integraatio on tuettu molemmilta puolilta."),
         ("Yhdistyykö lelu suoraan SplitCamiin?", "Ei — lelu paritetaan Lovense-appin kanssa; SplitCam näyttää Lovense-overlayn ja lähettää kameran."),
         ("Mitkä cam-sivut tukevat Lovenseä?", "Lovense Cam Extension tukee virallisesti Chaturbatea, Stripchatia, BongaCamsia, MyFreeCamsia ja CamSoda:ta, vaihtelevalla tuella muille — tarkista nykyinen lista Lovense-appista."),
         ("Voinko näyttää viimeisimmät tipit ruudulla?", "Kyllä — lisää Lovensen widget-URL Browser-kerroksena SplitCamiin."),
     ]},
    {"slug": "multistream-cams", "name": "Monta cam-sivua",
     "title": "Lähetys moneen cam-sivuun samanaikaisesti SplitCamilla",
     "desc": "Lähetys MyFreeCams:iin, Chaturbatessa, BongaCams:issa, CAM4:ssä, Stripchatissä ja useampaan samanaikaisesti SplitCamin ilmaisella multistreamingilla. Yksi klikkaus, ei vesileimaa.",
     "kw": "lähetys moneen cam-sivuun, multistream cam sites, lähetys chaturbateen ja bongacamsiin samanaikaisesti, multistream cam ohjelmisto",
     "h1html": 'Miten lähetät <span class="accent">moneen cam-sivuun</span> samanaikaisesti',
     "h1short": "Cam-multistreaming",
     "card": "Lähetys moneen cam-sivuun samanaikaisesti.",
     "intro": "Ilmainen <strong style='color:var(--text)'>SplitCam</strong> voi lähettää yhden koodauksen <strong style='color:var(--text)'>moneen cam-sivuun samanaikaisesti</strong> — MyFreeCams, Chaturbate, BongaCams, CAM4, Stripchat ja muut. Ei vesileimaa, yksi klikkaus.",
     "quick": "Moneen cam-sivuun samanaikaisesti lähettämiseksi: asenna SplitCam, rakenna näkymä, hanki jokaisen cam-sivun RTMP-palvelin-URL ja stream key, lisää kaikki SplitCamin multistreaming-asetuksiin, klikkaa Go Live kerran."
              "<ol><li>Asenna SplitCam.</li><li>Lisää kamera + näkymä.</li>"
              "<li>Hanki RTMP-avain jokaiselta cam-sivulta.</li>"
              "<li>Lisää kaikki avaimet SplitCamin multistreamiin.</li>"
              "<li>Paina Go Live kerran.</li></ol>",
     "steps": [
         ("Asenna SplitCam",
          "SplitCam on ilmainen streaming-ohjelmisto Windowsille ja macOS:lle sisäänrakennetulla multistreamingilla. Asenna — ilman vesileimaa, ilman rekisteröintiä."),
         ("Aseta kamera ja näkymä",
          "Avaa SplitCam, lisää webkamera ja rakenna näkymä overlayilla ja suodattimilla. Yksi näkymä syöttää jokaisen kohteen."),
         ("Hanki RTMP-avain jokaiselta cam-sivulta",
          "Jokaisella cam-alustalla aktivoi ulkoinen / RTMP-lähetys ja kopioi <strong>palvelin-URL</strong> ja <strong>stream key</strong>. Toista jokaiselle sivulle, jolle haluat lähettää — katso yksittäiset alustaoppaat tarkkoja reittejä varten."),
         ("Lisää jokainen kohde SplitCamiin",
          "Avaa <strong>Stream Settings</strong> ja lisää jokainen cam-sivu mukautettuna RTMP-kohteena — liitä palvelin-URL ja avain. Rastita kaikki, mitä haluat livenä."),
         ("Klikkaa Go Live kerran",
          "Paina <strong>Go Live</strong>. SplitCam lähettää streamin jokaiseen valittuun cam-sivuun samanaikaisesti, peer-to-peer, yhdestä koodauksesta — ilman lisämaksua."),
     ],
     "tips": [
         ("Seuraa uploadiasi", "Multistreaming kertoo upload-kuorman. Jokainen kohde kuluttaa oman bitratensa — varmista, että yhteytesi kestää summan."),
         ("Tarkista alustojen säännöt", "Jotkin cam-sivut kieltävät samanaikaisen lähetyksen muualle — vahvista ennen multistreamingia."),
         ("Kaapeli — droppeja ei voi sallia tässä", "Multistreaming kertoo upload-kuorman, joten yksi wi-fi-drop voi pudottaa kaikki kohteet kerralla. Kaapeli ei ole valinnainen tässä."),
         ("Seuraa terveysmonitoria", "SplitCam näyttää statuksen kohteittain — pudota sivu, jos upload ei kestä."),
     ],
     "faq": [
         ("Onko SplitCam-multistreaming ilmainen?", "Kyllä — multistreaming on sisäänrakennettu ja ilmainen, ei kohdekohtaista maksua, ei vesileimaa."),
         ("Kuinka moneen cam-sivuun voin lähettää samanaikaisesti?", "Niin moneen kuin upload-kaistanleveytesi kestää — jokainen kohde kuluttaa oman bitratensa."),
         ("Käyttääkö cloud-relayä?", "Ei — SplitCam lähettää streamit peer-to-peer suoraan PC:ltä jokaisen alustan ingestiin."),
         ("Hidastaako multistreaming PC:tä?", "Koodaus tehdään kerran ja käytetään uudelleen; laitteistokoodaus pitää CPU-kuorman alhaisena. Upload-kaistanleveys on todellinen raja."),
     ]},
    {"slug": "livejasmin", "name": "LiveJasmin",
     "title": "Lähetys LiveJasminissa SplitCamilla — HD ulkoinen enkooderi",
     "desc": "Lähetys LiveJasminissa ilmaisella SplitCamilla — Model Center ulkoinen enkooderi, HD 1080p, monikamera-näkymät ja overlayt. Ei vesileimaa, ei rekisteröitymistä.",
     "kw": "livejasmin lähetys, livejasmin obs, livejasmin ulkoinen enkooderi, livejasmin rtmp, livejasmin stream key, livejasmin model setup",
     "h1html": 'Miten lähetät <span class="accent">LiveJasminissa</span> SplitCamilla',
     "h1short": "Lähetys LiveJasmin",
     "card": "Ulkoisen enkooderin asetus LiveJasminin HD-only Model Centeriin.",
     "intro": "LiveJasmin on Docler Holdingin lippulaiva — yksi maailman suurimmista cam-verkostoista ja HD-only-alusta. Sen suosittelema lähetysohjelma on oma <strong>JasminCAM</strong>-asiakas, mutta Model Center tarjoaa myös standardin <strong>External Encoder</strong> -reitin, johon ilmainen <strong style='color:var(--text)'>SplitCam</strong> liittyy — saat monikamera-näkymät, kauneussuotimet ja overlayt samaan HD-striimiin.",
     "quick": "Lähetys LiveJasminissa SplitCamilla: asenna SplitCam, rakenna HD-näkymä, Model Centerissä avaa <em>Settings → Broadcast → External Encoder</em>, kopioi server URL ja stream key, liitä SplitCamiin, Go Live."
              "<ol><li>Asenna SplitCam.</li><li>Lisää kamera + HD-näkymä.</li>"
              "<li>Hae URL ja stream key Model Centeristä.</li><li>Liitä SplitCamiin.</li>"
              "<li>Paina Go Live.</li></ol>",
     "key_how": "Kirjaudu osoitteeseen <strong>modelcenter.livejasmin.com</strong>, avaa <strong>Settings → Broadcast → External Encoder</strong>. Model Center paljastaa tiliisi sidotun <strong>server URL</strong>:n ja <strong>stream key</strong>:n — kopioi molemmat SplitCamin custom RTMP -kenttiin. <strong>Huom:</strong> uudet tilit pitää hyväksyä (48–72 tuntia) ennen kuin External Encoder -vaihtoehto näkyy, ja alusta pakottaa HD-only-ulostulon.",
     "tips": [
         ("HD tai pudotat sijoituksia", "LiveJasmin on HD-only — alle 1280×720 voi näkyä vain matalapalkkaisilla listoilla, alle 1080p menettää 'Premium'-kelpoisuuden. Tähtää 1920×1080, 30 fps, 4 000–6 000 Kbps."),
         ("JasminCAM vs ulkoinen enkooderi", "Doclerin oma JasminCAM-asiakas antaa siisteimmän HD-vaatimustenmukaisuuden, mutta ulkoiset enkooderit (OBS, SplitCam, vMix) ovat virallisesti tuettuja, kun tili on hyväksytty — ne avaavat monikamera-näkymät ja overlayt, joita JasminCAM ei pysty tekemään."),
         ("Free chat ≠ private show", "Free chat on vain preview — ei alastomuutta. Private- ja Gold show -tiloissa malli tienaa. Suunnittele näkymä näyttämään vahvalta sekä vaatteissa ETTÄ show-tilassa."),
         _T_ETH,
     ],
     "faq": [
         ("Tukeeko LiveJasmin virallisesti ulkoisia enkoodereita kuten SplitCamia?", "Kyllä — Model Center sisältää External Encoder -vaihtoehdon kohdassa Settings → Broadcast. JasminCAM on suositeltu asiakas, mutta OBS, SplitCam ja muut RTMP-enkooderit on nimenomaisesti listattu tuetuiksi, kun malli-tili on hyväksytty."),
         ("Mistä saan LiveJasmin stream keyni?", "Model Centerin sisällä: Settings → Broadcast → External Encoder. Sekä server URL että uniikki stream key näkyvät siellä — kopioi molemmat SplitCamin custom RTMP -kenttiin. Avain on sidottu tiliisi; käsittele kuten salasanaa."),
         ("Mikä bitrate LiveJasminiin?", "LiveJasmin on HD-only — tähtää 1920×1080, 30 fps, 4 000–6 000 Kbps ja 2 sekunnin keyframe-väli. Tämän alle menevä menettää Premium-merkinnän ja putoaa sijoituksissa."),
         ("Onko SplitCam ilmainen LiveJasminin kanssa?", "Kyllä — SplitCam on ilmainen, ei vesileimaa eikä aikarajaa. Ainoa kustannus on LiveJasminin HD-vaatimusten täyttäminen, ja SplitCam hoitaa sen natiivisti 1080p-näkymäkoostamisella ja kauneussuotimilla."),
     ],
     "steps": [
         ("Lataa ja asenna SplitCam", "SplitCam on ilmainen live-streaming-ohjelma Windowsille ja macOS:lle — ei rekisteröitymistä, ei korttia, ei vesileimaa. Se on enkooderi, joka lähettää HD-videosi LiveJasminiin."),
         ("Rakenna HD-näkymä", "Avaa SplitCam ja lisää webkamera 1080p-tilassa. Kerro päälle overlayt, teksti, toinen kamera tai puhelin, kauneussuotimet tai AI-taustat — LiveJasmin vaatii HD-laatua ja kootun näkymän pitää näyttää premiumilta sekä free chatissa ETTÄ private show'ssa."),
         ("Hae LiveJasmin URL ja stream key", "Kirjaudu osoitteeseen <strong>modelcenter.livejasmin.com</strong> (tilisi pitää olla hyväksytty — yleensä 48–72 tuntia rekisteröinnistä). Avaa <strong>Settings → Broadcast → External Encoder</strong>. Sivu paljastaa <strong>server URL</strong>:n ja uniikin <strong>stream key</strong>:n. Kopioi molemmat."),
         ("Yhdistä SplitCam LiveJasminiin", "Avaa SplitCamissa <strong>Stream Settings</strong>, liitä LiveJasmin server URL ja stream key custom RTMP -kenttiin. Aseta bitrate 4 000–6 000 Kbps, 1920×1080, 30 fps, 2 sekunnin keyframe. Aja sisäänrakennettu nopeustesti ensin — HD-striimit vaativat paljon."),
         ("Klikkaa Go Live", "Paina SplitCamissa <strong>Go Live</strong>, sitten mene online LiveJasmin Model Centerissä. Noin 10 sekunnissa HD-feedisi saavuttaa LiveJasminin verkon. Seuraavat lähetykset ovat yhden klikkauksen — avaa SplitCam, Go Live, sitten online LiveJasminissa."),
     ],
    },
    {"slug": "myfreecams", "name": "MyFreeCams",
     "title": "Lähetys MyFreeCamsissa (MFC) SplitCamilla — Model Web Broadcasterin ohitus",
     "desc": "Lähetys MyFreeCamsissa ilmaisella SplitCamilla — Model Adminin External Broadcaster, MFC:n token-talous, monikamera-näkymät ja overlayt. Ei vesileimaa, ei rekisteröitymistä.",
     "kw": "myfreecams lähetys, mfc external broadcaster, myfreecams obs, mfc rtmp, mfc stream key, model admin, mfc token",
     "h1html": 'Miten lähetät <span class="accent">MyFreeCamsissa</span> SplitCamilla',
     "h1short": "Lähetys MyFreeCams",
     "card": "Ulkoisen broadcasterin asetus MFC:n token-pohjaiseen Model Adminiin.",
     "intro": "MyFreeCams (MFC) on yksi alan vanhimmista cam-alustoista — puhdas token-talous, ei mallin hyväksyntäkierrosta ja uskollinen Premium-jäsenten kanta. Oletuksena toimiva Model Web Broadcaster on yhden kameran selaintyökalu, mutta Model Admin tarjoaa myös <strong>External Broadcaster</strong> -vaihtoehdon, johon ilmainen <strong style='color:var(--text)'>SplitCam</strong> liittyy — avaten monikamera-näkymät, overlayt ja suotimet samaan token-striimiin.",
     "quick": "Lähetys MyFreeCamsissa SplitCamilla: asenna SplitCam, rakenna näkymä, Model Adminissa avaa Broadcaster ja vaihda Web Broadcasterista External Broadcasteriin, kopioi server URL ja stream key, liitä SplitCamiin, Go Live."
              "<ol><li>Asenna SplitCam.</li><li>Lisää kamera + näkymä.</li>"
              "<li>Vaihda External Broadcasteriin Model Adminissa.</li>"
              "<li>Liitä URL ja stream key SplitCamiin.</li><li>Paina Go Live.</li></ol>",
     "key_how": "Kirjaudu MyFreeCamsiin, avaa <strong>Model Admin → Broadcaster</strong>, vaihda <strong>Web Broadcasterista</strong> <strong>External Broadcasteriin</strong>. Sivu paljastaa server URL:n (<strong>rtmp://publish.myfreecams.com…</strong>) ja malli-tiliisi sidotun stream keyn — kopioi molemmat SplitCamin custom RTMP -kenttiin. Avain on tilikohtainen; käsittele kuten salasanaa.",
     "tips": [
         ("Puhdas tipping- ja token-talous, ei tilauksia", "MFC pyörii tippeillä ja tokeneilla — ei kuukausitilauksia. Tulot kasvavat group- ja private-showeilla, true private -tiloilla ja tip-menuilla, eivät tilaajilla. Suunnittele näkymä laukaisemaan tip-tavoitteita: token-laskuri, goal-grafiikka, tip menu jonossa."),
         ("Web Broadcaster vs External — valinta tehdään kerran", "Model Adminissa voi olla aktiivisena vain yksi tila: sisäänrakennettu Web Broadcaster tai External Broadcaster RTMP:llä. External käyttöön vaihtaminen poistaa selaimen esikatselun — kaikki näkymä- ja suodinasetukset hoidetaan SplitCamissa ja MFC ottaa vastaan valmiin striimin."),
         ("MFC Alerts mfcalerts.com:in kautta — Browser-layer", "mfcalerts.com tarjoaa julkiset URLit token-alertteja, goaleja ja top-tippereitä varten. Lisää URL Browser-layerina SplitCamiin läpinäkyvällä taustalla — alertit ilmestyvät suoraan kuvan päälle ilman erillistä ikkunaa."),
         _T_ETH,
     ],
     "faq": [
         ("Tukeeko MFC ulkoisia broadcastereita?", "Kyllä — Model Admin → Broadcaster -kohdassa. Vaihda Web Broadcasterista External Broadcasteriin, ja MFC antaa server URL:n ja stream keyn mille tahansa RTMP-enkooderille — SplitCam, OBS, vMix. Tämä on virallinen reitti, ei kiertotie."),
         ("Mistä saan MFC stream keyni?", "Model Admin → Broadcaster → External Broadcaster. Sekä server URL (publish.myfreecams.com) että uniikki stream key näkyvät siellä — kopioi molemmat SplitCamin custom RTMP -kenttiin. Avain on tilikohtainen; älä jaa ketään."),
         ("Mikä bitrate MFC:lle?", "MFC ottaa vastaan jopa noin 6 000 Kbps. Tähtää 1920×1080, 30 fps, 3 500–6 000 Kbps ja 2 sekunnin keyframe-väli. Tämä antaa terävän kuvan Premium-katsojille ja jää alustan kattoa pienemmäksi."),
         ("Onko SplitCam ilmainen MFC:n kanssa?", "Kyllä — SplitCam on ilmainen, ei vesileimaa, ei aikarajaa. Model Adminin External Broadcaster on standardi RTMP, joten ei tarvita lisälisenssejä eikä lisäosia."),
     ],
     "steps": [
         ("Lataa ja asenna SplitCam", "SplitCam on ilmainen live-streaming-ohjelma Windowsille ja macOS:lle — ei rekisteröitymistä, ei korttia, ei vesileimaa. Se on enkooderi, joka lähettää videosi MFC:lle."),
         ("Rakenna näkymäsi", "Avaa SplitCam ja lisää webkamera. Kerro päälle overlayt, teksti, toinen kamera tai puhelin, kauneussuotimet. MFC Alerteja varten lisää <strong>mfcalerts.com</strong>-URL Browser-layerina — token-laskuri, goal-grafiikka ja top-tipper-alertit ilmestyvät suoraan kuvaan."),
         ("Vaihda External Broadcasteriin ja kopioi tiedot", "Avaa <strong>Model Admin → Broadcaster</strong> ja vaihda <strong>Web Broadcasterista</strong> <strong>External Broadcasteriin</strong>. Sivu paljastaa server URL:n (<strong>rtmp://publish.myfreecams.com…</strong>) ja stream keyn. Kopioi molemmat."),
         ("Yhdistä SplitCam MFC:hen", "Avaa SplitCamissa <strong>Stream Settings</strong>, liitä MFC server URL ja stream key custom RTMP -kenttiin. Aseta bitrate 3 500–6 000 Kbps, 1920×1080, 30 fps, 2 sekunnin keyframe. Aja sisäänrakennettu nopeustesti ensin."),
         ("Klikkaa Go Live", "Paina SplitCamissa <strong>Go Live</strong> — MFC:n External Broadcaster ottaa striimin vastaan automaattisesti ja vie sinut online. Seuraavat lähetykset ovat yhden klikkauksen päässä — avaa SplitCam, Go Live, ja olet eetterissä MFC:llä."),
     ],
    },
    {"slug": "cherry-tv", "name": "Cherry.tv",
     "title": "Lähetys Cherry.tv:ssä SplitCamilla — Web3-ystävällinen ulkoinen enkooderi",
     "desc": "Lähetys Cherry.tv:ssä ilmaisella SplitCamilla — Streamer Dashboardin ulkoinen enkooderi, krypto-ystävällinen cam-alusta, monikamera-näkymät. Ei vesileimaa, ei rekisteröitymistä.",
     "kw": "cherry tv lähetys, cherry.tv obs, cherry tv ulkoinen enkooderi, cherry.tv rtmp, cherry.tv stream key, cherry tv streamer, web3 cam",
     "h1html": 'Miten lähetät <span class="accent">Cherry.tv</span>:ssä SplitCamilla',
     "h1short": "Lähetys Cherry.tv",
     "card": "Ulkoisen enkooderin asetus Cherry.tv:n Streamer Dashboardiin.",
     "intro": "Cherry.tv on uudempi, nopeasti kasvava cam-alusta Web3-kulmalla — krypto-ystävälliset maksut ja kevyempi sisäänpääsy kuin perinteisillä verkostoilla kuten LiveJasmin. Oletuksena toimiva broadcaster on selaimessa, mutta Streamer Dashboard tarjoaa myös standardin ulkoisen enkooderin reitin, johon ilmainen <strong style='color:var(--text)'>SplitCam</strong> liittyy — saat monikamera-näkymät, overlayt ja suotimet samaan striimiin.",
     "quick": "Lähetys Cherry.tv:ssä SplitCamilla: asenna SplitCam, rakenna näkymä, Streamer Dashboardissa avaa <em>Broadcast Settings → External Encoder</em>, kopioi server URL ja stream key, liitä SplitCamiin, Go Live."
              "<ol><li>Asenna SplitCam.</li><li>Lisää kamera + näkymä.</li>"
              "<li>Hae URL ja stream key Streamer Dashboardista.</li>"
              "<li>Liitä SplitCamiin.</li><li>Paina Go Live.</li></ol>",
     "key_how": "Kirjaudu Cherry.tv:n streamer-tiliisi, avaa <strong>Streamer Dashboard → Broadcast Settings → External Encoder</strong>. Server URL ja stream key on sidottu tiliin — kopioi molemmat SplitCamin custom RTMP -kenttiin. Uusilta tileiltä vaaditaan ensin perusverifiointi (Cherry.tv:n onboarding on kevyempi kuin perinteisillä verkoilla).",
     "tips": [
         ("Kevyempi sisäänpääsy, kasvava liikenne — hyvä early-mover -paikka", "Cherry.tv on nuorempi kuin LiveJasmin ja MFC, mutta kerää yleisöä nopeasti. Verifiointi on yksinkertaisempaa, listojen kärki ei vielä täynnä — nyt sisään tulemalla on helpompaa nousta esiin ja kerätä vakiokatsojia ennen kuin kilpailu kovenee."),
         ("Kryptomaksut fiatin rinnalla", "Cherry.tv tarjoaa kryptomaksut tavallisten pankkimaksujen lisäksi — kätevää, jos olet alueella missä fiat-nosto on hankalaa tai haluat pienemmät maksuliikennekulut. Aseta haluamasi tapa maksuosioon ennen ensimmäistä isoa sessiota."),
         ("Selainbroadcaster vs ulkoinen — mitä SplitCam tuo", "Cherry.tv:n selainbroadcaster on yksi kamera, ei overlayitä. SplitCamin External Encoder avaa monikamera-näkymät, kauneussuotimet, AI-taustat, alert-overlayt ja näkymänvaihdot — kaikki mikä nostaa kuvan keskitason mallin yläpuolelle alustalla."),
         _T_ETH,
     ],
     "faq": [
         ("Tukeeko Cherry.tv ulkoisia enkoodereita?", "Kyllä — Streamer Dashboardissa on External Encoder -vaihtoehto Broadcast Settings -kohdassa. SplitCam, OBS, vMix ja muut RTMP-enkooderit yhdistyvät standardisti kun perusverifiointi on tehty."),
         ("Mistä saan Cherry.tv stream keyni?", "Streamer Dashboardista: <strong>Broadcast Settings → External Encoder</strong>. Sekä server URL että uniikki stream key näkyvät siellä — kopioi molemmat SplitCamin custom RTMP -kenttiin. Avain on tilikohtainen; käsittele kuten salasanaa."),
         ("Mikä bitrate Cherry.tv:lle?", "Tähtää 3 500–6 000 Kbps, 1920×1080, 30 fps ja 2 sekunnin keyframe-väli. Tämä riittää terävään kuvaan kaikissa katsojan ikkunakokoluokissa eikä törmää ingestin kattoon."),
         ("Onko SplitCam ilmainen Cherry.tv:lle?", "Kyllä — SplitCam on ilmainen, ei vesileimaa eikä aikarajaa. Streamer Dashboardin External Encoder on standardi RTMP, ei lisälisenssejä."),
     ],
     "steps": [
         ("Lataa ja asenna SplitCam", "SplitCam on ilmainen live-streaming-ohjelma Windowsille ja macOS:lle — ei rekisteröitymistä, ei korttia, ei vesileimaa. Se on enkooderi, joka lähettää videosi Cherry.tv:lle."),
         ("Rakenna näkymäsi", "Avaa SplitCam ja lisää webkamera 1080p-tilassa. Kerro päälle overlayt, teksti, toinen kamera tai puhelin, kauneussuotimet tai AI-taustat. Cherry.tv:n yleisö on nuorempaa ja teknisesti perillä — moderni näkymä näkymänvaihdoilla ja overlayilla erottaa sinut heti selainstriimaajista."),
         ("Hae Cherry.tv URL ja stream key", "Kirjaudu Cherry.tv:n streamer-tilillesi, avaa <strong>Streamer Dashboard → Broadcast Settings → External Encoder</strong>. Sivu paljastaa <strong>server URL</strong>:n ja uniikin <strong>stream key</strong>:n. Kopioi molemmat."),
         ("Yhdistä SplitCam Cherry.tv:hen", "Avaa SplitCamissa <strong>Stream Settings</strong>, liitä Cherry.tv server URL ja stream key custom RTMP -kenttiin. Aseta bitrate 3 500–6 000 Kbps, 1920×1080, 30 fps, 2 sekunnin keyframe."),
         ("Klikkaa Go Live", "Paina SplitCamissa <strong>Go Live</strong>, sitten mene online Cherry.tv:ssä. Noin 10 sekunnissa striimi saavuttaa Cherry.tv:n verkon. Seuraavat lähetykset ovat yhden klikkauksen — avaa SplitCam, Go Live, sitten online Cherry.tv:ssä."),
     ],
    },
]
