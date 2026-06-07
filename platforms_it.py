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
        "kw": "trasmettere su chaturbate, chaturbate broadcast token, chaturbate rtmp obs, chaturbate encoder esterno, chaturbate live",
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
        "kw": "trasmettere su cam4, cam4.com, cam4 external encoder, cam4 stream key, cam4 rtmp obs",
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
        "kw": "bongacams, bongcams, trasmettere su bongacams, bongacams external encoder, bongacams rtmp obs",
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
        "kw": "strip cam, stripchat live stream, trasmettere su stripchat, stripchat external software, stripchat stream key, stripchat rtmp obs",
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
        "title": "Andare in diretta su OnlyFans con SplitCam — Autorizzazione o chiave",
        "desc": "Andare in diretta su OnlyFans con SplitCam gratis — accesso autorizzazione o OBS Key, scene multi-camera, overlay. Senza filigrana.",
        "kw": "andare in diretta su onlyfans, onlyfans live stream, onlyfans autorizzazione splitcam, onlyfans obs key, onlyfans software streaming",
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
        "kw": "trasmettere su camplace, camplace software trasmissione, camplace rtmp, camplace encoder esterno, camplace stream key",
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
        "title": "CamSoda live con SplitCam — Setup gratuito",
        "desc": "CamSoda live con SplitCam gratis — Use OBS Broadcaster, server regionali, scene e overlay. Senza filigrana, guida gratuita.",
        "kw": "camsoda live, trasmettere su camsoda, camsoda obs broadcaster, camsoda rtmp obs, camsoda live broadcast",
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
        "kw": "streamate, streamate sm connect, trasmettere su streamate, streamate software trasmissione, streamate rtmp",
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
        "kw": "streamray, streamray cam, trasmettere su streamray, streamray obs broadcaster, streamray rtmp",
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
        "kw": "xlovecam, x love cam, trasmettere su xlovecam, xlovecam rtmp link, xlovecam stream key",
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
        "kw": "soul cams, soulcams, trasmettere su soulcams, soulcams obs, soulcams rtmp, soulcams broadcast",
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
        "kw": "im live stream, imlive splitcam, trasmettere su imlive, imlive camera virtuale, imlive webcam, im live cam",
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
        "kw": "vxlive, visit-x, vxmodels splitcam, trasmettere su vxlive, visit-x stream, vxlive rtmp",
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
        "kw": "virtwish, trasmettere su virtwish, virtwish software trasmissione, virtwish rtmp, virtwish stream key, virtwish obs",
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
        "kw": "xmodels, trasmettere su xmodels, xmodels software trasmissione, xmodels rtmp, xmodels encoder esterno",
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
        "title": "Trasmettere su Flirt for Free cam con SplitCam — Guida gratuita",
        "desc": "Trasmettere su Flirt for Free cam con SplitCam gratis — External Broadcast Form, RTMP URL e Stream Name, scene e overlay.",
        "kw": "flirt for free cam, flirt 4 free cam, flirt4free, trasmettere su flirt4free, flirt4free external broadcast, flirt4free rtmp",
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
        "kw": "mfc alerts, myfreecams alerts, aggiungere mfc alerts, mfcalerts splitcam, myfreecams tip alerts, myfreecams alerts overlay",
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
        "kw": "aggiungere lovense allo stream, lovense cam stream, lovense splitcam, lovense splitcam toolset, lovense toy interattivo streaming",
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
        "desc": "Trasmettere su MyFreeCams, Chaturbate, BongaCams, CAM4, Stripchat e altri allo stesso tempo con la multidiffusione di SplitCam gratuita. Un clic, senza filigrana.",
        "kw": "trasmettere su più siti cam, multistream cam sites, trasmettere su chaturbate e bongacams insieme, software multidiffusione cam",
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
        "title": "Come trasmettere su LiveJasmin con SplitCam — encoder esterno HD",
        "desc": "Trasmettere su LiveJasmin con SplitCam gratis — encoder esterno del Model Center, setup HD 1080p, scene multicamera e overlay. Senza filigrana, senza registrazione.",
        "kw": "trasmettere livejasmin, livejasmin obs, livejasmin encoder esterno, livejasmin rtmp, livejasmin stream key, configurare modella livejasmin",
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
        "title": "Come trasmettere su MyFreeCams (MFC) con SplitCam — bypass del Model Web Broadcaster",
        "desc": "Trasmettere su MyFreeCams con SplitCam gratis — opzione broadcaster esterno del Model Admin, economia a token MFC, scene multicamera, overlay. Senza filigrana, senza registrazione.",
        "kw": "trasmettere myfreecams, mfc broadcaster esterno, myfreecams obs, mfc rtmp, mfc stream key, model admin, token mfc",
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
        "title": "Come trasmettere su Cherry.tv con SplitCam — encoder esterno Web3-friendly",
        "desc": "Trasmettere su Cherry.tv con SplitCam gratis — encoder esterno dello Streamer Dashboard, piattaforma cam cripto-friendly, scene multicamera. Senza filigrana, senza registrazione.",
        "kw": "trasmettere cherry tv, cherry.tv obs, cherry tv encoder esterno, cherry.tv rtmp, cherry.tv stream key, cherry tv streamer, cam web3",
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
        "title": "Come trasmettere su AmateurTV con SplitCam — il network cam in spagnolo",
        "desc": "Trasmettere su AmateurTV con SplitCam gratis — encoder esterno del Model Panel, network cam ispanofono (Spagna e LatAm), scene multicamera. Senza filigrana, senza registrazione.",
        "kw": "trasmettere amateurtv, amateur.tv obs, amateurtv encoder esterno, amateurtv rtmp, amateurtv stream key, modelle amateur tv",
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
        "title": "Come trasmettere su Camster con SplitCam — encoder esterno del Model Hub",
        "desc": "Trasmettere su Camster con SplitCam gratis — encoder esterno del Model Hub, piattaforma cam mid-tier consolidata, scene multicamera e overlay. Senza filigrana, senza registrazione.",
        "kw": "trasmettere camster, camster.com obs, camster encoder esterno, camster rtmp, camster stream key, camster model hub",
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
        "title": "Come trasmettere su Camversity con SplitCam — encoder esterno del Performer Dashboard",
        "desc": "Trasmettere su Camversity con SplitCam gratis — encoder esterno del Performer Dashboard, piattaforma cam indipendente in crescita, scene multicamera. Senza filigrana, senza registrazione.",
        "kw": "trasmettere camversity, camversity obs, camversity encoder esterno, camversity rtmp, camversity stream key, camversity performer",
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
        "title": "Come usare SkyPrivate con SplitCam — chiamate cam private via Skype",
        "desc": "Usa SkyPrivate con SplitCam gratuito come camera virtuale — chiamate cam private pay-per-minute via Skype, scene multicamera, filtri beauty. Senza filigrana, senza registrazione.",
        "kw": "skyprivate, sky private cam, skype cam privato, skyprivate splitcam, skyprivate camera virtuale, cam pay per minute",
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
        "title": "Come trasmettere su MV Live (ManyVids) con SplitCam — Creator Studio",
        "desc": "Trasmettere su MV Live di ManyVids con SplitCam gratuito — encoder esterno del Creator Studio, economia del creator stile OnlyFans, scene multicamera. Senza filigrana, senza registrazione.",
        "kw": "trasmettere manyvids, mv live, manyvids live broadcast, manyvids obs, mv live external encoder, manyvids stream key, manyvids creator",
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
        "title": "Come trasmettere su Fansly Live con SplitCam — encoder esterno del Creator Dashboard",
        "desc": "Trasmettere su Fansly Live con SplitCam gratuito — encoder esterno del Creator Dashboard, concorrente diretto di OnlyFans, scene multicamera e filtri beauty. Senza filigrana, senza registrazione.",
        "kw": "trasmettere fansly, fansly live, fansly broadcast, fansly obs, fansly encoder esterno, fansly rtmp, fansly stream key, fansly creator",
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
        "title": "Come trasmettere su iFriends con SplitCam — External Encoder del Model Center",
        "desc": "Trasmettere su iFriends con SplitCam gratuito — external encoder del Model Center, network cam indipendente di lunga data, scene multicamera. Senza filigrana, senza registrazione.",
        "kw": "trasmettere ifriends, ifriends obs, ifriends external encoder, ifriends rtmp, ifriends stream key, ifriends model center, ifriends.net",
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
        "title": "Come trasmettere su Babestation con SplitCam — setup del network cam UK",
        "desc": "Trasmettere su Babestation con SplitCam gratuito — external encoder del Performer Hub, network TV / cam per adulti del Regno Unito, scene multicamera e overlay. Senza filigrana, senza registrazione.",
        "kw": "trasmettere babestation, babestation cam, babestation obs, babestation external encoder, babestation rtmp, babestation performer, network cam uk",
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
        "title": "Come trasmettere su AdultWork con SplitCam — External Encoder della Members Area",
        "desc": "Trasmettere su AdultWork con SplitCam gratuito — external encoder della Members Area, marketplace britannico di servizi per adulti con funzione cam, scene multicamera. Senza filigrana, senza registrazione.",
        "kw": "trasmettere adultwork, adultwork cam, adultwork obs, adultwork external encoder, adultwork rtmp, adultwork webcam, cam uk",
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
        "title": "Trasmettere su Jerkmate con SplitCam — Setup rete Streamate",
        "desc": "Trasmettere su Jerkmate con SplitCam gratis — Jerkmate prende le sue modelle live dalla rete Streamate, quindi vai in onda tramite SM Connect e il canale Streamate integrato in SplitCam. Scene multi-camera, senza filigrana.",
        "kw": "trasmettere su jerkmate, diventare modella jerkmate, jerkmate cam, jerkmate streamate, jerkmate obs, jerkmate encoder esterno, jerkmate broadcast",
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
        "title": "Andare in diretta su JustForFans con SplitCam — Camera virtuale",
        "desc": "Andare in diretta su JustForFans (JFF) con SplitCam gratis — usa SplitCam come camera virtuale nel broadcaster live di JFF per scene multi-camera, overlay e filtri. Senza filigrana, senza registrazione.",
        "kw": "andare in diretta su justforfans, justforfans live, jff live stream, justforfans obs, justforfans camera virtuale, justfor.fans cam, justforfans broadcast",
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
]
