# -*- coding: utf-8 -*-
"""Portuguese (pt-BR) content for cam-streaming-guides. One dict per platform,
written natively for Brazilian and Portuguese audiences."""

_T_ETH = ("Use conexão por cabo", "Ethernet bate Wi-Fi numa live longa — um frame perdido é um "
          "tip perdido. Puxa um cabo até o PC do stream.")
_T_TEST = ("Faça um teste privado primeiro", "Rode uma transmissão curta de teste pra conferir "
           "câmera, áudio, enquadramento e overlays antes de abrir a sala pro público.")

PLATFORMS_PT = [
    {
        "slug": "chaturbate", "name": "Chaturbate",
        "title": "Transmitir no Chaturbate com SplitCam — Token & RTMP",
        "desc": "Transmitir no Chaturbate com SplitCam grátis — broadcast token, RTMP, cenas multi-câmera e overlays. Sem marca d'água, sem cadastro.",
        "kw": "transmitir no chaturbate, chaturbate broadcast token, chaturbate rtmp obs, chaturbate encoder externo, chaturbate live",
        "h1html": 'Como transmitir no <span class="accent">Chaturbate</span> com SplitCam',
        "h1short": "Transmitir no Chaturbate",
        "card": "Configuração por token com encoder externo no Chaturbate.",
        "intro": "O Chaturbate é uma das maiores plataformas cam, construída em economia de tokens. O broadcaster do navegador é só uma câmera plana — passar pelo <strong style='color:var(--text)'>encoder externo</strong> com o <strong style='color:var(--text)'>SplitCam</strong> grátis libera cenas multi-câmera, overlays e filtros nessa mesma transmissão baseada em token.",
        "quick": "Transmitir no Chaturbate com SplitCam: instalar SplitCam, montar a cena, no Chaturbate abrir <em>Broadcast Yourself → My Broadcast</em>, copiar o broadcast token, colar no SplitCam, Go Live."
                 "<ol><li>Instalar SplitCam.</li><li>Adicionar câmera + cena.</li>"
                 "<li>Copiar o broadcast token do Chaturbate.</li><li>Colar no SplitCam.</li>"
                 "<li>Pressionar Go Live.</li></ol>",
        "key_how": "No Chaturbate clica em <strong>Broadcast Yourself</strong> pra abrir a página <strong>My Broadcast</strong>, depois em <strong>View RTMP/OBS broadcast information and stream key</strong>. A chave aparece como o seu <strong>broadcast token</strong> — copia. Funciona como uma senha; nunca publica.",
        "tips": [
            ("O token é a chave", "O Chaturbate usa o seu broadcast token no lugar de uma stream key genérica. Trate como senha e resete se vazar."),
            ("Muita folga", "O ingest RTMP do Chaturbate aceita até 4K, 60 fps e bitrate bem alto — o limite é seu upload, não a plataforma. Keyframe a cada 2 segundos."),
            _T_ETH, _T_TEST,
        ],
        "faq": [
            ("O Chaturbate permite OBS / encoders externos?", "Sim — o Chaturbate suporta encoders externos oficialmente e tem seu próprio artigo «How do I set up OBS?». Ativa em «Use External Encoder to Broadcast» nas configurações de transmissão."),
            ("Onde está minha stream key do Chaturbate?", "Broadcast Yourself → My Broadcast → View RTMP/OBS broadcast information and stream key. A chave é o seu broadcast token."),
            ("Que bitrate pro Chaturbate?", "3.500–6.000 Kbps em 1080p basta de sobra. O teto do Chaturbate é alto — o limite real é seu upload; rode antes o teste de velocidade do SplitCam."),
            ("O SplitCam é grátis pro Chaturbate?", "Sim — totalmente grátis, sem marca d'água e sem limite de tempo: o encoder não engole seus ganhos em tokens."),
        ],
    },
    {
        "slug": "cam4", "name": "CAM4",
        "title": "Transmitir no CAM4 com SplitCam — External Encoder",
        "desc": "Transmitir no CAM4 com SplitCam grátis — External Encoder, stream key, geo-bloqueio e overlays. Sem marca d'água, guia grátis.",
        "kw": "transmitir no cam4, cam4.com, cam4 external encoder, cam4 stream key, cam4 rtmp obs",
        "h1html": 'Como transmitir no <span class="accent">CAM4</span> com SplitCam',
        "h1short": "Transmitir no CAM4",
        "card": "External Encoder no CAM4 com geo-controles.",
        "intro": "O CAM4 é uma plataforma cam-and-earn global com geo-controles embutidos — dá pra esconder sua transmissão em países selecionados. Transmitir pelo <strong style='color:var(--text)'>SplitCam</strong> grátis como encoder externo libera troca de cena e overlays que o broadcaster básico não faz.",
        "quick": "Transmitir no CAM4 com SplitCam: instalar SplitCam, montar a cena, no CAM4 abrir <em>Broadcast &amp; Earn Money → Start Broadcast → External Encoder</em>, Get Stream Key, colar no SplitCam, Go Live."
                 "<ol><li>Instalar SplitCam.</li><li>Adicionar câmera + cena.</li>"
                 "<li>Pegar a stream key do CAM4.</li><li>Colar no SplitCam.</li>"
                 "<li>Pressionar Go Live.</li></ol>",
        "key_how": "No CAM4 clica em <strong>Broadcast</strong> → <strong>Broadcast &amp; Earn Money</strong> → <strong>Start Broadcast</strong>, depois <strong>External Encoder</strong> em cima. Preenche data de nascimento, gênero e país, usa <strong>Get Stream Key</strong> e copia. Um slider verde no Stream Settings do SplitCam confirma a conexão.",
        "tips": [
            ("Configure as geo-restrições", "O CAM4 permite esconder a transmissão em países e regiões específicos — configure no lado CAM4 antes do live se precisar."),
            ("Olho no slider verde", "O setup do CAM4 mostra um slider verde no Stream Settings do SplitCam quando a chave é aceita — vermelho significa: revisa a chave."),
            ("Bitrate mais baixo que o normal", "O ingest do CAM4 limita o bitrate de vídeo a uns 3.000 Kbps — mais baixo que a maioria dos sites cam. Não empurra mais alto."),
            _T_ETH,
        ],
        "faq": [
            ("O CAM4 suporta oficialmente OBS / encoders externos?", "Sim — o CAM4 tem um OBS Guide oficial no site de suporte e recomenda a opção External Encoder pra melhor experiência. O SplitCam usa o mesmo caminho RTMP."),
            ("Posso geo-bloquear minha transmissão no CAM4?", "Sim — o CAM4 tem geo-restrição embutida pra esconder a transmissão em certos países. Configura no CAM4, não no SplitCam."),
            ("Onde fica a stream key do CAM4?", "Broadcast → Broadcast & Earn Money → Start Broadcast → External Encoder → Get Stream Key."),
            ("Que bitrate pro CAM4?", "Mais baixo que a média — o ingest do CAM4 limita em ~3.000 Kbps a 30 fps com keyframe de 1 segundo. A tabela oficial baseada em teste de velocidade recomenda não passar de ~3.000."),
        ],
    },
    {
        "slug": "bongacams", "name": "BongaCams",
        "title": "Transmitir no BongaCams com SplitCam — External Encoder",
        "desc": "Transmitir no BongaCams com SplitCam grátis — External Encoder, cenas multi-câmera, overlays e fundo com IA. Sem marca d'água.",
        "kw": "bongacams, bongcams, transmitir no bongacams, bongacams external encoder, bongacams rtmp obs",
        "h1html": 'Como transmitir no <span class="accent">BongaCams</span> com SplitCam',
        "h1short": "Transmitir no BongaCams",
        "card": "Configuração External Encoder pro BongaCams.",
        "intro": "O BongaCams é uma plataforma cam global. A transmissão por encoder externo nem sempre vem ativada — depois de liberada, o <strong style='color:var(--text)'>SplitCam</strong> grátis conduz a transmissão com cenas multi-câmera, overlays e fundo com IA.",
        "quick": "Transmitir no BongaCams com SplitCam: instalar SplitCam, montar a cena, no BongaCams abrir <em>Options → Broadcast settings → Select Encoder → External Encoder</em>, copiar URL e chave, colar no SplitCam, Go Live."
                 "<ol><li>Instalar SplitCam.</li><li>Adicionar câmera + cena.</li>"
                 "<li>Pegar URL e chave do BongaCams.</li><li>Colar no SplitCam.</li>"
                 "<li>Pressionar Go Live.</li></ol>",
        "key_how": "No BongaCams abre <strong>Options</strong> → <strong>Broadcast settings</strong> → <strong>Select Encoder</strong> → <strong>External Encoder</strong> e copia a URL do servidor e a stream key mostradas. <strong>Se o botão External Encoder não aparecer</strong>, fala com o suporte do BongaCams e pede pra liberar a codificação externa na sua conta.",
        "tips": [
            ("Sem botão External Encoder? Suporte", "O BongaCams libera codificação externa conta a conta — se a opção não estiver no Broadcast settings, é o suporte que ativa."),
            ("Casa a resolução", "O BongaCams recomenda que a resolução da webcam e a da transmissão coincidam — por exemplo as duas em 1280×720."),
            _T_ETH, _T_TEST,
        ],
        "faq": [
            ("Por que o botão External Encoder não aparece no BongaCams?", "A codificação externa não vem ativa por padrão em toda conta — fala com o suporte do BongaCams pra ativar e o botão aparece em Broadcast settings."),
            ("Preciso verificar a conta no BongaCams?", "Sim — pra transmitir é preciso ter 18+, ter documento oficial pra checagem de idade, e a aprovação da conta antes de entrar ao vivo."),
            ("Que bitrate pro BongaCams?", "O ingest RTMP do BongaCams limita o bitrate de vídeo em uns 6.000 Kbps com keyframe de 2 segundos — 3.500–6.000 em 1080p é o ponto ideal; testa o upload antes."),
            ("O SplitCam é grátis pro BongaCams?", "Sim — totalmente grátis, sem marca d'água e sem limite de tempo, então o encoder não morde seus ganhos em tokens no BongaCams."),
        ],
    },
    {
        "slug": "stripchat", "name": "Stripchat",
        "title": "Transmitir no Stripchat com SplitCam — Setup Strip Cam",
        "desc": "Transmitir no Stripchat — a plataforma strip cam — com SplitCam grátis. Software externo, chave-token, cenas e overlays.",
        "kw": "strip cam, stripchat live stream, transmitir no stripchat, stripchat external software, stripchat stream key, stripchat rtmp obs",
        "h1html": 'Como transmitir no <span class="accent">Stripchat</span> com SplitCam',
        "h1short": "Transmitir no Stripchat",
        "card": "Setup de software externo pra transmissões no Stripchat.",
        "intro": "O Stripchat é uma plataforma cam grande, focada em interatividade. O modo <em>external software</em> te dá uma chave baseada em token — joga ela no <strong style='color:var(--text)'>SplitCam</strong> grátis pra transmitir com cenas, overlays e filtros em vez de uma câmera plana.",
        "quick": "Transmitir no Stripchat com SplitCam: instalar SplitCam, montar a cena, no Stripchat escolher <em>Switch to external software</em>, copiar a stream key, colar no SplitCam, Go Live."
                 "<ol><li>Instalar SplitCam.</li><li>Adicionar câmera + cena.</li>"
                 "<li>Pegar a stream key do Stripchat.</li><li>Colar no SplitCam.</li>"
                 "<li>Pressionar Go Live.</li></ol>",
        "key_how": "No Stripchat escolhe <strong>Switch to external software</strong>, depois abre <strong>Show external software settings for the stream</strong>. Copia a stream key — o Stripchat mostra ela como um token. Mantém privada.",
        "tips": [
            ("Iguala a resolução à do site", "O FAQ do Stripchat avisa: a resolução no seu software tem que bater certinho com a do site, senão o vídeo pixela. Configure as duas iguais."),
            ("Cuidado com o mínimo de 2 Mbps", "O Stripchat informa 2 Mbps de upload como mínimo — e diz na lata que isso não é suficiente pra streaming via OBS nem pra multidifusão. Mire bem acima."),
            ("A chave é um token", "A stream key do Stripchat é um token — copia exata, nunca compartilha, reseta se vazar."),
            _T_ETH,
        ],
        "faq": [
            ("O Stripchat recomenda OBS / software externo?", "Sim — o FAQ oficial do Stripchat aconselha softwares de transmissão externos como OBS «pra obter melhor qualidade de vídeo e áudio». O SplitCam funciona igual."),
            ("Como troco o Stripchat pra software externo?", "No Broadcast Center escolhe Switch to External Broadcast Software (OBS), depois abre as configurações do software externo pra revelar a stream key (token)."),
            ("Que bitrate pro Stripchat?", "O ingest RTMP aceita até ~6.000 Kbps com keyframe de 2 segundos. 3.500–6.000 em 1080p é ideal — mas precisa ficar bem acima do mínimo de 2 Mbps, principalmente em streaming OBS."),
            ("O SplitCam é grátis pro Stripchat?", "Sim — sem taxa de licença, sem marca d'água, sem limite de tempo: nem shows interativos longos no Stripchat custam nada no lado do encoder."),
        ],
    },
    {
        "slug": "onlyfans", "name": "OnlyFans",
        "title": "Entrar ao vivo no OnlyFans com SplitCam — Autorização ou chave",
        "desc": "Entrar ao vivo no OnlyFans com SplitCam grátis — login por autorização ou OBS Key, cenas multi-câmera, overlays. Sem marca d'água.",
        "kw": "entrar ao vivo no onlyfans, onlyfans live stream, onlyfans autorização splitcam, onlyfans obs key, onlyfans software streaming",
        "h1html": 'Como entrar ao vivo no <span class="accent">OnlyFans</span> com SplitCam',
        "h1short": "Live no OnlyFans",
        "card": "Autorize uma vez ou cole a chave — live no OnlyFans.",
        "intro": "O live do OnlyFans é pros seus assinantes. O SplitCam conecta de <strong style='color:var(--text)'>duas formas</strong> — entra uma vez com seu login OnlyFans e o SplitCam busca e mantém a stream key sincronizada automaticamente, ou cola a OBS Key na mão. Nos dois casos você transmite com cenas multi-câmera, overlays e filtros.",
        "quick": "Live no OnlyFans com SplitCam: instalar SplitCam, montar a cena, abrir Stream Settings &rarr; Add Channel &rarr; OnlyFans e escolher <em>Autorização</em> — entrar com a conta OnlyFans, o SplitCam puxa a chave automaticamente — e clicar Go Live. Com a conta conectada dá pra mudar os parâmetros do stream OnlyFans dentro do SplitCam, sem abrir o site OnlyFans.",
        "steps": [
            ("Baixe e instale o SplitCam",
             "O SplitCam é um software de streaming grátis pra Windows e macOS — sem cadastro, sem cartão, sem marca d'água. É o encoder que envia seu vídeo pro OnlyFans."),
            ("Configure a câmera e a cena",
             "Abre o SplitCam e adiciona a webcam. Monta a cena que os espectadores vão ver — overlays, texto, uma segunda câmera, filtros de beleza ou fundo com IA, tudo aplicado ao vivo."),
            ("Conexão — Método 1: Autorização (recomendado)",
             "No SplitCam abre <strong>Stream Settings</strong> &rarr; <strong>Add Channel</strong> &rarr; <strong>OnlyFans</strong> e escolhe <strong>Autorização</strong>. Entra com email e senha do OnlyFans. O SplitCam conecta na sua conta, busca a stream key automaticamente e mantém sincronizada — e te deixa gerenciar os parâmetros do live OnlyFans dentro do SplitCam, mudando durante ou depois da transmissão sem abrir o site OnlyFans."),
            ("Conexão — Método 2: Stream Key (manual)",
             "Prefere não logar? Usa a chave. No OnlyFans vai em <strong>Profile</strong> &rarr; <strong>Settings</strong> &rarr; seção <strong>Other</strong> e copia a <strong>OBS Key</strong>. No SplitCam, Add Channel &rarr; OnlyFans, cola no campo de chave. Essa chave é estática — pra mudar configurações depois volta no site OnlyFans."),
            ("Go Live",
             "Seja qual for o método, aperta <strong>Go Live</strong> no SplitCam. Com o Método 1 dá pra continuar ajustando os parâmetros OnlyFans pelo SplitCam em tempo real; com o Método 2 a chave fica exatamente como você configurou."),
        ],
        "tips": [
            ("Autorização vs Stream Key", "Duas formas de conectar: <strong>Autorização</strong> (logar uma vez, a chave é puxada e mantida sincronizada — o jeito mais fácil) ou <strong>Stream Key</strong> (copia a OBS Key em OnlyFans → Profile → Settings → Other e cola). A autorização dispensa o copia-cola manual."),
            ("Mudar configs sem sair do SplitCam", "Com a autorização a conta fica conectada, então dá pra ajustar os parâmetros do live OnlyFans dentro do SplitCam no meio da transmissão ou depois — sem passar pelo site OnlyFans."),
            ("Mantém o bitrate modesto", "O ingest RTMP do OnlyFans limita o bitrate de vídeo em uns 2.500 Kbps — mais apertado que a maioria dos sites cam. Mira 720p–1080p em ~2.000–2.500."),
            _T_ETH,
        ],
        "faq": [
            ("Como conecto o OnlyFans no SplitCam?", "Duas formas. <strong>Autorização</strong> — Stream Settings → Add Channel → OnlyFans → entra com a conta OnlyFans e o SplitCam puxa a chave automaticamente. Ou <strong>Stream Key</strong> — copia a OBS Key em OnlyFans → Profile → Settings → Other e cola."),
            ("Posso mudar configurações do live OnlyFans sem abrir o site?", "Sim — com o método Autorização o SplitCam fica conectado na sua conta OnlyFans, então a chave e as configurações sincronizam sozinhas. Dá pra mudar tudo dentro do SplitCam durante ou depois da transmissão, sem visitar onlyfans.com."),
            ("Que bitrate pro OnlyFans?", "Modesto — o ingest RTMP do OnlyFans limita o bitrate em uns 2.500 Kbps, bem mais apertado que outras plataformas cam. Mira 720p–1080p em torno de 2.000–2.500 Kbps."),
            ("O SplitCam é grátis pra lives do OnlyFans?", "Sim — grátis, sem marca d'água e sem limite de tempo. Nenhum custo no lado do encoder."),
        ],
    },
    {
        "slug": "camplace", "name": "CamPlace",
        "title": "Transmitir no CamPlace com SplitCam — Guia grátis",
        "desc": "Transmitir no CamPlace com SplitCam grátis — encoder externo, chave RTMP, cenas e overlays. Guia passo a passo, sem marca d'água.",
        "kw": "transmitir no camplace, camplace software de transmissão, camplace rtmp, camplace encoder externo, camplace stream key",
        "h1html": 'Como transmitir no <span class="accent">CamPlace</span> com SplitCam',
        "h1short": "Transmitir no CamPlace",
        "card": "Setup de encoder externo pra transmissões no CamPlace.",
        "intro": "O CamPlace é uma plataforma cam-streaming. Não tem artigo público sobre OBS, então o <strong style='color:var(--text)'>guia em vídeo acima</strong> é a referência — o <strong style='color:var(--text)'>SplitCam</strong> grátis conecta via RTMP padrão e adiciona cenas, overlays e fundo com IA que a câmera básica não faz.",
        "quick": "Transmitir no CamPlace com SplitCam: instalar SplitCam, montar a cena, ativar a transmissão externa/RTMP no CamPlace, copiar URL do servidor e stream key, colar no SplitCam, Go Live. Segue o vídeo acima pro caminho atual."
                 "<ol><li>Instalar SplitCam.</li><li>Adicionar câmera + cena.</li>"
                 "<li>Pegar a chave RTMP do CamPlace.</li><li>Colar no SplitCam.</li>"
                 "<li>Pressionar Go Live.</li></ol>",
        "key_how": "Entra no CamPlace e abre as configurações de transmissão. Muda pra opção encoder externo / RTMP / OBS pra revelar a <strong>URL do servidor</strong> e a <strong>stream key</strong>, copia as duas. O CamPlace não publica documentação OBS oficial — o <strong>vídeo acima</strong> é o passo a passo mais confiável da interface atual.",
        "tips": [
            ("Sem guia OBS oficial — usa o vídeo", "O CamPlace não tem artigo público sobre encoders externos; o vídeo acima é a referência do caminho atual."),
            ("RTMP padrão funciona", "Mesmo sem documentação, o CamPlace aceita uma URL de servidor RTMP padrão e uma chave — o SplitCam conecta como destino RTMP personalizado."),
            ("Empilha overlays no SplitCam", "Metas de tip, nome e redes sociais como camadas de cena — a câmera básica do CamPlace não adiciona isso."),
            _T_ETH,
        ],
        "faq": [
            ("O CamPlace tem guia OBS oficial?", "Nenhum artigo público sobre encoders externos encontrado. O CamPlace aceita URL RTMP padrão e chave, então o SplitCam funciona — segue o vídeo acima."),
            ("O CamPlace suporta encoders externos?", "Sim — aceita uma stream key RTMP padrão, então o SplitCam conecta como destino RTMP personalizado."),
            ("Que bitrate pro CamPlace?", "O CamPlace não publica um número oficial — usa 3.500–6.000 Kbps em 1080p como faixa segura e deixa o teste de velocidade do SplitCam fixar seu teto real."),
            ("O SplitCam é grátis pro CamPlace?", "Sim — grátis, sem marca d'água e sem limite de tempo. Como o CamPlace não traz encoder próprio, uma ferramenta RTMP grátis dá conta."),
        ],
    },
    {
        "slug": "camsoda", "name": "CamSoda",
        "title": "CamSoda live com SplitCam — Setup grátis",
        "desc": "CamSoda live com SplitCam grátis — Use OBS Broadcaster, servidores regionais, cenas e overlays. Sem marca d'água, guia grátis.",
        "kw": "camsoda live, transmitir no camsoda, camsoda obs broadcaster, camsoda rtmp obs, camsoda live broadcast",
        "h1html": 'Como transmitir no <span class="accent">CamSoda</span> com SplitCam',
        "h1short": "Transmitir no CamSoda",
        "card": "Setup pelo Use OBS Broadcaster no CamSoda.",
        "intro": "O CamSoda é uma plataforma cam dos EUA conhecida por formatos de show interativos e diferentes. Suporta oficialmente transmissão por OBS — tem um botão <strong style='color:var(--text)'>Use OBS Broadcaster</strong> na página Go Live e um guia OBS oficial na wiki do CamSoda. O <strong style='color:var(--text)'>SplitCam</strong> grátis funciona do mesmo jeito.",
        "quick": "Transmitir no CamSoda com SplitCam: instalar SplitCam, montar a cena, clicar Use OBS Broadcaster na página Go Live do CamSoda, copiar URL do servidor e stream key, colar no SplitCam, Go Live."
                 "<ol><li>Instalar SplitCam.</li><li>Adicionar câmera + cena.</li>"
                 "<li>Clicar Use OBS Broadcaster no CamSoda.</li>"
                 "<li>Colar URL do servidor + chave no SplitCam.</li><li>Pressionar Go Live.</li></ol>",
        "key_how": "Na página <strong>Go Live</strong> do CamSoda clica em <strong>Use OBS Broadcaster</strong>. O CamSoda mostra a URL do servidor RTMP e a stream key — copia as duas. Escolhe o servidor regional (América do Norte, Europa, Ásia etc.) mais perto de você. A wiki do CamSoda tem um guia OBS completo se precisar do detalhe.",
        "tips": [
            ("Faça a verificação pra receber tips", "No CamSoda qualquer um pode transmitir, mas pra receber tips precisa concluir o processo de verificação do CamSoda."),
            ("Escolhe o servidor regional mais perto", "O CamSoda tem servidores de ingest regionais — escolher o mais perto (NA / Europa / Ásia / América do Sul / Oceania) reduz latência e frames perdidos."),
            ("Teto em 1080p / 30 fps", "O ingest do CamSoda vai até uns 1080p, 30 fps e ~6.000 Kbps — não precisa puxar mais alto."),
            _T_ETH,
        ],
        "faq": [
            ("O CamSoda suporta OBS / encoders externos?", "Sim — oficialmente. Tem o botão Use OBS Broadcaster na página Go Live e um guia OBS na wiki do CamSoda, então o SplitCam funciona."),
            ("Preciso me verificar no CamSoda?", "Pra transmitir, não. Pra receber tips, sim — o CamSoda exige completar o processo de verificação primeiro."),
            ("Que resolução o CamSoda suporta?", "Até 1920×1080 a 30 fps, em torno de 6.000 Kbps máximo no ingest RTMP."),
            ("O SplitCam é grátis pro CamSoda?", "Sim — grátis, sem marca d'água e sem limite de tempo. Funciona junto com o modo Use OBS Broadcaster grátis do CamSoda, então a cadeia toda não custa nada."),
        ],
    },
    {
        "slug": "streamate", "name": "Streamate",
        "title": "Transmitir no Streamate com SplitCam — Canal integrado",
        "desc": "Transmitir no Streamate com SplitCam grátis — canal integrado, chave SM Connect, cenas e overlays. Sem marca d'água, setup rápido.",
        "kw": "streamate, streamate sm connect, transmitir no streamate, streamate software transmissão, streamate rtmp",
        "h1html": 'Como transmitir no <span class="accent">Streamate</span> com SplitCam',
        "h1short": "Transmitir no Streamate",
        "card": "Streamate é canal integrado no SplitCam — setup rápido.",
        "intro": "O Streamate é uma plataforma cam estabelecida — e é um dos destinos <strong style='color:var(--text)'>pré-configurados no SplitCam</strong>, na lista de canais, então o setup é mais rápido que entrada RTMP manual: escolhe Streamate, cola a chave, pronto.",
        "quick": "Transmitir no Streamate com SplitCam: instalar SplitCam, montar a cena, no Streamate usar <em>SM Connect → Start Show</em> e copiar a chave, depois no SplitCam abrir <em>Stream Settings → Add Channel → Streamate</em> e colar."
                 "<ol><li>Instalar SplitCam.</li><li>Adicionar câmera + cena.</li>"
                 "<li>Pegar a chave Streamate via SM Connect.</li>"
                 "<li>Add Channel → Streamate no SplitCam.</li><li>Pressionar Go Live.</li></ol>",
        "key_how": "No Streamate abre <strong>SM Connect</strong>, aceita os termos, clica <strong>Start Show</strong> à esquerda e fecha a janela que abre — depois copia sua streaming key. No SplitCam abre <strong>Stream Settings</strong> → <strong>Add Channel</strong>, escolhe <strong>Streamate</strong> da lista e cola a chave. Um slider verde confirma a conexão.",
        "tips": [
            ("Streamate é canal integrado", "Não precisa URL RTMP manual — o SplitCam tem Streamate na lista Add Channel; só seleciona e cola a chave."),
            ("Fecha o popup do SM Connect", "Depois do Start Show o Streamate abre uma janela — fecha; ela só serviu pra revelar a streaming key."),
            ("Trava a resolução em 1080p", "O campo Video Resolution no SM Connect pode pular pra 1440, que na prática não é entregue e baixa silenciosamente sua qualidade — bota 1080p na mão. Bitrate caindo numa imagem parada é normal: o fluxo do Streamate é adaptativo."),
            _T_ETH, _T_TEST,
        ],
        "faq": [
            ("O Streamate é integrado no SplitCam?", "Sim — Streamate aparece na lista Add Channel do SplitCam; você seleciona em vez de digitar uma URL RTMP na mão."),
            ("Onde está a streaming key do Streamate?", "SM Connect → aceita os termos → Start Show → fecha o popup → copia a chave."),
            ("Que bitrate pro Streamate?", "O Streamate não fixa teto rígido — 3.500–6.000 Kbps em 1080p funciona bem. O fluxo é adaptativo, então bitrate mais baixo em imagem parada é normal, não bug."),
            ("O SplitCam é grátis pro Streamate?", "Sim — grátis, sem marca d'água e sem limite de tempo; e como Streamate é canal integrado no SplitCam, também não tem custo separado de encoder."),
        ],
    },
    {
        "slug": "streamray", "name": "StreamRay",
        "title": "Transmitir no StreamRay cam com SplitCam — URL do chat",
        "desc": "Transmitir no StreamRay cam com SplitCam grátis — URL postada no chat, modo OBS Broadcaster, cenas e overlays. Sem marca d'água.",
        "kw": "streamray, streamray cam, transmitir no streamray, streamray obs broadcaster, streamray rtmp",
        "h1html": 'Como transmitir no <span class="accent">StreamRay</span> com SplitCam',
        "h1short": "Transmitir no StreamRay",
        "card": "Setup de encoder externo URL-do-chat pro StreamRay.",
        "intro": "O StreamRay tem um setup de encoder externo incomum — entrega a URL do stream na <strong style='color:var(--text)'>janela de chat da transmissão</strong> e não usa stream key separada. O <strong style='color:var(--text)'>SplitCam</strong> grátis dá conta desse fluxo só-URL.",
        "quick": "Transmitir no StreamRay com SplitCam: instalar SplitCam, montar a cena, no StreamRay ativar o OBS Broadcaster, copiar a URL do stream da janela de chat, colar no SplitCam (deixa o campo de chave vazio), Go Live."
                 "<ol><li>Instalar SplitCam.</li><li>Adicionar câmera + cena.</li>"
                 "<li>Copiar a URL do StreamRay do chat.</li>"
                 "<li>Colar a URL no SplitCam.</li><li>Pressionar Go Live.</li></ol>",
        "key_how": "No StreamRay clica duas vezes em <strong>Broadcast Now</strong>, abre o menu <strong>Other</strong>, escolhe <strong>OBS Broadcaster</strong> e <strong>Save and Close</strong>. O StreamRay posta então sua <strong>URL do stream na janela de chat</strong> — copia de lá. Deixa o campo de stream key do SplitCam <strong>vazio</strong>; o StreamRay autentica só pela URL.",
        "tips": [
            ("A URL está no chat", "O StreamRay não mostra a URL do stream numa caixa de configurações — posta na janela de chat da transmissão. Copia de lá."),
            ("Deixa o campo de chave vazio", "O StreamRay não usa chave separada — só a URL. Não preenche o campo de chave no SplitCam."),
            _T_ETH, _T_TEST,
        ],
        "faq": [
            ("Onde está a URL do stream do StreamRay?", "Depois de ativar o OBS Broadcaster, o StreamRay posta a URL na janela de chat — copia do chat."),
            ("Por que não tem stream key no StreamRay?", "O StreamRay autentica só pela URL — deixa o campo de chave do SplitCam vazio."),
            ("Que bitrate pro StreamRay?", "O StreamRay não declara teto oficial — mira 3.500–6.000 Kbps em 1080p e roda o teste de velocidade do SplitCam, já que o modo só-URL não dá feedback de bitrate."),
            ("O SplitCam é grátis pro StreamRay?", "Sim — grátis, sem marca d'água e sem limite de tempo, o que combina com o fluxo só-URL do StreamRay: cola um link e tá no ar."),
        ],
    },
    {
        "slug": "xlovecam", "name": "XLoveCam",
        "title": "Transmitir no XLoveCam com SplitCam — Link RTMP & chave",
        "desc": "Transmitir no XLoveCam com SplitCam grátis — link RTMP e chave, servidores regionais, cenas e overlays. Sem marca d'água, guia grátis.",
        "kw": "xlovecam, x love cam, transmitir no xlovecam, xlovecam rtmp link, xlovecam stream key",
        "h1html": 'Como transmitir no <span class="accent">XLoveCam</span> com SplitCam',
        "h1short": "Transmitir no XLoveCam",
        "card": "Setup de link RTMP + chave pro XLoveCam.",
        "intro": "O XLoveCam é uma plataforma cam europeia e multilíngue. As configurações de conta expõem tanto um <strong style='color:var(--text)'>link RTMP</strong> quanto uma <strong style='color:var(--text)'>stream key</strong> — o <strong style='color:var(--text)'>SplitCam</strong> grátis pega os dois e transmite com cenas e overlays completos.",
        "quick": "Transmitir no XLoveCam com SplitCam: instalar SplitCam, montar a cena, no XLoveCam abrir <em>My Account → settings</em>, copiar link RTMP e stream key, colar os dois no SplitCam, iniciar o show."
                 "<ol><li>Instalar SplitCam.</li><li>Adicionar câmera + cena.</li>"
                 "<li>Copiar link RTMP + chave do XLoveCam.</li><li>Colar os dois no SplitCam.</li>"
                 "<li>Pressionar Go Live.</li></ol>",
        "key_how": "No XLoveCam abre <strong>My Account</strong> → <strong>settings</strong>. As configurações trazem tanto um <strong>link RTMP</strong> quanto uma <strong>stream key</strong> — copia os dois nos campos URL do servidor e chave do SplitCam, depois usa <strong>Start your show</strong> no XLoveCam.",
        "tips": [
            ("Copia link E chave", "O XLoveCam te dá um link RTMP E uma stream key separada — precisa dos dois no SplitCam, não só um."),
            ("Público multilíngue", "O XLoveCam é europeu e multilíngue — um overlay de texto claro no seu idioma ajuda os espectadores a te acharem."),
            ("Escolhe o servidor mais perto", "O XLoveCam tem servidores RTMP regionais — Europa, América do Norte, América do Sul e Ásia. O mais perto reduz latência e frames perdidos."),
            _T_ETH,
        ],
        "faq": [
            ("Onde estão os dados RTMP do XLoveCam?", "My Account → settings — mostra tanto o link RTMP quanto a chave."),
            ("O XLoveCam suporta encoders externos?", "Sim — fornece um link RTMP e uma chave, então o SplitCam funciona como encoder."),
            ("Que bitrate pro XLoveCam?", "O XLoveCam não publica limite fixo; 3.500–6.000 Kbps em 1080p é ideal. Escolher o servidor regional mais perto importa tanto quanto o número — reduz frames perdidos."),
            ("O SplitCam é grátis pro XLoveCam?", "Sim — grátis, sem marca d'água e sem limite de tempo. Atingir o público europeu multilíngue do XLoveCam não tem custo de software."),
        ],
    },
    {
        "slug": "soulcams", "name": "SoulCams",
        "title": "Transmitir no SoulCams com SplitCam — Configurações OBS",
        "desc": "Transmitir no SoulCams com SplitCam grátis — configurações OBS, servidor RTMP e chave, cenas multi-câmera e overlays.",
        "kw": "soul cams, soulcams, transmitir no soulcams, soulcams obs, soulcams rtmp, soulcams broadcast",
        "h1html": 'Como transmitir no <span class="accent">SoulCams</span> com SplitCam',
        "h1short": "Transmitir no SoulCams",
        "card": "Setup configurações OBS pro SoulCams.",
        "intro": "O SoulCams é uma plataforma cam cujas configurações OBS mostram <strong style='color:var(--text)'>servidor RTMP e stream key juntos</strong> numa janela. Joga os dois no <strong style='color:var(--text)'>SplitCam</strong> grátis pra transmitir com cenas multi-câmera e overlays.",
        "quick": "Transmitir no SoulCams com SplitCam: instalar SplitCam, montar a cena, no SoulCams clicar Go Online → Settings → OBS, copiar servidor e chave, colar os dois no SplitCam, Go Live."
                 "<ol><li>Instalar SplitCam.</li><li>Adicionar câmera + cena.</li>"
                 "<li>Abrir SoulCams Settings → OBS.</li><li>Colar servidor + chave no SplitCam.</li>"
                 "<li>Pressionar Go Live.</li></ol>",
        "key_how": "No SoulCams loga e clica <strong>Go Online</strong>, depois abre <strong>Settings</strong> → <strong>OBS</strong>. A janela OBS mostra <strong>servidor RTMP</strong> e <strong>stream key</strong> juntos — copia os dois no SplitCam.",
        "tips": [
            ("Servidor e chave lado a lado", "O SoulCams mostra servidor RTMP e chave na mesma janela OBS — pega os dois de uma vez."),
            ("Go Online primeiro", "As configurações OBS só aparecem depois de clicar Go Online no SoulCams — faz isso antes de procurar os dados do encoder."),
            ("Bloqueia regiões indesejadas", "O SoulCams permite bloqueio por país pelo lado da modelo — escolhe quais países não podem ver sua transmissão antes de clicar Go Online."),
            _T_ETH, _T_TEST,
        ],
        "faq": [
            ("Onde estão as configurações OBS do SoulCams?", "Loga, clica Go Online, depois Settings → OBS — servidor RTMP e stream key são mostrados juntos."),
            ("O SoulCams suporta encoders externos?", "Sim — as configurações OBS dão servidor RTMP e chave, então o SplitCam funciona."),
            ("Que bitrate pro SoulCams?", "O SoulCams não dá número oficial — mira 3.500–6.000 Kbps em 1080p e testa o upload antes, já que a janela OBS não mostra orientação de bitrate."),
            ("O SplitCam é grátis pro SoulCams?", "Sim — grátis, sem marca d'água e sem limite de tempo, então um show completo no SoulCams com cenas multi-câmera e overlays não custa nada pra codificar."),
        ],
    },
    {
        "slug": "imlive", "name": "ImLive",
        "title": "Transmitir no ImLive com SplitCam — Câmera virtual",
        "desc": "Setup Im Live stream com SplitCam grátis — o ImLive usa a webcam direto (sem RTMP), conecta o SplitCam como câmera virtual com cenas.",
        "kw": "im live stream, imlive splitcam, transmitir no imlive, imlive câmera virtual, imlive webcam, im live cam",
        "h1html": 'Como usar o <span class="accent">ImLive</span> com SplitCam',
        "h1short": "SplitCam no ImLive",
        "card": "Setup câmera virtual pro ImLive — sem RTMP.",
        "intro": "O ImLive usa sua webcam direto no navegador — não tem <strong style='color:var(--text)'>nem RTMP nem stream key</strong>. O <strong style='color:var(--text)'>SplitCam</strong> grátis conecta como <strong style='color:var(--text)'>câmera virtual</strong>: monta a cena no SplitCam e depois escolhe SplitCam como câmera dentro do ImLive.",
        "quick": "Usar o SplitCam no ImLive: instalar SplitCam, montar a cena com camadas de mídia, abrir o ImLive e iniciar um vídeo chat, nas configurações do ImLive selecionar SplitCam como webcam e microfone."
                 "<ol><li>Instalar SplitCam.</li><li>Montar a cena no SplitCam.</li>"
                 "<li>Iniciar um vídeo chat no ImLive.</li>"
                 "<li>Escolher SplitCam como câmera do ImLive.</li><li>Iniciar o chat.</li></ol>",
        "steps": [
            ("Instala o SplitCam",
             "O SplitCam é um software grátis pra Windows e macOS. Instala — sem marca d'água, sem cadastro. No ImLive funciona como <strong>câmera virtual</strong>, não como encoder RTMP."),
            ("Monta a cena no SplitCam",
             "Abre o SplitCam e usa <strong>Media Layers +</strong> pra adicionar a webcam mais quaisquer overlays, texto, filtros ou fundo com IA. Essa cena composta é o que o ImLive vai ver como sua câmera."),
            ("Inicia um vídeo chat no ImLive",
             "Entra no site do ImLive e clica <strong>Start Video Chat</strong>, depois abre <strong>Go To Settings</strong> pra chegar nas opções de câmera e microfone."),
            ("Escolhe SplitCam como câmera",
             "Nas configurações do ImLive escolhe <strong>SplitCam</strong> como webcam E como microfone. O ImLive mostra agora sua cena SplitCam completa em vez de uma webcam plana."),
            ("Inicia o Free Live Chat",
             "Clica <strong>Free Live Chat</strong> no ImLive pra entrar ao vivo. Pra mudar o visual no meio da sessão, edita a cena no SplitCam — o ImLive atualiza na hora."),
        ],
        "tips": [
            ("Não precisa de stream key", "O ImLive não tem RTMP — não procura URL do servidor nem chave. O SplitCam é só selecionado como dispositivo de câmera."),
            ("Bota SplitCam como mic também", "Escolhe SplitCam pro microfone além da câmera, pra que seu mix de áudio e a supressão de ruído passem pra live."),
            ("Monta a cena antes do live", "O ImLive mostra o que o SplitCam emitir — arruma as camadas antes de iniciar o chat."),
            _T_TEST,
        ],
        "faq": [
            ("O ImLive usa RTMP ou stream key?", "Não — o ImLive usa sua webcam direto pelo navegador. O SplitCam conecta como câmera virtual, não tem chave pra copiar."),
            ("Como escolho SplitCam no ImLive?", "Start Video Chat → Go To Settings → escolhe SplitCam como webcam e microfone."),
            ("Posso usar overlays no ImLive?", "Sim — monta na cena do SplitCam; o ImLive mostra o resultado composto."),
            ("O SplitCam é grátis pro ImLive?", "Sim — grátis, sem marca d'água e sem limite de tempo. Como câmera virtual pro ImLive não adiciona custo nem branding ao seu vídeo chat."),
        ],
    },
    {
        "slug": "vxlive", "name": "VXLive",
        "title": "Transmitir no VXLive com SplitCam — Suporte oficial",
        "desc": "Transmitir no VXLive (VXModels / VISIT-X) com SplitCam grátis — preset VISIT-X oficial, servidor e chave, cenas. Sem marca d'água.",
        "kw": "vxlive, visit-x, vxmodels splitcam, transmitir no vxlive, visit-x stream, vxlive rtmp",
        "h1html": 'Como transmitir no <span class="accent">VXLive</span> com SplitCam',
        "h1short": "Transmitir no VXLive",
        "card": "VXLive suporta SplitCam oficialmente (preset VISIT-X).",
        "intro": "O VXLive (VXModels / VISIT-X) é uma plataforma cam do mercado alemão — e uma das poucas que <strong style='color:var(--text)'>suporta SplitCam oficialmente pelo nome</strong>. A VXModels tem um artigo de ajuda dedicado pra conectar <strong style='color:var(--text)'>SplitCam</strong> ao VXLive, e o SplitCam traz VISIT-X como preset de canal pronto.",
        "quick": "Transmitir no VXLive com SplitCam: instalar SplitCam, montar a cena, no VXLive escolher «Stream with third-party software», copiar URL do servidor e chave, no SplitCam escolher o preset VISIT-X e colar, Go Live no SplitCam, depois GO ONLINE no VXLive."
                 "<ol><li>Instalar SplitCam.</li><li>Adicionar câmera + cena.</li>"
                 "<li>Pegar URL do servidor + chave do VXLive.</li>"
                 "<li>Escolher o preset VISIT-X no SplitCam, colar.</li>"
                 "<li>Go Live, depois GO ONLINE no VXLive.</li></ol>",
        "key_how": "No VXLive escolhe <strong>Stream with third-party software</strong> e seleciona a opção pra <strong>OBS, SplitCam ou XSplit</strong>. O VXLive fornece uma <strong>URL do servidor</strong> e uma <strong>stream key</strong>. No SplitCam escolhe <strong>VISIT-X</strong> como plataforma de streaming, cola os dois, aperta <strong>Go Live</strong> no SplitCam, depois <strong>GO ONLINE</strong> no VXLive.",
        "tips": [
            ("VISIT-X é preset integrado", "Não digita URL RTMP crua — o SplitCam tem VISIT-X na lista de plataformas; só seleciona e cola URL do servidor e chave."),
            ("Go-live em dois passos", "No VXLive aperta Go Live no SplitCam primeiro, depois GO ONLINE no VXLive — os dois, nessa ordem."),
            ("Mercado alemão", "O público VXLive é majoritariamente germânico — um overlay de texto ou título em alemão ajuda a conectar com os espectadores."),
            _T_ETH,
        ],
        "faq": [
            ("O VXLive suporta SplitCam oficialmente?", "Sim — a VXModels (VXLive) tem um artigo de ajuda oficial dedicado a configurar SplitCam e lista o SplitCam ao lado de OBS e XSplit como software de transmissão suportado."),
            ("Como conecto o SplitCam ao VXLive?", "No VXLive escolhe «Stream with third-party software», depois no SplitCam seleciona o preset VISIT-X e cola a URL do servidor e a stream key fornecidas pelo VXLive."),
            ("Eu entro ao vivo no SplitCam ou no VXLive?", "Nos dois — primeiro Go Live no SplitCam, depois GO ONLINE no VXLive."),
            ("Por que a VXModels recomenda o SplitCam?", "O artigo oficial de ajuda da VXModels recomenda SplitCam especificamente pra eliminar artefatos de imagem e pixelização da webcam e estabilizar a conexão — não só como encoder genérico."),
        ],
    },
    {
        "slug": "virtwish", "name": "VirtWish",
        "title": "Transmitir no VirtWish com SplitCam — URL & chave de stream",
        "desc": "Transmitir no VirtWish com SplitCam grátis — Profile → Start Broadcast seção OBS, URL do stream e chave, cenas e overlays.",
        "kw": "virtwish, transmitir no virtwish, virtwish software transmissão, virtwish rtmp, virtwish stream key, virtwish obs",
        "h1html": 'Como transmitir no <span class="accent">VirtWish</span> com SplitCam',
        "h1short": "Transmitir no VirtWish",
        "card": "Setup URL do stream + chave pro VirtWish.",
        "intro": "O VirtWish é uma plataforma cam interativa. As configurações de transmissão te dão uma <strong style='color:var(--text)'>URL do stream e uma stream key separada</strong> numa seção OBS — o <strong style='color:var(--text)'>SplitCam</strong> grátis pega as duas e toca o show com cenas e overlays.",
        "quick": "Transmitir no VirtWish com SplitCam: instalar SplitCam, montar a cena, no VirtWish abrir <em>Profile → Start Broadcast</em> até a seção OBS, copiar link e chave, colar os dois no SplitCam, Go Live."
                 "<ol><li>Instalar SplitCam.</li><li>Adicionar câmera + cena.</li>"
                 "<li>Pegar URL + chave do VirtWish.</li><li>Colar os dois no SplitCam.</li>"
                 "<li>Pressionar Go Live.</li></ol>",
        "key_how": "No VirtWish clica no ícone do canto superior direito → <strong>Profile</strong> → <strong>Start Broadcast</strong>, depois <strong>Start Broadcast</strong> de novo pra chegar na seção OBS. <strong>Copia o link da primeira linha</strong> no campo Stream URL do SplitCam, e a <strong>Stream Key</strong> separadamente no campo de chave.",
        "tips": [
            ("O link tá na primeira linha", "A seção OBS do VirtWish coloca a URL do stream na primeira linha — copia isso pro Stream URL do SplitCam, depois a chave separada."),
            ("Dois cliques em Start Broadcast", "Você clica Start Broadcast duas vezes no VirtWish pra chegar na seção OBS — é o esperado, não bug."),
            _T_ETH, _T_TEST,
        ],
        "faq": [
            ("Onde estão os dados RTMP do VirtWish?", "Ícone canto superior direito → Profile → Start Broadcast duas vezes → a seção OBS mostra o link e a stream key."),
            ("O VirtWish suporta encoders externos?", "Sim — a seção OBS fornece URL do stream e chave, então o SplitCam funciona."),
            ("Que bitrate pro VirtWish?", "O VirtWish não publica teto oficial; 3.500–6.000 Kbps em 1080p é faixa segura. Iguala a resolução do SplitCam à definida no VirtWish pra evitar rescaling."),
            ("O SplitCam é grátis pro VirtWish?", "Sim — grátis, sem marca d'água e sem limite de tempo. O setup URL-e-chave do VirtWish custa só os poucos minutos que leva."),
        ],
    },
    {
        "slug": "xmodels", "name": "XModels",
        "title": "Transmitir no XModels com SplitCam — Guia grátis",
        "desc": "Transmitir no XModels com SplitCam grátis — opção encoder externo nas configurações da conta modelo, chave RTMP, cenas e overlays.",
        "kw": "xmodels, transmitir no xmodels, xmodels software transmissão, xmodels rtmp, xmodels encoder externo",
        "h1html": 'Como transmitir no <span class="accent">XModels</span> com SplitCam',
        "h1short": "Transmitir no XModels",
        "card": "Setup encoder externo pra transmissões no XModels.",
        "intro": "O XModels é uma plataforma cam-streaming com uma <strong style='color:var(--text)'>opção de encoder externo</strong> integrada nas configurações da conta modelo. O <strong style='color:var(--text)'>SplitCam</strong> grátis transmite ali com cenas multi-câmera, overlays e filtros em vez de uma única câmera plana.",
        "quick": "Transmitir no XModels com SplitCam: instalar SplitCam, montar a cena, na conta modelo do XModels ativar a opção de encoder externo, copiar URL do servidor e stream key, colar no SplitCam, Go Live."
                 "<ol><li>Instalar SplitCam.</li><li>Adicionar câmera + cena.</li>"
                 "<li>Ativar o encoder externo nas configurações do XModels.</li>"
                 "<li>Colar URL do servidor + chave no SplitCam.</li><li>Pressionar Go Live.</li></ol>",
        "key_how": "Nas <strong>configurações da sua conta modelo</strong> do XModels, ativa a opção <strong>transmitir por encoder externo</strong>. O XModels fornece uma <strong>stream key</strong> — copia pro SplitCam. Se a opção não estiver onde você espera, o suporte XModels é via chat de FAQ no site e <strong>info@xmodels.com</strong>; o vídeo acima também mostra.",
        "tips": [
            ("Tá nas configurações da conta", "O XModels coloca a opção de encoder externo dentro das configurações da conta modelo, não numa tela de transmissão separada."),
            ("Suporte: chat + email", "O XModels não tem um grande centro de ajuda público — o chat FAQ no site e info@xmodels.com são os canais oficiais de suporte."),
            ("Empilha overlays no SplitCam", "Metas de tip, nome e redes sociais como camadas de cena — a câmera básica do XModels não adiciona isso."),
            _T_ETH,
        ],
        "faq": [
            ("O XModels suporta encoders externos?", "Sim — as configurações da conta modelo incluem uma opção de transmissão por encoder externo que fornece uma stream key, então o SplitCam funciona."),
            ("Onde busco ajuda do XModels?", "O suporte XModels é via chat FAQ no site e o email info@xmodels.com — não tem um grande centro de ajuda público."),
            ("Que bitrate pro XModels?", "O XModels não documenta número oficial — usa 3.500–6.000 Kbps em 1080p e roda o teste de velocidade do SplitCam, já que o suporte XModels é só chat e email."),
            ("O SplitCam é grátis pro XModels?", "Sim — grátis, sem marca d'água e sem limite de tempo, então transmitir pra rede europeia do XModels não adiciona custo de software."),
        ],
    },
    {
        "slug": "flirt4free", "name": "Flirt4Free",
        "title": "Transmitir no Flirt for Free cam com SplitCam — Guia grátis",
        "desc": "Transmitir no Flirt for Free cam com SplitCam grátis — External Broadcast Form, RTMP URL e Stream Name, cenas e overlays.",
        "kw": "flirt for free cam, flirt 4 free cam, flirt4free, transmitir no flirt4free, flirt4free external broadcast, flirt4free rtmp",
        "h1html": 'Como transmitir no <span class="accent">Flirt4Free</span> com SplitCam',
        "h1short": "Transmitir no Flirt4Free",
        "card": "Setup External Broadcast Form pro Flirt4Free.",
        "intro": "O Flirt4Free é uma das plataformas cam mais antigas, no ar desde os anos 1990. Suporta oficialmente transmissão externa via um <strong style='color:var(--text)'>External Broadcast Form</strong> — o <strong style='color:var(--text)'>SplitCam</strong> grátis envia o stream enquanto o formulário define resolução e bitrate.",
        "quick": "Transmitir no Flirt4Free com SplitCam: instalar SplitCam, montar a cena, abrir o External Broadcast Form do Flirt4Free, copiar RTMP URL e Stream Name e definir resolução/bitrate, colar no SplitCam, Go Live."
                 "<ol><li>Instalar SplitCam.</li><li>Adicionar câmera + cena.</li>"
                 "<li>Abrir o External Broadcast Form do Flirt4Free.</li>"
                 "<li>Colar RTMP URL + Stream Name no SplitCam.</li>"
                 "<li>Pressionar Go Live.</li></ol>",
        "key_how": "Na área da modelo do Flirt4Free abre o <strong>External Broadcast Form</strong>. Diferente da maioria dos sites cam, o Flirt4Free te dá uma <strong>RTMP URL</strong> e um <strong>Stream Name</strong> (não uma «chave»), mais campos de resolução e bitrate que você preenche no próprio formulário. Copia URL e Stream Name nos campos servidor e chave do SplitCam.",
        "tips": [
            ("É Stream Name, não chave", "O Flirt4Free chama o credencial de Stream Name. Cola no campo stream key do SplitCam — cumpre o mesmo papel."),
            ("Define resolução/bitrate no formulário", "O External Broadcast Form do Flirt4Free tem campos próprios de resolução e bitrate — alinha com as configurações do SplitCam pra imagem não ser reescalada."),
            ("Plataforma histórica", "O Flirt4Free roda desde os anos 90 — as ferramentas pra modelos são maduras e o External Broadcast Form é parte documentada disso."),
            _T_ETH,
        ],
        "faq": [
            ("O Flirt4Free suporta encoders externos?", "Sim — oficialmente, via o External Broadcast Form, que fornece RTMP URL e Stream Name. O SplitCam funciona como encoder."),
            ("Onde pego os dados RTMP do Flirt4Free?", "Do External Broadcast Form na área da modelo — mostra RTMP URL, Stream Name e campos de resolução/bitrate."),
            ("Que bitrate pro Flirt4Free?", "3.500–6.000 Kbps em 1080p — define o mesmo valor no External Broadcast Form e no SplitCam."),
            ("O SplitCam é grátis pro Flirt4Free?", "Sim — grátis, sem marca d'água e sem limite de tempo, o que combina com uma plataforma histórica como o Flirt4Free, onde os shows podem ser longos."),
        ],
    },
    {
        "slug": "mfc-alerts", "name": "MFC Alerts",
        "title": "Adicionar MFC Alerts ao stream com SplitCam",
        "desc": "Mostrar alerts animados de tips no stream MyFreeCams — URL do mfcalerts.com como camada Browser no SplitCam grátis, acima da webcam.",
        "kw": "mfc alerts, myfreecams alerts, adicionar mfc alerts, mfcalerts splitcam, myfreecams tip alerts, myfreecams alerts overlay",
        "h1html": 'Como adicionar <span class="accent">MFC Alerts</span> ao seu stream',
        "h1short": "Adicionar MFC Alerts",
        "card": "Mostre alerts animados de tips no seu stream MyFreeCams.",
        "intro": "O MFC Alerts mostra efeitos animados no seu stream MyFreeCams sempre que um espectador manda um tip. Roda como <strong style='color:var(--text)'>camada Browser</strong> dentro do <strong style='color:var(--text)'>SplitCam</strong> grátis — configura uma vez e os tips disparam reações na tela ao vivo.",
        "quick": "Adicionar MFC Alerts com SplitCam: instalar SplitCam, adicionar a webcam, abrir a aba Browser e carregar mfcalerts.com, copiar sua URL de alerts, adicionar como camada Browser acima da webcam, depois testar com um tip de teste."
                 "<ol><li>Instalar SplitCam.</li><li>Adicionar a webcam.</li>"
                 "<li>Pegar a URL em mfcalerts.com.</li>"
                 "<li>Adicionar como camada Browser acima da webcam.</li>"
                 "<li>Mandar um tip de teste.</li></ol>",
        "steps": [
            ("Instala o SplitCam e adiciona a webcam",
             "Instala o SplitCam grátis pra Windows ou macOS, depois adiciona a <strong>webcam</strong> como fonte. O MFC Alerts vai ficar como camada em cima dessa câmera."),
            ("Abre a aba Browser e vai pra mfcalerts.com",
             "No SplitCam abre a aba <strong>Browser</strong> e navega pra <strong>www.mfcalerts.com</strong>. Loga, ou cadastra se ainda não tem conta no mfcalerts.com."),
            ("Copia sua URL de alerts",
             "No mfcalerts.com usa <strong>Copy to clipboard</strong> pra copiar sua URL pessoal de alerts — é a página que renderiza as animações dos tips."),
            ("Adiciona a URL como camada Browser — acima da webcam",
             "Cola a URL na janela Browser do SplitCam e clica <strong>Add</strong>. Depois reordena a lista de fontes pra que o <strong>MFC Alerts fique acima da sua webcam</strong> (menu 3 pontos → Move Up). Se ficar abaixo, os efeitos ficam escondidos."),
            ("Testa com um tip de teste",
             "Abre <strong>Settings → Send test tip</strong> e confirma que o efeito de alert aparece sobre sua câmera. Depois transmite no MyFreeCams normal — tips reais disparam agora as animações."),
        ],
        "tips": [
            ("MFC Alerts tem que ficar acima da webcam", "O erro mais comum: se a camada MFC Alerts fica abaixo da webcam na lista de fontes, os efeitos ficam escondidos. Sobe."),
            ("Precisa de conta no mfcalerts.com", "A URL de alerts é pessoal — cadastra no mfcalerts.com primeiro se não tem conta."),
            ("Manda um tip de teste antes do live", "Usa Settings → Send test tip pra confirmar que o overlay funciona — não descobre o erro no meio do show."),
            _T_ETH,
        ],
        "faq": [
            ("O que é MFC Alerts?", "Um sistema de notificações pro MyFreeCams que mostra efeitos de vídeo no seu stream quando espectadores mandam tips — adicionado como overlay Browser no SplitCam."),
            ("Por que meus MFC Alerts não aparecem?", "Quase sempre é a ordem das camadas — a camada Browser do MFC Alerts tem que ficar acima da webcam na lista de fontes do SplitCam."),
            ("Preciso de conta pro MFC Alerts?", "Sim — cadastra no mfcalerts.com pra pegar sua URL pessoal de alerts."),
            ("O SplitCam é grátis pra isso?", "Sim — o SplitCam é grátis, sem marca d'água e sem limite de tempo, e o overlay browser do MFC Alerts roda dentro dele sem custo extra."),
        ],
    },
    {
        "slug": "lovense", "name": "Lovense",
        "title": "Adicionar um toy Lovense ao stream com SplitCam",
        "desc": "Conectar um toy Lovense interativo ao stream cam com SplitCam grátis — Lovense SplitCam Toolset, alerts de tips na tela, reações.",
        "kw": "adicionar lovense ao stream, lovense cam stream, lovense splitcam, lovense splitcam toolset, lovense toy interativo streaming",
        "h1html": 'Como adicionar um <span class="accent">toy Lovense</span> ao seu stream',
        "h1short": "Adicionar toy Lovense",
        "card": "Conectar um toy Lovense interativo ao seu stream cam.",
        "intro": "Roda seu stream cam pelo <strong style='color:var(--text)'>SplitCam</strong> grátis e pareia um toy <strong style='color:var(--text)'>Lovense</strong> que reage a tokens. A Lovense documenta oficialmente um <strong style='color:var(--text)'>Lovense SplitCam Toolset</strong>, e o SplitCam traz um plugin Lovense oficial — a integração é suportada dos dois lados.",
        "quick": "Pra adicionar um toy Lovense ao stream: instalar SplitCam e o software Lovense, parear o toy, ligar o Lovense à sua plataforma cam, adicionar o status Lovense como camada Browser no SplitCam, depois transmitir normal."
                 "<ol><li>Instalar SplitCam.</li><li>Instalar e parear o software Lovense.</li>"
                 "<li>Ligar o Lovense ao seu site cam.</li>"
                 "<li>Adicionar o overlay Lovense no SplitCam.</li><li>Pressionar Go Live.</li></ol>",
        "steps": [
            ("Instala o SplitCam",
             "O SplitCam é um software de streaming grátis pra Windows e macOS — o encoder que envia seu vídeo pra sua plataforma cam. Instala; sem marca d'água."),
            ("Instala e pareia o software Lovense",
             "Instala o Lovense Connect / Lovense Stream (o app oficial pra desktop). Liga o toy e pareia por Bluetooth pra que o app mostre conectado."),
            ("Liga o Lovense à sua plataforma cam",
             "No app Lovense conecta sua conta cam pra que o toy reaja aos tokens / tips dos espectadores. A maioria das grandes plataformas cam é suportada."),
            ("Adiciona o overlay Lovense no SplitCam",
             "A Lovense fornece uma URL de overlay / widget. Adiciona como camada <strong>Browser</strong> na sua cena SplitCam pra que os espectadores vejam o status do toy e os tips recentes na tela."),
            ("Monta a cena e Go Live",
             "Adiciona a câmera e os outros overlays, cola a chave RTMP da sua plataforma cam no SplitCam e clica <strong>Go Live</strong>. O toy reage aos tips em tempo real."),
        ],
        "tips": [
            ("Use o Lovense SplitCam Toolset oficial", "A Lovense publica um toolset específico pro SplitCam com guia de instalação próprio — ele adiciona o overlay de atividade do toy e alerts de tips feito pro SplitCam."),
            ("Atualize a Lovense Cam Extension", "O toolset precisa de uma Lovense Cam Extension recente (30.1.4 ou mais nova) — atualiza antes do live."),
            ("Mantém o toy carregado", "Bateria acabando no meio do show mata a parte interativa — carrega total antes de entrar ao vivo."),
            ("Testa a reação a tokens", "Manda um pequeno tip de teste pra confirmar que o toy reage antes de abrir a sala."),
            ("Confira os requisitos de versão", "O Lovense SplitCam Toolset precisa do SplitCam 10.4.5 ou mais novo. A Lovense Cam Extension cobre oficialmente Chaturbate, Stripchat, BongaCams, MyFreeCams e CamSoda — pra qualquer outro site, usa a integração Generic URL da Lovense."),
        ],
        "faq": [
            ("A Lovense suporta o SplitCam oficialmente?", "Sim — a Lovense documenta um «Lovense SplitCam Toolset» oficial com guia de instalação próprio, e o SplitCam traz um plugin Lovense oficial. A integração é suportada dos dois lados."),
            ("O toy conecta direto no SplitCam?", "Não — o toy pareia com o app Lovense; o SplitCam mostra o overlay Lovense e transmite sua câmera."),
            ("Quais sites cam suportam Lovense?", "A Cam Extension da Lovense suporta oficialmente Chaturbate, Stripchat, BongaCams, MyFreeCams e CamSoda, com suporte variável pra outros — confere a lista atual no app Lovense."),
            ("Posso mostrar tips recentes na tela?", "Sim — adiciona a URL do widget Lovense como camada Browser no SplitCam."),
        ],
    },
    {
        "slug": "multistream-cams", "name": "Vários sites cam",
        "title": "Transmitir em vários sites cam ao mesmo tempo com SplitCam",
        "desc": "Transmitir em MyFreeCams, Chaturbate, BongaCams, CAM4, Stripchat e mais ao mesmo tempo com a multidifusão grátis do SplitCam. Um clique, sem marca d'água.",
        "kw": "transmitir em vários sites cam, multistream cam sites, transmitir em chaturbate e bongacams ao mesmo tempo, software multidifusão cam",
        "h1html": 'Como transmitir em <span class="accent">vários sites cam</span> ao mesmo tempo',
        "h1short": "Multidifusão cam",
        "card": "Transmitir em vários sites cam ao mesmo tempo.",
        "intro": "O <strong style='color:var(--text)'>SplitCam</strong> grátis pode transmitir uma codificação pra <strong style='color:var(--text)'>vários sites cam ao mesmo tempo</strong> — MyFreeCams, Chaturbate, BongaCams, CAM4, Stripchat e mais. Sem marca d'água, um clique.",
        "quick": "Pra transmitir em vários sites cam de uma vez: instalar SplitCam, montar a cena, pegar a URL do servidor RTMP e a stream key de cada site cam, adicionar todas nas configurações de multidifusão do SplitCam, clicar Go Live uma vez."
                 "<ol><li>Instalar SplitCam.</li><li>Adicionar câmera + cena.</li>"
                 "<li>Pegar uma chave RTMP de cada site cam.</li>"
                 "<li>Adicionar todas as chaves na multidifusão do SplitCam.</li>"
                 "<li>Pressionar Go Live uma vez.</li></ol>",
        "steps": [
            ("Instala o SplitCam",
             "O SplitCam é um software de streaming grátis pra Windows e macOS com multidifusão embutida. Instala — sem marca d'água, sem cadastro."),
            ("Configura câmera e cena",
             "Abre o SplitCam, adiciona a webcam e monta a cena com overlays e filtros. Uma cena alimenta cada destino."),
            ("Pega uma chave RTMP de cada site cam",
             "Em cada plataforma cam ativa a transmissão externa / RTMP e copia a <strong>URL do servidor</strong> e a <strong>stream key</strong>. Repete pra cada site que você quer transmitir — vê os guias individuais pelas plataformas pra caminhos exatos."),
            ("Adiciona cada destino no SplitCam",
             "Abre <strong>Stream Settings</strong> e adiciona cada site cam como destino RTMP personalizado — cola URL do servidor e chave. Marca todos os que quer ao vivo."),
            ("Clica Go Live uma vez",
             "Aperta <strong>Go Live</strong>. O SplitCam envia seu stream pra cada site cam selecionado simultaneamente, peer-to-peer, de uma codificação única — sem taxa extra."),
        ],
        "tips": [
            ("Olho no seu upload", "A multidifusão multiplica a carga de upload. Cada destino consome seu próprio bitrate — garanta que sua conexão aguenta a soma."),
            ("Confira as regras de cada plataforma", "Alguns sites cam proíbem transmissão simultânea em outro lugar — confirma antes de multidifundir."),
            ("Cabo — aqui não dá pra ter queda", "A multidifusão multiplica a carga de upload, então uma única queda de Wi-Fi pode travar todos os destinos de uma vez. Cabo aqui não é opcional."),
            ("Acompanha o monitor de saúde", "O SplitCam mostra o status por destino — derruba um site se seu upload não aguentar."),
        ],
        "faq": [
            ("A multidifusão no SplitCam é grátis?", "Sim — a multidifusão é embutida e grátis, sem taxa por destino, sem marca d'água."),
            ("Pra quantos sites cam posso transmitir ao mesmo tempo?", "Tantos quanto sua banda de upload aguentar — cada destino consome seu próprio bitrate."),
            ("Usa relay em nuvem?", "Não — o SplitCam envia os streams em peer-to-peer direto do seu PC pro servidor de ingest de cada plataforma."),
            ("A multidifusão deixa meu PC lento?", "A codificação é feita uma vez e reutilizada; codificação por hardware mantém a carga de CPU baixa. A banda de upload é o limite real."),
        ],
    },
]
