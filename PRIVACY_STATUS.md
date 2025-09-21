# Repository Privacy Status Guide

*Last Verified: 2025-09-20*

## Quick Reference

### 🔒 PRIVATE Repositories (5)
| Repository | GitHub Name | Content Type | Sensitivity |
|------------|-------------|--------------|-------------|
| agent-music | spotify-analysis | Personal Spotify data | HIGH - Personal |
| CCB | private-personal-musings | Cognitive patterns, thoughts | HIGH - Personal |
| GM-RKB | GM-RKB | Knowledge base tools | MEDIUM - Proprietary |
| AWS-Amplify | AWS-Amplify | AWS project | MEDIUM - Infrastructure |
| openai-codex-demo | openai-codex-demo | OpenAI demo | LOW - Demo |

### 📁 LOCAL-ONLY Repositories (4)
| Repository | Status | Content Type | Sensitivity |
|------------|--------|--------------|-------------|
| GM-RKB-infrastructure | No remote | AWS configs, scripts | HIGH - Infrastructure |
| GM-RKB-site | No remote | Site development | LOW - Frontend |
| Ancalagon_annotation_analysis | Not git repo | Analysis project | UNKNOWN |
| mediawiki-mcp-server | Not git repo | MCP server | UNKNOWN |

### 🌐 PUBLIC Repositories (7)
| Repository | Purpose | License | Quality Score |
|------------|---------|---------|---------------|
| llm-judge | LLM evaluation library | MIT License ✅ | 43/60 (72%) Good |
| agentic-planner-cli | Educational AI demo | NO LICENSE ❌ | 33/60 (55%) Adequate |
| OpenAI_DeepResearch | Research implementation | NO LICENSE ❌ | 35/60 (58%) Adequate |
| DatGen | Synthetic data generator | NO LICENSE ❌ | 8/60 (13%) Critical |
| text-featurizer | Wiki text processing | NO LICENSE ❌ | 8/60 (13%) Critical |
| nlp-preprocessing-tools | NLP utilities | NO LICENSE ❌ | 7/60 (12%) Critical |
| notebooks_Jupyter | Public notebooks | NO LICENSE ❌ | 7/60 (12%) Critical |

**⚠️ LICENSE WARNING**: 6 of 7 public repositories lack proper licenses, making them legally problematic for others to use.

## Critical Distinctions

### Repository vs Service
- **GM-RKB**: PRIVATE repository → PUBLIC wiki service (gmelli.com)
  - Repository contains proprietary tools and configurations
  - Service delivers public knowledge to 325K bots/month
  - This separation protects intellectual property

### Data Sensitivity Levels
1. **HIGH - Personal**: Contains personal data (Spotify, thoughts)
   - Never make public
   - Guard API keys and personal patterns

2. **HIGH - Infrastructure**: Contains security-sensitive configs
   - AWS credentials, server configs
   - Keep local-only or private

3. **MEDIUM - Proprietary**: Contains intellectual property
   - Unique implementations, algorithms
   - Business logic and custom tools

4. **LOW - Educational**: Designed for public learning
   - Demos, examples, tutorials
   - Safe for public sharing

## Verification Commands

```bash
# Check all GitHub repository visibility
gh repo list gmelli --limit 50 --json name,visibility,isPrivate

# Check specific repository
gh repo view gmelli/REPO_NAME --json visibility

# Check local git remotes
git remote -v

# Find all local git repos
find ~/github -name ".git" -type d -maxdepth 2
```

## Privacy Rules

1. **Before describing any repository**: Check this document first
2. **When writing documentation**: Add privacy header as first lines
3. **When uncertain**: Assume PRIVATE until verified
4. **Personal data repos**: NEVER suggest making public
5. **Infrastructure repos**: Keep LOCAL-ONLY or PRIVATE

## Red Flags 🚩

Watch for these patterns that indicate PRIVATE status:
- Personal data (Spotify, thoughts, musings)
- AWS/infrastructure configurations
- Proprietary algorithms or tools
- Internal development work
- Uncommitted local changes with sensitive data

## Repository Descriptions Template

```markdown
### [PRIVACY_STATUS] Repository Name - Brief Description
- **Privacy**: [PRIVATE/PUBLIC/LOCAL-ONLY] - explanation
- **Data Sensitivity**: [Personal/Proprietary/Infrastructure/Open]
- **Purpose**: What it does
- **Special Notes**: Any privacy considerations
- **Quality Score** (if public): XX/60 (Grade)
```

## Public Repository Quality Assessment

### Grading Scale
- **54-60 (90-100%)**: Exceptional - Professional grade, production ready
- **42-53 (70-89%)**: Good - Solid project, minor improvements needed
- **30-41 (50-69%)**: Adequate - Functional but needs improvement
- **18-29 (30-49%)**: Poor - Major gaps, not ready for public use
- **0-17 (0-29%)**: Critical - Requires complete overhaul

### Current Status Summary
- **Good (70%+)**: 1 repository (llm-judge)
- **Adequate (50-69%)**: 2 repositories (OpenAI_DeepResearch, agentic-planner-cli)
- **Critical (<30%)**: 4 repositories need overhaul or archiving

### Quality Improvement Tracking
| Metric | Current | Target | Status |
|--------|---------|--------|--------|
| Repos with licenses | 1/7 (14%) | 7/7 (100%) | 🔴 Critical |
| Repos scoring >20 pts | 3/7 (43%) | 7/7 (100%) | 🟡 Needs Work |
| Repos at "Good" level | 1/7 (14%) | 4/7 (57%) | 🟡 In Progress |
| Total GitHub stars | ~0 | 50+ | 🔴 Need Promotion |

### Related Documents
- `PUBLIC_REPO_RUBRIC.md` - Detailed scoring criteria (60 points)
- `PUBLIC_REPO_SCORES.md` - Latest scoring report with recommendations
- `CLAUDE.md` - Main documentation with improvement tasks

---

*Last Updated: 2025-09-20*
*Next Quality Review: Monthly*