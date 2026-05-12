# VendorWatch AI

## Live Streamlit Deployment

This repository is now configured to run as a self-contained Streamlit app using `streamlit_app.py`.

### What is included

- `streamlit_app.py` — root Streamlit entrypoint for deployment
- `requirements.txt` — dependency list for Streamlit Cloud
- `.streamlit/config.toml` — Streamlit runtime settings
- `.github/workflows/ci.yml` — CI pipeline for automatic validation on GitHub push/PR

### Deployment path

1. Push your repository to GitHub.
2. Open https://share.streamlit.io and connect your GitHub account.
3. Create a new app from this repository.
4. Set the app file to `streamlit_app.py`.
5. Choose the `main` branch.

Streamlit Community Cloud will install dependencies from `requirements.txt` and deploy the live app automatically.

### GitHub CI

The CI workflow performs:

- checkout
- Python setup
- dependency installation
- syntax validation for critical app modules
- import smoke tests for Streamlit dependencies

### Local run

```powershell
python pipeline/run_pipeline.py
streamlit run streamlit_app.py
```
