# -*- coding: utf-8 -*-
LOVENSE_METHODS_PT = {
    "heading": "Configure o Lovense no SplitCam — 3 passos",
    "lead": "Isto reproduz a própria configuração em três passos da Lovense. A <strong>Cam Extension</strong> "
            "lê as gorjetas do seu site de cam, o <strong>Lovense Connect</strong> é a ponte Bluetooth até o "
            "seu brinquedo, e o <strong>SplitCam Toolset</strong> coloca a sobreposição da Lovense dentro do "
            "SplitCam, que transmite via RTMP. Tudo é gratuito; os botões de download reconhecem o seu sistema "
            "automaticamente.",
    "stage_word": "Passo",
    "get_label": "Baixar",
    "do_label": "Depois",
    "stages": [
        {
            "title": "Lovense Cam Extension",
            "role": "Lê as gorjetas do seu site de cam — instala no Chrome ou Edge.",
            "get": ["camext"],
            "steps": [
                "Baixe a Cam Extension e descompacte-a.",
                "Abra <strong>chrome://extensions</strong> (ou <strong>edge://extensions</strong>), "
                "ative o <strong>Developer mode</strong> no canto superior direito, clique em <strong>Load unpacked</strong> "
                "e selecione a pasta <em>lovense_cam</em> descompactada.",
                "Clique no ícone da Lovense na barra de ferramentas e faça login com a sua conta Lovense.",
            ],
        },
        {
            "title": "Lovense Connect",
            "role": "A ponte que se comunica com o seu brinquedo via Bluetooth.",
            "get": ["connect"],
            "steps": [
                "No computador: instale o Lovense Connect (recomenda-se um adaptador Bluetooth USB da Lovense). "
                "No celular: baixe o app Lovense Connect na Google Play ou na App Store.",
                "Ligue o seu brinquedo e pareie-o no Connect até aparecer como conectado. No app do celular, "
                "escaneie o QR code exibido no computador para vinculá-los.",
            ],
        },
        {
            "title": "SplitCam + Toolset",
            "role": "Mostra a sobreposição da Lovense no SplitCam e transmite o seu stream.",
            "get": ["splitcam", "toolset"],
            "steps": [
                "Instale o SplitCam e, em seguida, instale o Lovense SplitCam Toolset — o plugin que adiciona "
                "a sobreposição da Lovense ao SplitCam.",
                "Na Cam Extension, clique em <strong>+</strong> para adicionar o seu site de cam (Chaturbate, "
                "Stripchat, …) e configure o seu menu de gorjetas, depois abra a aba <strong>Video Feedback</strong> "
                "e escolha <strong>SplitCam</strong> na lista (OBS / SplitCam / Streamster).",
                "No SplitCam, adicione a fonte <strong>Lovense</strong> que o Toolset registrou — a sobreposição "
                "de menu de gorjetas / status do brinquedo aparece na sua cena. Mantenha-a acima das outras camadas.",
                "Adicione a sua câmera, cole a chave RTMP do seu site de cam nas <strong>Stream Settings</strong> "
                "do SplitCam e clique em <strong>Go Live</strong> — a sobreposição e o brinquedo reagem às gorjetas.",
            ],
        },
    ],
}
