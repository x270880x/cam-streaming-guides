# Extra FAQ templates appended to every platform guide.
# Captures high-volume informational queries (earnings / safety / signup / mobile)
# that aren't covered by the platform-specific 4-FAQ block in platforms_<lang>.py.
#
# Format: "common" entries apply to all platforms; "stream" or "vcam" picks one
# based on the platform's METHOD. {name} is substituted with the platform's display name.

FAQ_EXTRA_JA = {
    "common": [
        (
            "{name}でモデルはどれくらい稼げますか？",
            "{name}での収入は視聴者数、配信時間、投げ銭の状況によって変動します。"
            "アクティブな配信者の月収は通常2万〜30万円程度で、トップ層は100万円以上に達します。"
            "あなたの取り分は{name}の手数料体系に従うため、配信開始前にモデル契約書を必ず確認してください。"
        ),
        (
            "{name}は配信者にとって安全ですか？",
            "{name}は出金前に年齢と本人確認を必須としており、これがモデルを詐欺から守ります。"
            "ステージネームを使い、カメラの前で個人情報を絶対に明かさず、ジオブロック機能で自宅地域から配信を隠し、"
            "視聴者からのリクエストはすべて取引として扱ってください。"
            "SplitCamのオーバーレイやAI背景機能を使えば、実際の周囲の様子を隠したり差し替えたりすることもできます。"
        ),
        (
            "{name}でモデル登録するにはどんな書類が必要ですか？",
            "{name}では通常、政府発行の写真付き身分証（パスポート、運転免許証、マイナンバーカードなど）、"
            "その身分証を持った自撮り写真、そして税務・支払い用フォーム（米国居住者はW-9、それ以外はW-8BEN）が必要です。"
            "審査は通常24〜72時間で完了し、承認されればその日のうちに配信を開始できます。"
        ),
        (
            "{name}にスマホから配信できますか？",
            "{name}には大抵モバイル配信アプリかモバイルウェブ配信ツールが用意されていますが、"
            "オーバーレイなし、セカンドカメラなし、AI背景なしと機能が制限されます。"
            "本格的な配信品質を求めるなら、パソコンからSplitCamで配信し、スマホはセカンドカメラとして使うのがおすすめです"
            "（SplitCamはスマホからのIPカメラ入力に対応しています）。"
        ),
    ],
    "stream": (
        "{name}はOBSや外部エンコーダーに対応していますか？",
        "はい、対応しています。{name}の配信者パネルにRTMPサーバーURLとストリームキーが表示されます。"
        "両方をSplitCamの<strong>配信設定 → カスタムRTMP</strong>に貼り付け、"
        "1920×1080の30fps、ビットレート4,000〜5,000Kbpsに設定して<strong>配信開始</strong>をクリックしてください。"
        "カスタムRTMP経由ならSplitCamのシーン合成機能（マルチカメラ、オーバーレイ、フィルター）をフル活用できます。"
    ),
    "vcam": (
        "{name}でSplitCamを仮想カメラとして使えますか？",
        "はい、使えます。{name}の配信はブラウザ上で動作するため、SplitCamは"
        "<strong>「SplitCam Video Driver」</strong>という名前のウェブカメラとして認識されます。"
        "{name}の配信画面を開き、ブラウザのカメラ選択メニューからSplitCamを選んでください。"
        "合成済みのシーン（オーバーレイ、セカンドカメラ、フィルター、AI背景）が一本のウェブカメラ映像として視聴者に届きます。"
    ),
}
