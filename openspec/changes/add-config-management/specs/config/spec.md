## ADDED Requirements
### Requirement: Configuration File Support
The system SHALL support loading configuration from external files.

#### Scenario: Load TOML configuration
- **WHEN** a config.toml file exists in the project root
- **THEN** the system SHALL load and apply the configuration
- **AND** override default values with file settings

#### Scenario: Missing configuration file
- **WHEN** no configuration file exists
- **THEN** the system SHALL use built-in default configuration
- **AND** continue normal operation

### Requirement: Parameter Customization
The system SHALL allow customization of analysis parameters.

#### Scenario: Custom debt scoring weights
- **WHEN** user specifies custom weights in configuration
- **THEN** the debt scoring SHALL use the provided weights
- **AND** validate that weights sum to 1.0

#### Scenario: Custom analysis thresholds
- **WHEN** user defines custom complexity thresholds
- **THEN** the analysis SHALL use these thresholds for scoring
- **AND** provide warnings for invalid threshold values

### Requirement: Configuration Validation
The system SHALL validate configuration values before applying them.

#### Scenario: Invalid configuration values
- **WHEN** configuration contains invalid values
- **THEN** the system SHALL reject the configuration
- **AND** provide clear error messages with fix suggestions

#### Scenario: Configuration schema validation
- **WHEN** loading configuration file
- **THEN** the system SHALL validate against defined schema
- **AND** report schema violations with line numbers

## MODIFIED Requirements
### Requirement: MCP Server Initialization
The server SHALL initialize with configuration-based parameters instead of hardcoded values.

#### Scenario: Server startup with custom config
- **WHEN** server starts with custom configuration
- **THEN** all MCP tools SHALL use the configured parameters
- **AND** reflect the configuration in tool responses

#### Scenario: Configuration hot reload
- **WHEN** configuration file changes during operation
- **THEN** the server SHALL log the change
- **AND** require restart to apply new configuration
