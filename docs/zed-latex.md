# Zed LaTeX Setup

Use the Zed LaTeX extension for editing and task integration. It does not
install a LaTeX distribution, so install Tectonic once on your machine.

## Install

```sh
brew install tectonic
```

Optional but useful on macOS:

```sh
brew install --cask skim
```

Skim gives a better external PDF preview flow for LaTeX than the default macOS
Preview app.

## Build In Zed

Open `paper/main.tex`, then run one of the project tasks:

- `paper: build latex`
- `paper: open pdf`
- `paper: build and open pdf`

The Zed LaTeX extension also shows tasks tagged as `latex-build` from the run
button in LaTeX files.

The PDF is generated at:

```text
paper/build/main.pdf
```

## Build In Terminal

```sh
mkdir -p paper/build
tectonic --synctex --keep-logs --outdir paper/build paper/main.tex
open paper/build/main.pdf
```

If `tectonic` is not found, install it first and restart Zed so the editor sees
the updated shell path.
