# CLAUDE.md - LLM Integration Guide

## Project Overview

**The-OASIS-Project.github.io** is the public documentation website for the O.A.S.I.S. wearable computing platform. It's built with MkDocs and the Material theme, hosted on GitHub Pages at [oasisproject.net](https://www.oasisproject.net/).

---

## Repository Structure

```
github-pages/
├── docs/                    # Documentation source (Markdown)
│   ├── index.md             # Home page
│   ├── overview.md          # Project overview
│   ├── mirage.md            # MIRAGE HUD docs
│   ├── dawn.md              # DAWN AI docs
│   ├── aura.md              # AURA sensor docs
│   ├── spark.md             # SPARK gauntlet docs
│   ├── beacon.md            # Parts catalog
│   ├── comms.md             # Communications architecture
│   ├── llm.md               # Local LLM setup
│   ├── assets/              # Images, logos, media
│   ├── stylesheets/         # Custom CSS (extra.css)
│   └── blog/                # Blog posts
├── mkdocs.yml               # Site configuration
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

## Integration Points

### O.A.S.I.S. Ecosystem

This site documents all O.A.S.I.S. components:
- Component READMEs should link here for user-facing docs
- Technical details stay in component repos
- This site focuses on getting started and tutorials

### S.C.O.P.E. Coordination

- **Meta-repo**: [malcolmhoward/the-oasis-project-meta-repo](https://github.com/malcolmhoward/the-oasis-project-meta-repo)
- Documentation changes may need coordination with component updates

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
