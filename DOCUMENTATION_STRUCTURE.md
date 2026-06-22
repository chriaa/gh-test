# Unified Documentation Structure

## Overview

The documentation is now fully unified in Sphinx with multiple sections organized for clarity.

## Site Structure

When you visit the deployed site (`https://yourusername.github.io/gh-pages-ex/`), you'll see:

```
📚 MyLib Documentation
├── 📄 Overview
│   └── Project introduction and features
├── 📖 Guides
│   ├── Getting Started
│   └── Tutorial
├── 🔧 API Reference
│   ├── Core Module (auto-generated)
│   └── Utils Module (auto-generated)
├── 📚 Resources
│   ├── Architecture
│   ├── Best Practices
│   └── Contributing
├── 📋 Project
│   ├── Setup
│   └── Deployment
└── Search & Index
```

## File Organization

### Documentation Files (`/docs/`)

```
docs/
├── conf.py                 # Sphinx config (copies resources)
├── index.rst               # Main index with toctree
├── overview.rst            # Project overview
├── setup.rst               # Local setup instructions
├── deployment.rst          # GitHub Pages deployment guide
├── Makefile               # Build script
├── api/
│   ├── index.rst
│   ├── core.rst           # Auto-generated from mylib/core.py
│   └── utils.rst          # Auto-generated from mylib/utils.py
├── guides/
│   ├── getting_started.md
│   └── tutorial.md
└── resources/             # Copied from /resources (build artifact)
    ├── index.md
    ├── architecture.md
    ├── best_practices.md
    └── contributing.md
```

### Source Resources (`/resources/`)

```
resources/
├── index.md               # Resources section index
├── architecture.md        # System architecture guide
├── best_practices.md      # Development best practices
└── contributing.md        # Contribution guidelines
```

## How It Works

1. **Build Time**: When `make html` runs, `conf.py` automatically copies `/resources/` into `/docs/resources/`
2. **Sphinx Processing**: Sphinx processes both RST and Markdown files (via MyST parser)
3. **Website Generation**: All sections appear together in one unified site
4. **Deploy**: GitHub Pages hosts the complete generated HTML

## Navigation

### From the Homepage

- **Overview**: Introduction to MyLib
- **Guides**: Quick start and tutorials (Markdown)
- **API Reference**: Auto-generated code documentation (RST)
- **Resources**: Architecture, practices, contributing (Markdown)
- **Project**: Setup and deployment guides (RST)

### Cross-References

All sections link to each other:

```
Overview → API Reference
Getting Started → Tutorial → Best Practices
Setup → Deployment → Contributing
```

## Adding New Content

### Add to Guides (Markdown)

1. Create `docs/guides/myguide.md`
2. Add to `docs/index.rst` toctree

### Add to Resources (Markdown)

1. Create `resources/myguide.md`
2. Add to `resources/index.md` toctree
3. Will be automatically copied and integrated

### Add to API (Auto-generated)

1. Add module to `mylib/`
2. Create `docs/api/mymodule.rst` with autodoc directive
3. Add to `docs/api/index.rst`

### Add Custom Project Info (RST)

1. Create `docs/mypage.rst`
2. Add to `docs/index.rst` toctree

## Building Locally

```bash
cd docs
make clean
make html
open _build/html/index.html
```

The build will:
1. Copy resources to `docs/resources/`
2. Process all RST files
3. Process all Markdown files via MyST parser
4. Generate API documentation from docstrings
5. Create a unified HTML site

## Deployment

The GitHub Actions workflow (`.github/workflows/deploy.yml`):

1. Installs dependencies
2. Runs `make clean && make html` in docs folder
3. Uploads the entire `_build/html` directory
4. Deploys to GitHub Pages

## Benefits of This Structure

✅ **Unified Documentation**: One complete site, not separate pages  
✅ **Multiple Formats**: Mix RST and Markdown in one build  
✅ **Organized**: Clear sections for guides, API, resources  
✅ **Flexible**: Easy to reorganize or add sections  
✅ **Automatic**: API docs generated from code  
✅ **Scalable**: Structure grows cleanly with the project  

## Key Files

| File | Purpose |
|------|---------|
| `docs/index.rst` | Main documentation index with toctree |
| `docs/conf.py` | Sphinx config, copies resources |
| `docs/overview.rst` | Project overview |
| `docs/setup.rst` | Setup instructions |
| `docs/deployment.rst` | Deployment guide |
| `docs/guides/*.md` | User guides (Markdown) |
| `docs/api/*.rst` | API reference (auto-generated) |
| `resources/*.md` | Source resources (copied to docs/) |
| `.github/workflows/deploy.yml` | GitHub Actions deployment |

## Next Steps

1. Build locally: `cd docs && make clean && make html`
2. Review at `docs/_build/html/index.html`
3. Verify all sections appear and links work
4. Push to GitHub: `git add . && git commit -m "..." && git push`
5. GitHub Actions will build and deploy automatically
6. Visit your live site at `https://yourusername.github.io/gh-pages-ex/`

## Migration from Old Structure

If you had separate sections before:

- Old README.md → Now available as Overview section
- Old guides → Still in `/docs/guides/`
- Old resources → Now in `/resources/` → Auto-copied to docs
- API docs → Still auto-generated from code

All content is now accessible through one main navigation structure!
