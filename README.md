# sumsets
Powered by Python and itertools, leveraging the `combinations` function.

## Scenario
You're a small business owner trying to reconcile some expenses. Let's say this mystery expense needs to add up to $1,234.56. No problem. Import your transactions (CSV) and tell sumsets you need it to return a value that adds up to $1,234.56. Let the combinations algorithm do the heavy lifting. It will find all possible combinations of expenses that added up to $1,234.56. Your "needle in a haystack" problem just got a lot easier.

## Quick Start
Include a CSV of your transactions with proper formatting. Refer to the template. *Amounts* must be valid numbers formatted in dollars and cents (ie. "113.37"). Remove any currency symbols or dollar signs. This program will not transform your data. Name it **transactions.csv** and store it in the same folder as **sumsets.py**.

Once your transactions csv is ready, simply run **sumsets.py**.
