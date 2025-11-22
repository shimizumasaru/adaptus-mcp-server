# Project Context

## Purpose
Adaptusは、Pythonコードの技術的負債を分析し、設計改善提案を提供するMCP（Model Context Protocol）サーバーです。開発者がコード品質を継続的に改善できるよう、静的解析とAIを組み合わせた効率的なツールを提供します。

## Tech Stack
- **Python 3.10+**: 主要なプログラミング言語
- **FastMCP**: MCPサーバーフレームワーク
- **AST**: Pythonコードの静的解析
- **uv**: パッケージ管理と仮想環境
- **pytest**: テストフレームワーク
- **ruff**: リンティングとフォーマット
- **black**: コードフォーマッター
- **mypy**: 静的型チェック
- **GitHub Actions**: CI/CDパイプライン

## Project Conventions

### Code Style
- **Pythonスタイル**: PEP 8準拠、blackでフォーマット
- **行長**: 88文字以内
- **型ヒント**: 必須、mypyで静的チェック
- **命名規則**: 
  - 関数/変数: snake_case
  - クラス: PascalCase
  - 定数: UPPER_SNAKE_CASE
- **ドキュメント**: JSDoc風のdocstring、日本語OK

### Architecture Patterns
- **MCPサーバー**: FastMCPベースのツールアーキテクチャ
- **関心分離**: 分析、提案、検証の各機能を独立したツールとして実装
- **単一責任**: 各関数は単一の明確な責務を持つ
- **エラーハンドリング**: 例外を適切に処理、意味のあるエラーメッセージ

### Testing Strategy
- **単体テスト**: pytestを使用、すべての公開関数をカバー
- **カバレッジ**: 目標80%以上
- **テスト構成**: tests/ディレクトリに配置、test_*.py命名規則
- **モック**: 外部依存を適切にモック化
- **CI自動実行**: プッシュ時に自動テスト実行

### Git Workflow
- **ブランチ戦略**: mainブランチのみ（シンプルなプロジェクト）
- **コミット規約**: Conventional Commits
  - `feat`: 新機能
  - `fix`: バグ修正
  - `docs`: ドキュメント更新
  - `refactor`: リファクタリング
  - `test`: テスト関連
- **プルリクエスト**: 必須、レビュー必須
- **リリース**: タグベース、semver準拠

## Domain Context

### 技術的負債分析
- **メトリクス**: LOC（コード行数）、関数数、分岐数、循環的複雑度
- **スコアリング**: SQALE/SIG互換の重み付けアルゴリズム
- **対象**: Pythonソースコード、ASTベースの静的解析

### 設計改善提案
- **クラス図**: Mermaid形式のUML図
- **アーキテクチャ**: クリーンアーキテクチャ、関心分離
- **パターン**: ドメイン駆動設計の基本概念

### MCPプロトコル
- **ツール**: analyze_debt, propose_design, verify_patch
- **リソース**: スコア計算式のJSON提供
- **トランスポート**: HTTPストリーミング

## Important Constraints
- **Pythonバージョン**: 3.10以上必須（FastMCPの要件）
- **依存関係**: 最小限、セキュリティ重視
- **パフォーマンス**: 400行のコードを20秒以内に分析
- **互換性**: MCP 1.0+準拠
- **セキュリティ**: コード実行なし、読み取り専用アクセス

## External Dependencies
- **FastMCP**: MCPサーバーの実装基盤
- **GitHub Actions**: CI/CDと定期スキャン
- **MCPクライアント**: Cursor, Claude Codeとの連携
- **静的解析ライブラリ**: radon, lizard（将来的な拡張用）

## Quality Gates
- **テスト**: すべてのテストが通過必須
- **コード品質**: ruff, black, mypyのチェック必須
- **ドキュメント**: README.mdとAPIドキュメント必須
- **バージョニング**: semver準拠必須
