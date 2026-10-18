# Kuchisake-onna

<p align="center">
  <b>口裂け女 — The Slit-Mouthed Woman</b>
</p>

<p align="center">
  <i>"Am I beautiful?"</i>
</p>

---

You are walking alone.

Footsteps follow yours. A woman approaches, her face concealed behind a surgical mask. She stops in front of you.

Then she asks a question.

**There are only two answers. Neither will save you.**

`kuchisake-onna` is a Python package inspired by the infamous Japanese urban legend. It turns a simple question into an encounter you cannot escape.

## Installation

Clone the repository:

```bash
git clone <repository-url>
cd kuchisake-onna
```

Install the package:

```bash
python -m pip install .
```

Requires **Python 3.10 or later**.

## The Encounter

Import the package:

```python
import kuchisake_onna
```

You will be asked:

```text
Answer only with 'yes' or 'no'.
Am I beautiful?
```

Choose your answer carefully:

- `yes`
- `no`

Anything else? She asks again.

Once you provide a valid answer, the encounter ends in an exception:

```python
CutByKuchisakeOnnaError
```

**The question is unavoidable. The outcome is inevitable.**

## Exceptions

The package defines its own exception:

```python
from kuchisake_onna.exceptions import CutByKuchisakeOnnaError
```

It represents the fictional consequences of answering Kuchisake-onna's question.

Catching the exception may stop the error from propagating. It does not change the answer you gave.

## Important Warning

Importing `kuchisake_onna` immediately invokes the encounter. The package also ignores `SIGINT`, commonly associated with `Ctrl+C`.

These are behaviors of the current implementation. Importing this package can therefore affect the program that loads it.

**Do not import it casually into applications that require normal signal handling.**

## Testing

Install `pytest`:

```bash
python -m pip install pytest
```

Run the test suite from the repository root:

```bash
python -m pytest -v
```

GitHub Actions runs the tests on pushes, pull requests, and manual workflow dispatches.

## Project Structure

```text
kuchisake-onna/
├── .github/
│   └── workflows/
│       └── ci.yml
├── .gitignore
├── LICENSE
├── README.md
├── setup.py
├── src/
│   └── kuchisake_onna/
│       ├── __init__.py
│       ├── exceptions.py
│       └── kuchisake_onna.py
└── tests/
    └── test_kuchisake_onna.py
```

## License

This project is distributed under the [MIT License](LICENSE).

## Final Words

The mask comes off.

The question comes again.

And somewhere, in the silence between your answer and the exception, you begin to understand.

**You were never being asked whether she was beautiful.**
