# Lab 5 submission checklist

Files included:
- `vehicle_service.py` — cleaned implementation.
- `issues.md` — issue table and fixes.
- `reflection.md` — four reflection answers (the uploaded handout does not contain the exact four question prompts).

## Run and compare behaviour

```bash
python vehicle_service.py
```

The demo should report totals of 2300 for `KA01AB1234` and 2500 for `KA05XY9876`, and three vehicles on file. The job-card ID changes because MD5 was replaced with SHA-256. The busiest vehicle is `KA01AB1234`.

## Generate reports locally

Activate your virtual environment, install the tools, then run these commands from this directory:

```bash
python -m pip install pylint bandit flake8
python -m pylint vehicle_service.py > pylint_after.txt 2>&1
python -m bandit -r vehicle_service.py > bandit_after.txt 2>&1
python -m flake8 vehicle_service.py > flake8_after.txt 2>&1
```

For the before reports, run the same commands against your untouched original file before replacing it, naming the outputs `pylint_before.txt`, `bandit_before.txt`, and `flake8_before.txt`. Do not label reports as generated unless you actually ran the tools. This environment could not install the tools because package-index network access was unavailable, so no analyzer output or score is fabricated here.

## Suggested three commits

Make these commits in your Git repository, adjusting the files/staging to match your workflow:

1. `git add issues.md && git commit -m "docs: document static analysis findings"`
2. `git add vehicle_service.py && git commit -m "fix: address code quality and security issues"`
3. `git add reflection.md README_SUBMISSION.md && git commit -m "docs: add lab reflection and verification steps"`

The lab handout asks for before-and-after reports as well as three commits. Keep the original source/report outputs until the comparison is complete.
