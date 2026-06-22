# MyLib - A Simple Python Library

A dummy Python library demonstrating Sphinx documentation with Markdown support via MyST Parser.

## 📖 View Full Documentation

**⚠️ Important**: The full documentation is generated from `docs/index.md` and published via GitHub Actions.

Once deployed, visit: `https://chriaa.github.io/gh-test/`

### Verify GitHub Pages Deployment

1. **Check your Actions** → https://github.com/chriaa/gh-test/actions
   - Look for the build workflow and verify the latest run is ✅
   - It should build the Sphinx site and publish HTML from `docs/_build/html`
   
2. **Check GitHub Pages settings** → https://github.com/chriaa/gh-test/settings/pages
   - Set the source to **GitHub Actions**
   - This workflow publishes the site root directly from the generated docs

3. **View your site** → https://chriaa.github.io/gh-test/
   - The site should display the Sphinx documentation with a left sidebar navigation
   - You should see: User Guide, API Reference, and the generated docs from `docs/index.md`

## 🚀 Features

- Clean Python library structure
- Comprehensive Sphinx documentation
- Markdown support via MyST Parser
- Auto-generated API documentation
- GitHub Pages deployment via GitHub Actions
- Best practices guides and architecture documentation

## 📋 Installation

```bash
pip install -e .
```

## 🔨 Build Documentation Locally

```bash
# Install development dependencies
pip install -r requirements-dev.txt

# Build documentation
cd docs
make clean
make html

# View in browser
open _build/html/index.html
```

## 📁 Project Structure

- **mylib/** - Python library with core.py and utils.py
- **docs/** - Sphinx documentation source (RST format)
- **resources/** - Custom markdown documentation  
- **.github/workflows/** - GitHub Actions deployment workflow

## 🔗 Documentation Contents

Once deployed, the documentation site includes:

- **Overview** - Project introduction and features
- **Getting Started** - Quick introduction to MyLib
- **Tutorial** - Build a real application with MyLib  
- **API Reference** - Auto-generated from Python docstrings
- **Architecture** - System design and structure
- **Best Practices** - Development guidelines
- **Contributing** - How to contribute
- **Setup** - Local development setup
- **Deployment** - GitHub Pages deployment guide

## 🛠️ Development

### Add a New Function

1. Add function to `mylib/core.py` or `mylib/utils.py`
2. Include a comprehensive docstring
3. Export from `mylib/__init__.py`
4. Documentation updates automatically!

### Add a New Guide

1. Create `resources/myguide.md`
2. Update `resources/index.md` to link to it
3. Push and the site rebuilds automatically

## 🚢 Deployment

Push to `main` branch:

```bash
git add .
git commit -m "Your message"
git push origin main
```

The GitHub Actions workflow will:
1. Build the Sphinx documentation
2. Deploy to GitHub Pages
3. Site updates automatically! 🎉

**Check deployment status**: https://github.com/yourusername/gh-pages-ex/actions

## ⚠️ If Site Isn't Showing

1. **Check GitHub Pages Settings**
   - Go to repo Settings → Pages
   - Recommended: set Source to **`gh-pages` branch**
   - Alternative: set Source to **"GitHub Actions"** if you want actions-based deployment

2. **Check Actions Tab** 
   - Ensure the latest workflow run is ✅ green
   - If red ❌, click it to see the error

3. **Clear Browser Cache**
   - Hard refresh: Cmd+R (macOS) or Ctrl+F5 (Windows)

4. **Wait a Few Minutes**
   - GitHub Pages can take 1-2 minutes to update

5. **Check Deployment URL**
   - Should be: `https://yourusername.github.io/gh-pages-ex/`
   - Not: `https://yourusername.github.io/`

## 📚 Learn More

- [Complete Setup Guide](SETUP.md)
- [Deployment Guide](GITHUB_PAGES.md)  
- [Documentation Structure](DOCUMENTATION_STRUCTURE.md)
- [Sphinx Documentation](https://www.sphinx-doc.org/)
- [MyST Parser](https://myst-parser.readthedocs.io/)

## 📖 Documentation is Here

Once deployed, the full documentation is at:
**https://chriaa.github.io/gh-test/**

If GitHub Pages is serving the repository root, the repository now includes a root `index.html` redirect to the built docs.

On the live site, click the left sidebar entry:
- **Demo Application**

This will take you into the Sphinx-powered documentation for the dummy app and its extracted docstrings.
