# GitHub Pages Deployment Guide

This guide explains how to set up and use the GitHub Actions workflow to automatically deploy your Sphinx documentation to GitHub Pages.

## Prerequisites

- Your project hosted on GitHub
- GitHub repository with Pages enabled
- Main or master branch configured as the default branch

## Workflow Configuration

The `.github/workflows/deploy.yml` file automatically:

1. **Triggers** on every push to `main` or `master` branch
2. **Builds** the Sphinx documentation
3. **Deploys** the built HTML to GitHub Pages

### Workflow Steps

1. **Checkout**: Clones your repository
2. **Setup Python**: Uses Python 3.11
3. **Install Dependencies**: Installs Sphinx, MyST parser, and the mylib package
4. **Build Documentation**: Runs `make html` to generate the HTML documentation
5. **Upload Artifact**: Uploads the built HTML to GitHub's Pages artifact storage
6. **Deploy**: Automatically deploys to GitHub Pages (only on `main`/`master` pushes)

## Setting Up GitHub Pages

### Step 1: Enable GitHub Pages

1. Go to your GitHub repository
2. Click **Settings** → **Pages**
3. Under "Build and deployment":
   - **Source**: Select "GitHub Actions"
   - This allows the workflow to deploy directly

### Step 2: Verify Workflow Permissions

1. Go to **Settings** → **Actions** → **General**
2. Under "Workflow permissions", ensure:
   - ✓ Read and write permissions
   - ✓ Allow GitHub Actions to create and approve pull requests

### Step 3: Push to Trigger Build

Once you've configured GitHub Pages to use GitHub Actions:

```bash
git add .github/workflows/deploy.yml
git commit -m "Add GitHub Pages deployment workflow"
git push origin main
```

The workflow will automatically:
1. Build your documentation
2. Deploy to GitHub Pages
3. Your site will be available at `https://yourusername.github.io/repository-name/`

## Monitoring Deployment

### Check Workflow Status

1. Go to your repository on GitHub
2. Click the **Actions** tab
3. You'll see the "Deploy Documentation to GitHub Pages" workflow
4. Click on a workflow run to see detailed logs

### View Your Documentation

Once deployed successfully:
- Visit `https://yourusername.github.io/gh-pages-ex/` (replace `yourusername` with your GitHub username)
- Or go to **Settings** → **Pages** and click the live URL

## Troubleshooting

### Workflow Fails with "No Sphinx Build Output"

**Issue**: The `_build/html` directory is empty or missing.

**Solution**:
1. Check that `requirements-dev.txt` includes all needed packages
2. Verify `docs/conf.py` is correct
3. Run locally first: `cd docs && make clean && make html`

### "Permission Denied" Errors

**Issue**: Workflow can't write to Pages.

**Solution**:
1. Go to **Settings** → **Actions** → **General**
2. Set "Workflow permissions" to "Read and write permissions"

### Static Files Not Loading

**Issue**: CSS/images appear broken in GitHub Pages.

**Solution**:
1. Check that `html_static_path` in `docs/conf.py` is correct
2. Verify the Makefile generates files with correct paths

### Workflow Not Triggering

**Issue**: Push to `main` but workflow doesn't run.

**Solution**:
1. Check branch name: Must be exactly `main` or `master`
2. Verify `.github/workflows/deploy.yml` exists and is valid YAML
3. Go to **Actions** tab and check for syntax errors

## Workflow Customization

### Change Python Version

In `.github/workflows/deploy.yml`, modify:

```yaml
- name: Set up Python
  uses: actions/setup-python@v4
  with:
    python-version: '3.11'  # Change this to '3.9', '3.10', '3.12', etc.
```

### Trigger on Different Branches

Modify the `on` section:

```yaml
on:
  push:
    branches:
      - main
      - develop  # Add other branches
```

### Add Build Checks (Pull Requests)

The workflow already validates PRs but doesn't deploy:

```yaml
on:
  push:
    branches:
      - main
  pull_request:
    branches:
      - main
```

This means:
- PRs: Build and verify documentation, but don't deploy
- Push to main: Build and deploy to GitHub Pages

### Skip Deployment for Certain Commits

To skip deployment, add `[skip deploy]` or `[no deploy]` to your commit message:

```bash
git commit -m "Minor fix [skip deploy]"
git push origin main
```

(Note: This requires modifying the workflow file)

## Customizing the Deployment

### Change the Build Directory

If Sphinx builds to a different directory, update the artifact path:

```yaml
- name: Upload artifact
  uses: actions/upload-pages-artifact@v3
  with:
    path: 'docs/_build/html'  # Change this path
```

### Add Additional Build Steps

Before the "Build documentation" step, add:

```yaml
- name: Custom step
  run: |
    # Add your custom commands here
    echo "Building custom assets"
```

## Continuous Integration

The workflow also:

1. **Validates Pull Requests**: Builds documentation for every PR
2. **Prevents Broken Deployments**: Won't deploy if build fails
3. **Caches Dependencies**: Uses `cache: 'pip'` for faster builds

## GitHub Pages Site Settings

After first successful deployment, you can customize your site:

1. Go to **Settings** → **Pages**
2. Choose a theme or customize further
3. Add a CNAME file for custom domains (if needed)

## Viewing Build Logs

To debug any issues:

1. Go to **Actions** tab
2. Click the failed workflow run
3. Expand job sections to see detailed logs
4. Look for error messages in the "Build documentation" step

## Next Steps

1. Enable GitHub Pages (set Source to "GitHub Actions")
2. Push to `main` branch
3. Monitor **Actions** tab for workflow completion
4. Visit your deployed site at the GitHub Pages URL

## Useful Links

- [GitHub Pages Documentation](https://docs.github.com/en/pages)
- [GitHub Actions Documentation](https://docs.github.com/en/actions)
- [Sphinx Documentation](https://www.sphinx-doc.org/)
- [MyST Parser Documentation](https://myst-parser.readthedocs.io/)

## Rollback

If something goes wrong after deployment:

1. You can revert the last commit: `git revert HEAD`
2. Push the revert: `git push origin main`
3. The workflow will redeploy with the previous version

Or disable the workflow temporarily:

1. Go to **Actions** tab
2. Click "Deploy Documentation to GitHub Pages"
3. Click **...** → "Disable workflow"
4. Re-enable when ready
