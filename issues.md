# Static Code Analysis Issues

> The line numbers below refer to the original `vehicle_service.py` supplied for the lab. Confirm or adjust them against the actual Pylint, Bandit, and Flake8 reports generated on your machine. These are source-code findings, not claimed analyzer output.

| Issue | Type | Line(s) | Description | Fix Approach |
|---|---|---:|---|---|
| Shell command with `shell=True` | Security (high priority) | 55–57 | `subprocess.call("cp services.json " + folder, shell=True)` builds a shell command from a parameter. An unsafe folder value could alter the command. | Replaced shell execution with `pathlib.Path` and `shutil.copy2`, which copy the file without invoking a shell. |
| Mutable default argument | Bug / maintainability | 13 | `history=[]` is created once when the function is defined and can be shared by calls that omit `history`. | Changed the default to `None` and create a new list inside the function. |
| Broad exception handler | Reliability | 21–26 | `except Exception` catches unrelated errors and can hide the real cause. | Replaced exception handling with a dictionary lookup and an explicit missing-record check. |
| Weak hash for job card ID | Security / design | 39 | MD5 is a weak hash and should not be used for security-sensitive purposes. | Switched to SHA-256 while retaining a short, deterministic display ID. The ID value therefore changes. |
| Hardcoded credential | Security | 8 | `ADMIN_PASSWORD` embeds a password in source code and is not used by the demo. | Removed the unused credential. If authentication is added later, obtain secrets from environment/configuration and manage them securely. |
| Missing file encoding on write | Portability / style | 49–50 | The JSON output file is opened without explicitly specifying an encoding. | Added `encoding="utf-8"`. |
| Non-PEP 8 function and variable names / inconsistent spacing | Style | Throughout | Names such as `addService`, `totalCost`, and `jobCardId` use inconsistent naming, and spacing is inconsistent. | Renamed functions to `snake_case`, used descriptive names, and formatted the code consistently. |
| No main guard | Maintainability | 69–end | The demonstration runs whenever the module is imported, making it harder to reuse functions in tests or other modules. | Wrapped the demo call in `if __name__ == "__main__":`. |
