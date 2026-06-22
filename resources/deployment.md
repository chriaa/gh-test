# Deployment

This document explains how the documentation is deployed to GitHub Pages.

## GitHub Actions deployment

The repository is configured to build the Sphinx site from `docs/index.md` and publish the generated HTML from `docs/_build/html`.

### Deployment flow

1. Push code to the `main` branch.
2. GitHub Actions installs Python and dependencies.
3. Sphinx builds the documentation from the `docs/` source folder.
4. The generated HTML is published to GitHub Pages.

### Site behavior

- The site landing page is generated from `docs/index.md`.
- The `User Guide` section in the sidebar includes resources from `/resources`.
- The `API Reference` section is generated from package docstrings.
