# import pytest
# from py.xml import html

# # Customizing the HTML report metadata
# def pytest_html_report_title(report):
#     report.title = "USPS Address Lookup API Test Report"

# def pytest_html_results_summary(prefix, summary, postfix):
#     """Custom results summary."""
#     prefix.extend([html.p("This report contains test results for the USPS Address Lookup API.")])
#     summary.extend([html.p("All tests validate API response correctness, structure, and performance.")])
#     postfix.extend([html.p("Generated using pytest-html.")])

# def pytest_html_results_table_header(cells):
#     """Customize table headers."""
#     cells.insert(1, html.th("Description"))
#     cells.pop()  # Remove 'Links' column

# def pytest_html_results_table_html(report, data):
#     """Modify table structure."""
#     if report.passed:
#         data.insert(1, html.td("✅ Test Passed", class_="passed"))
#     elif report.failed:
#         data.insert(1, html.td("❌ Test Failed", class_="failed"))
#     elif report.skipped:
#         data.insert(1, html.td("⚠️ Test Skipped", class_="skipped"))

# def pytest_html_results_table_row(report, cells):
#     """Customize table row display."""
#     cells.insert(1, html.td(report.description if hasattr(report, "description") else "No description"))
#     cells.pop()  # Remove 'Links' column

# @pytest.hookimpl(hookwrapper=True)
# def pytest_runtest_makereport(item, call):
#     """Attach test description dynamically from function docstring."""
#     outcome = yield
#     report = outcome.get_result()
#     report.description = str(item.function.__doc__)


import pytest
from datetime import datetime

# Customizing the report title
def pytest_html_report_title(report):
    report.title = "USPS Address Lookup API Test Report"

# Customizing the results summary
@pytest.hookimpl(tryfirst=True)
def pytest_html_results_summary(prefix, summary, postfix):
    prefix.append("<p>USPS API Automated Testing Report.</p>")
    summary.append("<p>Validates USPS address lookup API responses dynamically.</p>")
    postfix.append(f"<p>Report generated on {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}.</p>")

# Customizing table headers
@pytest.hookimpl(tryfirst=True)
def pytest_html_results_table_header(cells):
    cells.insert(1, "<th>Description</th>")  # Add new column for descriptions
    cells.pop()  # Remove the 'Links' column

# Customizing table rows
@pytest.hookimpl(tryfirst=True)
def pytest_html_results_table_row(report, cells):
    cells.insert(1, f"<td>{report.description if hasattr(report, 'description') else 'No description'}</td>")
    cells.pop()  # Remove 'Links' column

# Attach test descriptions dynamically from function docstrings
@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    report = outcome.get_result()
    report.description = item.function.__doc__ if item.function.__doc__ else "No description"