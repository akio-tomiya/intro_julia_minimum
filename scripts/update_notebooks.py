#!/usr/bin/env python3
"""Generate the Japanese and English tutorial notebooks from aligned sources."""

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parent.parent
JA = []
EN = []


def markdown(source):
    return {"cell_type": "markdown", "metadata": {}, "source": source.strip() + "\n"}


def code(source):
    return {
        "cell_type": "code",
        "execution_count": None,
        "metadata": {},
        "outputs": [],
        "source": source.strip() + "\n",
    }


def add(ja, en, source=None, source_en=None):
    JA.append(markdown(ja))
    EN.append(markdown(en))
    if source is not None:
        JA.append(code(source))
        EN.append(code(source if source_en is None else source_en))


add(
    r"""
# 数値計算が専門でない理系向けの最小 Julia 入門

- 富谷昭夫（[GitHub](https://github.com/akio-tomiya)）
- 初版: 2020年12月21日
- 更新: 2026年9月14日
- Julia 1.13.0 / macOS で動作確認
""",
    r"""
# A minimal introduction to Julia for science students and researchers

- Akio Tomiya ([GitHub](https://github.com/akio-tomiya))
- First published: December 21, 2020
- Updated: September 14, 2026
- Tested with Julia 1.13.0 on macOS
""",
)

add(
    r"""
## このノートについて

Julia を初めて使う人が、基本文法から簡単な数値計算までを一通り試すための短い入門です。大学初年級の数学と、プログラムを少し見た経験を想定しています。

すべてを網羅するものではありません。詳しく知りたいときは、[Julia 公式ドキュメント](https://docs.julialang.org/)と各パッケージのドキュメントを参照してください。
""",
    r"""
## About this notebook

This short introduction takes a first-time Julia user from basic syntax to small numerical examples. It assumes first-year university mathematics and a little familiarity with programming.

It is intentionally incomplete. See the [official Julia documentation](https://docs.julialang.org/) and each package's documentation when you need more detail.
""",
)

add(
    r"""
## Julia とは？

Julia は、数値計算の速さと、対話的に書ける高水準言語の使いやすさを両立するために作られたオープンソースのプログラミング言語です。数式に近い記法、動的型付け、多重ディスパッチ、パッケージ環境の管理などが特徴です。

背景については、開発者による [Why We Created Julia](https://julialang.org/blog/2012/02/why-we-created-julia/) を参照してください。
""",
    r"""
## What is Julia?

Julia is an open-source programming language designed to combine fast numerical computation with the convenience of an interactive high-level language. Its features include familiar mathematical notation, dynamic typing, multiple dispatch, and built-in package environments.

For the motivation behind the language, see [Why We Created Julia](https://julialang.org/blog/2012/02/why-we-created-julia/).
""",
)

add(
    r"""
## Pythonとの違い、C++との違い

### Pythonとの違い

Julia は Python と同じように、REPL や Jupyter Notebook で対話的に試せます。変数の型を毎回宣言する必要がなく、短いコードから書き始められる点も似ています。

数値計算を Python で高速に行う場合、Python 自身の `for` ループを避け、教科書に書かれたアルゴリズムを NumPy のベクトル演算へ書き直すことがよくあります。うまく書き換えるには、NumPy の機能とデータ配置を理解する経験が必要です。場合によっては Numba、Cython、C/C++ なども使います。

Julia では、通常の `for` ループも、実行時に具体的な型に合わせてコンパイルされます。そのため、教科書のアルゴリズムをループのまま素直に実装しても、十分に高速なコードになることが多いです。高速化のためだけに、すべてをベクトル演算へ書き換える必要はありません。

### C++との違い

C++ は、型を明示して事前にコンパイルし、メモリや実行方法を細かく制御できる言語です。起動時間、低水準の制御、既存ライブラリの規模などで強みがあります。一方、テンプレート、ビルド設定、メモリ管理など、数値アルゴリズム以外に必要な記述も多くなります。

Julia は型宣言を省略でき、REPL で試しながら書けますが、実行する関数は具体的な型ごとにコンパイルされます。多重ディスパッチを使って、数値の型やデータ構造に応じた処理を自然に分けられます。
""",
    r"""
## How Julia differs from Python and C++

### Compared with Python

Like Python, Julia supports an interactive REPL and Jupyter Notebook. You can start with short code and usually do not need to declare the type of every variable.

For fast numerical work in Python, programmers often avoid Python-level `for` loops and reformulate a textbook algorithm as vectorized NumPy operations. Doing this well can require substantial knowledge of NumPy operations and data layout. Numba, Cython, or C/C++ extensions are also common when vectorization is not a good fit.

Julia compiles ordinary `for` loops for the concrete types used at runtime. A direct loop-based translation of a textbook algorithm can therefore remain efficient, and code does not have to be rewritten as vector operations merely to avoid slow language-level loops.

### Compared with C++

C++ uses explicit static types and ahead-of-time compilation, and gives detailed control over memory and execution. It has advantages in startup time, low-level control, and the size of its established ecosystem. Templates, build configuration, and memory management can also add code around the numerical algorithm itself.

Julia lets you omit most type declarations and develop interactively, while compiling functions for the concrete argument types that reach them. Multiple dispatch provides a natural way to select behavior for different numerical types and data structures.
""",
)

add(
    r"""
## インストールと起動

現在は、公式のインストーラー兼バージョン管理ツール [`juliaup`](https://julialang.org/install/) の利用が推奨されています。インストール後、ターミナルで `julia` を実行すると REPL が開きます。

このリポジトリのディレクトリで、最初に次を実行してください。

```shell
julia --project=. -e 'using Pkg; Pkg.instantiate()'
```

Jupyter Notebook は次のコマンドで起動できます。

```shell
julia --project=. -e 'using IJulia; notebook(dir=pwd())'
```

IJulia の標準カーネルは、ノートブックと同じ場所にある `Project.toml` を自動的に利用します。次のセルで現在の環境と Julia のバージョンを確認します。
""",
    r"""
## Installation and startup

The recommended installer and version manager is now [`juliaup`](https://julialang.org/install/). After installation, run `julia` in a terminal to open the REPL.

In this repository's directory, first run:

```shell
julia --project=. -e 'using Pkg; Pkg.instantiate()'
```

Start Jupyter Notebook with:

```shell
julia --project=. -e 'using IJulia; notebook(dir=pwd())'
```

The default IJulia kernel automatically uses a `Project.toml` beside the notebook. The next cell shows the active environment and Julia version.
""",
    r"""
using Pkg
Pkg.activate(".")
println("Julia ", VERSION)
println("Project: ", Base.active_project())
""",
)

add(
    r"""
## Hello, world

`print` は改行せず、`println` は最後に改行します。文字列の中では `$変数名` や `$(式)` で値を埋め込めます。
""",
    r"""
## Hello, world

`print` does not add a newline; `println` does. Interpolate a value into a string with `$name` or `$(expression)`.
""",
    r"""
print("Hello, ")
println("world!")

a = 12
println("a = $a")
println("a / 2 = $(a / 2)")
""",
)

add(
    r"""
`#` から行末まではコメントです。べき乗には `^` を使います。`π` やギリシャ文字も、そのまま定数名・変数名として使えます。Julia の REPL や Jupyter では、たとえば `\pi` の後に Tab キーを押すと `π` を入力できます。
""",
    r"""
Text from `#` to the end of a line is a comment. Use `^` for powers. Constants and variables may use Greek letters. In the Julia REPL or Jupyter, type `\pi` and press Tab to enter `π`.
""",
    r"""
radius = 2
area = π * radius^2  # 円の面積 / area of a circle

ξ = 1.2
println("area = $area, ξ = $ξ")
""",
)

add(
    r"""
## 配列と行列

角括弧でベクトルを作ります。要素型を明示する場合は `Float64[...]` のように書けますが、多くの場合は Julia の型推論に任せられます。
""",
    r"""
## Arrays and matrices

Use square brackets to create a vector. You can specify its element type with syntax such as `Float64[...]`, although Julia's type inference is usually sufficient.
""",
    r"""
integers = [4, 3, 2, 1]
floats = Float64[4, 3, 2, 1]

println(integers)
println(floats)
""",
)

add(
    r"""
末尾に1要素を追加するには `push!`、複数の要素を追加するには `append!` を使います。Julia では、名前が `!` で終わる関数は、慣例として引数を変更する可能性を示します。
""",
    r"""
Use `push!` to add one element at the end and `append!` to add all elements from another collection. By convention, a Julia function whose name ends in `!` may modify an argument.
""",
    r"""
values = Int[]
push!(values, 1)
append!(values, [3, 5])
values
""",
)

add(
    r"""
行の中では空白、行の間では改行またはセミコロンを使って行列を作ります。`*` は行列積、`.*` は要素ごとの積です。
""",
    r"""
Inside brackets, spaces separate columns and newlines or semicolons separate rows. `*` performs matrix multiplication, while `.*` multiplies element by element.
""",
    r"""
M = [
    1.0 2.0
    3.0 4.0
]
v = [1.0, 2.0]

println("M * v = ", M * v)
println("M .* M = ", M .* M)
""",
)

add(
    r"""
`v'` は `v` の随伴、つまり複素共役転置です。実数ベクトルでは通常の転置と同じになります。したがって `v * v'` は外積、`v' * v` は内積です。
""",
    r"""
`v'` is the adjoint of `v`, meaning its conjugate transpose. For a real vector this is the same as an ordinary transpose. Therefore `v * v'` is an outer product and `v' * v` is an inner product.
""",
    r"""
println("outer product = ", v * v')
println("inner product = ", v' * v)

z = [1 + 2im, 3 - im]
println("adjoint of a complex vector = ", z')
""",
)

add(
    r"""
Julia の添字は **1から**始まります。`begin` と `end` は先頭・末尾の添字を表します。範囲 `start:step:stop` もよく使います。
""",
    r"""
Julia uses **one-based** indexing. `begin` and `end` refer to the first and last valid indices. Ranges such as `start:step:stop` are also common.
""",
    r"""
data = [2, 4, 6, 8]
println("first = ", data[begin], ", last = ", data[end])
println("range = ", collect(0:0.25:1))
""",
)

add(
    r"""
## 処理の流れ: `if`、`for`、`function`

Julia のブロックは `end` で閉じます。次は整数の偶奇を判定する例です。`%` は余りを計算する演算子です。
""",
    r"""
## Control flow: `if`, `for`, and `function`

Julia closes blocks with `end`. This example tests whether an integer is even or odd. `%` is the remainder operator.
""",
    r"""
n = 7
if n % 2 == 0
    println("$n is even")
else
    println("$n is odd")
end
""",
)

add(
    r"""
`for` では範囲や配列の要素を順に処理できます。
""",
    r"""
A `for` loop can iterate over a range or over the elements of a collection.
""",
    r"""
for i in 1:3
    println("iteration $i")
end

for value in [10, 20, 30]
    println(value)
end
""",
)

add(
    r"""
複数の処理を再利用するには関数にまとめます。最後に評価された式が自動的に戻り値になります。明示的な `return` も使用できます。
""",
    r"""
Put reusable work in a function. Julia automatically returns the value of the last evaluated expression; an explicit `return` is also available.
""",
    r"""
function square(x)
    x^2
end

println("3^2 = ", square(3))
""",
)

add(
    r"""
## 作図（PythonPlot を使う例）

ここでは、Matplotlib に慣れた人にも分かりやすい例として、Matplotlib を Julia から使う [PythonPlot.jl](https://github.com/JuliaPy/PythonPlot.jl) を選びます。以前この教材で使っていた PyPlot.jl と、現在使う PythonPlot.jl は、どちらも Julia と Python の橋渡しをするパッケージです。PythonPlot.jl は新しい PythonCall.jl を基盤とし、必要な Python 環境は CondaPkg.jl が管理します。

**作図に Python が必須という意味ではありません。** [Plots.jl](https://docs.juliaplots.org/stable/) や [Makie.jl](https://docs.makie.org/stable/) などを使えば、Python や Matplotlib を用いず、Julia の環境だけで計算から作図まで完結できます。このノートの数値計算部分も Julia だけで実装されています。
""",
    r"""
## Plotting with PythonPlot

We use [PythonPlot.jl](https://github.com/JuliaPy/PythonPlot.jl), which calls Matplotlib from Julia, because its interface is familiar to Matplotlib users. Both the older PyPlot.jl previously used in this tutorial and the current PythonPlot.jl are bridges between Julia and Python. PythonPlot.jl is built on the newer PythonCall.jl, and CondaPkg.jl manages the required Python environment.

**Python is not required for plotting in Julia.** Packages such as [Plots.jl](https://docs.juliaplots.org/stable/) and [Makie.jl](https://docs.makie.org/stable/) let you complete the workflow from computation to plotting in the Julia environment without Python or Matplotlib. The numerical computations in this notebook are also implemented entirely in Julia.
""",
    r"""
using PythonPlot

x = range(0, 2π; length=200)
y = sin.(x)

fig, ax = subplots()
ax.plot(x, y)
ax.set_xlabel(raw"$x$")
ax.set_ylabel(raw"$\sin(x)$")
ax.set_title("Sine function")
fig
""",
)

add(
    r"""
`.` を関数や演算子に付けると、配列の各要素へ処理を適用できます。上の `sin.(x)` や、下の `0.05 .+ ...` がその例です。
""",
    r"""
A dot on a function or operator applies it element by element. Examples are `sin.(x)` above and `0.05 .+ ...` below.
""",
    r"""
using Random
Random.seed!(2026)

xdata = range(0, 1; length=10)
ydata = 2 .* xdata
errors = 0.05 .+ 0.05 .* rand(length(xdata))

fig, ax = subplots()
ax.errorbar(xdata, ydata; yerr=errors, fmt="o")
ax.set_xlabel("x")
ax.set_ylabel("y")
fig
""",
)

add(
    r"""
正規分布に従う乱数は `randn` で作れます。
""",
    r"""
Use `randn` to draw random numbers from the standard normal distribution.
""",
    r"""
samples = randn(10_000)

fig, ax = subplots()
ax.hist(samples; bins=50)
ax.set_xlabel("x")
ax.set_ylabel("count")
fig
""",
)

add(
    r"""
## Python のライブラリを使う（任意）

このセクションは、既存の Python 資産と連携する方法を示すための任意の例です。Julia の配列、乱数、線形代数、数値計算用パッケージを使えば、NumPy を呼び出さずに Julia だけで同じ種類の計算を行えます。

Python との連携が必要な場合は、[PythonCall.jl](https://juliapy.github.io/PythonCall.jl/stable/pythoncall/) の `pyimport` で Python パッケージを読み込めます。Python の値を Julia の型へ明示的に変換するときは `pyconvert` を使います。
""",
    r"""
## Calling Python libraries (optional)

This optional section demonstrates interoperability with existing Python software. Julia provides its own arrays, random-number tools, linear algebra, and numerical packages, so the same kinds of computation can be completed entirely in Julia without calling NumPy.

When Python interoperability is useful, load a Python package with `pyimport` from [PythonCall.jl](https://juliapy.github.io/PythonCall.jl/stable/pythoncall/). Use `pyconvert` when you want to explicitly convert a Python value to a Julia type.
""",
    r"""
using PythonCall

np = pyimport("numpy")
python_values = np.linspace(0, 1, 5)
julia_values = pyconvert(Vector{Float64}, python_values)
julia_values
""",
)

add(
    r"""
# 簡単な数値計算

ここからは、常微分方程式を解くオイラー法と、円周率を見積もるモンテカルロ積分を例にします。
""",
    r"""
# Small numerical examples

We now use the Euler method for an ordinary differential equation and Monte Carlo integration to estimate π.
""",
)

add(
    r"""
## オイラー法

常微分方程式

$$
\frac{dx}{dt}=f(t,x)
$$

に対し、現在の時刻 $t_n$ で右辺を評価して

$$
x_{n+1}=x_n+h f(t_n,x_n)
$$

と進めます。これは簡単ですが、精度はステップ幅 $h$ の1次です。

例として

$$
\frac{dx}{dt}=-4(t-1)x, \qquad x(0)=e^{-2}
$$

を $0\le t\le1$ で解きます。厳密解は $x(t)=\exp[-2(t-1)^2]$ です。
""",
    r"""
## Euler method

For the ordinary differential equation

$$
\frac{dx}{dt}=f(t,x),
$$

Euler's method evaluates the right-hand side at the current time $t_n$ and advances with

$$
x_{n+1}=x_n+h f(t_n,x_n).
$$

It is simple, but only first-order accurate in the step size $h$.

As an example, solve

$$
\frac{dx}{dt}=-4(t-1)x, \qquad x(0)=e^{-2}
$$

on $0\le t\le1$. The exact solution is $x(t)=\exp[-2(t-1)^2]$.
""",
    r"""
function euler_method(f, x0, tspan, h)
    t0, t1 = tspan
    nsteps = round(Int, (t1 - t0) / h)
    t = collect(range(t0; step=h, length=nsteps + 1))
    x = Vector{Float64}(undef, nsteps + 1)
    x[1] = x0
    for i in 1:nsteps
        x[i + 1] = x[i] + h * f(t[i], x[i])
    end
    t, x
end

f(t, x) = -4 * (t - 1) * x
t_exact = range(0, 1; length=201)
x_exact = exp.(-2 .* (t_exact .- 1).^2)

fig, ax = subplots()
ax.plot(t_exact, x_exact; label="exact", color="black")
for h in (0.1, 0.02)
    t, x = euler_method(f, exp(-2), (0.0, 1.0), h)
    ax.plot(t, x; marker="o", label="Euler h=$h")
end
ax.set_xlabel("t")
ax.set_ylabel("x(t)")
ax.legend()
fig
""",
)

add(
    r"""
## モンテカルロ積分

単位正方形の中に一様乱数で点を打ち、単位円の第1象限に入った割合を4倍して $π$ を推定します。試行回数を $N$ とすると、統計誤差は一般に $O(N^{-1/2})$ で減少します。
""",
    r"""
## Monte Carlo integration

Draw uniformly distributed points in the unit square. Four times the fraction inside the first quadrant of the unit circle estimates π. With $N$ trials, the statistical error generally decreases as $O(N^{-1/2})$.
""",
    r"""
function monte_carlo_pi(rng, n)
    x = rand(rng, n)
    y = rand(rng, n)
    inside = x.^2 .+ y.^2 .< 1
    4 * count(inside) / n, x, y, inside
end

rng = MersenneTwister(2026)
pi_estimate, xmc, ymc, inside = monte_carlo_pi(rng, 2_000)
println("estimate = $pi_estimate; error = $(pi_estimate - π)")

fig, ax = subplots()
ax.scatter(xmc[inside], ymc[inside]; s=5, alpha=0.5, label="inside")
ax.scatter(xmc[.!inside], ymc[.!inside]; s=5, alpha=0.5, label="outside")
θ = range(0, π / 2; length=200)
ax.plot(cos.(θ), sin.(θ); color="black")
ax.set_aspect("equal")
ax.set_xlim(0, 1)
ax.set_ylim(0, 1)
ax.legend()
fig
""",
)

add(
    r"""
## 線形代数

標準ライブラリ `LinearAlgebra` には、トレース、行列式、固有値などの機能があります。連立一次方程式 $Ax=b$ は、逆行列を明示的に作るより `A \ b` で解くのが基本です。
""",
    r"""
## Linear algebra

The `LinearAlgebra` standard library provides traces, determinants, eigenvalues, and more. To solve $Ax=b$, prefer `A \ b` over explicitly computing the inverse.
""",
    r"""
using LinearAlgebra

A = [1.0 2.0; 3.0 5.0]
b = [1.0, 2.0]

println("trace = ", tr(A))
println("determinant = ", det(A))
println("eigenvalues = ", eigvals(A))
println("solution of A*x=b: ", A \ b)
""",
)

add(
    r"""
## 次に読むもの

- [Julia 公式 Getting Started](https://docs.julialang.org/en/v1/manual/getting-started/)
- [Julia 公式マニュアル](https://docs.julialang.org/en/v1/manual/)
- [Pkg: プロジェクト環境](https://pkgdocs.julialang.org/v1/environments/)
- [IJulia ドキュメント](https://ijulia.org/stable/)

パッケージを更新する場合は、このプロジェクトを有効にした Julia で `using Pkg; Pkg.update()` を実行します。更新後はノートブックを上から順に再実行し、結果を確認してください。
""",
    r"""
## Where to go next

- [Official Julia Getting Started guide](https://docs.julialang.org/en/v1/manual/getting-started/)
- [Julia manual](https://docs.julialang.org/en/v1/manual/)
- [Pkg project environments](https://pkgdocs.julialang.org/v1/environments/)
- [IJulia documentation](https://ijulia.org/stable/)

To update packages, activate this project and run `using Pkg; Pkg.update()` in Julia. Then execute each notebook from top to bottom and inspect the results.
""",
)

add(
    r"""
## 高速なコードを書くためのチップス

性能が必要な計算は関数の中に書き、変数の型が途中で不必要に変わらないようにします。引数に具体的な型を付けること自体は、通常は高速化に必要ありません。グローバルな定数には `const` を付けます。

不要な配列などを繰り返し作らないことも重要です。メモリ確保が多いコードではガベージコレクションにも時間がかかります。既存の配列を書き換えて再利用する関数には、慣例として `!` で終わる名前が付いています。

Julia では、関数の初回実行にコンパイル時間がかかります。実行時間を測るときは、最初に一度関数を実行してから計測し、コンパイル時間と本来の計算時間を分けて考えます。ガベージコレクションやプログラムの配布方法も C++ とは異なります。

詳しくは公式マニュアルの [Performance Tips](https://docs.julialang.org/en/v1/manual/performance-tips/) を参照してください。
""",
    r"""
## Tips for writing fast Julia code

Put performance-sensitive computation inside functions and avoid unnecessary changes of variable type. Adding concrete type annotations to function arguments is usually not required for speed. Mark global constants with `const`.

Avoid repeatedly creating arrays and other temporary objects when they are not needed. Excessive allocation also increases the time spent in garbage collection. By convention, functions that modify and reuse an existing array often have names ending in `!`.

Julia compiles a function the first time it is called for a new set of argument types. When measuring execution time, call the function once before timing it so that compilation time can be considered separately from the computation itself. Garbage collection and program deployment also differ from C++.

See the official [Performance Tips](https://docs.julialang.org/en/v1/manual/performance-tips/) for more detail.
""",
    r"""
function sum_of_squares(xs)
    total = zero(eltype(xs))
    for x in xs
        total += x^2
    end
    total
end

sum_of_squares(1:100)  # first call includes compilation
sum_of_squares(1:100)  # subsequent calls reuse compiled code
""",
)


def notebook(cells):
    for number, cell in enumerate(cells):
        cell["id"] = f"cell-{number:03d}"
    return {
        "cells": cells,
        "metadata": {
            "kernelspec": {
                "display_name": "Julia 1.13",
                "language": "julia",
                "name": "julia-1.13",
            },
            "language_info": {
                "file_extension": ".jl",
                "mimetype": "application/julia",
                "name": "julia",
                "version": "1.13.0",
            },
        },
        "nbformat": 4,
        "nbformat_minor": 5,
    }


for filename, cells in (
    ("short_intro_julia.ipynb", JA),
    ("short_intro_julia_en.ipynb", EN),
):
    path = ROOT / filename
    path.write_text(
        json.dumps(notebook(cells), ensure_ascii=False, indent=1) + "\n",
        encoding="utf-8",
    )
    print(f"wrote {path.name}: {len(cells)} cells")
