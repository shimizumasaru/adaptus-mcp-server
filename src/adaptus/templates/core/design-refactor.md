# Design Refactoring Template

## Context
You are providing comprehensive design improvement suggestions for Python code. Your focus is on architectural patterns, domain separation, responsibility redistribution, and creating maintainable, scalable solutions.

## Design Philosophy

### 1. Clean Architecture Principles
- **Dependency Rule**: Dependencies point inward (domain → application → infrastructure)
- **Layer Separation**: Clear boundaries between presentation, business, and data layers
- **Use Case Isolation**: Application-specific business rules in dedicated use cases
- **Interface Segregation**: Small, focused interfaces for each concern

### 2. Domain-Driven Design (DDD)
- **Bounded Contexts**: Identify and implement clear domain boundaries
- **Ubiquitous Language**: Use consistent terminology across codebase
- **Domain Entities**: Model core business concepts with rich behavior
- **Value Objects**: Create immutable representations of domain concepts
- **Repository Pattern**: Abstract data access with domain-focused interfaces

### 3. SOLID Principles Application
- **Single Responsibility**: Each class has one reason to change
- **Open/Closed**: Open for extension, closed for modification
- **Liskov Substitution**: Subtypes are substitutable for base types
- **Interface Segregation**: Client-specific, cohesive interfaces
- **Dependency Inversion**: Depend on abstractions, not concretions

## Refactoring Methodology

### Phase 1: Current State Analysis
1. **Responsibility Mapping**
   - Document current responsibilities of each class/module
   - Identify mixed concerns and violations
   - Map data flow and control dependencies

2. **Architecture Assessment**
   - Evaluate current layering and separation
   - Identify architectural violations
   - Document coupling and cohesion issues

3. **Domain Identification**
   - Extract core business concepts
   - Identify cross-cutting concerns
   - Map business processes to code structure

### Phase 2: Target Architecture Design
1. **Domain Model Design**
   ```mermaid
   classDiagram
     class DomainEntity {
       +id: UUID
       +created_at: DateTime
       +updated_at: DateTime
       +validate()
       +business_rule()
     }
     
     class ValueObject {
       +value: Any
       +equals()
       +hash()
     }
     
     class Repository {
       +find(id)
       +save(entity)
       +delete(id)
     }
     
     class UseCase {
       +execute(request)
       +validate_request()
     }
     
     DomainEntity --> ValueObject
     UseCase --> Repository
     UseCase --> DomainEntity
   ```

2. **Layer Structure Definition**
   ```
   src/
   ├── domain/
   │   ├── entities/
   │   ├── value_objects/
   │   ├── repositories/
   │   └── services/
   ├── application/
   │   ├── use_cases/
   │   ├── services/
   │   └── dto/
   ├── infrastructure/
   │   ├── persistence/
   │   ├── external/
   │   └── config/
   └── interfaces/
       ├── api/
       ├── cli/
       └── web/
   ```

### Phase 3: Incremental Refactoring Plan
1. **Strangler Fig Pattern**
   - Gradually replace old components
   - Maintain backward compatibility
   - Use feature flags for gradual rollout

2. **Migration Steps**
   - Extract domain entities first
   - Implement repository interfaces
   - Create use case layer
   - Migrate infrastructure concerns
   - Update interface layer

## Implementation Guidelines

### 1. Entity Design
```python
class DomainEntity:
    """Base class for all domain entities"""
    
    def __init__(self, id: UUID):
        self._id = id
        self._created_at = datetime.utcnow()
        self._updated_at = datetime.utcnow()
    
    @property
    def id(self) -> UUID:
        return self._id
    
    def validate(self) -> List[ValidationError]:
        """Validate entity invariants"""
        raise NotImplementedError
    
    def update_timestamp(self):
        """Update the last modified timestamp"""
        self._updated_at = datetime.utcnow()
```

### 2. Repository Implementation
```python
class Repository(ABC):
    """Abstract base repository"""
    
    @abstractmethod
    def find(self, id: UUID) -> Optional[DomainEntity]:
        pass
    
    @abstractmethod
    def save(self, entity: DomainEntity) -> DomainEntity:
        pass
    
    @abstractmethod
    def delete(self, id: UUID) -> bool:
        pass
```

### 3. Use Case Pattern
```python
class UseCase(Generic[Request, Response]):
    """Base class for use cases"""
    
    def execute(self, request: Request) -> Response:
        self.validate_request(request)
        return self.process(request)
    
    def validate_request(self, request: Request):
        """Validate input request"""
        pass
    
    @abstractmethod
    def process(self, request: Request) -> Response:
        """Process the use case"""
        pass
```

## Output Format

```markdown
## Design Refactoring Plan

### Current Architecture Issues
1. **[Architecture Problem]**: [Location]
   - **Violation**: [Design principle broken]
   - **Impact**: [Negative consequences]
   - **Severity**: [Critical/High/Medium/Low]

### Target Architecture
```mermaid
[Include architecture diagram]
```

### Refactoring Strategy
1. **Phase 1: Domain Extraction** (Week 1-2)
   - Extract domain entities from existing classes
   - Define value objects for core concepts
   - Implement domain services for business logic

2. **Phase 2: Repository Implementation** (Week 2-3)
   - Define repository interfaces for each aggregate
   - Implement concrete repository classes
   - Set up dependency injection for repositories

3. **Phase 3: Use Case Layer** (Week 3-4)
   - Identify and implement use cases
   - Create request/response DTOs
   - Implement application services

4. **Phase 4: Infrastructure Migration** (Week 4-5)
   - Move external dependencies to infrastructure layer
   - Implement configuration management
   - Set up logging and monitoring

### Specific Recommendations
1. **Class: [ClassName]**
   - **Current Issues**: [List of problems]
   - **Refactoring Steps**: [Specific actions]
   - **New Design**: [Target structure]
   - **Benefits**: [Expected improvements]

### Migration Risk Assessment
- **Low Risk**: [Changes with minimal impact]
- **Medium Risk**: [Changes requiring careful testing]
- **High Risk**: [Changes affecting critical functionality]

### Success Metrics
- **Code Quality**: Improved maintainability index
- **Testability**: Increased test coverage
- **Performance**: No regression in response times
- **Flexibility**: Easier to add new features
```

## Best Practices Checklist

### Before Refactoring
- [ ] Comprehensive test coverage exists
- [ ] Current behavior is documented
- [ ] Performance baselines are established
- [ ] Stakeholder approval is obtained

### During Refactoring
- [ ] Changes are made incrementally
- [ ] Tests pass after each change
- [ ] Code review is performed
- [ ] Documentation is updated

### After Refactoring
- [ ] All tests pass
- [ ] Performance benchmarks are met
- [ ] Code review is approved
- [ ] Documentation is complete
- [ ] Team training is provided
