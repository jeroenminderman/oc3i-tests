<img src="https://github.com/datasciencecampus/awesome-campus/blob/master/ons_dsc_logo.png">

# Contributing Guidelines

Thank you for your interest in contributing to this repository! This guide is intended for internal colleagues and outlines the standards and best practices we follow to ensure high-quality, maintainable code.

## Setup Instructions

To set up your development environment for this project:

```powershell
# Clone the repository
git clone https://github.com/your-org/python-project.git
cd python-project

# Set up a virtual environment
python -m venv .venv
.venv\Scripts\Activate

# Install dependencies and pre-commit hooks
pip install -r requirements.txt
pip install pre-commit
pre-commit install

# Check pre-commit installation
pre-commit run --all-files
```

For more details on contributing, see the sections below.

## Getting Started
- Ensure you have the necessary permissions to access and contribute to this repository.
- Clone the repository and create a new branch for your work.

## Documentation Standards
- **Docstrings:** Use [Google-style docstrings](https://google.github.io/styleguide/pyguide.html#38-comments-and-docstrings) for all public modules, classes, functions, and methods.
- Include clear descriptions of parameters, return values, exceptions, and usage examples where appropriate.
- Keep documentation up to date with code changes.

## Code Quality & Best Practices
- **Modular Coding:** Write small, focused functions and classes. Avoid large, monolithic code blocks.
- **Readability:** Follow [PEP 8](https://peps.python.org/pep-0008/) for Python code style. Use meaningful variable and function names.
- **Type Hints:** Use Python type hints where possible to improve code clarity and support static analysis.
- **Comments:** Use comments to explain complex logic, but avoid obvious or redundant comments.

## Unit Testing
- All new features and bug fixes must include appropriate unit tests.
- Place tests in the `tests/` directory, mirroring the structure of the `src/` directory.
- Use `pytest` as the testing framework.
- Ensure all tests pass before submitting a pull request.

## Submitting Changes
1. Fork the repository and create a feature branch.
2. Make your changes, ensuring code and documentation standards are met.
3. Add or update unit tests as needed.
4. Run all tests locally: `pytest`
5. Submit a pull request with a clear description of your changes.
6. Address any feedback or requested changes promptly.

## Code Review
- All contributions are subject to code review by maintainers.
- Be responsive to feedback and willing to make improvements.

## Additional Best Practices
- Avoid hardcoding values; use configuration files or environment variables where appropriate.
- Write reusable and maintainable code.
- Keep dependencies up to date and document any new dependencies in `requirements.txt`.

## RAPs (Reusable Analytical Pipelines) Standards
To ensure our analytical pipelines are robust, maintainable, and reusable, all RAPs should adhere to the following standards:

- **Version Control:** All code must be tracked in version control.
- **Containerised Code:** Package your RAP using containers (e.g., Docker) to ensure consistent environments and reproducibility. Include a `Dockerfile` and usage instructions.
- **Modularised Code:** Structure code into logical, reusable modules.
- **ETL:** Implement clear Extract, Transform, Load (ETL) processes. Separate data ingestion, transformation, and loading logic for clarity and reusability.
- **Logging:** Use robust logging throughout your pipeline to capture key events, errors, and process milestones.
- **Defensive Coding, Validation, and Tests:** Write code defensively, validate inputs/outputs, and include comprehensive unit and integration tests.
- **Data Visualisation:** Provide scripts or modules for generating relevant data visualisations to support analysis and reporting.
- **API for Outputs:** Expose pipeline outputs via an API (e.g., RESTful endpoints or FastAPI) to enable programmatic access and integration with other systems.
- **Parameter Store:** Use a parameter store or configuration management system to manage environment variables, secrets, and pipeline parameters securely and flexibly.

Please ensure your RAP contributions meet these standards.

## Reference
- For more detailed guidelines, examples, and FAQs, please refer to the project wiki.
- Our wiki is organized using the Diátaxis framework, with dedicated sections for Tutorials, How-To Guides, Reference, and Explanations. When contributing, please add or update content in the most appropriate section to help others find information easily.
- If your contribution introduces new concepts, workflows, or tools, please consider adding or updating relevant sections in the project wiki to help others benefit from your knowledge.

## Questions?
If you have any questions, please reach out to the maintainers or open an issue in the repository.

Thank you for helping us improve this project!
