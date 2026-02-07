# CLAUDE.md - LLM Integration Guide

## Project Overview

**The-OASIS-Project.github.io** is the public documentation website for the O.A.S.I.S. wearable computing platform. Built with MkDocs and the Material theme, it aggregates documentation from all component repositories via S.C.O.P.E. (the meta-repo) and publishes the unified site to [oasisproject.net](https://www.oasisproject.net/). Component repos own their documentation; this repo aggregates and publishes it.

---

## Repository Structure

```
github-pages/
├── docs/                    # Documentation source (Markdown)
│   ├── index.md             # Home page
│   ├── overview.md          # Project overview
│   ├── videos.md            # Video content
│   ├── components/          # Aggregated component documentation
│   │   ├── mirage.md        # MIRAGE HUD (from repos/mirage/docs/guide.md)
│   │   ├── dawn.md          # DAWN AI (from repos/dawn/docs/guide.md)
│   │   ├── dawn-llm.md      # DAWN LLM setup (from repos/dawn/docs/local-llm.md)
│   │   ├── aura.md          # AURA helmet (from repos/aura/docs/guide.md)
│   │   ├── spark.md         # SPARK gauntlet (from repos/spark/docs/guide.md)
│   │   ├── beacon.md        # BEACON parts (from repos/beacon/docs/parts-catalog.md)
│   │   └── genesis.md       # GENESIS utilities (from repos/genesis/docs/guide.md)
│   ├── architecture/        # Aggregated coordination documentation
│   │   └── mqtt-protocols.md  # (from coordination/protocols/mqtt-communication.md)
│   ├── assets/              # Images, logos, media
│   ├── stylesheets/         # Custom CSS (extra.css)
│   └── blog/                # Blog posts
├── scripts/
│   ├── aggregate_docs.py    # Documentation aggregation script
│   └── test_aggregate_docs.py  # Aggregation tests (25 pytest tests)
├── mkdocs.yml               # Site configuration and navigation
├── CNAME                    # Custom domain (oasisproject.net)
└── .github/workflows/       # GitHub Actions for deployment
```

---

## Technology Stack

| Component | Technology |
|-----------|------------|
| Static Site Generator | MkDocs |
| Theme | Material for MkDocs |
| Hosting | GitHub Pages |
| Domain | oasisproject.net |
| Plugins | search, social, blog, mkdocs-video, glightbox |

---

## Working with This Repository

### Local Development

```bash
# Install dependencies
pip install mkdocs-material mkdocs-video mkdocs-glightbox

# Serve with live reload
mkdocs serve

# Build static site
mkdocs build
```

### Adding Content

1. Create or edit `.md` files in `docs/`
2. Update `nav:` section in `mkdocs.yml` if adding new pages
3. Preview locally with `mkdocs serve`
4. Commit and push - GitHub Actions handles deployment

### Key Files

| File | Purpose |
|------|---------|
| `mkdocs.yml` | Site configuration, navigation, theme settings |
| `docs/index.md` | Home page content |
| `docs/stylesheets/extra.css` | Custom CSS overrides |
| `CNAME` | Custom domain configuration |

---

## Content Guidelines

### Writing Style

- Write for makers and developers
- Use clear, concise language
- Include code examples where helpful
- Add images/diagrams for complex concepts

### Markdown Features

MkDocs Material supports extended Markdown:

```markdown
!!! note "Title"
    Admonition content

`inline code` and code blocks with syntax highlighting

| Tables | Are | Supported |
```

### Images

- Place in `docs/assets/`
- Use relative paths: `![Alt text](assets/image.png)`
- Optimize for web (compress large images)

---

## Navigation Structure

The site navigation is defined in `mkdocs.yml`:

```yaml
nav:
  - Home: index.md
  - Overview: overview.md
  - M.I.R.A.G.E.: mirage.md
  - D.A.W.N.: dawn.md
  # ... etc
```

To add a new page:
1. Create the `.md` file in `docs/`
2. Add entry to `nav:` in `mkdocs.yml`

---

## Deployment

The site deploys automatically via GitHub Actions when changes are pushed to `main`. The workflow:

1. Checks out code
2. Builds site with `mkdocs build`
3. Deploys to `gh-pages` branch
4. GitHub Pages serves from that branch

---

## Documentation Aggregation

### Content Decomposition (ADR-0004)

Documentation lives in the repository closest to the code it describes. This repo aggregates that content into a unified site. Component repos own their docs; this repo owns the build and presentation.

| Content Type | Source of Truth | Aggregated To |
|--------------|-----------------|---------------|
| Component docs | `repos/<component>/docs/guide.md` | `docs/components/<component>.md` |
| Coordination docs | `coordination/protocols/*.md` | `docs/architecture/*.md` |
| Site-specific | This repo (`docs/`) | `docs/` (root) |

### Running Aggregation

The aggregation script pulls documentation from sibling submodules when this repo is checked out as part of S.C.O.P.E.:

```bash
# From this repo's root (within S.C.O.P.E.)
python scripts/aggregate_docs.py

# Preview what would be copied without modifying files
python scripts/aggregate_docs.py --dry-run

# Specify S.C.O.P.E. root explicitly
python scripts/aggregate_docs.py --scope-root /path/to/meta-repo
```

The script auto-detects the S.C.O.P.E. root by walking up the directory tree. It pulls from whatever branch each submodule is currently checked out to.

### When to Re-Run Aggregation

Re-run `aggregate_docs.py` and commit the results when:
- Component `docs/guide.md` files have been updated
- Coordination documentation has changed
- New components are added to `COMPONENT_DOCS` mapping in the script

### Adding a New Component

1. Add the mapping to `COMPONENT_DOCS` in `scripts/aggregate_docs.py`
2. Add a nav entry to `mkdocs.yml`
3. Run `python scripts/aggregate_docs.py`
4. Commit the aggregated file and config changes

### CI Note

The CI workflow (`ci.yml`) currently deploys from committed content only. It does not run aggregation automatically. Automated CI aggregation is deferred until the project reaches steady-state maintenance (see ADR-0004).

## Integration Points

### O.A.S.I.S. Ecosystem

This site documents all O.A.S.I.S. components:
- Component repos own their documentation in `docs/guide.md`
- The aggregation script pulls component docs into this site
- Site-specific content (videos, credits, blog) lives directly in this repo

### S.C.O.P.E. Coordination

- **Meta-repo**: [malcolmhoward/the-oasis-project-meta-repo](https://github.com/malcolmhoward/the-oasis-project-meta-repo)
- This repo is a S.C.O.P.E. submodule at `repos/github-pages`
- Documentation changes coordinate with component updates via the aggregation script

---

## License

This repository is licensed under **GPLv3**. See LICENSE for details.

## Branch Naming Convention

**Critical**: Branch names must include the GitHub issue number being addressed.

### Format
```
feat/<component>/<issue#>-<short-description>
```

### Before Creating a Branch

1. **Identify the issue** you're working on (check GitHub Issues)
2. **Use that issue's number** in the branch name
3. **Verify** the issue number matches the work being done

### Examples
```bash
# Check available issues first
gh issue list --repo malcolmhoward/github-pages

# Create branch with correct issue number
git checkout -b feat/github-pages/<issue#>-description
```

### Common Mistake
❌ Using arbitrary numbers or the wrong issue number
✅ Always check `gh issue list` or GitHub Issues before creating a branch
