Kuchisake-onna

A Python library inspired by Kuchisake-onna (口裂け女), the slit-mouthed woman from Japanese urban folklore.

Kuchisake-onna is a small Python package that recreates the infamous question whispered through the legend:

«Am I beautiful?»

There is no safe answer.

The library asks the question, accepts "yes" or "no", and raises a custom exception regardless of which answer you give. Once she has asked, the outcome is already waiting.

Features

- Interactive question-and-answer mechanism.
- Accepts "yes" and "no" as valid answers.
- Re-prompts the user when an invalid answer is entered.
- Provides a custom exception: "CutByKuchisakeOnnaError".
- Exposes a simple function, "ask_question()".
- Includes automated tests using "pytest".
- Supports Python 3.10 and later.

Requirements

- Python 3.10 or later.
- "pip" for installation.
- A terminal that supports interactive input when running the question.

The package uses Python's standard library and does not require third-party runtime dependencies.

Installation

Install from source

Clone the repository and enter its directory:

git clone <repository-url>
cd kuchisake-onna

Replace "<repository-url>" with the actual Git repository URL.

Install the package:

python -m pip install .

To install it in editable mode during development:

python -m pip install -e .

The package configuration is defined in "setup.py".

Verify the installation

You can check the installed package metadata with:

python -m pip show kuchisake-onna

Quick Start

Warning: Importing "kuchisake_onna" immediately asks the question and raises "CutByKuchisakeOnnaError". This is intentional in the current implementation. Once imported, there may be no turning back.

Run the following in a Python terminal:

import kuchisake_onna

The package displays:

Answer only with 'yes' or 'no'.
Am I beautiful?

Enter either "yes" or "no".

The package then raises:

kuchisake_onna.exceptions.CutByKuchisakeOnnaError

The exception is raised regardless of your answer. She does not accept refusal, and she does not forgive mistakes.

How It Works

The main function is "ask_question()", implemented in "src/kuchisake_onna/kuchisake_onna.py".

Its behavior is straightforward:

1. Display instructions requiring "yes" or "no".
2. Ask the user whether Kuchisake-onna is beautiful.
3. Validate the response.
4. Repeat the question if the response is invalid.
5. Raise "CutByKuchisakeOnnaError" after a valid response.

Valid answers

Input| Behavior
"yes"| Raises "CutByKuchisakeOnnaError"
"no"| Raises "CutByKuchisakeOnnaError"
Any other input| Asks the question again

Note: The input is case-sensitive. For example, "YES", "Yes", and "No" are invalid responses in the current implementation.

The library does not distinguish between the consequences of answering "yes" and "no": both produce the same exception message. The question is asked, the answer is given, and something answers in return.

API Reference

"ask_question()"

ask_question() -> Never

Asks the user the question and raises "CutByKuchisakeOnnaError" after receiving a valid answer.

Parameters: None.

Returns: No value. The function is annotated with "typing.Never" because it always raises an exception after receiving a valid response.

Raises:

- "CutByKuchisakeOnnaError": Raised after the user enters either "yes" or "no".

Example:

from kuchisake_onna import ask_question

ask_question()

In the current implementation, importing the package itself already invokes "ask_question()". Consequently, the exception will occur during the import, before execution reaches the explicit function call. By then, the question has already been asked.

"CutByKuchisakeOnnaError"

class CutByKuchisakeOnnaError(Exception)

A custom exception representing the fictional consequences of answering Kuchisake-onna's question.

It inherits from Python's built-in "Exception" class.

Example:

from kuchisake_onna.exceptions import CutByKuchisakeOnnaError

Importing the package's submodule also initializes the parent package first. Therefore, this import triggers the question and exception under the current implementation. Even the path to the exception passes through her question.

"__version__"

__version__ = "1.0.0"

The package's current version string.

Normally, it can be accessed using:

import kuchisake_onna

print(kuchisake_onna.__version__)

However, the current import-time question raises an exception before this statement can execute normally. The version may remain unseen.

Exception Handling

The custom exception inherits from "Exception", so it can be caught using ordinary Python exception handling.

For example, the general pattern is:

try:
    # An operation that may raise the custom exception
    ...
except CutByKuchisakeOnnaError as exc:
    print(f"Kuchisake-onna raised an exception: {exc}")

Because the current package raises the exception during import, catching it requires wrapping the import itself:

try:
    import kuchisake_onna
except Exception as exc:
    print(type(exc).__name__)
    print(exc)

The import will still ask the question before raising the exception. Catching the error does not silence the question.

Project Structure

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

Source files

File| Purpose
"setup.py"| Defines package metadata and installation configuration.
"src/kuchisake_onna/__init__.py"| Initializes the package, exposes public names, and invokes the question.
"src/kuchisake_onna/kuchisake_onna.py"| Implements "ask_question()".
"src/kuchisake_onna/exceptions.py"| Defines "CutByKuchisakeOnnaError".
"tests/test_kuchisake_onna.py"| Contains automated tests for import behavior.
".github/workflows/ci.yml"| Runs automated tests using GitHub Actions.
".gitignore"| Lists files and directories Git should ignore.

Running Tests

The project uses "pytest" for automated testing.

Install the testing dependency:

python -m pip install pytest

Install the package in editable mode:

python -m pip install -e .

Run the tests from the repository root:

python -m pytest -v

The current test suite checks the import behavior for both valid answers:

- "yes"
- "no"

It replaces "input()" with a mocked function so the tests do not require manual keyboard input.

The tests expect the import to raise an exception for both answers.

Continuous Integration

The repository includes a GitHub Actions workflow at:

.github/workflows/ci.yml

The workflow runs on:

- Pushes to the repository.
- Pull requests.
- Manual workflow dispatches.

The CI job:

1. Checks out the repository.
2. Sets up Python 3.12.
3. Upgrades "pip" and "setuptools".
4. Installs the package in editable mode.
5. Installs "pytest".
6. Runs the test suite.

You can inspect the workflow file to modify the Python version or add additional checks.

Important Implementation Details

Import-time execution

The package currently calls "ask_question()" directly from "__init__.py".

This means importing the package is not a passive operation: it requests input and raises an exception.

For example:

import kuchisake_onna

does not simply load the package. It runs the interactive behavior.

This is an intentional aspect of the current design, but it also means the package cannot be imported normally without triggering the question. The moment the package enters your process, she is already there.

Signal handling

The package currently executes:

signal.signal(signal.SIGINT, signal.SIG_IGN)

during initialization.

This tells Python to ignore "SIGINT", which is commonly generated by pressing "Ctrl+C" in a terminal.

Important: This changes signal handling for the importing process. It can affect the application that imports this package, so use the library with that side effect in mind. Even an attempt to interrupt the encounter may go unanswered.

Input validation

The implementation accepts only the exact strings "yes" and "no".

It does not currently normalize whitespace or letter casing. Invalid responses cause the question to be repeated.

The question will continue until an answer is recognized. Silence is not an escape.

Exception behavior

Both valid answers lead to the same custom exception:

raise CutByKuchisakeOnnaError(
    "Kuchisake Onna Sama doesn't like your answer."
)

The exception is part of the library's fictional behavior, not an indication of an actual physical consequence. The warning is fictional; the unease is intentional.

Development

To contribute to development:

1. Clone the repository.
2. Install the package in editable mode.
3. Install "pytest".
4. Make your changes.
5. Run the test suite.
6. Submit a pull request.

Useful commands:

python -m pip install -e .
python -m pip install pytest
python -m pytest -v

Please ensure that changes to the question, input validation, exception behavior, or import-time execution are reflected in the tests and documentation.

Versioning

The current package version is:

1.0.0

The version is defined in "src/kuchisake_onna/__init__.py" and should remain consistent with the version in "setup.py" when releasing a new version.

License

This project is distributed under the MIT License. See the ""LICENSE"" (LICENSE) file for the complete license text.

Disclaimer

Kuchisake-onna is inspired by Japanese urban folklore. This package is a fictional programming project intended for entertainment and experimentation.

It does not cause real-world supernatural events or physical harm.

---

Answer carefully. She is listening. And she is closer than you think.
