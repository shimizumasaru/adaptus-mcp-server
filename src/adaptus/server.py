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
from typing import Any

from mcp.server.fastmcp import FastMCP  # type: ignore

mcp = FastMCP("Adaptus", json_response=True)


def _read_code(path: Path) -> str:
    """ファイル読込の内部関数"""
    return path.read_text(encoding="utf-8", errors="ignore")


def _read_resource(resource_path: str, version: str = "latest") -> str:
    """リソースファイル読み込みの内部関数"""
    base_path = Path(__file__).parent / "resources"

    # Handle versioned resources
    if version != "latest":
        versioned_path = base_path / "versions" / version / resource_path
        if versioned_path.exists():
            return versioned_path.read_text(encoding="utf-8")

    # Default to latest version
    resource_file = base_path / resource_path
    if resource_file.exists():
        content = resource_file.read_text(encoding="utf-8")
        # Add version metadata
        if content and not content.startswith("# Version:"):
            content = (
                f"# Version: latest\n# Updated: "
                f"{int(resource_file.stat().st_mtime)}\n\n{content}"
            )
        return content
    return f"Resource not found: {resource_path} (version: {version})"


def _semantic_analysis(code: str) -> dict[str, Any]:
    """Pythonコードの意味解析を実行"""
    try:
        tree = ast.parse(code)
    except SyntaxError:
        return {"errors": ["Syntax error in code"]}

    return _analyze_ast_nodes(tree)


def _analyze_ast_nodes(tree: ast.AST) -> dict[str, Any]:
    """ASTノードを解析して問題を検出"""
    issues = []
    smells = []
    patterns = []

    for node in ast.walk(tree):
        issues.extend(_analyze_function(node))
        issues.extend(_analyze_class(node))
        patterns.extend(_analyze_imports(node))
        smells.extend(_analyze_complexity(node))

    return {
        "issues": issues,
        "smells": smells,
        "patterns": patterns,
        "summary": {
            "total_issues": len(issues),
            "total_smells": len(smells),
            "total_patterns": len(patterns),
        },
    }


def _analyze_function(node: ast.AST) -> list[dict[str, Any]]:
    """関数ノードを解析"""
    issues: list[dict[str, Any]] = []
    if not isinstance(node, ast.FunctionDef):
        return issues

    end_lineno = getattr(node, "end_lineno", None)
    func_lines = (end_lineno - node.lineno + 1) if end_lineno is not None else 0

    if func_lines > 50:
        issues.append(
            {
                "type": "long_function",
                "name": node.name,
                "line": node.lineno,
                "length": func_lines,
                "severity": "medium",
            }
        )

    if len(node.args.args) > 7:
        issues.append(
            {
                "type": "too_many_params",
                "name": node.name,
                "line": node.lineno,
                "param_count": len(node.args.args),
                "severity": "high",
            }
        )

    return issues


def _analyze_class(node: ast.AST) -> list[dict[str, Any]]:
    """クラスノードを解析"""
    issues: list[dict[str, Any]] = []
    if not isinstance(node, ast.ClassDef):
        return issues

    methods = [n for n in node.body if isinstance(n, ast.FunctionDef)]

    if len(methods) > 20:
        issues.append(
            {
                "type": "large_class",
                "name": node.name,
                "line": node.lineno,
                "method_count": len(methods),
                "severity": "medium",
            }
        )

    return issues


def _analyze_imports(node: ast.AST) -> list[dict[str, Any]]:
    """インポートノードを解析"""
    patterns = []
    if isinstance(node, ast.ImportFrom):
        if node.module and node.module.startswith("."):
            patterns.append(
                {
                    "type": "relative_import",
                    "line": node.lineno,
                    "module": node.module,
                    "note": "Consider absolute imports",
                }
            )
    return patterns


def _analyze_complexity(node: ast.AST) -> list[dict[str, Any]]:
    """複雑さを解析"""
    smells = []
    if isinstance(node, ast.FunctionDef):
        nested_count = _count_nested_loops(node)
        if nested_count > 3:
            smells.append(
                {
                    "type": "deep_nesting",
                    "name": node.name,
                    "line": node.lineno,
                    "nesting_level": nested_count,
                    "severity": "high",
                }
            )
    return smells


def _count_nested_loops(node: ast.AST, depth: int = 0) -> int:
    """入れ子のループ深さをカウント"""
    max_depth = depth
    for child in ast.iter_child_nodes(node):
        if isinstance(child, (ast.For, ast.While, ast.If)):
            child_depth = _count_nested_loops(child, depth + 1)
            max_depth = max(max_depth, child_depth)
    return max_depth


def _read_template(template_path: str, variables: dict[str, str] | None = None) -> str:
    """テンプレートファイル読み込みと変数置換"""
    base_path = Path(__file__).parent / "templates"
    template_file = base_path / template_path

    if not template_file.exists():
        return f"Template not found: {template_path}"

    content = template_file.read_text(encoding="utf-8")

    # Variable substitution
    if variables:
        for key, value in variables.items():
            content = content.replace(f"{{{key}}}", value)

    return content


def _validate_template(template_content: str) -> dict[str, Any]:
    """テンプレートの妥当性検証"""
    issues = []

    # Check for required sections
    required_sections = ["## Context", "## Analysis Framework", "## Output Format"]
    for section in required_sections:
        if section not in template_content:
            issues.append(f"Missing required section: {section}")

    # Check for template variables
    import re

    variables = re.findall(r"\{([^}]+)\}", template_content)

    return {
        "is_valid": len(issues) == 0,
        "issues": issues,
        "variables": list(set(variables)),
        "length": len(template_content),
        "sections": len(re.findall(r"^#+", template_content, re.MULTILINE)),
    }


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


@mcp.resource("adaptus://guidelines/latest")
def get_guidelines() -> str:
    """設計規約集を返す"""
    return _read_resource("guidelines.md")


@mcp.resource("adaptus://guidelines/{version}")
def get_guidelines_versioned(version: str) -> str:
    """バージョン指定で設計規約集を返す"""
    return _read_resource("guidelines.md", version)


@mcp.resource("adaptus://prompt/core")
def get_core_prompts() -> str:
    """コアプロンプト雛形を返す"""
    return _read_resource("prompts.md")


@mcp.resource("adaptus://prompt/{version}/core")
def get_core_prompts_versioned(version: str) -> str:
    """バージョン指定でコアプロンプト雛形を返す"""
    return _read_resource("prompts.md", version)


@mcp.resource("adaptus://template/debt-analysis")
def get_debt_analysis_template() -> str:
    """負債分析テンプレートを返す"""
    return _read_template("core/debt-analysis.md")


@mcp.resource("adaptus://template/design-refactor")
def get_design_refactor_template() -> str:
    """設計リファクタリングテンプレートを返す"""
    return _read_template("core/design-refactor.md")


@mcp.resource("adaptus://template/{template_name}")
def get_template_by_name(template_name: str) -> str:
    """指定されたテンプレートを返す"""
    return _read_template(f"core/{template_name}.md")


@mcp.tool()
def analyze_debt(
    paths: list[str], lang: str = "python", include_semantic: bool = True
) -> dict[str, Any]:
    """負債候補の分析を行う"""
    results: dict[str, Any] = {}
    for p in paths:
        path = Path(p)
        if not path.exists():
            results[p] = {"error": 1.0}
            continue
        code = _read_code(path)
        m: dict[str, Any] = (
            _basic_metrics(code)  # type: ignore
            if lang == "python"
            else {"loc": float(len(code.splitlines()))}
        )
        m["score"] = _score_formula(m)  # type: ignore

        # Add semantic analysis for Python
        if lang == "python" and include_semantic:
            semantic = _semantic_analysis(code)
            m["semantic_analysis"] = semantic
            # Adjust score based on semantic issues
            if semantic.get("summary", {}).get("total_issues", 0) > 0:
                m["score"] = min(m["score"] + 1.0, 10.0)
            if semantic.get("summary", {}).get("total_smells", 0) > 0:
                m["score"] = min(m["score"] + 0.5, 10.0)

        results[p] = m
    return results


@mcp.tool()
def score_debt(metrics: dict[str, float]) -> dict[str, Any]:
    """独自式でファイル別スコアを算出"""
    score = _score_formula(metrics)
    breakdown = {
        "mi_normalized": min(max((100.0 - metrics.get("mi", 0.0)) / 100.0, 0.0), 1.0),
        "cc_normalized": min(
            max((metrics.get("branches", 0.0) - 10.0) / 40.0, 0.0), 1.0
        ),
        "dup_normalized": min(max(metrics.get("dup_rate", 0.0), 0.0), 1.0),
        "td_normalized": min(max(metrics.get("td_ratio", 0.0), 0.0), 1.0),
    }
    return {
        "score": score,
        "breakdown": breakdown,
        "weights": {"mi": 0.35, "cc": 0.25, "dup": 0.20, "td": 0.20},
        "severity": "low" if score < 3.0 else "medium" if score < 7.0 else "high",
    }


@mcp.tool()
def generate_tests(
    target: str, framework: str = "pytest", test_type: str = "unit"
) -> dict[str, Any]:
    """テスト雛形を生成し補完指示を付与"""

    if framework == "pytest":
        if test_type == "integration":
            test_template = f'''#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Integration test suite for {target}
Generated by Adaptus MCP Server
"""

import pytest
from unittest.mock import Mock, patch
# Import the module to test
# import {target}


class Test{target.title()}Integration:
    """Integration tests for {target}"""

    @pytest.fixture(scope="class")
    def setup_integration(self):
        """Set up integration test environment"""
        # Setup database connections, external services, etc.
        pass

    def test_full_workflow(self, setup_integration):
        """Test complete workflow"""
        # Arrange
        # Act
        # Assert
        assert True  # Replace with actual test

    def test_external_service_integration(self, setup_integration):
        """Test integration with external services"""
        # Mock external dependencies
        with patch('external_module.api_call') as mock_api:
            mock_api.return_value = {{"status": "success"}}
            # Test integration
            assert True  # Replace with actual test

    @pytest.mark.slow
    def test_performance_integration(self, setup_integration):
        """Test performance under integration conditions"""
        # Performance-related integration tests
        assert True  # Replace with actual test
'''
        else:
            test_template = f'''#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Test suite for {target}
Generated by Adaptus MCP Server
"""

import pytest
from unittest.mock import Mock, patch, MagicMock
# Import the module to test
# import {target}


class Test{target.title()}:
    """Test cases for {target}"""

    def setup_method(self):
        """Set up test fixtures before each test method"""
        pass

    def teardown_method(self):
        """Clean up after each test method"""
        pass

    def test_initialization(self):
        """Test that {target} initializes correctly"""
        # Arrange
        # Act
        # Assert
        assert True  # Replace with actual test

    def test_main_functionality(self):
        """Test main functionality of {target}"""
        # Arrange
        # Act
        # Assert
        assert True  # Replace with actual test

    def test_error_handling(self):
        """Test error handling in {target}"""
        # Arrange
        # Act
        # Assert
        assert True  # Replace with actual test

    @pytest.mark.parametrize("input_data,expected", [
        # Add test cases here
        (None, None),
    ])
    def test_parameterized_cases(self, input_data, expected):
        """Test {target} with various inputs"""
        # Arrange
        # Act
        # Assert
        assert True  # Replace with actual test

    @pytest.fixture
    def sample_data(self):
        """Provide sample data for tests"""
        return {{"key": "value"}}

    def test_with_fixture(self, sample_data):
        """Test using custom fixture"""
        assert sample_data is not None


if __name__ == "__main__":
    pytest.main([__file__])
'''

    elif framework == "unittest":
        if test_type == "integration":
            test_template = f'''#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Integration test suite for {target}
Generated by Adaptus MCP Server
"""

import unittest
from unittest.mock import Mock, patch
# Import the module to test
# import {target}


class Test{target.title()}Integration(unittest.TestCase):
    """Integration tests for {target}"""

    @classmethod
    def setUpClass(cls):
        """Set up integration test environment"""
        # Setup database connections, external services, etc.
        pass

    def test_full_workflow(self):
        """Test complete workflow"""
        # Add your test code here
        pass

    def test_external_service_integration(self):
        """Test integration with external services"""
        with patch('external_module.api_call') as mock_api:
            mock_api.return_value = {{"status": "success"}}
            # Test integration
            pass


if __name__ == "__main__":
    unittest.main()
'''
        else:
            test_template = f'''#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Test suite for {target}
Generated by Adaptus MCP Server
"""

import unittest
from unittest.mock import Mock, patch, MagicMock
# Import the module to test
# import {target}


class Test{target.title()}(unittest.TestCase):
    """Test cases for {target}"""

    def setUp(self):
        """Set up test fixtures before each test method"""
        pass

    def tearDown(self):
        """Clean up after each test method"""
        pass

    def test_initialization(self):
        """Test that {target} initializes correctly"""
        # Add your test code here
        pass

    def test_main_functionality(self):
        """Test main functionality of {target}"""
        # Add your test code here
        pass

    def test_error_handling(self):
        """Test error handling in {target}"""
        # Add your test code here
        pass

    def test_with_mock(self):
        """Test using mock objects"""
        with patch('module.function') as mock_function:
            mock_function.return_value = "mocked_value"
            # Test with mock
            pass


if __name__ == "__main__":
    unittest.main()
'''

    else:  # Custom framework or other
        test_template = f'''#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Test suite for {target} - {framework} framework
Generated by Adaptus MCP Server
"""

# Add framework-specific imports here
# import {framework}

class Test{target.title()}:
    """Test cases for {target} using {framework}"""

    def setup_test_environment(self):
        """Set up test environment for {framework}"""
        pass

    def test_basic_functionality(self):
        """Basic functionality test"""
        # Framework-specific test implementation
        pass

    # Add more framework-specific tests here
'''

    framework_specific_instructions: dict[str, Any] = {
        "pytest": {
            "features": ["Parametrized testing", "Fixtures", "Markers", "Plugins"],
            "commands": {
                "run": "pytest test_{target.lower()}.py",
                "coverage": "pytest --cov={target} test_{target.lower()}.py",
                "verbose": "pytest -v test_{target.lower()}.py",
            },
        },
        "unittest": {
            "features": ["Built-in framework", "Test discovery", "Mock support"],
            "commands": {
                "run": "python -m unittest test_{target.lower()}.py",
                "discover": "python -m unittest discover",
                "verbose": "python -m unittest -v test_{target.lower()}.py",
            },
        },
    }

    instructions = f"""
    ## Test Implementation Instructions for {
        framework.upper()
    }

    1. **Import Statements**: Uncomment and update import statements
       for your target module
    2. **Test Cases**: Replace placeholder assertions with actual test logic
    3. **Fixtures**: Update setup_method/setUp with necessary test data
    4. **Edge Cases**: Add tests for boundary conditions and error scenarios
    5. **Mock Dependencies**: Use Mock/patch to isolate the unit under test
    6. **Assertions**: Ensure each test has clear, meaningful assertions

    ## Framework Features: {
        framework.upper()
    }
    """

    if framework in framework_specific_instructions:
        for feature in framework_specific_instructions[framework]["features"]:
            instructions += f"- {feature}\n"

        instructions += "\n### Commands:\n"
        for cmd_name, cmd in framework_specific_instructions[framework][
            "commands"
        ].items():
            instructions += f"- {cmd_name}: `{cmd}`\n"

    return {
        "template": test_template,
        "framework": framework,
        "test_type": test_type,
        "instructions": instructions,
        "next_steps": [
            f"Save the template to test_{target.lower()}.py",
            "Add proper imports for your module",
            "Implement actual test logic",
            (
                "Run with: "
                + framework_specific_instructions.get(framework, {})
                .get("commands", {})
                .get("run", f"python test_{target.lower()}.py")
            ),
        ],
    }


@mcp.tool()
def summarize(repo_path: str) -> dict[str, Any]:
    """ホットスポットと難所を集約"""
    repo = Path(repo_path)
    if not repo.exists():
        return {"error": f"Repository path not found: {repo_path}"}

    # Find Python files
    python_files = list(repo.rglob("*.py"))
    if not python_files:
        return {"error": "No Python files found in repository"}

    # Analyze each file
    file_analysis = []
    total_loc = 0.0
    hotspots: list[dict[str, Any]] = []
    complexity_issues = []

    for file_path in python_files:
        try:
            code = _read_code(file_path)
            metrics = _basic_metrics(code)
            metrics["score"] = _score_formula(metrics)

            relative_path = str(file_path.relative_to(repo))
            file_analysis.append(
                {
                    "path": relative_path,
                    "metrics": metrics,
                }
            )

            total_loc += metrics["loc"]

            # Identify hotspots (high complexity or large files)
            if metrics["score"] > 5.0 or metrics["loc"] > 200:
                hotspots.append(
                    {
                        "path": relative_path,
                        "score": metrics["score"],
                        "loc": metrics["loc"],
                        "reason": (
                            "High debt score"
                            if metrics["score"] > 5.0
                            else "Large file size"
                        ),
                    }
                )

            # Identify complexity issues
            if metrics["branches"] > 20 or metrics["funcs"] > 15:
                complexity_issues.append(
                    {
                        "path": relative_path,
                        "branches": metrics["branches"],
                        "functions": metrics["funcs"],
                        "avg_args": metrics["avg_args"],
                    }
                )

        except Exception as e:
            file_analysis.append(
                {
                    "path": str(file_path.relative_to(repo)),
                    "error": str(e),
                }
            )

    # Sort by debt score
    hotspots.sort(key=lambda x: x["score"], reverse=True)

    # Generate recommendations
    recommendations = []
    if hotspots:
        recommendations.append(
            f"Focus on {len(hotspots)} hotspot files with highest debt scores"
        )
    if complexity_issues:
        recommendations.append(
            f"Consider refactoring {len(complexity_issues)} files with high complexity"
        )
    if total_loc > 1000:
        recommendations.append("Large codebase detected - consider modularization")

    return {
        "repository": repo_path,
        "summary": {
            "total_files": len(python_files),
            "total_loc": total_loc,
            "avg_loc_per_file": total_loc / len(python_files) if python_files else 0,
            "hotspots_count": len(hotspots),
            "complexity_issues_count": len(complexity_issues),
        },
        "hotspots": hotspots[:10],  # Top 10 hotspots
        "complexity_issues": complexity_issues[:10],  # Top 10 complexity issues
        "recommendations": recommendations,
        "file_analysis": file_analysis,
        "next_steps": [
            "Review hotspot files for refactoring opportunities",
            "Analyze complexity issues for design improvements",
            "Consider breaking down large files into smaller modules",
            "Implement automated testing for high-risk areas",
        ],
    }


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
    plan = "関心分離を徹底し、状態と手続を" "各ドメインへ再配置する。"
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
