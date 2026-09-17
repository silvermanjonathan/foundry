# Calling Foundry models from Python

A self-paced course module that teaches how to call Microsoft Foundry Models from Python through a single endpoint. It covers deployments, the v1 endpoint URL, API key and keyless (Microsoft Entra ID) authentication, the Responses API with a Chat Completions fallback, and common errors.

**Open the module:** [`index.html`](index.html). If GitHub Pages is enabled for this repo, it is also served at `https://<your-username>.github.io/<repo-name>/`.

## What's in the module

- Eight lessons, each with a "predict, then reveal" question
- An interactive builder that writes the client code for your resource and deployment names
- A four-task lab with solutions
- A troubleshooting table matching SDK errors to likely causes
- A 10-question knowledge check with explanations
- A one-screen cheat sheet

Progress through lessons and lab tasks is saved in the learner's browser.

## Run the lab code

Requires Python 3, an Azure subscription, and a Foundry resource with at least one model deployment.

```bash
python3 -m venv .venv
source .venv/bin/activate          # Windows: .venv\Scripts\Activate.ps1
pip install --upgrade -r requirements.txt
```

Replace `<resource>` and `deepseek-v3-0324` in the files with your own resource and deployment names.

| File | What it shows |
|---|---|
| `lab/first_call.py` | A first call with an API key read from `AZURE_INFERENCE_CREDENTIAL` |
| `lab/keyless_call.py` | The same call with keyless Entra ID authentication (run `az login` first) |
| `lab/foundry_client.py` | `make_client()`, which picks key or keyless auth, and `ask()`, which falls back to Chat Completions |
| `lab/compare.py` | One prompt sent to several deployments with no code changes |

`compare.py` and `foundry_client.py` read the resource name from `FOUNDRY_RESOURCE`, a variable name chosen for this lab rather than an Azure convention.

```bash
export FOUNDRY_RESOURCE="your-resource-name"
export AZURE_INFERENCE_CREDENTIAL="your-key"   # omit to use keyless auth
cd lab && python compare.py
```

Never commit keys. `.env` is already in `.gitignore`.

## Credits and sources

This module is based on [Endpoints for Microsoft Foundry Models](https://learn.microsoft.com/en-us/azure/foundry/foundry-models/concepts/endpoints?tabs=python) on Microsoft Learn (Python tab, page updated August 1, 2026), © Microsoft. Microsoft publishes that documentation under [CC BY 4.0](https://github.com/MicrosoftDocs/azure-ai-docs/blob/main/LICENSE) and its code samples under the [MIT License](https://github.com/MicrosoftDocs/azure-ai-docs/blob/main/LICENSE-CODE). The client code in `lab/first_call.py` and `lab/keyless_call.py` follows the patterns in those samples.

The lesson explanations, prediction questions, interactive builder, lab tasks, troubleshooting guide, knowledge check, and page design were written for this module.

Azure changes quickly. If something here disagrees with the source page, trust the source page.
