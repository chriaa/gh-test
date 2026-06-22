# Quick Start: GitHub Pages Deployment

## TL;DR - Get Started in 5 Minutes

### 1. Initialize Git Repository
```bash
cd /Users/christina/Desktop/gh-pages-ex
git init
git add .
git commit -m "Initial commit: MyLib with Sphinx docs"
```

### 2. Create GitHub Repository
- Go to [github.com/new](https://github.com/new)
- Create a new repository named `gh-pages-ex`
- Do NOT initialize with README (you already have one)
- Copy the push commands and run them

### 3. Enable GitHub Pages
1. Go to repository **Settings** → **Pages**
2. Under "Source", select **"GitHub Actions"**
3. Done! ✅

### 4. View Your Site
After the workflow completes (check **Actions** tab):
- Visit: `https://yourusername.github.io/gh-pages-ex/`

## What Gets Deployed

The workflow automatically:
- ✅ Installs dependencies (Sphinx, MyST parser)
- ✅ Builds Sphinx documentation from `docs/` directory
- ✅ Deploys to GitHub Pages on every push to `main`/`master`

## File Structure

```
.github/workflows/
└── deploy.yml          ← GitHub Actions workflow (automatic deployment)

docs/
├── conf.py             ← Sphinx configuration (includes MyST parser)
├── index.rst           ← Main documentation page (RST format)
├── Makefile            ← Build script
├── api/
│   ├── index.rst
│   ├── core.rst        ← Auto-generated from Python docstrings
│   └── utils.rst       ← Auto-generated from Python docstrings
└── guides/
    ├── getting_started.md    ← Custom markdown guide
    └── tutorial.md           ← Custom markdown guide

mylib/
├── __init__.py
├── core.py             ← Calculator class
└── utils.py            ← Text processing functions
```

## Making Changes

### Update Documentation
1. Edit files in `docs/guides/` (markdown) or `docs/api/` (RST)
2. Edit docstrings in `mylib/` (auto-generates API docs)
3. Push to `main`: `git add . && git commit -m "message" && git push`
4. Workflow deploys automatically! 🚀

### Local Testing (Optional)
Before pushing, test locally:
```bash
# Install dependencies
pip install -r requirements-dev.txt

# Build documentation
cd docs
make clean && make html

# View in browser
open _build/html/index.html
```

## Key Features

✅ **Automatic Builds**: Deploy with every push to `main`  
✅ **API Documentation**: Auto-generated from Python docstrings  
✅ **Markdown Support**: Write guides in Markdown (MyST parser)  
✅ **Pull Request Validation**: Documentation builds are tested on PRs  
✅ **Minimal Configuration**: Works out of the box!

## Workflow Triggers

| Event | Action |
|-------|--------|
| Push to `main`/`master` | Build + Deploy to Pages |
| Pull Request to `main` | Build + Verify (no deploy) |

## FAQ

**Q: Where is my site?**  
A: `https://yourusername.github.io/gh-pages-ex/`

**Q: How do I update the site?**  
A: Just push changes to `main`. The workflow handles everything!

**Q: Can I write documentation in Markdown?**  
A: Yes! MyST parser is enabled. Use `.md` files in `docs/guides/`

**Q: What if the build fails?**  
A: Check **Actions** tab → click workflow → see error logs

**Q: Can I use a custom domain?**  
A: Yes. Go to **Settings** → **Pages** → add CNAME file

## File Locations

- **Workflow file**: `.github/workflows/deploy.yml`
- **Documentation source**: `docs/`
- **Python library**: `mylib/`
- **Config files**: `setup.py`, `requirements-dev.txt`

## Common Tasks

### Add a New Python Module
1. Create `mylib/newmodule.py` with docstrings
2. Update `mylib/__init__.py` to export it
3. Create `docs/api/newmodule.rst` with autodoc
4. Add to `docs/api/index.rst`
5. Push → workflow deploys automatically

### Add a New Markdown Guide
1. Create `docs/guides/mynewguide.md`
2. Add to `docs/index.rst` in the toctree
3. Push → workflow deploys automatically

### Change Documentation Theme
Edit `docs/conf.py`:
```python
html_theme = 'alabaster'  # Change to 'sphinx_rtd_theme', 'press', etc.
```
Then push and redeploy.

## Troubleshooting

**Build fails in GitHub Actions?**
1. Check **Actions** tab for error logs
2. Test locally: `cd docs && make clean && make html`
3. Verify `requirements-dev.txt` has all dependencies

**Site shows old content?**
1. Clear browser cache (Ctrl+Shift+Del or Cmd+Shift+Delete)
2. Hard refresh (Cmd+R on macOS, Ctrl+F5 on Windows)

**404 error?**
1. Check GitHub Pages is enabled (**Settings** → **Pages**)
2. Verify Source is set to "GitHub Actions"
3. Check Actions tab - workflow may still be running

## Resources

- 📖 [Full Setup Guide](SETUP.md)
- 📄 [GitHub Pages Guide](GITHUB_PAGES.md)
- 🔗 [Sphinx Docs](https://www.sphinx-doc.org/)
- 🔗 [MyST Parser](https://myst-parser.readthedocs.io/)
