# 🛒 SauceDemo Test Automation Framework (Python)

[![E2E Tests](https://github.com/Kaustubh3197/saucedemo-test-automation/actions/workflows/tests.yml/badge.svg?branch=main)](https://github.com/Kaustubh3197/saucedemo-test-automation/actions/workflows/tests.yml)

End-to-end test automation for an e-commerce web app ([saucedemo.com](https://www.saucedemo.com), a public practice store),
written entirely in **Python** with **two industry-standard browser tools** and run automatically through **CI/CD**.

| Layer | Tool | What it does |
|---|---|---|
| Modern E2E tests | **Playwright + pytest** | Login, cart, sorting, checkout on Chrome, Firefox & mobile |
| Classic E2E tests | **Selenium + pytest** | The same critical flows, the enterprise way |
| Automation pipeline | **GitHub Actions** | Runs every test on each push, pull request & nightly |

## 🧩 How the pieces fit together

```
 You push code ──▶ GitHub Actions starts fresh Linux machines
                        │
       ┌────────────────┼────────────────┬──────────────┐
       ▼                ▼                ▼              ▼
  Playwright       Playwright       Playwright      Selenium
  (Chromium)       (Firefox)        (Mobile)        (Chrome)
       └────────────────┴───────┬────────┴──────────────┘
                                ▼
                  HTML reports + traces/screenshots
                                ▼
            ✅ / ❌ shown on the commit / pull request
```

- **pytest** is the test runner. It finds the tests, runs them and reports pass/fail.
- **Playwright / Selenium** are the robot testers. They open a real browser and act like a customer.
- **GitHub Actions** is the manager. It tells the robots to test whenever code changes.

## ✅ What is tested

| # | Scenario | Playwright | Selenium |
|---|---|:-:|:-:|
| 1 | Valid user can log in | ✅ | ✅ |
| 2 | Locked-out user sees an error | ✅ | ✅ |
| 3 | Wrong password is rejected | ✅ | ✅ |
| 4 | Logged-out user can't open the products page | ✅ | |
| 5 | Adding/removing items updates the cart badge | ✅ | ✅ |
| 6 | Products sort by price (low → high, high → low) | ✅ | |
| 7 | Products sort by name (Z → A) | ✅ | |
| 8 | Full checkout: cart → details → order confirmed | ✅ | ✅ |
| 9 | Order total = item total + tax | ✅ | |
| 10 | Checkout form requires first name | ✅ | |
| 11 | Product details page: name and price (3 products), add/remove, back button | ✅ | |

## 🏗️ Design patterns used
- **Page Object Model (POM)**: each page's selectors and actions live in one class, so tests read like plain English and a UI change is fixed in one place.
- **pytest fixtures**: reusable setup such as "a logged-in user on the products page", and clean browser start/stop.
- **Data-driven tests** with `@pytest.mark.parametrize`.
- **Explicit waits** (Selenium) and **auto-waiting** (Playwright) to avoid flaky tests.
- **Cross-browser & mobile testing** using a GitHub Actions matrix.
- **Artifacts on failure**: screenshots, videos, traces and HTML reports downloadable from each CI run.

## 📁 Project structure
```
├── .github/workflows/tests.yml   # CI pipeline
├── playwright-tests/
│   ├── pages/                    # Page objects
│   ├── tests/                    # Test files
│   ├── conftest.py               # Fixtures (logged-in user, etc.)
│   └── pytest.ini                # Base URL, tracing, screenshots
└── selenium-tests/
    ├── pages/                    # Page objects (+ BasePage with waits)
    ├── tests/                    # Test files
    ├── conftest.py               # Chrome driver fixture
    └── pytest.ini
```

## ▶️ Run locally

Needs Python 3.10+. Using a virtual environment is recommended:
```bash
python -m venv .venv
source .venv/bin/activate        # Windows: .venv\Scripts\activate
```

**Playwright**
```bash
cd playwright-tests
pip install -r requirements.txt
playwright install                       # downloads the browsers
pytest                                   # run on Chromium
pytest --headed --slowmo 500             # watch the browser
pytest --browser firefox                 # run on Firefox
pytest --device "Pixel 7"                # run as a phone
playwright show-trace test-results/<folder>/trace.zip   # debug a failure
```

**Selenium**
```bash
cd selenium-tests
pip install -r requirements.txt
pytest                                   # headless Chrome
HEADLESS=false pytest                    # watch the browser
```

## 🚀 Ideas to extend
- API tests with Playwright's `APIRequestContext`
- Visual regression testing with screenshots
- Accessibility checks with `axe-playwright-python`
- Allure reporting
- Test data loaded from a JSON/CSV file
