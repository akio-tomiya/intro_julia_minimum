# 理系向けの最小 Julia 入門

Julia の基本文法から、配列・行列、作図、Python 連携、簡単な数値計算までを短く学ぶ Jupyter Notebook です。日本語版と英語版があります。

- [日本語版ノートブック](short_intro_julia.ipynb)
- [English notebook](short_intro_julia_en.ipynb)

2026年9月14日に Julia 1.13.0 で動作確認しています。

## ブラウザですぐ試す

インストールせずに Binder で実行できます。初回の起動には数分かかることがあります。

- [![Binderで日本語版を開く](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/akio-tomiya/intro_julia_minimum/main?urlpath=lab/tree/short_intro_julia.ipynb) 日本語版
- [![Open English version in Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/akio-tomiya/intro_julia_minimum/main?urlpath=lab/tree/short_intro_julia_en.ipynb) English version

## 手元で実行する

1. [Julia の公式インストール案内](https://julialang.org/install/)に従い、`juliaup` と最新安定版の Julia をインストールします。
2. このリポジトリを取得し、プロジェクトの依存パッケージを準備します。

   ```shell
   git clone https://github.com/akio-tomiya/intro_julia_minimum.git
   cd intro_julia_minimum
   julia --project=. -e 'using Pkg; Pkg.instantiate()'
   ```

3. Jupyter Notebook を起動します。

   ```shell
   julia --project=. -e 'using IJulia; notebook(dir=pwd())'
   ```

   Jupyter が未導入の場合は、初回起動時の質問に Enter で答えると、IJulia 専用の環境へ自動的にインストールできます。

Julia のマイナーバージョンを更新した後にカーネルが見つからない場合は、Julia の REPL で `using Pkg; Pkg.build("IJulia")` を実行してください。

## 再現用の環境

`Project.toml` と `Manifest.toml` が教材で使う Julia パッケージを固定します。PythonPlot と PythonCall が使う Python パッケージは `CondaPkg.toml` で管理し、Binder では `postBuild` が事前に準備します。ノートブックを再生成する場合は `python3 scripts/update_notebooks.py` を実行してください。

---

This repository contains a short, bilingual introduction to Julia for science students and researchers. It was tested with Julia 1.13.0 on September 14, 2026. Follow the steps above, or open the English notebook directly with Binder.
