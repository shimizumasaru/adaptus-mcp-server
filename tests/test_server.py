#!/usr/bin/env python3
"""
Adaptus MCPサーバーのテスト
"""

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
    assert metrics["loc"] == 4.0  # 実際のコード行数
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
