## ADDED Requirements
### Requirement: Debt Scoring Tool
The system SHALL provide a dedicated tool for debt scoring calculation.

#### Scenario: Score individual metrics
- **WHEN** calling score_debt(metrics)
- **THEN** the system SHALL calculate debt score using custom formula
- **AND** return detailed scoring breakdown

#### Scenario: Batch scoring
- **WHEN** providing multiple metrics
- **THEN** the system SHALL calculate scores for all metrics
- **AND** maintain scoring consistency across calls

### Requirement: Test Generation Tool
The system SHALL generate test templates for various frameworks.

#### Scenario: Generate pytest tests
- **WHEN** calling generate_tests(target, framework="pytest")
- **THEN** the system SHALL generate pytest-compatible test cases
- **AND** include setup, teardown, and assertion templates

#### Scenario: Generate unittest tests
- **WHEN** calling generate_tests(target, framework="unittest")
- **THEN** the system SHALL generate unittest-compatible test cases
- **AND** follow Python unittest conventions

#### Scenario: Framework detection
- **WHEN** framework is not specified
- **THEN** the system SHALL detect appropriate framework from code
- **AND** default to pytest for modern Python projects

### Requirement: Repository Summary Tool
The system SHALL analyze and summarize repository hotspots.

#### Scenario: Analyze repository structure
- **WHEN** calling summarize(repo_path)
- **THEN** the system SHALL identify complex files and hotspots
- **AND** return prioritized list of areas needing attention

#### Scenario: Generate improvement recommendations
- **WHEN** analyzing repository
- **THEN** the system SHALL provide specific improvement suggestions
- **AND** estimate effort and impact for each recommendation

## MODIFIED Requirements
### Requirement: Enhanced Debt Analysis
The analyze_debt tool SHALL incorporate semantic analysis capabilities.

#### Scenario: Semantic code analysis
- **WHEN** analyzing Python code
- **THEN** the system SHALL identify code smells and anti-patterns
- **AND** provide contextual explanations for detected issues

#### Scenario: Multi-language support
- **WHEN** analyzing non-Python files
- **THEN** the system SHALL provide basic metrics analysis
- **AND** indicate limited analysis capabilities for unsupported languages
