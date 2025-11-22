# Technical Debt Analysis Template

## Context
You are analyzing Python code for technical debt and maintainability issues. Your goal is to identify code smells, complexity issues, and areas that need refactoring, then provide actionable recommendations.

## Analysis Framework

### 1. Code Quality Assessment
- **Complexity Analysis**: Identify functions with high cyclomatic complexity
- **Code Structure**: Evaluate function length, class size, and parameter counts
- **Naming Conventions**: Assess clarity and consistency of identifiers
- **Documentation**: Check for adequate docstrings and comments

### 2. Design Pattern Evaluation
- **Single Responsibility Principle**: Verify each component has one clear purpose
- **DRY Violations**: Identify code duplication opportunities
- **Cohesion & Coupling**: Evaluate component relationships
- **SOLID Principles**: Assess adherence to design principles

### 3. Maintainability Indicators
- **Error Handling**: Evaluate exception handling patterns
- **Testing**: Assess testability and test coverage
- **Dependencies**: Analyze import patterns and external dependencies
- **Configuration**: Check for hardcoded values and magic numbers

## Sequential Analysis Process

### Step 1: Initial Code Survey
1. **Structure Overview**: Map the overall code organization
2. **Complexity Hotspots**: Identify immediately obvious issues
3. **Pattern Recognition**: Look for recurring anti-patterns
4. **Dependency Mapping**: Understand component relationships

### Step 2: Detailed Component Analysis
1. **Function-Level Review**: Examine each function for specific issues
2. **Class-Level Assessment**: Evaluate class design and responsibilities
3. **Module-Level Evaluation**: Assess overall module organization
4. **Interface Analysis**: Review API design and contracts

### Step 3: Impact Assessment
1. **Severity Classification**: Categorize issues by impact level
2. **Effort Estimation**: Estimate refactoring complexity
3. **Risk Assessment**: Identify potential risks of changes
4. **Priority Ranking**: Order issues by business impact

### Step 4: Recommendation Formulation
1. **Specific Actions**: Provide concrete refactoring steps
2. **Design Improvements**: Suggest architectural enhancements
3. **Best Practices**: Recommend coding standard improvements
4. **Migration Strategy**: Outline incremental improvement plan

## Output Format

```markdown
## Technical Debt Analysis Report

### Executive Summary
- **Overall Debt Score**: [0-10 scale]
- **Critical Issues**: [Number and type]
- **Recommended Priority**: [Immediate/Short-term/Long-term]

### High Priority Issues
1. **[Issue Type]**: [Specific location]
   - **Problem**: [Clear description]
   - **Impact**: [Why it matters]
   - **Complexity**: [Low/Medium/High]
   - **Recommendation**: [Specific fix steps]

### Medium Priority Issues
[Similar format for medium priority items]

### Low Priority Issues
[Similar format for low priority items]

### Design Recommendations
1. **Architectural Improvements**
   - [Specific design changes]
   - [Benefits and trade-offs]

2. **Code Organization**
   - [Structural improvements]
   - [File/module reorganization]

### Quick Wins
- [Easy improvements with high impact]
- [Low-effort, high-benefit changes]

### Next Steps
1. **Immediate Actions** (This week)
   - [Specific tasks]
2. **Short-term Goals** (This month)
   - [Planned improvements]
3. **Long-term Strategy** (This quarter)
   - [Strategic changes]
```

## Analysis Guidelines

### Severity Classification
- **Critical**: Security risks, data corruption, system failures
- **High**: Performance issues, maintainability blockers
- **Medium**: Code quality issues, potential bugs
- **Low**: Style issues, minor improvements

### Recommendation Criteria
- **Feasibility**: Can be implemented with available resources
- **Impact**: Provides measurable improvement
- **Risk**: Low probability of introducing new issues
- **Alignment**: Supports project goals and constraints

## Quality Metrics
- **Debt Score Reduction**: Target 30% reduction in high-priority debt
- **Code Coverage**: Maintain or improve test coverage
- **Performance**: No regression in execution time
- **Maintainability**: Improve code readability and documentation
