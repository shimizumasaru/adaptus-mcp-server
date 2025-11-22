## ADDED Requirements
### Requirement: Design Guidelines Resource
The system SHALL provide design guidelines as an MCP resource.

#### Scenario: Access latest guidelines
- **WHEN** client requests adaptus://guidelines/latest
- **THEN** the system SHALL return current design guidelines
- **AND** include Python best practices and architectural patterns

#### Scenario: Guidelines versioning
- **WHEN** guidelines are updated
- **THEN** the system SHALL maintain version history
- **AND** allow access to specific versions via adaptus://guidelines/v{version}

### Requirement: Core Prompt Templates Resource
The system SHALL provide prompt templates as an MCP resource.

#### Scenario: Access core prompts
- **WHEN** client requests adaptus://prompt/core
- **THEN** the system SHALL return core prompt templates
- **AND** include debt-analysis and design-refactor templates

#### Scenario: Template rendering
- **WHEN** accessing prompt templates
- **THEN** the system SHALL support variable substitution
- **AND** provide context-aware template customization

### Requirement: Resource Caching
The system SHALL cache resources for performance optimization.

#### Scenario: Resource cache hit
- **WHEN** requesting frequently accessed resources
- **THEN** the system SHALL serve from cache
- **AND** update cache when underlying files change

#### Scenario: Cache invalidation
- **WHEN** resource files are modified
- **THEN** the system SHALL invalidate relevant cache entries
- **AND** refresh on next access
