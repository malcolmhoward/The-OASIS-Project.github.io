# The-OASIS-Project.github.io

**Public documentation website** for the O.A.S.I.S. (Open-source Assistive System for Integrated Services) wearable computing platform.

**Live site**: [oasisproject.net](https://www.oasisproject.net/)

## Overview

This repository contains the source files for The O.A.S.I.S. Project's public documentation, built with MkDocs and the Material theme.

## Quick Start

### Prerequisites

- Python 3.8+
- pip

### Local Development

```bash
# Install dependencies
pip install mkdocs-material mkdocs-video mkdocs-glightbox

# Serve locally
mkdocs serve

# Build static site
mkdocs build
```

Visit `http://127.0.0.1:8000` to preview the site.

## Project Structure

```
github-pages/
├── docs/                    # Documentation source files
│   ├── index.md             # Home page
│   ├── overview.md          # Project overview
│   ├── mirage.md            # MIRAGE HUD documentation
│   ├── dawn.md              # DAWN AI documentation
│   ├── aura.md              # AURA sensors documentation
│   ├── spark.md             # SPARK gauntlet documentation
│   ├── beacon.md            # BEACON parts catalog
│   ├── comms.md             # Communications architecture
│   ├── llm.md               # Local LLM setup
│   ├── assets/              # Images and media
│   └── stylesheets/         # Custom CSS
├── mkdocs.yml               # MkDocs configuration
├── CNAME                    # Custom domain config
├── CLAUDE.md                # LLM integration guide
├── CONTRIBUTING.md          # Contribution guidelines
└── LICENSE                  # GPLv3
```

## Documentation Sections

| Section | Content |
|---------|---------|
| Home | Project introduction and getting started |
| Overview | High-level architecture and components |
| M.I.R.A.G.E. | HUD display system documentation |
| D.A.W.N. | AI voice assistant documentation |
| A.U.R.A. | Helmet sensor documentation |
| S.P.A.R.K. | Hand/gauntlet documentation |
| Communications | MQTT and inter-component messaging |
| Local LLMs | Running AI models on Jetson |
| B.E.A.C.O.N. | 3D printable parts catalog |

## Related Repositories

| Repository | Purpose |
|------------|---------|
| [MIRAGE](https://github.com/The-OASIS-Project/mirage) | HUD source code |
| [DAWN](https://github.com/The-OASIS-Project/dawn) | AI assistant source |
| [AURA](https://github.com/The-OASIS-Project/aura) | Helmet firmware |
| [SPARK](https://github.com/The-OASIS-Project/spark) | Gauntlet firmware |
| [BEACON](https://github.com/The-OASIS-Project/beacon) | CAD models |
| [GENESIS](https://github.com/The-OASIS-Project/genesis) | Python utilities |

## Contributing

See [CONTRIBUTING.md](CONTRIBUTING.md) for guidelines on contributing to the documentation.

## License

This program is free software: you can redistribute it and/or modify it under the terms of the GNU General Public License as published by the Free Software Foundation, either version 3 of the License, or any later version.

See [LICENSE](LICENSE) for full details.
