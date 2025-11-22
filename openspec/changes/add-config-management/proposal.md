# Change: Add Configuration Management

## Why
現在のAdaptus MCPサーバーはハードコードされた設定を使用しており、ユーザーが分析パラメータやしきい値をカスタマイズできません。設定管理機能を追加することで、柔軟性と再利用性を向上させます。

## What Changes
- 設定ファイル読み込み機能を追加
- 分析パラメータのカスタマイズを可能に
- 設定値のバリデーションを実装
- デフォルト設定とのマージ機能を提供

## Impact
- Affected specs: config-management
- Affected code: src/adaptus/server.py, 新規設定モジュール
- **BREAKING**: 環境変数ベースの設定から設定ファイルベースへ移行
