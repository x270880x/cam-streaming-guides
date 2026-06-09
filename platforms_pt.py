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
        "kw": "como transmitir no chaturbate, chaturbate, chaturbate broadcast token, chaturbate obs, chaturbate external encoder, chaturbate rtmp, chaturbate stream key",
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
        "kw": "como transmitir no cam4, cam4, cam4 broadcast, cam4 obs, cam4 external encoder, cam4 rtmp, cam4 stream key",
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
        "kw": "como transmitir no bongacams, bongacams, bongacams broadcast, bongacams obs, bongacams external encoder, bongacams rtmp, bongacams stream key",
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
        "kw": "como transmitir no stripchat, stripchat, stripchat broadcast, stripchat obs, stripchat external software, stripchat rtmp, stripchat stream key",
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
        "title": "Ficar ao vivo no OnlyFans com SplitCam",
        "desc": "Fique ao vivo no OnlyFans com SplitCam grátis — login por autorização ou OBS Key, cenas multicâmera e overlays. Sem marca d'água, sem cadastro.",
        "kw": "como ficar ao vivo no onlyfans, onlyfans, onlyfans live, onlyfans obs key, onlyfans broadcast, onlyfans stream key, onlyfans software streaming",
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
        "kw": "como transmitir no camplace, camplace, camplace broadcast, camplace obs, camplace external encoder, camplace rtmp, camplace stream key",
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
        "kw": "como transmitir no camsoda, camsoda, camsoda broadcast, camsoda obs broadcaster, camsoda external encoder, camsoda rtmp, camsoda stream key",
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
        "kw": "como transmitir no streamate, streamate, streamate broadcast, streamate sm connect, streamate obs, streamate rtmp, streamate stream key",
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
        "kw": "como transmitir no streamray, streamray, streamray broadcast, streamray obs broadcaster, streamray external encoder, streamray rtmp",
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
        "kw": "como transmitir no xlovecam, xlovecam, xlovecam broadcast, xlovecam obs, xlovecam external encoder, xlovecam rtmp, xlovecam stream key",
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
        "kw": "como transmitir no soulcams, soulcams, soulcams broadcast, soulcams obs, soulcams external encoder, soulcams rtmp, soulcams stream key",
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
        "kw": "como transmitir no imlive, imlive, imlive virtual camera, imlive câmera virtual, imlive webcam, imlive splitcam, im live cam",
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
        "kw": "como transmitir no vxlive, vxlive, vxlive broadcast, vxlive obs, vxlive rtmp, vxlive stream key, visit-x, vxmodels splitcam",
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
        "kw": "como transmitir no virtwish, virtwish, virtwish broadcast, virtwish obs, virtwish external encoder, virtwish rtmp, virtwish stream key",
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
        "kw": "como transmitir no xmodels, xmodels, xmodels broadcast, xmodels obs, xmodels external encoder, xmodels rtmp, xmodels stream key",
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
        "kw": "como transmitir no flirt4free, flirt4free, flirt4free broadcast, flirt4free obs, flirt4free external broadcast, flirt4free rtmp, flirt for free cam",
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
        "kw": "como adicionar mfc alerts, mfc alerts, myfreecams, myfreecams alerts, mfc tip alerts, mfcalerts splitcam, mfc alerts overlay",
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
        "kw": "como adicionar lovense ao stream, lovense, lovense splitcam, lovense splitcam toolset, lovense toy interativo, lovense cam, lovense overlay",
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
        "kw": "como transmitir em vários sites cam, multistream cam, transmitir em chaturbate e bongacams ao mesmo tempo, software multidifusão cam, multidifusão cam sites, multistream cam sites",
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
    {
        "slug": "livejasmin", "name": "LiveJasmin",
        "title": "Como transmitir no LiveJasmin com SplitCam",
        "desc": "Transmita no LiveJasmin com SplitCam grátis — encoder externo do Model Center, setup HD 1080p, cenas multicâmera e overlays. Sem marca d'água.",
        "kw": "como transmitir no livejasmin, livejasmin, livejasmin broadcast, livejasmin obs, livejasmin external encoder, livejasmin rtmp, livejasmin stream key",
        "h1html": 'Como transmitir no <span class="accent">LiveJasmin</span> com SplitCam',
        "h1short": "Transmitir no LiveJasmin",
        "card": "Setup de encoder externo pro Model Center HD-only do LiveJasmin.",
        "intro": "O LiveJasmin é o carro-chefe da Docler Holding — uma das maiores redes cam do mundo e uma plataforma só em HD. O transmissor preferido dela é o cliente proprietário <strong>JasminCAM</strong>, mas o Model Center também expõe um caminho padrão <strong>External Encoder</strong> ao qual o <strong style='color:var(--text)'>SplitCam</strong> grátis conecta — pra você transmitir com cenas multicâmera, filtros de beleza e overlays no mesmo stream HD.",
        "quick": "Pra transmitir no LiveJasmin com SplitCam: instala o SplitCam, monta a cena HD, no Model Center vai em <em>Settings → Broadcast → External Encoder</em>, copia a URL do servidor e a stream key, cola no SplitCam e dá Go Live."
                 "<ol><li>Instala o SplitCam.</li><li>Adiciona câmera + cena HD.</li>"
                 "<li>Pega URL e stream key no Model Center.</li>"
                 "<li>Cola no SplitCam.</li>"
                 "<li>Aperta Go Live.</li></ol>",
        "key_how": "Entra em <strong>modelcenter.livejasmin.com</strong>, abre <strong>Settings → Broadcast → External Encoder</strong>. O Model Center mostra uma <strong>URL do servidor</strong> e uma <strong>stream key</strong> vinculadas à sua conta — copia as duas pros campos de RTMP personalizado do SplitCam. <strong>Aviso:</strong> contas novas precisam ser aprovadas (48–72 horas) antes da opção de encoder externo aparecer, e a plataforma exige saída só em HD.",
        "tips": [
            ("HD ou cai no ranking", "LiveJasmin é só HD — abaixo de 1280×720 você corre risco de só aparecer nas listas de paga baixa, abaixo de 1080p perde a elegibilidade 'Premium'. Mira em 1920×1080 a 30 fps, 4.000–6.000 Kbps."),
            ("JasminCAM vs encoder externo", "O JasminCAM, cliente oficial da Docler, dá a conformidade HD mais limpa, mas os encoders externos (OBS, SplitCam, vMix) são oficialmente suportados depois que sua conta é aprovada — e liberam cenas multicâmera e overlays que o JasminCAM não faz."),
            ("Free chat ≠ show privado", "O Free chat é só preview — sem nudez. O dinheiro tá nos privados e nos Gold shows. Pensa a cena pra ficar forte vestida E em modo show."),
            _T_ETH,
        ],
        "faq": [
            ("O LiveJasmin suporta oficialmente encoders externos tipo o SplitCam?", "Suporta — o Model Center tem a opção External Encoder em Settings → Broadcast. O JasminCAM é o cliente recomendado, mas OBS, SplitCam e os outros encoders RTMP estão listados explicitamente como suportados assim que sua conta de modelo é aprovada."),
            ("Onde pego minha stream key do LiveJasmin?", "Dentro do Model Center: Settings → Broadcast → External Encoder. A URL do servidor e a stream key única aparecem ali — copia as duas pros campos de RTMP personalizado do SplitCam. A chave é vinculada à conta; trata como senha."),
            ("Que bitrate usar no LiveJasmin?", "LiveJasmin é só HD — mira em 1920×1080 a 30 fps, 4.000–6.000 Kbps com keyframe a cada 2 segundos. Abaixo disso você perde o selo Premium e cai no ranking."),
            ("O SplitCam é grátis pra usar com o LiveJasmin?", "É — o SplitCam é grátis, sem marca d'água e sem limite de tempo. O único 'custo' é bater os requisitos HD do LiveJasmin, coisa que o SplitCam faz nativo com a composição de cena 1080p e os filtros de beleza."),
        ],
        "steps": [
            ("Baixa e instala o SplitCam",
             "O SplitCam é um software de live streaming grátis pra Windows e macOS — sem cadastro, sem cartão, sem marca d'água. É o encoder que manda seu vídeo HD pro LiveJasmin."),
            ("Monta sua cena HD",
             "Abre o SplitCam e adiciona sua webcam no modo 1080p. Encaixa overlays, texto, uma segunda câmera ou o celular, filtros de beleza ou fundo IA — o LiveJasmin exige qualidade HD e sua cena composta tem que parecer premium tanto no Free chat QUANTO em privado."),
            ("Pega a URL e a stream key do LiveJasmin",
             "Entra em <strong>modelcenter.livejasmin.com</strong> (a conta precisa ser aprovada antes — normalmente 48–72 horas depois do cadastro). Abre <strong>Settings → Broadcast → External Encoder</strong>. A página mostra uma <strong>URL do servidor</strong> e uma <strong>stream key</strong> única. Copia as duas."),
            ("Conecta o SplitCam ao LiveJasmin",
             "No SplitCam abre <strong>Stream Settings</strong>, cola a URL do servidor do LiveJasmin e a stream key nos campos de RTMP personalizado. Põe o bitrate em 4.000–6.000 Kbps a 1920×1080, 30 fps, com keyframe de 2 segundos. Roda primeiro o speed test embutido — stream HD pesa."),
            ("Clica Go Live",
             "Aperta <strong>Go Live</strong> no SplitCam e depois fica online no Model Center do LiveJasmin. Em uns 10 segundos seu feed HD chega na rede do LiveJasmin. As próximas transmissões são um clique — abre o SplitCam, Go Live, depois fica online no LiveJasmin."),
        ],
    },
    {
        "slug": "myfreecams", "name": "MyFreeCams",
        "title": "Como transmitir no MyFreeCams com SplitCam",
        "desc": "Transmita no MyFreeCams com SplitCam grátis — broadcaster externo do Model Admin, cenas multicâmera e overlays no stream por tokens. Sem marca d'água.",
        "kw": "como transmitir no myfreecams, myfreecams, mfc broadcast, myfreecams obs, mfc external encoder, mfc rtmp, mfc stream key",
        "h1html": 'Como transmitir no <span class="accent">MyFreeCams</span> com SplitCam',
        "h1short": "Transmitir no MyFreeCams",
        "card": "Setup de broadcaster externo pro Model Admin baseado em tokens do MFC.",
        "intro": "O MyFreeCams (MFC) é uma das plataformas cam mais antigas — economia 100 % token, sem maratona de aprovação de modelo, e uma base fiel de membros Premium. O <em>Model Web Broadcaster</em> padrão é uma ferramenta de navegador de câmera única, mas o Model Admin também expõe uma opção <strong>External Broadcaster</strong> à qual o <strong style='color:var(--text)'>SplitCam</strong> grátis conecta — destravando cenas multicâmera, overlays e filtros no mesmo stream monetizado por tokens.",
        "quick": "Pra transmitir no MyFreeCams com SplitCam: instala o SplitCam, monta sua cena, em <em>Model Admin → Broadcaster</em> troca o Web Broadcaster pelo External Broadcaster, copia a URL do servidor e a stream key, cola no SplitCam e dá Go Live."
                 "<ol><li>Instala o SplitCam.</li><li>Adiciona câmera + cena.</li>"
                 "<li>Pega URL e stream key no Model Admin.</li>"
                 "<li>Cola no SplitCam.</li>"
                 "<li>Aperta Go Live.</li></ol>",
        "key_how": "Entra no MyFreeCams, abre <strong>Model Admin → Broadcaster</strong> e troca de <em>Web Broadcaster</em> pro <strong>External Broadcaster</strong>. A página mostra uma <strong>URL do servidor</strong> (rtmp://publish.myfreecams.com…) e uma <strong>stream key</strong> vinculadas à sua conta de modelo — copia as duas pros campos de RTMP personalizado do SplitCam. A chave é vinculada à conta; trata como senha e reseta se vazar.",
        "tips": [
            ("Token MFC, não assinatura", "MFC é economia pura de gorjetas/tokens — os membros Premium podem entrar em privado, mas o grosso da grana sai das gorjetas do free chat. Pensa uma cena que renda vestida e casual, não só em show pelado."),
            ("Web Broadcaster vs External — escolhe uma vez", "O Web Broadcaster padrão é câmera única, fonte única. O External Broadcaster libera multi-cena, overlays e filtros de beleza via SplitCam/OBS. Troca em Model Admin → Broadcaster antes de entrar no ar."),
            ("Integração com MFC Alerts", "Os alertas animados de gorjeta na tela saem do mfcalerts.com — adiciona a URL do alerta como camada Browser no SplitCam, em cima da câmera. Vê nosso guia do MFC Alerts pro setup completo do overlay."),
            _T_ETH,
        ],
        "faq": [
            ("O MyFreeCams suporta oficialmente broadcasters externos tipo o SplitCam?", "Suporta — o Model Admin tem uma opção External Broadcaster que expõe URL de servidor RTMP padrão e stream key. OBS, SplitCam, vMix e os outros encoders RTMP funcionam; o MFC suporta explicitamente a opção na documentação pra modelos."),
            ("Onde pego minha stream key do MFC?", "Model Admin → Broadcaster → troca pro External Broadcaster. A URL do servidor (rtmp://publish.myfreecams.com…) e a stream key aparecem ali. Copia as duas pros campos de RTMP personalizado do SplitCam."),
            ("Que bitrate usar no MyFreeCams?", "MFC aceita até ~6.000 Kbps com intervalo de keyframe de 2 segundos. Manda 1920×1080 a 30 fps, 3.500–6.000 Kbps — seu upload é o limite real. Roda primeiro o speed test do SplitCam."),
            ("O SplitCam é grátis pra usar com o MyFreeCams?", "É — o SplitCam é grátis, sem marca d'água e sem limite de tempo. A própria opção External Broadcaster é grátis dentro do Model Admin. Custo total de broadcaster: zero."),
        ],
        "steps": [
            ("Baixa e instala o SplitCam",
             "O SplitCam é um software de live streaming grátis pra Windows e macOS — sem cadastro, sem cartão, sem marca d'água. É o encoder que manda seu vídeo pro MyFreeCams."),
            ("Monta sua cena",
             "Abre o SplitCam e adiciona sua webcam. Encaixa overlays, texto, uma segunda câmera ou o celular, filtros de beleza ou fundo IA — tudo aplicado ao vivo antes do stream sair do seu PC. Considera adicionar a URL do mfcalerts.com como camada Browser pros alertas animados de gorjeta."),
            ("Troca pro External Broadcaster no Model Admin",
             "Entra no MyFreeCams. Abre <strong>Model Admin → Broadcaster</strong>. Troca de <em>Web Broadcaster</em> pro <strong>External Broadcaster</strong>. A página mostra uma <strong>URL do servidor</strong> e uma <strong>stream key</strong> única. Copia as duas."),
            ("Conecta o SplitCam ao MyFreeCams",
             "No SplitCam abre <strong>Stream Settings</strong>, cola a URL do servidor do MFC e a stream key nos campos de RTMP personalizado. Põe o bitrate em 3.500–6.000 Kbps a 1920×1080, 30 fps, com keyframe de 2 segundos. Roda primeiro o speed test embutido."),
            ("Clica Go Live",
             "Aperta <strong>Go Live</strong> no SplitCam. Em uns 10 segundos seu stream chega no MyFreeCams. As próximas transmissões são um clique — abre o SplitCam, Go Live."),
        ],
    },
    {
        "slug": "cherry-tv", "name": "Cherry.tv",
        "title": "Como transmitir no Cherry.tv com SplitCam",
        "desc": "Transmita no Cherry.tv com SplitCam grátis — encoder externo do Streamer Dashboard, chave RTMP, cenas multicâmera e overlays. Sem marca d'água.",
        "kw": "como transmitir no cherry.tv, cherry.tv, cherry tv broadcast, cherry.tv obs, cherry tv external encoder, cherry.tv rtmp, cherry.tv stream key",
        "h1html": 'Como transmitir no <span class="accent">Cherry.tv</span> com SplitCam',
        "h1short": "Transmitir no Cherry.tv",
        "card": "Setup de encoder externo pro Streamer Dashboard do Cherry.tv.",
        "intro": "O Cherry.tv é uma plataforma cam mais nova, em rápido crescimento, com pegada Web3 — pagamentos cripto-friendly e barreira de entrada menor que as redes legacy tipo LiveJasmin. O broadcaster padrão é por navegador, mas o <strong>Streamer Dashboard</strong> também expõe um caminho padrão <strong>External Encoder</strong> ao qual o <strong style='color:var(--text)'>SplitCam</strong> grátis conecta — deixando você transmitir com cenas multicâmera, overlays e filtros.",
        "quick": "Pra transmitir no Cherry.tv com SplitCam: instala o SplitCam, monta sua cena, no Streamer Dashboard abre <em>Broadcast Settings → External Encoder</em>, copia a URL do servidor e a stream key, cola no SplitCam e dá Go Live."
                 "<ol><li>Instala o SplitCam.</li><li>Adiciona câmera + cena.</li>"
                 "<li>Pega URL e stream key no Streamer Dashboard.</li>"
                 "<li>Cola no SplitCam.</li>"
                 "<li>Aperta Go Live.</li></ol>",
        "key_how": "Entra na sua conta de streamer do Cherry.tv, abre o <strong>Streamer Dashboard</strong> e vai em <strong>Broadcast Settings → External Encoder</strong>. A página mostra uma <strong>URL do servidor</strong> e uma <strong>stream key</strong> vinculadas à sua conta — copia as duas pros campos de RTMP personalizado do SplitCam. Contas novas de streamer precisam passar por uma verificação básica (geralmente rápida — o Cherry.tv tem onboarding mais leve que as redes cam legacy) antes da opção de encoder externo ficar totalmente ativa.",
        "tips": [
            ("Entrada mais leve, tráfego subindo", "O onboarding do Cherry.tv é mais rápido que o das plataformas legacy (sem revisão Docler de 72 horas). Junto com o tráfego em crescimento, é um bom ponto early-mover pra montar uma base de seguidores antes da concorrência apertar."),
            ("Saque em cripto disponível", "O Cherry.tv suporta saque em cripto além do fiat padrão — útil se você tá numa região onde os pagamentos das redes cam tradicionais são lentos ou restritos."),
            ("Browser broadcaster vs externo", "O broadcaster por navegador é prático mas é fonte única. O SplitCam via External Encoder libera cenas multicâmera, overlays, filtros de beleza e fundo IA que a ferramenta de navegador não faz."),
            _T_ETH,
        ],
        "faq": [
            ("O Cherry.tv suporta oficialmente encoders externos tipo o SplitCam?", "Suporta — o Streamer Dashboard inclui External Encoder dentro de Broadcast Settings. A plataforma fornece uma URL de servidor RTMP padrão e uma stream key; OBS, SplitCam e os outros encoders RTMP conectam normal."),
            ("Onde pego minha stream key do Cherry.tv?", "Streamer Dashboard → Broadcast Settings → External Encoder. A URL do servidor e a stream key aparecem ali — copia as duas pros campos de RTMP personalizado do SplitCam. A chave é vinculada à conta; trata como senha."),
            ("Que bitrate usar no Cherry.tv?", "O Cherry.tv aceita as configurações cam-quality padrão — manda 1920×1080 a 30 fps, 3.500–6.000 Kbps com keyframe de 2 segundos. Roda primeiro o speed test embutido do SplitCam."),
            ("O SplitCam é grátis pra usar com o Cherry.tv?", "É — o SplitCam é grátis, sem marca d'água e sem limite de tempo. A opção de encoder externo do Cherry.tv é grátis pra ativar. Custo total de broadcaster: zero."),
        ],
        "steps": [
            ("Baixa e instala o SplitCam",
             "O SplitCam é um software de live streaming grátis pra Windows e macOS — sem cadastro, sem cartão, sem marca d'água. É o encoder que manda seu vídeo pro Cherry.tv."),
            ("Monta sua cena",
             "Abre o SplitCam e adiciona sua webcam. Encaixa overlays, texto, uma segunda câmera ou o celular, filtros de beleza ou fundo IA — tudo aplicado ao vivo. O público do Cherry.tv é mais jovem e mais antenado em plataforma, então uma cena caprichada ajuda a se destacar."),
            ("Pega a URL e a stream key do Cherry.tv",
             "Entra na sua conta de streamer do Cherry.tv, abre o <strong>Streamer Dashboard</strong> e vai em <strong>Broadcast Settings → External Encoder</strong>. A página mostra uma <strong>URL do servidor</strong> e uma <strong>stream key</strong> única. Copia as duas."),
            ("Conecta o SplitCam ao Cherry.tv",
             "No SplitCam abre <strong>Stream Settings</strong>, cola a URL do servidor do Cherry.tv e a stream key nos campos de RTMP personalizado. Põe o bitrate em 3.500–6.000 Kbps a 1920×1080, 30 fps, com keyframe de 2 segundos. Roda primeiro o speed test embutido."),
            ("Clica Go Live",
             "Aperta <strong>Go Live</strong> no SplitCam e depois fica online pelo Streamer Dashboard no Cherry.tv. Em uns 10 segundos seu stream chega no Cherry.tv. As próximas transmissões são um clique — abre o SplitCam, Go Live, depois fica online no Cherry.tv."),
        ],
    },
    {
        "slug": "amateurtv", "name": "AmateurTV",
        "title": "Como transmitir no AmateurTV com SplitCam",
        "desc": "Transmita no AmateurTV com SplitCam grátis — encoder externo do Model Panel, chave RTMP, cenas multicâmera e overlays. Sem marca d'água, sem cadastro.",
        "kw": "como transmitir no amateurtv, amateurtv, amateurtv broadcast, amateurtv obs, amateurtv external encoder, amateurtv rtmp, amateurtv stream key",
        "h1html": 'Como transmitir no <span class="accent">AmateurTV</span> com SplitCam',
        "h1short": "Transmitir no AmateurTV",
        "card": "Setup do encoder externo para a rede em espanhol do AmateurTV.",
        "intro": "O AmateurTV é a rede cam em espanhol mais forte — tráfego pesado na Espanha, México, Argentina e em toda a LatAm. O broadcaster padrão do Model Panel funciona por navegador, mas também expõe um caminho padrão <strong>External Encoder</strong> ao qual o <strong style='color:var(--text)'>SplitCam</strong> grátis conecta — pra você transmitir com cenas multicâmera, filtros de beleza e overlays pra um público hispano que as redes US-centric não atendem direito.",
        "quick": "Pra transmitir no AmateurTV com SplitCam: instala o SplitCam, monta sua cena, no Model Panel abre <em>Broadcast Settings → External Encoder</em>, copia a URL do servidor e a stream key, cola no SplitCam e dá Go Live."
                 "<ol><li>Instala o SplitCam.</li><li>Adiciona câmera + cena.</li>"
                 "<li>Pega URL e stream key no Model Panel.</li>"
                 "<li>Cola no SplitCam.</li>"
                 "<li>Aperta Go Live.</li></ol>",
        "key_how": "Entra na sua conta de modelo do AmateurTV, abre o <strong>Model Panel</strong> e vai em <strong>Broadcast Settings → External Encoder</strong>. A página mostra uma <strong>URL do servidor</strong> e uma <strong>stream key</strong> vinculadas à sua conta — copia as duas pros campos de RTMP personalizado do SplitCam. Contas novas precisam de verificação de ID antes de entrar no ar.",
        "tips": [
            ("Público hispano em primeiro lugar", "O tráfego do AmateurTV é majoritariamente em espanhol — Espanha de dia, LatAm no horário de noite dos EUA. Títulos de sala, texto e overlays em espanhol rendem muito mais que inglês puro. Vale a pena soltar um espanhol básico na sala mesmo se você fala português."),
            ("O fuso da LatAm é seu prime time", "O pico de tráfego coincide com a noite na LatAm (UTC-3 a UTC-6). Pra modelo brasileira, é praticamente o mesmo horário — vantagem natural pra quem transmite à noite no Brasil."),
            ("Payouts mid-tier estáveis", "Não é o RPM mais alto do mercado, mas o AmateurTV paga em dia, e o nicho hispano tem bem menos concorrência que as redes top americanas."),
            _T_ETH,
        ],
        "faq": [
            ("O AmateurTV suporta oficialmente encoders externos tipo o SplitCam?", "Suporta — o Model Panel tem a opção External Encoder em Broadcast Settings. O AmateurTV fornece uma URL de servidor RTMP padrão e uma stream key; OBS, SplitCam, vMix e os outros encoders RTMP conectam."),
            ("Onde pego minha stream key do AmateurTV?", "Model Panel → Broadcast Settings → External Encoder. A URL do servidor e a stream key aparecem ali. Copia as duas pros campos de RTMP personalizado do SplitCam. A chave é vinculada à conta."),
            ("Que bitrate usar no AmateurTV?", "Configurações cam-quality padrão — manda 1920×1080 a 30 fps, 3.500–6.000 Kbps com keyframe de 2 segundos. Roda primeiro o speed test embutido do SplitCam."),
            ("O SplitCam é grátis pra usar com o AmateurTV?", "É — o SplitCam é grátis, sem marca d'água e sem limite de tempo. A opção de encoder externo do AmateurTV é grátis pra ativar."),
        ],
        "steps": [
            ("Baixa e instala o SplitCam",
             "O SplitCam é um software de live streaming grátis pra Windows e macOS — sem cadastro, sem cartão, sem marca d'água. É o encoder que manda seu vídeo pro AmateurTV."),
            ("Monta sua cena",
             "Abre o SplitCam e adiciona sua webcam. Encaixa overlays, texto, uma segunda câmera ou o celular, filtros de beleza ou fundo IA. Põe os textos de overlay em espanhol — o público hispano do AmateurTV percebe e converte melhor."),
            ("Pega a URL e a stream key do AmateurTV",
             "Entra na sua conta de modelo do AmateurTV, abre o <strong>Model Panel</strong> e vai em <strong>Broadcast Settings → External Encoder</strong>. A página mostra uma <strong>URL do servidor</strong> e uma <strong>stream key</strong> única. Copia as duas."),
            ("Conecta o SplitCam ao AmateurTV",
             "No SplitCam abre <strong>Stream Settings</strong>, cola a URL do servidor do AmateurTV e a stream key nos campos de RTMP personalizado. Põe o bitrate em 3.500–6.000 Kbps a 1920×1080, 30 fps, com keyframe de 2 segundos. Roda primeiro o speed test embutido."),
            ("Clica Go Live",
             "Aperta <strong>Go Live</strong> no SplitCam e depois fica online pelo Model Panel do AmateurTV. Em uns 10 segundos seu stream chega na rede. As próximas transmissões são um clique — abre o SplitCam, Go Live."),
        ],
    },
    {
        "slug": "camster", "name": "Camster",
        "title": "Como transmitir no Camster com SplitCam",
        "desc": "Transmita no Camster com SplitCam grátis — encoder externo do Model Hub, chave RTMP, cenas multicâmera e overlays. Sem marca d'água, sem cadastro.",
        "kw": "como transmitir no camster, camster, camster broadcast, camster obs, camster external encoder, camster rtmp, camster stream key",
        "h1html": 'Como transmitir no <span class="accent">Camster</span> com SplitCam',
        "h1short": "Transmitir no Camster",
        "card": "Setup do encoder externo pro Model Hub do Camster.",
        "intro": "O Camster é uma plataforma cam mid-tier consolidada — menor que Chaturbate ou LiveJasmin, mas com uma base de usuários fiel e payouts justos. O broadcaster padrão do Model Hub funciona por navegador, mas também expõe um caminho padrão <strong>External Encoder</strong> ao qual o <strong style='color:var(--text)'>SplitCam</strong> grátis conecta — pra você transmitir com cenas multicâmera, overlays e filtros que o broadcaster nativo não entrega.",
        "quick": "Pra transmitir no Camster com SplitCam: instala o SplitCam, monta sua cena, no Model Hub abre <em>Broadcast Settings → External Encoder</em>, copia a URL do servidor e a stream key, cola no SplitCam e dá Go Live."
                 "<ol><li>Instala o SplitCam.</li><li>Adiciona câmera + cena.</li>"
                 "<li>Pega URL e stream key no Model Hub.</li>"
                 "<li>Cola no SplitCam.</li>"
                 "<li>Aperta Go Live.</li></ol>",
        "key_how": "Entra na sua conta de modelo do Camster, abre o <strong>Model Hub</strong> e vai em <strong>Broadcast Settings → External Encoder</strong>. A página mostra uma <strong>URL do servidor</strong> e uma <strong>stream key</strong> vinculadas à sua conta — copia as duas pros campos de RTMP personalizado do SplitCam. A chave é vinculada à conta; trata como senha.",
        "tips": [
            ("Mid-tier = menos concorrência", "O Camster tem tráfego estável, mas bem menos broadcasters que as redes top — é mais fácil aparecer na home com uma cena caprichada e um horário fixo."),
            ("Broadcaster por navegador vs externo", "O broadcaster por navegador é de fonte única. O SplitCam via External Encoder libera cenas multicâmera, overlays, filtros de beleza e fundo IA."),
            ("Payouts estáveis, split justo", "O split do Camster é justo pro mid-tier — não é o mais alto do mercado, mas os pagamentos mensais chegam em dia e quase não tem reclamação de atraso."),
            _T_ETH,
        ],
        "faq": [
            ("O Camster suporta oficialmente encoders externos tipo o SplitCam?", "Suporta — o Model Hub tem a opção External Encoder em Broadcast Settings. URL de servidor RTMP padrão e stream key; OBS, SplitCam e os outros encoders RTMP conectam."),
            ("Onde pego minha stream key do Camster?", "Model Hub → Broadcast Settings → External Encoder. A URL do servidor e a stream key aparecem ali. Copia as duas pros campos de RTMP personalizado do SplitCam."),
            ("Que bitrate usar no Camster?", "Configurações cam-quality padrão — manda 1920×1080 a 30 fps, 3.500–6.000 Kbps com keyframe de 2 segundos. Roda primeiro o speed test embutido do SplitCam."),
            ("O SplitCam é grátis pra usar com o Camster?", "É — o SplitCam é grátis, sem marca d'água e sem limite de tempo. A opção de encoder externo do Camster é grátis."),
        ],
        "steps": [
            ("Baixa e instala o SplitCam",
             "O SplitCam é um software de live streaming grátis pra Windows e macOS — sem cadastro, sem cartão, sem marca d'água."),
            ("Monta sua cena",
             "Abre o SplitCam e adiciona sua webcam. Encaixa overlays, texto, uma segunda câmera ou o celular, filtros de beleza ou fundo IA — tudo aplicado ao vivo."),
            ("Pega a URL e a stream key do Camster",
             "Entra na sua conta de modelo do Camster, abre o <strong>Model Hub</strong> e vai em <strong>Broadcast Settings → External Encoder</strong>. A página mostra uma <strong>URL do servidor</strong> e uma <strong>stream key</strong> única. Copia as duas."),
            ("Conecta o SplitCam ao Camster",
             "No SplitCam abre <strong>Stream Settings</strong>, cola a URL do servidor do Camster e a stream key nos campos de RTMP personalizado. Põe o bitrate em 3.500–6.000 Kbps a 1920×1080, 30 fps, com keyframe de 2 segundos. Roda primeiro o speed test embutido."),
            ("Clica Go Live",
             "Aperta <strong>Go Live</strong> no SplitCam e depois fica online pelo Model Hub. Em uns 10 segundos seu stream chega no Camster."),
        ],
    },
    {
        "slug": "camversity", "name": "Camversity",
        "title": "Como transmitir no Camversity com SplitCam",
        "desc": "Transmita no Camversity com SplitCam grátis — encoder externo do Performer Dashboard, chave RTMP, cenas multicâmera e overlays. Sem marca d'água.",
        "kw": "como transmitir no camversity, camversity, camversity broadcast, camversity obs, camversity external encoder, camversity rtmp, camversity stream key",
        "h1html": 'Como transmitir no <span class="accent">Camversity</span> com SplitCam',
        "h1short": "Transmitir no Camversity",
        "card": "Setup do encoder externo pro Performer Dashboard do Camversity.",
        "intro": "O Camversity é uma plataforma cam independente em crescimento, com foco em ferramentas amigáveis pro performer e comissões mais baixas que as redes legacy. O broadcaster padrão do Performer Dashboard funciona por navegador, mas também expõe um caminho padrão <strong>External Encoder</strong> ao qual o <strong style='color:var(--text)'>SplitCam</strong> grátis conecta — pra você transmitir com cenas multicâmera, overlays e filtros.",
        "quick": "Pra transmitir no Camversity com SplitCam: instala o SplitCam, monta sua cena, no Performer Dashboard abre <em>Stream Settings → External Encoder</em>, copia a URL do servidor e a stream key, cola no SplitCam e dá Go Live."
                 "<ol><li>Instala o SplitCam.</li><li>Adiciona câmera + cena.</li>"
                 "<li>Pega URL e stream key no Performer Dashboard.</li>"
                 "<li>Cola no SplitCam.</li>"
                 "<li>Aperta Go Live.</li></ol>",
        "key_how": "Entra na sua conta de performer do Camversity, abre o <strong>Performer Dashboard</strong> e vai em <strong>Stream Settings → External Encoder</strong>. A página mostra uma <strong>URL do servidor</strong> e uma <strong>stream key</strong> vinculadas à sua conta — copia as duas pros campos de RTMP personalizado do SplitCam. Contas novas passam por uma verificação de ID padrão antes de entrar no ar.",
        "tips": [
            ("Split mais amigo do performer", "O split do Camversity favorece mais o performer que as redes legacy — vale comparar com sua plataforma principal se você tá no começo da carreira cam."),
            ("Onboarding mais leve que o da Docler", "A verificação do Camversity é mais rápida que as 48–72 horas do LiveJasmin, e mesmo assim é legítima (nada de modelo sem verificação). Bom meio-termo."),
            ("Monta cena, não só webcam", "O broadcaster padrão do Performer Dashboard é fonte única. O SplitCam via External Encoder libera multicâmera, overlays, filtros de beleza."),
            _T_ETH,
        ],
        "faq": [
            ("O Camversity suporta oficialmente encoders externos tipo o SplitCam?", "Suporta — o Performer Dashboard tem a opção External Encoder em Stream Settings. URL de servidor RTMP padrão e stream key; OBS, SplitCam, vMix conectam."),
            ("Onde pego minha stream key do Camversity?", "Performer Dashboard → Stream Settings → External Encoder. A URL do servidor e a stream key aparecem ali."),
            ("Que bitrate usar no Camversity?", "Manda 1920×1080 a 30 fps, 3.500–6.000 Kbps com keyframe de 2 segundos. Roda primeiro o speed test embutido do SplitCam."),
            ("O SplitCam é grátis pra usar com o Camversity?", "É — o SplitCam é grátis, sem marca d'água e sem limite de tempo. A opção de encoder externo do Camversity é grátis."),
        ],
        "steps": [
            ("Baixa e instala o SplitCam",
             "O SplitCam é um software de live streaming grátis pra Windows e macOS — sem cadastro, sem cartão, sem marca d'água."),
            ("Monta sua cena",
             "Abre o SplitCam e adiciona sua webcam. Encaixa overlays, texto, uma segunda câmera ou o celular, filtros de beleza ou fundo IA."),
            ("Pega a URL e a stream key do Camversity",
             "Entra na sua conta de performer do Camversity, abre o <strong>Performer Dashboard</strong> e vai em <strong>Stream Settings → External Encoder</strong>. A página mostra uma <strong>URL do servidor</strong> e uma <strong>stream key</strong> única. Copia as duas."),
            ("Conecta o SplitCam ao Camversity",
             "No SplitCam abre <strong>Stream Settings</strong>, cola a URL do servidor do Camversity e a stream key nos campos de RTMP personalizado. Põe o bitrate em 3.500–6.000 Kbps a 1920×1080, 30 fps, com keyframe de 2 segundos."),
            ("Clica Go Live",
             "Aperta <strong>Go Live</strong> no SplitCam e depois fica online pelo Performer Dashboard. Em uns 10 segundos seu stream chega no Camversity."),
        ],
    },
    {
        "slug": "skyprivate", "name": "SkyPrivate",
        "title": "Como usar o SkyPrivate com SplitCam",
        "desc": "Use o SkyPrivate com SplitCam grátis como câmera virtual — chamadas cam privadas via Skype, cenas multicâmera e filtros de beleza. Sem marca d'água.",
        "kw": "como usar o skyprivate, skyprivate, skyprivate virtual camera, skyprivate câmera virtual, skyprivate splitcam, skyprivate skype, skype cam privado",
        "h1html": 'Como usar o <span class="accent">SkyPrivate</span> com SplitCam',
        "h1short": "SplitCam no SkyPrivate",
        "card": "Setup de câmera virtual pras chamadas cam do SkyPrivate baseadas em Skype.",
        "intro": "O SkyPrivate é uma plataforma cam diferente — em vez de broadcast por RTMP, ela monetiza <strong>chamadas cam privadas pay-per-minute via Skype</strong>. O cliente reserva e paga por minuto no marketplace do SkyPrivate, e a videochamada em si roda no Skype. O <strong style='color:var(--text)'>SplitCam</strong> grátis entra como <strong>câmera virtual</strong>: monta sua cena no SplitCam e depois escolhe SplitCam como câmera dentro do Skype antes de atender uma chamada reservada via SkyPrivate.",
        "quick": "Pra usar o SkyPrivate com SplitCam: instala o SplitCam, monta sua cena, instala o Skype com o add-on do SkyPrivate, em <em>Video Settings</em> do Skype escolhe SplitCam como câmera e microfone, e atende as chamadas reservadas pelo SkyPrivate — o Skype entrega sua cena já montada pro cliente."
                 "<ol><li>Instala o SplitCam.</li><li>Monta a cena no SplitCam.</li>"
                 "<li>Instala Skype + add-on do SkyPrivate.</li>"
                 "<li>Escolhe SplitCam como câmera no Skype.</li>"
                 "<li>Atende as chamadas.</li></ol>",
        "key_how": "O SkyPrivate não usa RTMP nem stream key — usa o Skype como transporte de vídeo, com um add-on de cobrança por minuto. Instala o Skype, instala o add-on de navegador/desktop do SkyPrivate e depois no Skype abre <strong>Settings → Audio &amp; Video → Camera</strong> e escolhe <strong>SplitCam</strong> no lugar da sua webcam. A cena composta pelo SplitCam (overlays, multicâmera, filtros de beleza) é o que o cliente do SkyPrivate vê pelo Skype.",
        "tips": [
            ("Sem RTMP — fluxo de câmera virtual", "Não procura URL de servidor nem stream key. O SkyPrivate roda no Skype, e o Skype só vê o SplitCam como uma webcam. Monta a cena no SplitCam e depois escolhe SplitCam nas configurações de câmera do Skype."),
            ("Põe o SplitCam como microfone também", "No Audio do Skype escolhe SplitCam como microfone além de câmera — é assim que a redução de ruído, o áudio mixado e a música de intro chegam no cliente."),
            ("Faz uma chamada de teste no Skype", "Antes da sua primeira chamada paga no SkyPrivate, faz uma chamada de teste grátis no Skype (Echo / Sound Test Service) pra confirmar que o SplitCam é a câmera ativa e que a cena tá bem montada."),
            _T_TEST,
        ],
        "faq": [
            ("O SkyPrivate usa RTMP ou stream key?", "Nenhum dos dois. O SkyPrivate cuida da reserva e da cobrança; o vídeo em si vai pelo Skype. Não precisa de URL de servidor RTMP nem de stream key — basta configurar o SplitCam como câmera dentro do Skype."),
            ("Como seleciono o SplitCam no Skype pro SkyPrivate?", "Abre Skype Settings → Audio &amp; Video → Camera, escolhe SplitCam na lista. Faz o mesmo em Microphone. As chamadas do SkyPrivate chegam como chamadas normais do Skype com sua cena do SplitCam como feed da câmera."),
            ("Dá pra usar overlays e filtros de beleza com SkyPrivate?", "Dá — monta dentro da sua cena no SplitCam. O Skype só recebe o resultado composto como uma única câmera, então tudo que o SplitCam compõe (overlays, filtros de beleza, fundo IA, cenas multicâmera) aparece pro cliente do SkyPrivate."),
            ("O SplitCam é grátis pro SkyPrivate?", "É — o SplitCam é grátis, sem marca d'água e sem limite de tempo. Como câmera virtual pras chamadas SkyPrivate via Skype, ele não adiciona custo nem marca na chamada."),
        ],
        "steps": [
            ("Instala o SplitCam",
             "O SplitCam é grátis pra Windows e macOS — sem cadastro, sem cartão, sem marca d'água. Pro SkyPrivate ele funciona como <strong>câmera virtual</strong> que o Skype reconhece como uma webcam qualquer."),
            ("Monta sua cena no SplitCam",
             "Abre o SplitCam e usa <strong>Media Layers +</strong> pra adicionar sua webcam mais overlays, texto, filtros de beleza ou fundo IA. Essa cena composta é o que o Skype vai entregar pro cliente do SkyPrivate."),
            ("Instala o Skype e o add-on do SkyPrivate",
             "Instala o Skype no mesmo PC, faz login e depois instala o add-on / app desktop do SkyPrivate seguindo o onboarding do SkyPrivate. O add-on cuida da cobrança por minuto do lado do SkyPrivate."),
            ("Escolhe SplitCam como câmera e mic no Skype",
             "No Skype abre <strong>Settings → Audio &amp; Video</strong>. Põe <strong>Camera = SplitCam</strong> e <strong>Microphone = SplitCam</strong>. Faz uma chamada de teste rápida no Skype (Echo / Sound Test Service) pra confirmar que a cena tá indo bem em imagem e som."),
            ("Atende as chamadas do SkyPrivate",
             "Quando um cliente do SkyPrivate reservar uma chamada paga, ela chega como chamada do Skype — atende. Ele vê sua cena composta do SplitCam; o SkyPrivate cobra por minuto. Dá pra ajustar a cena no meio da chamada editando no SplitCam — o Skype atualiza na hora."),
        ],
    },
    {
        "slug": "manyvids", "name": "ManyVids",
        "title": "Ficar ao vivo no MV Live (ManyVids) com SplitCam",
        "desc": "Fique ao vivo no MV Live do ManyVids com SplitCam grátis — encoder externo do Creator Studio, chave RTMP, cenas multicâmera e overlays. Sem marca d'água.",
        "kw": "como ficar ao vivo no manyvids, manyvids, mv live, manyvids live, manyvids obs, mv live external encoder, manyvids stream key",
        "h1html": 'Como transmitir no <span class="accent">MV Live</span> com SplitCam',
        "h1short": "Transmitir no MV Live",
        "card": "Setup do encoder externo pro Creator Studio do MV Live (ManyVids).",
        "intro": "O ManyVids é uma plataforma de economia do criador — venda de clipes, vídeos personalizados, assinaturas de fã-clube e o produto ao vivo <strong>MV Live</strong>. O broadcaster padrão do Creator Studio funciona por navegador, mas também expõe um caminho padrão de <strong>External Encoder</strong> ao qual o <strong style='color:var(--text)'>SplitCam</strong> grátis conecta — pra você transmitir com cenas multicâmera, overlays e filtros na mesma plataforma criador-friendly.",
        "quick": "Pra transmitir no MV Live com SplitCam: instala o SplitCam, monta sua cena, no Creator Studio abre <em>MV Live → Broadcast Settings → External Encoder</em>, copia a URL do servidor e a stream key, cola no SplitCam e dá Go Live."
                 "<ol><li>Instala o SplitCam.</li><li>Adiciona câmera + cena.</li>"
                 "<li>Pega URL e stream key no Creator Studio.</li>"
                 "<li>Cola no SplitCam.</li>"
                 "<li>Aperta Go Live.</li></ol>",
        "key_how": "Entra na sua conta de criador do ManyVids, abre o <strong>Creator Studio</strong> e vai em <strong>MV Live → Broadcast Settings → External Encoder</strong>. A página mostra uma <strong>URL do servidor</strong> e uma <strong>stream key</strong> vinculadas à sua conta — copia as duas pros campos de RTMP personalizado do SplitCam. Contas de criador precisam estar totalmente verificadas (ID + dados fiscais) antes do MV Live ficar disponível.",
        "tips": [
            ("Economia do criador, não só ao vivo", "ManyVids não é uma plataforma cam pura — o MV Live é uma fonte de receita ao lado da venda de clipes, dos vídeos personalizados e das assinaturas de fã-clube. Usa as lives pra empurrar o público pras outras monetizações."),
            ("Tipping com tokens dentro do MV Live", "O MV Live tem o próprio sistema de tipping com tokens dentro da sala. Planeja menus de meta e gatilhos de recompensa estilo Chaturbate / Stripchat — convertem bem com o público que o ManyVids já tem."),
            ("Browser vs encoder externo", "O broadcaster embutido por navegador do Creator Studio é de câmera única. O SplitCam via External Encoder libera multicâmera, overlays e filtros."),
            _T_ETH,
        ],
        "faq": [
            ("O MV Live (ManyVids) suporta encoders externos tipo o SplitCam?", "Suporta — a seção do MV Live no Creator Studio tem a opção External Encoder em Broadcast Settings. URL de servidor RTMP padrão e stream key; OBS, SplitCam, vMix conectam."),
            ("Onde pego minha stream key do MV Live?", "Creator Studio → MV Live → Broadcast Settings → External Encoder. A URL do servidor e a stream key aparecem ali — copia as duas pros campos de RTMP personalizado do SplitCam."),
            ("Que bitrate usar no MV Live?", "Manda 1920×1080 a 30 fps, 3.500–6.000 Kbps com keyframe de 2 segundos. Roda primeiro o speed test embutido do SplitCam."),
            ("O SplitCam é grátis pra usar com o MV Live?", "É — o SplitCam é grátis, sem marca d'água e sem limite de tempo. A opção de encoder externo do ManyVids é grátis no Creator Studio."),
        ],
        "steps": [
            ("Baixa e instala o SplitCam",
             "O SplitCam é um software de live streaming grátis pra Windows e macOS — sem cadastro, sem cartão, sem marca d'água."),
            ("Monta sua cena",
             "Abre o SplitCam e adiciona sua webcam. Encaixa overlays, texto, uma segunda câmera ou o celular, filtros de beleza ou fundo IA — perfeito pros menus de meta e gatilhos de recompensa do MV Live."),
            ("Pega a URL e a stream key do MV Live",
             "Entra na sua conta de criador do ManyVids, abre o <strong>Creator Studio</strong> e vai em <strong>MV Live → Broadcast Settings → External Encoder</strong>. A página mostra uma <strong>URL do servidor</strong> e uma <strong>stream key</strong> única. Copia as duas."),
            ("Conecta o SplitCam ao MV Live",
             "No SplitCam abre <strong>Stream Settings</strong>, cola a URL do servidor do MV Live e a stream key nos campos de RTMP personalizado. Põe o bitrate em 3.500–6.000 Kbps a 1920×1080, 30 fps, com keyframe de 2 segundos."),
            ("Clica Go Live",
             "Aperta <strong>Go Live</strong> no SplitCam e depois inicia a transmissão do MV Live pelo Creator Studio. Em uns 10 segundos seu stream chega no público do MV Live."),
        ],
    },
    {
        "slug": "fansly", "name": "Fansly",
        "title": "Ficar ao vivo no Fansly Live com SplitCam",
        "desc": "Fique ao vivo no Fansly com SplitCam grátis — encoder externo do Creator Dashboard, chave RTMP, cenas multicâmera e filtros de beleza. Sem marca d'água.",
        "kw": "como ficar ao vivo no fansly, fansly, fansly live, fansly broadcast, fansly obs, fansly external encoder, fansly rtmp, fansly stream key",
        "h1html": 'Como transmitir no <span class="accent">Fansly Live</span> com SplitCam',
        "h1short": "Transmitir no Fansly",
        "card": "Setup do encoder externo pro Creator Dashboard do Fansly.",
        "intro": "O Fansly é um concorrente direto do OnlyFans, com regras de conteúdo mais soltas e uma base de criadores em crescimento — assinaturas, pay-per-view e o produto ao vivo <strong>Fansly Live</strong>. O broadcaster padrão funciona por navegador, mas o <strong>Creator Dashboard</strong> também expõe um caminho padrão de <strong>External Encoder</strong> ao qual o <strong style='color:var(--text)'>SplitCam</strong> grátis conecta — pra você transmitir com cenas multicâmera, overlays e filtros pra sua base de assinantes.",
        "quick": "Pra transmitir no Fansly Live com SplitCam: instala o SplitCam, monta sua cena, no Creator Dashboard abre <em>Live → Broadcast Settings → External Encoder</em>, copia a URL do servidor e a stream key, cola no SplitCam e dá Go Live."
                 "<ol><li>Instala o SplitCam.</li><li>Adiciona câmera + cena.</li>"
                 "<li>Pega URL e stream key no Creator Dashboard.</li>"
                 "<li>Cola no SplitCam.</li>"
                 "<li>Aperta Go Live.</li></ol>",
        "key_how": "Entra na sua conta de criador do Fansly, abre o <strong>Creator Dashboard</strong> e vai em <strong>Live → Broadcast Settings → External Encoder</strong>. A página mostra uma <strong>URL do servidor</strong> e uma <strong>stream key</strong> vinculadas à sua conta — copia as duas pros campos de RTMP personalizado do SplitCam. Contas de criador precisam passar pela verificação de ID antes do Fansly Live ser liberado.",
        "tips": [
            ("Público de assinante primeiro", "O público do Fansly é de assinatura — sua live chega em gente que já te paga todo mês. Planeja conteúdo que premia fidelidade (Q&amp;A exclusivo, bastidores, metas de gorjeta personalizadas) em vez de correr atrás de métrica de sala pública."),
            ("Gorjetas além da assinatura", "O Fansly Live aceita tipping na live além da assinatura base. Pra criador já estabelecido, a receita combinada pode passar do tipping puro das plataformas cam."),
            ("Broadcaster do navegador vs externo", "O broadcaster padrão do navegador é fonte única. O SplitCam via External Encoder libera multicâmera, overlays, filtros de beleza e fundo IA, no mesmo nível de acabamento do conteúdo pago pra assinante."),
            _T_ETH,
        ],
        "faq": [
            ("O Fansly Live suporta encoders externos tipo o SplitCam?", "Suporta — a seção Live do Creator Dashboard tem a opção External Encoder em Broadcast Settings. URL de servidor RTMP padrão e stream key; OBS, SplitCam, vMix conectam."),
            ("Onde pego minha stream key do Fansly?", "Creator Dashboard → Live → Broadcast Settings → External Encoder. A URL do servidor e a stream key aparecem ali. Copia as duas pros campos de RTMP personalizado do SplitCam."),
            ("Que bitrate usar no Fansly Live?", "Manda 1920×1080 a 30 fps, 3.500–6.000 Kbps com keyframe de 2 segundos. Roda primeiro o speed test embutido do SplitCam."),
            ("O SplitCam é grátis pra usar com o Fansly?", "É — o SplitCam é grátis, sem marca d'água e sem limite de tempo. A opção de encoder externo do Fansly é grátis no Creator Dashboard."),
        ],
        "steps": [
            ("Baixa e instala o SplitCam",
             "O SplitCam é um software de live streaming grátis pra Windows e macOS — sem cadastro, sem cartão, sem marca d'água."),
            ("Monta sua cena",
             "Abre o SplitCam e adiciona sua webcam. Encaixa overlays, texto, uma segunda câmera ou o celular, filtros de beleza ou fundo IA — uma cena caprichada combina com a expectativa premium dos seus assinantes pagantes."),
            ("Pega a URL e a stream key do Fansly",
             "Entra na sua conta de criador do Fansly, abre o <strong>Creator Dashboard</strong> e vai em <strong>Live → Broadcast Settings → External Encoder</strong>. A página mostra uma <strong>URL do servidor</strong> e uma <strong>stream key</strong> única. Copia as duas."),
            ("Conecta o SplitCam ao Fansly",
             "No SplitCam abre <strong>Stream Settings</strong>, cola a URL do servidor do Fansly e a stream key nos campos de RTMP personalizado. Põe o bitrate em 3.500–6.000 Kbps a 1920×1080, 30 fps, com keyframe de 2 segundos."),
            ("Clica Go Live",
             "Aperta <strong>Go Live</strong> no SplitCam e depois inicia a transmissão do Fansly Live pelo Creator Dashboard. Em uns 10 segundos seu stream chega nos seus assinantes do Fansly."),
        ],
    },
    {
        "slug": "ifriends", "name": "iFriends",
        "title": "Como transmitir no iFriends com SplitCam",
        "desc": "Transmita no iFriends com SplitCam grátis — encoder externo do Model Center, chave RTMP, cenas multicâmera e overlays. Sem marca d'água, sem cadastro.",
        "kw": "como transmitir no ifriends, ifriends, ifriends broadcast, ifriends obs, ifriends external encoder, ifriends rtmp, ifriends stream key",
        "h1html": 'Como transmitir no <span class="accent">iFriends</span> com SplitCam',
        "h1short": "Transmitir no iFriends",
        "card": "Setup do encoder externo pro Model Center maduro do iFriends.",
        "intro": "O iFriends (WebPower) é uma das redes cam independentes mais antigas em atividade — discretamente lucrativa, com base de usuários fiel e um Model Center maduro, criado antes de os broadcasters de navegador virarem comuns. A plataforma oferece um caminho padrão de <strong>External Encoder</strong> a partir do Model Center, ao qual o <strong style='color:var(--text)'>SplitCam</strong> grátis conecta — pra você transmitir com cenas multicâmera modernas, overlays e filtros nessa rede já consolidada.",
        "quick": "Pra transmitir no iFriends com SplitCam: instala o SplitCam, monta sua cena, no Model Center abre <em>Broadcast Settings → External Encoder</em>, copia a URL do servidor e a stream key, cola no SplitCam e dá Go Live."
                 "<ol><li>Instala o SplitCam.</li><li>Adiciona câmera + cena.</li>"
                 "<li>Pega URL e stream key no Model Center.</li>"
                 "<li>Cola no SplitCam.</li>"
                 "<li>Aperta Go Live.</li></ol>",
        "key_how": "Entra na sua conta de modelo do iFriends, abre o <strong>Model Center</strong> e vai em <strong>Broadcast Settings → External Encoder</strong>. A página mostra uma <strong>URL do servidor</strong> e uma <strong>stream key</strong> vinculadas à sua conta — copia as duas pros campos de RTMP personalizado do SplitCam. A aprovação de novas contas de modelo no iFriends é rigorosa, mas legítima; depois de verificada, a opção de encoder externo fica disponível pra sempre.",
        "tips": [
            ("Público fiel, rede madura", "O iFriends roda desde o fim dos anos 90 com uma base de usuários fiel — boa parte é de assinantes antigos, não de visitantes de primeira viagem. Renda estável pra modelos consolidadas, crescimento mais lento pra quem está chegando."),
            ("Broadcaster do navegador vs externo", "O broadcaster legado do iFriends foi feito antes da experiência multicâmera moderna. Migrar pro SplitCam pelo External Encoder é um salto perceptível — cenas multicâmera, overlays e filtros de beleza que a ferramenta antiga não entrega."),
            ("Pagamentos constantes, poucas surpresas", "A controladora do iFriends (WebPower) paga as modelos com confiabilidade há décadas — em prazos mais lentos que as plataformas novas amigas de cripto, mas com pouquíssimas histórias de terror."),
            _T_ETH,
        ],
        "faq": [
            ("O iFriends suporta oficialmente encoders externos tipo o SplitCam?", "Suporta — o Model Center tem a opção External Encoder em Broadcast Settings. URL de servidor RTMP padrão e stream key; OBS, SplitCam e vMix conectam assim que sua conta é aprovada."),
            ("Onde pego minha stream key do iFriends?", "Model Center → Broadcast Settings → External Encoder. A URL do servidor e a stream key aparecem ali — copia as duas pros campos de RTMP personalizado do SplitCam."),
            ("Que bitrate usar no iFriends?", "Manda 1920×1080 a 30 fps, 3.500–6.000 Kbps com keyframe de 2 segundos. Roda primeiro o speed test embutido do SplitCam."),
            ("O SplitCam é grátis pra usar com o iFriends?", "É — o SplitCam é grátis, sem marca d'água e sem limite de tempo. A opção de encoder externo do iFriends é grátis no Model Center."),
        ],
        "steps": [
            ("Baixa e instala o SplitCam",
             "O SplitCam é um software de live streaming grátis pra Windows e macOS — sem cadastro, sem cartão, sem marca d'água."),
            ("Monta sua cena",
             "Abre o SplitCam e adiciona sua webcam. Encaixa overlays, texto, uma segunda câmera ou o celular, filtros de beleza ou fundo IA — cenas modernas e caprichadas se destacam nessa rede madura."),
            ("Pega a URL e a stream key do iFriends",
             "Entra na sua conta de modelo do iFriends, abre o <strong>Model Center</strong> e vai em <strong>Broadcast Settings → External Encoder</strong>. A página mostra uma <strong>URL do servidor</strong> e uma <strong>stream key</strong> única. Copia as duas."),
            ("Conecta o SplitCam ao iFriends",
             "No SplitCam abre <strong>Stream Settings</strong>, cola a URL do servidor do iFriends e a stream key nos campos de RTMP personalizado. Põe o bitrate em 3.500–6.000 Kbps a 1920×1080, 30 fps, com keyframe de 2 segundos."),
            ("Clica Go Live",
             "Aperta <strong>Go Live</strong> no SplitCam e depois fica online pelo Model Center do iFriends. Em uns 10 segundos seu stream chega na rede."),
        ],
    },
    {
        "slug": "babestation", "name": "Babestation",
        "title": "Como transmitir no Babestation com SplitCam",
        "desc": "Transmita no Babestation com SplitCam grátis — encoder externo do Performer Hub, chave RTMP, cenas multicâmera e overlays. Sem marca d'água, sem cadastro.",
        "kw": "como transmitir no babestation, babestation, babestation broadcast, babestation obs, babestation external encoder, babestation rtmp, babestation stream key",
        "h1html": 'Como transmitir no <span class="accent">Babestation</span> com SplitCam',
        "h1short": "Transmitir no Babestation",
        "card": "Setup do encoder externo pro Performer Hub do Babestation, do Reino Unido.",
        "intro": "O Babestation é a maior rede cam / TV adulta do Reino Unido — um híbrido de canais de TV aberta e um produto cam ao vivo alimentado pelas performers logadas no Performer Hub. A plataforma oferece um caminho padrão de <strong>External Encoder</strong> a partir do Performer Hub, ao qual o <strong style='color:var(--text)'>SplitCam</strong> grátis conecta — pra performers independentes do Reino Unido transmitirem com cenas multicâmera, overlays e filtros de beleza que vão além do broadcaster padrão, com cara de estúdio de TV, do Babestation.",
        "quick": "Pra transmitir no Babestation com SplitCam: instala o SplitCam, monta sua cena, no Performer Hub abre <em>Broadcast Settings → External Encoder</em>, copia a URL do servidor e a stream key, cola no SplitCam e dá Go Live."
                 "<ol><li>Instala o SplitCam.</li><li>Adiciona câmera + cena.</li>"
                 "<li>Pega URL e stream key no Performer Hub.</li>"
                 "<li>Cola no SplitCam.</li>"
                 "<li>Aperta Go Live.</li></ol>",
        "key_how": "Entra na sua conta de performer do Babestation, abre o <strong>Performer Hub</strong> e vai em <strong>Broadcast Settings → External Encoder</strong>. A página mostra uma <strong>URL do servidor</strong> e uma <strong>stream key</strong> vinculadas à sua conta — copia as duas pros campos de RTMP personalizado do SplitCam. O onboarding de performers do Babestation no Reino Unido inclui verificação de ID, conforme as regras britânicas de checagem de idade.",
        "tips": [
            ("Público e horário voltados ao Reino Unido", "O pico de tráfego do Babestation é o fim de noite / madrugada no Reino Unido (GMT/BST). Se você está em outro fuso, transmitir no horário noturno britânico rende bem mais do que mirar o horário nobre local nessa rede."),
            ("Acabamento de estúdio de TV é esperado", "A marca do Babestation está ligada aos seus canais de TV — o público espera cenários e iluminação mais produzidos do que numa webcam comum. As cenas do SplitCam (overlays, texto com marca, fundo IA) ajudam a alcançar a estética caprichada da plataforma."),
            ("Performers independentes vs de estúdio", "O Babestation trabalha tanto com estúdios britânicos quanto com performers independentes. Quem transmite de forma independente pelo External Encoder recebe pelo mesmo modelo de pagamento das câmeras alimentadas por estúdio."),
            _T_ETH,
        ],
        "faq": [
            ("O Babestation suporta encoders externos tipo o SplitCam?", "Suporta — o Performer Hub tem a opção External Encoder em Broadcast Settings. URL de servidor RTMP padrão e stream key; OBS, SplitCam e vMix conectam depois que a verificação da performer é concluída."),
            ("Onde pego minha stream key do Babestation?", "Performer Hub → Broadcast Settings → External Encoder. A URL do servidor e a stream key aparecem ali — copia as duas pros campos de RTMP personalizado do SplitCam."),
            ("Que bitrate usar no Babestation?", "Manda 1920×1080 a 30 fps, 3.500–6.000 Kbps com keyframe de 2 segundos. A banda de upload no Reino Unido costuma ser boa, mas roda primeiro o speed test do SplitCam."),
            ("O SplitCam é grátis pra usar com o Babestation?", "É — o SplitCam é grátis, sem marca d'água e sem limite de tempo. A opção de encoder externo do Babestation é grátis no Performer Hub."),
        ],
        "steps": [
            ("Baixa e instala o SplitCam",
             "O SplitCam é um software de live streaming grátis pra Windows e macOS — sem cadastro, sem cartão, sem marca d'água."),
            ("Monta sua cena",
             "Abre o SplitCam e adiciona sua webcam. Encaixa overlays, texto, uma segunda câmera ou o celular, filtros de beleza ou fundo IA — acompanha o acabamento de estúdio de TV do Babestation pra se destacar."),
            ("Pega a URL e a stream key do Babestation",
             "Entra na sua conta de performer do Babestation, abre o <strong>Performer Hub</strong> e vai em <strong>Broadcast Settings → External Encoder</strong>. A página mostra uma <strong>URL do servidor</strong> e uma <strong>stream key</strong> única. Copia as duas."),
            ("Conecta o SplitCam ao Babestation",
             "No SplitCam abre <strong>Stream Settings</strong>, cola a URL do servidor do Babestation e a stream key nos campos de RTMP personalizado. Põe o bitrate em 3.500–6.000 Kbps a 1920×1080, 30 fps, com keyframe de 2 segundos."),
            ("Clica Go Live",
             "Aperta <strong>Go Live</strong> no SplitCam e depois fica online pelo Performer Hub. Em uns 10 segundos seu stream chega ao público britânico do Babestation."),
        ],
    },
    {
        "slug": "adultwork", "name": "AdultWork",
        "title": "Como transmitir no AdultWork com SplitCam",
        "desc": "Transmita no AdultWork com SplitCam grátis — encoder externo da Members Area, chave RTMP, cenas multicâmera e overlays. Sem marca d'água, sem cadastro.",
        "kw": "como transmitir no adultwork, adultwork, adultwork broadcast, adultwork obs, adultwork external encoder, adultwork rtmp, adultwork stream key",
        "h1html": 'Como transmitir no <span class="accent">AdultWork</span> com SplitCam',
        "h1short": "Transmitir no AdultWork",
        "card": "Setup do encoder externo pro recurso de cam da Members Area do AdultWork, do Reino Unido.",
        "intro": "O AdultWork é o consolidado marketplace de serviços adultos do Reino Unido — conhecido principalmente por agendamentos de acompanhantes, venda de fotos / vídeos e serviços por telefone, com um <strong>recurso de webcam</strong> ao vivo ao lado. A plataforma oferece um caminho padrão de <strong>External Encoder</strong> a partir da Members Area, ao qual o <strong style='color:var(--text)'>SplitCam</strong> grátis conecta — pra performers independentes do Reino Unido somarem receita de cam ao vivo com cenas multicâmera, overlays e filtros.",
        "quick": "Pra transmitir no AdultWork com SplitCam: instala o SplitCam, monta sua cena, na Members Area abre <em>Members → Broadcasting → External Encoder</em>, copia a URL do servidor e a stream key, cola no SplitCam e dá Go Live."
                 "<ol><li>Instala o SplitCam.</li><li>Adiciona câmera + cena.</li>"
                 "<li>Pega URL e stream key na Members Area.</li>"
                 "<li>Cola no SplitCam.</li>"
                 "<li>Aperta Go Live.</li></ol>",
        "key_how": "Entra na sua conta de performer do AdultWork, abre a <strong>Members Area</strong> e vai em <strong>Members → Broadcasting → External Encoder</strong>. A página mostra uma <strong>URL do servidor</strong> e uma <strong>stream key</strong> vinculadas à sua conta — copia as duas pros campos de RTMP personalizado do SplitCam. A verificação no AdultWork é obrigatória pro recurso de cam ao vivo e cobre a conformidade com a checagem de idade do Reino Unido.",
        "tips": [
            ("Venda cruzada a partir dos outros serviços do AdultWork", "A força do AdultWork é a base de clientes que já tem — quem assiste talvez já contrate seus serviços de foto / vídeo / telefone. Use as lives de cam pra fazer venda cruzada com clientes que ainda não experimentaram sua cam, em vez de correr atrás de desconhecidos."),
            ("A Members Area é a porta de entrada", "Não procure o broadcaster no site público — tudo do lado da performer fica dentro da Members Area. Configurações de transmissão, pagamentos e gestão de conteúdo estão todos ali."),
            ("Foco no Reino Unido, mas pagamentos internacionais", "A maior parte do tráfego é do Reino Unido / Europa. Os pagamentos funcionam internacionalmente por transferência bancária / carteira digital padrão, com prazos semanais comuns na plataforma."),
            _T_ETH,
        ],
        "faq": [
            ("O AdultWork suporta encoders externos tipo o SplitCam?", "Suporta — a Members Area tem a opção External Encoder em Broadcasting. URL de servidor RTMP padrão e stream key; OBS, SplitCam e vMix conectam depois da verificação da performer."),
            ("Onde pego minha stream key do AdultWork?", "Members Area → Members → Broadcasting → External Encoder. A URL do servidor e a stream key aparecem ali — copia as duas pros campos de RTMP personalizado do SplitCam."),
            ("Que bitrate usar no AdultWork?", "Manda 1920×1080 a 30 fps, 3.500–6.000 Kbps com keyframe de 2 segundos. Roda primeiro o speed test embutido do SplitCam."),
            ("O SplitCam é grátis pra usar com o AdultWork?", "É — o SplitCam é grátis, sem marca d'água e sem limite de tempo. A opção de encoder externo do AdultWork é grátis na Members Area."),
        ],
        "steps": [
            ("Baixa e instala o SplitCam",
             "O SplitCam é um software de live streaming grátis pra Windows e macOS — sem cadastro, sem cartão, sem marca d'água."),
            ("Monta sua cena",
             "Abre o SplitCam e adiciona sua webcam. Encaixa overlays, texto, uma segunda câmera ou o celular, filtros de beleza ou fundo IA — usa os overlays pra divulgar seu conteúdo / serviços por telefone do AdultWork e fazer venda cruzada durante a live."),
            ("Pega a URL e a stream key do AdultWork",
             "Entra na sua conta de performer do AdultWork, abre a <strong>Members Area</strong> e vai em <strong>Members → Broadcasting → External Encoder</strong>. A página mostra uma <strong>URL do servidor</strong> e uma <strong>stream key</strong> única. Copia as duas."),
            ("Conecta o SplitCam ao AdultWork",
             "No SplitCam abre <strong>Stream Settings</strong>, cola a URL do servidor do AdultWork e a stream key nos campos de RTMP personalizado. Põe o bitrate em 3.500–6.000 Kbps a 1920×1080, 30 fps, com keyframe de 2 segundos."),
            ("Clica Go Live",
             "Aperta <strong>Go Live</strong> no SplitCam e depois fica online pela Members Area. Em uns 10 segundos seu stream chega ao público do AdultWork."),
        ],
    },
    {
        "slug": "jerkmate", "name": "Jerkmate",
        "title": "Como transmitir no Jerkmate com SplitCam",
        "desc": "Transmita no Jerkmate com SplitCam grátis — o Jerkmate puxa modelos da rede Streamate, então você vai ao ar via SM Connect, com cenas multicâmera.",
        "kw": "como transmitir no jerkmate, jerkmate, jerkmate broadcast, jerkmate sm connect, jerkmate streamate, jerkmate obs, jerkmate stream key",
        "h1html": 'Como transmitir no <span class="accent">Jerkmate</span> com SplitCam',
        "h1short": "Transmitir no Jerkmate",
        "card": "O Jerkmate puxa os modelos da rede Streamate — transmite via SM Connect + SplitCam.",
        "intro": "O Jerkmate é uma das marcas cam mais buscadas, famosa pelo matchmaker com IA que liga os espectadores aos modelos ao vivo. Ele não roda broadcaster próprio — o Jerkmate <strong>puxa os modelos ao vivo da rede Streamate</strong>. Você transmite como modelo da rede Streamate e o seu show é distribuído pro Jerkmate e os sites parceiros. Como o Streamate já vem <strong style='color:var(--text)'>pré-configurado na lista de canais</strong> do SplitCam, o <strong style='color:var(--text)'>SplitCam</strong> grátis te deixa adicionar cenas multi-câmera, overlays e filtros sem digitar RTMP na mão.",
        "quick": "Transmitir no Jerkmate com SplitCam: instalar SplitCam, montar a cena, cadastrar como modelo na rede Streamate que alimenta o Jerkmate, abrir <em>SM Connect → Start Show</em> e copiar a chave, depois no SplitCam abrir <em>Stream Settings → Add Channel → Streamate</em> e colar, Go Live."
                 "<ol><li>Instalar SplitCam.</li><li>Adicionar câmera + cena.</li>"
                 "<li>Cadastrar como modelo da rede Streamate.</li>"
                 "<li>Pegar a chave via SM Connect.</li>"
                 "<li>Add Channel → Streamate, Go Live.</li></ol>",
        "key_how": "As cams ao vivo do Jerkmate vêm da <strong>rede de transmissão Streamate</strong> — não existe um \"Jerkmate encoder\" separado. Cadastra pelo programa de modelos do Jerkmate ou direto na rede Streamate, abre <strong>SM Connect</strong>, aceita os termos, clica <strong>Start Show</strong> e copia a sua streaming key. No SplitCam abre <strong>Stream Settings → Add Channel</strong>, escolhe <strong>Streamate</strong> da lista integrada e cola a chave. Daí o seu stream chega ao Jerkmate e aos sites parceiros da rede de uma vez só.",
        "tips": [
            ("Por baixo é a rede Streamate", "Não procura um broadcaster específico do Jerkmate — você transmite no Streamate e o Jerkmate redistribui. Tudo que vale pro Streamate (SM Connect, o canal integrado do SplitCam) vale pro Jerkmate."),
            ("Converte o tráfego do matchmaker", "O matchmaker do Jerkmate empurra pros modelos os espectadores que combinam com as escolhas deles — uma cena caprichada no SplitCam, com overlays e bom enquadramento, converte esse público casado muito melhor que uma webcam plana."),
            ("Um feed, vários sites", "Transmitir pra rede Streamate te coloca no Jerkmate e nos sites parceiros ao mesmo tempo — mais alcance a partir de um único stream do SplitCam, sem setup extra."),
            _T_ETH,
        ],
        "faq": [
            ("O Jerkmate tem broadcaster ou stream key próprios?", "Não — o Jerkmate puxa os modelos ao vivo da rede Streamate. Você transmite como modelo da rede Streamate via SM Connect e o seu show aparece no Jerkmate automaticamente."),
            ("Como pego minha stream key do Jerkmate?", "Pelo SM Connect, do lado de modelo da rede Streamate: aceita os termos → Start Show → copia a chave. Cola no canal Streamate integrado do SplitCam — sem URL RTMP manual."),
            ("Que bitrate pro Jerkmate?", "Trava 1080p a 30 fps. O feed da rede é adaptativo, então bitrate mais baixo numa imagem parada é normal. Roda o teste de velocidade do SplitCam e usa conexão por cabo."),
            ("O SplitCam é grátis pro Jerkmate?", "Sim — grátis, sem marca d'água e sem limite de tempo. O Streamate (que alimenta o Jerkmate) é canal integrado no SplitCam, então não tem custo separado de encoder."),
        ],
        "steps": [
            ("Baixa e instala o SplitCam", "O SplitCam é um software de live streaming grátis pra Windows e macOS — sem cadastro, sem cartão, sem marca d'água."),
            ("Monta sua cena", "Abre o SplitCam e adiciona a webcam. Encaixa overlays, texto, uma segunda câmera ou o celular, filtros de beleza ou fundo com IA — uma cena forte converte os espectadores casados do Jerkmate."),
            ("Cadastra como modelo e pega a chave", "Cadastra pelo programa de modelos do Jerkmate ou direto na <strong>rede Streamate</strong> que o alimenta. Abre <strong>SM Connect</strong>, aceita os termos, clica <strong>Start Show</strong> e copia a sua streaming key."),
            ("Adiciona o Streamate como canal no SplitCam", "Abre <strong>Stream Settings → Add Channel</strong>, escolhe <strong>Streamate</strong> da lista integrada e cola a chave — sem URL RTMP manual. Trava a resolução em 1080p."),
            ("Clica Go Live", "Aperta <strong>Go Live</strong> no SplitCam — um slider verde confirma a conexão. Seu show sai por toda a rede Streamate e aparece no Jerkmate."),
        ],
    },
    {
        "slug": "justforfans", "name": "JustForFans",
        "title": "Ficar ao vivo no JustForFans com SplitCam",
        "desc": "Fique ao vivo no JustForFans (JFF) com SplitCam grátis como câmera virtual — cenas multicâmera, overlays e filtros no broadcaster do JFF. Sem marca d'água.",
        "kw": "como ficar ao vivo no justforfans, justforfans, justforfans live, justforfans virtual camera, justforfans câmera virtual, justforfans obs, jff cam",
        "h1html": 'Como entrar ao vivo no <span class="accent">JustForFans</span> com SplitCam',
        "h1short": "Live no JustForFans",
        "card": "Usa o SplitCam como câmera virtual no broadcaster ao vivo do JustForFans.",
        "intro": "O JustForFans (JFF) é uma plataforma de assinatura controlada por criadores — uma alternativa ao OnlyFans antiga e fundada por performers, com assinaturas, pay-per-view e um recurso ao vivo no navegador. O broadcaster ao vivo mostra uma webcam plana e simples; apontar ele pro <strong style='color:var(--text)'>SplitCam</strong> grátis como <strong>câmera virtual</strong> libera cenas multi-câmera, overlays e filtros. Se o seu painel de criador também expõe uma opção de encoder externo / stream key, o SplitCam conecta via RTMP no lugar disso.",
        "quick": "Live no JustForFans com SplitCam: instalar SplitCam, montar a cena, iniciar uma transmissão ao vivo no JFF e, no seletor de câmera do broadcaster, escolher <em>SplitCam</em> como webcam — daí é só entrar ao vivo."
                 "<ol><li>Instalar SplitCam.</li><li>Adicionar câmera + cena.</li>"
                 "<li>Iniciar uma transmissão ao vivo no JFF.</li>"
                 "<li>Selecionar SplitCam na lista de câmeras.</li><li>Go Live.</li></ol>",
        "key_how": "O live do JustForFans roda no navegador. Monta a cena no SplitCam — ele aparece como uma webcam do sistema chamada <strong>\"SplitCam Video Driver\"</strong> — depois abre o broadcaster ao vivo do JFF e, na lista de câmeras, escolhe <strong>SplitCam</strong> no lugar da webcam crua. Sua cena composta substitui a câmera plana. Se o painel de criador do JFF oferecer uma opção de <strong>encoder externo / stream key</strong>, cola essa chave nos campos de RTMP personalizado do SplitCam.",
        "tips": [
            ("Câmera virtual funciona em qualquer lugar", "Mesmo quando o live de uma plataforma é só no navegador, o SplitCam aparece como webcam selecionável — então sua cena multi-câmera, overlays e filtros funcionam no JFF sem stream key nenhuma."),
            ("Controlado por criadores, amigo das performers", "O JFF é tocado por performers e mantém uma base fiel de assinantes. Overlays divulgando seu PPV ou assinatura convertem bem num público que já está pagando."),
            ("Dá permissão de câmera ao navegador", "Se o SplitCam não aparecer na lista de câmeras do JFF, confere se o SplitCam está aberto antes e se o navegador tem permissão de câmera — depois recarrega o broadcaster."),
            _T_TEST,
        ],
        "faq": [
            ("Como o SplitCam conecta no JustForFans?", "O live do JFF é no navegador, então o SplitCam conecta como câmera virtual: escolhe SplitCam no seletor de câmera do broadcaster do JFF. Não precisa de stream key."),
            ("Dá pra usar overlays e várias câmeras no JFF?", "Dá — monta a cena no SplitCam (segunda câmera, overlays, filtros de beleza ou fundo com IA) e o JFF vê a cena pronta como uma única webcam."),
            ("O JustForFans suporta OBS ou encoders externos?", "O live do JFF é principalmente por navegador/webcam. Se o seu painel de criador mostrar uma opção de encoder externo ou stream key, cola ela nos campos de RTMP personalizado do SplitCam; senão, usa o método da câmera virtual."),
            ("O SplitCam é grátis pro JustForFans?", "Sim — grátis, sem marca d'água e sem limite de tempo."),
        ],
        "steps": [
            ("Baixa e instala o SplitCam", "O SplitCam é um software de live streaming grátis pra Windows e macOS — sem cadastro, sem cartão, sem marca d'água. Ele instala uma câmera virtual que o navegador consegue selecionar."),
            ("Monta sua cena", "Abre o SplitCam e adiciona a webcam. Encaixa overlays, texto, uma segunda câmera ou o celular, filtros de beleza ou fundo com IA — tudo aplicado ao vivo."),
            ("Inicia uma transmissão ao vivo no JFF", "Entra na sua conta de criador do JustForFans e abre o broadcaster ao vivo pra começar uma transmissão pros seus assinantes."),
            ("Seleciona o SplitCam como câmera", "Na lista de câmeras do broadcaster do JFF, escolhe <strong>SplitCam</strong> no lugar da webcam crua — sua cena composta substitui a câmera plana. (Ou, se disponível, cola a chave de encoder externo do JFF nos campos de RTMP personalizado do SplitCam.)"),
            ("Go Live", "Inicia a transmissão — sua cena do SplitCam, overlays e filtros chegam aos seus assinantes do JustForFans."),
        ],
    },
    {
        "slug": "fanvue", "name": "Fanvue",
        "title": "Ficar ao vivo no Fanvue com SplitCam — Câmera Virtual",
        "desc": "Fique ao vivo no Fanvue com SplitCam grátis como câmera virtual — cenas multicâmera, overlays e filtros pros seus assinantes. Sem marca d'água.",
        "kw": "como ficar ao vivo no fanvue, fanvue, fanvue live, fanvue câmera virtual, fanvue virtual camera, fanvue obs, fanvue criador",
        "h1html": 'Como entrar ao vivo no <span class="accent">Fanvue</span> com SplitCam',
        "h1short": "Live no Fanvue",
        "card": "Usa o SplitCam como câmera virtual no live do Fanvue.",
        "intro": "O Fanvue é uma plataforma britânica de assinatura para criadores que cresce rápido — uma alternativa ao OnlyFans conhecida por ser amiga dos criadores e da IA, com assinaturas, pay-per-view e transmissão ao vivo. O broadcaster ao vivo roda no navegador, então apontar ele pro <strong style='color:var(--text)'>SplitCam</strong> grátis como <strong>câmera virtual</strong> libera cenas multi-câmera, overlays e filtros. Se o seu painel de criador expõe uma opção de encoder externo / stream key, o SplitCam conecta via RTMP no lugar disso.",
        "quick": "Live no Fanvue com SplitCam: instalar SplitCam, montar a cena, iniciar uma transmissão ao vivo no Fanvue e, no seletor de câmera do broadcaster, escolher <em>SplitCam</em> — daí é só entrar ao vivo."
                 "<ol><li>Instalar SplitCam.</li><li>Adicionar câmera + cena.</li>"
                 "<li>Iniciar uma transmissão ao vivo no Fanvue.</li>"
                 "<li>Selecionar SplitCam na lista de câmeras.</li><li>Go Live.</li></ol>",
        "key_how": "O live do Fanvue roda no navegador. Monta a cena no SplitCam — ele aparece como uma webcam do sistema chamada <strong>\"SplitCam Video Driver\"</strong> — depois abre o broadcaster ao vivo do Fanvue e, na lista de câmeras, escolhe <strong>SplitCam</strong> no lugar da webcam crua. Se o seu painel de criador oferecer uma opção de <strong>encoder externo / stream key</strong>, cola essa chave nos campos de RTMP personalizado do SplitCam.",
        "tips": [
            ("Câmera virtual funciona em qualquer lugar", "Mesmo quando o live de uma plataforma é só no navegador, o SplitCam aparece como webcam selecionável — cenas multi-câmera, overlays e filtros funcionam no Fanvue sem stream key nenhuma."),
            ("Amigo dos criadores e da IA", "O Fanvue acolhe criadores de IA e paga de forma limpa. Overlays que fazem venda cruzada da sua assinatura ou PPV convertem bem num público que já está pagando."),
            ("Dá permissão de câmera ao navegador", "Se o SplitCam não aparecer na lista de câmeras do Fanvue, confere se o SplitCam está aberto antes e se o navegador tem permissão de câmera — depois recarrega."),
            _T_TEST,
        ],
        "faq": [
            ("Como o SplitCam conecta no Fanvue?", "O live do Fanvue é no navegador, então o SplitCam conecta como câmera virtual: escolhe SplitCam no seletor de câmera. Não precisa de stream key."),
            ("Dá pra usar overlays e várias câmeras no Fanvue?", "Dá — monta a cena no SplitCam (segunda câmera, overlays, filtros de beleza ou fundo com IA) e o Fanvue vê a cena pronta como uma única webcam."),
            ("O Fanvue suporta OBS ou encoders externos?", "O live do Fanvue é principalmente por navegador/webcam. Se o seu painel mostrar uma opção de encoder externo ou stream key, cola ela nos campos de RTMP personalizado do SplitCam; senão, usa o método da câmera virtual."),
            ("O SplitCam é grátis pro Fanvue?", "Sim — grátis, sem marca d'água e sem limite de tempo."),
        ],
        "steps": [
            ("Baixa e instala o SplitCam", "O SplitCam é um software de live streaming grátis pra Windows e macOS — sem cadastro, sem cartão, sem marca d'água. Ele instala uma câmera virtual que o navegador consegue selecionar."),
            ("Monta sua cena", "Abre o SplitCam e adiciona a webcam. Encaixa overlays, texto, uma segunda câmera ou o celular, filtros de beleza ou fundo com IA — tudo aplicado ao vivo."),
            ("Inicia uma transmissão ao vivo no Fanvue", "Entra na sua conta de criador do Fanvue e abre o broadcaster ao vivo pra começar uma transmissão pros seus assinantes."),
            ("Seleciona o SplitCam como câmera", "Na lista de câmeras do Fanvue, escolhe <strong>SplitCam</strong> no lugar da webcam crua — sua cena composta substitui a câmera plana. (Ou, se disponível, cola a chave de encoder externo nos campos de RTMP personalizado do SplitCam.)"),
            ("Go Live", "Inicia a transmissão — sua cena do SplitCam, overlays e filtros chegam aos seus assinantes do Fanvue."),
        ],
    },
    {
        "slug": "loyalfans", "name": "LoyalFans",
        "title": "Ficar ao vivo no LoyalFans com SplitCam — Câmera Virtual",
        "desc": "Fique ao vivo no LoyalFans com SplitCam grátis como câmera virtual — cenas multicâmera, overlays e filtros pros assinantes e quem dá tip. Sem marca d'água.",
        "kw": "como ficar ao vivo no loyalfans, loyalfans, loyalfans live, loyalfans câmera virtual, loyalfans virtual camera, loyalfans obs, loyal fans",
        "h1html": 'Como entrar ao vivo no <span class="accent">LoyalFans</span> com SplitCam',
        "h1short": "Live no LoyalFans",
        "card": "Usa o SplitCam como câmera virtual no live do LoyalFans.",
        "intro": "O LoyalFans é uma plataforma de assinatura para criadores — com assinaturas, pay-per-view, tips e um recurso de <strong>live cam</strong> embutido. O broadcaster ao vivo roda no navegador, então conectar o <strong style='color:var(--text)'>SplitCam</strong> grátis como <strong>câmera virtual</strong> soma cenas multi-câmera, overlays e filtros por cima da webcam padrão. Se o seu painel expõe uma opção de encoder externo / stream key, o SplitCam conecta via RTMP no lugar disso.",
        "quick": "Live no LoyalFans com SplitCam: instalar SplitCam, montar a cena, iniciar uma transmissão ao vivo no LoyalFans e escolher <em>SplitCam</em> no seletor de câmera do broadcaster — daí é só entrar ao vivo."
                 "<ol><li>Instalar SplitCam.</li><li>Adicionar câmera + cena.</li>"
                 "<li>Iniciar uma transmissão ao vivo no LoyalFans.</li>"
                 "<li>Selecionar SplitCam na lista de câmeras.</li><li>Go Live.</li></ol>",
        "key_how": "O live do LoyalFans roda no navegador. Monta a cena no SplitCam — ele aparece como uma webcam do sistema chamada <strong>\"SplitCam Video Driver\"</strong> — depois abre o broadcaster ao vivo do LoyalFans e, na lista de câmeras, escolhe <strong>SplitCam</strong>. Se aparecer uma opção de <strong>stream key / encoder externo</strong> no seu painel de criador, cola ela nos campos de RTMP personalizado do SplitCam.",
        "tips": [
            ("Câmera virtual, sem chave nenhuma", "O live no navegador ainda recebe a sua cena completa do SplitCam — overlays, segunda câmera e filtros — só de escolher o SplitCam como webcam."),
            ("Os tips premiam produção", "O LoyalFans se apoia em tips; overlays de meta de tip na tela e uma cena caprichada incentivam mais do que uma webcam plana."),
            ("Dá permissão de câmera ao navegador", "Se o SplitCam não estiver na lista de câmeras do LoyalFans, abre o SplitCam antes, libera o acesso à câmera no navegador e recarrega o broadcaster."),
            _T_TEST,
        ],
        "faq": [
            ("Como o SplitCam conecta no LoyalFans?", "O live do LoyalFans é no navegador, então o SplitCam conecta como câmera virtual — escolhe SplitCam no seletor de câmera. Não precisa de stream key."),
            ("Dá pra usar overlays e várias câmeras no LoyalFans?", "Dá — monta a cena no SplitCam (segunda câmera, overlays, filtros de beleza ou fundo com IA); o LoyalFans vê tudo como uma única webcam."),
            ("O LoyalFans suporta OBS ou encoders externos?", "O live é principalmente por navegador/webcam. Se o seu painel mostrar uma opção de stream key, cola ela nos campos de RTMP personalizado do SplitCam; senão, usa o método da câmera virtual."),
            ("O SplitCam é grátis pro LoyalFans?", "Sim — grátis, sem marca d'água e sem limite de tempo."),
        ],
        "steps": [
            ("Baixa e instala o SplitCam", "O SplitCam é um software de live streaming grátis pra Windows e macOS — sem cadastro, sem cartão, sem marca d'água. Ele instala uma câmera virtual que o navegador consegue selecionar."),
            ("Monta sua cena", "Abre o SplitCam e adiciona a webcam. Encaixa overlays, texto de meta de tip, uma segunda câmera ou o celular, filtros de beleza ou fundo com IA."),
            ("Inicia uma transmissão ao vivo no LoyalFans", "Entra na sua conta do LoyalFans e abre o broadcaster ao vivo pra entrar ao vivo pros seus assinantes."),
            ("Seleciona o SplitCam como câmera", "Na lista de câmeras do LoyalFans, escolhe <strong>SplitCam</strong> no lugar da webcam crua — sua cena substitui a câmera plana. (Ou, se disponível, cola a stream key nos campos de RTMP personalizado do SplitCam.)"),
            ("Go Live", "Inicia a transmissão — sua cena do SplitCam chega ao público do LoyalFans."),
        ],
    },
    {
        "slug": "fancentro", "name": "FanCentro",
        "title": "Ficar ao vivo no FanCentro com SplitCam — Câmera Virtual",
        "desc": "Fique ao vivo no FanCentro com SplitCam grátis como câmera virtual — cenas multicâmera, overlays e filtros pros seus assinantes. Sem marca d'água.",
        "kw": "como ficar ao vivo no fancentro, fancentro, fancentro live, fancentro câmera virtual, fancentro virtual camera, fancentro obs, fan centro",
        "h1html": 'Como entrar ao vivo no <span class="accent">FanCentro</span> com SplitCam',
        "h1short": "Live no FanCentro",
        "card": "Usa o SplitCam como câmera virtual no live do FanCentro.",
        "intro": "O FanCentro é uma plataforma de monetização para criadores que está no mercado há tempo — assinaturas, mensagens pay-per-view, conteúdo e transmissão ao vivo. O live roda no navegador, então conectar o <strong style='color:var(--text)'>SplitCam</strong> grátis como <strong>câmera virtual</strong> soma cenas multi-câmera, overlays e filtros que vão além da webcam simples. Se o seu painel expõe uma opção de encoder externo / stream key, o SplitCam conecta via RTMP no lugar disso.",
        "quick": "Live no FanCentro com SplitCam: instalar SplitCam, montar a cena, iniciar uma transmissão ao vivo no FanCentro e escolher <em>SplitCam</em> no seletor de câmera do broadcaster — daí é só entrar ao vivo."
                 "<ol><li>Instalar SplitCam.</li><li>Adicionar câmera + cena.</li>"
                 "<li>Iniciar uma transmissão ao vivo no FanCentro.</li>"
                 "<li>Selecionar SplitCam na lista de câmeras.</li><li>Go Live.</li></ol>",
        "key_how": "O live do FanCentro roda no navegador. Monta a cena no SplitCam — ele aparece como uma webcam do sistema chamada <strong>\"SplitCam Video Driver\"</strong> — depois abre o broadcaster ao vivo do FanCentro e, na lista de câmeras, escolhe <strong>SplitCam</strong>. Se for oferecida uma opção de <strong>stream key / encoder externo</strong>, cola ela nos campos de RTMP personalizado do SplitCam.",
        "tips": [
            ("Câmera virtual funciona em qualquer lugar", "O live só no navegador ainda recebe a sua cena completa do SplitCam — overlays, segunda câmera e filtros — só de escolher o SplitCam como webcam."),
            ("Faça venda cruzada do seu funil", "O FanCentro é construído em torno de funis de criador e PPV. Overlays divulgando sua assinatura ou mensagens pagas convertem quem assiste em comprador."),
            ("Dá permissão de câmera ao navegador", "Se o SplitCam não estiver listado, abre o SplitCam antes, libera o acesso à câmera no navegador e recarrega o broadcaster."),
            _T_TEST,
        ],
        "faq": [
            ("Como o SplitCam conecta no FanCentro?", "O live do FanCentro é no navegador, então o SplitCam conecta como câmera virtual — escolhe SplitCam no seletor de câmera. Não precisa de stream key."),
            ("Dá pra usar overlays e várias câmeras no FanCentro?", "Dá — monta a cena no SplitCam; o FanCentro vê a cena pronta como uma única webcam."),
            ("O FanCentro suporta OBS ou encoders externos?", "O live é principalmente por navegador/webcam. Se aparecer uma opção de stream key no seu painel, cola ela nos campos de RTMP personalizado do SplitCam; senão, usa o método da câmera virtual."),
            ("O SplitCam é grátis pro FanCentro?", "Sim — grátis, sem marca d'água e sem limite de tempo."),
        ],
        "steps": [
            ("Baixa e instala o SplitCam", "O SplitCam é um software de live streaming grátis pra Windows e macOS — sem cadastro, sem cartão, sem marca d'água. Ele instala uma câmera virtual que o navegador consegue selecionar."),
            ("Monta sua cena", "Abre o SplitCam e adiciona a webcam. Encaixa overlays, texto, uma segunda câmera ou o celular, filtros de beleza ou fundo com IA."),
            ("Inicia uma transmissão ao vivo no FanCentro", "Entra na sua conta do FanCentro e abre o broadcaster ao vivo pra entrar ao vivo pros seus assinantes."),
            ("Seleciona o SplitCam como câmera", "Na lista de câmeras do FanCentro, escolhe <strong>SplitCam</strong> no lugar da webcam crua. (Ou, se disponível, cola a stream key nos campos de RTMP personalizado do SplitCam.)"),
            ("Go Live", "Inicia a transmissão — sua cena do SplitCam chega aos seus assinantes do FanCentro."),
        ],
    },
    {
        "slug": "ismygirl", "name": "IsMyGirl",
        "title": "Ficar ao vivo no IsMyGirl com SplitCam — Câmera Virtual",
        "desc": "Fique ao vivo no IsMyGirl com SplitCam grátis como câmera virtual — cenas multicâmera, overlays e filtros pros seus assinantes. Sem marca d'água.",
        "kw": "como ficar ao vivo no ismygirl, ismygirl, ismygirl live, ismygirl câmera virtual, ismygirl virtual camera, ismygirl obs, is my girl",
        "h1html": 'Como entrar ao vivo no <span class="accent">IsMyGirl</span> com SplitCam',
        "h1short": "Live no IsMyGirl",
        "card": "Usa o SplitCam como câmera virtual no live do IsMyGirl.",
        "intro": "O IsMyGirl é uma plataforma de assinatura para criadores — uma alternativa ao OnlyFans com assinaturas, conteúdo pago e transmissão ao vivo, conhecida pelo suporte próximo aos criadores. O broadcaster ao vivo roda no navegador, então conectar o <strong style='color:var(--text)'>SplitCam</strong> grátis como <strong>câmera virtual</strong> traz cenas multi-câmera, overlays e filtros. Se o seu painel expõe uma opção de encoder externo / stream key, o SplitCam conecta via RTMP no lugar disso.",
        "quick": "Live no IsMyGirl com SplitCam: instalar SplitCam, montar a cena, iniciar uma transmissão ao vivo no IsMyGirl e selecionar <em>SplitCam</em> no seletor de câmera do broadcaster — daí é só entrar ao vivo."
                 "<ol><li>Instalar SplitCam.</li><li>Adicionar câmera + cena.</li>"
                 "<li>Iniciar uma transmissão ao vivo no IsMyGirl.</li>"
                 "<li>Selecionar SplitCam na lista de câmeras.</li><li>Go Live.</li></ol>",
        "key_how": "O live do IsMyGirl roda no navegador. Monta a cena no SplitCam — ele aparece como uma webcam do sistema chamada <strong>\"SplitCam Video Driver\"</strong> — depois abre o broadcaster ao vivo do IsMyGirl e, na lista de câmeras, escolhe <strong>SplitCam</strong>. Se aparecer uma opção de <strong>stream key / encoder externo</strong>, cola ela nos campos de RTMP personalizado do SplitCam.",
        "tips": [
            ("Câmera virtual, sem chave nenhuma", "O live só no navegador ainda recebe a sua cena completa do SplitCam — overlays, segunda câmera e filtros — só de escolher o SplitCam como webcam."),
            ("Aproveita o suporte ao criador", "O IsMyGirl divulga suporte forte e promoção pros criadores. Uma cena caprichada no SplitCam mais overlays de venda cruzada aproveitam ao máximo o tráfego que eles te enviam."),
            ("Dá permissão de câmera ao navegador", "Se o SplitCam não estiver listado, abre o SplitCam antes, libera o acesso à câmera e recarrega o broadcaster."),
            _T_TEST,
        ],
        "faq": [
            ("Como o SplitCam conecta no IsMyGirl?", "O live do IsMyGirl é no navegador, então o SplitCam conecta como câmera virtual — escolhe SplitCam no seletor de câmera. Não precisa de stream key."),
            ("Dá pra usar overlays e várias câmeras no IsMyGirl?", "Dá — monta a cena no SplitCam; o IsMyGirl vê tudo como uma única webcam."),
            ("O IsMyGirl suporta OBS ou encoders externos?", "O live é principalmente por navegador/webcam. Se aparecer uma opção de stream key, cola ela nos campos de RTMP personalizado do SplitCam; senão, usa o método da câmera virtual."),
            ("O SplitCam é grátis pro IsMyGirl?", "Sim — grátis, sem marca d'água e sem limite de tempo."),
        ],
        "steps": [
            ("Baixa e instala o SplitCam", "O SplitCam é um software de live streaming grátis pra Windows e macOS — sem cadastro, sem cartão, sem marca d'água. Ele instala uma câmera virtual que o navegador consegue selecionar."),
            ("Monta sua cena", "Abre o SplitCam e adiciona a webcam. Encaixa overlays, texto, uma segunda câmera ou o celular, filtros de beleza ou fundo com IA."),
            ("Inicia uma transmissão ao vivo no IsMyGirl", "Entra na sua conta do IsMyGirl e abre o broadcaster ao vivo pra entrar ao vivo pros seus assinantes."),
            ("Seleciona o SplitCam como câmera", "Na lista de câmeras do IsMyGirl, escolhe <strong>SplitCam</strong> no lugar da webcam crua. (Ou, se disponível, cola a stream key nos campos de RTMP personalizado do SplitCam.)"),
            ("Go Live", "Inicia a transmissão — sua cena do SplitCam chega aos seus assinantes do IsMyGirl."),
        ],
    },
    {
        "slug": "dxlive", "name": "DXLive",
        "title": "Transmitir no DXLive com SplitCam — External Encoder",
        "desc": "Transmita no DXLive com SplitCam grátis — encoder externo da rede cam premium japonesa, cenas multicâmera e overlays. Sem marca d'água, sem cadastro.",
        "kw": "como transmitir no dxlive, dxlive, dxlive broadcast, dxlive obs, dxlive external encoder, dxlive rtmp, dxlive performer",
        "h1html": 'Como transmitir no <span class="accent">DXLive</span> com SplitCam',
        "h1short": "Transmitir no DXLive",
        "card": "Setup do encoder externo pra rede cam premium do DXLive.",
        "intro": "O DXLive é uma rede de webcam premium consolidada, popular no Japão e em toda a Ásia, construída num modelo de pagamento por minuto com um público fiel. A área de performer suporta um caminho padrão de <strong>External Encoder</strong> ao qual o <strong style='color:var(--text)'>SplitCam</strong> grátis conecta — deixando você transmitir com cenas multicâmera, overlays e filtros de beleza no lugar de uma única webcam plana.",
        "quick": "Transmitir no DXLive com SplitCam: instala o SplitCam, monta sua cena, na área de performer abre as configurações de <em>external encoder / broadcast</em>, copia a URL do servidor e a stream key, cola no SplitCam e dá Go Live."
                 "<ol><li>Instala o SplitCam.</li><li>Adiciona câmera + cena.</li>"
                 "<li>Pega URL e stream key na área de performer.</li>"
                 "<li>Cola no SplitCam.</li>"
                 "<li>Aperta Go Live.</li></ol>",
        "key_how": "Entra na sua conta de performer do DXLive e abre as configurações de <strong>broadcast / external encoder</strong> na área de performer. A página mostra uma <strong>URL do servidor</strong> e uma <strong>stream key</strong> vinculadas à sua conta — copia as duas pros campos de RTMP personalizado do SplitCam. A verificação no DXLive é obrigatória antes de o recurso de live cam ser liberado.",
        "tips": [
            ("Feito pro mercado asiático", "O público do DXLive pende pro Japão/Ásia e paga por minuto. Programa seus shows pras noites no horário JST e a base fiel e pagante converte bem."),
            ("Produção bate webcam crua", "Uma cena limpa no SplitCam com overlays e filtros de beleza se destaca numa rede premium de pagamento por minuto, onde o público espera qualidade."),
            ("Usa o encoder externo, não só a webcam", "Passar pelo RTMP do SplitCam, e não pela cam básica do navegador, é o que libera cenas multicâmera e filtros."),
            _T_ETH,
        ],
        "faq": [
            ("O DXLive suporta encoders externos tipo o SplitCam?", "Suporta — a área de performer tem um caminho padrão de external encoder / RTMP. Copia a URL do servidor e a stream key pro SplitCam depois da verificação."),
            ("Onde pego minha stream key do DXLive?", "Nas configurações de broadcast / external encoder da área de performer — a URL do servidor e a stream key aparecem ali. Cola as duas nos campos de RTMP personalizado do SplitCam."),
            ("Que bitrate usar no DXLive?", "Manda 1920×1080 a 30 fps, 3.500–6.000 Kbps com keyframe de 2 segundos. Roda primeiro o speed test embutido do SplitCam."),
            ("O SplitCam é grátis pra usar com o DXLive?", "É — o SplitCam é grátis, sem marca d'água e sem limite de tempo. A opção de encoder externo do DXLive é grátis na área de performer."),
        ],
        "steps": [
            ("Baixa e instala o SplitCam",
             "O SplitCam é um software de live streaming grátis pra Windows e macOS — sem cadastro, sem cartão, sem marca d'água."),
            ("Monta sua cena",
             "Abre o SplitCam e adiciona sua webcam. Encaixa overlays, texto, uma segunda câmera ou o celular, filtros de beleza ou fundo IA."),
            ("Pega a URL e a stream key do DXLive",
             "Entra na sua conta de performer do DXLive e abre as configurações de <strong>broadcast / external encoder</strong>. Copia a <strong>URL do servidor</strong> e a <strong>stream key</strong>."),
            ("Conecta o SplitCam ao DXLive",
             "No SplitCam abre <strong>Stream Settings</strong>, cola a URL do servidor do DXLive e a stream key nos campos de RTMP personalizado. Põe o bitrate em 3.500–6.000 Kbps a 1920×1080, 30 fps, com keyframe de 2 segundos."),
            ("Clica Go Live",
             "Aperta <strong>Go Live</strong> no SplitCam e depois fica online pela área de performer. Em uns 10 segundos seu stream chega ao público do DXLive."),
        ],
    },
    {
        "slug": "streamen", "name": "Streamen",
        "title": "Transmitir no Streamen com SplitCam — External Encoder",
        "desc": "Transmita no Streamen com SplitCam grátis — setup de encoder externo, cenas multicâmera, overlays e filtros de beleza. Sem marca d'água, sem cadastro.",
        "kw": "como transmitir no streamen, streamen, streamen broadcast, streamen obs, streamen external encoder, streamen rtmp, streamen.tv",
        "h1html": 'Como transmitir no <span class="accent">Streamen</span> com SplitCam',
        "h1short": "Transmitir no Streamen",
        "card": "Setup do encoder externo pra plataforma cam Streamen.",
        "intro": "O Streamen é uma plataforma de live cam onde os modelos transmitem pra um público movido a tips. As configurações de transmissão expõem um caminho padrão de <strong>External Encoder</strong> ao qual o <strong style='color:var(--text)'>SplitCam</strong> grátis conecta — pra você transmitir com cenas multicâmera, overlays e filtros, e não com uma única webcam simples.",
        "quick": "Transmitir no Streamen com SplitCam: instala o SplitCam, monta sua cena, no seu painel de modelo abre <em>broadcast settings → external encoder</em>, copia a URL do servidor e a stream key, cola no SplitCam e dá Go Live."
                 "<ol><li>Instala o SplitCam.</li><li>Adiciona câmera + cena.</li>"
                 "<li>Pega URL e stream key no painel.</li>"
                 "<li>Cola no SplitCam.</li>"
                 "<li>Aperta Go Live.</li></ol>",
        "key_how": "Entra na sua conta de modelo do Streamen e abre a seção de <strong>broadcast settings / external encoder</strong>. Ela mostra uma <strong>URL do servidor</strong> e uma <strong>stream key</strong> vinculadas à sua conta — copia as duas pros campos de RTMP personalizado do SplitCam. A verificação de modelo é obrigatória antes de a transmissão ser liberada.",
        "tips": [
            ("Público movido a tips", "Quem assiste o Streamen dá tip — metas de tip na tela e uma cena caprichada incentivam mais tips que uma webcam plana."),
            ("O encoder externo libera as cenas", "Passar pelo RTMP do SplitCam, e não pela cam básica do navegador, é o que habilita layouts multicâmera, overlays e filtros."),
            ("Trava a sua resolução", "Define 1080p na mão pra que o feed não baixe a qualidade sem avisar; um bitrate que cai numa imagem parada é normal em feeds adaptativos."),
            _T_ETH,
        ],
        "faq": [
            ("O Streamen suporta encoders externos tipo o SplitCam?", "Suporta — as configurações de transmissão têm um caminho padrão de external encoder / RTMP. Copia a URL do servidor e a stream key pro SplitCam depois da verificação."),
            ("Onde pego minha stream key do Streamen?", "Nas configurações de broadcast / external encoder do seu painel de modelo — a URL do servidor e a stream key aparecem ali. Cola as duas nos campos de RTMP personalizado do SplitCam."),
            ("Que bitrate usar no Streamen?", "Manda 1920×1080 a 30 fps, 3.500–6.000 Kbps com keyframe de 2 segundos. Roda primeiro o speed test do SplitCam."),
            ("O SplitCam é grátis pra usar com o Streamen?", "É — o SplitCam é grátis, sem marca d'água e sem limite de tempo. A opção de encoder externo do Streamen é grátis no painel."),
        ],
        "steps": [
            ("Baixa e instala o SplitCam",
             "O SplitCam é um software de live streaming grátis pra Windows e macOS — sem cadastro, sem cartão, sem marca d'água."),
            ("Monta sua cena",
             "Abre o SplitCam e adiciona sua webcam. Encaixa overlays, texto de meta de tip, uma segunda câmera ou o celular, filtros de beleza ou fundo IA."),
            ("Pega a URL e a stream key do Streamen",
             "Entra na sua conta de modelo do Streamen, abre <strong>broadcast settings → external encoder</strong> e copia a <strong>URL do servidor</strong> e a <strong>stream key</strong>."),
            ("Conecta o SplitCam ao Streamen",
             "No SplitCam abre <strong>Stream Settings</strong>, cola a URL do servidor do Streamen e a stream key nos campos de RTMP personalizado. Põe o bitrate em 3.500–6.000 Kbps a 1920×1080, 30 fps, com keyframe de 2 segundos."),
            ("Clica Go Live",
             "Aperta <strong>Go Live</strong> no SplitCam e depois fica online pelo painel. Em uns 10 segundos seu stream chega ao público do Streamen."),
        ],
    },
    {
        "slug": "xcams", "name": "XCams",
        "title": "Transmitir no XCams com SplitCam — External Encoder",
        "desc": "Transmita no XCams com SplitCam grátis — encoder externo da comunidade cam europeia, cenas multicâmera, overlays e filtros. Sem marca d'água, sem cadastro.",
        "kw": "como transmitir no xcams, xcams, xcams broadcast, xcams obs, xcams external encoder, xcams rtmp, x cams",
        "h1html": 'Como transmitir no <span class="accent">XCams</span> com SplitCam',
        "h1short": "Transmitir no XCams",
        "card": "Setup do encoder externo pra comunidade europeia XCams.",
        "intro": "O XCams é uma comunidade europeia de live cam — forte na Itália, na França e na Espanha — construída em torno de shows ao vivo e de uma economia de tips e shows privados. A área de modelo suporta um caminho padrão de <strong>External Encoder</strong> ao qual o <strong style='color:var(--text)'>SplitCam</strong> grátis conecta, pra você transmitir com cenas multicâmera, overlays e filtros de beleza.",
        "quick": "Transmitir no XCams com SplitCam: instala o SplitCam, monta sua cena, na área de modelo abre <em>broadcast / external encoder</em>, copia a URL do servidor e a stream key, cola no SplitCam e dá Go Live."
                 "<ol><li>Instala o SplitCam.</li><li>Adiciona câmera + cena.</li>"
                 "<li>Pega URL e stream key na área de modelo.</li>"
                 "<li>Cola no SplitCam.</li>"
                 "<li>Aperta Go Live.</li></ol>",
        "key_how": "Entra na sua conta de modelo do XCams e abre as configurações de <strong>broadcast / external encoder</strong> na área de modelo. A página mostra uma <strong>URL do servidor</strong> e uma <strong>stream key</strong> vinculadas à sua conta — copia as duas pros campos de RTMP personalizado do SplitCam. A verificação no XCams é obrigatória antes de transmitir.",
        "tips": [
            ("Horário nobre europeu", "O tráfego do XCams tem pico nas noites da Europa (CET). Transmitir nesse horário rende bem mais que fora de pico nessa comunidade."),
            ("Shows privados premiam qualidade", "O XCams roda em shows privados/spy — uma cena caprichada no SplitCam com overlays converte quem só passeia em privados pagos."),
            ("O encoder externo libera as cenas", "Passar pelo RTMP do SplitCam, e não pela cam do navegador, habilita layouts multicâmera, overlays e filtros."),
            _T_ETH,
        ],
        "faq": [
            ("O XCams suporta encoders externos tipo o SplitCam?", "Suporta — a área de modelo tem um caminho padrão de external encoder / RTMP. Copia a URL do servidor e a stream key pro SplitCam depois da verificação."),
            ("Onde pego minha stream key do XCams?", "Nas configurações de broadcast / external encoder da área de modelo — a URL do servidor e a stream key aparecem ali. Cola as duas nos campos de RTMP personalizado do SplitCam."),
            ("Que bitrate usar no XCams?", "Manda 1920×1080 a 30 fps, 3.500–6.000 Kbps com keyframe de 2 segundos. Roda primeiro o speed test do SplitCam."),
            ("O SplitCam é grátis pra usar com o XCams?", "É — o SplitCam é grátis, sem marca d'água e sem limite de tempo. A opção de encoder externo do XCams é grátis na área de modelo."),
        ],
        "steps": [
            ("Baixa e instala o SplitCam",
             "O SplitCam é um software de live streaming grátis pra Windows e macOS — sem cadastro, sem cartão, sem marca d'água."),
            ("Monta sua cena",
             "Abre o SplitCam e adiciona sua webcam. Encaixa overlays, texto, uma segunda câmera ou o celular, filtros de beleza ou fundo IA."),
            ("Pega a URL e a stream key do XCams",
             "Entra na sua conta de modelo do XCams, abre <strong>broadcast / external encoder</strong> e copia a <strong>URL do servidor</strong> e a <strong>stream key</strong>."),
            ("Conecta o SplitCam ao XCams",
             "No SplitCam abre <strong>Stream Settings</strong>, cola a URL do servidor do XCams e a stream key nos campos de RTMP personalizado. Põe o bitrate em 3.500–6.000 Kbps a 1920×1080, 30 fps, com keyframe de 2 segundos."),
            ("Clica Go Live",
             "Aperta <strong>Go Live</strong> no SplitCam e depois fica online pela área de modelo. Em uns 10 segundos seu stream chega ao público do XCams."),
        ],
    },
    {
        "slug": "camcontacts", "name": "CamContacts",
        "title": "Transmitir no CamContacts com SplitCam — External Encoder",
        "desc": "Transmita no CamContacts com SplitCam grátis — encoder externo do site cam pay-per-minute, cenas multicâmera e overlays. Sem marca d'água.",
        "kw": "como transmitir no camcontacts, camcontacts, camcontacts broadcast, camcontacts obs, camcontacts external encoder, camcontacts rtmp, cam contacts",
        "h1html": 'Como transmitir no <span class="accent">CamContacts</span> com SplitCam',
        "h1short": "Transmitir no CamContacts",
        "card": "Setup do encoder externo pra cam pay-per-minute do CamContacts.",
        "intro": "O CamContacts é um dos sites cam independentes mais antigos em atividade — um modelo de pagamento por minuto com público maduro e fiel e fama de pagamentos constantes. A área de performer suporta um caminho padrão de <strong>External Encoder</strong> ao qual o <strong style='color:var(--text)'>SplitCam</strong> grátis conecta, pra você transmitir com cenas multicâmera, overlays e filtros de beleza.",
        "quick": "Transmitir no CamContacts com SplitCam: instala o SplitCam, monta sua cena, na área de performer abre as configurações de <em>external encoder / broadcast</em>, copia a URL do servidor e a stream key, cola no SplitCam e dá Go Live."
                 "<ol><li>Instala o SplitCam.</li><li>Adiciona câmera + cena.</li>"
                 "<li>Pega URL e stream key na área de performer.</li>"
                 "<li>Cola no SplitCam.</li>"
                 "<li>Aperta Go Live.</li></ol>",
        "key_how": "Entra na sua conta de performer do CamContacts e abre as configurações de <strong>broadcast / external encoder</strong> na área de performer. A página mostra uma <strong>URL do servidor</strong> e uma <strong>stream key</strong> vinculadas à sua conta — copia as duas pros campos de RTMP personalizado do SplitCam. A verificação no CamContacts é obrigatória pro recurso de live cam.",
        "tips": [
            ("Público maduro e fiel", "O CamContacts roda há décadas com membros de longa data — regulares mais constantes e que pagam mais que num site grátis de muita rotatividade, mas com crescimento mais lento pra quem chega."),
            ("Pagamento por minuto premia retenção", "Mantém quem assiste em tempo pago com uma cena caprichada e overlays; a produção estende as sessões num modelo por minuto."),
            ("O encoder externo libera as cenas", "Passar pelo RTMP do SplitCam, e não pela cam básica, habilita layouts multicâmera, overlays e filtros."),
            _T_ETH,
        ],
        "faq": [
            ("O CamContacts suporta encoders externos tipo o SplitCam?", "Suporta — a área de performer tem um caminho padrão de external encoder / RTMP. Copia a URL do servidor e a stream key pro SplitCam depois da verificação."),
            ("Onde pego minha stream key do CamContacts?", "Nas configurações de broadcast / external encoder da área de performer — a URL do servidor e a stream key aparecem ali. Cola as duas nos campos de RTMP personalizado do SplitCam."),
            ("Que bitrate usar no CamContacts?", "Manda 1920×1080 a 30 fps, 3.500–6.000 Kbps com keyframe de 2 segundos. Roda primeiro o speed test do SplitCam."),
            ("O SplitCam é grátis pra usar com o CamContacts?", "É — o SplitCam é grátis, sem marca d'água e sem limite de tempo. A opção de encoder externo do CamContacts é grátis na área de performer."),
        ],
        "steps": [
            ("Baixa e instala o SplitCam",
             "O SplitCam é um software de live streaming grátis pra Windows e macOS — sem cadastro, sem cartão, sem marca d'água."),
            ("Monta sua cena",
             "Abre o SplitCam e adiciona sua webcam. Encaixa overlays, texto, uma segunda câmera ou o celular, filtros de beleza ou fundo IA."),
            ("Pega a URL e a stream key do CamContacts",
             "Entra na sua conta de performer do CamContacts, abre as configurações de <strong>broadcast / external encoder</strong> e copia a <strong>URL do servidor</strong> e a <strong>stream key</strong>."),
            ("Conecta o SplitCam ao CamContacts",
             "No SplitCam abre <strong>Stream Settings</strong>, cola a URL do servidor do CamContacts e a stream key nos campos de RTMP personalizado. Põe o bitrate em 3.500–6.000 Kbps a 1920×1080, 30 fps, com keyframe de 2 segundos."),
            ("Clica Go Live",
             "Aperta <strong>Go Live</strong> no SplitCam e depois fica online pela área de performer. Em uns 10 segundos seu stream chega ao público do CamContacts."),
        ],
    },
    {
        "slug": "royalcams", "name": "RoyalCams",
        "title": "Transmitir no RoyalCams com SplitCam — External Encoder",
        "desc": "Transmita no RoyalCams com SplitCam grátis — encoder externo do site cam grátis por token, cenas multicâmera, overlays e filtros. Sem marca d'água.",
        "kw": "como transmitir no royalcams, royalcams, royalcams broadcast, royalcams obs, royalcams external encoder, royalcams rtmp, royal cams",
        "h1html": 'Como transmitir no <span class="accent">RoyalCams</span> com SplitCam',
        "h1short": "Transmitir no RoyalCams",
        "card": "Setup do encoder externo pro site cam por token do RoyalCams.",
        "intro": "O RoyalCams é um site cam grátis baseado em token — salas públicas abertas bancadas por tips, com shows privados por cima. As configurações de transmissão suportam um caminho padrão de <strong>External Encoder</strong> ao qual o <strong style='color:var(--text)'>SplitCam</strong> grátis conecta, pra você transmitir com cenas multicâmera, overlays e filtros de beleza no lugar de uma única webcam plana.",
        "quick": "Transmitir no RoyalCams com SplitCam: instala o SplitCam, monta sua cena, no seu painel de modelo abre <em>broadcast settings → external encoder</em>, copia a URL do servidor e a stream key, cola no SplitCam e dá Go Live."
                 "<ol><li>Instala o SplitCam.</li><li>Adiciona câmera + cena.</li>"
                 "<li>Pega URL e stream key no painel.</li>"
                 "<li>Cola no SplitCam.</li>"
                 "<li>Aperta Go Live.</li></ol>",
        "key_how": "Entra na sua conta de modelo do RoyalCams e abre a seção de <strong>broadcast settings / external encoder</strong>. Ela mostra uma <strong>URL do servidor</strong> e uma <strong>stream key</strong> vinculadas à sua conta — copia as duas pros campos de RTMP personalizado do SplitCam. A verificação de modelo é obrigatória antes de transmitir.",
        "tips": [
            ("Salas de token premiam produção", "As salas públicas do RoyalCams rodam em tips — overlays de meta de tip e uma cena caprichada convertem quem só observa em quem dá tip e fecha shows privados."),
            ("Converte em shows privados", "Usa uma cena pública forte pra fazer upsell de shows privados, onde está o dinheiro de verdade nos sites cam por token."),
            ("O encoder externo libera as cenas", "Passar pelo RTMP do SplitCam, e não pela cam do navegador, habilita layouts multicâmera, overlays e filtros."),
            _T_ETH,
        ],
        "faq": [
            ("O RoyalCams suporta encoders externos tipo o SplitCam?", "Suporta — as configurações de transmissão têm um caminho padrão de external encoder / RTMP. Copia a URL do servidor e a stream key pro SplitCam depois da verificação."),
            ("Onde pego minha stream key do RoyalCams?", "Nas configurações de broadcast / external encoder do seu painel de modelo — a URL do servidor e a stream key aparecem ali. Cola as duas nos campos de RTMP personalizado do SplitCam."),
            ("Que bitrate usar no RoyalCams?", "Manda 1920×1080 a 30 fps, 3.500–6.000 Kbps com keyframe de 2 segundos. Roda primeiro o speed test do SplitCam."),
            ("O SplitCam é grátis pra usar com o RoyalCams?", "É — o SplitCam é grátis, sem marca d'água e sem limite de tempo. A opção de encoder externo do RoyalCams é grátis no painel."),
        ],
        "steps": [
            ("Baixa e instala o SplitCam",
             "O SplitCam é um software de live streaming grátis pra Windows e macOS — sem cadastro, sem cartão, sem marca d'água."),
            ("Monta sua cena",
             "Abre o SplitCam e adiciona sua webcam. Encaixa overlays, texto de meta de tip, uma segunda câmera ou o celular, filtros de beleza ou fundo IA."),
            ("Pega a URL e a stream key do RoyalCams",
             "Entra na sua conta de modelo do RoyalCams, abre <strong>broadcast settings → external encoder</strong> e copia a <strong>URL do servidor</strong> e a <strong>stream key</strong>."),
            ("Conecta o SplitCam ao RoyalCams",
             "No SplitCam abre <strong>Stream Settings</strong>, cola a URL do servidor do RoyalCams e a stream key nos campos de RTMP personalizado. Põe o bitrate em 3.500–6.000 Kbps a 1920×1080, 30 fps, com keyframe de 2 segundos."),
            ("Clica Go Live",
             "Aperta <strong>Go Live</strong> no SplitCam e depois fica online pelo painel. Em uns 10 segundos seu stream chega ao público do RoyalCams."),
        ],
    },
    {
        "slug": "modelhub", "name": "Modelhub",
        "title": "Transmitir no Modelhub com SplitCam — External Encoder",
        "desc": "Transmita no Modelhub Live com SplitCam grátis — encoder externo da plataforma de criadores do Pornhub, cenas multicâmera e overlays. Sem marca d'água.",
        "kw": "como transmitir no modelhub, modelhub, modelhub live, modelhub obs, modelhub external encoder, modelhub rtmp, modelhub cam",
        "h1html": 'Como transmitir no <span class="accent">Modelhub</span> com SplitCam',
        "h1short": "Transmitir no Modelhub",
        "card": "Setup do encoder externo pro Modelhub Live (Pornhub).",
        "intro": "O Modelhub é a plataforma de criadores do Pornhub — venda de vídeos, assinaturas de fãs e um produto de <strong>live cam</strong> com tráfego enorme no topo do funil vindo da rede Pornhub. O painel de modelo suporta um caminho padrão de <strong>External Encoder</strong> ao qual o <strong style='color:var(--text)'>SplitCam</strong> grátis conecta, pra você transmitir com cenas multicâmera, overlays e filtros de beleza.",
        "quick": "Transmitir no Modelhub com SplitCam: instala o SplitCam, monta sua cena, no painel de modelo abre <em>Live → broadcast / external encoder</em>, copia a URL do servidor e a stream key, cola no SplitCam e dá Go Live."
                 "<ol><li>Instala o SplitCam.</li><li>Adiciona câmera + cena.</li>"
                 "<li>Pega URL e stream key no painel.</li>"
                 "<li>Cola no SplitCam.</li>"
                 "<li>Aperta Go Live.</li></ol>",
        "key_how": "Entra na sua conta de modelo do Modelhub e abre as configurações de <strong>Live / broadcast / external encoder</strong> no painel. A página mostra uma <strong>URL do servidor</strong> e uma <strong>stream key</strong> vinculadas à sua conta — copia as duas pros campos de RTMP personalizado do SplitCam. A verificação de modelo na rede é obrigatória antes de entrar ao vivo.",
        "tips": [
            ("Tráfego enorme no topo do funil", "O Modelhub puxa espectadores da rede Pornhub — uma cena caprichada no SplitCam converte esse público grande e casual em espectadores ao vivo pagantes e assinantes."),
            ("Faz venda cruzada dos seus vídeos", "Usa overlays pra direcionar quem assiste ao vivo pros seus vídeos e assinatura do Modelhub — a plataforma é feita pra esse funil."),
            ("O encoder externo libera as cenas", "Passar pelo RTMP do SplitCam, e não pela cam básica, habilita layouts multicâmera, overlays e filtros."),
            _T_ETH,
        ],
        "faq": [
            ("O Modelhub suporta encoders externos tipo o SplitCam?", "Suporta — o painel de modelo tem um caminho padrão de external encoder / RTMP pro Modelhub Live. Copia a URL do servidor e a stream key pro SplitCam depois da verificação."),
            ("Onde pego minha stream key do Modelhub?", "Nas configurações de Live / broadcast / external encoder do painel — a URL do servidor e a stream key aparecem ali. Cola as duas nos campos de RTMP personalizado do SplitCam."),
            ("Que bitrate usar no Modelhub?", "Manda 1920×1080 a 30 fps, 3.500–6.000 Kbps com keyframe de 2 segundos. Roda primeiro o speed test do SplitCam."),
            ("O SplitCam é grátis pra usar com o Modelhub?", "É — o SplitCam é grátis, sem marca d'água e sem limite de tempo. A opção de encoder externo do Modelhub é grátis no painel."),
        ],
        "steps": [
            ("Baixa e instala o SplitCam",
             "O SplitCam é um software de live streaming grátis pra Windows e macOS — sem cadastro, sem cartão, sem marca d'água."),
            ("Monta sua cena",
             "Abre o SplitCam e adiciona sua webcam. Encaixa overlays, texto, uma segunda câmera ou o celular, filtros de beleza ou fundo IA."),
            ("Pega a URL e a stream key do Modelhub",
             "Entra na sua conta de modelo do Modelhub, abre <strong>Live → broadcast / external encoder</strong> e copia a <strong>URL do servidor</strong> e a <strong>stream key</strong>."),
            ("Conecta o SplitCam ao Modelhub",
             "No SplitCam abre <strong>Stream Settings</strong>, cola a URL do servidor do Modelhub e a stream key nos campos de RTMP personalizado. Põe o bitrate em 3.500–6.000 Kbps a 1920×1080, 30 fps, com keyframe de 2 segundos."),
            ("Clica Go Live",
             "Aperta <strong>Go Live</strong> no SplitCam e depois fica online pelo painel. Em uns 10 segundos seu stream chega ao público do Modelhub."),
        ],
    },
    {
        "slug": "xhamsterlive", "name": "xHamsterLive",
        "title": "Transmitir no xHamsterLive com SplitCam — RTMP/OBS",
        "desc": "Transmita no xHamsterLive com SplitCam grátis via RTMP — cenas multicâmera, overlays e filtros. Pegue o tráfego mainstream do xHamster, sem marca d'água.",
        "kw": "como transmitir no xhamsterlive, xhamsterlive, xhamsterlive obs, xhamsterlive rtmp, xhamsterlive broadcast, xhamsterlive modelo, xhamster live cam, xhamsterlive stream key",
        "h1html": 'Como transmitir no <span class="accent">xHamsterLive</span> com SplitCam',
        "h1short": "Transmitir no xHamsterLive",
        "card": "SplitCam grátis → stream RTMP/OBS pro xHamsterLive.",
        "intro": "O xHamsterLive é o braço de live cam do xHamster — mesma tecnologia de broadcaster do Stripchat, mas canalizada pelo tráfego mainstream do xHamster, uma das maiores bases de espectadores do adulto. As modelos transmitem pelo <strong>Studio</strong> do xHamsterLive, que aceita tanto o broadcaster da webcam no navegador quanto um <strong>encoder externo via RTMP</strong>. Com o <strong style='color:var(--text)'>SplitCam</strong> grátis você transmite como encoder externo pra ter cenas multicâmera, overlays e filtros — ou, se preferir transmitir pelo navegador, aponta o xHamsterLive pro SplitCam como <strong>câmera virtual</strong> pro mesmo efeito.",
        "quick": "Transmitir no xHamsterLive com SplitCam: instala o SplitCam, monta a cena, copia a URL do servidor e a stream key do Studio do xHamsterLive, cola nos campos de RTMP do SplitCam e dá Go Live."
                 "<ol><li>Instala o SplitCam.</li><li>Adiciona câmera + cena.</li>"
                 "<li>Copia URL + stream key do Studio do xHamsterLive → External Encoder.</li>"
                 "<li>Cola no RTMP personalizado do SplitCam.</li>"
                 "<li>Clica Go Live.</li></ol>",
        "key_how": "O Studio do xHamsterLive mostra pro broadcaster uma aba de <strong>encoder externo</strong> com URL do servidor e stream key. Cola as duas no SplitCam em <strong>Stream Settings → Custom RTMP</strong>; escolhe 4.000–6.000 Kbps a 1920×1080, 30 fps, keyframe de 2 segundos. Aperta <strong>Go Live</strong> no SplitCam e depois entra online pelo Studio. Se preferir o broadcaster do navegador, abre ele e escolhe <strong>SplitCam</strong> na lista de câmeras — sua cena composta substitui a webcam crua.",
        "tips": [
            ("Tráfego do xHamster, motor do Stripchat", "Mesma ferramenta de broadcaster do Stripchat (painel Studio, menu de tips, Lovense), mas com o funil mainstream do xHamster — chega na sua sala um mix de público diferente."),
            ("Usa encoder externo sempre que der", "O RTMP do SplitCam dá bitrate estável e cenas multicâmera/overlays completas; o broadcaster do navegador funciona, mas limita a composição."),
            ("Tip menu converte público mainstream", "Muitos visitantes do xHamster são novos em cam — um tip menu limpo na tela e uma barra de meta deixam claro o que esperar e elevam a conversão."),
            _T_TEST,
        ],
        "faq": [
            ("O xHamsterLive é o mesmo que o Stripchat?", "Roda no motor de broadcaster do Stripchat, mas a marca e a fonte de tráfego são diferentes — o xHamster canaliza o público mainstream pra cá, então o perfil de espectador difere de quem cadastra direto no Stripchat."),
            ("Onde pego a stream key do xHamsterLive?", "No Studio do xHamsterLive, abre o painel de <em>Broadcast</em> ou <em>External Encoder</em> — a URL do servidor e a stream key aparecem ali. Cola as duas nos campos de RTMP personalizado do SplitCam."),
            ("Broadcaster do navegador ou RTMP?", "Encoder externo (RTMP) é o preferido pra quem leva a sério — bitrate estável e cenas completas do SplitCam. O broadcaster do navegador também serve: escolhe o SplitCam como webcam."),
            ("O SplitCam é grátis pra usar com o xHamsterLive?", "É — o SplitCam é grátis, sem marca d'água e sem limite de tempo."),
        ],
        "steps": [
            ("Baixa e instala o SplitCam", "O SplitCam é um software de live streaming grátis pra Windows e macOS — sem cadastro, sem cartão, sem marca d'água."),
            ("Monta sua cena", "Abre o SplitCam e adiciona a webcam. Encaixa overlays, tip menu, uma segunda câmera ou o celular, filtros de beleza ou fundo com IA — tudo ao vivo."),
            ("Pega a URL do Studio do xHamsterLive + key", "Entra no xHamsterLive, abre o Studio, troca pra <strong>External Encoder</strong> e copia a <strong>URL do servidor</strong> e sua <strong>stream key</strong>."),
            ("Conecta o SplitCam ao xHamsterLive", "No SplitCam → <strong>Stream Settings → Custom RTMP</strong>, cola a URL e a key. Põe 4.000–6.000 Kbps a 1920×1080, 30 fps, keyframe de 2 segundos."),
            ("Clica Go Live", "Aperta <strong>Go Live</strong> no SplitCam e depois fica online pelo Studio do xHamsterLive. Em uns 10 segundos seu stream cai na lista pública."),
        ],
    },
    {
        "slug": "premium-chat", "name": "Premium.Chat",
        "title": "Usar o SplitCam no Premium.Chat — Chamadas Pagas",
        "desc": "Use o SplitCam grátis como câmera virtual no Premium.Chat — aceite chamadas pagas por minuto com cenas multicâmera, overlays e filtros. Sem marca d'água.",
        "kw": "como usar splitcam no premium chat, premium chat, premium chat video call, premium chat câmera virtual, premium.chat por minuto, premium chat modelo, premium chat consultor, premium chat live",
        "h1html": 'Como usar o SplitCam no <span class="accent">Premium.Chat</span>',
        "h1short": "Premium.Chat com SplitCam",
        "card": "Usa o SplitCam como câmera virtual nas chamadas pagas do Premium.Chat.",
        "intro": "O Premium.Chat é uma plataforma paga por minuto: você define a sua tarifa por minuto pra chat, voz ou <strong>chamadas de vídeo</strong>, compartilha seu link pessoal, e o cliente paga pra falar com você. As chamadas rodam no navegador, então o <strong style='color:var(--text)'>SplitCam</strong> grátis encaixa direto como <strong>câmera virtual</strong> — cenas multicâmera, overlays, filtros de iluminação e fundo com IA chegam até quem ligou sem mudar o jeito de usar o Premium.Chat.",
        "quick": "Usar o SplitCam no Premium.Chat: instala o SplitCam, monta uma cena limpa pra chamadas de vídeo, aceita uma chamada que entrar no Premium.Chat e, no seletor de câmera da chamada, escolhe <em>SplitCam</em>."
                 "<ol><li>Instala o SplitCam.</li><li>Monta a cena (boa luz, overlay opcional).</li>"
                 "<li>Define sua tarifa por minuto no Premium.Chat.</li>"
                 "<li>Aceita a chamada de vídeo que entrar.</li>"
                 "<li>Escolhe SplitCam como câmera.</li></ol>",
        "key_how": "As chamadas do Premium.Chat rodam no navegador. O SplitCam instala uma webcam virtual chamada <strong>\"SplitCam Video Driver\"</strong> — quando a chamada começa, clica no menu do ícone de câmera na janela do Premium.Chat e troca da sua webcam embutida pro <strong>SplitCam</strong>. Sua cena composta (câmera real + overlays + filtros) vira o que o cliente vê.",
        "tips": [
            ("Premium.Chat é por minuto, não é streaming", "Diferente de salas estilo Chaturbate com tip, aqui você é paga por minuto. Luz suave, áudio claro e fundo com IA parecem mais uma consulta premium do que cam pública."),
            ("Divulga o seu link, não um perfil", "O Premium.Chat te dá um link pessoal pra você jogar nas redes, na bio do OnlyFans ou num Linktree — é assim que o cliente te encontra."),
            ("Overlays só se ajudarem", "Em chamada 1-a-1, overlay pesado distrai. Usa o SplitCam pela qualidade de câmera, luz e fundo — mantém a tela majoritariamente em você."),
            _T_TEST,
        ],
        "faq": [
            ("Como o SplitCam conecta no Premium.Chat?", "Como câmera virtual. As chamadas do Premium.Chat rodam no navegador; escolhe o SplitCam no seletor de câmera da chamada — sem stream key, sem RTMP."),
            ("O Premium.Chat suporta OBS?", "O Premium.Chat é baseado em navegador, então o OBS encaixa do mesmo jeito que o SplitCam — via câmera virtual. O SplitCam é a opção mais leve, grátis e sem marca d'água."),
            ("Dá pra usar uma segunda câmera ou overlay no Premium.Chat?", "Dá — monta a cena no SplitCam (segunda câmera, overlays, filtros) e o Premium.Chat enxerga uma única webcam. Vai com moderação em 1-a-1."),
            ("O SplitCam é grátis?", "É — grátis, sem marca d'água e sem limite de tempo."),
        ],
        "steps": [
            ("Baixa e instala o SplitCam", "O SplitCam é um software de live streaming grátis pra Windows e macOS — sem cadastro, sem cartão, sem marca d'água. Ele instala uma câmera virtual que o navegador consegue usar."),
            ("Monta sua cena pra chamadas", "Abre o SplitCam, adiciona a webcam, ajusta a luz e, se quiser, põe um fundo com IA ou um overlay discreto. Mantém o enquadramento limpo — é chamada paga, não palco."),
            ("Define sua tarifa no Premium.Chat", "Entra no Premium.Chat, define sua tarifa por minuto pra chamada de vídeo e copia seu link pessoal. Compartilha nas redes ou em bios."),
            ("Aceita a chamada de vídeo que entrar", "Quando o cliente paga pelo tempo, a chamada entra. Aceita pelo painel do Premium.Chat."),
            ("Escolhe o SplitCam como câmera", "No menu do ícone de câmera da janela da chamada, troca da webcam embutida pro <strong>SplitCam</strong>. Sua cena composta agora chega ao cliente."),
        ],
    },
    {
        "slug": "arousr", "name": "Arousr",
        "title": "Usar o SplitCam no Arousr — Sexting e Vídeo Chat",
        "desc": "Use o SplitCam grátis como câmera virtual no vídeo chat do Arousr — cenas multicâmera, overlays e filtros pra sexting, voz e vídeo pagos. Sem marca d'água.",
        "kw": "como usar splitcam no arousr, arousr, arousr video chat, arousr câmera virtual, arousr cam girl, arousr modelo, plataforma de sexting splitcam, arousr live",
        "h1html": 'Como usar o SplitCam no <span class="accent">Arousr</span>',
        "h1short": "Arousr com SplitCam",
        "card": "Usa o SplitCam como câmera virtual no vídeo chat do Arousr.",
        "intro": "O Arousr é uma plataforma paga de <strong>sexting + voz + vídeo chat</strong> — os clientes compram créditos pra mandar mensagem, falar ou fazer vídeo com modelos, e você é paga por sessão. O lado de vídeo roda no navegador (ou no app mobile do Arousr no celular), então o <strong style='color:var(--text)'>SplitCam</strong> grátis conecta como <strong>câmera virtual</strong> no desktop: cenas multicâmera, overlays, filtros de iluminação e fundo com IA vão direto pro cliente.",
        "quick": "Usar o SplitCam no Arousr: instala o SplitCam, monta a cena, aceita um pedido de vídeo que entrar no Arousr e, no seletor de câmera, escolhe <em>SplitCam</em>."
                 "<ol><li>Instala o SplitCam.</li><li>Monta cena + iluminação.</li>"
                 "<li>Define suas tarifas de sexting/vídeo no Arousr.</li>"
                 "<li>Aceita o pedido de vídeo que entrar.</li>"
                 "<li>Escolhe SplitCam na lista de câmeras.</li></ol>",
        "key_how": "O vídeo web do Arousr roda no navegador. O SplitCam instala uma webcam virtual chamada <strong>\"SplitCam Video Driver\"</strong> — quando começa uma sessão de vídeo no painel do Arousr, troca a câmera na janela da sessão pro <strong>SplitCam</strong>. A cena composta (câmera + overlays + filtros) vira o que o cliente vê. No app mobile do Arousr câmera virtual não funciona — usa a câmera real do celular ali e deixa o SplitCam pras sessões no desktop.",
        "tips": [
            ("Sessões são pagas por tempo", "Os clientes compram créditos por minuto (ou por mensagem no texto). Vídeo caprichado — boa luz, fundo com IA, filtro de beleza — se paga em sessões mais longas."),
            ("Sexting primeiro, vídeo como upsell", "A maior parte da grana do Arousr vem do texto. Uma prévia em vídeo curtinha durante um sexting empurra o cliente pra uma sessão de vídeo completa — é ali que a tarifa por minuto entra."),
            ("Sessão no app mobile ≠ desktop", "Câmera virtual funciona no vídeo do navegador no desktop. O app mobile do Arousr usa a câmera do celular direto — mesmo fluxo, ferramenta diferente."),
            _T_TEST,
        ],
        "faq": [
            ("Como o SplitCam conecta no Arousr?", "Como câmera virtual. O vídeo chat do Arousr roda no navegador no desktop — escolhe o SplitCam no seletor de câmera. Não precisa de stream key."),
            ("O Arousr suporta OBS?", "O Arousr é baseado em navegador, então o OBS encaixa do mesmo jeito que o SplitCam — via câmera virtual. O SplitCam é a opção grátis e sem marca d'água."),
            ("Dá pra usar overlays numa sessão de sexting + vídeo?", "Dá — monta a cena no SplitCam (luz, overlay, segunda câmera) e o Arousr enxerga uma única webcam. Vai leve com overlay no 1-a-1."),
            ("O SplitCam é grátis pra usar com o Arousr?", "É — grátis, sem marca d'água e sem limite de tempo."),
        ],
        "steps": [
            ("Baixa e instala o SplitCam", "O SplitCam é um software de live streaming grátis pra Windows e macOS — sem cadastro, sem cartão, sem marca d'água. Ele instala uma câmera virtual que o navegador consegue selecionar."),
            ("Monta sua cena", "Abre o SplitCam, adiciona a webcam, ajusta a luz e, se quiser, põe um fundo com IA ou filtro de beleza. Mantém o clima intimista — é sessão 1-a-1 paga, não palco público."),
            ("Define suas tarifas no Arousr", "Entra no Arousr, define sua tarifa por mensagem e por minuto de vídeo, e confere se seu perfil está aprovado pra receber pedidos."),
            ("Aceita o pedido de vídeo que entrar", "Quando o cliente abre uma sessão de vídeo (pelo sexting ou direto), aceita pelo painel do Arousr."),
            ("Escolhe o SplitCam como câmera", "Na lista de câmeras da janela da sessão, troca da webcam embutida pro <strong>SplitCam</strong>. Sua cena composta agora chega ao cliente."),
        ],
    },
    {
        "slug": "cams-com", "name": "Cams.com",
        "title": "Transmitir no Cams.com com SplitCam — RTMP/OBS",
        "desc": "Transmita no Cams.com com SplitCam grátis via RTMP — cenas multicâmera, overlays e filtros. Alcance a base pagante do AFF. Sem marca d'água.",
        "kw": "como transmitir no cams.com, cams.com, cams.com obs, cams.com rtmp, cams.com modelo, cams.com broadcaster, cams.com stream key, adult friend finder cams, cams com modelo cadastro",
        "h1html": 'Como transmitir no <span class="accent">Cams.com</span> com SplitCam',
        "h1short": "Transmitir no Cams.com",
        "card": "SplitCam grátis → stream RTMP pra rede Cams.com / AFF.",
        "intro": "O Cams.com é o braço cam da rede AdultFriendFinder — um dos ecossistemas mais antigos de namoro + cam online, com uma base considerável de <strong>membros que já pagam</strong> chegando do AFF, do AmateurMatch e de outras propriedades da FriendFinder. As modelos transmitem pelo <strong>Model Center</strong> do Cams.com, que aceita tanto o broadcaster do navegador quanto um <strong>encoder externo via RTMP</strong>. O <strong style='color:var(--text)'>SplitCam</strong> grátis transmite via RTMP pra entregar cenas multicâmera, overlays e filtros completos — ou, no broadcaster do navegador, registra como <strong>câmera virtual</strong> pro mesmo resultado.",
        "quick": "Transmitir no Cams.com: instala o SplitCam, monta a cena, pega a URL do servidor RTMP e a stream key do Model Center, cola no SplitCam e dá Go Live."
                 "<ol><li>Instala o SplitCam.</li><li>Adiciona câmera + cena.</li>"
                 "<li>Copia URL + key do Model Center do Cams.com → External Encoder.</li>"
                 "<li>Cola no RTMP personalizado do SplitCam.</li>"
                 "<li>Clica Go Live.</li></ol>",
        "key_how": "O Model Center do Cams.com tem uma aba de <strong>External Encoder / OBS</strong> com URL do servidor e stream key. Cola as duas no SplitCam em <strong>Stream Settings → Custom RTMP</strong>; escolhe 3.500–5.000 Kbps a 1920×1080, 30 fps, keyframe de 2 segundos. Aperta <strong>Go Live</strong> no SplitCam e depois começa seu show pelo Model Center. Se preferir o broadcaster no navegador, escolhe <strong>SplitCam</strong> na lista de câmeras.",
        "tips": [
            ("Cross-traffic do AFF = membros pagantes", "O Cams.com puxa público de contas do AdultFriendFinder que já têm método de pagamento cadastrado — diferente de um público recém-cadastrado. A conversão pra privado e tip costuma ser mais alta."),
            ("Encoder externo bate o navegador", "O RTMP do SplitCam dá bitrate limpo e cenas multicâmera com overlays; o broadcaster do navegador funciona, mas limita a produção."),
            ("Usa as ferramentas de show privado", "O Cams.com se apoia em sessões privadas/exclusivas. Um tip menu e um caminho claro pro privado (em overlay) elevam a receita por espectador bastante."),
            _T_TEST,
        ],
        "faq": [
            ("O Cams.com é o mesmo que o AdultFriendFinder?", "Mesma rede mãe. O Cams.com é a marca de broadcast cam; o espectador pode chegar pelo AFF, AmateurMatch e outros sites da FriendFinder, e isso é uma parte grande do tráfego."),
            ("Onde pego a stream key do Cams.com?", "No Model Center do Cams.com, abre a aba <em>External Encoder</em> ou <em>OBS</em> — a URL do servidor e a stream key aparecem ali. Cola as duas nos campos de RTMP personalizado do SplitCam."),
            ("Broadcaster do navegador ou RTMP?", "RTMP (encoder externo) é o preferido — bitrate estável e cenas completas do SplitCam. O broadcaster do navegador serve como fallback: escolhe o SplitCam como webcam."),
            ("O SplitCam é grátis pra usar com o Cams.com?", "É — o SplitCam é grátis, sem marca d'água e sem limite de tempo."),
        ],
        "steps": [
            ("Baixa e instala o SplitCam", "O SplitCam é um software de live streaming grátis pra Windows e macOS — sem cadastro, sem cartão, sem marca d'água."),
            ("Monta sua cena", "Abre o SplitCam e adiciona a webcam. Encaixa overlays, tip menu, uma segunda câmera ou o celular, filtros de beleza ou fundo com IA — tudo ao vivo."),
            ("Pega a URL do Cams.com + stream key", "Entra no Model Center do Cams.com, abre a aba <strong>External Encoder / OBS</strong> e copia a <strong>URL do servidor</strong> e a <strong>stream key</strong>."),
            ("Conecta o SplitCam ao Cams.com", "No SplitCam → <strong>Stream Settings → Custom RTMP</strong>, cola a URL e a key. Põe 3.500–5.000 Kbps a 1920×1080, 30 fps, keyframe de 2 segundos."),
            ("Clica Go Live", "Aperta <strong>Go Live</strong> no SplitCam e depois fica online pelo Model Center. Em uns 10 segundos seu stream cai na rede Cams.com / AFF."),
        ],
    },
    {
        "slug": "stripcamfun", "name": "StripCamFun",
        "title": "Transmitir no StripCamFun com SplitCam — RTMP/OBS",
        "desc": "Transmita no StripCamFun com SplitCam grátis via RTMP — cenas multicâmera, overlays e filtros pra um público indie. Sem marca d'água, sem cadastro.",
        "kw": "como transmitir no stripcamfun, stripcamfun, stripcamfun obs, stripcamfun rtmp, stripcamfun modelo, stripcamfun broadcast, strip cam fun cadastro modelo, stripcamfun stream key, site cam indie obs",
        "h1html": 'Como transmitir no <span class="accent">StripCamFun</span> com SplitCam',
        "h1short": "Transmitir no StripCamFun",
        "card": "SplitCam grátis → stream RTMP/OBS pro StripCamFun.",
        "intro": "O StripCamFun é um site de live cam independente — menor que os gigantes do nível do Chaturbate, mas com um público real, menos saturado, e bem menos concorrência de broadcaster por nicho. As modelos transmitem pelo painel de modelo do StripCamFun, que mostra uma opção de <strong>encoder externo / RTMP</strong>. O <strong style='color:var(--text)'>SplitCam</strong> grátis conecta via RTMP pra entregar cenas multicâmera, overlays e filtros completos — e onde tem broadcaster no navegador, o SplitCam também registra como <strong>câmera virtual</strong>.",
        "quick": "Transmitir no StripCamFun: instala o SplitCam, monta a cena, copia a URL do servidor e a stream key do StripCamFun, cola no SplitCam e dá Go Live."
                 "<ol><li>Instala o SplitCam.</li><li>Adiciona câmera + cena.</li>"
                 "<li>Copia URL + stream key do painel de modelo do StripCamFun → External Encoder.</li>"
                 "<li>Cola no RTMP personalizado do SplitCam.</li>"
                 "<li>Clica Go Live.</li></ol>",
        "key_how": "Abre o painel de modelo do StripCamFun e a seção <strong>External Encoder / OBS</strong>. Copia a URL do servidor e sua stream key pro SplitCam em <strong>Stream Settings → Custom RTMP</strong>; põe 3.500–5.000 Kbps a 1920×1080, 30 fps, keyframe de 2 segundos. Aperta <strong>Go Live</strong> no SplitCam e depois fica online pelo painel.",
        "tips": [
            ("Pool menor, mais fácil aparecer", "Num site Tier-1 você é uma entre milhares online; no StripCamFun a lista de broadcaster é curta — uma cena caprichada do SplitCam se destaca mais rápido na home."),
            ("Cross-broadcast pra alcance", "Sites cam indie casam bem com multi-streaming. Usa o SplitCam pra transmitir simultaneamente pro StripCamFun e pra um site maior pra capturar tipper dos dois lados."),
            ("Investe na tag de nicho", "Público indie busca mais por nicho do que por estrela. Tags específicas + um overlay de cena que nomeia o nicho puxam o espectador da listagem."),
            _T_TEST,
        ],
        "faq": [
            ("Onde pego a stream key do StripCamFun?", "No painel de modelo, abre a aba <em>External Encoder / OBS</em> — a URL do servidor e a stream key aparecem ali. Cola as duas nos campos de RTMP personalizado do SplitCam."),
            ("É seguro transmitir no StripCamFun?", "Como em qualquer site cam indie, confere o contrato de modelo e os termos de pagamento antes de entrar ao vivo. Usa um e-mail real e valida seu método de pagamento primeiro."),
            ("Dá pra fazer multi-stream pro StripCamFun e outro site cam?", "Dá — o SplitCam consegue enviar pra vários endpoints de RTMP personalizado ao mesmo tempo. Confere as regras de exclusividade de cada site antes."),
            ("O SplitCam é grátis pra usar com o StripCamFun?", "É — grátis, sem marca d'água e sem limite de tempo."),
        ],
        "steps": [
            ("Baixa e instala o SplitCam", "O SplitCam é um software de live streaming grátis pra Windows e macOS — sem cadastro, sem cartão, sem marca d'água."),
            ("Monta sua cena", "Abre o SplitCam e adiciona a webcam. Encaixa overlays, tip menu, uma segunda câmera ou o celular, filtros de beleza ou fundo com IA — tudo ao vivo."),
            ("Pega a URL do StripCamFun + stream key", "Entra no painel de modelo do StripCamFun, abre <strong>External Encoder / OBS</strong> e copia a <strong>URL do servidor</strong> e a <strong>stream key</strong>."),
            ("Conecta o SplitCam ao StripCamFun", "No SplitCam → <strong>Stream Settings → Custom RTMP</strong>, cola a URL e a key. Põe 3.500–5.000 Kbps a 1920×1080, 30 fps, keyframe de 2 segundos."),
            ("Clica Go Live", "Aperta <strong>Go Live</strong> no SplitCam e depois fica online pelo painel do StripCamFun. Em uns 10 segundos seu stream cai na lista pública."),
        ],
    },
    {
        "slug": "mym-fans", "name": "MYM.fans",
        "title": "Transmitir ao Vivo no MYM.fans com SplitCam — Câmera Virtual",
        "desc": "Transmita ao vivo no MYM.fans (a alternativa francesa ao OnlyFans) com SplitCam grátis como câmera virtual — cenas, overlays e filtros. Sem marca d'água.",
        "kw": "como transmitir no mym, mym.fans live, mym fans câmera virtual, mym criador, mym france, mym live stream, mym obs, mym fans broadcast, mym influencer",
        "h1html": 'Como transmitir ao vivo no <span class="accent">MYM.fans</span> com SplitCam',
        "h1short": "Ao vivo no MYM.fans",
        "card": "Usa o SplitCam como câmera virtual no live do MYM.fans.",
        "intro": "O MYM.fans é a maior plataforma francesa de assinatura pra criadores — a resposta da França pro OnlyFans, com assinaturas, pay-per-view, tip e um recurso de <strong>live stream</strong> embutido pros fãs. O broadcaster roda no navegador, então apontar o <strong style='color:var(--text)'>SplitCam</strong> grátis pro MYM como <strong>câmera virtual</strong> adiciona cenas multicâmera, overlays e filtros por cima da webcam comum. Se o painel de criadora liberar a opção de encoder externo, o SplitCam também conecta via RTMP.",
        "quick": "Transmitir ao vivo no MYM.fans com SplitCam: instala o SplitCam, monta a cena, começa um live no MYM e, no seletor de câmera do broadcaster, escolhe <em>SplitCam</em> — depois fica ao vivo."
                 "<ol><li>Instala o SplitCam.</li><li>Adiciona câmera + cena.</li><li>Começa um live no MYM.fans.</li><li>Escolhe SplitCam no menu de câmera.</li><li>Go Live.</li></ol>",
        "key_how": "O live do MYM.fans roda no navegador. Monta a cena no SplitCam — ele registra como uma webcam chamada <strong>\"SplitCam Video Driver\"</strong> — depois abre o broadcaster do MYM e escolhe o <strong>SplitCam</strong> no menu de câmera. Se aparecer a opção de <strong>stream key / encoder externo</strong> no seu painel, cola nos campos de RTMP personalizado do SplitCam.",
        "tips": [
            ("Maior plataforma de criadores da França", "O MYM é a fan platform #1 na França, com um público francês/europeu acostumado a pagar em EUR. Uma cena caprichada do SplitCam com overlays em francês converte mais que uma webcam pelada."),
            ("Câmera virtual funciona sem stream key", "O live só pelo navegador ainda entrega a cena completa do SplitCam — segunda câmera, overlays, filtro de beleza ou fundo com IA — só escolhendo o SplitCam como webcam."),
            ("Vende PPV durante o live", "O MYM é construído em cima de conteúdo pago. Overlays na tela divulgando sua assinatura ou destravando mensagens PPV transformam quem tá no live em assinante pagante."),
            _T_TEST,
        ],
        "faq": [
            ("Como o SplitCam conecta no MYM.fans?", "O live do MYM é baseado em navegador, então o SplitCam conecta como câmera virtual — escolhe o SplitCam no seletor de câmera. Não precisa de stream key."),
            ("Dá pra usar overlays e várias câmeras no MYM?", "Dá — monta a cena no SplitCam (segunda câmera, overlays, fundo com IA); o MYM vê a cena pronta como uma única webcam."),
            ("O MYM.fans suporta OBS ou encoder externo?", "O live é principalmente via navegador/webcam. Se o seu painel mostrar a opção de stream key, cola nos campos de RTMP personalizado do SplitCam; senão, usa o método de câmera virtual."),
            ("O SplitCam é grátis pra usar com o MYM.fans?", "É — o SplitCam é grátis, sem marca d'água e sem limite de tempo."),
        ],
        "steps": [
            ("Baixa e instala o SplitCam", "O SplitCam é um software de live streaming grátis pra Windows e macOS — sem cadastro, sem cartão, sem marca d'água. Ele instala uma câmera virtual que o navegador consegue selecionar."),
            ("Monta sua cena", "Abre o SplitCam e adiciona a webcam. Encaixa overlays, texto (em francês se seu público for FR), uma segunda câmera ou o celular, filtros de beleza ou fundo com IA."),
            ("Começa um live no MYM.fans", "Entra na sua conta de criadora do MYM e abre o broadcaster pra começar uma transmissão pros assinantes."),
            ("Escolhe o SplitCam como câmera", "No menu de câmera do MYM, troca da webcam crua pro <strong>SplitCam</strong> — sua cena composta substitui a câmera achatada. (Ou cola uma stream key nos campos de RTMP personalizado do SplitCam se disponível.)"),
            ("Go Live", "Começa a transmissão — sua cena do SplitCam, com overlays e filtros, chega nos assinantes do MYM."),
        ],
    },
    {
        "slug": "fc2-live", "name": "FC2 Live",
        "title": "Transmitir no FC2 Live com SplitCam (RTMP/OBS)",
        "desc": "Transmita no FC2 Live (maior site cam do Japão) com SplitCam grátis via RTMP — cenas multicâmera, overlays e filtros. Sem marca d'água, sem cadastro.",
        "kw": "como transmitir no fc2 live, fc2 live obs, fc2 live rtmp, fc2 live broadcast, fc2 live配信, fc2 live stream key, fc2 live modelo, fc2 live japão, fc2 ライブ",
        "h1html": 'Como transmitir no <span class="accent">FC2 Live</span> com SplitCam',
        "h1short": "Transmitir no FC2 Live",
        "card": "SplitCam grátis → stream RTMP/OBS pro FC2 Live.",
        "intro": "O FC2 Live é a maior plataforma de live streaming do Japão — base de espectadores enorme, uma seção adulta dedicada e um fluxo separado de paid-show que faz dele um dos mercados cam mais lucrativos da Ásia. As modelos transmitem pelo painel de broadcaster do FC2, que suporta tanto o broadcaster do navegador quanto um <strong>encoder externo via RTMP</strong>. O <strong style='color:var(--text)'>SplitCam</strong> grátis transmite via RTMP pra entregar cenas multicâmera, overlays e filtros completos.",
        "quick": "Transmitir no FC2 Live com SplitCam: instala o SplitCam, monta a cena, copia a URL do servidor e a stream key do painel de broadcaster do FC2, cola no RTMP do SplitCam e clica Go Live."
                 "<ol><li>Instala o SplitCam.</li><li>Adiciona câmera + cena.</li><li>Copia URL + stream key do painel de broadcaster do FC2.</li><li>Cola no RTMP personalizado do SplitCam.</li><li>Clica Go Live.</li></ol>",
        "key_how": "Abre o painel de broadcaster do FC2 Live e troca pro modo <strong>External Encoder / RTMP</strong>. Copia a URL do servidor e sua stream key pro SplitCam em <strong>Stream Settings → Custom RTMP</strong>; põe 3.500–5.000 Kbps a 1920×1080, 30 fps, keyframe de 2 segundos. Aperta <strong>Go Live</strong> no SplitCam e depois começa o show pelo painel do FC2.",
        "tips": [
            ("Público japonês gigante", "O FC2 é Tier 1 no Japão — espectadores locais, acostumados a pagar em JPY e que curtem shows pagos mais longos. Overlay em japonês (ex: tip menu em 円 / JPY) levanta a conversão de forma considerável."),
            ("A seção adulta é separada", "O FC2 tem lives gerais e adultos. Define a categoria certa antes de ficar ao vivo — show adulto não aparece pra quem tá navegando na seção geral."),
            ("Usa encoder externo pra bitrate estável", "O público japonês é majoritariamente mobile e sente cada quadro que cai. RTMP do SplitCam num bitrate firme de 4 Mbps bate o broadcaster do navegador em confiabilidade."),
            _T_TEST,
        ],
        "faq": [
            ("Onde pego a stream key do FC2 Live?", "No painel de broadcaster do FC2 Live, troca pra <em>External Encoder</em> ou <em>OBS</em> — a URL do servidor e a stream key aparecem ali. Cola as duas nos campos de RTMP personalizado do SplitCam."),
            ("Broadcaster do navegador ou RTMP?", "RTMP (encoder externo) é o preferido — bitrate estável, cenas completas do SplitCam. O broadcaster do navegador serve como fallback: escolhe o SplitCam como webcam."),
            ("Precisa de uma conta japonesa pra transmitir no FC2?", "Precisa de uma conta FC2, e transmissão adulta tem passos extras de verificação de idade pra modelo. Segue o onboarding do FC2."),
            ("O SplitCam é grátis pra usar com o FC2 Live?", "É — o SplitCam é grátis, sem marca d'água e sem limite de tempo."),
        ],
        "steps": [
            ("Baixa e instala o SplitCam", "O SplitCam é um software de live streaming grátis pra Windows e macOS — sem cadastro, sem cartão, sem marca d'água."),
            ("Monta sua cena", "Abre o SplitCam e adiciona a webcam. Encaixa overlays, um tip menu em 円 (JPY), uma segunda câmera ou o celular, filtros de beleza ou fundo com IA — tudo ao vivo."),
            ("Pega sua URL do FC2 Live + stream key", "Entra no FC2, abre o painel de broadcaster do Live, troca pra <strong>External Encoder</strong> e copia a <strong>URL do servidor</strong> e sua <strong>stream key</strong>."),
            ("Conecta o SplitCam ao FC2 Live", "No SplitCam → <strong>Stream Settings → Custom RTMP</strong>, cola a URL e a key. Põe 3.500–5.000 Kbps a 1920×1080, 30 fps, keyframe de 2 segundos."),
            ("Clica Go Live", "Aperta <strong>Go Live</strong> no SplitCam e depois começa o show pelo painel do FC2. Em uns 10 segundos seu stream cai na lista pública."),
        ],
    },
    {
        "slug": "boosty", "name": "Boosty",
        "title": "Transmitir ao Vivo no Boosty com SplitCam — Câmera Virtual",
        "desc": "Transmita ao vivo no Boosty (plataforma russa de criadores) com SplitCam grátis como câmera virtual — cenas, overlays e filtros. Sem marca d'água.",
        "kw": "como transmitir no boosty, boosty live, boosty stream, boosty câmera virtual, boosty criador, бусти прямой эфир, boosty obs, boosty live pago, boosty assinante",
        "h1html": 'Como transmitir ao vivo no <span class="accent">Boosty</span> com SplitCam',
        "h1short": "Ao vivo no Boosty",
        "card": "Usa o SplitCam como câmera virtual no live do Boosty.",
        "intro": "O Boosty é a maior plataforma de monetização pra criadores da Rússia — um serviço estilo Patreon com assinaturas, posts pagos, tips e um recurso de <strong>transmissão ao vivo</strong>, com um público de criadores que vai do mainstream ao adulto. O live roda no navegador, então conectar o <strong style='color:var(--text)'>SplitCam</strong> grátis como <strong>câmera virtual</strong> adiciona cenas multicâmera, overlays e filtros que os assinantes não teriam com uma webcam comum.",
        "quick": "Transmitir ao vivo no Boosty com SplitCam: instala o SplitCam, monta a cena, começa um live no Boosty e escolhe <em>SplitCam</em> no seletor de câmera do broadcaster — depois fica ao vivo."
                 "<ol><li>Instala o SplitCam.</li><li>Adiciona câmera + cena.</li><li>Começa um live no Boosty.</li><li>Escolhe SplitCam no menu de câmera.</li><li>Go Live.</li></ol>",
        "key_how": "O live do Boosty roda no navegador. Monta a cena no SplitCam — ele registra como uma webcam chamada <strong>\"SplitCam Video Driver\"</strong> — depois abre o broadcaster do Boosty e escolhe o <strong>SplitCam</strong> no menu de câmera no lugar da sua webcam crua.",
        "tips": [
            ("Maior plataforma de criadores da Rússia", "O Boosty substituiu o Patreon pra muito criador russo depois das sanções, então o público é fiel e acostumado a pagar em RUB. Uma cena caprichada do SplitCam com overlays em russo converte bem."),
            ("Lives por nível de assinatura", "O Boosty deixa você restringir live por tier de assinante. O SplitCam funciona com todos os tiers — o encoder não tá nem aí pro nível do espectador, você transmite uma vez e o Boosty cuida do acesso."),
            ("Overlay de tip e pay-per-view", "O Boosty suporta posts pagos pra destravar e tips. Um overlay na tela mencionando as vantagens do tier sobe a conversão durante o live."),
            _T_TEST,
        ],
        "faq": [
            ("Como o SplitCam conecta no Boosty?", "O live do Boosty é baseado em navegador, então o SplitCam conecta como câmera virtual — escolhe o SplitCam no seletor de câmera. Não precisa de stream key."),
            ("Dá pra usar overlays num live do Boosty?", "Dá — monta a cena no SplitCam (overlays, segunda câmera, fundo com IA); o Boosty enxerga uma única webcam. Os assinantes recebem a cena composta inteira."),
            ("O Boosty suporta OBS ou encoder externo?", "O live do Boosty é principalmente via navegador. Se aparecer uma opção de stream key no seu painel de criadora, cola nos campos de RTMP personalizado do SplitCam; senão, usa o método de câmera virtual."),
            ("O SplitCam é grátis pra usar com o Boosty?", "É — o SplitCam é grátis, sem marca d'água e sem limite de tempo."),
        ],
        "steps": [
            ("Baixa e instala o SplitCam", "O SplitCam é um software de live streaming grátis pra Windows e macOS — sem cadastro, sem cartão, sem marca d'água. Ele instala uma câmera virtual que o navegador consegue selecionar."),
            ("Monta sua cena", "Abre o SplitCam e adiciona a webcam. Encaixa overlays (em russo pro seu público), uma segunda câmera ou o celular, filtros de beleza ou fundo com IA."),
            ("Começa um live no Boosty", "Entra na sua conta de criadora do Boosty e abre o broadcaster. Configura o tier gating se quiser deixar o live só pra quem paga um nível específico."),
            ("Escolhe o SplitCam como câmera", "No menu de câmera do Boosty, troca da webcam crua pro <strong>SplitCam</strong> — sua cena composta substitui a câmera achatada."),
            ("Go Live", "Começa a transmissão — sua cena do SplitCam, com overlays e filtros, chega nos assinantes do Boosty."),
        ],
    },
    {
        "slug": "amateurcommunity", "name": "AmateurCommunity",
        "title": "Transmitir no AmateurCommunity com SplitCam (RTMP)",
        "desc": "Transmita no AmateurCommunity (maior site amador da Alemanha) com SplitCam grátis via RTMP — cenas multicâmera, overlays e filtros. Sem marca d'água.",
        "kw": "como transmitir no amateurcommunity, amateurcommunity obs, amateurcommunity rtmp, amateur community deutschland, amateurcommunity modelo, ac community broadcast, amateurcommunity live, amateur cam deutschland",
        "h1html": 'Como transmitir no <span class="accent">AmateurCommunity</span> com SplitCam',
        "h1short": "Transmitir no AmateurCommunity",
        "card": "SplitCam grátis → stream RTMP pro AmateurCommunity (DE).",
        "intro": "O AmateurCommunity é a maior comunidade de cam e conteúdo amador da Alemanha — no ar desde o começo dos anos 2000, com um público de língua alemã super fiel e acostumado a pagar por conteúdo e show ao vivo. As modelos transmitem pelo painel de modelo do AC, que suporta um <strong>encoder externo via RTMP</strong> além do broadcaster do navegador. O <strong style='color:var(--text)'>SplitCam</strong> grátis transmite via RTMP pra entregar cenas multicâmera, overlays e filtros completos — overlays em alemão falam direto com o público local.",
        "quick": "Transmitir no AmateurCommunity: instala o SplitCam, monta a cena, copia a URL do servidor e a stream key do AC pelo painel de modelo, cola no RTMP do SplitCam e clica Go Live."
                 "<ol><li>Instala o SplitCam.</li><li>Adiciona câmera + cena.</li><li>Copia URL + stream key do painel de modelo do AC.</li><li>Cola no RTMP personalizado do SplitCam.</li><li>Clica Go Live.</li></ol>",
        "key_how": "Abre o painel de modelo do AmateurCommunity e a aba <strong>External Encoder / OBS</strong>. Copia a URL do servidor e sua stream key pro SplitCam em <strong>Stream Settings → Custom RTMP</strong>; põe 3.500–5.000 Kbps a 1920×1080, 30 fps, keyframe de 2 segundos. Aperta <strong>Go Live</strong> no SplitCam e depois fica online pelo painel.",
        "tips": [
            ("Público de fala alemã, paga em alemão", "O público do AmateurCommunity é maciçamente DACH (DE/AT/CH) e paga em EUR — overlays, tip menu e chat na tela em alemão convertem bem mais que em inglês."),
            ("PPV premium + combo de live", "O AC deixa você vender conteúdo PPV junto com live. Um show ao vivo que dá uma prévia do PPV (com overlay na tela) costuma puxar as vendas de PPV durante e depois da transmissão."),
            ("Encoder externo pra qualidade estável", "O público do AC espera produção alta; RTMP firme em 4 Mbps do SplitCam bate o bitrate variável do broadcaster do navegador."),
            _T_TEST,
        ],
        "faq": [
            ("Onde pego a stream key do AmateurCommunity?", "No painel de modelo do AC, abre a aba <em>External Encoder</em> ou <em>OBS</em> — a URL do servidor e a stream key aparecem ali. Cola as duas nos campos de RTMP personalizado do SplitCam."),
            ("Broadcaster do navegador ou RTMP?", "RTMP (encoder externo) é o preferido pra modelo profissional — bitrate estável, cenas completas do SplitCam. O broadcaster do navegador serve como fallback: escolhe o SplitCam como webcam."),
            ("Preciso estar na Alemanha pra transmitir no AC?", "Não, mas o público é de língua alemã. Modelos de qualquer lugar podem se cadastrar — passar a verificação de modelo + os formulários de imposto é o passo principal."),
            ("O SplitCam é grátis pra usar com o AmateurCommunity?", "É — o SplitCam é grátis, sem marca d'água e sem limite de tempo."),
        ],
        "steps": [
            ("Baixa e instala o SplitCam", "O SplitCam é um software de live streaming grátis pra Windows e macOS — sem cadastro, sem cartão, sem marca d'água."),
            ("Monta sua cena", "Abre o SplitCam e adiciona a webcam. Encaixa overlays (em alemão — \"Trinkgeld\" / \"PPV freischalten\"), uma segunda câmera ou o celular, filtros de beleza ou fundo com IA — tudo ao vivo."),
            ("Pega sua URL do AmateurCommunity + stream key", "Entra no painel de modelo do AC, abre <strong>External Encoder / OBS</strong> e copia a <strong>URL do servidor</strong> e a <strong>stream key</strong>."),
            ("Conecta o SplitCam ao AmateurCommunity", "No SplitCam → <strong>Stream Settings → Custom RTMP</strong>, cola a URL e a key. Põe 3.500–5.000 Kbps a 1920×1080, 30 fps, keyframe de 2 segundos."),
            ("Clica Go Live", "Aperta <strong>Go Live</strong> no SplitCam e depois fica online pelo painel de modelo do AC. Em uns 10 segundos seu stream cai na lista pública."),
        ],
    },
]
