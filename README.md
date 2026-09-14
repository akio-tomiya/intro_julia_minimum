# A minimal introduction to Julia for science students and researchers

[日本語版はこちら](README_jp.md)

This short Jupyter Notebook tutorial covers Julia's basic syntax, arrays and matrices, plotting, optional Python interoperability, and small numerical examples. Japanese and English editions are available.

- [English notebook](short_intro_julia_en.ipynb)
- [Japanese notebook](short_intro_julia.ipynb)

Tested with Julia 1.13.0 on September 14, 2026.

## Try it in your browser

You can run either notebook on Binder without installing anything. The first launch may take a few minutes.

- [![Open English version in Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/akio-tomiya/intro_julia_minimum/main?urlpath=lab/tree/short_intro_julia_en.ipynb) English version
- [![日本語版をBinderで開く](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/akio-tomiya/intro_julia_minimum/main?urlpath=lab/tree/short_intro_julia.ipynb) Japanese version

## Run it locally

1. Follow the [official Julia installation guide](https://julialang.org/install/) to install `juliaup` and the latest stable version of Julia.
2. Clone this repository and instantiate its package environment.

   ```shell
   git clone https://github.com/akio-tomiya/intro_julia_minimum.git
   cd intro_julia_minimum
   julia --project=. -e 'using Pkg; Pkg.instantiate()'
   ```

3. Start Jupyter Notebook.

   ```shell
   julia --project=. -e 'using IJulia; notebook(dir=pwd())'
   ```

   If Jupyter is not installed, press Enter when IJulia asks whether it should install a private Jupyter environment.

If the Julia kernel is missing after a Julia minor-version update, run `using Pkg; Pkg.build("IJulia")` from the Julia REPL.

## Reproducible environment

`Project.toml` and `Manifest.toml` pin the Julia packages used by the tutorial. `CondaPkg.toml` manages the Python packages used by PythonPlot and PythonCall, and `postBuild` prepares them on Binder. Run `python3 scripts/update_notebooks.py` to regenerate the two aligned notebooks.
