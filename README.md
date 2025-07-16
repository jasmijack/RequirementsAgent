# Business Requirements Generator

> A simple, interactive Python script that captures user input and system metadata to generate a Business Requirements Document (BRD), including user stories, technical requirements, and a suggested system architecture. Optional export to JIRA-ready formats included.


## Features
- Interactive prompts for feature ideas, goals, stakeholders, and expected impact
- Outputs a Word document (.docx) formatted as a BRD
- Includes auto-generated user stories and technical requirements based on system type
- Provides a basic suggested system architecture block
- Exports a CSV file ready for JIRA import (includes summary, description, and issue type)

## Prerequisites
- Python 3.7 or later
- python-docx
- (Optional) requests if you want to auto-import to JIRA
pip install python-docx requests


## Usage
Run the script:

_python business_requirements_generator.py_

You'll be prompted to provide:

- A new feature or idea

- The primary business goal

- Target users or stakeholders

- The expected business impact

Output:

- Business_Requirements_YYYYMMDD_HHMMSS.docx – full document including:

  - Business context

  - Stakeholders

  - Expected impact

  - User stories

  - Technical requirements

  - Suggested architecture

- Jira_Import_YYYYMMDD_HHMMSS.csv


## Jira Import CSV Format

| Summary      | Description                                         | Issue Type |
| ------------ | --------------------------------------------------- | ---------- |
| Feature Idea | Overview, impact, and system config combined in one | Task       |


## 🧾 License
This project is for educational and internal use only.


## 🤝 Contributing
Contributions are welcome! Feel free to submit issues or pull requests to improve JIRA integration or expand export capabilities.





