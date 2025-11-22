# Change: Add Missing MCP Features

## Why
現在のAdaptus MCPサーバーは技術設計ドキュメントで定義されたMCP三本柱の一部のみを実装しています。不足しているResources、Tools、Promptsを実装することで、完全なコード品質分析と設計改善プラットフォームを提供します。

## What Changes
- 設計規約集とコアプロンプトのResourcesを追加
- スコア算出、テスト生成、リポジトリ要約のToolsを実装
- 逐次推論と設計方針のPromptテンプレートを提供
- 既存機能の拡張と統合

## Impact
- Affected specs: resources, tools, prompts, analysis
- Affected code: src/adaptus/server.py, 新規モジュール群
- 新規リソースファイル: guidelines/, prompts/, templates/
