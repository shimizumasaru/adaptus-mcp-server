# Adaptus 設計ガイドライン

## Pythonコード品質基準

### 1. コード構造

- **単一責任原則**: 各関数/クラスは明確な単一の責務を持つべき
- **DRY原則**: 抽象化によってコードの重複を避ける
- **SOLID原則**: SOLID設計原則を遵守する
- **クリーンアーキテクチャ**: 関心事を明確に分離したレイヤー構造を採用する

### 2. 命名規則

- **関数名**: snake_caseを使用し、動作内容を示す動詞を命名
- **クラス名**: PascalCaseを使用し、明確な名詞を命名
- **定数**: UPPER_SNAKE_CASE形式で命名
- **変数名**: snake_caseを使用し、意味が明確な名前を付ける

### 3. コード構成

```
src/
├── domain/           # ビジネスロジック層
├── infrastructure/   # 外部依存関係層
├── application/      # ユースケース層
└── interfaces/       # API/外部インターフェース層
```

### 4. エラー処理

- 具体的な例外タイプを使用する
- 意味のあるエラーメッセージを提供する
- 適切なロギングを実装する
- 早期に明確に失敗を検出する設計とする

### 5. テストガイドライン

- **単体テスト**: 個々のコンポーネントを分離してテストする
- **統合テスト**: コンポーネント間の相互作用をテストする
- **テスト網羅率**: 最低80%のテストカバー率を確保する
- **テスト命名規則**: シナリオを説明する意味のあるテスト名を使用する

（descriptive_test_names_that_explain_scenario）

### 6. ドキュメント整備

- 公開関数すべてにドキュストリングを記述する
- 関数シグネチャに型ヒントを付与する
- 各モジュールごとにREADMEファイルを作成する
- アーキテクチャ決定記録（ADRs）を作成する

### 7. パフォーマンス考慮事項

- 最適化前にプロファイリングを実施する
- 時間計算量と空間計算量を考慮する
- 適切なデータ構造を選択する
- 有効であればキャッシュ機構を実装する

### 8. セキュリティベストプラクティス

- すべての入力値を検証する
- セキュアコーディングプラクティスを遵守する
- 適切な認証/認可機構を実装する
- 依存関係を最新の状態に保つ

### 9. コードメトリクス目標値

- **循環的複雑度**: 関数あたり10未満
- **関数行数**: 50行未満
- **クラスサイズ**: 300行未満
- **コード重複率**: コードベース全体で5%未満

### 10. リファクタリングガイドライン

- 小規模で段階的な変更を行う
- リファクタリング後は毎回テストを実施する
- 既存の動作を変更しない
- コードの可読性と保守性を向上させる

## Development Workflow & Rules

### 11. Git Workflow

- **Always Check Status First**: Start every session with `git status` and `git branch`
- **Feature Branches Only**: Create feature branches for ALL work, never work on main/master
- **Incremental Commits**: Commit frequently with meaningful messages
- **Verify Before Commit**: Always `git diff` to review changes before staging
- **Non-Destructive Workflow**: Always preserve ability to rollback changes

### 12. File Organization

- **Think Before Write**: Always consider WHERE to place files before creating them
- **Claude-Specific Documentation**: Put reports, analyses, summaries in `claudedocs/` directory
- **Test Organization**: Place all tests in `tests/`, `__tests__/`, or `test/` directories
- **Script Organization**: Place utility scripts in `scripts/`, `tools/`, or `bin/` directories
- **No Scattered Tests**: Never create test_*.py or*.test.js next to source files

### 13. Safety & Temporal Rules

- **Framework Respect**: Check package.json/deps before using libraries
- **Pattern Adherence**: Follow existing project conventions and import styles
- **Always Verify Current Date**: Check <env> context for "Today's date" before ANY temporal assessment
- **Temporal Calculations**: Base all time math on verified current date, not assumptions

### 14. Tool Optimization

- **Best Tool Selection**: Always use the most powerful tool for each task (MCP > Native > Basic)
- **Parallel Everything**: Execute independent operations in parallel, never sequentially
- **Batch Operations**: Use MultiEdit over multiple Edits, batch Read calls
- **Efficiency First**: Choose speed and power over familiarity

### 15. Decision Trees

**Before Any File Operations**

```
File operation needed?
├─ Writing/Editing? → Read existing first → Understand patterns → Edit
├─ Creating new? → Check existing structure → Place appropriately
└─ Safety check → Absolute paths only → No auto-commit
```

**Starting New Feature**

```
New feature request?
├─ Scope clear? → No → Brainstorm mode first
├─ >3 steps? → Yes → TodoWrite required
├─ Patterns exist? → Yes → Follow exactly
├─ Tests available? → Yes → Run before starting
└─ Framework deps? → Check package.json first
```

## ソフトウェア工学の法則と原則

### 開発の法則

- **コンウェイの法則**: システムの構造は、そのシステムを設計する組織のコミュニケーション構造を反映する。
- **ブルックスの法則**: 遅れているソフトウェアプロジェクトへの要員追加は、さらに遅らせることになる。
- **マーフィーの法則**: 失敗する可能性のあるものは、いずれ失敗する（堅牢な設計の重要性）。
- **ガルの法則**: 複雑なシステムは、機能していた単純なシステムから進化したものでなければならない。最初から複雑に作られたシステムは機能しない。
- **リナスの法則**: 目玉の数さえ十分であれば、あらゆるバグは深刻ではない（コードレビューの重要性）。
- **ボーイスカウトの規則**: コードを触るときは、来た時よりも美しくして去ること。

### 設計原則（拡張）

- **KISS (Keep It Simple, Stupid)**: 単純性が最良の設計指針。過度な複雑さを避ける。
- **YAGNI (You Aren't Gonna Need It)**: 今必要な機能だけを実装する。将来必要になるかもしれない機能は、本当に必要になるまで作らない。
- **DRY (Don't Repeat Yourself)**: 知識の重複を避ける。すべての知識はシステム内で単一の、曖昧さのない表現を持つべきである。
- **驚き最小の原則 (POLA)**: インターフェースや振る舞いは、ユーザーや他の開発者が予想する通りであるべき。

## 運用・チームルール

### コラボレーション

- **心理的安全性**: 失敗を責めず、学習の機会とする文化を醸成する。
- **情報の透明性**: 決定事項や知識はドキュメント化し、特定の個人に依存しないようにする（バス係数対策）。
- **非同期コミュニケーション**: 割り込みを減らすため、可能な限り非同期でのコミュニケーションを優先する。

### コードレビューの心得

- **人格ではなくコードをレビューする**: 指摘はコードに対するものであり、書いた人への攻撃ではない。
- **肯定的なフィードバックもする**: 良いコードや工夫された実装には称賛を送る。
- **理由は明確に**: 「ダメです」ではなく「〜という理由で、〜の方が良いと考えます」と提案する。
- **小さなプルリクエスト**: レビューの負担を減らし、品質を高めるため、変更は小さく保つ。

## 避けるべきアンチパターン

1. **神オブジェクト**: 機能が集中しすぎたクラス
2. **長すぎる引数リスト**: 5つ以上の引数を持つ関数
3. **マジックナンバー**: 名前のない定数
4. **深いネスト構造**: 4段階以上のインデント
5. **コメントアウトされたコード**: 未使用のコードは削除する
6. **コピー＆ペーストプログラミング**: 抽象化手法を活用する

## コードレビューチェックリスト

- [ ] コードがスタイルガイドラインに準拠している
- [ ] 各関数が単一の責務を持っている
- [ ] エラー処理が適切に実装されている
- [ ] テストケースが網羅的である
- [ ] ドキュメントが明確で分かりやすい
- [ ] 明らかなセキュリティ上の問題がない
- [ ] パフォーマンス面での考慮事項が適切に対処されている
- [ ] コードが保守可能で可読性が高い
