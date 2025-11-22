#!/usr/bin/env python3
"""
Adaptus MCPサーバー
コード品質分析と設計改善を提供するMCPサーバー
"""

from __future__ import annotations

import ast
import json
import subprocess
from pathlib import Path

from mcp.server.fastmcp import FastMCP

mcp = FastMCP("Adaptus", json_response=True)


def _read_code(path: Path) -> str:
    """ファイル読込の内部関数"""
    return path.read_text(encoding="utf-8", errors="ignore")


def _basic_metrics(code: str) -> dict[str, float]:
    """Pythonコードの簡易指標を抽出"""
    try:
        tree = ast.parse(code)
    except SyntaxError:
        return {
            "loc": len(code.splitlines()),
            "funcs": 0,
            "branches": 0,
            "avg_args": 0.0,
        }

    funcs, branches, args = 0, 0, []
    for node in ast.walk(tree):
        if isinstance(node, ast.FunctionDef):
            funcs += 1
            args.append(len([a for a in node.args.args if a.arg != "self"]))
        if isinstance(node, (ast.If, ast.For, ast.While, ast.Try, ast.BoolOp)):
            branches += 1

    loc = len(
        [
            line
            for line in code.splitlines()
            if line.strip() and not line.strip().startswith("#")
        ]
    )
    avg_args = sum(args) / len(args) if args else 0.0
    return {
        "loc": float(loc),
        "funcs": float(funcs),
        "branches": float(branches),
        "avg_args": float(avg_args),
    }


def _score_formula(metrics: dict[str, float]) -> float:
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
        "note": "SQALE・SIGと定期較正すること",
    }
    return json.dumps(payload, ensure_ascii=False)


@mcp.tool()
def analyze_debt(paths: list[str], lang: str = "python") -> dict[str, dict[str, float]]:
    """負債候補の分析を行う"""
    results: dict[str, dict[str, float]] = {}
    for p in paths:
        path = Path(p)
        if not path.exists():
            results[p] = {"error": 1.0}
            continue
        code = _read_code(path)
        m = (
            _basic_metrics(code)
            if lang == "python"
            else {"loc": float(len(code.splitlines()))}
        )
        m["score"] = _score_formula(m)
        results[p] = m
    return results


@mcp.tool()
def propose_design(summary: str) -> dict[str, str]:
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
def verify_patch(cmd_build: str = "", cmd_test: str = "") -> dict[str, int]:
    """外部検証を実行する"""
    rc_build = subprocess.call(cmd_build, shell=True) if cmd_build else 0
    rc_test = subprocess.call(cmd_test, shell=True) if cmd_test else 0
    return {"build_rc": rc_build, "test_rc": rc_test}


def main() -> None:
    """メインエントリーポイント"""
    mcp.run(transport="streamable-http")


if __name__ == "__main__":
    main()
