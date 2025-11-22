# Adaptus MCP Server - Usage Examples

## Overview

This document provides comprehensive examples of how to use the Adaptus MCP Server for code quality analysis, test generation, and design improvement.

## Resources

### 1. Design Guidelines

Access the latest design guidelines:

```
GET adaptus://guidelines/latest
```

**Response:**
```markdown
# Version: latest
# Updated: 1701234567.89

# Adaptus Design Guidelines
## Python Code Quality Standards
...
```

### 2. Core Prompts

Get core prompt templates:

```
GET adaptus://prompt/core
```

**Response:**
```markdown
# Core Prompt Templates
## Debt Analysis Template
...
```

### 3. Versioned Resources

Access specific versions:

```
GET adaptus://guidelines/v1.0
GET adaptus://prompt/v2.0/core
```

### 4. Analysis Templates

Get specialized templates:

```
GET adaptus://template/debt-analysis
GET adaptus://template/design-refactor
```

## Tools

### 1. Code Analysis

#### Basic Debt Analysis

```python
# Analyze specific files
result = analyze_debt([
    "src/main.py",
    "src/utils.py",
    "src/models.py"
])

# Response structure
{
    "src/main.py": {
        "loc": 150.0,
        "funcs": 8.0,
        "branches": 25.0,
        "avg_args": 2.5,
        "score": 4.2
    },
    "src/utils.py": {
        "loc": 80.0,
        "funcs": 5.0,
        "branches": 12.0,
        "avg_args": 1.8,
        "score": 2.1
    }
}
```

#### Enhanced Analysis with Semantic Analysis

```python
# Include semantic analysis for deeper insights
result = analyze_debt(
    ["src/complex.py"],
    lang="python",
    include_semantic=True
)

# Enhanced response with semantic insights
{
    "src/complex.py": {
        "loc": 300.0,
        "funcs": 15.0,
        "branches": 45.0,
        "avg_args": 4.2,
        "score": 7.8,
        "semantic_analysis": {
            "issues": [
                {
                    "type": "long_function",
                    "name": "process_data",
                    "line": 45,
                    "length": 85,
                    "severity": "medium"
                },
                {
                    "type": "too_many_params",
                    "name": "complex_function",
                    "line": 120,
                    "param_count": 9,
                    "severity": "high"
                }
            ],
            "smells": [
                {
                    "type": "deep_nesting",
                    "name": "nested_logic",
                    "line": 200,
                    "nesting_level": 5,
                    "severity": "high"
                }
            ],
            "patterns": [],
            "summary": {
                "total_issues": 2,
                "total_smells": 1,
                "total_patterns": 0
            }
        }
    }
}
```

### 2. Debt Scoring

#### Calculate Custom Scores

```python
# Score based on custom metrics
metrics = {
    "loc": 200.0,
    "funcs": 12.0,
    "branches": 30.0,
    "avg_args": 3.5,
    "mi": 75.0,
    "dup_rate": 0.08,
    "td_ratio": 0.12
}

result = score_debt(metrics)

# Detailed scoring response
{
    "score": 5.8,
    "breakdown": {
        "mi_normalized": 0.25,
        "cc_normalized": 0.5,
        "dup_normalized": 0.08,
        "td_normalized": 0.12
    },
    "weights": {
        "mi": 0.35,
        "cc": 0.25,
        "dup": 0.20,
        "td": 0.20
    },
    "severity": "medium"
}
```

### 3. Test Generation

#### Generate Unit Tests with Pytest

```python
# Generate pytest unit tests
result = generate_tests(
    target="user_service",
    framework="pytest",
    test_type="unit"
)

# Response includes template and instructions
{
    "template": "#!/usr/bin/env python3\n# -*- coding: utf-8 -*-\n...",
    "framework": "pytest",
    "test_type": "unit",
    "instructions": "## Test Implementation Instructions for PYTEST\n...",
    "next_steps": [
        "Save the template to test_user_service.py",
        "Add proper imports for your module",
        "Implement actual test logic",
        "Run with: pytest test_user_service.py"
    ]
}
```

#### Generate Integration Tests

```python
# Generate integration tests
result = generate_tests(
    target="payment_service",
    framework="pytest",
    test_type="integration"
)

# Integration test template includes fixtures and external service mocking
```

#### Generate Tests with Unittest

```python
# Generate unittest-based tests
result = generate_tests(
    target="data_processor",
    framework="unittest",
    test_type="unit"
)
```

### 4. Repository Analysis

#### Analyze Entire Repository

```python
# Analyze repository for hotspots and issues
result = summarize("/path/to/your/repository")

# Comprehensive repository analysis
{
    "repository": "/path/to/your/repository",
    "summary": {
        "total_files": 25,
        "total_loc": 3500,
        "avg_loc_per_file": 140.0,
        "hotspots_count": 4,
        "complexity_issues_count": 7
    },
    "hotspots": [
        {
            "path": "src/legacy/old_module.py",
            "score": 8.5,
            "loc": 450,
            "reason": "High debt score"
        },
        {
            "path": "src/core/processor.py",
            "score": 6.2,
            "loc": 280,
            "reason": "Large file size"
        }
    ],
    "complexity_issues": [
        {
            "path": "src/utils/helpers.py",
            "branches": 35,
            "functions": 18,
            "avg_args": 4.8
        }
    ],
    "recommendations": [
        "Focus on 4 hotspot files with highest debt scores",
        "Consider refactoring 7 files with high complexity",
        "Large codebase detected - consider modularization"
    ],
    "next_steps": [
        "Review hotspot files for refactoring opportunities",
        "Analyze complexity issues for design improvements",
        "Consider breaking down large files into smaller modules",
        "Implement automated testing for high-risk areas"
    ]
}
```

## Complete Workflow Examples

### Example 1: New Project Analysis

```python
# Step 1: Analyze the entire codebase
repo_analysis = summarize("/path/to/new_project")

# Step 2: Focus on high-priority hotspots
hotspot_files = [h["path"] for h in repo_analysis["hotspots"][:3]]
detailed_analysis = analyze_debt(hotspot_files, include_semantic=True)

# Step 3: Generate tests for critical modules
for file_path in hotspot_files:
    module_name = Path(file_path).stem
    test_result = generate_tests(module_name, "pytest", "unit")
    # Save and implement tests

# Step 4: Create improvement plan
print("Repository Summary:", repo_analysis["summary"])
print("Top Recommendations:", repo_analysis["recommendations"])
```

### Example 2: Legacy Code Refactoring

```python
# Step 1: Identify problematic areas
legacy_analysis = analyze_debt(
    ["src/legacy/module1.py", "src/legacy/module2.py"],
    include_semantic=True
)

# Step 2: Get refactoring guidance
design_template = get_template_by_name("design-refactor")

# Step 3: Generate comprehensive tests before refactoring
for file_path in legacy_analysis.keys():
    module_name = Path(file_path).stem
    # Generate both unit and integration tests
    unit_tests = generate_tests(module_name, "pytest", "unit")
    integration_tests = generate_tests(module_name, "pytest", "integration")

# Step 4: Create refactoring plan based on analysis
for file_path, metrics in legacy_analysis.items():
    if metrics["score"] > 7.0:
        print(f"High priority refactoring needed for {file_path}")
        print(f"Issues: {metrics['semantic_analysis']['summary']}")
```

### Example 3: Continuous Integration Integration

```python
# CI pipeline analysis script
def ci_quality_check(repo_path, threshold_score=6.0):
    """Run quality checks in CI pipeline"""
    
    # Analyze repository
    summary = summarize(repo_path)
    
    # Check if any hotspots exceed threshold
    critical_hotspots = [
        h for h in summary["hotspots"] 
        if h["score"] > threshold_score
    ]
    
    if critical_hotspots:
        print(f"❌ CI FAILED: {len(critical_hotspots)} files exceed quality threshold")
        for hotspot in critical_hotspots:
            print(f"  - {hotspot['path']}: score {hotspot['score']}")
        return False
    
    # Generate detailed report
    analysis = analyze_debt([
        h["path"] for h in summary["hotspots"]
    ], include_semantic=True)
    
    print(f"✅ CI PASSED: Code quality is acceptable")
    print(f"Repository: {summary['summary']['total_files']} files, {summary['summary']['total_loc']} LOC")
    return True

# Usage in CI
if __name__ == "__main__":
    success = ci_quality_check(".", threshold_score=5.0)
    exit(0 if success else 1)
```

## Best Practices

### 1. Analysis Workflow

1. **Start with repository summary** to get overview
2. **Focus on hotspots** identified by high debt scores
3. **Use semantic analysis** for detailed code insights
4. **Generate tests** before making changes
5. **Create refactoring plan** using design templates

### 2. Test Generation

1. **Generate unit tests** for individual components
2. **Create integration tests** for component interactions
3. **Use framework-specific features** (pytest fixtures, unittest mocks)
4. **Customize templates** based on project needs

### 3. Quality Gates

1. **Set score thresholds** for different environments
2. **Monitor trends** over time
3. **Focus on high-impact improvements** first
4. **Balance technical debt** with feature delivery

### 4. Team Collaboration

1. **Share analysis results** with the team
2. **Use consistent templates** across projects
3. **Document decisions** made during refactoring
4. **Track improvements** in quality metrics

## Configuration

### Environment Variables

```bash
# Optional configuration
export ADAPTUS_CACHE_DIR=/path/to/cache
export ADAPTUS_LOG_LEVEL=INFO
export ADAPTUS_THRESHOLD_SCORE=5.0
```

### Custom Templates

You can add custom templates by placing them in:
```
src/adaptus/templates/custom/
├── my-analysis-template.md
└── my-design-template.md
```

Then access them via:
```
GET adaptus://template/my-analysis-template
GET adaptus://template/my-design-template
```

## Troubleshooting

### Common Issues

1. **Resource not found errors**: Check file paths and permissions
2. **High memory usage**: Analyze smaller batches of files
3. **Slow analysis**: Consider caching results for unchanged files
4. **Template errors**: Validate template syntax and required sections

### Performance Tips

1. **Use semantic analysis selectively** for large codebases
2. **Cache repository summaries** for repeated analysis
3. **Parallelize test generation** for multiple modules
4. **Monitor resource usage** in CI environments

## Integration Examples

### VS Code Extension

```typescript
// Example VS Code extension integration
const analysis = await mcpClient.call('analyze_debt', {
    paths: document.uri.fsPath,
    include_semantic: true
});

// Show results in diagnostics
const diagnostics = analysis[document.uri.fsPath];
if (diagnostics.score > 5.0) {
    showWarningMessage(`High technical debt: ${diagnostics.score}/10`);
}
```

### GitHub Actions

```yaml
# .github/workflows/quality-check.yml
name: Code Quality Check
on: [push, pull_request]

jobs:
  quality:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v2
      - name: Setup Python
        uses: actions/setup-python@v2
        with:
          python-version: '3.9'
      
      - name: Install Adaptus
        run: pip install adaptus-mcp
      
      - name: Run Quality Analysis
        run: |
          python -c "
          from adaptus.server import summarize, analyze_debt
          summary = summarize('.')
          if summary['summary']['hotspots_count'] > 0:
            print('Hotspots found:', summary['hotspots'])
            exit(1)
          "
```

This comprehensive guide should help you integrate Adaptus MCP Server into your development workflow effectively.
