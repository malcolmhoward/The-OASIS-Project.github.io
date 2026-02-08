# The O.A.S.I.S. Project Documentation Portal

<img src="https://www.oasisproject.net/assets/logo.png" alt="O.A.S.I.S. Logo" width="350" align="right">

## Overview

The O.A.S.I.S. Project documentation portal is the public-facing website for the O.A.S.I.S. wearable computing platform. Built with MkDocs and the Material theme, it aggregates documentation from all component repositories into a unified, searchable site hosted at [oasisproject.net](https://www.oasisproject.net/).

The portal serves as the primary entry point for users, contributors, and anyone interested in the O.A.S.I.S. ecosystem. It provides component documentation, architecture guides, video content, and a blog.

## Software Dependencies

| Component | Technology | Purpose |
|-----------|------------|---------|
| [MkDocs](https://www.mkdocs.org/) | Static site generator | Builds Markdown into HTML |
| [Material for MkDocs](https://squidfunk.github.io/mkdocs-material/) | Theme | Navigation, search, responsive design |
| [mkdocs-video](https://github.com/soulless-viewer/mkdocs-video) | Plugin | Embedded video support |
| [mkdocs-glightbox](https://github.com/blueswen/mkdocs-glightbox) | Plugin | Image lightbox overlays |
| Python 3.7+ | Runtime | Required by MkDocs |

## Installation

### Prerequisites

- Python 3.7+
- pip

### Setup

```bash
# Clone the repository
git clone https://github.com/The-OASIS-Project/The-OASIS-Project.github.io.git
cd The-OASIS-Project.github.io

# Install dependencies
pip install mkdocs-material mkdocs-video mkdocs-glightbox
```

## Configuration

Site configuration is managed through `mkdocs.yml`:

| Setting | Location | Purpose |
|---------|----------|---------|
| `site_name` | `mkdocs.yml` | Site title |
| `nav` | `mkdocs.yml` | Navigation structure and page ordering |
| `theme.palette` | `mkdocs.yml` | Color scheme (ironman theme) |
| `plugins` | `mkdocs.yml` | Enabled plugins (search, social, blog, video, glightbox) |
| `CNAME` | Root | Custom domain (oasisproject.net) |
| `extra.css` | `docs/stylesheets/extra.css` | Custom CSS overrides |

### Adding a New Page

1. Create a `.md` file in `docs/`
2. Add an entry to the `nav:` section in `mkdocs.yml`
3. Preview locally with `mkdocs serve`

## Usage

### Local Development

```bash
# Serve with live reload (http://localhost:8000)
mkdocs serve

# Build static site to site/ directory
mkdocs build
```

### Deployment

The site deploys automatically via GitHub Actions when changes are pushed to `main`:

1. GitHub Actions checks out the code
2. Builds the site with `mkdocs build`
3. Deploys to the `gh-pages` branch
4. GitHub Pages serves from that branch at oasisproject.net

### Content Structure

```
docs/
├── index.md                    # Home page
├── overview.md                 # Project overview
├── videos.md                   # Video content
├── components/                 # Component documentation
│   ├── mirage.md               # MIRAGE HUD
│   ├── dawn.md                 # DAWN AI assistant
│   ├── dawn-llm.md             # DAWN local LLM setup
│   ├── aura.md                 # AURA helmet firmware
│   ├── spark.md                # SPARK gauntlet firmware
│   └── beacon.md               # BEACON parts catalog
├── architecture/               # Architecture documentation
│   └── mqtt-protocols.md       # MQTT communication protocols
├── assets/                     # Images, logos, media
├── stylesheets/                # Custom CSS
├── blog/                       # Blog posts
├── opensource.md                # Open source acknowledgments
└── credits.md                  # Project credits
```

### Documentation Aggregation

When checked out as part of S.C.O.P.E. (the meta-repo), this site can aggregate documentation from all component repositories. Each component maintains its own `docs/guide.md` as the source of truth, and the aggregation pipeline compiles them into the portal.

| Source | Destination |
|--------|-------------|
| `repos/<component>/docs/guide.md` | `docs/components/<component>.md` |
| `repos/<component>/docs/<topic>.md` | `docs/components/<component>-<topic>.md` |
| `coordination/protocols/*.md` | `docs/architecture/*.md` |

The portal can also be built standalone using only its own content in `docs/`. The aggregation step is optional and only runs when the site is built within the S.C.O.P.E. context.

See [ADR-0004: Documentation Infrastructure](https://github.com/malcolmhoward/the-oasis-project-meta-repo/blob/main/coordination/decisions/adr/0004-documentation-infrastructure.md) for the full aggregation architecture.

### Writing Style

- Write for makers and developers
- Use clear, concise language
- Include code examples where helpful
- Add images/diagrams for complex concepts
- Use MkDocs Material admonitions (`!!! note`, `!!! warning`) for callouts

## Troubleshooting

| Issue | Possible Cause | Solution |
|-------|---------------|----------|
| `mkdocs serve` fails | Missing dependencies | Run `pip install mkdocs-material mkdocs-video mkdocs-glightbox` |
| Page not appearing in nav | Not added to `mkdocs.yml` | Add entry to `nav:` section in `mkdocs.yml` |
| Images not loading | Wrong path | Use relative paths from `docs/` (e.g., `assets/image.png`) |
| Custom CSS not applied | Cache or wrong path | Clear browser cache; verify path in `extra_css` section |
| Deployment fails | GitHub Actions workflow error | Check `.github/workflows/` for configuration; verify branch permissions |
| Blog posts not showing | Missing metadata | Ensure blog posts have required front matter (date, title) |
| Video embeds broken | Missing plugin | Verify `mkdocs-video` is installed and listed in `plugins:` |

## Related Components

- [M.I.R.A.G.E.](https://www.oasisproject.net/components/mirage/) - HUD system documentation aggregated from component repo
- [D.A.W.N.](https://www.oasisproject.net/components/dawn/) - AI assistant documentation aggregated from component repo
- [A.U.R.A.](https://www.oasisproject.net/components/aura/) - Helmet firmware documentation aggregated from component repo
- [S.P.A.R.K.](https://www.oasisproject.net/components/spark/) - Gauntlet firmware documentation aggregated from component repo
- [B.E.A.C.O.N.](https://www.oasisproject.net/components/beacon/) - Parts catalog aggregated from component repo
- S.C.O.P.E. - Meta-repo that coordinates this portal as a submodule alongside all component repos
