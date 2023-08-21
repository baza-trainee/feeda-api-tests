from setuptools import setup, find_packages

setup(
    name="Feeda API tests",
    version="0.1.0",
    authors=["Oleksandr Kozlov", "Dmytro Tyshchenko"],
    packages=find_packages(),
    entry_points={
        "console_scripts": [
            "run-tests=feeda-api-tests:run_tests",
            "allure-report=feeda-api-tests:generate_allure_report",
            "allure-serve=feeda-api-tests:serve_allure_report",
        ],
    },
)
