# Lab 5 — Static Code Analysis Issues

| Issue | Type | Line(s) | Description | Fix Approach |
|---|---|---|---|---|
| Unsafe `eval()` | Security — Medium | 27 | Evaluates user-supplied expressions, potentially allowing arbitrary code execution. | Replace with explicitly supported promo codes and validated inputs. |
| Mutable default argument | Bug | 10 | The default receipt list is shared across function calls. | Use `None` as the default and initialize the list inside the function. |
| Bare exception | Code quality | 16 | Catches all exceptions and silently hides errors. | Catch specific exceptions and handle invalid cart items. |
| Unused imports | Code quality | 1, 3 | `json` and `logging` are imported but never used. | Remove the unused imports. |
| Incorrect stock update | Logic bug | 29–34 | The function does not actually update stock and suppresses errors. | Validate the item and quantity, then update stock correctly. |
| Unclosed file | Reliability | 36–38 | The receipt file is not explicitly closed. | Use a context manager with `with open()`. |
| Invalid quantities and tax | Logic bug | 44–47 | Negative quantities and invalid tax rates are accepted. | Validate quantities and tax rates before billing. |
| Naming and documentation | Code quality | 1, 41 | Missing docstrings and non-standard function naming reduce readability. | Add docstrings and rename `printSales()` to `print_sales()`. |
| Formatting violations | Style | Multiple | Missing blank lines and an overlong line violate PEP 8 conventions. | Apply Flake8's formatting recommendations. |