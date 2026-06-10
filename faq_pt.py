# Extra FAQ templates appended to every platform guide.
# Captures high-volume informational queries (earnings / safety / signup / mobile)
# that aren't covered by the platform-specific 4-FAQ block in platforms_<lang>.py.
#
# Format: "common" entries apply to all platforms; "stream" or "vcam" picks one
# based on the platform's METHOD. {name} is substituted with the platform's display name.

FAQ_EXTRA_PT = {
    "common": [
        (
            "Quanto as criadoras ganham no {name}?",
            "Os ganhos no {name} dependem do tamanho do público, das horas ao vivo e do volume de "
            "gorjetas. Criadoras ativas costumam levar para casa de R$ 1.000 a R$ 15.000 por mês; "
            "as top performers chegam a R$ 50.000+. Sua porcentagem segue a comissão do {name} — "
            "leia o contrato de modelo antes de entrar ao vivo."
        ),
        (
            "O {name} é seguro para quem transmite?",
            "O {name} exige verificação de idade e documento antes de liberar o pagamento, o que "
            "protege a criadora contra fraudes. Use um nome artístico, nunca mostre dados pessoais "
            "na câmera, ative bloqueio geográfico para esconder a transmissão da sua região e trate "
            "todo pedido de assinante como transacional. Os overlays e o fundo com IA do SplitCam "
            "também escondem ou substituem o ambiente real."
        ),
        (
            "Quais documentos eu preciso para virar modelo no {name}?",
            "O {name} geralmente pede um documento oficial com foto (RG, CNH ou passaporte), uma "
            "selfie segurando o documento e o formulário fiscal/de pagamento (W-9 para EUA, W-8BEN "
            "fora dos EUA; no Brasil costumam aceitar CPF para receber via PIX por gateway). A "
            "aprovação leva de 24 a 72 horas; aprovada, você já entra ao vivo no mesmo dia."
        ),
        (
            "Dá para transmitir no {name} pelo celular?",
            "O {name} normalmente oferece um app de transmissão ou um broadcaster mobile pelo "
            "navegador, mas a experiência é limitada — sem overlays, sem segunda câmera, sem fundo "
            "com IA. Para qualidade de produção completa, transmita pelo computador com o SplitCam "
            "e use o celular como segunda câmera (o SplitCam aceita entrada de câmera IP a partir "
            "do celular)."
        ),
    ],
    "stream": (
        "O {name} aceita OBS ou encoder externo?",
        "Sim — o {name} disponibiliza uma URL de servidor RTMP e uma chave de transmissão no painel "
        "da criadora. Cole as duas em <strong>Stream Settings → Custom RTMP</strong> do SplitCam, "
        "configure 1920×1080 a 30 fps com bitrate de 4.000 a 5.000 Kbps e clique em "
        "<strong>Go Live</strong>. A rota Custom RTMP libera a composição de cena completa do "
        "SplitCam (multicâmera, overlays, filtros)."
    ),
    "vcam": (
        "Posso usar o SplitCam como câmera virtual no {name}?",
        "Sim — o ao vivo do {name} roda no navegador, então o SplitCam aparece como uma webcam "
        "chamada <strong>\"SplitCam Video Driver\"</strong>. Abra o broadcaster do {name}, clique "
        "no seletor de câmera do navegador e escolha SplitCam. Sua cena composta (overlays, segunda "
        "câmera, filtros, fundo com IA) chega aos assinantes como um único sinal de webcam."
    ),
}
