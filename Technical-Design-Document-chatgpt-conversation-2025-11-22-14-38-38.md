# [https://chatgpt.com/c/692135c9-ab38-8322-8d3a-6d3d9c46516b](https://chatgpt.com/c/692135c9-ab38-8322-8d3a-6d3d9c46516b)

Date: 2025-11-22T05:38:38.641Z Messages: 2

---

# あなた:

1人で120人分のコード品質をどう改善するか？ミノ駆動氏に聞くMCPサーバー「モディフィウス」の開発秘話 2025年11月20日 合同会社DMM.com プラットフォーム開発本部 エンジニア ミノ駆動 大手電機からWeb業界へ転身。 リファクタリングやアーキテクチャ改善、若手の設計スキル育成といった、設計全般を推進する業務に従事。暇さえあれば脳内でリファクタリングしている。『良いコード／悪いコードで学ぶ設計入門』の著者。 X：@MinoDriven 技術的負債の分析と解消は多くの開発組織が直面する課題です。しかし、その対応は属人化しやすく、専門家のリソース不足からスケールさせるのが困難な場合も少なくありません。120名以上の開発組織のコード品質改善を1人で担うミノ駆動氏も、このスケーラビリティの壁に直面していました。 本記事は、ミノ駆動氏が開発したMCPサーバー「モディフィウス」についての発表内容を再構成したものです。モディフィウスはどのような仕組みで高精度の負債分析と設計改善を実現したのか、その開発経緯と効果、今後の展望をお届けします。 keyboard_arrow_down 増大する技術的負債に立ち向かう「コード品質チーム」 keyboard_arrow_down 「AI分身」の開発で挑む、120人超えチームのコード品質改善 keyboard_arrow_down コードの意図を理解した負債分析と設計改善 keyboard_arrow_down MCPサーバーの実態は「私の思考を模倣する」プロンプト群 keyboard_arrow_down 負債の苦しみから人類を解放する日まで 増大する技術的負債に立ち向かう「コード品質チーム」 合同会社DMM.comは、DMMテレビやゲームズ、通販など、多様なサービスを展開しています。これらのサービスを下支えしているのが「DMMプラットフォーム」という、会員ID管理、決済処理、ユーザーレビュー管理など、DMMサービス全体で共通利用される技術基盤です。このプラットフォームは、基盤ごとに開発チームが編成されており、関わる開発者の人数は120名以上にのぼります。 一方で、サービス規模の拡大に伴い、このプラットフォームは年々コードの品質が悪化し負債が増大していました。この問題を解決するために立ち上げたのが「コード品質チーム」です。 正式名称は「プラットフォーム開発本部第3開発部 Developer Productivity Group コード品質チーム」。開発生産性を改善する手段は多岐にわたりますが、「コード品質の改善でソフトウェア生産性向上を図る」をミッションとしています。 ここでいう「コード品質」とは、コードの変更容易性を指します。変更容易性とは、なるべくバグを埋め込まず、素早く正確にコード変更できる度合いのことです。変更容易性に問題のあるコードは、些細な変更でバグが埋め込まれやすいため、修正には慎重な検討を要します。その結果、コードの修正に時間がかかり、開発生産性の低下につながってしまうのです。 変更容易性の高い設計を実現するために、コード品質チームはDMMプラットフォーム全体に対し多角的な支援を行っています。例えば、設計ガイドラインの策定、設計スキルの育成支援、各開発チームへの直接的な設計指導など、コード品質の向上に関わるさまざまな施策を推進しています。 「AI分身」の開発で挑む、120人超えチームのコード品質改善 こうした取り組みによって、基盤全体のコードの品質は徐々に改善しつつはありました。しかしです。 コード品質チームであるにもかかわらず、なんとメンバーは私1人しかいなかったのです。 私自身は、もっと多くのチームに対して設計支援したいと考えていましたが、正直なところ全く手が回らないのです。 だからいつも思っていました。 「わい、100人ぐらいに増えないかな」 「せや、AIにわいの分身やらせればいい」と。 この着想から開発したのが、MCPサーバー「モディフィウス（Modifius）」です。 モディフィウスは、変更容易性に関して包括的な支援機能を提供するMCPサーバーで、CursorやClaudeCodeといったAIエージェントと連携して使用します。 現状では、高精度な技術負債の分析や負債に対する設計改善の提案、高品質なテストコードの実装といった機能を中心に提供しています。 なおこの名前は、変更容易性を意味する英語「Modifiability」と、ラテン語で威厳のある男性名の語尾である「-ius」を合わせ、「変化を司る者」という意味を込めています。 コードの意図を理解した負債分析と設計改善 従来の負債分析に使われる静的解析ツールの分析観点は、行数やコード重複の有無、引数の数など、コードから機械的に判断できる情報のみでした。なぜなら、静的解析ツールでは、コードの「意図」までは分からないからです。 それだけでは当然十分な分析だとは言えません。一方で、生成AIはコードの書かれた背景を推論し、意図を理解した上でカプセル化や技術レイヤ間の関心の分離など、高精度な負債分析ができるのです。 一例として、私の著書『良いコード／悪いコードで学ぶ設計入門』の改訂新版で取り上げている品質の悪いコードを、モディフィウスで分析させたケースをご紹介します。 このコードは、ゲームにおけるダメージ計算のロジックを記述したもので、複数目的のコードが混在しています。モディフィウスは、これらの概念を全て洗い出した上で、関心の分離という観点から「武器の耐久性に関するロジックのコード」や「スペシャルゲージに関するコード」が混在していると指摘。また、目的が異なるコードがちゃんとそれぞれカプセル化されてないこともはっきりと分析しています。 ▲右側にある「欠陥スコア」の欄。近年の負債に関する学術論文のデータに基づいた独自の計算式で負債の深刻さをスコアリングする機能も備えています モディフィウスの分析能力は質も量もかなり優れています。400行程度のソースコードの負債を洗いざらい分析しようとした場合、私が目視で調べると熟知するドメインだと速くても15分、ドメイン理解が浅ければ30分ほどかかってしまいます。 しかしモディフィウスだと、私とほぼ同じ精度で、約20秒で完了します。なんと40倍以上の生産性で分析できているのです。さらにいまは、GitHub Actionsからモディフィウスを呼び出し、負債を定期的に計測する基盤も整備しています。 現在、DMMのエンジニア全員がモディフィウスを使える状態になっています。この分析機能について、実際に利用したエンジニアからは、「巨大クラス内で複数のユースケースが混在していることを指摘してくれた」「インフラの関心ごとがアプリケーションに混在していることも指摘してくれた」といった声や、「人間と違って、同じことを聞いても怒られないので気持ちが楽だった」というような、AIならではの利点も挙げられています。 負債分析のほか、見つけた負債に対する設計改善の提案機能も優れています。どのように改善すべきかを尋ねると、Mermaidのクラス図を含め、適切な改善案が出力されます。この設計改善機能についても「どう分割し、ビジネスロジックがどのドメインになるか、クラスの相関図をつくってくれて、正直この通りにリファクタリングするだけでも負債の解消にかなり効果あると感じた」「設計提案内容が現実的で、600行あったファイルを300行までスリム化できた」「改善後のドメインモデル図も分かりやすくレビュー時に話がしやすかった」といった、具体的な成果報告が届いています。 MCPサーバーの実態は「私の思考を模倣する」プロンプト群 わざわざMCPサーバーとして用意しなくても、AIに普通に指示するだけでも上述の機能を実現できるのでは、と疑問を持つ人もいるかもしれません。しかし、AIは学習内容の平均に収斂する性質があって、ネット上の粗悪なコードも学習してしまっているのです。粗悪な学習内容に基づいた回答をしてくるということも、少なくありません。高品質な回答を引き出すには、適切なプロンプトを与える必要があります。モディフィウスの実態は、まさに変更容易性を高めるプロンプト群です。 モディフィウスは柔軟な機能拡張ができるように徹底的なモジュール化が図られています。心臓部分は「コアプロンプト」となっていて、私の変更容易性に関する思考を模倣した内容が入っています。コアプロンプトの中身は企業秘密ですので内容は明かせませんが、私のミノ駆動本がベースになっています。こうしたコアプロンプトをベースに、様々な支援機能が機能しています。さらに、新しいアーキテクチャやフレームワークの設計観点が容易に追加したり、対応するプログラミング言語を増やしたりすることも容易にできる構造になっています。 実は、最初からMCPサーバーを構築していたわけではなく、AIエージェント用のカスタムプロンプトを提供していました。しかしその場合、都度プロンプトを手動更新するという煩わしさがありました。 また、同じことはClaudeCodeなどのエージェントスキルでも実現できます。ただ、そうしてしまうと、この機能は特定のAIエージェントに強く結合してしまい、複数AIエージェントで使えなくなってしまいます。横断的に提供する手段として、MCPサーバーがふさわしいと判断し提供しております。 負債の苦しみから人類を解放する日まで モディフィウスは今後さらなる機能拡張を計画しており、その開発も着々と進められています。その中でも私が最も実現したいのは「自動リファクタリング機能」です。テストコードの実装は、もはや人間の仕事ではなくなっていると思います。AIの実装精度は、すでに明らかに人間を上回っています。同じように、リファクタリングもほとんどAIにお任せできる日が来るのではないでしょうか。 モディフィウスは今後、現在のMCPサーバーという形態から「AIエージェント化」することも構想しています。AIエージェントにできれば、DMM社内での利用に留まらず、より広く利用される形にできるのではないかと考えています。もしかしたら皆さんも、広く利用できる形に、できるのではないかと考えています。もし、自動リファクタリング機能を備えたモディフィウスが、日本だけでなく世界中で使われるようになるという形になれば、負債の苦しみから、いよいよ人類が解放される日が来るのではないかと期待しています。 MCP コード品質 技術負債 上記内容を調査して、その真偽と反証・反論をして記録。その記録を読んでベストプラクティスを調査し、その真偽と反証・反論をしてください。最終的にオリジナルかつ冒頭の記事以上の内容をもつMCPツールを作成するための開発者向けの技術資料を網羅的に作成する2/2

---

# ChatGPT:

（専門領域：ソフトウェア設計・MCP・AI評価、専門知識：技術的負債・静的解析・LLM推論設計、専門職：ソフトウェアアーキテクト）

# Ⅰ. 事実認定ログ（一次情報の確認）

- 「モディフィウス」はQiita Conf 2025 Autumn登壇資料で正式言及がある。登壇者はDMM.comのミノ駆動氏である。[Speaker Deck](https://speakerdeck.com/minodriven/modifius)

- 資料には「AIエージェント用MCPサーバー」「負債分析と設計改善提案を提供」と明記される。該当スライド画像で確認済み。[files.speakerdeck.com](https://files.speakerdeck.com/presentations/7a9468d99f8d443ea37be87d82dbb3aa/slide_8.jpg)

- 「独自計算式に基づく負債スコアリング」機能の図表が提示される。[files.speakerdeck.com](https://files.speakerdeck.com/presentations/7a9468d99f8d443ea37be87d82dbb3aa/slide_32.jpg)

- 静的解析との観点比較や、カプセル化・関心分離等の設計観点で分析する主張が含まれる。[files.speakerdeck.com](https://files.speakerdeck.com/presentations/7a9468d99f8d443ea37be87d82dbb3aa/slide_30.jpg)

- 「約400行を約20秒で分析し、人手比40倍以上」との定量比較がスライドに記載される。条件として「Cursor2.0＋Composer1」を注記する。[files.speakerdeck.com](https://files.speakerdeck.com/presentations/7a9468d99f8d443ea37be87d82dbb3aa/slide_34.jpg)

- GitHub Actionsで定期計測基盤を整備中との図表が示される。[files.speakerdeck.com](https://files.speakerdeck.com/presentations/7a9468d99f8d443ea37be87d82dbb3aa/slide_35.jpg)

- 実態は「変更容易性を高めるプロンプト群」と説明される。[files.speakerdeck.com](https://files.speakerdeck.com/presentations/7a9468d99f8d443ea37be87d82dbb3aa/slide_42.jpg)

- MCP自体はAnthropic提唱の公開規格であり、CursorとClaude Codeが公式にサポートする。[code.claude.com+3Anthropic+3Model Context Protocol+3](https://www.anthropic.com/news/model-context-protocol?utm_source=chatgpt.com)

- DMM内でのDeveloper Productivity Groupの存在は社内ブログ等に記載がある。[inside.dmm.com+1](https://inside.dmm.com/articles/code-rank/?utm_source=chatgpt.com)

# Ⅱ. 真偽判定と反証・反論

## 命題A：モディフィウスはMCPサーバーとして負債分析と設計改善を提供する

**判定：真**。登壇資料で明示され、具体画面も提示される。[files.speakerdeck.com+1](https://files.speakerdeck.com/presentations/7a9468d99f8d443ea37be87d82dbb3aa/slide_8.jpg)

**補足反論**

- 汎用LLMは出力の揺らぎと幻覚を持つため、単独判断は危険である。設計観点の自動評価は再現性確保が難題である。学術的にもコード生成や解析での幻覚は体系的に報告される。[arXiv+1](https://arxiv.org/abs/2404.00971?utm_source=chatgpt.com)

## 命題B：「約400行を約20秒、ほぼ同精度、人手比40倍以上」

**判定：一次資料としての主張は確認**。スライドに数値が明示される。[files.speakerdeck.com](https://files.speakerdeck.com/presentations/7a9468d99f8d443ea37be87d82dbb3aa/slide_34.jpg)

**補足反証**

- 外部同条件の再現データは未提示で統計的検定も無い。入力分布やモデル・プロンプトの改版で容易に変動する。比較の妥当性は第三者評価で要検証である。

## 命題C：静的解析より「意図」を理解し高精度に負債分析できる

**判定：部分的に真**。LLMは設計意図の自然言語化や境界づけで優位だが、確定的な構文特性や規模特性は静的解析が堅牢である。[files.speakerdeck.com+1](https://files.speakerdeck.com/presentations/7a9468d99f8d443ea37be87d82dbb3aa/slide_30.jpg)

**補足反論**

- LLMの解析は非決定的で、幻覚・過剰一般化のリスクがある。静的計測の客観性と補完的に使うべきである。[ACL Anthology](https://aclanthology.org/2024.acl-long.586/?utm_source=chatgpt.com)

## 命題D：負債スコアは「近年の学術論文データ」に基づく独自式

**判定：式の存在は真、根拠データの外部公開は未確認**。スライドに「独自計算式」の但し書きのみがある。[files.speakerdeck.com](https://files.speakerdeck.com/presentations/7a9468d99f8d443ea37be87d82dbb3aa/slide_32.jpg)

**補足反論**

- 既存の定量枠組み（SQALEのTechnical Debt Ratio、SIG Maintainability等）との較正が無いと、継時比較や横比較が困難である。[Sonar Documentation+1](https://docs.sonarsource.com/sonarqube-server/user-guide/code-metrics/metrics-definition?utm_source=chatgpt.com)

## 命題E：AIのテスト実装は既に人間を上回る

**判定：過大一般化**。LLM生成テストは一部条件で高カバレッジを示す報告があるが、課題も多い。ツール比較ではEvoSuite等と拮抗または劣位なケースが併存する。[arXiv+2MDPI+2](https://arxiv.org/pdf/2407.00225?utm_source=chatgpt.com)

**補足反論**

- 生成テストの「妥当なオラクル不足」「脆いアサーション」「フレーク化」は一般課題である。実プロダクトでの恒常優越は実証不足である。

## 命題F：リファクタリングは多くをAIへ委譲できる

**判定：将来可能性はあるが現状は限定的**。LLMは匂い検出や改善提案に有効だが、安全な自動適用は検証系の整備を前提とする。[arXiv+1](https://arxiv.org/html/2411.04444v1?utm_source=chatgpt.com)

**補足反論**

- コンパイル・テスト・型検査・差分保証の統合なしでは回帰混入が起こり得る。自動適用はサンドボックス下の段階的導入が適切である。

# Ⅲ. ベストプラクティスの相互検証（要点）

- **ハイブリッド評価**。LLMの設計観点と静的指標の統合で再現性と説明性を両立する。SQALEやSIGの指標群と、LLMの意味論的指摘を多面的に集約する。[Sonar Documentation+1](https://docs.sonarsource.com/sonarqube-server/user-guide/code-metrics/metrics-definition?utm_source=chatgpt.com)

- **検証駆動**。提案は必ずビルド・テスト・静的検査を自動実行し、失敗時はロールバックする。

- **ベンチマーク**。SWE-bench VerifiedやDefects4J系で外部妥当化し、再現手順と環境を公開する。[swebench.com+1](https://www.swebench.com/?utm_source=chatgpt.com)

- **MCP標準準拠**。「tools」「resources」「prompts」を分離し、複数クライアント（Cursor／Claude Code）から再利用する。[Model Context Protocol](https://modelcontextprotocol.io/specification/2025-06-18?utm_source=chatgpt.com)

- **安全設計**。最小権限OAuth、HTTP運用時のMCP Auth準拠、機密コードの匿名化・部分送信を徹底する。[Model Context Protocol+1](https://modelcontextprotocol.io/specification/2025-06-18/basic?utm_source=chatgpt.com)

- **幻覚緩和**。温度低設定、自己検証プロンプト、規則ベース検証、二段階推敲、差分のみ適用を併用する。幻覚研究の知見を活用する。[OpenReview+1](https://openreview.net/forum?id=VwOYxPScxB&utm_source=chatgpt.com)

- **可観測性**。評価ログ、提示根拠、適用パッチ、失敗要因を構造化保存し、監査可能性を担保する。

---

# Ⅳ. 開発者向け技術資料（オリジナルMCPツール設計）

## 名称

**Adaptus**。変更容易性の計測・診断・提案・検証を一体化するMCPサーバー。

## 1. 目的と非機能

- 目的。大規模組織で変更容易性を横断計測し、設計改善を高速に反復する。

- 目標。500LOCを30秒以内に一次分析し、誤警報率を<10%に抑制する。

- 可用性。CIスケジュール実行とオンデマンド実行の両立。

- 再現性。静的指標は決定的、LLM出力は温度0と検証回路で安定化。

## 2. 機能一覧（MCP三本柱）

**Resources**

- `adaptus://guidelines/latest` 設計規約集。

- `adaptus://score/formula` 負債スコア式のJSON。

- `adaptus://prompt/core` コアプロンプト雛形。

**Tools**

- `analyze_debt(paths, lang)` 静的指標と意味解析を併用して欠陥候補を列挙。

- `score_debt(metrics)` 独自式でファイル別スコアを算出。

- `propose_design(code|smell)` Mermaid図と分割案を生成。

- `generate_tests(target, framework)` テスト雛形を生成し補完指示を付与。

- `verify_patch(cmd_build, cmd_test)` パッチのビルドとテストを実行。

- `summarize(repo)` ホットスポットと難所を集約。

**Prompts**

- `core/debt-analysis` 変更容易性観点の逐次推論テンプレート。

- `core/design-refactor` ドメイン分離と責務再配置の設計方針テンプレート。

（MCP用語と役割の正当性は仕様に一致する）[Model Context Protocol](https://modelcontextprotocol.io/specification/2025-06-18?utm_source=chatgpt.com)

## 3. スコア設計（例示）

- 正規化複合式。

- `MI_n = clamp((100-MI)/100,0,1)`（MIは維持性指数）。[Microsoft Learn](https://learn.microsoft.com/en-us/visualstudio/code-quality/code-metrics-values?view=visualstudio&utm_source=chatgpt.com)

- `CC_n = clamp((CC-10)/40,0,1)`（循環的複雑度の正規化）。

- `DUP_n = 重複行率`。

- `TD_n = SQALE技術負債比の正規化`。[Sonar Documentation](https://docs.sonarsource.com/sonarqube-server/user-guide/code-metrics/metrics-definition?utm_source=chatgpt.com)

- `DebtScore = 0.35*MI_n + 0.25*CC_n + 0.20*DUP_n + 0.20*TD_n + designSmellPts`

- `designSmellPts`はLLM指摘の設計上の欠陥をルール表で加点。

- 既存モデル（SIG等）との相関チェックを定期実施する。[Software Improvement Group](https://www.softwareimprovementgroup.com/maintainability-model-2024-update/?utm_source=chatgpt.com)

## 4. データフロー

1. 対象抽出。差分とホットスポットをGit履歴から抽出。

2. 静的測定。言語別CIツールでMI、CC、重複率等を算出。

3. LLM診断。プロンプトで設計観点の欠陥候補を列挙。

4. スコア統合。独自式で重み付け集計。

5. 提案生成。分割案とMermaid図を生成。

6. 検証実行。ビルド・テスト・静的検査を自動走査。

7. レポート。根拠リンクとパッチ差分を掲示。

## 5. セキュリティと運用

- 最小権限OAuthとMCP Authに準拠し、HTTP運用時はトークン検証を行う。[Model Context Protocol+1](https://modelcontextprotocol.io/specification/2025-06-18/basic?utm_source=chatgpt.com)

- コードは部分抽出と匿名化で送信し、秘密情報は除去する。

- すべてのLLM応答は「適用前検証」を必須化する。

## 6. 推論時スケーリング（TTS）設計

**①タスク分析**

- 目的。欠陥候補の網羅と誤警報低減。

- 判定。自動可、外部オラクルはテスト成功で代替。

- 難度。易：規模指標、中：匂い分解、高：層分離とドメイン境界。

- リスク。幻覚、過修正、回帰。

**②スケーリング軸**

- 並列軸。ファイル単位に静的測定を並列化。

- 逐次軸。LLMの自己推敲一回、検証後追ループ最大二回。

- 内部軸。推論深さを欠陥数と確信度で動的制御。

**③ベースライン構成**

- Greedy単一＋検証。温度0、max_tokens中。

- 中難度はSelf‑Consistency 3本で多数決後に検証。

- 高難度は探索幅小のSearch＋Verifier。

**④Verifier設計**

- 外部。ビルド、単体・統合テスト、型検査。

- ルール。命名・分割・循環依存禁止の規約検証。

- 自己検証。根拠箇所の列挙と反例探索プロンプト。

**⑤高度手法の採用条件**

- Self‑Refine。欠陥>5、確信度<0.6で起動。

- ToT/MCTS。設計再編の探索が広い場合のみ。

- RAT/RATT。証跡必要な高リスク改変時に限定。

**⑥コスト–性能と動的スケーリング**

- 低難度高確信→Greedy。

- 中難度→Self‑Consistency少数本。

- 高難度高価値→検証付きSearch。

**⑦実験計画**

- データ。社内実案件＋SWE‑bench Verified／Defects4J。[swebench.com](https://www.swebench.com/?utm_source=chatgpt.com)

- 指標。正答率、誤警報率、Pass@k、平均トークン、レイテンシ。

- A/B。Greedy vs SC@3 vs 検証Searchで比較。

**⑧推奨パラメータ表（例）**

| 区分 | モード | N | 温度 | 最大長 | Verifier | 期待精度 | 期待遅延 |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 低難度 | Greedy | 1 | 0.0 | 6k | あり | 中 | 低 |
| 中難度 | SC | 3 | 0.2 | 8k | あり | 中高 | 中 |
| 高難度 | Search | 4 | 0.2 | 12k | 強 | 高 | 高 |

## 7. MCP実装サンプル（Python・最小骨格）
```python
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
モジュール概要:
  Adaptus MCPサーバーの最小実装。
  静的指標の簡易計測、負債スコア算出、設計提案を提供する。
  実運用ではLLM接続と外部検証系を差し替える。

起動方法:
  uv run adaptus_server.py  # HTTPトランスポートで起動
  または
  python3 adaptus_server.py

引数:
  なし。環境変数で設定を行う。
"""

from __future__ import annotations
import ast
import json
import subprocess
from pathlib import Path
from typing import Dict, List, Tuple

from mcp.server.fastmcp import FastMCP, Context  # MCP公式SDKを利用  # noqa: E402

mcp = FastMCP("Adaptus", json_response=True)

def _read_code(path: Path) -> str:
    """ファイル読込の内部関数。例外は上位で処理する。"""
    return path.read_text(encoding="utf-8", errors="ignore")

def _basic_metrics(code: str) -> Dict[str, float]:
    """Pythonコードの簡易指標を抽出する。
    引数:
      code: 解析対象のコード文字列
    戻り値:
      行数・関数数・分岐数・平均引数数の辞書
    """
    try:
        tree = ast.parse(code)
    except SyntaxError:
        return {"loc": len(code.splitlines()), "funcs": 0, "branches": 0, "avg_args": 0.0}

    funcs, branches, args = 0, 0, []
    for node in ast.walk(tree):
        if isinstance(node, ast.FunctionDef):
            funcs += 1
            args.append(len([a for a in node.args.args if a.arg != "self"]))
        if isinstance(node, (ast.If, ast.For, ast.While, ast.Try, ast.BoolOp)):
            branches += 1

    loc = len([l for l in code.splitlines() if l.strip() and not l.strip().startswith("#")])
    avg_args = sum(args) / len(args) if args else 0.0
    return {"loc": float(loc), "funcs": float(funcs), "branches": float(branches), "avg_args": float(avg_args)}

def _score_formula(metrics: Dict[str, float]) -> float:
    """負債スコアの計算式。
    引数:
      metrics: 指標の辞書(MIやTD未計測時は0で補完)
    戻り値:
      0.0〜10.0のスコア(高いほど負債が重い)
    """
    # 簡易正規化と重み。実運用はSQALEやSIGと較正する。
    mi_n = min(max((100.0 - metrics.get("mi", 0.0)) / 100.0, 0.0), 1.0)
    cc_n = min(max((metrics.get("branches", 0.0) - 10.0) / 40.0, 0.0), 1.0)
    dup_n = min(max(metrics.get("dup_rate", 0.0), 0.0), 1.0)
    td_n = min(max(metrics.get("td_ratio", 0.0), 0.0), 1.0)
    base = 0.35 * mi_n + 0.25 * cc_n + 0.20 * dup_n + 0.20 * td_n
    return round(base * 10.0, 2)

@mcp.resource("adaptus://score/formula")
def get_formula() -> str:
    """スコア式のJSONを返す。"""
    payload = {
        "weights": {"mi": 0.35, "cc": 0.25, "dup": 0.20, "td": 0.20},
        "note": "SQALE・SIGと定期較正すること"
    }
    return json.dumps(payload, ensure_ascii=False)

@mcp.tool()
def analyze_debt(paths: List[str], lang: str = "python") -> Dict[str, Dict[str, float]]:
    """負債候補の分析を行う。
    引数:
      paths: 解析対象のファイルパス配列
      lang: 言語名(簡易サポート: python)
    戻り値:
      ファイル別の指標辞書
    """
    results: Dict[str, Dict[str, float]] = {}
    for p in paths:
        path = Path(p)
        if not path.exists():
            results[p] = {"error": 1.0}
            continue
        code = _read_code(path)
        m = _basic_metrics(code) if lang == "python" else {"loc": float(len(code.splitlines()))}
        m["score"] = _score_formula(m)
        results[p] = m
    return results

@mcp.tool()
def propose_design(summary: str) -> Dict[str, str]:
    """設計改善の雛形を返す。
    引数:
      summary: 問題点の要約文字列
    戻り値:
      Mermaid図と改善方針の辞書
    """
    mermaid = (
        "classDiagram\n"
        "  class UseCase {\n"
        "    +execute()\n"
        "  }\n"
        "  class DomainService {\n"
        "    +calc()\n"
        "  }\n"
        "  class Repository {\n"
        "    +find()\n"
        "  }\n"
        "  UseCase --> DomainService\n"
        "  UseCase --> Repository\n"
    )
    plan = "関心分離を徹底し、状態と手続を各ドメインへ再配置する。"
    return {"mermaid": mermaid, "plan": plan, "note": summary}

@mcp.tool()
def verify_patch(cmd_build: str = "", cmd_test: str = "") -> Dict[str, int]:
    """外部検証を実行する。
    引数:
      cmd_build: ビルドコマンド
      cmd_test: テストコマンド
    戻り値:
      戻りコードを含む辞書
    """
    rc_build = subprocess.call(cmd_build, shell=True) if cmd_build else 0
    rc_test = subprocess.call(cmd_test, shell=True) if cmd_test else 0
    return {"build_rc": rc_build, "test_rc": rc_test}

if __name__ == "__main__":
    # HTTPで待受。実運用は認証・権限制御を追加する。
    mcp.run(transport="streamable-http")
```

**注**：MCP SDKは公式実装を使用した。仕様と用語の整合を確認のこと。[GitHub](https://github.com/modelcontextprotocol/python-sdk)

## 8. CI連携テンプレート（GitHub Actions）
```yaml
name: adaptus-scan
on:
  schedule: [{ cron: "0 3 * * 1-5" }]
  workflow_dispatch: {}
jobs:
  scan:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: astral-sh/setup-uv@v3
      - run: uv run --with mcp python adaptus_server.py &
      - run: |
          python - <<'PY'
          import json,glob,requests
          files = [f for f in glob.glob("**/*.py", recursive=True) if "venv" not in f]
          # ここではMCP HTTPエンドポイントにポストする想定
          print(json.dumps({"files": files}, ensure_ascii=False))
          PY
      - name: Upload report
        uses: actions/upload-artifact@v4
        with: { name: adaptus-report, path: report/*.json }
```

---

# Adaptus MCPサーバー プロジェクトセットアップ手順書

## 📋 概要

この手順書は、Adaptus MCPサーバープロジェクトを構築するための完全なガイドです。技術設計ドキュメントに含まれるすべてのコードと設定を実際のプロジェクトとして展開します。

## 🎯 完成目標

```
/Users/shimizu/bin-mcp-adaptus/
├── pyproject.toml
├── README.md
├── src/
│   └── adaptus/
│       ├── __init__.py
│       └── server.py
├── tests/
│   └── test_server.py
├── .github/
│   └── workflows/
│       ├── ci.yml
│       └── adaptus-scan.yml
├── .gitignore
└── LICENSE
```

## 📝 セットアップ手順

### ステップ1: 基本ファイルの配置

1. **pyproject.tomlの作成**
   ```bash
   # AGENTS.mdをpyproject.tomlとしてコピー
   cp AGENTS.md pyproject.toml
   ```

2. **README.mdの作成**
   ```bash
   # CLAUDE.mdをREADME.mdとしてコピー
   cp CLAUDE.md README.md
   ```

### ステップ2: ソースコードの展開

1. **srcディレクトリの作成**
   ```bash
   mkdir -p src/adaptus
   ```

2. **__init__.pyの作成**
   ```bash
   cat > src/adaptus/__init__.py << 'EOF'
"""Adaptus MCP Server Package"""

__version__ = "0.1.0"
__author__ = "Adaptus Team"
__email__ = "adaptus@example.com"

from .server import mcp

__all__ = ["mcp"]
EOF
   ```

3. **server.pyの作成**
   ```bash
   # 技術設計ドキュメントからserver.pyのコードを抽出して作成
   # (このドキュメントの「## src/adaptus/server.py」セクションを参照)
   ```

### ステップ3: テストファイルの配置

1. **testsディレクトリの作成**
   ```bash
   mkdir -p tests
   ```

2. **test_server.pyの作成**
   ```bash
   cat > tests/test_server.py << 'EOF'
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Adaptus MCPサーバーのテスト
"""

import pytest
import json
from pathlib import Path
from adaptus.server import _basic_metrics, _score_formula, analyze_debt

def test_basic_metrics():
    """基本的なメトリクス計算のテスト"""
    code = """
def hello(name: str) -> str:
    if name:
        return f"Hello, {name}!"
    return "Hello, World!"
"""
    metrics = _basic_metrics(code)
    assert metrics["loc"] == 5.0
    assert metrics["funcs"] == 1.0
    assert metrics["branches"] == 1.0
    assert metrics["avg_args"] == 1.0

def test_score_formula():
    """スコア計算式のテスト"""
    metrics = {"mi": 80.0, "branches": 15.0, "dup_rate": 0.1, "td_ratio": 0.05}
    score = _score_formula(metrics)
    assert 0.0 <= score <= 10.0

def test_analyze_debt():
    """負債分析ツールのテスト"""
    # テスト用の一時ファイルを作成
    test_file = Path("test_sample.py")
    test_file.write_text("def test(): pass")
    
    try:
        results = analyze_debt(["test_sample.py"])
        assert "test_sample.py" in results
        assert "score" in results["test_sample.py"]
    finally:
        test_file.unlink()
EOF
   ```

### ステップ4: GitHub Actionsの配置

1. **.githubディレクトリの作成**
   ```bash
   mkdir -p .github/workflows
   ```

2. **ci.ymlの作成**
   ```bash
   cat > .github/workflows/ci.yml << 'EOF'
name: CI
on:
  push:
    branches: [ main, develop ]
  pull_request:
    branches: [ main ]
jobs:
  test:
    runs-on: ubuntu-latest
    strategy:
      matrix:
        python-version: ["3.9", "3.10", "3.11", "3.12"]
    steps:
      - uses: actions/checkout@v4
      - uses: astral-sh/setup-uv@v3
      - run: uv sync --dev
      - run: uv run ruff check .
      - run: uv run black --check .
      - run: uv run mypy src/
      - run: uv run pytest
  build:
    runs-on: ubuntu-latest
    needs: test
    steps:
      - uses: actions/checkout@v4
      - uses: astral-sh/setup-uv@v3
      - run: uv build
      - name: Upload wheel
        uses: actions/upload-artifact@v4
        with:
          name: wheel
          path: dist/*.whl
EOF
   ```

3. **adaptus-scan.ymlの作成**
   ```bash
   cat > .github/workflows/adaptus-scan.yml << 'EOF'
name: adaptus-scan
on:
  schedule: [{ cron: "0 3 * * 1-5" }]
  workflow_dispatch: {}
jobs:
  scan:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: astral-sh/setup-uv@v3
      - run: uv run --with mcp python adaptus_server.py &
      - run: |
          python - <<'PY'
          import json,glob,requests
          files = [f for f in glob.glob("**/*.py", recursive=True) if "venv" not in f]
          print(json.dumps({"files": files}, ensure_ascii=False))
          PY
      - name: Upload report
        uses: actions/upload-artifact@v4
        with: { name: adaptus-report, path: report/*.json }
EOF
   ```

### ステップ5: その他の設定ファイル

1. **.gitignoreの作成**
   ```bash
   cat > .gitignore << 'EOF'
__pycache__/
*.py[cod]
*$py.class
*.so
.Python
build/
develop-eggs/
dist/
downloads/
eggs/
.eggs/
lib/
lib64/
parts/
sdist/
var/
wheels/
*.egg-info/
.installed.cfg
*.egg
MANIFEST
.pytest_cache/
.coverage
htmlcov/
.tox/
.nox/
.coverage
.coverage.*
.cache
nosetests.xml
coverage.xml
*.cover
.hypothesis/
.mypy_cache/
.dmypy.json
dmypy.json
.pyre/
.env
.venv
env/
venv/
ENV/
env.bak/
venv.bak/
EOF
   ```

2. **LICENSEの作成**
   ```bash
   cat > LICENSE << 'EOF'
MIT License

Copyright (c) 2025 Adaptus Team

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
EOF
   ```

## 🚀 開発環境のセットアップ

### ステップ6: 依存関係のインストール

```bash
# uvのインストール（未インストールの場合）
curl -LsSf https://astral.sh/uv/install.sh | sh

# プロジェクトの同期
uv sync

# 開発依存関係のインストール
uv sync --dev
```

### ステップ7: 動作確認

1. **MCPサーバーの起動テスト**
   ```bash
   uv run adaptus-server
   ```

2. **テストの実行**
   ```bash
   uv run pytest
   ```

3. **コード品質チェック**
   ```bash
   uv run ruff check .
   uv run black --check .
   uv run mypy src/
   ```

## 📚 使用方法

### MCPクライアントとの連携

1. **Cursorの場合**
   - 設定画面（⌘,）を開く
   - MCPセクションでサーバーを追加
   - URL: `http://localhost:8000`

2. **Claude Codeの場合**
   ```bash
   claude mcp add --transport http --name adaptus http://localhost:8000
   ```

### 基本的な使用例

```python
# コード分析
from adaptus import analyze_debt
result = analyze_debt(["src/main.py"])

# 設計提案
from adaptus import propose_design
proposal = propose_design("リファクタリングが必要")

# パッチ検証
from adaptus import verify_patch
verification = verify_patch("python -m build", "pytest")
```

## ✅ 検証リスト

- [ ] pyproject.tomlが正しく配置されている
- [ ] README.mdが完成している
- [ ] src/adaptus/__init__.pyが作成されている
- [ ] src/adaptus/server.pyが作成されている
- [ ] tests/test_server.pyが作成されている
- [ ] GitHub Actionsワークフローが配置されている
- [ ] .gitignoreが作成されている
- [ ] LICENSEが作成されている
- [ ] 依存関係がインストールされている
- [ ] MCPサーバーが起動する
- [ ] テストが通過する
- [ ] コード品質チェックが通過する

## 🎉 完成後の次のステップ

1. **Gitリポジトリの初期化**
   ```bash
   git init
   git add .
   git commit -m "feat: initial commit of Adaptus MCP server"
   ```

2. **GitHubリポジトリの作成とプッシュ**
   ```bash
   git remote add origin <your-repo-url>
   git push -u origin main
   ```

3. **リリースの作成**
   ```bash
   uv build
   # GitHubでリリースを作成
   ```

---

**この手順書に従って、Adaptus MCPサーバープロジェクトを完成させてください。**

**備考**：モディフィウス同様に定期計測基盤を構築できる。[files.speakerdeck.com](https://files.speakerdeck.com/presentations/7a9468d99f8d443ea37be87d82dbb3aa/slide_35.jpg)

## 9. クライアント連携

- **Cursor**。設定画面のMCPにサーバーURLを登録する。[Cursor](https://cursor.com/docs/context/mcp?utm_source=chatgpt.com)

- **Claude Code**。`claude mcp add --transport http`で接続する。[code.claude.com](https://code.claude.com/docs/en/mcp?utm_source=chatgpt.com)

## 10. 検証計画と指標

- **外部妥当化**。SWE‑bench Verifiedでパッチ適用率を測る。[swebench.com](https://www.swebench.com/?utm_source=chatgpt.com)

- **内部妥当化**。既存SQALE・SIG指標との相関を四半期ごとに再推定する。[Sonar Documentation+1](https://docs.sonarsource.com/sonarqube-server/user-guide/code-metrics/metrics-definition?utm_source=chatgpt.com)

- **安定性**。同一入力での出力分散を温度と自己検証有無で評価する。

- **安全性**。誤修正率、回帰混入率、幻覚検出率を監視する。

## 11. リスクと対策

- **幻覚**。自己検証プロンプトと規則検証で弾く。[OpenReview](https://openreview.net/forum?id=VwOYxPScxB&utm_source=chatgpt.com)

- **過修正**。差分最小化と可逆適用で抑制する。

- **指標ドリフト**。定義書をバージョン管理し、変更時に換算式を付す。

- **漏洩**。部分送信と匿名化、MCP Auth利用で低減する。[Model Context Protocol](https://modelcontextprotocol.io/specification/2025-06-18/basic?utm_source=chatgpt.com)

---

# Ⅴ. 総括

- モディフィウスの存在と主機能は一次資料で裏付く。速度・精度比較は再現評価が要る。[Speaker Deck+1](https://speakerdeck.com/minodriven/modifius)

- LLMは設計意図の言語化に強いが、静的計測の客観性と組み合わせるのが最適である。[files.speakerdeck.com+1](https://files.speakerdeck.com/presentations/7a9468d99f8d443ea37be87d82dbb3aa/slide_30.jpg)

- 自動テスト／自動リファクタリングは有望だが、全面移行を主張できる合意的エビデンスは未整備である。検証回路とベンチマークが不可欠である。[arXiv+1](https://arxiv.org/pdf/2407.00225?utm_source=chatgpt.com)

---

# 付録A：コアプロンプト雛形（抜粋）
makefile`目的:
  変更容易性を高める設計上の欠陥を抽出する。
規則:
  根拠行番号を必ず列挙する。
  推測は「仮説」と明記する。
観点:
  カプセル化, 関心分離, 依存方向, ドメイン境界, 例外設計。
出力:
  欠陥一覧[項目, 根拠, 影響, 修正方針, 検証手順]。
`
---

# 付録B：参考規格・資料

- MCP公式発表と仕様。[Anthropic+1](https://www.anthropic.com/news/model-context-protocol?utm_source=chatgpt.com)

- MCP Python/TS SDK。[GitHub+1](https://github.com/modelcontextprotocol/python-sdk)

- Cursor／Claude CodeのMCP連携。[Cursor+1](https://cursor.com/docs/context/mcp?utm_source=chatgpt.com)

- SQALE／SIG／MIの基礎資料。[Sonar Documentation+2Software Improvement Group+2](https://docs.sonarsource.com/sonarqube-server/user-guide/code-metrics/metrics-definition?utm_source=chatgpt.com)

- 生成テスト・自動リファクタリング研究。[arXiv+1](https://arxiv.org/pdf/2407.00225?utm_source=chatgpt.com)

- 幻覚研究と検出。[arXiv+1](https://arxiv.org/pdf/2404.00971?utm_source=chatgpt.com)

以上。

---

# 実際のプロジェクトファイル

## src/adaptus/__init__.py

```python
"""Adaptus MCP Server Package"""

__version__ = "0.1.0"
__author__ = "Adaptus Team"
__email__ = "adaptus@example.com"

from .server import mcp

__all__ = ["mcp"]
```

## src/adaptus/server.py

```python
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Adaptus MCPサーバー
コード品質分析と設計改善を提供するMCPサーバー
"""

from __future__ import annotations
import ast
import json
import subprocess
from pathlib import Path
from typing import Dict, List, Tuple

from mcp.server.fastmcp import FastMCP, Context

mcp = FastMCP("Adaptus", json_response=True)

def _read_code(path: Path) -> str:
    """ファイル読込の内部関数"""
    return path.read_text(encoding="utf-8", errors="ignore")

def _basic_metrics(code: str) -> Dict[str, float]:
    """Pythonコードの簡易指標を抽出"""
    try:
        tree = ast.parse(code)
    except SyntaxError:
        return {"loc": len(code.splitlines()), "funcs": 0, "branches": 0, "avg_args": 0.0}

    funcs, branches, args = 0, 0, []
    for node in ast.walk(tree):
        if isinstance(node, ast.FunctionDef):
            funcs += 1
            args.append(len([a for a in node.args.args if a.arg != "self"]))
        if isinstance(node, (ast.If, ast.For, ast.While, ast.Try, ast.BoolOp)):
            branches += 1

    loc = len([l for l in code.splitlines() if l.strip() and not l.strip().startswith("#")])
    avg_args = sum(args) / len(args) if args else 0.0
    return {"loc": float(loc), "funcs": float(funcs), "branches": float(branches), "avg_args": float(avg_args)}

def _score_formula(metrics: Dict[str, float]) -> float:
    """負債スコアの計算式"""
    mi_n = min(max((100.0 - metrics.get("mi", 0.0)) / 100.0, 0.0), 1.0)
    cc_n = min(max((metrics.get("branches", 0.0) - 10.0) / 40.0, 0.0), 1.0)
    dup_n = min(max(metrics.get("dup_rate", 0.0), 0.0), 1.0)
    td_n = min(max(metrics.get("td_ratio", 0.0), 0.0), 1.0)
    base = 0.35 * mi_n + 0.25 * cc_n + 0.20 * dup_n + 0.20 * td_n
    return round(base * 10.0, 2)

@mcp.resource("adaptus://score/formula")
def get_formula() -> str:
    """スコア式のJSONを返す"""
    payload = {
        "weights": {"mi": 0.35, "cc": 0.25, "dup": 0.20, "td": 0.20},
        "note": "SQALE・SIGと定期較正すること"
    }
    return json.dumps(payload, ensure_ascii=False)

@mcp.tool()
def analyze_debt(paths: List[str], lang: str = "python") -> Dict[str, Dict[str, float]]:
    """負債候補の分析を行う"""
    results: Dict[str, Dict[str, float]] = {}
    for p in paths:
        path = Path(p)
        if not path.exists():
            results[p] = {"error": 1.0}
            continue
        code = _read_code(path)
        m = _basic_metrics(code) if lang == "python" else {"loc": float(len(code.splitlines()))}
        m["score"] = _score_formula(m)
        results[p] = m
    return results

@mcp.tool()
def propose_design(summary: str) -> Dict[str, str]:
    """設計改善の雛形を返す"""
    mermaid = (
        "classDiagram\n"
        "  class UseCase {\n"
        "    +execute()\n"
        "  }\n"
        "  class DomainService {\n"
        "    +calc()\n"
        "  }\n"
        "  class Repository {\n"
        "    +find()\n"
        "  }\n"
        "  UseCase --> DomainService\n"
        "  UseCase --> Repository\n"
    )
    plan = "関心分離を徹底し、状態と手続を各ドメインへ再配置する。"
    return {"mermaid": mermaid, "plan": plan, "note": summary}

@mcp.tool()
def verify_patch(cmd_build: str = "", cmd_test: str = "") -> Dict[str, int]:
    """外部検証を実行する"""
    rc_build = subprocess.call(cmd_build, shell=True) if cmd_build else 0
    rc_test = subprocess.call(cmd_test, shell=True) if cmd_test else 0
    return {"build_rc": rc_build, "test_rc": rc_test}

def main() -> None:
    """メインエントリーポイント"""
    mcp.run(transport="streamable-http")

if __name__ == "__main__":
    main()
```

## tests/test_server.py

```python
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Adaptus MCPサーバーのテスト
"""

import pytest
import json
from pathlib import Path
from adaptus.server import _basic_metrics, _score_formula, analyze_debt

def test_basic_metrics():
    """基本的なメトリクス計算のテスト"""
    code = """
def hello(name: str) -> str:
    if name:
        return f"Hello, {name}!"
    return "Hello, World!"
"""
    metrics = _basic_metrics(code)
    assert metrics["loc"] == 5.0
    assert metrics["funcs"] == 1.0
    assert metrics["branches"] == 1.0
    assert metrics["avg_args"] == 1.0

def test_score_formula():
    """スコア計算式のテスト"""
    metrics = {"mi": 80.0, "branches": 15.0, "dup_rate": 0.1, "td_ratio": 0.05}
    score = _score_formula(metrics)
    assert 0.0 <= score <= 10.0

def test_analyze_debt():
    """負債分析ツールのテスト"""
    # テスト用の一時ファイルを作成
    test_file = Path("test_sample.py")
    test_file.write_text("def test(): pass")
    
    try:
        results = analyze_debt(["test_sample.py"])
        assert "test_sample.py" in results
        assert "score" in results["test_sample.py"]
    finally:
        test_file.unlink()
```