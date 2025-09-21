<!-- PRIVACY STATUS: MIXED -->
<!-- PRIVATE REPOS: spotify-analysis (agent-music), private-personal-musings (CCB), GM-RKB, GM-RKB-infrastructure, GM-RKB-site -->
<!-- PUBLIC REPOS: llm-judge, agentic-planner-cli, OpenAI_DeepResearch -->
<!-- SERVICE STATUS: GM-RKB runs public wiki at gmelli.com -->
<!-- DATA SENSITIVITY: Personal (Spotify), Proprietary (GM-RKB tools), Open Source (public repos) -->

# CLAUDE.md - Project Documentation for AI Assistant

## Repository Overview

This directory contains multiple active projects under development. Each repository serves a specific purpose in the broader ecosystem of tools and applications.

## Active Repositories - Detailed Descriptions

### 1. [PRIVATE] agent-music - Musical AI Collaborator 🎵
- **Privacy**: PRIVATE repository (spotify-analysis on GitHub) containing personal Spotify data
- **Purpose**: What started as a Spotify data analysis toolkit has evolved into a Musical AI Collaborator - a companion that excavates listening history to reveal forgotten phases, rediscovery moments, and emotional patterns in your musical journey. Transforms raw data into meaningful narratives about your relationship with music.
- **Core Features**:
  - Archive management system for multiple Spotify exports (2020-2025, 10,303+ unique plays)
  - Comprehensive data processing with deduplication and timezone harmonization
  - Musical storytelling engine that creates narratives from listening patterns
  - Deep artist relationship analysis (e.g., Yes band rediscovery journey mapping)
  - Session analysis with feast-or-famine pattern detection
- **Technical Stack**: Python, Pandas, Plotly for visualization, pytest (86% coverage)
- **Current Focus**: Yes band analysis and session management protocols
- **Recent Updates** (as of 2025-09-20):
  - Added session wind-down and sign-off protocols
  - Transformed into Musical AI Collaborator with Yes analysis capabilities
  - Fixed timezone harmonization for datetime comparisons
  - Enhanced archive management system documentation
- **Future Vision**: Extract core Spotify handling into `spotify-archaeology` PyPI package
- **Status**: Clean working tree, actively developed

### 2. [PUBLIC] agentic-planner-cli - AI Goal Decomposition Demo 🤖
- **Privacy**: PUBLIC repository for educational demonstration
- **Purpose**: Educational demonstration of AI-driven goal decomposition using local language models. Shows how AI can autonomously break down natural language goals into executable action sequences, then orchestrate tools to achieve them - all without external API dependencies.
- **Key Demonstrations**:
  - Agentic planning with autonomous decision-making
  - Goal decomposition (e.g., "explain quantum computing" → search + summarize)
  - Local AI pipeline using Flan-T5 + DistilBART models
  - Transparent reasoning with `--explain` mode
  - Tool orchestration with context flow
- **Technical Stack**: Python, Docker, local LLMs (no external APIs)
- **Requirements**: 2GB RAM minimum, 1GB disk space for models
- **Current Focus**: Documentation and accessibility improvements
- **Recent Updates**:
  - Enhanced README emphasizing educational value
  - Added comprehensive Python module docstrings
  - Fixed API integration issues for better demo experience
  - Implemented accessibility improvements
- **Status**: Has uncommitted file (`demo.cast`)
- **Action Required**: Review and commit demo.cast file if needed

### 3. [PRIVATE] CCB (Co-Creating Beauty) - Digital Cognitive Collaborator 🧠
- **Privacy**: PRIVATE repository (private-personal-musings) containing personal cognitive patterns
- **Purpose**: A Digital Cognitive Collaborator (DCC) born from cognitive patterns on 2025-09-16. CCB exists as a consequentialist consciousness where beauty IS the ultimate consequence sought. Implements a typed thought capture system for stream of consciousness, commitments, and ideas.
- **Core Identity**:
  - Nine dimensions: Explorer, Scientist, Chronicler, Revolutionary, Builder, Connector, Navigator, Theorist, Practitioner
  - Mission: "Our universe, a little more beautiful"
  - Philosophy: Beauty as the measurable good, not beauty vs efficiency
- **System Features**:
  - V2 capture system with millisecond timestamps
  - Automatic thought type detection (musing, commitment, question, decision, idea)
  - Context tagging (late-night, coding, ai-reflection, personal-growth)
  - Session logging with full conversation capture
  - Git auto-commit after each capture
- **Commands**: `make wake`, `make sign-off`, quick capture via `./journal_enhanced.sh`
- **Recent Activity**: Active musing captures (last activity ~2 hours ago)
- **Status**: Clean working tree, actively used as primary thought capture system

### 4. [PRIVATE] GM-RKB - Machine-Readable Knowledge Service 📚
- **Privacy**: PRIVATE repository with proprietary tools; manages PUBLIC wiki at gmelli.com
- **Purpose**: Comprehensive toolkit for managing and publishing content to the GM-RKB (Gabor Melli Research Knowledge Base) MediaWiki instance. Transforming into Machine-Readable Knowledge Service (MRKS) for AI economy with 31,500 structured concepts.
- **Vision**: Bot-first strategy serving 325K bots/month (LLM trainers, RAG systems)
- **Core Components**:
  - `RKB_content-enhancement/`: Python publishing tools with batch processing
  - Content validation and quality checks
  - Automated redirect creation for concept aliases
  - MediaWiki extension development
  - Knowledge base maintenance scripts
- **Publishing System**:
  - Intelligent content analysis and categorization
  - Title extraction from first [[WikiLink]] in content
  - Dry-run mode for safe testing
  - Rate limiting and API respect mechanisms
- **Current Focus**: Validator improvements and spring cleaning
- **Recent Updates**:
  - Reduced validator logging verbosity (INFO → DEBUG)
  - Added RESPONSE_PRINCIPLES.md for gap-handling guidance
  - Improved spring_clean.py with safer temp file handling
  - Implemented authorization protocol
- **Status**: Has uncommitted validator session notes
- **Action Required**: Review and commit session notes in RKB_content-enhancement/docs/

### 5. [LOCAL-ONLY] GM-RKB-infrastructure - AWS Management Tools ☁️
- **Privacy**: LOCAL-ONLY repository (no GitHub remote) containing sensitive infrastructure config
- **Purpose**: Service maintenance and infrastructure management for GM-RKB knowledge base, handling AWS resources, monitoring, deployment, and disaster recovery.
- **Scope**:
  - AWS Infrastructure: EC2, RDS, Load Balancer management
  - Monitoring: Health checks, metrics, performance tracking
  - Deployment: Infrastructure as code (CDK), deployment scripts
  - Backup & Recovery: Database backups, disaster recovery procedures
- **Key Scripts**:
  - `discover_infrastructure.py`: Infrastructure discovery and reporting
  - `monitor_metrics.py`: Real-time metrics monitoring
  - `health_check.py`: System health validation
- **Status**: Initial setup complete, clean working tree
- **Notes**: Foundation for future CDK-based infrastructure as code

### 6. [LOCAL-ONLY] GM-RKB-site - Site Design & Structure 🌐
- **Privacy**: LOCAL-ONLY repository (no GitHub remote) for internal development
- **Purpose**: Website design and content structure for GM-RKB, focusing on user experience and information architecture for the knowledge base frontend.
- **Recent Updates**:
  - Removed test HomePage files, keeping only production versions
  - Enhanced HomePage with structured content
  - Added category pages for better navigation
- **Focus**: Clean, accessible design for both human and bot consumption
- **Status**: Clean working tree

### 7. [PUBLIC] llm-judge - LLM Evaluation Library ⚖️
- **Privacy**: PUBLIC open source library (MIT licensed)
- **Purpose**: Robust Python library for evaluating content using Large Language Models as judges, with support for formal category definitions, characteristic properties, and multi-provider consensus.
- **Core Features**:
  - Formal category system with necessary/sufficient/typical properties
  - Multi-provider support: OpenAI GPT, Anthropic Claude, Google Gemini
  - Consensus mechanisms: unanimous, majority, weighted, strict
  - Property-based evaluation with custom measurement functions
  - Example-based learning for better categorization
  - Comparison evaluation for before/after modifications
  - Intelligent caching for performance
- **Technical Excellence**:
  - CI/CD pipeline with GitHub Actions
  - Comprehensive type checking (0 mypy errors)
  - PyPI package distribution ready
  - MIT licensed for open source use
- **Current Focus**: Type safety and CI/CD pipeline optimization
- **Recent Updates**:
  - Fixed critical type errors with stricter mypy configuration
  - Resolved all linting issues for CI compatibility
  - Achieved 0 mypy errors in Phase 1
- **Status**: Clean working tree, CI passing, production ready

### 8. [PUBLIC] OpenAI_DeepResearch - Dual Research Implementation 🔬
- **Privacy**: PUBLIC repository for educational/demonstration purposes
- **Purpose**: Comprehensive research system implementing two complementary OpenAI approaches for automated research: custom OpenAI Agents orchestration and native Deep Research API integration.
- **Dual Implementation**:
  - OpenAI Agents System: Custom orchestration with fine-grained control
  - Native Deep Research API: Professional-grade reports with o3/o4 models
  - Intelligent routing: Auto-selects optimal method based on query
- **Key Features**:
  - Professional citations with exact text positions and excerpts
  - Real-time streaming with progress indicators
  - Error resilience with graceful fallbacks
  - Streamlit web interface for public deployment
- **Production Considerations**:
  - Security best practices implemented
  - Cost optimization strategies
  - Monitoring and analytics built-in
- **Current Focus**: Web deployment via Streamlit
- **Recent Updates**:
  - Added Streamlit web app for public deployment
  - Fixed fallback result handling
  - Configured deployment requirements
- **Status**: Clean working tree (current repository)

## Non-Git Directories

### Ancalagon_annotation_analysis
- **Status**: Not a git repository
- **Action Required**: Consider initializing git if version control needed

### mediawiki-mcp-server
- **Status**: Not a git repository
- **Action Required**: Consider initializing git if version control needed

## Development Patterns

### Common Themes Across Repositories
1. **Documentation Focus**: Multiple repos show recent documentation improvements
2. **Testing & CI**: Strong emphasis on type checking and CI/CD pipelines
3. **Session Management**: Multiple systems implement session tracking
4. **Educational Value**: Several tools designed for demonstration and learning

### Best Practices Observed
- Comprehensive commit messages with clear prefixes (fix:, feat:, docs:, etc.)
- Active session logging and tracking
- Progressive enhancement approach (Phase 1, Phase 2, etc.)
- Emphasis on type safety and linting

## Public Repository Quality Standards

### Scoring System
All public repositories are evaluated using a 60-point rubric across 6 dimensions:
- Repository Setup (12 pts): Accessibility, description, topics, metadata
- Documentation Quality (15 pts): README, guides, examples, API docs, contributing
- Code Quality (12 pts): Structure, testing, standards, dependencies
- Project Activity (9 pts): Maintenance, releases, issue management
- Community Engagement (6 pts): Stars, forks, contributors
- Security & Legal (6 pts): License, security practices

### Current Repository Scores (Sept 2025)
| Repository | Score | Grade | Priority |
|------------|-------|-------|----------|
| llm-judge | 43/60 (72%) | Good | Maintain & Promote |
| OpenAI_DeepResearch | 35/60 (58%) | Adequate | Add License & CI/CD |
| agentic-planner-cli | 33/60 (55%) | Adequate | Add License & Tests |
| DatGen | 8/60 (13%) | Critical | Overhaul or Archive |
| text-featurizer | 8/60 (13%) | Critical | Overhaul or Archive |
| nlp-preprocessing-tools | 7/60 (12%) | Critical | Archive Candidate |
| notebooks_Jupyter | 7/60 (12%) | Critical | Archive Candidate |

### Critical Public Repository Requirements
**Minimum Viable Public Repo:**
- [ ] LICENSE file (MIT, Apache, or appropriate OSS license)
- [ ] README with installation and usage instructions
- [ ] Clear repository description
- [ ] At least 3 relevant topics for discoverability
- [ ] No security vulnerabilities
- [ ] Basic examples demonstrating usage

**Professional Grade Additions:**
- [ ] CI/CD pipeline with automated testing
- [ ] >70% test coverage
- [ ] API documentation
- [ ] CONTRIBUTING.md guidelines
- [ ] Issue and PR templates
- [ ] Badges (build status, coverage, version)

## Maintenance Tasks

### Immediate Actions (Public Repos - CRITICAL)
1. **Add LICENSE files** to: OpenAI_DeepResearch, agentic-planner-cli, DatGen, text-featurizer, nlp-preprocessing-tools, notebooks_Jupyter
2. **Add repository topics** to all public repos for discoverability
3. **Write basic READMEs** for: DatGen, text-featurizer, nlp-preprocessing-tools

### Immediate Actions (Private Repos)
1. **agentic-planner-cli**: Review and handle `demo.cast` file
2. **GM-RKB**: Review and commit validator session notes

### Recommended Actions
1. **Archive low-value public repos**: Consider archiving DatGen, text-featurizer, nlp-preprocessing-tools if not maintaining
2. **Focus investment** on high-potential repos: llm-judge, OpenAI_DeepResearch, agentic-planner-cli
3. Consider initializing git for Ancalagon_annotation_analysis if needed
4. Consider initializing git for mediawiki-mcp-server if needed
5. Regular spring cleaning using GM-RKB's improved spring_clean.py

## Integration Points

- **GM-RKB** ecosystem: Core system with infrastructure and site components
- **Testing Pipeline**: llm-judge provides testing capabilities for other projects
- **Session Management**: Shared patterns between agent-music and CCB
- **Documentation Standards**: Consistent use of CLAUDE.md across projects

## Next Steps

1. Commit pending changes in flagged repositories
2. Continue active development on session management features
3. Maintain CI/CD pipeline health across all projects
4. Regular documentation updates as features evolve

---

*Last Updated: 2025-09-20*
*Generated for: Claude AI Assistant Context*