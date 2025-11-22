## ADDED Requirements
### Requirement: Debt Analysis Prompt Template
The system SHALL provide structured prompt templates for debt analysis.

#### Scenario: Sequential reasoning template
- **WHEN** using core/debt-analysis template
- **THEN** the system SHALL provide step-by-step analysis framework
- **AND** include maintainability, complexity, and coupling considerations

#### Scenario: Context-aware analysis
- **WHEN** applying debt analysis template
- **THEN** the system SHALL adapt analysis based on code context
- **AND** prioritize relevant metrics and patterns

### Requirement: Design Refactor Prompt Template
The system SHALL provide templates for design refactoring guidance.

#### Scenario: Domain separation guidance
- **WHEN** using core/design-refactor template
- **THEN** the system SHALL provide domain-driven design guidance
- **AND** include responsibility redistribution strategies

#### Scenario: Architectural pattern suggestions
- **WHEN** analyzing design issues
- **THEN** the system SHALL suggest appropriate architectural patterns
- **AND** provide implementation guidance for suggested patterns

### Requirement: Template Customization
The system SHALL allow customization of prompt templates.

#### Scenario: Custom template variables
- **WHEN** rendering prompt templates
- **THEN** the system SHALL support custom variable injection
- **AND** validate variable completeness before rendering

#### Scenario: Template composition
- **WHEN** creating complex analysis workflows
- **THEN** the system SHALL allow template composition
- **AND** maintain context across template boundaries

### Requirement: Prompt Validation
The system SHALL validate prompt templates for quality and completeness.

#### Scenario: Template syntax validation
- **WHEN** loading prompt templates
- **THEN** the system SHALL validate template syntax
- **AND** report errors with specific line references

#### Scenario: Content quality checks
- **WHEN** validating templates
- **THEN** the system SHALL check for required sections
- **AND** ensure template follows best practices
