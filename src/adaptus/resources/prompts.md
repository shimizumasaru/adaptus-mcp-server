# Core Prompt Templates

## Debt Analysis Template

### Context
You are analyzing Python code for technical debt and maintainability issues. Focus on identifying code smells, complexity issues, and areas that need refactoring.

### Analysis Framework

#### 1. Maintainability Assessment
- **Code Complexity**: Identify functions with high cyclomatic complexity
- **Code Length**: Flag overly long functions and classes
- **Parameter Count**: Watch for functions with too many parameters
- **Nesting Depth**: Identify deeply nested code blocks

#### 2. Design Pattern Evaluation
- **Single Responsibility**: Check if classes/functions have one clear purpose
- **DRY Violations**: Look for code duplication
- **Cohesion**: Assess how well-related code is grouped together
- **Coupling**: Evaluate dependencies between components

#### 3. Code Quality Indicators
- **Naming**: Are variable/function/class names descriptive?
- **Comments**: Is there appropriate documentation?
- **Error Handling**: Are exceptions handled properly?
- **Testing**: Is the code testable and well-tested?

### Sequential Reasoning Steps

1. **Initial Assessment**: Scan the code structure and identify obvious issues
2. **Detailed Analysis**: Examine each function/class for specific problems
3. **Pattern Recognition**: Identify recurring anti-patterns
4. **Impact Evaluation**: Assess the severity and priority of each issue
5. **Recommendation Formulation**: Provide specific, actionable improvements

### Output Format

```
## Technical Debt Analysis

### High Priority Issues
1. **[Issue Type]**: [Specific location]
   - **Problem**: [Description]
   - **Impact**: [Why it matters]
   - **Recommendation**: [How to fix]

### Medium Priority Issues
[Similar format]

### Low Priority Issues
[Similar format]

### Overall Assessment
- **Debt Score**: [0-10 scale]
- **Key Areas**: [Main problem areas]
- **Quick Wins**: [Easy improvements]
```

## Design Refactor Template

### Context
You are providing design improvement suggestions for Python code. Focus on architectural patterns, domain separation, and responsibility redistribution.

### Design Principles

#### 1. Domain-Driven Design
- **Bounded Contexts**: Identify clear domain boundaries
- **Ubiquitous Language**: Use consistent terminology
- **Domain Entities**: Model core business concepts
- **Value Objects**: Create immutable concept representations

#### 2. Clean Architecture
- **Dependency Rule**: Dependencies point inward
- **Layer Separation**: Distinct presentation, business, and data layers
- **Use Cases**: Application-specific business rules
- **Interface Segregation**: Small, focused interfaces

#### 3. SOLID Principles Application
- **Single Responsibility**: One reason to change
- **Open/Closed**: Open for extension, closed for modification
- **Liskov Substitution**: Subtypes must be substitutable
- **Interface Segregation**: Client-specific interfaces
- **Dependency Inversion**: Depend on abstractions

### Refactoring Strategy

#### Phase 1: Structure Analysis
1. Identify current responsibilities
2. Map dependencies and coupling
3. Spot violation of design principles
4. Document current architecture issues

#### Phase 2: Domain Separation
1. Extract core business logic
2. Separate infrastructure concerns
3. Isolate presentation layer
4. Define clear interfaces

#### Phase 3: Responsibility Redistribution
1. Move methods to appropriate classes
2. Extract cohesive modules
3. Implement design patterns
4. Create abstraction layers

### Output Format

```
## Design Refactoring Plan

### Current Issues
1. **[Architecture Problem]**: [Location]
   - **Violation**: [Design principle broken]
   - **Consequences**: [Negative impact]

### Proposed Structure
```mermaid
classDiagram
  [New class relationships]
```

### Refactoring Steps
1. **Step 1**: [Specific action]
   - **Files to modify**: [List]
   - **Risk level**: [Low/Medium/High]

2. **Step 2**: [Continue with steps...]

### Benefits
- **Maintainability**: [How it improves]
- **Testability**: [Testing improvements]
- **Flexibility**: [Future benefits]
```

## Customization Guidelines

### Template Variables
- `{project_context}`: Specific project information
- `{code_focus}`: Particular areas of concern
- `{priority_level}`: Analysis depth required
- `{framework}`: Relevant framework constraints

### Context Adaptation
- Adjust terminology based on domain
- Modify focus areas based on project type
- Scale recommendations based on team size
- Consider existing architectural decisions
