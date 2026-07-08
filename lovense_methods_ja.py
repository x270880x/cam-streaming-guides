# -*- coding: utf-8 -*-
LOVENSE_METHODS_JA = {
    "heading": "SplitCamでLovenseを設定する — 3ステップ",
    "lead": "これはLovense公式の3ステップ設定をそのまま再現したものです。<strong>Cam Extension</strong>が"
            "配信サイトの投げ銭を読み取り、<strong>Lovense Connect</strong>がトイへのBluetooth"
            "ブリッジとなり、<strong>SplitCam Toolset</strong>がLovenseのオーバーレイをSplitCam内に"
            "表示し、SplitCamがRTMPで配信します。すべて無料で、ダウンロードボタンはお使いの"
            "システムに自動で合わせて表示されます。",
    "stage_word": "ステップ",
    "get_label": "ダウンロード",
    "do_label": "次に",
    "stages": [
        {
            "title": "Lovense Cam Extension",
            "role": "配信サイトから投げ銭を読み取ります — ChromeまたはEdgeにインストールします。",
            "get": ["camext"],
            "steps": [
                "Cam Extensionをダウンロードして解凍します。",
                "<strong>chrome://extensions</strong>（または<strong>edge://extensions</strong>）を開き、"
                "右上の<strong>Developer mode</strong>をオンにして、<strong>Load unpacked</strong>を"
                "クリックし、解凍した<em>lovense_cam</em>フォルダを選択します。",
                "ツールバーのLovenseアイコンをクリックし、Lovenseアカウントでログインします。",
            ],
        },
        {
            "title": "Lovense Connect",
            "role": "Bluetooth経由でトイと通信するブリッジです。",
            "get": ["connect"],
            "steps": [
                "パソコンの場合：Lovense Connectをインストールします（Lovense USB Bluetoothアダプターの"
                "使用を推奨します）。スマホの場合：Google PlayまたはApp StoreからLovense Connectアプリを"
                "入手します。",
                "トイの電源を入れ、接続済みと表示されるまでConnectでペアリングします。スマホアプリでは、"
                "パソコンに表示されたQRコードをスキャンして連携させます。",
            ],
        },
        {
            "title": "SplitCam + Toolset",
            "role": "SplitCamにLovenseのオーバーレイを表示し、配信を行います。",
            "get": ["splitcam", "toolset"],
            "steps": [
                "SplitCamをインストールし、続いてLovense SplitCam Toolset — SplitCamにLovenseの"
                "オーバーレイを追加するプラグイン — をインストールします。",
                "Cam Extensionで<strong>+</strong>をクリックして配信サイト（Chaturbate、Stripchatなど）を"
                "追加し、投げ銭メニューを設定します。次に<strong>Video Feedback</strong>タブを開き、"
                "リスト（OBS / SplitCam / Streamster）から<strong>SplitCam</strong>を選択します。",
                "SplitCamで、Toolsetが登録した<strong>Lovense</strong>ソースを追加します — 投げ銭メニュー／"
                "トイの状態を示すオーバーレイがシーンに表示されます。他のレイヤーより上に配置してください。",
                "カメラを追加し、配信サイトのRTMPキーをSplitCamの<strong>Stream Settings</strong>に貼り付け、"
                "<strong>Go Live</strong>をクリックします — オーバーレイとトイが投げ銭に反応します。",
            ],
        },
    ],
}
