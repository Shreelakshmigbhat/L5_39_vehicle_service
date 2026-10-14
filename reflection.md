# Reflection — Lab 5: Static Code Analysis

**Note:** The supplied handout describes reflection questions but does not show the four questions themselves. The answers below cover four standard reflection prompts. If your instructor provided a separate page with exact questions, use those exact prompts instead.

## 1. What is static code analysis, and why is it useful?

Static code analysis examines source code without executing the program. It helps identify likely bugs, unsafe coding patterns, maintainability problems, and style violations early. It complements testing: tests show how code behaves for selected inputs, while static analysis can flag suspicious patterns even when a test does not exercise them.

## 2. What is the difference between Pylint, Bandit, and Flake8?

Pylint focuses on code quality, naming, documentation, design, and possible programming errors. Bandit scans Python code for common security weaknesses, such as risky shell execution. Flake8 focuses on PEP 8 style and common lint errors, including whitespace, line length, and unused imports. Their checks overlap in places, so using all three provides broader coverage than relying on one tool.

## 3. Which issues were important in this program, and how were they fixed?

The most important security issue was constructing a shell command with `shell=True` and a function argument. I replaced it with `pathlib` and `shutil.copy2`, avoiding shell interpretation. I also fixed the mutable default list by using `None`, removed the broad exception handler, replaced MD5 with SHA-256 for the job-card identifier, removed the unused hardcoded password, added explicit UTF-8 encoding, standardized naming and formatting, and added a main guard.

## 4. What did you learn, and what are the limitations of static analysis?

I learned that code can appear to work while still containing reliability, security, and maintainability problems. Static analysis provides fast and repeatable feedback, but its findings must be interpreted in context. A warning can be a false positive, and a clean report does not prove that the program is correct or secure. I would combine these tools with unit tests, code review, and runtime testing. After making changes, I would rerun the demo and all three tools and compare the before-and-after reports.
