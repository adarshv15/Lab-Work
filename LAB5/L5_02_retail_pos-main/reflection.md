# Lab 5: Static Code Analysis — Reflection

### 1. What is static code analysis, and why is it useful?

Static code analysis examines source code without executing it to identify potential bugs, security vulnerabilities, and style violations. It helps improve code quality, readability, security, and maintainability.

### 2. What did Pylint, Bandit, and Flake8 identify?

Pylint identified issues such as mutable default arguments, broad exception handling, unsafe `eval()` usage, naming conventions, and missing documentation. Bandit identified the unsafe use of `eval()` and other potentially problematic patterns. Flake8 identified unused imports, missing blank lines, and formatting violations.

### 3. What changes did you make to improve the program?

I replaced unrestricted `eval()` with explicitly supported promo codes, removed unused imports, replaced the mutable default argument with `None`, added input validation, improved exception handling, used a context manager for receipt logging, and corrected formatting and naming issues.

### 4. What did you learn from this lab?

I learned that a program can execute successfully and still contain security, logic, and maintainability problems. Using multiple static analysis tools helps identify different categories of issues. Testing the program after making changes is also important to ensure that the fixes preserve its intended functionality.