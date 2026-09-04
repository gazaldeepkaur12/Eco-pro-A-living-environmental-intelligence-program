# Manual testing

Eco-pro currently uses simple manual tests rather than an automated testing framework.

The Python program can be tested from its menu using **Option 1 — Run test sensor data**.

The test readings are designed to check different conditions:

| Test condition | What it checks |
|---|---|
| High temperature + wet soil | Plant-specific advice and classification |
| Very high temperature | High/critical classification behaviour |
| Dry soil | Dry-soil advice |
| Warm + high humidity | Multiple environmental conditions |

After running Option 1, **Option 2 — Show garden history** can be used to check that the readings were written to the CSV file with a date and time.

These are functional checks for the current learning project, not a formal software-testing suite.
