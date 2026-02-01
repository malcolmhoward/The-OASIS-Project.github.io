# Contributing to O.A.S.I.S. Documentation

Thank you for your interest in improving The O.A.S.I.S. Project documentation!

This guide explains how to contribute to the public documentation website.

---

## Before You Start

### Understanding Our Workflow

We use a **fork-first workflow**. This means:
- You work on your own copy (fork) of the repository
- Changes are proposed via Pull Requests from your fork
- This keeps the main repository clean and organized

---

## Fork-First Workflow

### Step 1: Fork the Repository

1. Click the "Fork" button on the repository page
2. This creates your personal copy

### Step 2: Clone Your Fork

```bash
git clone https://github.com/YOUR-USERNAME/The-OASIS-Project.github.io.git
cd The-OASIS-Project.github.io

git remote add upstream https://github.com/The-OASIS-Project/The-OASIS-Project.github.io.git
```

### Step 3: Set Up Local Development

```bash
# Install MkDocs and dependencies
pip install mkdocs-material mkdocs-video mkdocs-glightbox

# Serve locally with live reload
mkdocs serve
```

Visit `http://127.0.0.1:8000` to preview your changes.

### Step 4: Create a Feature Branch

```bash
git checkout -b type/description
```

---

## Branch Naming Conventions

| Type | Purpose | Example |
|------|---------|---------|
| `docs/` | Documentation updates | `docs/mirage-installation` |
| `fix/` | Fix errors or typos | `fix/broken-links` |
| `feat/` | New documentation pages | `feat/troubleshooting-guide` |
| `style/` | Formatting/styling changes | `style/code-blocks` |

---

## Content Guidelines

### Writing Style

- **Audience**: Makers, developers, and hobbyists
- **Tone**: Friendly, clear, and helpful
- **Structure**: Use headings, lists, and tables for scannability
- **Examples**: Include code snippets and commands where helpful

### Markdown Tips

MkDocs Material supports extended Markdown:

```markdown
# Headings

!!! note "Admonition Title"
    Helpful information here.

!!! warning
    Important warning.

`inline code` for commands

| Column 1 | Column 2 |
|----------|----------|
| Data     | Data     |
```

### Images

- Place images in `docs/assets/`
- Use descriptive filenames: `mirage-wiring-diagram.png`
- Optimize for web (compress large images)
- Reference with relative paths: `![Alt text](assets/image.png)`

---

## Types of Contributions

### Fix Typos or Errors

1. Find the relevant `.md` file in `docs/`
2. Make your correction
3. Submit a PR with a brief description

### Improve Existing Content

1. Identify what needs improvement
2. Make changes while preserving existing structure
3. Preview locally to verify formatting
4. Submit a PR explaining the improvement

### Add New Content

1. Discuss in an issue first for major additions
2. Create new `.md` file in appropriate location
3. Add navigation entry in `mkdocs.yml`
4. Submit a PR with description of new content

---

## Pull Request Process

### Before Submitting

- [ ] Preview locally with `mkdocs serve`
- [ ] Check for broken links
- [ ] Verify images display correctly
- [ ] Spell-check your content
- [ ] Commit messages follow conventions

### PR Description Template

```markdown
## Summary
Brief description of documentation changes.

## Type of Change
- [ ] Typo/error fix
- [ ] Content improvement
- [ ] New documentation
- [ ] Style/formatting

## Pages Changed
List of modified files

## Preview
If helpful, include screenshots of changes
```

---

## Style Guide

### Headings

- Use Title Case for main headings
- Use sentence case for subheadings
- Don't skip heading levels (h1 → h3)

### Code Blocks

Always specify the language for syntax highlighting:

````markdown
```bash
# Commands use bash
mkdocs serve
```

```python
# Python code
print("Hello")
```
````

### Links

- Use descriptive link text: `[MIRAGE documentation](mirage.md)`
- Not: `Click [here](mirage.md)`

---

## Code of Conduct

We are committed to providing a welcoming and inclusive environment.
Please be respectful and constructive in all interactions.

---

## Getting Help

- **Questions**: Open a GitHub Discussion or Issue
- **Technical Issues**: Check component repositories for code-related questions
- **O.A.S.I.S. Ecosystem**: See [S.C.O.P.E.](https://github.com/malcolmhoward/the-oasis-project-meta-repo) for cross-project coordination
