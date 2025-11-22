# Adaptus MCP Server

コード品質分析と設計改善のためのMCP（Model Context Protocol）サーバー

## 📋 概要

Adaptusは、Pythonコードの技術的負債を分析し、設計改善提案を提供するMCPサーバーです。静的解析とAIを組み合わせることで、効率的なコード品質改善を実現します。

## 🚀 主な機能

### 🔍 コード分析 (`analyze_debt`)
- Pythonコードの基本的なメトリクスを抽出
- 負債スコアを計算（SQALE/SIG互換の計算式）
- 複数ファイルの一括分析に対応

### 📐 設計提案 (`propose_design`)
- クラス図の雛形をMermaid形式で生成
- 設計改善の具体的な計画を提案
- 関心分離を徹底したアーキテクチャ案を提示

### ✅ パッチ検証 (`verify_patch`)
- 外部ビルドコマンドの実行
- テストスイートの自動実行
- CI/CDパイプラインとの連携

### 📊 スコア計算式リソース
- 負債スコアの計算式をJSON形式で提供
- 重み付け設定の参照
- 定期的な較正を推奨

## 🛠️ インストール

### 前提条件
- Python 3.10以上
- uv（推奨）またはpip

### インストール手順

```bash
# uvを使用する場合（推奨）
curl -LsSf https://astral.sh/uv/install.sh | sh
git clone https://github.com/shimizumasaru/adaptus-mcp-server.git
cd adaptus-mcp-server
uv sync

# pipを使用する場合
git clone https://github.com/shimizumasaru/adaptus-mcp-server.git
cd adaptus-mcp-server
pip install -e .
```

## 🚀 使い方

### MCPサーバーの起動

```bash
# uvを使用
uv run adaptus-server

# pipを使用
adaptus-server
```

### MCPクライアントとの連携

#### Cursorの場合
1. 設定画面（⌘,）を開く
2. MCPセクションでサーバーを追加
3. URL: `http://localhost:8000`

#### Claude Codeの場合
```bash
claude mcp add --transport http --name adaptus http://localhost:8000
```

### ツールの使用例

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

## 🧪 開発

### 開発環境のセットアップ

```bash
# 開発依存関係のインストール
uv sync --dev

# テストの実行
uv run pytest tests/ -v

# コード品質チェック
uv run ruff check .
uv run black .
uv run mypy src/
```

### テスト

```bash
# すべてのテストを実行
uv run pytest

# カバレッジを含めて実行
uv run pytest --cov=adaptus
```

### コード品質

- **ruff**: リンティングとフォーマットチェック
- **black**: コードフォーマッター
- **mypy**: 静的型チェック

## 📊 負債スコア計算式

Adaptusでは以下の重み付けで負債スコアを計算します：

```json
{
  "weights": {
    "mi": 0.35,    // 保守性
    "cc": 0.25,    // 複雑度
    "dup": 0.20,   // 重複率
    "td": 0.20     // テストカバレッジ
  }
}
```

スコアは0.0〜10.0の範囲で、数値が高いほど負債が大きいことを示します。

## 🔄 CI/CD

### GitHub Actions
- **CI**: 自動テストとコード品質チェック
- **定期スキャン**: 平日の定期的なコード分析

### ワークフロー
```yaml
# .github/workflows/ci.yml
- テスト実行
- コード品質チェック
- ビルドとパッケージ化

# .github/workflows/adaptus-scan.yml
- 定期的な負債分析
- レポート生成
- アーティファクト保存
```

## 📝 貢献

1. Forkする
2. 機能ブランチを作成 (`git checkout -b feature/amazing-feature`)
3. 変更をコミット (`git commit -m 'Add amazing feature'`)
4. ブランチにプッシュ (`git push origin feature/amazing-feature`)
5. Pull Requestを作成

## 📄 ライセンス

MIT License - [LICENSE](LICENSE) を参照してください。

## 🔗 関連リンク

- [GitHubリポジトリ](https://github.com/shimizumasaru/adaptus-mcp-server)
- [MCP仕様](https://modelcontextprotocol.io/)
- [FastMCP](https://github.com/jlowin/fastmcp)

## 🤝 サポート

バグ報告や機能要望については、GitHub Issuesをご利用ください。

---

**Adaptus** - より良いコード品質へ 🔧
