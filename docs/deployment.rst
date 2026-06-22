Deployment to GitHub Pages
===========================

This page explains how to deploy MyLib documentation to GitHub Pages using GitHub Actions.

Overview
--------

The GitHub Actions workflow automatically:

1. Builds the Sphinx documentation
2. Installs all dependencies
3. Generates API documentation from code
4. Deploys to GitHub Pages on every push to ``main`` or ``master``

Quick Start
-----------

Follow these steps to set up GitHub Pages deployment:

Step 1: Enable GitHub Pages
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

1. Go to your GitHub repository
2. Click **Settings** → **Pages**
3. Under "Build and deployment":

   - **Source**: Select **GitHub Actions**

Step 2: Push to Repository
^^^^^^^^^^^^^^^^^^^^^^^^^^^

The workflow is configured in ``.github/workflows/deploy.yml``:

.. code-block:: bash

    git push origin main

Step 3: Monitor Deployment
^^^^^^^^^^^^^^^^^^^^^^^^^^^

1. Go to the **Actions** tab on GitHub
2. Click the "Deploy Documentation to GitHub Pages" workflow
3. Watch the build progress
4. When complete, visit your site at: ``https://yourusername.github.io/gh-pages-ex/``

Workflow Details
----------------

The ``.github/workflows/deploy.yml`` file defines:

**Trigger Events**

- Push to ``main`` or ``master`` branch
- Pull requests to ``main`` or ``master`` branch (builds but doesn't deploy)

**Build Steps**

1. **Checkout**: Clone your repository
2. **Setup Python**: Uses Python 3.11
3. **Install Dependencies**: Installs Sphinx, MyST parser, mylib package
4. **Build Documentation**: Runs ``make clean && make html`` in docs folder
5. **Upload Artifact**: Uploads built HTML to GitHub Pages storage
6. **Deploy**: Deploys to GitHub Pages (only on ``main``/``master`` pushes)

**Permissions**

The workflow requires:

- ``read``: Read repository contents
- ``pages``: Write to GitHub Pages
- ``id-token``: Authenticate with GitHub

Workflow Configuration
----------------------

To customize the workflow, edit ``.github/workflows/deploy.yml``:

Change Python Version
^^^^^^^^^^^^^^^^^^^^^

.. code-block:: yaml

    - name: Set up Python
      uses: actions/setup-python@v4
      with:
        python-version: '3.11'  # Change this

Change Build Directory
^^^^^^^^^^^^^^^^^^^^^^^

.. code-block:: yaml

    - name: Upload artifact
      uses: actions/upload-pages-artifact@v3
      with:
        path: 'docs/_build/html'  # Change this path

Trigger on Different Branches
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block:: yaml

    on:
      push:
        branches:
          - main
          - develop  # Add other branches
          - staging

Monitoring Deployment
---------------------

Check Build Status
^^^^^^^^^^^^^^^^^^^

1. Go to **Actions** tab
2. Click "Deploy Documentation to GitHub Pages"
3. View recent workflow runs
4. Click a run to see detailed logs

View Your Site
^^^^^^^^^^^^^^

After successful deployment:

- Visit: ``https://yourusername.github.io/gh-pages-ex/``
- Or check **Settings** → **Pages** for the live URL

Troubleshooting
---------------

Build Fails: ModuleNotFoundError
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

**Error**: ``ModuleNotFoundError: No module named 'mylib'``

**Solution**:
Verify ``requirements-dev.txt`` includes all dependencies:

.. code-block:: text

    sphinx>=4.0.0
    myst-parser>=0.18.0
    alabaster>=0.7.12

Build Fails: Sphinx Not Found
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

**Error**: ``sphinx: command not found``

**Solution**:
Ensure ``requirements-dev.txt`` is installed:

.. code-block:: bash

    pip install -r requirements-dev.txt

Workflow Not Triggering
^^^^^^^^^^^^^^^^^^^^^^^

**Problem**: Push to ``main`` but workflow doesn't run

**Solution**:

1. Check branch name is exactly ``main`` or ``master``
2. Verify ``.github/workflows/deploy.yml`` exists
3. Go to **Settings** → **Actions** → **General**
4. Set "Workflow permissions" to **Read and write permissions**

Permission Denied Errors
^^^^^^^^^^^^^^^^^^^^^^^^

**Error**: ``Permission denied`` when deploying

**Solution**:

1. Go to **Settings** → **Actions** → **General**
2. Under "Workflow permissions":

   - ✅ Check **Read and write permissions**
   - ✅ Check **Allow GitHub Actions to create and approve pull requests**

CSS/Images Not Loading
^^^^^^^^^^^^^^^^^^^^^^

**Problem**: Site loads but CSS/images appear broken

**Solution**:

1. Check ``docs/conf.py`` has correct ``html_static_path``
2. Verify Makefile generates files with correct paths
3. Rebuild locally to test: ``cd docs && make clean && make html``

Site Shows Old Content
^^^^^^^^^^^^^^^^^^^^^^

**Problem**: Site shows outdated documentation

**Solution**:

1. Clear browser cache
2. Hard refresh: ``Cmd+R`` (macOS) or ``Ctrl+F5`` (Windows)
3. Check **Actions** tab - workflow may still be running

Advanced Configuration
----------------------

Skip Deployment for Certain Commits
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Modify the workflow to skip on specific commit messages:

.. code-block:: yaml

    - name: Check commit message
      if: "!contains(github.event.head_commit.message, '[skip deploy]')"
      run: echo "Will deploy"

Then skip with: ``git commit -m "Message [skip deploy]"``

Add Custom Build Steps
^^^^^^^^^^^^^^^^^^^^^^^

Add steps before "Build documentation":

.. code-block:: yaml

    - name: Generate API documentation
      run: |
        cd docs
        sphinx-apidoc -o api ../mylib

Add Pre-build Validation
^^^^^^^^^^^^^^^^^^^^^^^^

Check documentation for issues before deploying:

.. code-block:: yaml

    - name: Check for warnings
      run: |
        cd docs
        make clean
        make html 2>&1 | grep -i "warning" && exit 1 || true

Deploy to Multiple Branches
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Create separate workflow files for different branches:

.. code-block:: yaml

    on:
      push:
        branches:
          - main
          - develop

Then use conditional steps to deploy to different URLs.

Continuous Integration
----------------------

The workflow provides continuous integration benefits:

✅ **Auto-build on Push**: Documentation builds on every push  
✅ **Validate PRs**: Documentation is tested for every PR  
✅ **Prevent Broken Deploys**: Won't deploy if build fails  
✅ **Cache Dependencies**: Uses pip cache for faster builds  

Viewing Build Logs
-------------------

To debug issues:

1. Go to **Actions** tab
2. Click the failed workflow run
3. Expand sections to see detailed logs
4. Look for error messages in output

Rollback Deployment
-------------------

If something goes wrong:

**Option 1: Revert Last Commit**

.. code-block:: bash

    git revert HEAD
    git push origin main
    # Workflow will redeploy with previous version

**Option 2: Disable Workflow**

1. Go to **Actions** tab
2. Click "Deploy Documentation to GitHub Pages"
3. Click **...** → "Disable workflow"
4. Re-enable when ready

Deployment Best Practices
--------------------------

1. **Test Locally First**

   .. code-block:: bash

       cd docs
       make clean
       make html
       # Review _build/html/ before pushing

2. **Keep Dependencies Updated**

   Review and update ``requirements-dev.txt`` regularly

3. **Monitor Build Status**

   Check **Actions** tab after each push

4. **Document Changes**

   Update guides when adding features

5. **Use Meaningful Commits**

   Clear commit messages help track changes

Useful GitHub Actions Workflows
--------------------------------

Consider these additional workflows:

**Run Tests on Every Push**

.. code-block:: yaml

    - name: Run tests
      run: pytest tests/

**Check Code Quality**

.. code-block:: yaml

    - name: Lint code
      run: flake8 mylib/

**Update Dependencies**

.. code-block:: yaml

    - name: Create dependency update PR
      uses: dependabot/fetch-metadata@v1

Next Steps
----------

- :doc:`Getting Started <guides/getting_started>` with MyLib
- :doc:`Project Setup <setup>` for local development
- :doc:`Contributing <resources/contributing>` guidelines
- See `GitHub Pages Documentation <https://docs.github.com/en/pages>`_
- See `GitHub Actions Documentation <https://docs.github.com/en/actions>`_
