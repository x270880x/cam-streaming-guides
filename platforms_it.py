# -*- coding: utf-8 -*-
"""Italian content for cam-streaming-guides. One dict per platform, written natively
for Italian-speaking audiences."""

_T_ETH = ("Connessione via cavo", "L'Ethernet è più affidabile del Wi-Fi per una diretta lunga — "
          "un frame perso è una mancia persa. Tira un cavo fino al PC di streaming.")
_T_TEST = ("Prima un test privato", "Fai una breve diretta di prova per controllare camera, audio, "
           "inquadratura e overlay prima di aprire la stanza al pubblico.")

PLATFORMS_IT = [
    {
        "slug": "chaturbate", "name": "Chaturbate",
        "title": "Trasmettere su Chaturbate con SplitCam — Token & RTMP",
        "desc": "Trasmettere su Chaturbate con SplitCam gratis — token di trasmissione, RTMP, scene multi-camera e overlay. Senza filigrana, senza registrazione.",
        "kw": "trasmettere su chaturbate, chaturbate, chaturbate broadcast, chaturbate obs, chaturbate external encoder, chaturbate rtmp, chaturbate broadcast token, chaturbate stream key",
        "h1html": 'Come trasmettere su <span class="accent">Chaturbate</span> con SplitCam',
        "h1short": "Trasmettere su Chaturbate",
        "card": "Configurazione tramite token con encoder esterno per Chaturbate.",
        "intro": "Chaturbate è una delle piattaforme cam più grandi, basata su un'economia di token. Il broadcaster integrato nel browser è solo una camera piatta — passare per l'<strong style='color:var(--text)'>encoder esterno</strong> con <strong style='color:var(--text)'>SplitCam</strong> gratuito sblocca scene multi-camera, overlay e filtri sullo stesso stream basato su token.",
        "quick": "Trasmettere su Chaturbate con SplitCam: installare SplitCam, comporre la scena, su Chaturbate aprire <em>Broadcast Yourself → My Broadcast</em>, copiare il broadcast token, incollarlo in SplitCam, Go Live."
                 "<ol><li>Installare SplitCam.</li><li>Aggiungere camera + scena.</li>"
                 "<li>Copiare il broadcast token di Chaturbate.</li><li>Incollarlo in SplitCam.</li>"
                 "<li>Premere Go Live.</li></ol>",
        "key_how": "Su Chaturbate clicca <strong>Broadcast Yourself</strong> per aprire la pagina <strong>My Broadcast</strong>, poi clicca <strong>View RTMP/OBS broadcast information and stream key</strong>. La chiave appare come il tuo <strong>broadcast token</strong> — copialo. Funziona come una password; non pubblicarlo mai.",
        "tips": [
            ("Il token è la chiave", "Chaturbate usa il tuo broadcast token al posto di una stream key generica. Trattalo come una password e resettalo se viene compromesso."),
            ("Molto margine", "L'ingest RTMP di Chaturbate accetta fino a 4K, 60 fps e un bitrate molto alto — il limite è il tuo upload, non la piattaforma. Intervallo keyframe: 2 secondi."),
            _T_ETH, _T_TEST,
        ],
        "faq": [
            ("Chaturbate consente OBS / encoder esterni?", "Sì — Chaturbate supporta ufficialmente gli encoder esterni e ha il proprio articolo «How do I set up OBS?». Si attiva tramite «Use External Encoder to Broadcast» nelle impostazioni di trasmissione."),
            ("Dove trovo la stream key di Chaturbate?", "Broadcast Yourself → My Broadcast → View RTMP/OBS broadcast information and stream key. La chiave è il tuo broadcast token."),
            ("Quale bitrate per Chaturbate?", "3.500–6.000 Kbps a 1080p sono più che sufficienti. Il tetto di Chaturbate è molto alto — il vero limite è il tuo upload; lancia prima lo speed test di SplitCam."),
            ("SplitCam è gratuito per Chaturbate?", "Sì — completamente gratis, senza filigrana e senza limite di tempo: l'encoder non si mangia i tuoi guadagni in token."),
        ],
    },
    {
        "slug": "cam4", "name": "CAM4",
        "title": "Trasmettere su CAM4 con SplitCam — External Encoder",
        "desc": "Trasmettere su CAM4 con SplitCam gratis — External Encoder, stream key, geo-blocco e overlay. Senza filigrana, guida gratuita.",
        "kw": "trasmettere su cam4, cam4, cam4 broadcast, cam4 obs, cam4 external encoder, cam4 rtmp, cam4 stream key",
        "h1html": 'Come trasmettere su <span class="accent">CAM4</span> con SplitCam',
        "h1short": "Trasmettere su CAM4",
        "card": "External Encoder per CAM4 con geo-controlli.",
        "intro": "CAM4 è una piattaforma cam-and-earn globale con geo-controlli integrati — puoi nascondere la tua trasmissione in determinati paesi. Trasmettere tramite <strong style='color:var(--text)'>SplitCam</strong> gratuito come encoder esterno aggiunge cambi di scena e overlay che il broadcaster base non può fare.",
        "quick": "Trasmettere su CAM4 con SplitCam: installare SplitCam, comporre la scena, su CAM4 aprire <em>Broadcast &amp; Earn Money → Start Broadcast → External Encoder</em>, Get Stream Key, incollare in SplitCam, Go Live."
                 "<ol><li>Installare SplitCam.</li><li>Aggiungere camera + scena.</li>"
                 "<li>Ottenere la stream key di CAM4.</li><li>Incollarla in SplitCam.</li>"
                 "<li>Premere Go Live.</li></ol>",
        "key_how": "Su CAM4 clicca <strong>Broadcast</strong> → <strong>Broadcast &amp; Earn Money</strong> → <strong>Start Broadcast</strong>, poi <strong>External Encoder</strong> in alto. Compila data di nascita, genere e paese, quindi usa <strong>Get Stream Key</strong> e copia la chiave. Uno slider verde negli Stream Settings di SplitCam conferma la connessione.",
        "tips": [
            ("Imposta le geo-restrizioni", "CAM4 ti permette di nascondere la trasmissione in paesi e regioni specifici — impostalo lato CAM4 prima di andare live se serve."),
            ("Occhio allo slider verde", "Il setup di CAM4 mostra uno slider verde negli Stream Settings di SplitCam quando la chiave è accettata — rosso significa: ricontrolla la chiave."),
            ("Bitrate più basso del solito", "L'ingest di CAM4 limita il bitrate video a circa 3.000 Kbps — più basso di gran parte dei siti cam. Non spingere oltre."),
            _T_ETH,
        ],
        "faq": [
            ("CAM4 supporta ufficialmente OBS / gli encoder esterni?", "Sì — CAM4 ha un OBS Guide ufficiale sul sito di supporto e raccomanda l'opzione External Encoder per la migliore esperienza. SplitCam usa lo stesso percorso RTMP."),
            ("Posso geo-bloccare la mia trasmissione su CAM4?", "Sì — CAM4 ha la geo-restrizione integrata per nascondere la trasmissione in certi paesi. Si imposta su CAM4, non in SplitCam."),
            ("Dov'è la stream key di CAM4?", "Broadcast → Broadcast & Earn Money → Start Broadcast → External Encoder → Get Stream Key."),
            ("Quale bitrate per CAM4?", "Più basso della media — l'ingest di CAM4 si ferma a circa 3.000 Kbps a 30 fps con keyframe da 1 secondo. La tabella ufficiale basata sullo speed test consiglia di non superare ~3.000."),
        ],
    },
    {
        "slug": "bongacams", "name": "BongaCams",
        "title": "Trasmettere su BongaCams con SplitCam — External Encoder",
        "desc": "Trasmettere su BongaCams con SplitCam gratis — External Encoder, scene multi-camera, overlay e sfondo IA. Senza filigrana.",
        "kw": "trasmettere su bongacams, bongacams, bongcams, bongacams broadcast, bongacams obs, bongacams external encoder, bongacams rtmp, bongacams stream key",
        "h1html": 'Come trasmettere su <span class="accent">BongaCams</span> con SplitCam',
        "h1short": "Trasmettere su BongaCams",
        "card": "Configurazione External Encoder per BongaCams.",
        "intro": "BongaCams è una piattaforma cam globale. Lo streaming via encoder esterno lì non è sempre attivo per default — una volta abilitato, <strong style='color:var(--text)'>SplitCam</strong> gratuito pilota la trasmissione con scene multi-camera, overlay e sfondo IA.",
        "quick": "Trasmettere su BongaCams con SplitCam: installare SplitCam, comporre la scena, su BongaCams aprire <em>Options → Broadcast settings → Select Encoder → External Encoder</em>, copiare URL e chiave, incollare in SplitCam, Go Live."
                 "<ol><li>Installare SplitCam.</li><li>Aggiungere camera + scena.</li>"
                 "<li>Ottenere URL e chiave di BongaCams.</li><li>Incollare in SplitCam.</li>"
                 "<li>Premere Go Live.</li></ol>",
        "key_how": "Su BongaCams apri <strong>Options</strong> → <strong>Broadcast settings</strong> → <strong>Select Encoder</strong> → <strong>External Encoder</strong> e copia l'URL del server e la stream key mostrati. <strong>Se il pulsante External Encoder non c'è</strong>, contatta il supporto BongaCams e chiedi di abilitare la codifica esterna sul tuo account.",
        "tips": [
            ("Niente pulsante External Encoder? Supporto", "BongaCams limita la codifica esterna account per account — se l'opzione manca in Broadcast settings, deve abilitarla il supporto."),
            ("Allinea la risoluzione", "BongaCams raccomanda che la risoluzione della webcam e quella di trasmissione coincidano — ad esempio entrambe a 1280×720."),
            _T_ETH, _T_TEST,
        ],
        "faq": [
            ("Perché manca il pulsante External Encoder su BongaCams?", "La codifica esterna non è attiva per default su tutti gli account — contatta il supporto BongaCams per attivarla, poi il pulsante compare in Broadcast settings."),
            ("Devo verificare il mio account su BongaCams?", "Sì — per trasmettere serve essere 18+, avere un documento di identità valido per la verifica dell'età, e l'approvazione dell'account prima di andare live."),
            ("Quale bitrate per BongaCams?", "L'ingest RTMP di BongaCams limita il bitrate video a circa 6.000 Kbps con keyframe di 2 secondi — 3.500–6.000 a 1080p è il sweet spot; testa prima il tuo upload."),
            ("SplitCam è gratuito per BongaCams?", "Sì — completamente gratis, senza filigrana e senza limite di tempo, quindi l'encoder non intacca i tuoi guadagni in token su BongaCams."),
        ],
    },
    {
        "slug": "stripchat", "name": "Stripchat",
        "title": "Trasmettere su Stripchat con SplitCam — Setup Strip Cam",
        "desc": "Trasmettere su Stripchat — la piattaforma strip cam — con SplitCam gratis. Software esterno, chiave-token, scene e overlay.",
        "kw": "trasmettere su stripchat, stripchat, strip cam, stripchat broadcast, stripchat obs, stripchat external encoder, stripchat rtmp, stripchat stream key",
        "h1html": 'Come trasmettere su <span class="accent">Stripchat</span> con SplitCam',
        "h1short": "Trasmettere su Stripchat",
        "card": "Setup software esterno per le trasmissioni Stripchat.",
        "intro": "Stripchat è una grande piattaforma cam focalizzata sull'interattività. La sua modalità <em>external software</em> ti dà una chiave basata su token — passala a <strong style='color:var(--text)'>SplitCam</strong> gratuito per trasmettere con scene, overlay e filtri invece di una singola camera piatta.",
        "quick": "Trasmettere su Stripchat con SplitCam: installare SplitCam, comporre la scena, su Stripchat scegliere <em>Switch to external software</em>, copiare la stream key, incollarla in SplitCam, Go Live."
                 "<ol><li>Installare SplitCam.</li><li>Aggiungere camera + scena.</li>"
                 "<li>Ottenere la stream key di Stripchat.</li><li>Incollarla in SplitCam.</li>"
                 "<li>Premere Go Live.</li></ol>",
        "key_how": "Su Stripchat scegli <strong>Switch to external software</strong>, poi apri <strong>Show external software settings for the stream</strong>. Copia la stream key — Stripchat la mostra come un token. Tienila privata.",
        "tips": [
            ("Allinea la risoluzione a quella del sito", "La FAQ di Stripchat avverte: la risoluzione nel tuo software deve coincidere esattamente con quella impostata sul sito, altrimenti il video pixella. Imposta entrambe uguali."),
            ("Il minimo di 2 Mbps non basta", "Stripchat indica 2 Mbps di upload come minimo — e dice esplicitamente che non è sufficiente per streaming via OBS o multidiffusione. Punta ben oltre."),
            ("La chiave è un token", "La stream key di Stripchat è un token — copiala esatta, non condividerla, resettala se viene compromessa."),
            _T_ETH,
        ],
        "faq": [
            ("Stripchat raccomanda OBS / software esterno?", "Sì — la FAQ ufficiale di Stripchat consiglia software di trasmissione esterno come OBS «per ottenere migliore qualità video e audio». SplitCam funziona allo stesso modo."),
            ("Come passo Stripchat su software esterno?", "Nel Broadcast Center scegli Switch to External Broadcast Software (OBS), poi apri le impostazioni del software esterno per rivelare la stream key (token)."),
            ("Quale bitrate per Stripchat?", "L'ingest RTMP accetta fino a ~6.000 Kbps con keyframe di 2 secondi. 3.500–6.000 a 1080p è ideale — ma serve molto sopra il minimo di 2 Mbps, soprattutto con streaming OBS."),
            ("SplitCam è gratuito per Stripchat?", "Sì — nessuna licenza, niente filigrana, nessun limite di tempo: anche show interattivi lunghi su Stripchat non costano nulla lato encoder."),
        ],
    },
    {
        "slug": "onlyfans", "name": "OnlyFans",
        "title": "Andare in diretta su OnlyFans con SplitCam",
        "desc": "Andare in diretta su OnlyFans con SplitCam gratis — accesso autorizzazione o OBS Key, scene multi-camera, overlay. Senza filigrana.",
        "kw": "andare in diretta su onlyfans, onlyfans, onlyfans live, onlyfans broadcast, onlyfans obs, onlyfans obs key, onlyfans stream key",
        "h1html": 'Come andare in diretta su <span class="accent">OnlyFans</span> con SplitCam',
        "h1short": "Diretta su OnlyFans",
        "card": "Autorizza una volta o incolla la chiave — diretta su OnlyFans.",
        "intro": "La diretta OnlyFans è per i tuoi iscritti. SplitCam si collega in <strong style='color:var(--text)'>due modi</strong> — fai login una volta con le credenziali OnlyFans e SplitCam recupera e mantiene sincronizzata la stream key in automatico, oppure incolla l'OBS Key a mano. In entrambi i casi trasmetti con scene multi-camera, overlay e filtri.",
        "quick": "Andare in diretta su OnlyFans con SplitCam: installare SplitCam, comporre la scena, aprire Stream Settings &rarr; Add Channel &rarr; OnlyFans e scegliere <em>Autorizzazione</em> — accedere con il proprio account OnlyFans e SplitCam recupera la chiave automaticamente — poi Go Live. Con l'account collegato puoi modificare le impostazioni dello stream OnlyFans dentro SplitCam, senza aprire il sito.",
        "steps": [
            ("Scarica e installa SplitCam",
             "SplitCam è un software di streaming gratuito per Windows e macOS — niente registrazione, niente carta, niente filigrana. È l'encoder che invia il tuo video a OnlyFans."),
            ("Configura camera e scena",
             "Apri SplitCam e aggiungi la webcam. Costruisci la scena che vedranno gli spettatori — overlay, testo, una seconda camera, filtri beauty o sfondo IA, applicati in diretta."),
            ("Connessione — Metodo 1: Autorizzazione (consigliato)",
             "In SplitCam apri <strong>Stream Settings</strong> &rarr; <strong>Add Channel</strong> &rarr; <strong>OnlyFans</strong> e scegli <strong>Autorizzazione</strong>. Accedi con email e password di OnlyFans. SplitCam si connette al tuo account, recupera la stream key in automatico e la mantiene sincronizzata — e ti permette di gestire le impostazioni dello stream OnlyFans dentro SplitCam, modificandole durante o dopo la diretta senza aprire il sito OnlyFans."),
            ("Connessione — Metodo 2: Stream Key (manuale)",
             "Preferisci non fare login? Usa la chiave. Su OnlyFans vai in <strong>Profile</strong> &rarr; <strong>Settings</strong> &rarr; sezione <strong>Other</strong> e copia l'<strong>OBS Key</strong>. In SplitCam, Add Channel &rarr; OnlyFans, incollala nel campo chiave. Questa chiave è statica — per cambiare impostazioni in seguito devi tornare sul sito OnlyFans."),
            ("Go Live",
             "Qualunque sia il metodo, premi <strong>Go Live</strong> in SplitCam. Con il Metodo 1 puoi continuare ad aggiustare le impostazioni OnlyFans da SplitCam in tempo reale; con il Metodo 2 la chiave resta esattamente come l'hai impostata."),
        ],
        "tips": [
            ("Autorizzazione vs Stream Key", "Due modi per collegarsi: <strong>Autorizzazione</strong> (login una volta, la chiave viene recuperata e mantenuta sincronizzata — il modo più semplice) o <strong>Stream Key</strong> (copia l'OBS Key da OnlyFans → Profile → Settings → Other e incollala). L'autorizzazione evita il copia-incolla manuale."),
            ("Modifica le impostazioni senza uscire da SplitCam", "Con l'autorizzazione l'account resta collegato, così puoi aggiustare le impostazioni dello stream OnlyFans dentro SplitCam in corso di trasmissione o dopo — senza passare dal sito OnlyFans."),
            ("Tieni il bitrate moderato", "L'ingest RTMP di OnlyFans limita il bitrate video a circa 2.500 Kbps — più stretto della media dei siti cam. Punta a 720p–1080p a ~2.000–2.500."),
            _T_ETH,
        ],
        "faq": [
            ("Come collego OnlyFans a SplitCam?", "Due modi. <strong>Autorizzazione</strong> — Stream Settings → Add Channel → OnlyFans → accedi con il tuo account OnlyFans e SplitCam recupera la chiave automaticamente. Oppure <strong>Stream Key</strong> — copia l'OBS Key da OnlyFans → Profile → Settings → Other e incollala."),
            ("Posso cambiare le impostazioni dello stream OnlyFans senza aprire il sito?", "Sì — con il metodo Autorizzazione SplitCam resta collegato al tuo account OnlyFans, quindi chiave e impostazioni si sincronizzano da sole. Puoi modificarle dentro SplitCam durante la diretta o dopo, senza visitare onlyfans.com."),
            ("Quale bitrate per OnlyFans?", "Tienilo moderato — l'ingest RTMP di OnlyFans limita il bitrate a circa 2.500 Kbps, molto più stretto della media. Punta a 720p–1080p attorno a 2.000–2.500 Kbps."),
            ("SplitCam è gratuito per le dirette OnlyFans?", "Sì — gratis, senza filigrana e senza limite di tempo. Nessun costo lato encoder."),
        ],
    },
    {
        "slug": "camplace", "name": "CamPlace",
        "title": "Trasmettere su CamPlace con SplitCam — Guida gratuita",
        "desc": "Trasmettere su CamPlace con SplitCam gratis — encoder esterno, chiave RTMP, scene e overlay. Guida passo dopo passo, senza filigrana.",
        "kw": "trasmettere su camplace, camplace, camplace broadcast, camplace obs, camplace external encoder, camplace rtmp, camplace stream key",
        "h1html": 'Come trasmettere su <span class="accent">CamPlace</span> con SplitCam',
        "h1short": "Trasmettere su CamPlace",
        "card": "Setup encoder esterno per le trasmissioni CamPlace.",
        "intro": "CamPlace è una piattaforma cam-streaming senza un articolo di aiuto pubblico su OBS — la <strong style='color:var(--text)'>guida video qui sopra</strong> è il riferimento. <strong style='color:var(--text)'>SplitCam</strong> gratuito si collega via RTMP standard e aggiunge scene, overlay e sfondo IA che la camera base non può fare.",
        "quick": "Trasmettere su CamPlace con SplitCam: installare SplitCam, comporre la scena, abilitare la trasmissione esterna/RTMP in CamPlace, copiare URL del server e stream key, incollare in SplitCam, Go Live. Segui la guida video sopra per il percorso attuale."
                 "<ol><li>Installare SplitCam.</li><li>Aggiungere camera + scena.</li>"
                 "<li>Ottenere la chiave RTMP di CamPlace.</li><li>Incollarla in SplitCam.</li>"
                 "<li>Premere Go Live.</li></ol>",
        "key_how": "Accedi a CamPlace e apri le impostazioni di trasmissione. Passa all'opzione encoder esterno / RTMP / OBS per rivelare l'<strong>URL del server</strong> e la <strong>stream key</strong>, copia entrambi. CamPlace non pubblica documentazione OBS ufficiale — la <strong>guida video sopra</strong> è la spiegazione più affidabile dell'interfaccia attuale.",
        "tips": [
            ("Niente guida OBS ufficiale — usa il video", "CamPlace non ha un articolo di aiuto pubblico sugli encoder esterni; la guida video sopra è il riferimento per il percorso attuale."),
            ("Il RTMP standard funziona", "Anche senza documentazione, CamPlace accetta un'URL server RTMP standard e una chiave — SplitCam si collega come destinazione RTMP personalizzata."),
            ("Sovrapponi gli overlay in SplitCam", "Obiettivi di mancia, nome utente e social come livelli di scena — la camera base di CamPlace non li può aggiungere."),
            _T_ETH,
        ],
        "faq": [
            ("CamPlace ha una guida OBS ufficiale?", "Nessun articolo di aiuto pubblico sugli encoder esterni trovato. CamPlace accetta un'URL RTMP e una chiave standard, quindi SplitCam funziona — segui la guida video sopra."),
            ("CamPlace supporta gli encoder esterni?", "Sì — accetta una stream key RTMP standard, quindi SplitCam si collega come destinazione RTMP personalizzata."),
            ("Quale bitrate per CamPlace?", "CamPlace non pubblica un numero ufficiale — prendi 3.500–6.000 Kbps a 1080p come range sicuro e lascia che lo speed test di SplitCam fissi il tuo vero tetto."),
            ("SplitCam è gratuito per CamPlace?", "Sì — gratis, senza filigrana e senza limite di tempo. Visto che CamPlace non porta un proprio encoder, uno strumento RTMP gratuito basta e avanza."),
        ],
    },
    {
        "slug": "camsoda", "name": "CamSoda",
        "title": "Trasmettere su CamSoda con SplitCam — OBS Broadcaster",
        "desc": "Trasmettere su CamSoda con SplitCam gratis — Use OBS Broadcaster, server regionali, scene e overlay. Senza filigrana, guida gratuita.",
        "kw": "trasmettere su camsoda, camsoda, camsoda broadcast, camsoda obs, camsoda external encoder, camsoda rtmp, camsoda stream key",
        "h1html": 'Come trasmettere su <span class="accent">CamSoda</span> con SplitCam',
        "h1short": "Trasmettere su CamSoda",
        "card": "Setup tramite Use OBS Broadcaster per CamSoda.",
        "intro": "CamSoda è una piattaforma cam statunitense nota per format di show interattivi e originali. Supporta ufficialmente la trasmissione tramite OBS — c'è un pulsante <strong style='color:var(--text)'>Use OBS Broadcaster</strong> nella pagina Go Live e una guida OBS ufficiale nel wiki CamSoda. <strong style='color:var(--text)'>SplitCam</strong> gratuito funziona allo stesso modo.",
        "quick": "Trasmettere su CamSoda con SplitCam: installare SplitCam, comporre la scena, cliccare Use OBS Broadcaster nella pagina Go Live di CamSoda, copiare URL del server e stream key, incollare in SplitCam, Go Live."
                 "<ol><li>Installare SplitCam.</li><li>Aggiungere camera + scena.</li>"
                 "<li>Cliccare Use OBS Broadcaster su CamSoda.</li>"
                 "<li>Incollare URL del server + chiave in SplitCam.</li><li>Premere Go Live.</li></ol>",
        "key_how": "Nella pagina <strong>Go Live</strong> di CamSoda clicca <strong>Use OBS Broadcaster</strong>. CamSoda mostra l'URL server RTMP e la stream key — copia entrambi. Scegli il server regionale (Nord America, Europa, Asia, ecc.) più vicino a te. Il wiki di CamSoda contiene una guida OBS completa se ti serve il dettaglio.",
        "tips": [
            ("Fatti verificare per ricevere mance", "Su CamSoda chiunque può trasmettere, ma per ricevere mance bisogna completare la procedura di verifica di CamSoda."),
            ("Scegli il server regionale più vicino", "CamSoda offre server di ingest regionali — scegliere il più vicino (NA / Europa / Asia / Sud America / Oceania) riduce la latenza e i frame persi."),
            ("Tetto a 1080p / 30 fps", "L'ingest di CamSoda arriva fino a circa 1080p, 30 fps e ~6.000 Kbps — inutile spingere oltre."),
            _T_ETH,
        ],
        "faq": [
            ("CamSoda supporta OBS / gli encoder esterni?", "Sì — ufficialmente. C'è un pulsante Use OBS Broadcaster nella pagina Go Live e una guida OBS nel wiki CamSoda, quindi SplitCam funziona."),
            ("Devo verificarmi su CamSoda?", "Per trasmettere, no. Per ricevere mance, sì — CamSoda richiede di completare prima la procedura di verifica."),
            ("Quale risoluzione supporta CamSoda?", "Fino a 1920×1080 a 30 fps, circa 6.000 Kbps al massimo sull'ingest RTMP."),
            ("SplitCam è gratuito per CamSoda?", "Sì — gratis, senza filigrana e senza limite di tempo. Funziona accanto alla modalità Use OBS Broadcaster gratuita di CamSoda, quindi tutta la catena non costa nulla."),
        ],
    },
    {
        "slug": "streamate", "name": "Streamate",
        "title": "Trasmettere su Streamate con SplitCam — Canale integrato",
        "desc": "Trasmettere su Streamate con SplitCam gratis — canale integrato, chiave SM Connect, scene e overlay. Senza filigrana, setup rapido.",
        "kw": "trasmettere su streamate, streamate, streamate broadcast, streamate sm connect, streamate obs, streamate rtmp, streamate stream key",
        "h1html": 'Come trasmettere su <span class="accent">Streamate</span> con SplitCam',
        "h1short": "Trasmettere su Streamate",
        "card": "Streamate è un canale integrato in SplitCam — setup rapido.",
        "intro": "Streamate è una piattaforma cam consolidata — ed è una delle destinazioni <strong style='color:var(--text)'>preconfigurate in SplitCam</strong>, nell'elenco dei canali; il setup è quindi più veloce di un inserimento RTMP manuale: scegli Streamate, incolla la chiave, fatto.",
        "quick": "Trasmettere su Streamate con SplitCam: installare SplitCam, comporre la scena, su Streamate usare <em>SM Connect → Start Show</em> per ottenere la chiave, poi in SplitCam aprire <em>Stream Settings → Add Channel → Streamate</em> e incollarla."
                 "<ol><li>Installare SplitCam.</li><li>Aggiungere camera + scena.</li>"
                 "<li>Ottenere la chiave Streamate via SM Connect.</li>"
                 "<li>Add Channel → Streamate in SplitCam.</li><li>Premere Go Live.</li></ol>",
        "key_how": "Su Streamate apri <strong>SM Connect</strong>, accetta i termini, clicca <strong>Start Show</strong> a sinistra e chiudi la finestra che si apre — poi copia la tua streaming key. In SplitCam apri <strong>Stream Settings</strong> → <strong>Add Channel</strong>, scegli <strong>Streamate</strong> dalla lista e incolla la chiave. Uno slider verde conferma la connessione.",
        "tips": [
            ("Streamate è un canale integrato", "Non serve un'URL RTMP manuale — SplitCam ha Streamate nella lista Add Channel; basta selezionarlo e incollare la chiave."),
            ("Chiudi il popup di SM Connect", "Dopo Start Show Streamate apre una finestra — chiudila; serviva solo a rivelare la streaming key."),
            ("Blocca la risoluzione su 1080p", "Il campo Video Resolution in SM Connect può saltare a 1440, che in realtà non viene consegnato e abbassa silenziosamente la tua qualità — impostalo a 1080p a mano. Un bitrate che cala su un'immagine ferma è normale: il flusso di Streamate è adattivo."),
            _T_ETH, _T_TEST,
        ],
        "faq": [
            ("Streamate è integrato in SplitCam?", "Sì — Streamate appare nella lista Add Channel di SplitCam, lo selezioni invece di inserire un'URL RTMP a mano."),
            ("Dov'è la streaming key di Streamate?", "SM Connect → accetta i termini → Start Show → chiudi il popup → copia la chiave."),
            ("Quale bitrate per Streamate?", "Streamate non fissa un tetto rigido — 3.500–6.000 Kbps a 1080p funziona bene. Il flusso è adattivo, quindi un bitrate più basso su immagini ferme è normale, non un bug."),
            ("SplitCam è gratuito per Streamate?", "Sì — gratis, senza filigrana e senza limite di tempo; e dato che Streamate è un canale integrato in SplitCam, non c'è nemmeno un costo separato di encoder."),
        ],
    },
    {
        "slug": "streamray", "name": "StreamRay",
        "title": "Trasmettere su StreamRay cam con SplitCam — URL dalla chat",
        "desc": "Trasmettere su StreamRay cam con SplitCam gratis — URL pubblicata nella finestra chat, modalità OBS Broadcaster, scene e overlay. Senza filigrana.",
        "kw": "trasmettere su streamray, streamray, streamray cam, streamray broadcast, streamray obs, streamray external encoder, streamray rtmp",
        "h1html": 'Come trasmettere su <span class="accent">StreamRay</span> con SplitCam',
        "h1short": "Trasmettere su StreamRay",
        "card": "Setup encoder esterno con URL-dalla-chat per StreamRay.",
        "intro": "StreamRay ha un setup di encoder esterno insolito — ti consegna l'URL dello stream nella <strong style='color:var(--text)'>finestra chat della trasmissione</strong> e non usa una stream key separata. <strong style='color:var(--text)'>SplitCam</strong> gratuito gestisce senza problemi questo flusso solo-URL.",
        "quick": "Trasmettere su StreamRay con SplitCam: installare SplitCam, comporre la scena, su StreamRay abilitare OBS Broadcaster, copiare l'URL dello stream dalla finestra chat, incollarla in SplitCam (lasciare vuoto il campo chiave), Go Live."
                 "<ol><li>Installare SplitCam.</li><li>Aggiungere camera + scena.</li>"
                 "<li>Copiare l'URL di StreamRay dalla chat.</li>"
                 "<li>Incollare l'URL in SplitCam.</li><li>Premere Go Live.</li></ol>",
        "key_how": "Su StreamRay clicca due volte <strong>Broadcast Now</strong>, apri il menu <strong>Other</strong>, scegli <strong>OBS Broadcaster</strong> e <strong>Save and Close</strong>. StreamRay pubblica poi la tua <strong>URL dello stream nella finestra chat</strong> — copiala da lì. Lascia <strong>vuoto</strong> il campo stream key di SplitCam; StreamRay autentica solo tramite URL.",
        "tips": [
            ("L'URL sta in chat", "StreamRay non mostra l'URL dello stream in un riquadro di impostazioni — la pubblica nella tua finestra chat di trasmissione. Copiala da lì."),
            ("Lascia la stream key vuota", "StreamRay non usa una chiave separata — solo l'URL. Non riempire il campo chiave in SplitCam."),
            _T_ETH, _T_TEST,
        ],
        "faq": [
            ("Dov'è l'URL dello stream di StreamRay?", "Dopo aver abilitato OBS Broadcaster, StreamRay pubblica l'URL nella finestra chat — copiala dalla chat."),
            ("Perché non c'è la stream key di StreamRay?", "StreamRay autentica solo tramite URL — lascia vuoto il campo chiave di SplitCam."),
            ("Quale bitrate per StreamRay?", "StreamRay non indica un tetto ufficiale — punta a 3.500–6.000 Kbps a 1080p e lancia lo speed test di SplitCam, dato che la modalità solo-URL non dà feedback sul bitrate."),
            ("SplitCam è gratuito per StreamRay?", "Sì — gratis, senza filigrana e senza limite di tempo, il che si adatta al flusso solo-URL di StreamRay dove basta incollare un link e si parte."),
        ],
    },
    {
        "slug": "xlovecam", "name": "XLoveCam",
        "title": "Trasmettere su XLoveCam con SplitCam — Link RTMP & chiave",
        "desc": "Trasmettere su XLoveCam con SplitCam gratis — link RTMP e chiave, server regionali, scene e overlay. Senza filigrana, guida gratuita.",
        "kw": "trasmettere su xlovecam, xlovecam, x love cam, xlovecam broadcast, xlovecam obs, xlovecam external encoder, xlovecam rtmp, xlovecam stream key",
        "h1html": 'Come trasmettere su <span class="accent">XLoveCam</span> con SplitCam',
        "h1short": "Trasmettere su XLoveCam",
        "card": "Setup link RTMP + chiave per XLoveCam.",
        "intro": "XLoveCam è una piattaforma cam europea e multilingue. Le impostazioni dell'account espongono sia un <strong style='color:var(--text)'>link RTMP</strong> sia una <strong style='color:var(--text)'>stream key</strong> — <strong style='color:var(--text)'>SplitCam</strong> gratuito prende entrambi e trasmette con scene e overlay completi.",
        "quick": "Trasmettere su XLoveCam con SplitCam: installare SplitCam, comporre la scena, su XLoveCam aprire <em>My Account → settings</em>, copiare link RTMP e stream key, incollare entrambi in SplitCam, avviare lo show."
                 "<ol><li>Installare SplitCam.</li><li>Aggiungere camera + scena.</li>"
                 "<li>Copiare link RTMP + chiave di XLoveCam.</li><li>Incollare entrambi in SplitCam.</li>"
                 "<li>Premere Go Live.</li></ol>",
        "key_how": "Su XLoveCam apri <strong>My Account</strong> → <strong>settings</strong>. Le impostazioni contengono sia un <strong>link RTMP</strong> sia una <strong>stream key</strong> — copiali entrambi nei campi URL server e chiave di SplitCam, poi usa <strong>Start your show</strong> su XLoveCam.",
        "tips": [
            ("Copia link E chiave", "XLoveCam ti dà un link RTMP E una stream key separata — ti servono entrambi in SplitCam, non solo uno."),
            ("Pubblico multilingue", "XLoveCam è europea e multilingue — un overlay di testo chiaro nella tua lingua aiuta gli spettatori a trovarti."),
            ("Scegli il server più vicino", "XLoveCam opera server RTMP regionali — Europa, Nord America, Sud America e Asia. Scegliere il più vicino riduce latenza e frame persi."),
            _T_ETH,
        ],
        "faq": [
            ("Dove sono i dati RTMP di XLoveCam?", "My Account → settings — mostra sia il link RTMP che la chiave."),
            ("XLoveCam supporta gli encoder esterni?", "Sì — fornisce un link RTMP e una chiave, quindi SplitCam funziona come encoder."),
            ("Quale bitrate per XLoveCam?", "XLoveCam non pubblica un limite fisso; 3.500–6.000 Kbps a 1080p è ideale. Scegliere il server regionale più vicino conta tanto quanto il numero — riduce i frame persi."),
            ("SplitCam è gratuito per XLoveCam?", "Sì — gratis, senza filigrana e senza limite di tempo. Raggiungere il pubblico europeo multilingue di XLoveCam non comporta costi software."),
        ],
    },
    {
        "slug": "soulcams", "name": "SoulCams",
        "title": "Trasmettere su SoulCams con SplitCam — Impostazioni OBS",
        "desc": "Trasmettere su SoulCams con SplitCam gratis — impostazioni OBS, server RTMP e chiave, scene multi-camera e overlay.",
        "kw": "trasmettere su soulcams, soulcams, soul cams, soulcams broadcast, soulcams obs, soulcams external encoder, soulcams rtmp, soulcams stream key",
        "h1html": 'Come trasmettere su <span class="accent">SoulCams</span> con SplitCam',
        "h1short": "Trasmettere su SoulCams",
        "card": "Setup impostazioni OBS per SoulCams.",
        "intro": "SoulCams è una piattaforma cam le cui impostazioni OBS mostrano <strong style='color:var(--text)'>server RTMP e stream key insieme</strong> in un'unica finestra. Inserisci entrambi in <strong style='color:var(--text)'>SplitCam</strong> gratuito per trasmettere con scene multi-camera e overlay.",
        "quick": "Trasmettere su SoulCams con SplitCam: installare SplitCam, comporre la scena, su SoulCams cliccare Go Online → Settings → OBS, copiare server e chiave, incollare entrambi in SplitCam, Go Live."
                 "<ol><li>Installare SplitCam.</li><li>Aggiungere camera + scena.</li>"
                 "<li>Aprire SoulCams Settings → OBS.</li><li>Incollare server + chiave in SplitCam.</li>"
                 "<li>Premere Go Live.</li></ol>",
        "key_how": "Su SoulCams accedi e clicca <strong>Go Online</strong>, poi apri <strong>Settings</strong> → <strong>OBS</strong>. La finestra OBS mostra <strong>server RTMP</strong> e <strong>stream key</strong> insieme — copiali entrambi in SplitCam.",
        "tips": [
            ("Server e chiave fianco a fianco", "SoulCams mostra il server RTMP e la chiave nella stessa finestra OBS — prendili entrambi in un colpo solo."),
            ("Prima Go Online", "Le impostazioni OBS appaiono solo dopo aver cliccato Go Online su SoulCams — fallo prima di cercare i dati dell'encoder."),
            ("Blocca le regioni indesiderate", "SoulCams permette il blocco per paese lato modella — scegli quali paesi non possono vedere la tua trasmissione prima di cliccare Go Online."),
            _T_ETH, _T_TEST,
        ],
        "faq": [
            ("Dove sono le impostazioni OBS di SoulCams?", "Accedi, clicca Go Online, poi Settings → OBS — server RTMP e stream key sono mostrati insieme."),
            ("SoulCams supporta gli encoder esterni?", "Sì — le sue impostazioni OBS forniscono server RTMP e chiave, quindi SplitCam funziona."),
            ("Quale bitrate per SoulCams?", "SoulCams non dà un numero ufficiale — punta a 3.500–6.000 Kbps a 1080p e testa prima il tuo upload, dato che la finestra OBS non mostra indicazioni sul bitrate."),
            ("SplitCam è gratuito per SoulCams?", "Sì — gratis, senza filigrana e senza limite di tempo, quindi uno show completo su SoulCams con scene multi-camera e overlay non costa nulla lato encoder."),
        ],
    },
    {
        "slug": "imlive", "name": "ImLive",
        "title": "Trasmettere su ImLive con SplitCam — Camera virtuale",
        "desc": "Setup Im Live stream con SplitCam gratis — ImLive usa la webcam direttamente (niente RTMP), collega SplitCam come camera virtuale con scene.",
        "kw": "trasmettere su imlive, imlive, im live cam, imlive virtual camera, imlive camera virtuale, imlive webcam, imlive splitcam",
        "h1html": 'Come usare <span class="accent">ImLive</span> con SplitCam',
        "h1short": "SplitCam su ImLive",
        "card": "Setup camera virtuale per ImLive — niente RTMP.",
        "intro": "ImLive usa la tua webcam direttamente nel browser — non c'è <strong style='color:var(--text)'>né RTMP né stream key</strong>. <strong style='color:var(--text)'>SplitCam</strong> gratuito si collega come <strong style='color:var(--text)'>camera virtuale</strong>: componi la scena in SplitCam, poi scegli SplitCam come camera dentro ImLive.",
        "quick": "Usare SplitCam su ImLive: installare SplitCam, comporre la scena con livelli media, aprire ImLive e avviare una video chat, poi nelle impostazioni ImLive selezionare SplitCam come webcam e microfono."
                 "<ol><li>Installare SplitCam.</li><li>Comporre la scena in SplitCam.</li>"
                 "<li>Avviare una video chat su ImLive.</li>"
                 "<li>Scegliere SplitCam come camera ImLive.</li><li>Avviare la chat.</li></ol>",
        "steps": [
            ("Installa SplitCam",
             "SplitCam è un software gratuito per Windows e macOS. Installalo — senza filigrana e senza registrazione. Su ImLive funziona come <strong>camera virtuale</strong>, non come encoder RTMP."),
            ("Componi la scena in SplitCam",
             "Apri SplitCam e usa <strong>Media Layers +</strong> per aggiungere la webcam più qualsiasi overlay, testo, filtri o sfondo IA. Questa scena composta è quella che ImLive vedrà come la tua camera."),
            ("Avvia una video chat su ImLive",
             "Vai sul sito ImLive e clicca <strong>Start Video Chat</strong>, poi apri <strong>Go To Settings</strong> per arrivare alle opzioni camera e microfono."),
            ("Scegli SplitCam come camera",
             "Nelle impostazioni di ImLive scegli <strong>SplitCam</strong> come webcam E come microfono. ImLive mostra ora la tua scena SplitCam completa al posto di una webcam piatta."),
            ("Avvia il Free Live Chat",
             "Su ImLive clicca <strong>Free Live Chat</strong> per andare live. Per cambiare aspetto durante la sessione, modifica la scena in SplitCam — ImLive si aggiorna all'istante."),
        ],
        "tips": [
            ("Niente stream key", "ImLive non ha RTMP — non cercare URL server o chiave. SplitCam si seleziona semplicemente come dispositivo camera."),
            ("Imposta SplitCam anche come microfono", "Scegli SplitCam per il microfono oltre che per la camera, così il tuo mix audio e la soppressione del rumore arrivano nella diretta."),
            ("Componi la scena prima del live", "ImLive mostra qualunque cosa SplitCam emetta — sistema i livelli prima di avviare la chat."),
            _T_TEST,
        ],
        "faq": [
            ("ImLive usa RTMP o una stream key?", "No — ImLive usa la tua webcam direttamente via browser. SplitCam si collega come camera virtuale, quindi non c'è alcuna chiave da copiare."),
            ("Come scelgo SplitCam su ImLive?", "Start Video Chat → Go To Settings → scegli SplitCam come webcam e microfono."),
            ("Posso usare overlay su ImLive?", "Sì — componili nella scena di SplitCam; ImLive mostra il risultato composto."),
            ("SplitCam è gratuito per ImLive?", "Sì — gratis, senza filigrana e senza limite di tempo. Come camera virtuale per ImLive non aggiunge né costi né branding alla tua video chat."),
        ],
    },
    {
        "slug": "vxlive", "name": "VXLive",
        "title": "Trasmettere su VXLive con SplitCam — Supporto ufficiale",
        "desc": "Trasmettere su VXLive (VXModels / VISIT-X) con SplitCam gratis — preset VISIT-X ufficiale, server e chiave, scene. Senza filigrana.",
        "kw": "trasmettere su vxlive, vxlive, visit-x, vxmodels, vxlive broadcast, vxlive obs, vxlive external encoder, vxlive rtmp",
        "h1html": 'Come trasmettere su <span class="accent">VXLive</span> con SplitCam',
        "h1short": "Trasmettere su VXLive",
        "card": "VXLive supporta SplitCam ufficialmente (preset VISIT-X).",
        "intro": "VXLive (VXModels / VISIT-X) è una piattaforma cam del mercato tedesco — e una delle poche a <strong style='color:var(--text)'>supportare ufficialmente SplitCam per nome</strong>. VXModels ha un articolo di aiuto dedicato per collegare <strong style='color:var(--text)'>SplitCam</strong> a VXLive, e SplitCam porta VISIT-X come preset di canale pronto all'uso.",
        "quick": "Trasmettere su VXLive con SplitCam: installare SplitCam, comporre la scena, su VXLive scegliere «Stream with third-party software», copiare URL server e chiave, in SplitCam scegliere il preset VISIT-X e incollare, Go Live in SplitCam, poi GO ONLINE su VXLive."
                 "<ol><li>Installare SplitCam.</li><li>Aggiungere camera + scena.</li>"
                 "<li>Ottenere URL server + chiave di VXLive.</li>"
                 "<li>Scegliere il preset VISIT-X in SplitCam, incollare.</li>"
                 "<li>Go Live, poi GO ONLINE su VXLive.</li></ol>",
        "key_how": "Su VXLive scegli <strong>Stream with third-party software</strong> e seleziona l'opzione per <strong>OBS, SplitCam o XSplit</strong>. VXLive fornisce un'<strong>URL server</strong> e una <strong>stream key</strong>. In SplitCam scegli <strong>VISIT-X</strong> come piattaforma di streaming, incolla entrambi, premi <strong>Go Live</strong> in SplitCam, poi <strong>GO ONLINE</strong> su VXLive.",
        "tips": [
            ("VISIT-X è un preset integrato", "Non inserisci un'URL RTMP grezza — SplitCam ha VISIT-X nella lista delle piattaforme; basta selezionarlo e incollare URL server e chiave."),
            ("Go-live in due tempi", "Su VXLive premi prima Go Live in SplitCam, poi GO ONLINE in VXLive — entrambi, in quest'ordine."),
            ("Mercato di lingua tedesca", "Il pubblico VXLive è prevalentemente di lingua tedesca — un overlay di testo o titolo in tedesco aiuta a connettersi con gli spettatori."),
            _T_ETH,
        ],
        "faq": [
            ("VXLive supporta SplitCam ufficialmente?", "Sì — VXModels (VXLive) ha un articolo di aiuto ufficiale dedicato alla configurazione di SplitCam, e lo elenca insieme a OBS e XSplit come software di trasmissione supportato."),
            ("Come collego SplitCam a VXLive?", "In VXLive scegli «Stream with third-party software», poi in SplitCam seleziona il preset VISIT-X e incolla l'URL server e la stream key fornite da VXLive."),
            ("Vado in diretta da SplitCam o da VXLive?", "Da entrambi — prima Go Live in SplitCam, poi GO ONLINE in VXLive."),
            ("Perché VXModels raccomanda SplitCam?", "L'articolo di aiuto ufficiale VXModels raccomanda SplitCam specificamente per eliminare gli artefatti dell'immagine e la pixellatura della webcam e per stabilizzare la connessione — non come semplice encoder generico."),
        ],
    },
    {
        "slug": "virtwish", "name": "VirtWish",
        "title": "Trasmettere su VirtWish con SplitCam — URL stream & chiave",
        "desc": "Trasmettere su VirtWish con SplitCam gratis — Profile → Start Broadcast sezione OBS, URL stream e chiave, scene e overlay.",
        "kw": "trasmettere su virtwish, virtwish, virtwish broadcast, virtwish obs, virtwish external encoder, virtwish rtmp, virtwish stream key",
        "h1html": 'Come trasmettere su <span class="accent">VirtWish</span> con SplitCam',
        "h1short": "Trasmettere su VirtWish",
        "card": "Setup URL stream + chiave per VirtWish.",
        "intro": "VirtWish è una piattaforma cam interattiva. Le sue impostazioni di trasmissione ti danno una <strong style='color:var(--text)'>URL stream e una stream key separata</strong> in una sezione OBS — <strong style='color:var(--text)'>SplitCam</strong> gratuito prende entrambe e manda avanti lo show con scene e overlay.",
        "quick": "Trasmettere su VirtWish con SplitCam: installare SplitCam, comporre la scena, su VirtWish aprire <em>Profile → Start Broadcast</em> fino alla sezione OBS, copiare il link e la chiave, incollare entrambi in SplitCam, Go Live."
                 "<ol><li>Installare SplitCam.</li><li>Aggiungere camera + scena.</li>"
                 "<li>Ottenere URL + chiave di VirtWish.</li><li>Incollare entrambi in SplitCam.</li>"
                 "<li>Premere Go Live.</li></ol>",
        "key_how": "Su VirtWish clicca sull'icona in alto a destra → <strong>Profile</strong> → <strong>Start Broadcast</strong>, poi di nuovo <strong>Start Broadcast</strong> per arrivare alla sezione OBS. <strong>Copia il link della prima riga</strong> nel campo Stream URL di SplitCam, e la <strong>Stream Key</strong> a parte nel campo chiave.",
        "tips": [
            ("Il link è sulla prima riga", "La sezione OBS di VirtWish mette l'URL dello stream sulla prima riga — copiala in Stream URL di SplitCam, poi la chiave a parte."),
            ("Due clic su Start Broadcast", "Su VirtWish clicchi Start Broadcast due volte per arrivare alla sezione OBS — è previsto, non un bug."),
            _T_ETH, _T_TEST,
        ],
        "faq": [
            ("Dove sono i dati RTMP di VirtWish?", "Icona in alto a destra → Profile → Start Broadcast due volte → la sezione OBS mostra il link e la stream key."),
            ("VirtWish supporta gli encoder esterni?", "Sì — la sua sezione OBS fornisce un'URL stream e una chiave, quindi SplitCam funziona."),
            ("Quale bitrate per VirtWish?", "VirtWish non pubblica un tetto ufficiale; 3.500–6.000 Kbps a 1080p è un range sicuro. Allinea la risoluzione di SplitCam a quella impostata su VirtWish per evitare il rescaling."),
            ("SplitCam è gratuito per VirtWish?", "Sì — gratis, senza filigrana e senza limite di tempo. Il setup URL-e-chiave di VirtWish costa solo i pochi minuti che ci vogliono."),
        ],
    },
    {
        "slug": "xmodels", "name": "XModels",
        "title": "Trasmettere su XModels con SplitCam — Guida gratuita",
        "desc": "Trasmettere su XModels con SplitCam gratis — opzione encoder esterno nelle impostazioni dell'account modella, chiave RTMP, scene e overlay.",
        "kw": "trasmettere su xmodels, xmodels, xmodels broadcast, xmodels obs, xmodels external encoder, xmodels rtmp, xmodels stream key",
        "h1html": 'Come trasmettere su <span class="accent">XModels</span> con SplitCam',
        "h1short": "Trasmettere su XModels",
        "card": "Setup encoder esterno per le trasmissioni XModels.",
        "intro": "XModels è una piattaforma cam-streaming con un'<strong style='color:var(--text)'>opzione encoder esterno</strong> integrata nelle impostazioni dell'account modella. <strong style='color:var(--text)'>SplitCam</strong> gratuito vi trasmette con scene multi-camera, overlay e filtri invece di una singola camera piatta.",
        "quick": "Trasmettere su XModels con SplitCam: installare SplitCam, comporre la scena, nell'account modella XModels abilitare l'opzione encoder esterno, copiare URL server e stream key, incollare in SplitCam, Go Live."
                 "<ol><li>Installare SplitCam.</li><li>Aggiungere camera + scena.</li>"
                 "<li>Abilitare l'encoder esterno nelle impostazioni dell'account XModels.</li>"
                 "<li>Incollare URL server + chiave in SplitCam.</li><li>Premere Go Live.</li></ol>",
        "key_how": "Nelle <strong>impostazioni del tuo account modella</strong> XModels, abilita l'opzione <strong>trasmetti tramite encoder esterno</strong>. XModels fornisce una <strong>stream key</strong> — copiala in SplitCam. Se l'opzione non è dove te l'aspetti, il supporto XModels passa dalla FAQ-chat sul sito e da <strong>info@xmodels.com</strong>; la guida video sopra la mostra anche.",
        "tips": [
            ("Sta nelle impostazioni dell'account", "XModels mette l'opzione encoder esterno dentro le impostazioni dell'account modella, non su una schermata di trasmissione separata."),
            ("Supporto: chat + email", "XModels non ha un grande centro assistenza pubblico — la chat FAQ sul sito e info@xmodels.com sono i canali ufficiali di supporto."),
            ("Sovrapponi gli overlay in SplitCam", "Obiettivi di mancia, nome utente e social come livelli di scena — la camera base di XModels non li può aggiungere."),
            _T_ETH,
        ],
        "faq": [
            ("XModels supporta gli encoder esterni?", "Sì — le impostazioni dell'account modella includono un'opzione di trasmissione tramite encoder esterno che fornisce una stream key, quindi SplitCam funziona."),
            ("Dove ottengo aiuto su XModels?", "Il supporto XModels è via la chat FAQ sul sito e l'email info@xmodels.com — non c'è un grande centro assistenza pubblico."),
            ("Quale bitrate per XModels?", "XModels non documenta un numero ufficiale — usa 3.500–6.000 Kbps a 1080p e lancia lo speed test di SplitCam, dato che il supporto XModels è solo chat ed email."),
            ("SplitCam è gratuito per XModels?", "Sì — gratis, senza filigrana e senza limite di tempo, quindi trasmettere sulla rete europea di XModels non aggiunge costi software."),
        ],
    },
    {
        "slug": "flirt4free", "name": "Flirt4Free",
        "title": "Trasmettere su Flirt4Free con SplitCam — Encoder esterno",
        "desc": "Trasmettere su Flirt4Free con SplitCam gratis — External Broadcast Form, RTMP URL e Stream Name, scene e overlay. Senza filigrana.",
        "kw": "trasmettere su flirt4free, flirt4free, flirt for free cam, flirt4free broadcast, flirt4free obs, flirt4free external encoder, flirt4free rtmp",
        "h1html": 'Come trasmettere su <span class="accent">Flirt4Free</span> con SplitCam',
        "h1short": "Trasmettere su Flirt4Free",
        "card": "Setup External Broadcast Form per Flirt4Free.",
        "intro": "Flirt4Free è una delle piattaforme cam più longeve, online dagli anni '90. Supporta ufficialmente la trasmissione esterna tramite un <strong style='color:var(--text)'>External Broadcast Form</strong> — <strong style='color:var(--text)'>SplitCam</strong> gratuito invia lo stream mentre il modulo imposta risoluzione e bitrate.",
        "quick": "Trasmettere su Flirt4Free con SplitCam: installare SplitCam, comporre la scena, aprire l'External Broadcast Form di Flirt4Free, copiare RTMP URL e Stream Name e impostare risoluzione/bitrate, incollare in SplitCam, Go Live."
                 "<ol><li>Installare SplitCam.</li><li>Aggiungere camera + scena.</li>"
                 "<li>Aprire l'External Broadcast Form di Flirt4Free.</li>"
                 "<li>Incollare RTMP URL + Stream Name in SplitCam.</li>"
                 "<li>Premere Go Live.</li></ol>",
        "key_how": "Nell'area modella di Flirt4Free apri l'<strong>External Broadcast Form</strong>. Diversamente dalla maggior parte dei siti cam, Flirt4Free ti dà un'<strong>RTMP URL</strong> e uno <strong>Stream Name</strong> (non una «chiave»), più campi di risoluzione e bitrate da compilare nel modulo stesso. Copia URL e Stream Name nei campi server e chiave di SplitCam.",
        "tips": [
            ("È uno Stream Name, non una chiave", "Flirt4Free chiama queste credenziali Stream Name. Incollalo nel campo stream key di SplitCam — svolge lo stesso ruolo."),
            ("Imposta risoluzione/bitrate nel modulo", "L'External Broadcast Form di Flirt4Free ha i propri campi di risoluzione e bitrate — allineali alle tue impostazioni SplitCam così l'immagine non viene riscalata."),
            ("Piattaforma storica", "Flirt4Free è attiva dagli anni '90 — gli strumenti per modelle sono maturi e l'External Broadcast Form ne è una parte documentata."),
            _T_ETH,
        ],
        "faq": [
            ("Flirt4Free supporta gli encoder esterni?", "Sì — ufficialmente, tramite il suo External Broadcast Form, che fornisce un'RTMP URL e uno Stream Name. SplitCam funziona come encoder."),
            ("Dove ottengo i dati RTMP di Flirt4Free?", "Dall'External Broadcast Form nell'area modella — mostra RTMP URL, Stream Name e campi di risoluzione/bitrate."),
            ("Quale bitrate per Flirt4Free?", "3.500–6.000 Kbps a 1080p — imposta lo stesso valore nell'External Broadcast Form e in SplitCam."),
            ("SplitCam è gratuito per Flirt4Free?", "Sì — gratis, senza filigrana e senza limite di tempo, il che si adatta a una piattaforma storica come Flirt4Free dove gli show possono durare a lungo."),
        ],
    },
    {
        "slug": "mfc-alerts", "name": "MFC Alerts",
        "title": "Aggiungere MFC Alerts allo stream con SplitCam",
        "desc": "Mostrare alert animati delle mance sullo stream MyFreeCams — URL mfcalerts.com come livello Browser in SplitCam gratuito, sopra la webcam.",
        "kw": "aggiungere mfc alerts, mfc alerts, myfreecams, myfreecams alerts, mfc tip alerts, mfcalerts splitcam, mfc alerts overlay",
        "h1html": 'Come aggiungere <span class="accent">MFC Alerts</span> al tuo stream',
        "h1short": "Aggiungere MFC Alerts",
        "card": "Mostra alert animati delle mance sullo stream MyFreeCams.",
        "intro": "MFC Alerts mostra effetti animati sul tuo stream MyFreeCams ogni volta che uno spettatore manda una mancia. Gira come <strong style='color:var(--text)'>livello Browser</strong> dentro <strong style='color:var(--text)'>SplitCam</strong> gratuito — lo configuri una volta e le mance fanno scattare reazioni a schermo in diretta.",
        "quick": "Aggiungere MFC Alerts con SplitCam: installare SplitCam, aggiungere la webcam, aprire la scheda Browser e caricare mfcalerts.com, copiare la propria URL degli alert, aggiungerla come livello Browser sopra la webcam, poi testare con una mancia di prova."
                 "<ol><li>Installare SplitCam.</li><li>Aggiungere la webcam.</li>"
                 "<li>Ottenere l'URL su mfcalerts.com.</li>"
                 "<li>Aggiungerla come livello Browser sopra la webcam.</li>"
                 "<li>Mandare una mancia di prova.</li></ol>",
        "steps": [
            ("Installa SplitCam e aggiungi la webcam",
             "Installa SplitCam gratuito per Windows o macOS, poi aggiungi la tua <strong>webcam</strong> come fonte. MFC Alerts farà da livello sopra questa camera."),
            ("Apri la scheda Browser e vai su mfcalerts.com",
             "In SplitCam apri la scheda <strong>Browser</strong> e naviga su <strong>www.mfcalerts.com</strong>. Accedi, o registrati se non hai ancora un account mfcalerts.com."),
            ("Copia la tua URL degli alert",
             "Su mfcalerts.com usa <strong>Copy to clipboard</strong> per copiare la tua URL personale degli alert — è la pagina che renderizza le animazioni delle mance."),
            ("Aggiungi l'URL come livello Browser — sopra la webcam",
             "Incolla l'URL nella finestra Browser di SplitCam e clicca <strong>Add</strong>. Poi riordina la lista delle fonti perché <strong>MFC Alerts stia sopra la webcam</strong> (menu a 3 punti → Move Up). Se è sotto, gli effetti restano nascosti."),
            ("Prova con una mancia di test",
             "Apri <strong>Settings → Send test tip</strong> e verifica che l'effetto di alert compaia sopra la tua camera. Poi trasmetti su MyFreeCams come al solito — le mance vere fanno scattare ora le animazioni."),
        ],
        "tips": [
            ("MFC Alerts deve stare sopra la webcam", "L'errore più comune: se il livello MFC Alerts sta sotto la webcam nella lista delle fonti, gli effetti restano nascosti. Spostalo sopra."),
            ("Ti serve un account mfcalerts.com", "L'URL degli alert è personale per il tuo account — registrati prima su mfcalerts.com se non ne hai uno."),
            ("Manda una mancia di test prima del live", "Usa Settings → Send test tip per verificare che l'overlay funzioni — non scoprire un guasto a metà show."),
            _T_ETH,
        ],
        "faq": [
            ("Cos'è MFC Alerts?", "Un sistema di notifiche per MyFreeCams che mostra effetti video sul tuo stream quando gli spettatori mandano mance — aggiunto come overlay Browser in SplitCam."),
            ("Perché i miei MFC Alerts non si vedono?", "Quasi sempre è l'ordine dei livelli — il livello Browser di MFC Alerts deve stare sopra la webcam nella lista delle fonti di SplitCam."),
            ("Serve un account per MFC Alerts?", "Sì — registrati su mfcalerts.com per ottenere la tua URL personale degli alert."),
            ("SplitCam è gratuito per questo?", "Sì — SplitCam è gratis, senza filigrana e senza limite di tempo, e l'overlay browser di MFC Alerts gira dentro senza costi aggiuntivi."),
        ],
    },
    {
        "slug": "lovense", "name": "Lovense",
        "title": "Aggiungere un toy Lovense allo stream con SplitCam",
        "desc": "Collegare un toy Lovense interattivo allo stream cam con SplitCam gratis — Lovense SplitCam Toolset, alert delle mance a schermo, reazioni.",
        "kw": "aggiungere lovense allo stream, lovense, lovense toy, lovense cam stream, lovense splitcam, lovense splitcam toolset, lovense toy interattivo",
        "h1html": 'Come aggiungere un <span class="accent">toy Lovense</span> al tuo stream',
        "h1short": "Aggiungere un toy Lovense",
        "card": "Collegare un toy Lovense interattivo al tuo stream cam.",
        "intro": "Trasmetti il tuo stream cam tramite <strong style='color:var(--text)'>SplitCam</strong> gratuito e accoppia un toy <strong style='color:var(--text)'>Lovense</strong> che reagisce ai token. Lovense documenta ufficialmente un <strong style='color:var(--text)'>Lovense SplitCam Toolset</strong>, e SplitCam porta un plugin Lovense ufficiale — l'integrazione è supportata da entrambi i lati.",
        "quick": "Per aggiungere un toy Lovense allo stream: installare SplitCam e il software Lovense, accoppiare il toy, collegare Lovense alla tua piattaforma cam, aggiungere lo stato di Lovense come livello Browser in SplitCam, poi trasmettere come al solito."
                 "<ol><li>Installare SplitCam.</li><li>Installare e accoppiare il software Lovense.</li>"
                 "<li>Collegare Lovense al tuo sito cam.</li>"
                 "<li>Aggiungere l'overlay Lovense in SplitCam.</li><li>Premere Go Live.</li></ol>",
        "steps": [
            ("Installa SplitCam",
             "SplitCam è un software di streaming gratuito per Windows e macOS — l'encoder che invia il tuo video alla tua piattaforma cam. Installalo; senza filigrana."),
            ("Installa e accoppia il software Lovense",
             "Installa Lovense Connect / Lovense Stream (l'app desktop ufficiale). Accendi il toy e accoppialo via Bluetooth perché l'app lo mostri come connesso."),
            ("Collega Lovense alla tua piattaforma cam",
             "Nell'app Lovense collega il tuo account cam così il toy reagisce ai token / mance degli spettatori. La maggior parte delle grandi piattaforme cam è supportata."),
            ("Aggiungi l'overlay Lovense in SplitCam",
             "Lovense fornisce un'URL di overlay / widget. Aggiungila come livello <strong>Browser</strong> nella tua scena SplitCam così gli spettatori vedono lo stato del toy e le mance recenti a schermo."),
            ("Componi la scena e Go Live",
             "Aggiungi la camera e gli altri overlay, incolla la chiave RTMP della tua piattaforma cam in SplitCam e clicca <strong>Go Live</strong>. Il toy reagisce alle mance in tempo reale."),
        ],
        "tips": [
            ("Usa il Lovense SplitCam Toolset ufficiale", "Lovense pubblica un toolset specifico per SplitCam con la sua guida di installazione — aggiunge l'overlay attività-toy e alert-mance pensato per SplitCam."),
            ("Aggiorna la Lovense Cam Extension", "Il toolset richiede una Lovense Cam Extension recente (30.1.4 o successiva) — aggiornala prima del live."),
            ("Tieni il toy carico", "Una batteria a terra a metà show uccide la parte interattiva — caricalo a fondo prima di andare live."),
            ("Testa la reazione al token", "Manda una piccola mancia di prova per confermare che il toy reagisce prima di aprire la stanza."),
            ("Controlla i requisiti di versione", "Il Lovense SplitCam Toolset richiede SplitCam 10.4.5 o successivo. La Lovense Cam Extension copre ufficialmente Chaturbate, Stripchat, BongaCams, MyFreeCams e CamSoda — per qualsiasi altro sito, usa l'integrazione Generic URL di Lovense."),
        ],
        "faq": [
            ("Lovense supporta SplitCam ufficialmente?", "Sì — Lovense documenta un «Lovense SplitCam Toolset» ufficiale con la sua guida di installazione, e SplitCam porta un plugin Lovense ufficiale. L'integrazione è supportata da entrambi i lati."),
            ("Il toy si collega direttamente a SplitCam?", "No — il toy si accoppia con l'app Lovense; SplitCam mostra l'overlay Lovense e trasmette la tua camera."),
            ("Quali siti cam supportano Lovense?", "La Cam Extension di Lovense supporta ufficialmente Chaturbate, Stripchat, BongaCams, MyFreeCams e CamSoda, con supporto variabile per altri — controlla la lista attuale nell'app Lovense."),
            ("Posso mostrare le mance recenti a schermo?", "Sì — aggiungi l'URL del widget Lovense come livello Browser in SplitCam."),
        ],
    },
    {
        "slug": "multistream-cams", "name": "Più siti cam",
        "title": "Trasmettere su più siti cam contemporaneamente con SplitCam",
        "desc": "Trasmettere su Chaturbate, BongaCams, CAM4, Stripchat e altri contemporaneamente con la multidiffusione gratuita di SplitCam. Un clic, senza filigrana.",
        "kw": "trasmettere su più siti cam, multistream cam, multidiffusione cam, trasmettere su chaturbate e bongacams insieme, software multistream cam, multistream rtmp",
        "h1html": 'Come trasmettere su <span class="accent">più siti cam</span> contemporaneamente',
        "h1short": "Multidiffusione cam",
        "card": "Trasmettere su più siti cam contemporaneamente.",
        "intro": "<strong style='color:var(--text)'>SplitCam</strong> gratuito può trasmettere un'unica codifica su <strong style='color:var(--text)'>più siti cam contemporaneamente</strong> — MyFreeCams, Chaturbate, BongaCams, CAM4, Stripchat e altri. Senza filigrana, in un clic.",
        "quick": "Per trasmettere su più siti cam in una volta: installare SplitCam, comporre la scena, ottenere l'URL server RTMP e la stream key da ogni sito cam, aggiungerli tutti nelle impostazioni di multidiffusione di SplitCam, cliccare Go Live una volta."
                 "<ol><li>Installare SplitCam.</li><li>Aggiungere camera + scena.</li>"
                 "<li>Ottenere una chiave RTMP da ogni sito cam.</li>"
                 "<li>Aggiungere tutte le chiavi nella multidiffusione di SplitCam.</li>"
                 "<li>Premere Go Live una volta.</li></ol>",
        "steps": [
            ("Installa SplitCam",
             "SplitCam è un software di streaming gratuito per Windows e macOS con multidiffusione integrata. Installalo — senza filigrana, senza registrazione."),
            ("Configura camera e scena",
             "Apri SplitCam, aggiungi la webcam e componi la scena con overlay e filtri. Un'unica scena alimenta ogni destinazione."),
            ("Ottieni una chiave RTMP da ogni sito cam",
             "Su ogni piattaforma cam abilita la trasmissione esterna / RTMP e copia il suo <strong>URL server</strong> e la <strong>stream key</strong>. Ripeti per ogni sito su cui vuoi trasmettere — guarda le guide individuali per i percorsi esatti."),
            ("Aggiungi ogni destinazione in SplitCam",
             "Apri <strong>Stream Settings</strong> e aggiungi ogni sito cam come destinazione RTMP personalizzata — incolla URL server e chiave. Spunta tutti quelli che vuoi in diretta."),
            ("Clicca Go Live una volta",
             "Premi <strong>Go Live</strong>. SplitCam invia il tuo stream contemporaneamente a ogni sito cam selezionato, in peer-to-peer, da un'unica codifica — senza costi extra."),
        ],
        "tips": [
            ("Attento al tuo upload", "La multidiffusione moltiplica il carico di upload. Ogni destinazione consuma il proprio bitrate — assicurati che la connessione regga la somma."),
            ("Controlla le regole di ogni piattaforma", "Alcuni siti cam vietano la trasmissione simultanea altrove — verifica prima di multidiffondere."),
            ("Cavo — qui non puoi permetterti un calo", "La multidiffusione moltiplica il carico di upload, quindi un singolo calo Wi-Fi può bloccare tutte le destinazioni in una volta. Il cavo qui non è opzionale."),
            ("Osserva il monitor di stato", "SplitCam mostra lo stato per destinazione — togli un sito se il tuo upload non regge."),
        ],
        "faq": [
            ("La multidiffusione in SplitCam è gratuita?", "Sì — la multidiffusione è integrata e gratuita, senza costi per destinazione, senza filigrana."),
            ("Su quanti siti cam posso trasmettere contemporaneamente?", "Tanti quanti la tua banda di upload regge — ogni destinazione consuma il proprio bitrate."),
            ("Usa un relay cloud?", "No — SplitCam invia gli stream in peer-to-peer direttamente dal tuo PC al server di ingest di ciascuna piattaforma."),
            ("La multidiffusione rallenta il PC?", "La codifica si fa una volta e si riutilizza; la codifica hardware tiene basso il carico CPU. La banda di upload è il vero limite."),
        ],
    },
    {
        "slug": "livejasmin", "name": "LiveJasmin",
        "title": "Trasmettere su LiveJasmin con SplitCam — Encoder esterno",
        "desc": "Trasmettere su LiveJasmin con SplitCam gratis — encoder esterno del Model Center, setup HD 1080p, scene multicamera e overlay. Senza filigrana.",
        "kw": "trasmettere su livejasmin, livejasmin, livejasmin broadcast, livejasmin obs, livejasmin external encoder, livejasmin rtmp, livejasmin stream key",
        "h1html": 'Come trasmettere su <span class="accent">LiveJasmin</span> con SplitCam',
        "h1short": "Trasmettere su LiveJasmin",
        "card": "Setup encoder esterno per il Model Center HD-only di LiveJasmin.",
        "intro": "LiveJasmin è l'ammiraglia di Docler Holding — uno dei più grandi network cam al mondo e una piattaforma solo HD. Il suo broadcaster preferito è il client proprietario <strong>JasminCAM</strong>, ma il Model Center espone anche una via standard <strong>External Encoder</strong> a cui si collega <strong style='color:var(--text)'>SplitCam</strong> gratuito — così trasmetti con scene multicamera, filtri beauty e overlay sullo stesso flusso HD.",
        "quick": "Per trasmettere su LiveJasmin con SplitCam: installare SplitCam, comporre la scena HD, nel Model Center andare in <em>Settings → Broadcast → External Encoder</em>, copiare URL del server e stream key, incollare in SplitCam, premere Go Live."
                 "<ol><li>Installare SplitCam.</li><li>Aggiungere camera + scena HD.</li>"
                 "<li>Prendere URL e stream key dal Model Center.</li>"
                 "<li>Incollare in SplitCam.</li>"
                 "<li>Premere Go Live.</li></ol>",
        "key_how": "Accedi su <strong>modelcenter.livejasmin.com</strong>, apri <strong>Settings → Broadcast → External Encoder</strong>. Il Model Center mostra una <strong>URL del server</strong> e una <strong>stream key</strong> legate al tuo account — copia entrambe nei campi RTMP personalizzato di SplitCam. <strong>Nota:</strong> i nuovi account devono essere approvati (48–72 ore) prima che compaia l'opzione encoder esterno, e la piattaforma impone uscita solo in HD.",
        "tips": [
            ("HD o ti declassano", "LiveJasmin è solo HD — sotto i 1280×720 rischi di apparire solo nelle liste a paga bassa, sotto i 1080p perdi l'idoneità 'Premium'. Punta a 1920×1080 a 30 fps, 4.000–6.000 Kbps."),
            ("JasminCAM vs encoder esterno", "JasminCAM, il client ufficiale Docler, dà la conformità HD più pulita, ma gli encoder esterni (OBS, SplitCam, vMix) sono ufficialmente supportati una volta approvato l'account — e sbloccano scene multicamera e overlay che JasminCAM non sa fare."),
            ("Free chat ≠ show privato", "Il Free chat è solo preview — niente nudo. I soldi sono nei privati e nei Gold show. Pensa la scena perché tenga forte sia vestita SIA in modalità show."),
            _T_ETH,
        ],
        "faq": [
            ("LiveJasmin supporta ufficialmente encoder esterni come SplitCam?", "Sì — il Model Center include l'opzione External Encoder in Settings → Broadcast. JasminCAM è il client consigliato, ma OBS, SplitCam e gli altri encoder RTMP sono esplicitamente elencati come supportati una volta approvato l'account modella."),
            ("Dove prendo la stream key di LiveJasmin?", "Nel Model Center: Settings → Broadcast → External Encoder. URL del server e stream key unica compaiono lì — copia entrambe nei campi RTMP personalizzato di SplitCam. La chiave è legata al tuo account; trattala come una password."),
            ("Che bitrate uso per LiveJasmin?", "LiveJasmin è solo HD — punta a 1920×1080 a 30 fps, 4.000–6.000 Kbps con keyframe ogni 2 secondi. Sotto perdi l'etichetta Premium e ti declassano."),
            ("SplitCam è gratis con LiveJasmin?", "Sì — SplitCam è gratis, senza filigrana e senza limite di tempo. L'unico 'costo' è centrare i requisiti HD di LiveJasmin, cosa che SplitCam fa nativamente con la composizione di scena 1080p e i filtri beauty."),
        ],
        "steps": [
            ("Scarica e installa SplitCam",
             "SplitCam è un software di live streaming gratuito per Windows e macOS — senza registrazione, senza carta, senza filigrana. È l'encoder che manda il tuo video HD a LiveJasmin."),
            ("Componi la scena HD",
             "Apri SplitCam e aggiungi la webcam in modalità 1080p. Sovrapponi overlay, testo, una seconda camera o il telefono, filtri beauty o sfondo IA — LiveJasmin richiede qualità HD e la tua scena composta deve sembrare premium sia in Free chat SIA in privato."),
            ("Prendi URL e stream key di LiveJasmin",
             "Accedi su <strong>modelcenter.livejasmin.com</strong> (l'account deve essere prima approvato — di solito 48–72 ore dopo la registrazione). Apri <strong>Settings → Broadcast → External Encoder</strong>. La pagina mostra una <strong>URL del server</strong> e una <strong>stream key</strong> unica. Copia entrambe."),
            ("Collega SplitCam a LiveJasmin",
             "In SplitCam apri <strong>Stream Settings</strong>, incolla URL del server LiveJasmin e stream key nei campi RTMP personalizzato. Imposta il bitrate a 4.000–6.000 Kbps a 1920×1080, 30 fps, keyframe 2 secondi. Lancia prima lo speed test integrato — i flussi HD sono esigenti."),
            ("Clicca Go Live",
             "Premi <strong>Go Live</strong> in SplitCam, poi vai online nel Model Center di LiveJasmin. In ~10 secondi il tuo feed HD raggiunge la rete LiveJasmin. Le dirette successive sono un clic — apri SplitCam, Go Live, poi vai online su LiveJasmin."),
        ],
    },
    {
        "slug": "myfreecams", "name": "MyFreeCams",
        "title": "Trasmettere su MyFreeCams (MFC) con SplitCam",
        "desc": "Trasmettere su MyFreeCams con SplitCam gratis — broadcaster esterno del Model Admin, economia a token MFC, scene multicamera e overlay. Senza filigrana.",
        "kw": "trasmettere su myfreecams, myfreecams, mfc, myfreecams broadcast, myfreecams obs, mfc external encoder, mfc rtmp, mfc stream key",
        "h1html": 'Come trasmettere su <span class="accent">MyFreeCams</span> con SplitCam',
        "h1short": "Trasmettere su MyFreeCams",
        "card": "Setup broadcaster esterno per il Model Admin a token di MFC.",
        "intro": "MyFreeCams (MFC) è una delle piattaforme cam più longeve — economia di puri token, niente trafila di approvazione modella, e una base fedele di membri Premium. Il suo <em>Model Web Broadcaster</em> di default è uno strumento da browser monocamera, ma il Model Admin espone anche un'opzione <strong>External Broadcaster</strong> a cui si collega <strong style='color:var(--text)'>SplitCam</strong> gratuito — sbloccando scene multicamera, overlay e filtri sullo stesso flusso monetizzato a token.",
        "quick": "Per trasmettere su MyFreeCams con SplitCam: installare SplitCam, comporre la scena, in <em>Model Admin → Broadcaster</em> passare da Web Broadcaster a External Broadcaster, copiare URL del server e stream key, incollare in SplitCam, premere Go Live."
                 "<ol><li>Installare SplitCam.</li><li>Aggiungere camera + scena.</li>"
                 "<li>Prendere URL e stream key dal Model Admin.</li>"
                 "<li>Incollare in SplitCam.</li>"
                 "<li>Premere Go Live.</li></ol>",
        "key_how": "Accedi a MyFreeCams, apri <strong>Model Admin → Broadcaster</strong> e passa da <em>Web Broadcaster</em> a <strong>External Broadcaster</strong>. La pagina mostra una <strong>URL del server</strong> (rtmp://publish.myfreecams.com…) e una <strong>stream key</strong> legate al tuo account modella — copia entrambe nei campi RTMP personalizzato di SplitCam. La chiave è legata all'account; trattala come una password e resettala se trapela.",
        "tips": [
            ("Token MFC, non abbonamenti", "MFC è pura economia di mance/token — i membri Premium possono fare il privato, ma il grosso dell'incasso arriva dalle mance in free chat. Pensa una scena che renda vestita e casual, non solo in show nudo."),
            ("Web Broadcaster vs External — scegli una volta", "Il Web Broadcaster di default è monocamera, sorgente singola. External Broadcaster sblocca multi-scena, overlay e filtri beauty via SplitCam/OBS. Cambia in Model Admin → Broadcaster prima di andare in diretta."),
            ("Integrazione con MFC Alerts", "Le alert animate per le mance sullo schermo arrivano da mfcalerts.com — aggiungi l'URL dell'alert come layer Browser in SplitCam, sopra la camera. Vedi la nostra guida MFC Alerts per il setup completo dell'overlay."),
            _T_ETH,
        ],
        "faq": [
            ("MyFreeCams supporta ufficialmente broadcaster esterni come SplitCam?", "Sì — Model Admin ha un'opzione External Broadcaster che espone una URL del server RTMP standard e una stream key. OBS, SplitCam, vMix e gli altri encoder RTMP funzionano; MFC supporta esplicitamente l'opzione nella documentazione per modelle."),
            ("Dove trovo la mia stream key MFC?", "Model Admin → Broadcaster → passa a External Broadcaster. Sia la URL del server (rtmp://publish.myfreecams.com…) sia la stream key compaiono lì. Copia entrambe nei campi RTMP personalizzato di SplitCam."),
            ("Che bitrate uso per MyFreeCams?", "MFC accetta fino a ~6.000 Kbps con intervallo di keyframe di 2 secondi. Spingi 1920×1080 a 30 fps, 3.500–6.000 Kbps — il tuo upload è il vero limite. Lancia prima lo speed test di SplitCam."),
            ("SplitCam è gratis con MyFreeCams?", "Sì — SplitCam è gratis, senza filigrana e senza limite di tempo. L'opzione External Broadcaster è gratis dentro Model Admin. Costo totale broadcaster: zero."),
        ],
        "steps": [
            ("Scarica e installa SplitCam",
             "SplitCam è un software di live streaming gratuito per Windows e macOS — senza registrazione, senza carta, senza filigrana. È l'encoder che manda il tuo video a MyFreeCams."),
            ("Componi la scena",
             "Apri SplitCam e aggiungi la webcam. Sovrapponi overlay, testo, una seconda camera o il telefono, filtri beauty o sfondo IA — tutto applicato in diretta prima che il flusso esca dal tuo PC. Pensa ad aggiungere l'URL di mfcalerts.com come layer Browser per le alert animate delle mance."),
            ("Passa a External Broadcaster nel Model Admin",
             "Accedi a MyFreeCams. Apri <strong>Model Admin → Broadcaster</strong>. Passa da <em>Web Broadcaster</em> a <strong>External Broadcaster</strong>. La pagina mostra una <strong>URL del server</strong> e una <strong>stream key</strong> unica. Copia entrambe."),
            ("Collega SplitCam a MyFreeCams",
             "In SplitCam apri <strong>Stream Settings</strong>, incolla URL del server MFC e stream key nei campi RTMP personalizzato. Imposta il bitrate a 3.500–6.000 Kbps a 1920×1080, 30 fps, con keyframe ogni 2 secondi. Lancia prima lo speed test integrato."),
            ("Clicca Go Live",
             "Premi <strong>Go Live</strong> in SplitCam. In ~10 secondi il tuo flusso raggiunge MyFreeCams. Le dirette successive sono un clic — apri SplitCam, Go Live."),
        ],
    },
    {
        "slug": "cherry-tv", "name": "Cherry.tv",
        "title": "Trasmettere su Cherry.tv con SplitCam — Encoder esterno",
        "desc": "Trasmettere su Cherry.tv con SplitCam gratis — encoder esterno dello Streamer Dashboard, piattaforma cripto-friendly, scene multicamera. Senza filigrana.",
        "kw": "trasmettere su cherry.tv, cherry.tv, cherry tv, cherry.tv broadcast, cherry.tv obs, cherry.tv external encoder, cherry.tv rtmp, cherry.tv stream key",
        "h1html": 'Come trasmettere su <span class="accent">Cherry.tv</span> con SplitCam',
        "h1short": "Trasmettere su Cherry.tv",
        "card": "Setup encoder esterno per lo Streamer Dashboard di Cherry.tv.",
        "intro": "Cherry.tv è una piattaforma cam più recente, in rapida crescita, con un'anima Web3 — pagamenti cripto-friendly e barriere d'ingresso più basse delle reti legacy come LiveJasmin. Il broadcaster di default va da browser, ma lo <strong>Streamer Dashboard</strong> espone anche una via standard <strong>External Encoder</strong> a cui si collega <strong style='color:var(--text)'>SplitCam</strong> gratuito — così trasmetti con scene multicamera, overlay e filtri.",
        "quick": "Per trasmettere su Cherry.tv con SplitCam: installare SplitCam, comporre la scena, nello Streamer Dashboard aprire <em>Broadcast Settings → External Encoder</em>, copiare URL del server e stream key, incollare in SplitCam, premere Go Live."
                 "<ol><li>Installare SplitCam.</li><li>Aggiungere camera + scena.</li>"
                 "<li>Prendere URL e stream key dallo Streamer Dashboard.</li>"
                 "<li>Incollare in SplitCam.</li>"
                 "<li>Premere Go Live.</li></ol>",
        "key_how": "Accedi al tuo account streamer di Cherry.tv, apri lo <strong>Streamer Dashboard</strong> e vai in <strong>Broadcast Settings → External Encoder</strong>. La pagina mostra una <strong>URL del server</strong> e una <strong>stream key</strong> legate al tuo account — copia entrambe nei campi RTMP personalizzato di SplitCam. I nuovi account streamer devono completare una verifica di base (di solito veloce — Cherry.tv ha un onboarding più snello rispetto alle reti cam legacy) prima che l'opzione encoder esterno sia pienamente attiva.",
        "tips": [
            ("Ingresso più snello, traffico in crescita", "L'onboarding di Cherry.tv è più rapido di quello delle piattaforme legacy (niente revisione stile Docler da 72 ore). Unito al traffico in crescita, è un buon spot early-mover per costruire una base di follower prima che la concorrenza si stringa."),
            ("Pagamenti in cripto disponibili", "Cherry.tv supporta il prelievo in cripto oltre al fiat standard — utile se sei in una zona dove i pagamenti delle reti cam tradizionali sono lenti o limitati."),
            ("Browser broadcaster vs esterno", "Il broadcaster da browser è comodo ma a sorgente singola. SplitCam via External Encoder sblocca scene multicamera, overlay, filtri beauty e sfondo IA che lo strumento da browser non può fare."),
            _T_ETH,
        ],
        "faq": [
            ("Cherry.tv supporta ufficialmente encoder esterni come SplitCam?", "Sì — lo Streamer Dashboard include External Encoder dentro Broadcast Settings. La piattaforma fornisce una URL del server RTMP standard e una stream key; OBS, SplitCam e gli altri encoder RTMP si collegano senza problemi."),
            ("Dove prendo la mia stream key Cherry.tv?", "Streamer Dashboard → Broadcast Settings → External Encoder. URL del server e stream key compaiono lì — copia entrambe nei campi RTMP personalizzato di SplitCam. La chiave è legata all'account; trattala come una password."),
            ("Che bitrate uso per Cherry.tv?", "Cherry.tv accetta le impostazioni cam-quality standard — spingi 1920×1080 a 30 fps, 3.500–6.000 Kbps con keyframe ogni 2 secondi. Lancia prima lo speed test integrato di SplitCam."),
            ("SplitCam è gratis con Cherry.tv?", "Sì — SplitCam è gratis, senza filigrana e senza limite di tempo. L'opzione encoder esterno di Cherry.tv è gratis da attivare. Costo totale broadcaster: zero."),
        ],
        "steps": [
            ("Scarica e installa SplitCam",
             "SplitCam è un software di live streaming gratuito per Windows e macOS — senza registrazione, senza carta, senza filigrana. È l'encoder che manda il tuo video a Cherry.tv."),
            ("Componi la scena",
             "Apri SplitCam e aggiungi la webcam. Sovrapponi overlay, testo, una seconda camera o il telefono, filtri beauty o sfondo IA — tutto applicato in diretta. Il pubblico di Cherry.tv è più giovane e smaliziato sulle piattaforme, quindi una scena curata aiuta a distinguersi."),
            ("Prendi URL e stream key di Cherry.tv",
             "Accedi al tuo account streamer di Cherry.tv, apri lo <strong>Streamer Dashboard</strong> e vai in <strong>Broadcast Settings → External Encoder</strong>. La pagina mostra una <strong>URL del server</strong> e una <strong>stream key</strong> unica. Copia entrambe."),
            ("Collega SplitCam a Cherry.tv",
             "In SplitCam apri <strong>Stream Settings</strong>, incolla URL del server Cherry.tv e stream key nei campi RTMP personalizzato. Imposta il bitrate a 3.500–6.000 Kbps a 1920×1080, 30 fps, con keyframe ogni 2 secondi. Lancia prima lo speed test integrato."),
            ("Clicca Go Live",
             "Premi <strong>Go Live</strong> in SplitCam, poi vai online dallo Streamer Dashboard su Cherry.tv. In ~10 secondi il tuo flusso raggiunge Cherry.tv. Le dirette successive sono un clic — apri SplitCam, Go Live, poi vai online su Cherry.tv."),
        ],
    },
    {
        "slug": "amateurtv", "name": "AmateurTV",
        "title": "Trasmettere su AmateurTV con SplitCam — Encoder esterno",
        "desc": "Trasmettere su AmateurTV con SplitCam gratis — encoder esterno del Model Panel, network cam ispanofono, scene multicamera e overlay. Senza filigrana.",
        "kw": "trasmettere su amateurtv, amateurtv, amateur.tv, amateurtv broadcast, amateurtv obs, amateurtv external encoder, amateurtv rtmp, amateurtv stream key",
        "h1html": 'Come trasmettere su <span class="accent">AmateurTV</span> con SplitCam',
        "h1short": "Trasmettere su AmateurTV",
        "card": "Setup dell'encoder esterno per il network ispanofono di AmateurTV.",
        "intro": "AmateurTV è il network cam ispanofono di riferimento — traffico forte in Spagna, Messico, Argentina e in tutta la LatAm. Il broadcaster di default del Model Panel funziona da browser, ma viene esposta anche una via standard <strong>External Encoder</strong> a cui si collega <strong style='color:var(--text)'>SplitCam</strong> gratuito — così trasmetti con scene multicamera, filtri beauty e overlay verso un pubblico ispanofono che le reti US-centric servono male.",
        "quick": "Per trasmettere su AmateurTV con SplitCam: installare SplitCam, comporre la scena, nel Model Panel aprire <em>Broadcast Settings → External Encoder</em>, copiare URL del server e stream key, incollare in SplitCam, premere Go Live."
                 "<ol><li>Installare SplitCam.</li><li>Aggiungere camera + scena.</li>"
                 "<li>Prendere URL e stream key dal Model Panel.</li>"
                 "<li>Incollare in SplitCam.</li>"
                 "<li>Premere Go Live.</li></ol>",
        "key_how": "Accedi al tuo account modella di AmateurTV, apri il <strong>Model Panel</strong> e vai in <strong>Broadcast Settings → External Encoder</strong>. La pagina mostra una <strong>URL del server</strong> e una <strong>stream key</strong> legate al tuo account — copia entrambe nei campi RTMP personalizzato di SplitCam. Gli account nuovi devono superare la verifica ID prima di andare in diretta.",
        "tips": [
            ("Pubblico ispanofono prima di tutto", "Il traffico di AmateurTV è in larga parte in spagnolo — Spagna di giorno, LatAm nelle ore serali statunitensi. Titoli di stanza, scritte in sovrimpressione e overlay in spagnolo rendono molto più dell'inglese da solo."),
            ("Il fuso LatAm è il tuo prime time", "Il picco di traffico coincide con la sera LatAm (UTC-3 a UTC-6). Se hai flessibilità, trasmettere tarda sera CET / mattina asiatica colpisce contemporaneamente Spagna e LatAm."),
            ("Payout mid-tier solidi", "Non è l'RPM più alto del settore, ma AmateurTV paga regolare e la nicchia ispanofona è molto meno affollata rispetto ai top network statunitensi."),
            _T_ETH,
        ],
        "faq": [
            ("AmateurTV supporta ufficialmente encoder esterni come SplitCam?", "Sì — il Model Panel include l'opzione External Encoder in Broadcast Settings. AmateurTV fornisce una URL del server RTMP standard e una stream key; OBS, SplitCam, vMix e gli altri encoder RTMP si collegano."),
            ("Dove prendo la mia stream key di AmateurTV?", "Model Panel → Broadcast Settings → External Encoder. Sia la URL del server sia la stream key compaiono lì. Copia entrambe nei campi RTMP personalizzato di SplitCam. La chiave è legata all'account."),
            ("Che bitrate uso per AmateurTV?", "Impostazioni cam-quality standard — spingi 1920×1080 a 30 fps, 3.500–6.000 Kbps con keyframe ogni 2 secondi. Lancia prima lo speed test integrato di SplitCam."),
            ("SplitCam è gratis con AmateurTV?", "Sì — SplitCam è gratis, senza filigrana e senza limite di tempo. L'opzione encoder esterno di AmateurTV è gratis da attivare."),
        ],
        "steps": [
            ("Scarica e installa SplitCam",
             "SplitCam è un software di live streaming gratuito per Windows e macOS — senza registrazione, senza carta, senza filigrana. È l'encoder che manda il tuo video ad AmateurTV."),
            ("Componi la scena",
             "Apri SplitCam e aggiungi la webcam. Sovrapponi overlay, testo, una seconda camera o il telefono, filtri beauty o sfondo IA. Metti i testi degli overlay in spagnolo — il pubblico ispanofono di AmateurTV lo nota e converte meglio."),
            ("Prendi URL e stream key di AmateurTV",
             "Accedi al tuo account modella di AmateurTV, apri il <strong>Model Panel</strong> e vai in <strong>Broadcast Settings → External Encoder</strong>. La pagina mostra una <strong>URL del server</strong> e una <strong>stream key</strong> unica. Copia entrambe."),
            ("Collega SplitCam ad AmateurTV",
             "In SplitCam apri <strong>Stream Settings</strong>, incolla URL del server di AmateurTV e stream key nei campi RTMP personalizzato. Imposta il bitrate a 3.500–6.000 Kbps a 1920×1080, 30 fps, con keyframe ogni 2 secondi. Lancia prima lo speed test integrato."),
            ("Clicca Go Live",
             "Premi <strong>Go Live</strong> in SplitCam, poi vai online dal Model Panel su AmateurTV. In ~10 secondi il tuo flusso raggiunge la rete. Le dirette successive sono un clic — apri SplitCam, Go Live."),
        ],
    },
    {
        "slug": "camster", "name": "Camster",
        "title": "Trasmettere su Camster con SplitCam — Encoder esterno",
        "desc": "Trasmettere su Camster con SplitCam gratis — encoder esterno del Model Hub, piattaforma cam mid-tier, scene multicamera e overlay. Senza filigrana.",
        "kw": "trasmettere su camster, camster, camster broadcast, camster obs, camster external encoder, camster rtmp, camster stream key",
        "h1html": 'Come trasmettere su <span class="accent">Camster</span> con SplitCam',
        "h1short": "Trasmettere su Camster",
        "card": "Setup dell'encoder esterno per il Model Hub di Camster.",
        "intro": "Camster è una piattaforma cam mid-tier consolidata — più piccola di Chaturbate o LiveJasmin, ma con una base utenti fedele e payout corretti. Il broadcaster di default del Model Hub funziona da browser, ma viene esposta anche una via standard <strong>External Encoder</strong> a cui si collega <strong style='color:var(--text)'>SplitCam</strong> gratuito — così trasmetti con scene multicamera, overlay e filtri che il broadcaster nativo non può dare.",
        "quick": "Per trasmettere su Camster con SplitCam: installare SplitCam, comporre la scena, nel Model Hub aprire <em>Broadcast Settings → External Encoder</em>, copiare URL del server e stream key, incollare in SplitCam, premere Go Live."
                 "<ol><li>Installare SplitCam.</li><li>Aggiungere camera + scena.</li>"
                 "<li>Prendere URL e stream key dal Model Hub.</li>"
                 "<li>Incollare in SplitCam.</li>"
                 "<li>Premere Go Live.</li></ol>",
        "key_how": "Accedi al tuo account modella di Camster, apri il <strong>Model Hub</strong> e vai in <strong>Broadcast Settings → External Encoder</strong>. La pagina mostra una <strong>URL del server</strong> e una <strong>stream key</strong> legate al tuo account — copia entrambe nei campi RTMP personalizzato di SplitCam. La chiave è legata all'account; trattala come una password.",
        "tips": [
            ("Mid-tier = meno concorrenza", "Camster ha traffico stabile ma molte meno broadcaster rispetto ai network top — è più facile finire in homepage con una scena curata e un calendario costante."),
            ("Broadcaster da browser vs esterno", "Il broadcaster da browser è a sorgente singola. SplitCam via External Encoder sblocca scene multicamera, overlay, filtri beauty e sfondo IA."),
            ("Payout stabili, split corretto", "Lo split di Camster è corretto per il mid-tier — non il più alto del settore, ma pagamenti mensili puntuali e poche lamentele sui ritardi."),
            _T_ETH,
        ],
        "faq": [
            ("Camster supporta ufficialmente encoder esterni come SplitCam?", "Sì — il Model Hub include l'opzione External Encoder in Broadcast Settings. URL del server RTMP standard e stream key; OBS, SplitCam e gli altri encoder RTMP si collegano."),
            ("Dove prendo la mia stream key di Camster?", "Model Hub → Broadcast Settings → External Encoder. URL del server e stream key compaiono lì. Copia entrambe nei campi RTMP personalizzato di SplitCam."),
            ("Che bitrate uso per Camster?", "Impostazioni cam-quality standard — spingi 1920×1080 a 30 fps, 3.500–6.000 Kbps con keyframe ogni 2 secondi. Lancia prima lo speed test integrato di SplitCam."),
            ("SplitCam è gratis con Camster?", "Sì — SplitCam è gratis, senza filigrana e senza limite di tempo. L'opzione encoder esterno di Camster è gratis."),
        ],
        "steps": [
            ("Scarica e installa SplitCam",
             "SplitCam è un software di live streaming gratuito per Windows e macOS — senza registrazione, senza carta, senza filigrana."),
            ("Componi la scena",
             "Apri SplitCam e aggiungi la webcam. Sovrapponi overlay, testo, una seconda camera o il telefono, filtri beauty o sfondo IA — tutto applicato in diretta."),
            ("Prendi URL e stream key di Camster",
             "Accedi al tuo account modella di Camster, apri il <strong>Model Hub</strong> e vai in <strong>Broadcast Settings → External Encoder</strong>. La pagina mostra una <strong>URL del server</strong> e una <strong>stream key</strong> unica. Copia entrambe."),
            ("Collega SplitCam a Camster",
             "In SplitCam apri <strong>Stream Settings</strong>, incolla URL del server di Camster e stream key nei campi RTMP personalizzato. Imposta il bitrate a 3.500–6.000 Kbps a 1920×1080, 30 fps, con keyframe ogni 2 secondi. Lancia prima lo speed test integrato."),
            ("Clicca Go Live",
             "Premi <strong>Go Live</strong> in SplitCam, poi vai online dal Model Hub. In ~10 secondi il tuo flusso raggiunge Camster."),
        ],
    },
    {
        "slug": "camversity", "name": "Camversity",
        "title": "Trasmettere su Camversity con SplitCam — Encoder esterno",
        "desc": "Trasmettere su Camversity con SplitCam gratis — encoder esterno del Performer Dashboard, piattaforma cam indipendente, scene multicamera. Senza filigrana.",
        "kw": "trasmettere su camversity, camversity, camversity broadcast, camversity obs, camversity external encoder, camversity rtmp, camversity stream key",
        "h1html": 'Come trasmettere su <span class="accent">Camversity</span> con SplitCam',
        "h1short": "Trasmettere su Camversity",
        "card": "Setup dell'encoder esterno per il Performer Dashboard di Camversity.",
        "intro": "Camversity è una piattaforma cam indipendente in crescita, con focus su strumenti pensati per il performer e commissioni più basse rispetto ai network legacy. Il broadcaster di default del Performer Dashboard funziona da browser, ma viene esposta anche una via standard <strong>External Encoder</strong> a cui si collega <strong style='color:var(--text)'>SplitCam</strong> gratuito — così trasmetti con scene multicamera, overlay e filtri.",
        "quick": "Per trasmettere su Camversity con SplitCam: installare SplitCam, comporre la scena, nel Performer Dashboard aprire <em>Stream Settings → External Encoder</em>, copiare URL del server e stream key, incollare in SplitCam, premere Go Live."
                 "<ol><li>Installare SplitCam.</li><li>Aggiungere camera + scena.</li>"
                 "<li>Prendere URL e stream key dal Performer Dashboard.</li>"
                 "<li>Incollare in SplitCam.</li>"
                 "<li>Premere Go Live.</li></ol>",
        "key_how": "Accedi al tuo account performer di Camversity, apri il <strong>Performer Dashboard</strong> e vai in <strong>Stream Settings → External Encoder</strong>. La pagina mostra una <strong>URL del server</strong> e una <strong>stream key</strong> legate al tuo account — copia entrambe nei campi RTMP personalizzato di SplitCam. Gli account nuovi superano una verifica ID standard prima di andare in diretta.",
        "tips": [
            ("Split più favorevole al performer", "Lo split di Camversity è più favorevole al performer rispetto ai network legacy — vale la pena confrontarlo con la tua piattaforma principale se sei agli inizi del cam."),
            ("Onboarding più snello di Docler", "La verifica di Camversity è più rapida delle 48–72 ore di LiveJasmin, restando comunque seria (nessun modello non verificato). Buon compromesso."),
            ("Componi una scena, non solo una webcam", "Il broadcaster di default del Performer Dashboard è a sorgente singola. SplitCam via External Encoder sblocca multicamera, overlay, filtri beauty."),
            _T_ETH,
        ],
        "faq": [
            ("Camversity supporta ufficialmente encoder esterni come SplitCam?", "Sì — il Performer Dashboard include l'opzione External Encoder in Stream Settings. URL del server RTMP standard e stream key; OBS, SplitCam, vMix si collegano."),
            ("Dove prendo la mia stream key di Camversity?", "Performer Dashboard → Stream Settings → External Encoder. URL del server e stream key compaiono lì."),
            ("Che bitrate uso per Camversity?", "Spingi 1920×1080 a 30 fps, 3.500–6.000 Kbps con keyframe ogni 2 secondi. Lancia prima lo speed test integrato di SplitCam."),
            ("SplitCam è gratis con Camversity?", "Sì — SplitCam è gratis, senza filigrana e senza limite di tempo. L'opzione encoder esterno di Camversity è gratis."),
        ],
        "steps": [
            ("Scarica e installa SplitCam",
             "SplitCam è un software di live streaming gratuito per Windows e macOS — senza registrazione, senza carta, senza filigrana."),
            ("Componi la scena",
             "Apri SplitCam e aggiungi la webcam. Sovrapponi overlay, testo, una seconda camera o il telefono, filtri beauty o sfondo IA."),
            ("Prendi URL e stream key di Camversity",
             "Accedi al tuo account performer di Camversity, apri il <strong>Performer Dashboard</strong> e vai in <strong>Stream Settings → External Encoder</strong>. La pagina mostra una <strong>URL del server</strong> e una <strong>stream key</strong> unica. Copia entrambe."),
            ("Collega SplitCam a Camversity",
             "In SplitCam apri <strong>Stream Settings</strong>, incolla URL del server di Camversity e stream key nei campi RTMP personalizzato. Imposta il bitrate a 3.500–6.000 Kbps a 1920×1080, 30 fps, con keyframe ogni 2 secondi."),
            ("Clicca Go Live",
             "Premi <strong>Go Live</strong> in SplitCam, poi vai online dal Performer Dashboard. In ~10 secondi il tuo flusso raggiunge Camversity."),
        ],
    },
    {
        "slug": "skyprivate", "name": "SkyPrivate",
        "title": "Usare SkyPrivate con SplitCam — Camera virtuale Skype",
        "desc": "Usare SkyPrivate con SplitCam gratis come camera virtuale — chiamate cam private pay-per-minute via Skype, scene e filtri beauty. Senza filigrana.",
        "kw": "skyprivate, sky private cam, skyprivate splitcam, skyprivate virtual camera, skyprivate camera virtuale, skype cam privato, cam pay per minute",
        "h1html": 'Come usare <span class="accent">SkyPrivate</span> con SplitCam',
        "h1short": "SplitCam su SkyPrivate",
        "card": "Setup camera virtuale per le chiamate cam SkyPrivate basate su Skype.",
        "intro": "SkyPrivate è una piattaforma cam atipica — invece di un broadcast RTMP monetizza <strong>chiamate cam private pay-per-minute via Skype</strong>. Il cliente prenota e paga al minuto dal marketplace SkyPrivate, e la videochiamata vera e propria passa su Skype. <strong style='color:var(--text)'>SplitCam</strong> gratuito si collega come <strong>camera virtuale</strong>: componi la scena in SplitCam, poi scegli SplitCam come camera dentro Skype prima di rispondere a una chiamata prenotata via SkyPrivate.",
        "quick": "Per usare SkyPrivate con SplitCam: installa SplitCam, componi la scena, installa Skype con l'add-on SkyPrivate, in <em>Video Settings</em> di Skype seleziona SplitCam come camera e microfono, e rispondi alle chiamate prenotate via SkyPrivate — Skype consegna la tua scena composta al cliente."
                 "<ol><li>Installa SplitCam.</li><li>Componi la scena in SplitCam.</li>"
                 "<li>Installa Skype + add-on SkyPrivate.</li>"
                 "<li>Seleziona SplitCam come camera in Skype.</li>"
                 "<li>Rispondi alle chiamate.</li></ol>",
        "key_how": "SkyPrivate non usa RTMP né stream key — usa Skype come trasporto video con un add-on per la fatturazione al minuto. Installa Skype, installa l'add-on browser/desktop SkyPrivate, poi in Skype apri <strong>Settings → Audio &amp; Video → Camera</strong> e seleziona <strong>SplitCam</strong> al posto della tua webcam. La scena composta da SplitCam (overlay, multicamera, filtri beauty) è ciò che vede il cliente SkyPrivate via Skype.",
        "tips": [
            ("Niente RTMP — flusso camera virtuale", "Non cercare URL del server né stream key. SkyPrivate passa da Skype, e Skype vede SplitCam come una semplice webcam. Componi la scena in SplitCam, poi scegli SplitCam nelle impostazioni camera di Skype."),
            ("Imposta SplitCam anche come microfono", "Nelle impostazioni Audio di Skype scegli SplitCam come microfono oltre che come camera — così la riduzione rumore, l'audio mixato e la musica d'intro arrivano al cliente."),
            ("Fai una chiamata di test su Skype", "Prima della tua prima chiamata SkyPrivate a pagamento, fai una chiamata di test gratuita su Skype (Echo / Sound Test Service) per verificare che SplitCam sia la camera attiva e che la scena sia composta bene."),
            _T_TEST,
        ],
        "faq": [
            ("SkyPrivate usa RTMP o una stream key?", "Nessuno dei due. SkyPrivate gestisce prenotazione e fatturazione; il video vero e proprio passa da Skype. Non ti serve URL del server RTMP né stream key — basta configurare SplitCam come camera dentro Skype."),
            ("Come seleziono SplitCam in Skype per SkyPrivate?", "Apri Skype Settings → Audio &amp; Video → Camera, scegli SplitCam dalla lista. Fai lo stesso per Microphone. Le chiamate SkyPrivate arrivano poi come normali chiamate Skype con la tua scena SplitCam come feed camera."),
            ("Posso usare overlay e filtri beauty con SkyPrivate?", "Sì — componili dentro la scena SplitCam. Skype riceve solo il risultato composto come unico feed camera, quindi tutto ciò che SplitCam compone (overlay, filtri beauty, sfondo IA, scene multicamera) è visibile al cliente SkyPrivate."),
            ("SplitCam è gratuito per SkyPrivate?", "Sì — SplitCam è gratuito, senza filigrana e senza limite di tempo. Come camera virtuale per le chiamate SkyPrivate via Skype non aggiunge costi né branding alla chiamata."),
        ],
        "steps": [
            ("Installa SplitCam",
             "SplitCam è gratuito per Windows e macOS — senza registrazione, senza carta, senza filigrana. Per SkyPrivate fa da <strong>camera virtuale</strong> che Skype riconosce come una webcam qualsiasi."),
            ("Componi la scena in SplitCam",
             "Apri SplitCam e usa <strong>Media Layers +</strong> per aggiungere la webcam più overlay, testo, filtri beauty o sfondo IA. Questa scena composta è ciò che Skype consegnerà al cliente SkyPrivate."),
            ("Installa Skype e l'add-on SkyPrivate",
             "Installa Skype sullo stesso PC, accedi, poi installa l'add-on / app desktop SkyPrivate seguendo l'onboarding di SkyPrivate. L'add-on gestisce la fatturazione al minuto sul lato SkyPrivate."),
            ("Seleziona SplitCam come camera e mic in Skype",
             "In Skype apri <strong>Settings → Audio &amp; Video</strong>. Imposta <strong>Camera = SplitCam</strong> e <strong>Microphone = SplitCam</strong>. Lancia una chiamata di test rapida su Skype (Echo / Sound Test Service) per verificare resa video e audio."),
            ("Rispondi alle chiamate SkyPrivate",
             "Quando un cliente SkyPrivate prenota una chiamata a pagamento, arriva come chiamata Skype — rispondi. Vede la tua scena composta SplitCam; SkyPrivate fattura al minuto. Puoi modificare la scena durante la chiamata editandola in SplitCam — Skype aggiorna all'istante."),
        ],
    },
    {
        "slug": "manyvids", "name": "ManyVids",
        "title": "Andare in diretta su MV Live (ManyVids) con SplitCam",
        "desc": "Andare in diretta su MV Live di ManyVids con SplitCam gratis — encoder esterno del Creator Studio, scene multicamera e overlay. Senza filigrana.",
        "kw": "andare in diretta su manyvids, manyvids, mv live, manyvids live, manyvids broadcast, manyvids obs, mv live external encoder, manyvids stream key",
        "h1html": 'Come trasmettere su <span class="accent">MV Live</span> con SplitCam',
        "h1short": "Trasmettere su MV Live",
        "card": "Setup dell'encoder esterno per il Creator Studio MV Live di ManyVids.",
        "intro": "ManyVids è una piattaforma di economia del creator — vendita di clip, video personalizzati, abbonamenti fan club e il prodotto live <strong>MV Live</strong>. Il broadcaster di default del Creator Studio funziona da browser, ma viene esposta anche una via standard <strong>External Encoder</strong> a cui si collega <strong style='color:var(--text)'>SplitCam</strong> gratuito — così trasmetti con scene multicamera, overlay e filtri sulla stessa piattaforma creator-friendly.",
        "quick": "Per trasmettere su MV Live con SplitCam: installare SplitCam, comporre la scena, nel Creator Studio aprire <em>MV Live → Broadcast Settings → External Encoder</em>, copiare URL del server e stream key, incollare in SplitCam, premere Go Live."
                 "<ol><li>Installare SplitCam.</li><li>Aggiungere camera + scena.</li>"
                 "<li>Prendere URL e stream key dal Creator Studio.</li>"
                 "<li>Incollare in SplitCam.</li>"
                 "<li>Premere Go Live.</li></ol>",
        "key_how": "Accedi al tuo account creator di ManyVids, apri il <strong>Creator Studio</strong> e vai in <strong>MV Live → Broadcast Settings → External Encoder</strong>. La pagina mostra una <strong>URL del server</strong> e una <strong>stream key</strong> legate al tuo account — copia entrambe nei campi RTMP personalizzato di SplitCam. Gli account creator devono essere completamente verificati (ID + fiscale) prima che MV Live sia disponibile.",
        "tips": [
            ("Economia del creator, non solo live", "ManyVids non è una piattaforma cam pura — MV Live è una via di reddito affiancata a vendita di clip, video personalizzati e abbonamenti fan club. Usa il live per spingere il pubblico verso le altre monetizzazioni."),
            ("Tipping con token dentro MV Live", "MV Live ha il suo sistema di tipping con token dentro la stanza. Pianifica menu di obiettivi e trigger di reward stile Chaturbate / Stripchat — convertono bene sul pubblico esistente di ManyVids."),
            ("Browser vs encoder esterno", "Il broadcaster integrato browser del Creator Studio è a singola camera. SplitCam via External Encoder sblocca multicamera, overlay e filtri."),
            _T_ETH,
        ],
        "faq": [
            ("MV Live (ManyVids) supporta encoder esterni come SplitCam?", "Sì — la sezione MV Live del Creator Studio include l'opzione External Encoder in Broadcast Settings. URL del server RTMP standard e stream key; OBS, SplitCam, vMix si collegano."),
            ("Dove prendo la mia stream key di MV Live?", "Creator Studio → MV Live → Broadcast Settings → External Encoder. URL del server e stream key compaiono lì — copia entrambe nei campi RTMP personalizzato di SplitCam."),
            ("Che bitrate uso per MV Live?", "Spingi 1920×1080 a 30 fps, 3.500–6.000 Kbps con keyframe ogni 2 secondi. Lancia prima lo speed test integrato di SplitCam."),
            ("SplitCam è gratis con MV Live?", "Sì — SplitCam è gratis, senza filigrana e senza limite di tempo. L'opzione encoder esterno di ManyVids è gratis nel Creator Studio."),
        ],
        "steps": [
            ("Scarica e installa SplitCam",
             "SplitCam è un software di live streaming gratuito per Windows e macOS — senza registrazione, senza carta, senza filigrana."),
            ("Componi la scena",
             "Apri SplitCam e aggiungi la webcam. Sovrapponi overlay, testo, una seconda camera o il telefono, filtri beauty o sfondo IA — perfetto per i menu di obiettivi e i trigger di reward di MV Live."),
            ("Prendi URL e stream key di MV Live",
             "Accedi al tuo account creator di ManyVids, apri il <strong>Creator Studio</strong> e vai in <strong>MV Live → Broadcast Settings → External Encoder</strong>. La pagina mostra una <strong>URL del server</strong> e una <strong>stream key</strong> unica. Copia entrambe."),
            ("Collega SplitCam a MV Live",
             "In SplitCam apri <strong>Stream Settings</strong>, incolla URL del server di MV Live e stream key nei campi RTMP personalizzato. Imposta il bitrate a 3.500–6.000 Kbps a 1920×1080, 30 fps, con keyframe ogni 2 secondi."),
            ("Clicca Go Live",
             "Premi <strong>Go Live</strong> in SplitCam, poi avvia la trasmissione MV Live dal Creator Studio. In ~10 secondi il tuo flusso raggiunge il pubblico di MV Live."),
        ],
    },
    {
        "slug": "fansly", "name": "Fansly",
        "title": "Andare in diretta su Fansly Live con SplitCam",
        "desc": "Andare in diretta su Fansly Live con SplitCam gratis — encoder esterno del Creator Dashboard, scene multicamera e filtri beauty. Senza filigrana.",
        "kw": "andare in diretta su fansly, fansly, fansly live, fansly broadcast, fansly obs, fansly external encoder, fansly rtmp, fansly stream key",
        "h1html": 'Come trasmettere su <span class="accent">Fansly Live</span> con SplitCam',
        "h1short": "Trasmettere su Fansly",
        "card": "Setup dell'encoder esterno per il Creator Dashboard di Fansly.",
        "intro": "Fansly è un concorrente diretto di OnlyFans con regole sui contenuti più permissive e una base di creator in crescita — abbonamenti, pay-per-view e il prodotto live <strong>Fansly Live</strong>. Il broadcaster di default funziona da browser, ma il <strong>Creator Dashboard</strong> espone anche una via standard <strong>External Encoder</strong> a cui si collega <strong style='color:var(--text)'>SplitCam</strong> gratuito — per trasmettere con scene multicamera, overlay e filtri verso la tua base di abbonati.",
        "quick": "Per trasmettere su Fansly Live con SplitCam: installare SplitCam, comporre la scena, nel Creator Dashboard aprire <em>Live → Broadcast Settings → External Encoder</em>, copiare URL del server e stream key, incollare in SplitCam, premere Go Live."
                 "<ol><li>Installare SplitCam.</li><li>Aggiungere camera + scena.</li>"
                 "<li>Prendere URL e stream key dal Creator Dashboard.</li>"
                 "<li>Incollare in SplitCam.</li>"
                 "<li>Premere Go Live.</li></ol>",
        "key_how": "Accedi al tuo account creator di Fansly, apri il <strong>Creator Dashboard</strong> e vai in <strong>Live → Broadcast Settings → External Encoder</strong>. La pagina mostra una <strong>URL del server</strong> e una <strong>stream key</strong> legate al tuo account — copia entrambe nei campi RTMP personalizzato di SplitCam. Gli account creator devono passare una verifica ID prima che Fansly Live venga abilitato.",
        "tips": [
            ("Pubblico in abbonamento, prima di tutto", "Il pubblico di Fansly è in abbonamento — il tuo live raggiunge gente che già ti paga ogni mese. Pianifica contenuti che premino la fedeltà (Q&amp;A esclusivi, dietro le quinte, obiettivi di mancia personalizzati) invece di rincorrere metriche da stanza pubblica."),
            ("Mance oltre agli abbonamenti", "Fansly Live supporta le mance in diretta oltre all'abbonamento base. Per creator già avviati i ricavi combinati possono superare il tipping puro delle piattaforme cam."),
            ("Broadcaster browser vs esterno", "Il broadcaster browser di default è a sorgente singola. SplitCam via External Encoder sblocca multicamera, overlay, filtri beauty e sfondo IA che eguagliano la cura dei contenuti a pagamento per gli abbonati."),
            _T_ETH,
        ],
        "faq": [
            ("Fansly Live supporta encoder esterni come SplitCam?", "Sì — la sezione Live del Creator Dashboard include l'opzione External Encoder in Broadcast Settings. URL del server RTMP standard e stream key; OBS, SplitCam, vMix si collegano."),
            ("Dove prendo la mia stream key di Fansly?", "Creator Dashboard → Live → Broadcast Settings → External Encoder. URL del server e stream key compaiono lì. Copia entrambe nei campi RTMP personalizzato di SplitCam."),
            ("Che bitrate uso per Fansly Live?", "Spingi 1920×1080 a 30 fps, 3.500–6.000 Kbps con keyframe ogni 2 secondi. Lancia prima lo speed test integrato di SplitCam."),
            ("SplitCam è gratis con Fansly?", "Sì — SplitCam è gratis, senza filigrana e senza limite di tempo. L'opzione encoder esterno di Fansly è gratis nel Creator Dashboard."),
        ],
        "steps": [
            ("Scarica e installa SplitCam",
             "SplitCam è un software di live streaming gratuito per Windows e macOS — senza registrazione, senza carta, senza filigrana."),
            ("Componi la scena",
             "Apri SplitCam e aggiungi la webcam. Sovrapponi overlay, testo, una seconda camera o il telefono, filtri beauty o sfondo IA — una scena curata è all'altezza delle aspettative premium dei tuoi abbonati a pagamento."),
            ("Prendi URL e stream key di Fansly",
             "Accedi al tuo account creator di Fansly, apri il <strong>Creator Dashboard</strong> e vai in <strong>Live → Broadcast Settings → External Encoder</strong>. La pagina mostra una <strong>URL del server</strong> e una <strong>stream key</strong> unica. Copia entrambe."),
            ("Collega SplitCam a Fansly",
             "In SplitCam apri <strong>Stream Settings</strong>, incolla URL del server di Fansly e stream key nei campi RTMP personalizzato. Imposta il bitrate a 3.500–6.000 Kbps a 1920×1080, 30 fps, con keyframe ogni 2 secondi."),
            ("Clicca Go Live",
             "Premi <strong>Go Live</strong> in SplitCam, poi avvia la trasmissione Fansly Live dal Creator Dashboard. In ~10 secondi il tuo flusso raggiunge i tuoi abbonati Fansly."),
        ],
    },
    {
        "slug": "ifriends", "name": "iFriends",
        "title": "Trasmettere su iFriends con SplitCam — Encoder esterno",
        "desc": "Trasmettere su iFriends con SplitCam gratis — external encoder del Model Center, network cam indipendente storico, scene multicamera. Senza filigrana.",
        "kw": "trasmettere su ifriends, ifriends, ifriends.net, ifriends broadcast, ifriends obs, ifriends external encoder, ifriends rtmp, ifriends stream key",
        "h1html": 'Come trasmettere su <span class="accent">iFriends</span> con SplitCam',
        "h1short": "Trasmettere su iFriends",
        "card": "Setup dell'encoder esterno per il maturo Model Center di iFriends.",
        "intro": "iFriends (WebPower) è uno dei network cam indipendenti più longevi — redditizio senza clamore, con un pubblico fedele e un Model Center maturo, nato prima che i broadcaster da browser fossero la norma. La piattaforma offre una via standard <strong>External Encoder</strong> dal Model Center a cui si collega <strong style='color:var(--text)'>SplitCam</strong> gratuito — per trasmettere con scene multicamera, overlay e filtri moderni su questo network ormai affermato.",
        "quick": "Per trasmettere su iFriends con SplitCam: installare SplitCam, comporre la scena, nel Model Center aprire <em>Broadcast Settings → External Encoder</em>, copiare URL del server e stream key, incollare in SplitCam, premere Go Live."
                 "<ol><li>Installare SplitCam.</li><li>Aggiungere camera + scena.</li>"
                 "<li>Prendere URL e stream key dal Model Center.</li>"
                 "<li>Incollare in SplitCam.</li>"
                 "<li>Premere Go Live.</li></ol>",
        "key_how": "Accedi al tuo account modella iFriends, apri il <strong>Model Center</strong> e vai in <strong>Broadcast Settings → External Encoder</strong>. La pagina mostra una <strong>URL del server</strong> e una <strong>stream key</strong> legate al tuo account — copia entrambe nei campi RTMP personalizzato di SplitCam. L'approvazione iFriends per i nuovi account modella è rigorosa ma seria; una volta verificato, l'opzione encoder esterno resta disponibile a tempo indeterminato.",
        "tips": [
            ("Pubblico di nicchia, network maturo", "iFriends è attivo dalla fine degli anni '90 e ha un pubblico fedele — molti utenti sono abbonati di lungo corso, non visitatori occasionali. Reddito stabile per le modelle già avviate, crescita più lenta per chi inizia."),
            ("Broadcaster da browser vs esterno", "Il broadcaster storico di iFriends è nato prima della UX multicamera moderna. Passare a SplitCam via External Encoder è un salto di qualità netto — scene multicamera, overlay e filtri beauty che lo strumento più datato non può offrire."),
            ("Pagamenti puntuali, poche sorprese", "La casa madre di iFriends (WebPower) paga le modelle con regolarità da decenni — tempi di accredito più lenti rispetto alle piattaforme cripto-friendly più recenti, ma pochissime brutte storie."),
            _T_ETH,
        ],
        "faq": [
            ("iFriends supporta ufficialmente encoder esterni come SplitCam?", "Sì — il Model Center include l'opzione External Encoder in Broadcast Settings. URL del server RTMP standard e stream key; OBS, SplitCam, vMix si collegano una volta approvato il tuo account."),
            ("Dove prendo la mia stream key di iFriends?", "Model Center → Broadcast Settings → External Encoder. URL del server e stream key compaiono lì — copia entrambe nei campi RTMP personalizzato di SplitCam."),
            ("Che bitrate uso per iFriends?", "Spingi 1920×1080 a 30 fps, 3.500–6.000 Kbps con keyframe ogni 2 secondi. Lancia prima lo speed test integrato di SplitCam."),
            ("SplitCam è gratis con iFriends?", "Sì — SplitCam è gratis, senza filigrana e senza limite di tempo. L'opzione encoder esterno di iFriends è gratis nel Model Center."),
        ],
        "steps": [
            ("Scarica e installa SplitCam",
             "SplitCam è un software di live streaming gratuito per Windows e macOS — senza registrazione, senza carta, senza filigrana."),
            ("Componi la scena",
             "Apri SplitCam e aggiungi la webcam. Sovrapponi overlay, testo, una seconda camera o il telefono, filtri beauty o sfondo IA — scene moderne e curate spiccano su questo network maturo."),
            ("Prendi URL e stream key di iFriends",
             "Accedi al tuo account modella iFriends, apri il <strong>Model Center</strong> e vai in <strong>Broadcast Settings → External Encoder</strong>. La pagina mostra una <strong>URL del server</strong> e una <strong>stream key</strong> unica. Copia entrambe."),
            ("Collega SplitCam a iFriends",
             "In SplitCam apri <strong>Stream Settings</strong>, incolla URL del server di iFriends e stream key nei campi RTMP personalizzato. Imposta il bitrate a 3.500–6.000 Kbps a 1920×1080, 30 fps, con keyframe ogni 2 secondi."),
            ("Clicca Go Live",
             "Premi <strong>Go Live</strong> in SplitCam, poi vai online dal Model Center di iFriends. In ~10 secondi il tuo flusso raggiunge il network."),
        ],
    },
    {
        "slug": "babestation", "name": "Babestation",
        "title": "Trasmettere su Babestation con SplitCam — Encoder esterno",
        "desc": "Trasmettere su Babestation con SplitCam gratis — external encoder del Performer Hub, network TV / cam per adulti UK, scene multicamera. Senza filigrana.",
        "kw": "trasmettere su babestation, babestation, babestation cam, babestation broadcast, babestation obs, babestation external encoder, babestation rtmp, babestation stream key",
        "h1html": 'Come trasmettere su <span class="accent">Babestation</span> con SplitCam',
        "h1short": "Trasmettere su Babestation",
        "card": "Setup dell'encoder esterno per il Performer Hub UK di Babestation.",
        "intro": "Babestation è il principale network TV / cam per adulti del Regno Unito — un ibrido tra canali della TV via etere e un prodotto cam dal vivo alimentato dalle performer collegate al Performer Hub. La piattaforma offre una via standard <strong>External Encoder</strong> dal Performer Hub a cui si collega <strong style='color:var(--text)'>SplitCam</strong> gratuito — per dare alle performer indipendenti britanniche scene multicamera, overlay e filtri beauty che vanno oltre il broadcaster di default in stile studio televisivo di Babestation.",
        "quick": "Per trasmettere su Babestation con SplitCam: installare SplitCam, comporre la scena, nel Performer Hub aprire <em>Broadcast Settings → External Encoder</em>, copiare URL del server e stream key, incollare in SplitCam, premere Go Live."
                 "<ol><li>Installare SplitCam.</li><li>Aggiungere camera + scena.</li>"
                 "<li>Prendere URL e stream key dal Performer Hub.</li>"
                 "<li>Incollare in SplitCam.</li>"
                 "<li>Premere Go Live.</li></ol>",
        "key_how": "Accedi al tuo account performer Babestation, apri il <strong>Performer Hub</strong> e vai in <strong>Broadcast Settings → External Encoder</strong>. La pagina mostra una <strong>URL del server</strong> e una <strong>stream key</strong> legate al tuo account — copia entrambe nei campi RTMP personalizzato di SplitCam. L'onboarding delle performer britanniche di Babestation include la verifica dell'identità prevista dalla normativa UK sulla verifica dell'età.",
        "tips": [
            ("Pubblico britannico, occhio agli orari", "Il traffico migliore di Babestation è quello della sera / nottata britannica (GMT/BST). Se sei in un altro fuso, trasmettere nelle ore tarde del Regno Unito rende molto più che puntare sull'orario di punta locale, su questo network."),
            ("Si pretende un tocco da studio TV", "Il marchio Babestation è legato ai suoi canali televisivi — gli spettatori si aspettano set e luci più curati rispetto a una webcam qualsiasi. Le scene SplitCam (overlay, testo brandizzato, sfondo IA) aiutano a centrare l'estetica raffinata della piattaforma."),
            ("Performer indipendenti vs di studio", "Babestation lavora sia con studi britannici sia con performer indipendenti. Chi trasmette in autonomia via External Encoder riceve lo stesso modello di pagamento delle camere gestite dagli studi."),
            _T_ETH,
        ],
        "faq": [
            ("Babestation supporta encoder esterni come SplitCam?", "Sì — il Performer Hub include l'opzione External Encoder in Broadcast Settings. URL del server RTMP standard e stream key; OBS, SplitCam, vMix si collegano una volta completata la verifica della performer."),
            ("Dove prendo la mia stream key di Babestation?", "Performer Hub → Broadcast Settings → External Encoder. URL del server e stream key compaiono lì — copia entrambe nei campi RTMP personalizzato di SplitCam."),
            ("Che bitrate uso per Babestation?", "Spingi 1920×1080 a 30 fps, 3.500–6.000 Kbps con keyframe ogni 2 secondi. La banda in upload nel Regno Unito è in genere buona, ma lancia comunque prima lo speed test di SplitCam."),
            ("SplitCam è gratis con Babestation?", "Sì — SplitCam è gratis, senza filigrana e senza limite di tempo. L'opzione encoder esterno di Babestation è gratis nel Performer Hub."),
        ],
        "steps": [
            ("Scarica e installa SplitCam",
             "SplitCam è un software di live streaming gratuito per Windows e macOS — senza registrazione, senza carta, senza filigrana."),
            ("Componi la scena",
             "Apri SplitCam e aggiungi la webcam. Sovrapponi overlay, testo, una seconda camera o il telefono, filtri beauty o sfondo IA — eguaglia la cura da studio televisivo di Babestation per farti notare."),
            ("Prendi URL e stream key di Babestation",
             "Accedi al tuo account performer Babestation, apri il <strong>Performer Hub</strong> e vai in <strong>Broadcast Settings → External Encoder</strong>. La pagina mostra una <strong>URL del server</strong> e una <strong>stream key</strong> unica. Copia entrambe."),
            ("Collega SplitCam a Babestation",
             "In SplitCam apri <strong>Stream Settings</strong>, incolla URL del server di Babestation e stream key nei campi RTMP personalizzato. Imposta il bitrate a 3.500–6.000 Kbps a 1920×1080, 30 fps, con keyframe ogni 2 secondi."),
            ("Clicca Go Live",
             "Premi <strong>Go Live</strong> in SplitCam, poi vai online dal Performer Hub. In ~10 secondi il tuo flusso raggiunge il pubblico britannico di Babestation."),
        ],
    },
    {
        "slug": "adultwork", "name": "AdultWork",
        "title": "Trasmettere su AdultWork con SplitCam — Encoder esterno",
        "desc": "Trasmettere su AdultWork con SplitCam gratis — external encoder della Members Area, marketplace cam britannico, scene multicamera. Senza filigrana.",
        "kw": "trasmettere su adultwork, adultwork, adultwork cam, adultwork broadcast, adultwork obs, adultwork external encoder, adultwork rtmp, adultwork stream key",
        "h1html": 'Come trasmettere su <span class="accent">AdultWork</span> con SplitCam',
        "h1short": "Trasmettere su AdultWork",
        "card": "Setup dell'encoder esterno per la funzione cam della Members Area UK di AdultWork.",
        "intro": "AdultWork è il marketplace britannico di servizi per adulti ormai affermato — noto soprattutto per la prenotazione di escort, la vendita di foto / video e i servizi telefonici, con accanto una <strong>funzione webcam</strong> dal vivo. La piattaforma offre una via standard <strong>External Encoder</strong> dalla Members Area a cui si collega <strong style='color:var(--text)'>SplitCam</strong> gratuito — per dare alle performer indipendenti britanniche un nuovo flusso di guadagno dal vivo con scene multicamera, overlay e filtri.",
        "quick": "Per trasmettere su AdultWork con SplitCam: installare SplitCam, comporre la scena, nella Members Area aprire <em>Members → Broadcasting → External Encoder</em>, copiare URL del server e stream key, incollare in SplitCam, premere Go Live."
                 "<ol><li>Installare SplitCam.</li><li>Aggiungere camera + scena.</li>"
                 "<li>Prendere URL e stream key dalla Members Area.</li>"
                 "<li>Incollare in SplitCam.</li>"
                 "<li>Premere Go Live.</li></ol>",
        "key_how": "Accedi al tuo account performer AdultWork, apri la <strong>Members Area</strong> e vai in <strong>Members → Broadcasting → External Encoder</strong>. La pagina mostra una <strong>URL del server</strong> e una <strong>stream key</strong> legate al tuo account — copia entrambe nei campi RTMP personalizzato di SplitCam. La verifica AdultWork è obbligatoria per la funzione cam dal vivo e copre la conformità alla normativa UK sulla verifica dell'età.",
        "tips": [
            ("Cross-sell dagli altri servizi AdultWork", "Il punto di forza di AdultWork è la sua base clienti già esistente — gli spettatori potrebbero già prenotare i tuoi servizi di foto / video / telefono. Usa le dirette cam per fare cross-sell ai clienti che non hanno ancora provato la tua cam, non per rincorrere sconosciuti."),
            ("La Members Area è il punto di partenza", "Non cercare il broadcaster nella parte pubblica del sito — tutto ciò che riguarda le performer sta dentro la Members Area. Impostazioni di trasmissione, pagamenti e gestione dei contenuti sono lì."),
            ("Baricentro britannico, pagamenti internazionali", "La gran parte del traffico è UK/EU. I pagamenti funzionano a livello internazionale tramite bonifico bancario / e-wallet, con cadenza settimanale comune sulla piattaforma."),
            _T_ETH,
        ],
        "faq": [
            ("AdultWork supporta encoder esterni come SplitCam?", "Sì — la Members Area include l'opzione External Encoder nella sezione Broadcasting. URL del server RTMP standard e stream key; OBS, SplitCam, vMix si collegano dopo la verifica della performer."),
            ("Dove prendo la mia stream key di AdultWork?", "Members Area → Members → Broadcasting → External Encoder. URL del server e stream key compaiono lì — copia entrambe nei campi RTMP personalizzato di SplitCam."),
            ("Che bitrate uso per AdultWork?", "Spingi 1920×1080 a 30 fps, 3.500–6.000 Kbps con keyframe ogni 2 secondi. Lancia prima lo speed test integrato di SplitCam."),
            ("SplitCam è gratis con AdultWork?", "Sì — SplitCam è gratis, senza filigrana e senza limite di tempo. L'opzione encoder esterno di AdultWork è gratis nella Members Area."),
        ],
        "steps": [
            ("Scarica e installa SplitCam",
             "SplitCam è un software di live streaming gratuito per Windows e macOS — senza registrazione, senza carta, senza filigrana."),
            ("Componi la scena",
             "Apri SplitCam e aggiungi la webcam. Sovrapponi overlay, testo, una seconda camera o il telefono, filtri beauty o sfondo IA — usa gli overlay per pubblicizzare i tuoi contenuti AdultWork / i servizi telefonici e fare cross-sell durante la diretta."),
            ("Prendi URL e stream key di AdultWork",
             "Accedi al tuo account performer AdultWork, apri la <strong>Members Area</strong> e vai in <strong>Members → Broadcasting → External Encoder</strong>. La pagina mostra una <strong>URL del server</strong> e una <strong>stream key</strong> unica. Copia entrambe."),
            ("Collega SplitCam ad AdultWork",
             "In SplitCam apri <strong>Stream Settings</strong>, incolla URL del server di AdultWork e stream key nei campi RTMP personalizzato. Imposta il bitrate a 3.500–6.000 Kbps a 1920×1080, 30 fps, con keyframe ogni 2 secondi."),
            ("Clicca Go Live",
             "Premi <strong>Go Live</strong> in SplitCam, poi vai online dalla Members Area. In ~10 secondi il tuo flusso raggiunge il pubblico di AdultWork."),
        ],
    },
    {
        "slug": "jerkmate", "name": "Jerkmate",
        "title": "Trasmettere su Jerkmate con SplitCam — Rete Streamate",
        "desc": "Trasmettere su Jerkmate con SplitCam gratis — le modelle arrivano dalla rete Streamate: vai in onda via SM Connect e il canale integrato. Senza filigrana.",
        "kw": "trasmettere su jerkmate, jerkmate, jerkmate streamate, jerkmate sm connect, jerkmate broadcast, jerkmate obs, jerkmate cam, diventare modella jerkmate",
        "h1html": 'Come trasmettere su <span class="accent">Jerkmate</span> con SplitCam',
        "h1short": "Trasmettere su Jerkmate",
        "card": "Jerkmate prende le modelle dalla rete Streamate — vai in onda via SM Connect + SplitCam.",
        "intro": "Jerkmate è uno dei brand cam più cercati, noto per il suo matchmaker IA che abbina gli spettatori alle performer in diretta. Non ha un broadcaster proprio — Jerkmate <strong>prende le sue modelle live dalla rete Streamate</strong>. Trasmetti come modella della rete Streamate e il tuo show viene distribuito a Jerkmate e ai siti partner. Dato che Streamate è <strong style='color:var(--text)'>preconfigurato in SplitCam</strong>, nell'elenco dei canali, SplitCam gratuito ti permette di aggiungere scene multi-camera, overlay e filtri senza inserire alcun RTMP a mano.",
        "quick": "Trasmettere su Jerkmate con SplitCam: installare SplitCam, comporre la scena, registrarsi come modella sulla rete Streamate che alimenta Jerkmate, aprire <em>SM Connect → Start Show</em> e copiare la chiave, poi in SplitCam aprire <em>Stream Settings → Add Channel → Streamate</em>, incollarla e Go Live."
                 "<ol><li>Installare SplitCam.</li><li>Aggiungere camera + scena.</li>"
                 "<li>Registrarsi come modella della rete Streamate.</li>"
                 "<li>Ottenere la chiave via SM Connect.</li>"
                 "<li>Add Channel → Streamate, Go Live.</li></ol>",
        "key_how": "Le cam live di Jerkmate arrivano dalla <strong>rete di trasmissione Streamate</strong> — non esiste un \"Jerkmate encoder\" separato. Registrati tramite il programma modelle di Jerkmate o direttamente sulla rete Streamate, apri <strong>SM Connect</strong>, accetta i termini, clicca <strong>Start Show</strong> e copia la tua streaming key. In SplitCam apri <strong>Stream Settings → Add Channel</strong>, scegli <strong>Streamate</strong> dalla lista integrata e incolla la chiave. Il tuo flusso raggiunge così Jerkmate e i siti partner della rete in un colpo solo.",
        "tips": [
            ("Sotto c'è la rete Streamate", "Non cercare un broadcaster specifico di Jerkmate — trasmetti su Streamate e Jerkmate lo ridistribuisce. Tutto ciò che funziona per Streamate (SM Connect, il canale integrato in SplitCam) funziona anche per Jerkmate."),
            ("Converti il traffico abbinato dall'IA", "Il matchmaker di Jerkmate convoglia gli spettatori verso le modelle che corrispondono alle loro scelte — una scena SplitCam curata, con overlay e una buona inquadratura, converte quegli spettatori abbinati molto meglio di una webcam piatta."),
            ("Un flusso, tanti siti", "Trasmettere sulla rete Streamate ti mette su Jerkmate e sui suoi siti partner contemporaneamente — più visibilità da un unico stream SplitCam, senza setup aggiuntivo."),
            _T_ETH,
        ],
        "faq": [
            ("Jerkmate ha un broadcaster o una stream key propri?", "No — Jerkmate prende le modelle live dalla rete Streamate. Trasmetti come modella della rete Streamate tramite SM Connect e il tuo show compare su Jerkmate in automatico."),
            ("Come ottengo la mia stream key di Jerkmate?", "Tramite SM Connect lato modella della rete Streamate: accetta i termini → Start Show → copia la chiave. Incollala nel canale Streamate integrato in SplitCam — niente URL RTMP a mano."),
            ("Quale bitrate per Jerkmate?", "Blocca 1080p a 30 fps. Il flusso della rete è adattivo, quindi un bitrate più basso su un'immagine ferma è normale. Lancia lo speed test di SplitCam e usa una connessione via cavo."),
            ("SplitCam è gratuito per Jerkmate?", "Sì — SplitCam è gratis, senza filigrana e senza limite di tempo. Streamate (che alimenta Jerkmate) è un canale integrato in SplitCam, quindi non c'è un costo separato di encoder."),
        ],
        "steps": [
            ("Scarica e installa SplitCam",
             "SplitCam è un software di live streaming gratuito per Windows e macOS — niente registrazione, niente carta, niente filigrana."),
            ("Componi la scena",
             "Apri SplitCam e aggiungi la webcam. Sovrapponi overlay, testo, una seconda camera o il telefono, filtri beauty o sfondo IA — una scena curata converte gli spettatori abbinati di Jerkmate."),
            ("Registrati come modella e prendi la chiave",
             "Iscriviti tramite il programma modelle di Jerkmate o direttamente sulla <strong>rete Streamate</strong> che lo alimenta. Apri <strong>SM Connect</strong>, accetta i termini, clicca <strong>Start Show</strong> e copia la tua streaming key."),
            ("Aggiungi Streamate come canale in SplitCam",
             "Apri <strong>Stream Settings → Add Channel</strong>, scegli <strong>Streamate</strong> dalla lista integrata e incolla la chiave — niente URL RTMP a mano. Blocca la risoluzione su 1080p."),
            ("Clicca Go Live",
             "Premi <strong>Go Live</strong> in SplitCam — uno slider verde conferma la connessione. Il tuo show va in onda su tutta la rete Streamate e compare su Jerkmate."),
        ],
    },
    {
        "slug": "justforfans", "name": "JustForFans",
        "title": "Andare in diretta su JustForFans con SplitCam",
        "desc": "Andare in diretta su JustForFans (JFF) con SplitCam gratis — camera virtuale nel live di JFF per scene multicamera, overlay e filtri. Senza filigrana.",
        "kw": "andare in diretta su justforfans, justforfans, jff live, justforfans live, justforfans virtual camera, justforfans camera virtuale, justforfans obs, justforfans broadcast",
        "h1html": 'Come andare in diretta su <span class="accent">JustForFans</span> con SplitCam',
        "h1short": "Diretta su JustForFans",
        "card": "Usa SplitCam come camera virtuale nel broadcaster live di JustForFans.",
        "intro": "JustForFans (JFF) è una piattaforma in abbonamento di proprietà dei creator — un'alternativa a OnlyFans nata da una performer e attiva da anni, con abbonamenti, pay-per-view e una funzione live basata su browser. Il suo broadcaster live mostra una singola webcam piatta; puntarlo su <strong style='color:var(--text)'>SplitCam</strong> gratuito come <strong>camera virtuale</strong> sblocca scene multi-camera, overlay e filtri. Se la tua dashboard creator espone anche un'opzione encoder esterno / stream key, SplitCam si collega invece via RTMP.",
        "quick": "Andare in diretta su JustForFans con SplitCam: installare SplitCam, comporre la scena, avviare una diretta su JFF e, nel selettore camera del broadcaster, scegliere <em>SplitCam</em> come webcam — poi andare live."
                 "<ol><li>Installare SplitCam.</li><li>Aggiungere camera + scena.</li>"
                 "<li>Avviare una diretta su JFF.</li>"
                 "<li>Selezionare SplitCam nel menu camera.</li><li>Premere Go Live.</li></ol>",
        "key_how": "Il live di JustForFans gira nel browser. Componi la scena in SplitCam — viene registrata come webcam di sistema chiamata <strong>\"SplitCam Video Driver\"</strong> — poi apri il broadcaster live di JFF e, nel menu camera, scegli <strong>SplitCam</strong> al posto della webcam grezza. La tua scena composta sostituisce la camera piatta. Se la dashboard creator di JFF offre un'opzione <strong>encoder esterno / stream key</strong>, incolla invece quella chiave nei campi RTMP personalizzato di SplitCam.",
        "tips": [
            ("La camera virtuale funziona ovunque", "Anche quando il live di una piattaforma è solo da browser, SplitCam compare come webcam selezionabile — così scene multi-camera, overlay e filtri funzionano su JFF senza alcuna stream key."),
            ("Di proprietà dei creator, fatta per le performer", "JFF è gestita da performer e mantiene una base di iscritti fedele. Gli overlay che fanno cross-sell del tuo PPV o abbonamento convertono bene su un pubblico che già paga."),
            ("Concedi il permesso camera al browser", "Se SplitCam non compare nell'elenco camere di JFF, assicurati che SplitCam sia già avviato e che il browser abbia il permesso camera — poi ricarica il broadcaster."),
            _T_TEST,
        ],
        "faq": [
            ("Come si collega SplitCam a JustForFans?", "Il live di JFF è basato su browser, quindi SplitCam si collega come camera virtuale: scegli SplitCam nel selettore camera del broadcaster JFF. Nessuna stream key necessaria."),
            ("Posso usare overlay e più camere su JFF?", "Sì — componi la scena in SplitCam (seconda camera, overlay, filtri beauty o sfondo IA) e JFF vede la scena finita come un'unica webcam."),
            ("JustForFans supporta OBS o gli encoder esterni?", "Il live di JFF è prevalentemente da browser/webcam. Se la tua dashboard creator mostra un'opzione encoder esterno o stream key, incollala nei campi RTMP personalizzato di SplitCam; altrimenti usa il metodo della camera virtuale."),
            ("SplitCam è gratuito per JustForFans?", "Sì — SplitCam è gratis, senza filigrana e senza limite di tempo."),
        ],
        "steps": [
            ("Scarica e installa SplitCam",
             "SplitCam è un software di live streaming gratuito per Windows e macOS — niente registrazione, niente carta, niente filigrana. Installa una camera virtuale che il browser può selezionare."),
            ("Componi la scena",
             "Apri SplitCam e aggiungi la webcam. Sovrapponi overlay, testo, una seconda camera o il telefono, filtri beauty o sfondo IA — applicati in diretta."),
            ("Avvia una diretta su JFF",
             "Accedi al tuo account creator JustForFans e apri il broadcaster live per avviare una diretta per i tuoi iscritti."),
            ("Seleziona SplitCam come camera",
             "Nel menu camera del broadcaster JFF scegli <strong>SplitCam</strong> al posto della webcam grezza — la tua scena composta sostituisce la camera piatta. (Oppure, se disponibile, incolla la chiave encoder esterno di JFF nei campi RTMP personalizzato di SplitCam.)"),
            ("Go Live",
             "Avvia la trasmissione — la tua scena SplitCam, gli overlay e i filtri raggiungono i tuoi iscritti JustForFans."),
        ],
    },
    {
        "slug": "fanvue", "name": "Fanvue",
        "title": "Andare in diretta su Fanvue con SplitCam",
        "desc": "Andare in diretta su Fanvue con SplitCam gratis — camera virtuale per scene multicamera, overlay e filtri per i tuoi iscritti. Senza filigrana.",
        "kw": "andare in diretta su fanvue, fanvue, fanvue live, fanvue stream, fanvue camera virtuale, fanvue virtual camera, fanvue obs, fanvue creator",
        "h1html": 'Come andare in diretta su <span class="accent">Fanvue</span> con SplitCam',
        "h1short": "Diretta su Fanvue",
        "card": "Usa SplitCam come camera virtuale per le dirette di Fanvue.",
        "intro": "Fanvue è una piattaforma in abbonamento britannica in forte crescita — un'alternativa a OnlyFans nota per essere aperta ai creator e all'IA, con abbonamenti, pay-per-view e dirette. Il suo broadcaster live gira nel browser, quindi puntarlo su <strong style='color:var(--text)'>SplitCam</strong> gratuito come <strong>camera virtuale</strong> sblocca scene multi-camera, overlay e filtri. Se la tua dashboard creator espone un'opzione encoder esterno / stream key, SplitCam si collega invece via RTMP.",
        "quick": "Andare in diretta su Fanvue con SplitCam: installare SplitCam, comporre la scena, avviare una diretta su Fanvue e, nel selettore camera del broadcaster, scegliere <em>SplitCam</em> — poi andare live."
                 "<ol><li>Installare SplitCam.</li><li>Aggiungere camera + scena.</li>"
                 "<li>Avviare una diretta su Fanvue.</li>"
                 "<li>Selezionare SplitCam nel menu camera.</li><li>Premere Go Live.</li></ol>",
        "key_how": "Il live di Fanvue gira nel browser. Componi la scena in SplitCam — viene registrata come webcam di sistema chiamata <strong>\"SplitCam Video Driver\"</strong> — poi apri il broadcaster live di Fanvue e, nel menu camera, scegli <strong>SplitCam</strong> al posto della webcam grezza. Se la tua dashboard creator offre un'opzione <strong>encoder esterno / stream key</strong>, incolla invece quella chiave nei campi RTMP personalizzato di SplitCam.",
        "tips": [
            ("La camera virtuale funziona ovunque", "Anche quando il live di una piattaforma è solo da browser, SplitCam compare come webcam selezionabile — così scene multi-camera, overlay e filtri funzionano su Fanvue senza alcuna stream key."),
            ("Aperta ai creator e all'IA", "Fanvue accoglie i creator IA e paga in modo lineare. Gli overlay che fanno cross-sell del tuo abbonamento o del PPV convertono bene su un pubblico che già paga."),
            ("Concedi il permesso camera al browser", "Se SplitCam non compare nell'elenco camere di Fanvue, assicurati che SplitCam sia già avviato e che il browser abbia il permesso camera — poi ricarica."),
            _T_TEST,
        ],
        "faq": [
            ("Come si collega SplitCam a Fanvue?", "Il live di Fanvue è basato su browser, quindi SplitCam si collega come camera virtuale: scegli SplitCam nel selettore camera. Nessuna stream key necessaria."),
            ("Posso usare overlay e più camere su Fanvue?", "Sì — componi la scena in SplitCam (seconda camera, overlay, filtri beauty o sfondo IA) e Fanvue vede la scena finita come un'unica webcam."),
            ("Fanvue supporta OBS o gli encoder esterni?", "Il live di Fanvue è prevalentemente da browser/webcam. Se la tua dashboard mostra un'opzione encoder esterno o stream key, incollala nei campi RTMP personalizzato di SplitCam; altrimenti usa il metodo della camera virtuale."),
            ("SplitCam è gratuito per Fanvue?", "Sì — SplitCam è gratis, senza filigrana e senza limite di tempo."),
        ],
        "steps": [
            ("Scarica e installa SplitCam",
             "SplitCam è un software di live streaming gratuito per Windows e macOS — niente registrazione, niente carta, niente filigrana. Installa una camera virtuale che il browser può selezionare."),
            ("Componi la scena",
             "Apri SplitCam e aggiungi la webcam. Sovrapponi overlay, testo, una seconda camera o il telefono, filtri beauty o sfondo IA — applicati in diretta."),
            ("Avvia una diretta su Fanvue",
             "Accedi al tuo account creator Fanvue e apri il broadcaster live per avviare una diretta per i tuoi iscritti."),
            ("Seleziona SplitCam come camera",
             "Nel menu camera di Fanvue scegli <strong>SplitCam</strong> al posto della webcam grezza — la tua scena composta sostituisce la camera piatta. (Oppure, se disponibile, incolla una stream key nei campi RTMP personalizzato di SplitCam.)"),
            ("Go Live",
             "Avvia la trasmissione — la tua scena SplitCam, gli overlay e i filtri raggiungono i tuoi iscritti Fanvue."),
        ],
    },
    {
        "slug": "loyalfans", "name": "LoyalFans",
        "title": "Andare in diretta su LoyalFans con SplitCam",
        "desc": "Andare in diretta su LoyalFans con SplitCam gratis — camera virtuale per scene multicamera, overlay e filtri per iscritti e tipper. Senza filigrana.",
        "kw": "andare in diretta su loyalfans, loyalfans, loyalfans live, loyalfans stream, loyalfans camera virtuale, loyalfans virtual camera, loyalfans obs, loyal fans",
        "h1html": 'Come andare in diretta su <span class="accent">LoyalFans</span> con SplitCam',
        "h1short": "Diretta su LoyalFans",
        "card": "Usa SplitCam come camera virtuale per le dirette di LoyalFans.",
        "intro": "LoyalFans è una piattaforma in abbonamento con abbonamenti, pay-per-view, mance e una funzione <strong>live cam</strong> integrata. Il broadcaster live gira nel browser, quindi collegare <strong style='color:var(--text)'>SplitCam</strong> gratuito come <strong>camera virtuale</strong> aggiunge scene multi-camera, overlay e filtri sopra la webcam standard. Se la tua dashboard espone un'opzione encoder esterno / stream key, SplitCam si collega invece via RTMP.",
        "quick": "Andare in diretta su LoyalFans con SplitCam: installare SplitCam, comporre la scena, avviare una diretta su LoyalFans e scegliere <em>SplitCam</em> nel selettore camera del broadcaster — poi andare live."
                 "<ol><li>Installare SplitCam.</li><li>Aggiungere camera + scena.</li>"
                 "<li>Avviare una diretta su LoyalFans.</li>"
                 "<li>Selezionare SplitCam nel menu camera.</li><li>Premere Go Live.</li></ol>",
        "key_how": "Il live di LoyalFans gira nel browser. Componi la scena in SplitCam — viene registrata come webcam di sistema chiamata <strong>\"SplitCam Video Driver\"</strong> — poi apri il broadcaster live di LoyalFans e, nel menu camera, seleziona <strong>SplitCam</strong>. Se nella tua dashboard creator compare un'opzione <strong>stream key / encoder esterno</strong>, incollala invece nei campi RTMP personalizzato di SplitCam.",
        "tips": [
            ("Camera virtuale, nessuna chiave necessaria", "Il live da browser riceve comunque la tua scena SplitCam completa — overlay, seconda camera e filtri — basta selezionare SplitCam come webcam."),
            ("Le mance premiano la qualità", "LoyalFans punta molto sulle mance; overlay con obiettivi di mancia a schermo e una scena curata spingono i tipper più di una webcam piatta."),
            ("Concedi il permesso camera al browser", "Se SplitCam non è nell'elenco camere di LoyalFans, avvia prima SplitCam, concedi l'accesso alla camera nel browser e poi ricarica il broadcaster."),
            _T_TEST,
        ],
        "faq": [
            ("Come si collega SplitCam a LoyalFans?", "Il live di LoyalFans è basato su browser, quindi SplitCam si collega come camera virtuale — scegli SplitCam nel selettore camera. Nessuna stream key necessaria."),
            ("Posso usare overlay e più camere su LoyalFans?", "Sì — componi la scena in SplitCam (seconda camera, overlay, filtri beauty o sfondo IA); LoyalFans la vede come un'unica webcam."),
            ("LoyalFans supporta OBS o gli encoder esterni?", "Il suo live è prevalentemente da browser/webcam. Se la tua dashboard mostra un'opzione stream key, incollala nei campi RTMP personalizzato di SplitCam; altrimenti usa il metodo della camera virtuale."),
            ("SplitCam è gratuito per LoyalFans?", "Sì — gratis, senza filigrana e senza limite di tempo."),
        ],
        "steps": [
            ("Scarica e installa SplitCam",
             "SplitCam è un software di live streaming gratuito per Windows e macOS — niente registrazione, niente carta, niente filigrana. Installa una camera virtuale che il browser può selezionare."),
            ("Componi la scena",
             "Apri SplitCam e aggiungi la webcam. Sovrapponi overlay, testo con obiettivi di mancia, una seconda camera o il telefono, filtri beauty o sfondo IA."),
            ("Avvia una diretta su LoyalFans",
             "Accedi al tuo account LoyalFans e apri il broadcaster live per andare in diretta per i tuoi iscritti."),
            ("Seleziona SplitCam come camera",
             "Nel menu camera di LoyalFans scegli <strong>SplitCam</strong> al posto della webcam grezza — la tua scena sostituisce la camera piatta. (Oppure, se disponibile, incolla una stream key nei campi RTMP personalizzato di SplitCam.)"),
            ("Go Live",
             "Avvia la trasmissione — la tua scena SplitCam raggiunge il pubblico di LoyalFans."),
        ],
    },
    {
        "slug": "fancentro", "name": "FanCentro",
        "title": "Andare in diretta su FanCentro con SplitCam",
        "desc": "Andare in diretta su FanCentro con SplitCam gratis — camera virtuale per scene multicamera, overlay e filtri per i tuoi iscritti. Senza filigrana.",
        "kw": "andare in diretta su fancentro, fancentro, fancentro live, fancentro stream, fancentro camera virtuale, fancentro virtual camera, fancentro obs, fan centro",
        "h1html": 'Come andare in diretta su <span class="accent">FanCentro</span> con SplitCam',
        "h1short": "Diretta su FanCentro",
        "card": "Usa SplitCam come camera virtuale per le dirette di FanCentro.",
        "intro": "FanCentro è una piattaforma di monetizzazione per creator attiva da anni — abbonamenti, messaggi pay-per-view, contenuti e dirette. Il suo live gira nel browser, quindi collegare <strong style='color:var(--text)'>SplitCam</strong> gratuito come <strong>camera virtuale</strong> aggiunge scene multi-camera, overlay e filtri oltre la semplice webcam. Se la tua dashboard espone un'opzione encoder esterno / stream key, SplitCam si collega invece via RTMP.",
        "quick": "Andare in diretta su FanCentro con SplitCam: installare SplitCam, comporre la scena, avviare una diretta su FanCentro e scegliere <em>SplitCam</em> nel selettore camera del broadcaster — poi andare live."
                 "<ol><li>Installare SplitCam.</li><li>Aggiungere camera + scena.</li>"
                 "<li>Avviare una diretta su FanCentro.</li>"
                 "<li>Selezionare SplitCam nel menu camera.</li><li>Premere Go Live.</li></ol>",
        "key_how": "Il live di FanCentro gira nel browser. Componi la scena in SplitCam — viene registrata come webcam di sistema chiamata <strong>\"SplitCam Video Driver\"</strong> — poi apri il broadcaster live di FanCentro e, nel menu camera, scegli <strong>SplitCam</strong>. Se è offerta un'opzione <strong>stream key / encoder esterno</strong>, incollala invece nei campi RTMP personalizzato di SplitCam.",
        "tips": [
            ("La camera virtuale funziona ovunque", "Il live solo da browser riceve comunque la tua scena SplitCam completa — overlay, seconda camera e filtri — selezionando SplitCam come webcam."),
            ("Fai cross-sell nel tuo funnel", "FanCentro è costruita attorno ai funnel dei creator e al PPV. Gli overlay che promuovono il tuo abbonamento o i messaggi a pagamento trasformano gli spettatori della diretta in acquirenti."),
            ("Concedi il permesso camera al browser", "Se SplitCam non è in elenco, avvia prima SplitCam, concedi l'accesso alla camera nel browser e poi ricarica il broadcaster."),
            _T_TEST,
        ],
        "faq": [
            ("Come si collega SplitCam a FanCentro?", "Il live di FanCentro è basato su browser, quindi SplitCam si collega come camera virtuale — scegli SplitCam nel selettore camera. Nessuna stream key necessaria."),
            ("Posso usare overlay e più camere su FanCentro?", "Sì — componi la scena in SplitCam; FanCentro vede la scena finita come un'unica webcam."),
            ("FanCentro supporta OBS o gli encoder esterni?", "Il suo live è prevalentemente da browser/webcam. Se nella tua dashboard compare un'opzione stream key, incollala nei campi RTMP personalizzato di SplitCam; altrimenti usa il metodo della camera virtuale."),
            ("SplitCam è gratuito per FanCentro?", "Sì — gratis, senza filigrana e senza limite di tempo."),
        ],
        "steps": [
            ("Scarica e installa SplitCam",
             "SplitCam è un software di live streaming gratuito per Windows e macOS — niente registrazione, niente carta, niente filigrana. Installa una camera virtuale che il browser può selezionare."),
            ("Componi la scena",
             "Apri SplitCam e aggiungi la webcam. Sovrapponi overlay, testo, una seconda camera o il telefono, filtri beauty o sfondo IA."),
            ("Avvia una diretta su FanCentro",
             "Accedi al tuo account FanCentro e apri il broadcaster live per andare in diretta per i tuoi iscritti."),
            ("Seleziona SplitCam come camera",
             "Nel menu camera di FanCentro scegli <strong>SplitCam</strong> al posto della webcam grezza. (Oppure, se disponibile, incolla una stream key nei campi RTMP personalizzato di SplitCam.)"),
            ("Go Live",
             "Avvia la trasmissione — la tua scena SplitCam raggiunge i tuoi iscritti FanCentro."),
        ],
    },
    {
        "slug": "ismygirl", "name": "IsMyGirl",
        "title": "Andare in diretta su IsMyGirl con SplitCam",
        "desc": "Andare in diretta su IsMyGirl con SplitCam gratis — camera virtuale per scene multicamera, overlay e filtri per i tuoi iscritti. Senza filigrana.",
        "kw": "andare in diretta su ismygirl, ismygirl, ismygirl live, ismygirl stream, ismygirl camera virtuale, ismygirl virtual camera, ismygirl obs, is my girl",
        "h1html": 'Come andare in diretta su <span class="accent">IsMyGirl</span> con SplitCam',
        "h1short": "Diretta su IsMyGirl",
        "card": "Usa SplitCam come camera virtuale per le dirette di IsMyGirl.",
        "intro": "IsMyGirl è una piattaforma in abbonamento — un'alternativa a OnlyFans con abbonamenti, contenuti a pagamento e dirette, nota per il supporto diretto ai creator. Il broadcaster live gira nel browser, quindi collegare <strong style='color:var(--text)'>SplitCam</strong> gratuito come <strong>camera virtuale</strong> porta scene multi-camera, overlay e filtri. Se la tua dashboard espone un'opzione encoder esterno / stream key, SplitCam si collega invece via RTMP.",
        "quick": "Andare in diretta su IsMyGirl con SplitCam: installare SplitCam, comporre la scena, avviare una diretta su IsMyGirl e selezionare <em>SplitCam</em> nel selettore camera del broadcaster — poi andare live."
                 "<ol><li>Installare SplitCam.</li><li>Aggiungere camera + scena.</li>"
                 "<li>Avviare una diretta su IsMyGirl.</li>"
                 "<li>Selezionare SplitCam nel menu camera.</li><li>Premere Go Live.</li></ol>",
        "key_how": "Il live di IsMyGirl gira nel browser. Componi la scena in SplitCam — viene registrata come webcam di sistema chiamata <strong>\"SplitCam Video Driver\"</strong> — poi apri il broadcaster live di IsMyGirl e, nel menu camera, scegli <strong>SplitCam</strong>. Se compare un'opzione <strong>stream key / encoder esterno</strong>, incollala invece nei campi RTMP personalizzato di SplitCam.",
        "tips": [
            ("Camera virtuale, nessuna chiave necessaria", "Il live solo da browser riceve comunque la tua scena SplitCam completa — overlay, seconda camera e filtri — selezionando SplitCam come webcam."),
            ("Sfrutta il supporto ai creator", "IsMyGirl punta su un forte supporto e promozione dei creator. Una scena SplitCam curata più overlay di cross-sell valorizza al massimo il traffico che ti inviano."),
            ("Concedi il permesso camera al browser", "Se SplitCam non è in elenco, avvia prima SplitCam, concedi l'accesso alla camera e poi ricarica il broadcaster."),
            _T_TEST,
        ],
        "faq": [
            ("Come si collega SplitCam a IsMyGirl?", "Il live di IsMyGirl è basato su browser, quindi SplitCam si collega come camera virtuale — scegli SplitCam nel selettore camera. Nessuna stream key necessaria."),
            ("Posso usare overlay e più camere su IsMyGirl?", "Sì — componi la scena in SplitCam; IsMyGirl la vede come un'unica webcam."),
            ("IsMyGirl supporta OBS o gli encoder esterni?", "Il suo live è prevalentemente da browser/webcam. Se compare un'opzione stream key, incollala nei campi RTMP personalizzato di SplitCam; altrimenti usa il metodo della camera virtuale."),
            ("SplitCam è gratuito per IsMyGirl?", "Sì — gratis, senza filigrana e senza limite di tempo."),
        ],
        "steps": [
            ("Scarica e installa SplitCam",
             "SplitCam è un software di live streaming gratuito per Windows e macOS — niente registrazione, niente carta, niente filigrana. Installa una camera virtuale che il browser può selezionare."),
            ("Componi la scena",
             "Apri SplitCam e aggiungi la webcam. Sovrapponi overlay, testo, una seconda camera o il telefono, filtri beauty o sfondo IA."),
            ("Avvia una diretta su IsMyGirl",
             "Accedi al tuo account IsMyGirl e apri il broadcaster live per andare in diretta per i tuoi iscritti."),
            ("Seleziona SplitCam come camera",
             "Nel menu camera di IsMyGirl scegli <strong>SplitCam</strong> al posto della webcam grezza. (Oppure, se disponibile, incolla una stream key nei campi RTMP personalizzato di SplitCam.)"),
            ("Go Live",
             "Avvia la trasmissione — la tua scena SplitCam raggiunge i tuoi iscritti IsMyGirl."),
        ],
    },
    {
        "slug": "dxlive", "name": "DXLive",
        "title": "Trasmettere su DXLive con SplitCam — Encoder esterno",
        "desc": "Trasmettere su DXLive con SplitCam gratis — encoder esterno per il network cam premium giapponese, scene multicamera e overlay. Senza filigrana.",
        "kw": "trasmettere su dxlive, dxlive, dxlive cam, dxlive broadcast, dxlive obs, dxlive external encoder, dxlive rtmp, dxlive performer",
        "h1html": 'Come trasmettere su <span class="accent">DXLive</span> con SplitCam',
        "h1short": "Trasmettere su DXLive",
        "card": "Setup dell'encoder esterno per il network cam premium di DXLive.",
        "intro": "DXLive è un network webcam premium affermato, popolare in Giappone e in tutta l'Asia, costruito su un modello pay-per-minute con un pubblico fedele. L'area performer supporta una via standard <strong>External Encoder</strong> a cui si collega <strong style='color:var(--text)'>SplitCam</strong> gratuito — per trasmettere con scene multi-camera, overlay e filtri beauty al posto di una singola webcam piatta.",
        "quick": "Per trasmettere su DXLive con SplitCam: installare SplitCam, comporre la scena, nell'area performer aprire le impostazioni <em>external encoder / broadcast</em>, copiare URL del server e stream key, incollare in SplitCam, premere Go Live."
                 "<ol><li>Installare SplitCam.</li><li>Aggiungere camera + scena.</li>"
                 "<li>Prendere URL e stream key dall'area performer.</li>"
                 "<li>Incollare in SplitCam.</li>"
                 "<li>Premere Go Live.</li></ol>",
        "key_how": "Accedi al tuo account performer DXLive e apri le impostazioni <strong>broadcast / external encoder</strong> nell'area performer. La pagina mostra una <strong>URL del server</strong> e una <strong>stream key</strong> legate al tuo account — copia entrambe nei campi RTMP personalizzato di SplitCam. La verifica DXLive è obbligatoria prima che la funzione live cam venga attivata.",
        "tips": [
            ("Pensato per il mercato asiatico", "Il pubblico di DXLive è orientato a Giappone/Asia e paga al minuto. Programma gli spettacoli nelle serate JST e la base fedele e pagante converte bene."),
            ("La cura batte la webcam grezza", "Una scena SplitCam pulita con overlay e filtri beauty spicca su un network premium pay-per-minute, dove gli spettatori si aspettano qualità."),
            ("Usa l'encoder esterno, non solo la webcam", "Passare per l'RTMP di SplitCam invece della camera base del browser è ciò che sblocca scene multi-camera e filtri."),
            _T_ETH,
        ],
        "faq": [
            ("DXLive supporta encoder esterni come SplitCam?", "Sì — l'area performer espone una via standard external encoder / RTMP. Copia URL del server e stream key in SplitCam dopo la verifica."),
            ("Dove prendo la mia stream key di DXLive?", "Nelle impostazioni broadcast / external encoder dell'area performer — URL del server e stream key compaiono lì. Incolla entrambe nei campi RTMP personalizzato di SplitCam."),
            ("Che bitrate uso per DXLive?", "Spingi 1920×1080 a 30 fps, 3.500–6.000 Kbps con keyframe ogni 2 secondi. Lancia prima lo speed test integrato di SplitCam."),
            ("SplitCam è gratis con DXLive?", "Sì — SplitCam è gratis, senza filigrana e senza limite di tempo. L'opzione encoder esterno di DXLive è gratis nell'area performer."),
        ],
        "steps": [
            ("Scarica e installa SplitCam",
             "SplitCam è un software di live streaming gratuito per Windows e macOS — senza registrazione, senza carta, senza filigrana."),
            ("Componi la scena",
             "Apri SplitCam e aggiungi la webcam. Sovrapponi overlay, testo, una seconda camera o il telefono, filtri beauty o sfondo IA."),
            ("Prendi URL e stream key di DXLive",
             "Accedi al tuo account performer DXLive e apri le impostazioni <strong>broadcast / external encoder</strong>. Copia la <strong>URL del server</strong> e la <strong>stream key</strong>."),
            ("Collega SplitCam a DXLive",
             "In SplitCam apri <strong>Stream Settings</strong>, incolla URL del server di DXLive e stream key nei campi RTMP personalizzato. Imposta 3.500–6.000 Kbps a 1920×1080, 30 fps, con keyframe ogni 2 secondi."),
            ("Clicca Go Live",
             "Premi <strong>Go Live</strong> in SplitCam, poi vai online dall'area performer. In ~10 secondi il tuo flusso raggiunge il pubblico di DXLive."),
        ],
    },
    {
        "slug": "streamen", "name": "Streamen",
        "title": "Trasmettere su Streamen con SplitCam — Encoder esterno",
        "desc": "Trasmettere su Streamen con SplitCam gratis — encoder esterno, scene multicamera, overlay e filtri beauty. Senza filigrana, senza registrazione.",
        "kw": "trasmettere su streamen, streamen, streamen cam, streamen broadcast, streamen obs, streamen external encoder, streamen rtmp, streamen.tv",
        "h1html": 'Come trasmettere su <span class="accent">Streamen</span> con SplitCam',
        "h1short": "Trasmettere su Streamen",
        "card": "Setup dell'encoder esterno per la piattaforma cam Streamen.",
        "intro": "Streamen è una piattaforma di live cam dove le modelle trasmettono a un pubblico basato sulle mance. Le sue impostazioni di trasmissione espongono una via standard <strong>External Encoder</strong> a cui si collega <strong style='color:var(--text)'>SplitCam</strong> gratuito — così puoi trasmettere con scene multi-camera, overlay e filtri invece di una singola webcam piatta.",
        "quick": "Per trasmettere su Streamen con SplitCam: installare SplitCam, comporre la scena, nella dashboard modella aprire <em>broadcast settings → external encoder</em>, copiare URL del server e stream key, incollare in SplitCam, premere Go Live."
                 "<ol><li>Installare SplitCam.</li><li>Aggiungere camera + scena.</li>"
                 "<li>Prendere URL e stream key dalla dashboard.</li>"
                 "<li>Incollare in SplitCam.</li>"
                 "<li>Premere Go Live.</li></ol>",
        "key_how": "Accedi al tuo account modella Streamen e apri la sezione <strong>broadcast settings / external encoder</strong>. Mostra una <strong>URL del server</strong> e una <strong>stream key</strong> legate al tuo account — copia entrambe nei campi RTMP personalizzato di SplitCam. La verifica della modella è obbligatoria prima che la trasmissione venga attivata.",
        "tips": [
            ("Pubblico orientato alle mance", "Gli spettatori di Streamen danno mance — obiettivi di mancia a schermo e una scena curata spingono più mance di una webcam piatta."),
            ("L'encoder esterno sblocca le scene", "Passare per l'RTMP di SplitCam invece della camera base del browser è ciò che abilita layout multi-camera, overlay e filtri."),
            ("Blocca la risoluzione", "Imposta il 1080p a mano così il flusso non cala di qualità in silenzio; un bitrate che scende su un'inquadratura ferma è normale sui flussi adattivi."),
            _T_ETH,
        ],
        "faq": [
            ("Streamen supporta encoder esterni come SplitCam?", "Sì — le impostazioni di trasmissione espongono una via standard external encoder / RTMP. Copia URL del server e stream key in SplitCam dopo la verifica."),
            ("Dove prendo la mia stream key di Streamen?", "Nelle impostazioni broadcast / external encoder della tua dashboard modella — URL del server e stream key compaiono lì. Incolla entrambe nei campi RTMP personalizzato di SplitCam."),
            ("Che bitrate uso per Streamen?", "Spingi 1920×1080 a 30 fps, 3.500–6.000 Kbps con keyframe ogni 2 secondi. Lancia prima lo speed test di SplitCam."),
            ("SplitCam è gratis con Streamen?", "Sì — SplitCam è gratis, senza filigrana e senza limite di tempo. L'opzione encoder esterno di Streamen è gratis nella dashboard."),
        ],
        "steps": [
            ("Scarica e installa SplitCam",
             "SplitCam è un software di live streaming gratuito per Windows e macOS — senza registrazione, senza carta, senza filigrana."),
            ("Componi la scena",
             "Apri SplitCam e aggiungi la webcam. Sovrapponi overlay, testo con obiettivi di mancia, una seconda camera o il telefono, filtri beauty o sfondo IA."),
            ("Prendi URL e stream key di Streamen",
             "Accedi al tuo account modella Streamen, apri <strong>broadcast settings → external encoder</strong> e copia la <strong>URL del server</strong> e la <strong>stream key</strong>."),
            ("Collega SplitCam a Streamen",
             "In SplitCam apri <strong>Stream Settings</strong>, incolla URL del server di Streamen e stream key nei campi RTMP personalizzato. Imposta 3.500–6.000 Kbps a 1920×1080, 30 fps, con keyframe ogni 2 secondi."),
            ("Clicca Go Live",
             "Premi <strong>Go Live</strong> in SplitCam, poi vai online dalla tua dashboard. In ~10 secondi il tuo flusso raggiunge il pubblico di Streamen."),
        ],
    },
    {
        "slug": "xcams", "name": "XCams",
        "title": "Trasmettere su XCams con SplitCam — Encoder esterno",
        "desc": "Trasmettere su XCams con SplitCam gratis — encoder esterno per la community cam europea, scene multicamera, overlay e filtri. Senza filigrana.",
        "kw": "trasmettere su xcams, xcams, xcams cam, xcams broadcast, xcams obs, xcams external encoder, xcams rtmp, x cams",
        "h1html": 'Come trasmettere su <span class="accent">XCams</span> con SplitCam',
        "h1short": "Trasmettere su XCams",
        "card": "Setup dell'encoder esterno per la community europea di XCams.",
        "intro": "XCams è una community europea di live cam — forte in Italia, Francia e Spagna — costruita attorno agli spettacoli dal vivo e a un'economia di mance e spettacoli privati. L'area modella supporta una via standard <strong>External Encoder</strong> a cui si collega <strong style='color:var(--text)'>SplitCam</strong> gratuito, così puoi trasmettere con scene multi-camera, overlay e filtri beauty.",
        "quick": "Per trasmettere su XCams con SplitCam: installare SplitCam, comporre la scena, nell'area modella aprire <em>broadcast / external encoder</em>, copiare URL del server e stream key, incollare in SplitCam, premere Go Live."
                 "<ol><li>Installare SplitCam.</li><li>Aggiungere camera + scena.</li>"
                 "<li>Prendere URL e stream key dall'area modella.</li>"
                 "<li>Incollare in SplitCam.</li>"
                 "<li>Premere Go Live.</li></ol>",
        "key_how": "Accedi al tuo account modella XCams e apri le impostazioni <strong>broadcast / external encoder</strong> nell'area modella. La pagina mostra una <strong>URL del server</strong> e una <strong>stream key</strong> legate al tuo account — copia entrambe nei campi RTMP personalizzato di SplitCam. La verifica XCams è obbligatoria prima di trasmettere.",
        "tips": [
            ("Prime time europeo", "Il traffico di XCams ha il picco nelle serate europee (CET). Trasmettere in quelle ore rende molto più che fuori dalle ore di punta su questa community."),
            ("Gli spettacoli privati premiano la qualità", "XCams vive di spettacoli privati/spy — una scena SplitCam curata con overlay trasforma i curiosi in privati a pagamento."),
            ("L'encoder esterno sblocca le scene", "Passare per l'RTMP di SplitCam invece della camera del browser abilita layout multi-camera, overlay e filtri."),
            _T_ETH,
        ],
        "faq": [
            ("XCams supporta encoder esterni come SplitCam?", "Sì — l'area modella espone una via standard external encoder / RTMP. Copia URL del server e stream key in SplitCam dopo la verifica."),
            ("Dove prendo la mia stream key di XCams?", "Nelle impostazioni broadcast / external encoder dell'area modella — URL del server e stream key compaiono lì. Incolla entrambe nei campi RTMP personalizzato di SplitCam."),
            ("Che bitrate uso per XCams?", "Spingi 1920×1080 a 30 fps, 3.500–6.000 Kbps con keyframe ogni 2 secondi. Lancia prima lo speed test di SplitCam."),
            ("SplitCam è gratis con XCams?", "Sì — SplitCam è gratis, senza filigrana e senza limite di tempo. L'opzione encoder esterno di XCams è gratis nell'area modella."),
        ],
        "steps": [
            ("Scarica e installa SplitCam",
             "SplitCam è un software di live streaming gratuito per Windows e macOS — senza registrazione, senza carta, senza filigrana."),
            ("Componi la scena",
             "Apri SplitCam e aggiungi la webcam. Sovrapponi overlay, testo, una seconda camera o il telefono, filtri beauty o sfondo IA."),
            ("Prendi URL e stream key di XCams",
             "Accedi al tuo account modella XCams, apri <strong>broadcast / external encoder</strong> e copia la <strong>URL del server</strong> e la <strong>stream key</strong>."),
            ("Collega SplitCam a XCams",
             "In SplitCam apri <strong>Stream Settings</strong>, incolla URL del server di XCams e stream key nei campi RTMP personalizzato. Imposta 3.500–6.000 Kbps a 1920×1080, 30 fps, con keyframe ogni 2 secondi."),
            ("Clicca Go Live",
             "Premi <strong>Go Live</strong> in SplitCam, poi vai online dall'area modella. In ~10 secondi il tuo flusso raggiunge il pubblico di XCams."),
        ],
    },
    {
        "slug": "camcontacts", "name": "CamContacts",
        "title": "Trasmettere su CamContacts con SplitCam — Encoder",
        "desc": "Trasmettere su CamContacts con SplitCam gratis — encoder esterno per il sito cam pay-per-minute storico, scene multicamera e overlay. Senza filigrana.",
        "kw": "trasmettere su camcontacts, camcontacts, camcontacts cam, camcontacts broadcast, camcontacts obs, camcontacts external encoder, camcontacts rtmp, cam contacts",
        "h1html": 'Come trasmettere su <span class="accent">CamContacts</span> con SplitCam',
        "h1short": "Trasmettere su CamContacts",
        "card": "Setup dell'encoder esterno per la cam pay-per-minute di CamContacts.",
        "intro": "CamContacts è uno dei siti cam indipendenti più longevi — un modello pay-per-minute con un pubblico maturo e fedele e una reputazione di pagamenti regolari. L'area performer supporta una via standard <strong>External Encoder</strong> a cui si collega <strong style='color:var(--text)'>SplitCam</strong> gratuito, così puoi trasmettere con scene multi-camera, overlay e filtri beauty.",
        "quick": "Per trasmettere su CamContacts con SplitCam: installare SplitCam, comporre la scena, nell'area performer aprire le impostazioni <em>external encoder / broadcast</em>, copiare URL del server e stream key, incollare in SplitCam, premere Go Live."
                 "<ol><li>Installare SplitCam.</li><li>Aggiungere camera + scena.</li>"
                 "<li>Prendere URL e stream key dall'area performer.</li>"
                 "<li>Incollare in SplitCam.</li>"
                 "<li>Premere Go Live.</li></ol>",
        "key_how": "Accedi al tuo account performer CamContacts e apri le impostazioni <strong>broadcast / external encoder</strong> nell'area performer. La pagina mostra una <strong>URL del server</strong> e una <strong>stream key</strong> legate al tuo account — copia entrambe nei campi RTMP personalizzato di SplitCam. La verifica CamContacts è obbligatoria per la funzione live cam.",
        "tips": [
            ("Pubblico maturo e fedele", "CamContacts è attivo da decenni con membri di lungo corso — abituali più stabili e più paganti rispetto a un sito free ad alto ricambio, ma crescita più lenta per chi inizia."),
            ("Il pay-per-minute premia la fidelizzazione", "Tieni gli spettatori in tempo a pagamento con una scena curata e overlay; la qualità di produzione allunga le sessioni su un modello al minuto."),
            ("L'encoder esterno sblocca le scene", "Passare per l'RTMP di SplitCam invece della camera base abilita layout multi-camera, overlay e filtri."),
            _T_ETH,
        ],
        "faq": [
            ("CamContacts supporta encoder esterni come SplitCam?", "Sì — l'area performer espone una via standard external encoder / RTMP. Copia URL del server e stream key in SplitCam dopo la verifica."),
            ("Dove prendo la mia stream key di CamContacts?", "Nelle impostazioni broadcast / external encoder dell'area performer — URL del server e stream key compaiono lì. Incolla entrambe nei campi RTMP personalizzato di SplitCam."),
            ("Che bitrate uso per CamContacts?", "Spingi 1920×1080 a 30 fps, 3.500–6.000 Kbps con keyframe ogni 2 secondi. Lancia prima lo speed test di SplitCam."),
            ("SplitCam è gratis con CamContacts?", "Sì — SplitCam è gratis, senza filigrana e senza limite di tempo. L'opzione encoder esterno di CamContacts è gratis nell'area performer."),
        ],
        "steps": [
            ("Scarica e installa SplitCam",
             "SplitCam è un software di live streaming gratuito per Windows e macOS — senza registrazione, senza carta, senza filigrana."),
            ("Componi la scena",
             "Apri SplitCam e aggiungi la webcam. Sovrapponi overlay, testo, una seconda camera o il telefono, filtri beauty o sfondo IA."),
            ("Prendi URL e stream key di CamContacts",
             "Accedi al tuo account performer CamContacts, apri le impostazioni <strong>broadcast / external encoder</strong> e copia la <strong>URL del server</strong> e la <strong>stream key</strong>."),
            ("Collega SplitCam a CamContacts",
             "In SplitCam apri <strong>Stream Settings</strong>, incolla URL del server di CamContacts e stream key nei campi RTMP personalizzato. Imposta 3.500–6.000 Kbps a 1920×1080, 30 fps, con keyframe ogni 2 secondi."),
            ("Clicca Go Live",
             "Premi <strong>Go Live</strong> in SplitCam, poi vai online dall'area performer. In ~10 secondi il tuo flusso raggiunge il pubblico di CamContacts."),
        ],
    },
    {
        "slug": "royalcams", "name": "RoyalCams",
        "title": "Trasmettere su RoyalCams con SplitCam — Encoder",
        "desc": "Trasmettere su RoyalCams con SplitCam gratis — encoder esterno per il sito cam free a token, scene multicamera, overlay e filtri. Senza filigrana.",
        "kw": "trasmettere su royalcams, royalcams, royalcams cam, royalcams broadcast, royalcams obs, royalcams external encoder, royalcams rtmp, royal cams",
        "h1html": 'Come trasmettere su <span class="accent">RoyalCams</span> con SplitCam',
        "h1short": "Trasmettere su RoyalCams",
        "card": "Setup dell'encoder esterno per il sito cam a token RoyalCams.",
        "intro": "RoyalCams è un sito cam gratuito basato su token — stanze pubbliche aperte finanziate dalle mance, con spettacoli privati in aggiunta. Le impostazioni di trasmissione supportano una via standard <strong>External Encoder</strong> a cui si collega <strong style='color:var(--text)'>SplitCam</strong> gratuito, così puoi trasmettere con scene multi-camera, overlay e filtri beauty al posto di una singola webcam piatta.",
        "quick": "Per trasmettere su RoyalCams con SplitCam: installare SplitCam, comporre la scena, nella dashboard modella aprire <em>broadcast settings → external encoder</em>, copiare URL del server e stream key, incollare in SplitCam, premere Go Live."
                 "<ol><li>Installare SplitCam.</li><li>Aggiungere camera + scena.</li>"
                 "<li>Prendere URL e stream key dalla dashboard.</li>"
                 "<li>Incollare in SplitCam.</li>"
                 "<li>Premere Go Live.</li></ol>",
        "key_how": "Accedi al tuo account modella RoyalCams e apri la sezione <strong>broadcast settings / external encoder</strong>. Mostra una <strong>URL del server</strong> e una <strong>stream key</strong> legate al tuo account — copia entrambe nei campi RTMP personalizzato di SplitCam. La verifica della modella è obbligatoria prima di trasmettere.",
        "tips": [
            ("Le stanze a token premiano la produzione", "Le stanze pubbliche di RoyalCams vivono di mance — overlay con obiettivi di mancia e una scena curata trasformano i passivi in tipper e spettacoli privati."),
            ("Converti in spettacoli privati", "Usa una scena pubblica efficace per fare upselling verso gli spettacoli privati, dove stanno i veri guadagni sui siti cam a token."),
            ("L'encoder esterno sblocca le scene", "Passare per l'RTMP di SplitCam invece della camera del browser abilita layout multi-camera, overlay e filtri."),
            _T_ETH,
        ],
        "faq": [
            ("RoyalCams supporta encoder esterni come SplitCam?", "Sì — le impostazioni di trasmissione espongono una via standard external encoder / RTMP. Copia URL del server e stream key in SplitCam dopo la verifica."),
            ("Dove prendo la mia stream key di RoyalCams?", "Nelle impostazioni broadcast / external encoder della tua dashboard modella — URL del server e stream key compaiono lì. Incolla entrambe nei campi RTMP personalizzato di SplitCam."),
            ("Che bitrate uso per RoyalCams?", "Spingi 1920×1080 a 30 fps, 3.500–6.000 Kbps con keyframe ogni 2 secondi. Lancia prima lo speed test di SplitCam."),
            ("SplitCam è gratis con RoyalCams?", "Sì — SplitCam è gratis, senza filigrana e senza limite di tempo. L'opzione encoder esterno di RoyalCams è gratis nella dashboard."),
        ],
        "steps": [
            ("Scarica e installa SplitCam",
             "SplitCam è un software di live streaming gratuito per Windows e macOS — senza registrazione, senza carta, senza filigrana."),
            ("Componi la scena",
             "Apri SplitCam e aggiungi la webcam. Sovrapponi overlay, testo con obiettivi di mancia, una seconda camera o il telefono, filtri beauty o sfondo IA."),
            ("Prendi URL e stream key di RoyalCams",
             "Accedi al tuo account modella RoyalCams, apri <strong>broadcast settings → external encoder</strong> e copia la <strong>URL del server</strong> e la <strong>stream key</strong>."),
            ("Collega SplitCam a RoyalCams",
             "In SplitCam apri <strong>Stream Settings</strong>, incolla URL del server di RoyalCams e stream key nei campi RTMP personalizzato. Imposta 3.500–6.000 Kbps a 1920×1080, 30 fps, con keyframe ogni 2 secondi."),
            ("Clicca Go Live",
             "Premi <strong>Go Live</strong> in SplitCam, poi vai online dalla tua dashboard. In ~10 secondi il tuo flusso raggiunge il pubblico di RoyalCams."),
        ],
    },
    {
        "slug": "modelhub", "name": "Modelhub",
        "title": "Trasmettere su Modelhub con SplitCam — Encoder",
        "desc": "Trasmettere su Modelhub Live con SplitCam gratis — encoder esterno per la piattaforma creator di Pornhub, scene multicamera e overlay. Senza filigrana.",
        "kw": "trasmettere su modelhub, modelhub, modelhub live, modelhub broadcast, modelhub obs, modelhub external encoder, modelhub rtmp, modelhub cam",
        "h1html": 'Come trasmettere su <span class="accent">Modelhub</span> con SplitCam',
        "h1short": "Trasmettere su Modelhub",
        "card": "Setup dell'encoder esterno per Modelhub Live (Pornhub).",
        "intro": "Modelhub è la piattaforma per creator di Pornhub — vendita di video, abbonamenti dei fan e un prodotto <strong>live cam</strong> con un enorme traffico in cima al funnel proveniente dal network Pornhub. La dashboard modella supporta una via standard <strong>External Encoder</strong> a cui si collega <strong style='color:var(--text)'>SplitCam</strong> gratuito, così puoi trasmettere con scene multi-camera, overlay e filtri beauty.",
        "quick": "Per trasmettere su Modelhub con SplitCam: installare SplitCam, comporre la scena, nella dashboard modella aprire <em>Live → broadcast / external encoder</em>, copiare URL del server e stream key, incollare in SplitCam, premere Go Live."
                 "<ol><li>Installare SplitCam.</li><li>Aggiungere camera + scena.</li>"
                 "<li>Prendere URL e stream key dalla dashboard.</li>"
                 "<li>Incollare in SplitCam.</li>"
                 "<li>Premere Go Live.</li></ol>",
        "key_how": "Accedi al tuo account modella Modelhub e apri le impostazioni <strong>Live / broadcast / external encoder</strong> nella dashboard. La pagina mostra una <strong>URL del server</strong> e una <strong>stream key</strong> legate al tuo account — copia entrambe nei campi RTMP personalizzato di SplitCam. La verifica della modella presso il network è obbligatoria prima di andare live.",
        "tips": [
            ("Enorme traffico in cima al funnel", "Modelhub attira spettatori dal network Pornhub — una scena SplitCam curata trasforma quel grande pubblico occasionale in spettatori live paganti e abbonati."),
            ("Fai cross-sell dei tuoi video", "Usa gli overlay per indirizzare gli spettatori live ai tuoi video Modelhub e all'abbonamento — la piattaforma è costruita per quel funnel."),
            ("L'encoder esterno sblocca le scene", "Passare per l'RTMP di SplitCam invece della camera base abilita layout multi-camera, overlay e filtri."),
            _T_ETH,
        ],
        "faq": [
            ("Modelhub supporta encoder esterni come SplitCam?", "Sì — la dashboard modella espone una via standard external encoder / RTMP per Modelhub Live. Copia URL del server e stream key in SplitCam dopo la verifica."),
            ("Dove prendo la mia stream key di Modelhub?", "Nelle impostazioni Live / broadcast / external encoder della dashboard — URL del server e stream key compaiono lì. Incolla entrambe nei campi RTMP personalizzato di SplitCam."),
            ("Che bitrate uso per Modelhub?", "Spingi 1920×1080 a 30 fps, 3.500–6.000 Kbps con keyframe ogni 2 secondi. Lancia prima lo speed test di SplitCam."),
            ("SplitCam è gratis con Modelhub?", "Sì — SplitCam è gratis, senza filigrana e senza limite di tempo. L'opzione encoder esterno di Modelhub è gratis nella dashboard."),
        ],
        "steps": [
            ("Scarica e installa SplitCam",
             "SplitCam è un software di live streaming gratuito per Windows e macOS — senza registrazione, senza carta, senza filigrana."),
            ("Componi la scena",
             "Apri SplitCam e aggiungi la webcam. Sovrapponi overlay, testo, una seconda camera o il telefono, filtri beauty o sfondo IA."),
            ("Prendi URL e stream key di Modelhub",
             "Accedi al tuo account modella Modelhub, apri <strong>Live → broadcast / external encoder</strong> e copia la <strong>URL del server</strong> e la <strong>stream key</strong>."),
            ("Collega SplitCam a Modelhub",
             "In SplitCam apri <strong>Stream Settings</strong>, incolla URL del server di Modelhub e stream key nei campi RTMP personalizzato. Imposta 3.500–6.000 Kbps a 1920×1080, 30 fps, con keyframe ogni 2 secondi."),
            ("Clicca Go Live",
             "Premi <strong>Go Live</strong> in SplitCam, poi vai online dalla dashboard. In ~10 secondi il tuo flusso raggiunge il pubblico di Modelhub."),
        ],
    },
    {
        "slug": "xhamsterlive", "name": "xHamsterLive",
        "title": "Trasmettere su xHamsterLive con SplitCam — RTMP/OBS",
        "desc": "Trasmettere su xHamsterLive con SplitCam gratis via RTMP — scene multi-camera, overlay e filtri. Traffico mainstream di xHamster, senza filigrana.",
        "kw": "trasmettere su xhamsterlive, xhamsterlive, xhamsterlive obs, xhamsterlive rtmp, xhamsterlive broadcast, xhamsterlive modella, xhamster live cam, xhamsterlive stream key",
        "h1html": 'Come trasmettere su <span class="accent">xHamsterLive</span> con SplitCam',
        "h1short": "Trasmettere su xHamsterLive",
        "card": "SplitCam gratis → stream RTMP/OBS verso xHamsterLive.",
        "intro": "xHamsterLive è il braccio live-cam di xHamster — stessa tecnologia broadcaster di Stripchat, ma alimentata dal traffico mainstream di xHamster, una delle basi di spettatori più grandi nell'adult. Le modelle trasmettono dallo <strong>Studio</strong> di xHamsterLive, che supporta sia il broadcaster integrato nel browser sia un <strong>encoder esterno via RTMP</strong>. Con <strong style='color:var(--text)'>SplitCam</strong> gratuito trasmetti come encoder esterno per scene multi-camera complete, overlay e filtri — oppure, se trasmetti dal browser, punta xHamsterLive su SplitCam come <strong>camera virtuale</strong> per lo stesso risultato.",
        "quick": "Trasmettere su xHamsterLive con SplitCam: installare SplitCam, comporre la scena, copiare URL server e stream key dallo Studio xHamsterLive, incollarli nelle impostazioni RTMP di SplitCam, premere Go Live."
                 "<ol><li>Installare SplitCam.</li><li>Aggiungere camera + scena.</li>"
                 "<li>Copiare URL + stream key dallo Studio xHamsterLive → External Encoder.</li>"
                 "<li>Incollare nell'RTMP personalizzato di SplitCam.</li>"
                 "<li>Premere Go Live.</li></ol>",
        "key_how": "Lo Studio di xHamsterLive mostra alle broadcaster una scheda <strong>external encoder</strong> con una URL del server e una stream key. Incolla entrambe in <strong>Stream Settings → Custom RTMP</strong> di SplitCam; scegli 4.000–6.000 Kbps a 1920×1080, 30 fps, keyframe ogni 2 secondi. Clicca <strong>Go Live</strong> in SplitCam, poi vai online dallo Studio. Se preferisci usare il broadcaster nel browser, aprilo e seleziona <strong>SplitCam</strong> dal menu camera — la tua scena composta sostituisce la webcam grezza.",
        "tips": [
            ("Traffico xHamster, motore Stripchat", "Stessi strumenti broadcaster di Stripchat (pannello Studio, tip menu, Lovense) ma con il funnel mainstream di xHamster — nella tua stanza arriva un mix di pubblico diverso."),
            ("Meglio l'encoder esterno se puoi", "L'RTMP da SplitCam dà bitrate stabile e scene multi-camera/overlay complete; il broadcaster del browser va bene ma limita le opzioni di composizione."),
            ("I tip menu convertono il pubblico mainstream", "Molti visitatori xHamster sono nuovi alle cam — un tip menu pulito a schermo e una goal bar fissano le aspettative e alzano la conversione."),
            _T_TEST,
        ],
        "faq": [
            ("xHamsterLive è la stessa cosa di Stripchat?", "Gira sul motore broadcaster di Stripchat, ma il brand e la fonte di traffico sono diversi — xHamster ci convoglia il suo pubblico mainstream, quindi il profilo dello spettatore differisce da una registrazione solo Stripchat."),
            ("Dove prendo la stream key di xHamsterLive?", "Nello Studio xHamsterLive, apri il pannello <em>Broadcast</em> o <em>External Encoder</em> — vedrai URL del server e stream key. Incolla entrambe nei campi RTMP personalizzato di SplitCam."),
            ("Broadcaster del browser o RTMP?", "L'encoder esterno (RTMP) è preferibile per chi fa sul serio — bitrate stabile e scene SplitCam complete. Anche il broadcaster del browser funziona: scegli SplitCam come webcam."),
            ("SplitCam è gratis su xHamsterLive?", "Sì — SplitCam è gratis, senza filigrana e senza limite di tempo."),
        ],
        "steps": [
            ("Scarica e installa SplitCam",
             "SplitCam è un software di live streaming gratuito per Windows e macOS — senza registrazione, senza carta, senza filigrana."),
            ("Componi la scena",
             "Apri SplitCam e aggiungi la webcam. Sovrapponi overlay, un tip menu, una seconda camera o il telefono, filtri beauty o sfondo IA — tutto in diretta."),
            ("Prendi URL e key dallo Studio xHamsterLive",
             "Accedi a xHamsterLive, apri lo Studio, passa a <strong>External Encoder</strong> e copia la <strong>URL del server</strong> e la tua <strong>stream key</strong>."),
            ("Collega SplitCam a xHamsterLive",
             "In SplitCam → <strong>Stream Settings → Custom RTMP</strong>, incolla URL e key. Imposta 4.000–6.000 Kbps a 1920×1080, 30 fps, keyframe ogni 2 secondi."),
            ("Clicca Go Live",
             "Premi <strong>Go Live</strong> in SplitCam, poi vai online dallo Studio xHamsterLive. In ~10 secondi il tuo flusso arriva sulla lista pubblica."),
        ],
    },
    {
        "slug": "premium-chat", "name": "Premium.Chat",
        "title": "Usare SplitCam su Premium.Chat — Videochiamate a pagamento",
        "desc": "Usa SplitCam gratis come camera virtuale su Premium.Chat — videochiamate al minuto con scene multi-camera, overlay e filtri. Senza filigrana.",
        "kw": "usare splitcam su premium chat, premium chat videochiamata, premium chat camera virtuale, premium.chat al minuto, premium chat modella, premium chat advisor, premium chat live, videochiamate splitcam",
        "h1html": 'Come usare SplitCam su <span class="accent">Premium.Chat</span>',
        "h1short": "Premium.Chat con SplitCam",
        "card": "Usa SplitCam come camera virtuale per le chiamate a pagamento di Premium.Chat.",
        "intro": "Premium.Chat è una piattaforma pay-per-minute: imposti la tua tariffa al minuto per chat, voce o <strong>videochiamate</strong>, condividi il tuo link personale e i clienti pagano per parlarti. Le chiamate girano nel browser, quindi <strong style='color:var(--text)'>SplitCam</strong> gratuito si collega direttamente come <strong>camera virtuale</strong> — scene multi-camera, overlay, filtri luce e sfondo IA arrivano al chiamante senza cambiare il funzionamento di Premium.Chat.",
        "quick": "Usare SplitCam su Premium.Chat: installare SplitCam, costruire una scena pulita per le videochiamate, accettare una chiamata Premium.Chat in arrivo e nel selettore camera della chiamata scegliere <em>SplitCam</em>."
                 "<ol><li>Installare SplitCam.</li><li>Sistemare la scena (buona luce, overlay opzionale).</li>"
                 "<li>Impostare la tariffa al minuto su Premium.Chat.</li>"
                 "<li>Accettare la videochiamata in arrivo.</li>"
                 "<li>Selezionare SplitCam come camera.</li></ol>",
        "key_how": "Le chiamate Premium.Chat avvengono nel browser. SplitCam installa una webcam virtuale chiamata <strong>\"SplitCam Video Driver\"</strong> — quando parte una chiamata, clicca il menu dell'icona camera nella finestra di Premium.Chat e passa dalla webcam integrata a <strong>SplitCam</strong>. La tua scena composta (camera reale + overlay + filtri) diventa ciò che vede il chiamante.",
        "tips": [
            ("Premium.Chat è al minuto, non streaming", "A differenza delle stanze a token stile Chaturbate, qui sei pagata al minuto. Luce soffusa, audio pulito e uno sfondo IA fanno sembrare la chiamata più una consulenza premium che una cam pubblica."),
            ("Promuovi il link, non un profilo", "Premium.Chat ti dà un link personale da mettere sui social, nella bio OnlyFans o in un Linktree — è così che i clienti ti trovano."),
            ("Overlay solo se servono", "Nelle chiamate 1-a-1 gli overlay pesanti distraggono. Usa SplitCam per la qualità camera, la luce e lo sfondo — tieni lo schermo prevalentemente su di te."),
            _T_TEST,
        ],
        "faq": [
            ("Come si collega SplitCam a Premium.Chat?", "Come camera virtuale. Le chiamate Premium.Chat girano nel browser; scegli SplitCam nel selettore camera della chiamata — niente stream key, niente RTMP."),
            ("Premium.Chat supporta OBS?", "Premium.Chat è browser-based, quindi OBS si collega come SplitCam — via camera virtuale. SplitCam è l'opzione più leggera e gratuita, senza filigrana."),
            ("Posso usare una seconda camera o un overlay su Premium.Chat?", "Sì — componi la scena in SplitCam (seconda camera, overlay, filtri) e Premium.Chat vede una sola webcam. Usali con misura nelle 1-a-1."),
            ("SplitCam è gratis?", "Sì — gratis, senza filigrana e senza limite di tempo."),
        ],
        "steps": [
            ("Scarica e installa SplitCam",
             "SplitCam è un software di live streaming gratuito per Windows e macOS — senza registrazione, senza carta, senza filigrana. Installa una camera virtuale che il browser può usare."),
            ("Prepara la scena per le chiamate",
             "Apri SplitCam, aggiungi la webcam, sistema la luce, eventualmente aggiungi uno sfondo IA o un overlay discreto. Inquadratura pulita — è una chiamata a pagamento, non un palco."),
            ("Imposta la tariffa su Premium.Chat",
             "Accedi a Premium.Chat, imposta la tariffa al minuto per le videochiamate e copia il tuo link personale. Condividilo sui social o nelle bio."),
            ("Accetta la videochiamata in arrivo",
             "Quando un cliente paga per il tempo, arriva la richiesta. Accettala nella dashboard di Premium.Chat."),
            ("Seleziona SplitCam come camera",
             "Nel menu dell'icona camera della finestra di chiamata, passa dalla webcam integrata a <strong>SplitCam</strong>. La tua scena composta arriva al chiamante."),
        ],
    },
    {
        "slug": "arousr", "name": "Arousr",
        "title": "Usare SplitCam su Arousr — Sexting e videochat",
        "desc": "Usa SplitCam gratis come camera virtuale su Arousr — scene multi-camera, overlay e filtri per sexting, voce e video a pagamento. Senza filigrana.",
        "kw": "usare splitcam su arousr, arousr videochat, arousr camera virtuale, arousr cam girl, arousr modella, sexting splitcam, arousr live, arousr broadcast",
        "h1html": 'Come usare SplitCam su <span class="accent">Arousr</span>',
        "h1short": "Arousr con SplitCam",
        "card": "Usa SplitCam come camera virtuale per le videochat Arousr.",
        "intro": "Arousr è una piattaforma a pagamento di <strong>sexting + voce + videochat</strong> — i clienti comprano crediti per scrivere, parlare o videochiamare le modelle e tu sei pagata a sessione. La parte video gira nel browser (o nell'app mobile Arousr sui telefoni), quindi <strong style='color:var(--text)'>SplitCam</strong> gratuito si collega come <strong>camera virtuale</strong> su desktop: scene multi-camera, overlay, filtri luce e sfondo IA passano direttamente al cliente.",
        "quick": "Usare SplitCam su Arousr: installare SplitCam, preparare la scena, accettare una richiesta video Arousr in arrivo e nel selettore camera scegliere <em>SplitCam</em>."
                 "<ol><li>Installare SplitCam.</li><li>Preparare scena + illuminazione.</li>"
                 "<li>Impostare le tariffe sexting/video su Arousr.</li>"
                 "<li>Accettare la richiesta video in arrivo.</li>"
                 "<li>Selezionare SplitCam nel menu camera.</li></ol>",
        "key_how": "Il video web di Arousr gira nel browser. SplitCam installa una webcam virtuale chiamata <strong>\"SplitCam Video Driver\"</strong> — quando parte una sessione video nella dashboard di Arousr, cambia camera nella finestra di sessione e seleziona <strong>SplitCam</strong>. La scena composta (camera + overlay + filtri) diventa ciò che vede il cliente. Sull'app mobile Arousr le camere virtuali non sono disponibili — lì usa la vera camera del telefono e riserva SplitCam per le sessioni desktop.",
        "tips": [
            ("Le sessioni sono pagate a tempo", "I clienti comprano crediti al minuto (o per messaggio in chat testo). Un video curato — buona luce, sfondo IA, filtro beauty — si ripaga in sessioni più lunghe."),
            ("Prima il sexting, poi l'upsell video", "Gran parte del fatturato Arousr è testo. Una breve anteprima video durante una chat sexting porta il cliente verso una sessione video completa — è lì che scatta la tariffa al minuto."),
            ("App mobile ≠ desktop", "Le camere virtuali funzionano nel video del browser su desktop. L'app mobile Arousr usa direttamente la camera del telefono — stesso flusso, strumento diverso."),
            _T_TEST,
        ],
        "faq": [
            ("Come si collega SplitCam ad Arousr?", "Come camera virtuale. La videochat Arousr gira nel browser su desktop — scegli SplitCam nel selettore camera. Nessuna stream key richiesta."),
            ("Arousr supporta OBS?", "Arousr è browser-based, quindi OBS si collega come SplitCam — via camera virtuale. SplitCam è l'opzione gratuita senza filigrana."),
            ("Posso usare overlay in una sessione sexting + video?", "Sì — componi la scena in SplitCam (luce, overlay, seconda camera) e Arousr vede una sola webcam. Tieni gli overlay leggeri nelle 1-a-1."),
            ("SplitCam è gratis con Arousr?", "Sì — gratis, senza filigrana e senza limite di tempo."),
        ],
        "steps": [
            ("Scarica e installa SplitCam",
             "SplitCam è un software di live streaming gratuito per Windows e macOS — senza registrazione, senza carta, senza filigrana. Installa una camera virtuale che il browser può scegliere."),
            ("Componi la scena",
             "Apri SplitCam, aggiungi la webcam, regola la luce, aggiungi eventualmente uno sfondo IA o un filtro beauty. Mantieni un'atmosfera intima — è una sessione 1-a-1 a pagamento, non un palco."),
            ("Imposta le tariffe su Arousr",
             "Accedi ad Arousr, imposta la tariffa al messaggio e al minuto video, e assicurati che il profilo sia approvato per ricevere richieste."),
            ("Accetta la richiesta video in arrivo",
             "Quando un cliente avvia una sessione video da una sexting chat o direttamente, accettala nella dashboard di Arousr."),
            ("Seleziona SplitCam come camera",
             "Nel menu camera della finestra di sessione, passa dalla webcam integrata a <strong>SplitCam</strong>. La tua scena composta arriva al cliente."),
        ],
    },
    {
        "slug": "cams-com", "name": "Cams.com",
        "title": "Trasmettere su Cams.com con SplitCam — RTMP/OBS",
        "desc": "Trasmettere su Cams.com con SplitCam gratis via RTMP — scene multi-camera, overlay e filtri. Raggiungi la base spender di AFF. Senza filigrana.",
        "kw": "trasmettere su cams.com, cams.com obs, cams.com rtmp, cams.com modella, cams.com broadcaster, cams.com stream key, adult friend finder cams, cams.com live, cams com registrazione modella",
        "h1html": 'Come trasmettere su <span class="accent">Cams.com</span> con SplitCam',
        "h1short": "Trasmettere su Cams.com",
        "card": "SplitCam gratis → stream RTMP verso il network Cams.com / AFF.",
        "intro": "Cams.com è il braccio cam del network AdultFriendFinder — uno degli ecosistemi dating + cam più longevi online, con una base consistente di <strong>membri già paganti</strong> che arrivano in flusso incrociato da AFF, AmateurMatch e altre proprietà FriendFinder. Le modelle trasmettono dal <strong>Model Center</strong> di Cams.com, che supporta sia il broadcaster integrato nel browser sia un <strong>encoder esterno via RTMP</strong>. <strong style='color:var(--text)'>SplitCam</strong> gratuito trasmette via RTMP per scene multi-camera complete, overlay e filtri — oppure, nel broadcaster del browser, si registra come <strong>camera virtuale</strong> per lo stesso risultato.",
        "quick": "Trasmettere su Cams.com: installare SplitCam, comporre la scena, prendere URL server e stream key dal Model Center di Cams.com, incollarli in SplitCam, premere Go Live."
                 "<ol><li>Installare SplitCam.</li><li>Aggiungere camera + scena.</li>"
                 "<li>Copiare URL server + key dal Model Center Cams.com → External Encoder.</li>"
                 "<li>Incollare nell'RTMP personalizzato di SplitCam.</li>"
                 "<li>Premere Go Live.</li></ol>",
        "key_how": "Il Model Center di Cams.com ha una scheda <strong>External Encoder / OBS</strong> con URL server e stream key. Incolla entrambe in <strong>Stream Settings → Custom RTMP</strong> di SplitCam; scegli 3.500–5.000 Kbps a 1920×1080, 30 fps, keyframe ogni 2 secondi. Clicca <strong>Go Live</strong> in SplitCam, poi avvia lo show dal Model Center. Se preferisci usare il broadcaster integrato nel browser, scegli <strong>SplitCam</strong> dal menu camera.",
        "tips": [
            ("Cross-traffic AFF = membri paganti", "Cams.com pesca spettatori da account AdultFriendFinder che hanno già un metodo di pagamento in archivio — diverso da un pubblico appena registrato. La conversione verso il privato e le mance tende a essere più alta."),
            ("L'encoder esterno batte il browser", "L'RTMP da SplitCam dà bitrate pulito e permette scene multi-camera con overlay; il broadcaster del browser funziona ma limita la produzione."),
            ("Usa gli strumenti del privato", "Cams.com punta su sessioni private/esclusive. Un tip menu e un percorso chiaro al privato (negli overlay) alzano in modo netto il ricavo per spettatore."),
            _T_TEST,
        ],
        "faq": [
            ("Cams.com è la stessa cosa di AdultFriendFinder?", "Stesso network madre. Cams.com è il brand cam-broadcasting; gli spettatori possono arrivare da AFF, AmateurMatch e altri siti FriendFinder — una grossa parte del suo traffico."),
            ("Dove prendo la stream key di Cams.com?", "Nel Model Center di Cams.com, apri la scheda <em>External Encoder</em> o <em>OBS</em> — vedrai URL del server e stream key. Incolla entrambe nei campi RTMP personalizzato di SplitCam."),
            ("Broadcaster del browser o RTMP?", "L'RTMP (encoder esterno) è preferibile — bitrate stabile, scene SplitCam complete. Il broadcaster del browser fa da fallback: scegli SplitCam come webcam."),
            ("SplitCam è gratis su Cams.com?", "Sì — SplitCam è gratis, senza filigrana e senza limite di tempo."),
        ],
        "steps": [
            ("Scarica e installa SplitCam",
             "SplitCam è un software di live streaming gratuito per Windows e macOS — senza registrazione, senza carta, senza filigrana."),
            ("Componi la scena",
             "Apri SplitCam e aggiungi la webcam. Sovrapponi overlay, un tip menu, una seconda camera o il telefono, filtri beauty o sfondo IA — tutto in diretta."),
            ("Prendi URL e stream key di Cams.com",
             "Accedi al Model Center di Cams.com, apri la scheda <strong>External Encoder / OBS</strong> e copia la <strong>URL del server</strong> e la <strong>stream key</strong>."),
            ("Collega SplitCam a Cams.com",
             "In SplitCam → <strong>Stream Settings → Custom RTMP</strong>, incolla URL e key. Imposta 3.500–5.000 Kbps a 1920×1080, 30 fps, keyframe ogni 2 secondi."),
            ("Clicca Go Live",
             "Premi <strong>Go Live</strong> in SplitCam, poi vai online dal Model Center. Il tuo flusso atterra nel network Cams.com / AFF in ~10 secondi."),
        ],
    },
    {
        "slug": "stripcamfun", "name": "StripCamFun",
        "title": "Trasmettere su StripCamFun con SplitCam — RTMP/OBS",
        "desc": "Trasmettere su StripCamFun con SplitCam gratis via RTMP — scene multi-camera, overlay e filtri per un pubblico cam indie. Senza filigrana.",
        "kw": "trasmettere su stripcamfun, stripcamfun, stripcamfun obs, stripcamfun rtmp, stripcamfun modella, stripcamfun broadcast, strip cam fun registrazione modella, stripcamfun stream key",
        "h1html": 'Come trasmettere su <span class="accent">StripCamFun</span> con SplitCam',
        "h1short": "Trasmettere su StripCamFun",
        "card": "SplitCam gratis → stream RTMP/OBS verso StripCamFun.",
        "intro": "StripCamFun è un sito live-cam indipendente — più piccolo dei giganti tipo Chaturbate ma con un pubblico reale, meno saturo e con molta meno concorrenza tra broadcaster per nicchia. Le modelle trasmettono dal pannello modella di StripCamFun, che espone un'opzione <strong>external-encoder / RTMP</strong>. <strong style='color:var(--text)'>SplitCam</strong> gratuito si collega via RTMP per scene multi-camera complete, overlay e filtri — e dove è offerto un broadcaster nel browser, SplitCam si registra anche come <strong>camera virtuale</strong>.",
        "quick": "Trasmettere su StripCamFun: installare SplitCam, comporre la scena, copiare URL server e stream key di StripCamFun, incollarli nelle impostazioni RTMP di SplitCam, premere Go Live."
                 "<ol><li>Installare SplitCam.</li><li>Aggiungere camera + scena.</li>"
                 "<li>Copiare URL + stream key dal pannello modella StripCamFun → External Encoder.</li>"
                 "<li>Incollare nell'RTMP personalizzato di SplitCam.</li>"
                 "<li>Premere Go Live.</li></ol>",
        "key_how": "Apri la dashboard modella di StripCamFun e la sezione <strong>External Encoder / OBS</strong>. Copia URL del server e stream key nei campi <strong>Stream Settings → Custom RTMP</strong> di SplitCam; imposta 3.500–5.000 Kbps a 1920×1080, 30 fps, keyframe ogni 2 secondi. Clicca <strong>Go Live</strong> in SplitCam, poi mettiti online dalla dashboard.",
        "tips": [
            ("Pool più piccolo, visibilità più facile", "Su un sito Tier-1 sei una tra migliaia online; su StripCamFun la lista broadcaster è corta — una scena SplitCam curata spicca in homepage molto prima."),
            ("Cross-broadcast per la reach", "I siti cam indie si sposano bene con il multi-streaming. Usa SplitCam per trasmettere in contemporanea su StripCamFun e un sito più grande, così peschi tipper da entrambi i bacini."),
            ("Punta sul tag di nicchia", "I pubblici indie cercano per nicchia più che per star. Tag specifici + un overlay di scena che nomina la nicchia tirano spettatori fuori dalla lista."),
            _T_TEST,
        ],
        "faq": [
            ("Dove prendo la stream key di StripCamFun?", "Nella dashboard modella, apri la scheda <em>External Encoder / OBS</em> — vedrai URL del server e stream key. Incolla entrambe nei campi RTMP personalizzato di SplitCam."),
            ("StripCamFun è sicuro per trasmettere?", "Come ogni sito cam indie, controlla l'accordo modella e i termini di payout prima di andare live. Usa un'email reale e verifica prima il metodo di pagamento."),
            ("Posso fare multi-stream su StripCamFun e un altro sito cam?", "Sì — SplitCam può spingere su più endpoint RTMP personalizzati in contemporanea. Verifica prima le regole di esclusiva di ogni sito."),
            ("SplitCam è gratis su StripCamFun?", "Sì — gratis, senza filigrana e senza limite di tempo."),
        ],
        "steps": [
            ("Scarica e installa SplitCam",
             "SplitCam è un software di live streaming gratuito per Windows e macOS — senza registrazione, senza carta, senza filigrana."),
            ("Componi la scena",
             "Apri SplitCam e aggiungi la webcam. Sovrapponi overlay, un tip menu, una seconda camera o il telefono, filtri beauty o sfondo IA — tutto in diretta."),
            ("Prendi URL e stream key di StripCamFun",
             "Accedi alla dashboard modella di StripCamFun, apri <strong>External Encoder / OBS</strong> e copia la <strong>URL del server</strong> e la <strong>stream key</strong>."),
            ("Collega SplitCam a StripCamFun",
             "In SplitCam → <strong>Stream Settings → Custom RTMP</strong>, incolla URL e key. Imposta 3.500–5.000 Kbps a 1920×1080, 30 fps, keyframe ogni 2 secondi."),
            ("Clicca Go Live",
             "Premi <strong>Go Live</strong> in SplitCam, poi mettiti online nella dashboard di StripCamFun. In ~10 secondi il tuo flusso arriva sulla lista pubblica."),
        ],
    },
    {
        "slug": "mym-fans", "name": "MYM.fans",
        "title": "Andare in diretta su MYM.fans con SplitCam — Camera virtuale",
        "desc": "Vai in diretta su MYM.fans (l'OnlyFans francese) con SplitCam gratis come camera virtuale — scene multi-camera, overlay e filtri. Senza filigrana.",
        "kw": "andare in diretta su mym, mym.fans live, mym fans camera virtuale, creator mym, mym francia, mym live stream, mym obs, mym fans broadcast, influencer mym",
        "h1html": 'Come andare in diretta su <span class="accent">MYM.fans</span> con SplitCam',
        "h1short": "In diretta su MYM.fans",
        "card": "Usa SplitCam come camera virtuale per le dirette MYM.fans.",
        "intro": "MYM.fans è la principale piattaforma francese di abbonamento per creator — la risposta francese a OnlyFans, con abbonamenti, pay-per-view, mance e una funzione di <strong>live stream</strong> integrata per i fan. Il broadcaster gira nel browser, quindi puntare il free <strong style='color:var(--text)'>SplitCam</strong> su MYM come <strong>camera virtuale</strong> aggiunge scene multi-camera, overlay e filtri sopra la webcam standard. Se la tua dashboard creator espone un'opzione external-encoder, SplitCam può collegarsi anche via RTMP.",
        "quick": "Vai in diretta su MYM.fans con SplitCam: installa SplitCam, componi la scena, avvia una diretta su MYM e nel selettore camera del broadcaster scegli <em>SplitCam</em> — poi vai live."
                 "<ol><li>Installa SplitCam.</li><li>Aggiungi camera + scena.</li><li>Avvia una diretta su MYM.fans.</li><li>Seleziona SplitCam nel menu camera.</li><li>Go Live.</li></ol>",
        "key_how": "La diretta di MYM.fans gira nel browser. Componi la scena in SplitCam — viene riconosciuto come una webcam chiamata <strong>\"SplitCam Video Driver\"</strong> — poi apri il broadcaster live di MYM e seleziona <strong>SplitCam</strong> nel menu camera. Se nella dashboard creator è offerta un'opzione <strong>stream-key / external-encoder</strong>, incollala nei campi Custom RTMP di SplitCam.",
        "tips": [
            ("La più grande piattaforma creator francese", "MYM è la fan-platform numero 1 in Francia, con un pubblico francese/europeo abituato a pagare in EUR. Una scena SplitCam curata + overlay in francese convertono meglio di una webcam piatta."),
            ("La camera virtuale funziona senza stream key", "La diretta solo-browser comunque ti permette la scena SplitCam completa — seconda camera, overlay, filtri beauty o sfondo IA — basta selezionare SplitCam come webcam."),
            ("Cross-sell PPV durante la diretta", "MYM è costruita attorno ai contenuti a pagamento. Overlay on-screen che promuovono l'abbonamento o lo sblocco di messaggi PPV trasformano gli spettatori live in abbonati paganti."),
            _T_TEST,
        ],
        "faq": [
            ("Come si collega SplitCam a MYM.fans?", "Le dirette MYM sono browser-based, quindi SplitCam si collega come camera virtuale — scegli SplitCam nel selettore camera. Nessuna stream key necessaria."),
            ("Posso usare overlay e più camere su MYM?", "Sì — componi la scena in SplitCam (seconda camera, overlay, sfondo IA); MYM vede la scena finita come un'unica webcam."),
            ("MYM.fans supporta OBS o encoder esterni?", "La diretta è principalmente browser/webcam-based. Se la dashboard offre un'opzione stream-key, incollala nei campi Custom RTMP di SplitCam; altrimenti usa il metodo camera virtuale."),
            ("SplitCam è gratis su MYM.fans?", "Sì — SplitCam è gratis, senza filigrana e senza limite di tempo."),
        ],
        "steps": [
            ("Scarica e installa SplitCam",
             "SplitCam è un software di live streaming gratuito per Windows e macOS — senza registrazione, senza carta, senza filigrana. Installa una camera virtuale che il browser può selezionare."),
            ("Componi la scena",
             "Apri SplitCam e aggiungi la webcam. Sovrapponi overlay, testo (in francese se il pubblico è FR), una seconda camera o il telefono, filtri beauty o sfondo IA."),
            ("Avvia una diretta su MYM.fans",
             "Accedi al tuo account creator MYM e apri il broadcaster live per avviare una diretta per i tuoi abbonati."),
            ("Seleziona SplitCam come camera",
             "Nel menu camera di MYM scegli <strong>SplitCam</strong> al posto della webcam grezza — la tua scena composta sostituisce la camera piatta. (Oppure incolla una stream key nei campi Custom RTMP di SplitCam se disponibile.)"),
            ("Go Live",
             "Avvia la trasmissione — la scena, gli overlay e i filtri di SplitCam arrivano ai tuoi abbonati MYM."),
        ],
    },
    {
        "slug": "fc2-live", "name": "FC2 Live",
        "title": "Trasmettere su FC2 Live con SplitCam (RTMP/OBS)",
        "desc": "Trasmetti su FC2 Live (la più grande live-cam del Giappone) con SplitCam gratis via RTMP — scene multi-camera, overlay e filtri. Senza filigrana.",
        "kw": "trasmettere su fc2 live, fc2 live obs, fc2 live rtmp, fc2 live broadcast, fc2 live配信, fc2 live stream key, fc2 live model, fc2 live giappone, fc2 ライブ",
        "h1html": 'Come trasmettere su <span class="accent">FC2 Live</span> con SplitCam',
        "h1short": "Trasmettere su FC2 Live",
        "card": "SplitCam gratis → stream RTMP/OBS verso FC2 Live.",
        "intro": "FC2 Live è la più grande piattaforma di live streaming del Giappone — un bacino di spettatori enorme, una sezione adulta dedicata e un flusso separato di paid show che ne fa uno dei mercati cam più redditizi dell'Asia. Le modelle trasmettono dal pannello broadcaster di FC2, che supporta sia il broadcaster nel browser sia un <strong>encoder esterno via RTMP</strong>. <strong style='color:var(--text)'>SplitCam</strong> gratuito si collega via RTMP per scene multi-camera complete, overlay e filtri.",
        "quick": "Trasmettere su FC2 Live con SplitCam: installa SplitCam, componi la scena, copia URL server + stream key dal pannello broadcaster FC2, incollali nelle impostazioni RTMP di SplitCam, premi Go Live."
                 "<ol><li>Installa SplitCam.</li><li>Aggiungi camera + scena.</li><li>Copia URL + stream key dal pannello broadcaster FC2.</li><li>Incolla nell'RTMP personalizzato di SplitCam.</li><li>Premi Go Live.</li></ol>",
        "key_how": "Apri il pannello broadcaster di FC2 Live e passa a <strong>External Encoder / RTMP</strong>. Copia URL del server e la tua stream key nei campi <strong>Stream Settings → Custom RTMP</strong> di SplitCam; imposta 3.500–5.000 Kbps a 1920×1080, 30 fps, keyframe ogni 2 secondi. Clicca <strong>Go Live</strong> in SplitCam, poi avvia lo show dalla dashboard FC2.",
        "tips": [
            ("Enorme pubblico giapponese", "FC2 è Tier 1 in Giappone — gli spettatori sono locali, abituati a pagare in JPY e propensi a paid show più lunghi. Overlay in giapponese (es. tip menu in 円 / JPY) alzano nettamente la conversione."),
            ("La sezione adulta è separata", "FC2 ha sia live general sia adult. Imposta correttamente la categoria della stanza prima di andare in diretta — gli show adulti non sono scopribili dalla sezione general."),
            ("Encoder esterno per un bitrate stabile", "Il pubblico giapponese, in gran parte mobile, è sensibile ai frame persi. RTMP da SplitCam a 4 Mbps costanti batte il broadcaster nel browser per affidabilità."),
            _T_TEST,
        ],
        "faq": [
            ("Dove prendo la stream key di FC2 Live?", "Nel pannello broadcaster di FC2 Live, passa a <em>External Encoder</em> o <em>OBS</em> — vedrai URL del server e stream key. Incolla entrambe nei campi Custom RTMP di SplitCam."),
            ("Broadcaster nel browser o RTMP?", "RTMP (encoder esterno) è preferito — bitrate stabile, scene SplitCam complete. Il broadcaster nel browser funziona come fallback: scegli SplitCam come webcam."),
            ("Serve un account giapponese per trasmettere su FC2?", "Serve un account FC2, e lo streaming adulto ha passaggi aggiuntivi di verifica età per la modella. Segui l'onboarding di FC2."),
            ("SplitCam è gratis su FC2 Live?", "Sì — SplitCam è gratis, senza filigrana e senza limite di tempo."),
        ],
        "steps": [
            ("Scarica e installa SplitCam",
             "SplitCam è un software di live streaming gratuito per Windows e macOS — senza registrazione, senza carta, senza filigrana."),
            ("Componi la scena",
             "Apri SplitCam e aggiungi la webcam. Sovrapponi overlay, un tip menu in 円 (JPY), una seconda camera o il telefono, filtri beauty o sfondo IA — tutto in diretta."),
            ("Prendi URL e stream key di FC2 Live",
             "Accedi a FC2, apri il pannello broadcaster Live, passa a <strong>External Encoder</strong> e copia <strong>URL del server</strong> e <strong>stream key</strong>."),
            ("Collega SplitCam a FC2 Live",
             "In SplitCam → <strong>Stream Settings → Custom RTMP</strong>, incolla URL e key. Imposta 3.500–5.000 Kbps a 1920×1080, 30 fps, keyframe ogni 2 secondi."),
            ("Clicca Go Live",
             "Premi <strong>Go Live</strong> in SplitCam, poi avvia lo show dalla dashboard FC2. In ~10 secondi il tuo flusso arriva sulla lista pubblica."),
        ],
    },
    {
        "slug": "boosty", "name": "Boosty",
        "title": "Andare in diretta su Boosty con SplitCam — Camera virtuale",
        "desc": "Vai in diretta su Boosty (la piattaforma creator russa) con SplitCam gratis come camera virtuale — scene multi-camera, overlay e filtri. Senza filigrana.",
        "kw": "andare in diretta su boosty, boosty live, boosty stream, boosty camera virtuale, creator boosty, бусти прямой эфир, boosty obs, boosty paid live, abbonato boosty",
        "h1html": 'Come andare in diretta su <span class="accent">Boosty</span> con SplitCam',
        "h1short": "In diretta su Boosty",
        "card": "Usa SplitCam come camera virtuale per le dirette Boosty.",
        "intro": "Boosty è la più grande piattaforma russa di monetizzazione per creator — un servizio in stile Patreon con abbonamenti, post a pagamento, mance e una funzione di <strong>diretta live</strong>, con un'utenza creator che include autori adult accanto a quelli mainstream. La diretta gira nel browser, quindi collegare il free <strong style='color:var(--text)'>SplitCam</strong> come <strong>camera virtuale</strong> aggiunge scene multi-camera, overlay e filtri che gli abbonati non avrebbero da una webcam piatta.",
        "quick": "Vai in diretta su Boosty con SplitCam: installa SplitCam, componi la scena, avvia una diretta su Boosty e seleziona <em>SplitCam</em> nel menu camera del broadcaster — poi vai live."
                 "<ol><li>Installa SplitCam.</li><li>Aggiungi camera + scena.</li><li>Avvia una diretta su Boosty.</li><li>Seleziona SplitCam nel menu camera.</li><li>Go Live.</li></ol>",
        "key_how": "La diretta di Boosty gira nel browser. Componi la scena in SplitCam — viene riconosciuto come una webcam chiamata <strong>\"SplitCam Video Driver\"</strong> — poi apri il broadcaster live di Boosty e scegli <strong>SplitCam</strong> nel menu camera al posto della webcam grezza.",
        "tips": [
            ("La più grande piattaforma creator della Russia", "Boosty ha sostituito Patreon per molti creator RU dopo le sanzioni, perciò il pubblico è fedele e abituato a pagare in RUB. Una scena SplitCam curata con overlay in russo converte bene."),
            ("Dirette gated per livello di abbonamento", "Boosty permette di limitare le dirette per tier di abbonamento. SplitCam funziona con tutti i tier — all'encoder non importa su quale tier sia lo spettatore: tu trasmetti una volta e Boosty gestisce l'accesso."),
            ("Overlay tip e pay-per-view", "Boosty supporta sblocchi di post a pagamento e mance. Un overlay on-screen che nomina i benefit del tier alza le conversioni durante le dirette."),
            _T_TEST,
        ],
        "faq": [
            ("Come si collega SplitCam a Boosty?", "La diretta Boosty è browser-based, quindi SplitCam si collega come camera virtuale — scegli SplitCam nel selettore camera. Nessuna stream key necessaria."),
            ("Posso usare overlay durante una diretta Boosty?", "Sì — componi la scena in SplitCam (overlay, seconda camera, sfondo IA); Boosty vede un'unica webcam. Gli abbonati vedono la scena composta completa."),
            ("Boosty supporta OBS o encoder esterni?", "La diretta Boosty è principalmente browser-based. Se nel pannello creator compare un'opzione stream-key, incollala nei campi Custom RTMP di SplitCam; altrimenti usa il metodo camera virtuale."),
            ("SplitCam è gratis su Boosty?", "Sì — SplitCam è gratis, senza filigrana e senza limite di tempo."),
        ],
        "steps": [
            ("Scarica e installa SplitCam",
             "SplitCam è un software di live streaming gratuito per Windows e macOS — senza registrazione, senza carta, senza filigrana. Installa una camera virtuale che il browser può selezionare."),
            ("Componi la scena",
             "Apri SplitCam e aggiungi la webcam. Sovrapponi overlay (in russo per il tuo pubblico), una seconda camera o il telefono, filtri beauty o sfondo IA."),
            ("Avvia una diretta su Boosty",
             "Accedi al tuo account creator Boosty e apri il broadcaster live. Imposta il gating per tier se vuoi che la diretta resti dietro un livello a pagamento."),
            ("Seleziona SplitCam come camera",
             "Nel menu camera di Boosty scegli <strong>SplitCam</strong> al posto della webcam grezza — la tua scena composta sostituisce la camera piatta."),
            ("Go Live",
             "Avvia la trasmissione — la scena, gli overlay e i filtri di SplitCam arrivano ai tuoi abbonati Boosty."),
        ],
    },
    {
        "slug": "amateurcommunity", "name": "AmateurCommunity",
        "title": "Trasmettere su AmateurCommunity con SplitCam (RTMP)",
        "desc": "Trasmetti su AmateurCommunity (il più grande cam amatoriale tedesco) con SplitCam gratis via RTMP — scene multi-camera, overlay e filtri. Senza filigrana.",
        "kw": "trasmettere su amateurcommunity, amateurcommunity obs, amateurcommunity rtmp, amateur community deutschland, amateurcommunity modella, ac community broadcast, amateurcommunity live, amateur cam deutschland",
        "h1html": 'Come trasmettere su <span class="accent">AmateurCommunity</span> con SplitCam',
        "h1short": "Trasmettere su AmateurCommunity",
        "card": "SplitCam gratis → stream RTMP verso AmateurCommunity (DE).",
        "intro": "AmateurCommunity è la più grande community cam e content amatoriale della Germania — attiva dai primi anni 2000 con un pubblico di lingua tedesca profondamente fedele, abituato a pagare per contenuti e dirette. Le modelle trasmettono dal pannello modella AC, che supporta un <strong>encoder esterno via RTMP</strong> oltre al broadcaster nel browser. <strong style='color:var(--text)'>SplitCam</strong> gratuito si collega via RTMP per scene multi-camera complete, overlay e filtri — overlay in tedesco parlano direttamente al pubblico locale.",
        "quick": "Trasmettere su AmateurCommunity: installa SplitCam, componi la scena, copia URL server + stream key di AC dal pannello modella, incollali nelle impostazioni RTMP di SplitCam, premi Go Live."
                 "<ol><li>Installa SplitCam.</li><li>Aggiungi camera + scena.</li><li>Copia URL + stream key dal pannello modella AC.</li><li>Incolla nell'RTMP personalizzato di SplitCam.</li><li>Premi Go Live.</li></ol>",
        "key_how": "Apri il pannello modella di AmateurCommunity e la scheda <strong>External Encoder / OBS</strong>. Copia URL del server e stream key nei campi <strong>Stream Settings → Custom RTMP</strong> di SplitCam; imposta 3.500–5.000 Kbps a 1920×1080, 30 fps, keyframe ogni 2 secondi. Clicca <strong>Go Live</strong> in SplitCam, poi mettiti online dal pannello.",
        "tips": [
            ("Pubblico di lingua tedesca, che paga in EUR", "Il pubblico di AmateurCommunity è in larga parte DACH (DE/AT/CH) e paga in EUR — overlay, tip menu e chat on-stream in tedesco convertono nettamente meglio dell'inglese."),
            ("Combo PPV premium + live", "AC consente di vendere contenuti PPV accanto alla diretta. Uno show live che teasera il PPV (con un overlay on-screen) tende ad alzare le vendite PPV durante e dopo la trasmissione."),
            ("Encoder esterno per qualità stabile", "Il pubblico di AC si aspetta alta produzione; RTMP a 4 Mbps costanti da SplitCam batte il bitrate variabile del broadcaster nel browser."),
            _T_TEST,
        ],
        "faq": [
            ("Dove prendo la stream key di AmateurCommunity?", "Nel pannello modella AC apri la scheda <em>External Encoder</em> o <em>OBS</em> — vedrai URL del server e stream key. Incolla entrambe nei campi Custom RTMP di SplitCam."),
            ("Broadcaster nel browser o RTMP?", "RTMP (encoder esterno) è preferito per modelle serie — bitrate stabile, scene SplitCam complete. Il broadcaster nel browser funziona come fallback: scegli SplitCam come webcam."),
            ("Devo essere in Germania per trasmettere su AC?", "No, ma il pubblico è di lingua tedesca. Le modelle possono registrarsi da ovunque — il passaggio chiave è superare la verifica modella e i moduli fiscali."),
            ("SplitCam è gratis su AmateurCommunity?", "Sì — SplitCam è gratis, senza filigrana e senza limite di tempo."),
        ],
        "steps": [
            ("Scarica e installa SplitCam",
             "SplitCam è un software di live streaming gratuito per Windows e macOS — senza registrazione, senza carta, senza filigrana."),
            ("Componi la scena",
             "Apri SplitCam e aggiungi la webcam. Sovrapponi overlay (in tedesco — \"Trinkgeld\" / \"PPV freischalten\"), una seconda camera o il telefono, filtri beauty o sfondo IA — tutto in diretta."),
            ("Prendi URL e stream key di AmateurCommunity",
             "Accedi al pannello modella AC, apri <strong>External Encoder / OBS</strong> e copia la <strong>URL del server</strong> e la <strong>stream key</strong>."),
            ("Collega SplitCam ad AmateurCommunity",
             "In SplitCam → <strong>Stream Settings → Custom RTMP</strong>, incolla URL e key. Imposta 3.500–5.000 Kbps a 1920×1080, 30 fps, keyframe ogni 2 secondi."),
            ("Clicca Go Live",
             "Premi <strong>Go Live</strong> in SplitCam, poi mettiti online nel pannello modella AC. In ~10 secondi il tuo flusso arriva sulla lista pubblica."),
        ],
    },
]
