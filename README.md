# 🎓 TalentSync - Campus Placement Portal 🚀

![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Flask](https://img.shields.io/badge/Flask-000000?style=for-the-badge&logo=flask&logoColor=white)
![MySQL](https://img.shields.io/badge/MySQL-4479A1?style=for-the-badge&logo=mysql&logoColor=white)
![HTML5](https://img.shields.io/badge/HTML5-E34F26?style=for-the-badge&logo=html5&logoColor=white)
![CSS3](https://img.shields.io/badge/CSS3-1572B6?style=for-the-badge&logo=css3&logoColor=white)

> An enterprise-grade, full-stack Campus Placement Management System designed to seamlessly bridge the gap between College Placement Cells (TPOs) and Students.

---

## ✨ Core Features

*   **🔐 Role-Based Access Control (RBAC):** Highly secure, dedicated dashboards tailored for Administrators (TPOs) and Students via session handling.
*   **⚙️ Automated Eligibility Engine:** Smart backend logic that automatically filters and displays active job drives by dynamically checking a student's academic CGPA and branch against company requirements.
*   **📊 Application Tracking:** A relational database architecture mapping student profiles to job postings for streamlined administrative oversight.
*   **🎨 Modern Enterprise UI:** A fully responsive, clean, and aesthetic frontend utilizing CSS grid and card layouts for an intuitive user experience.

---

## 🏗️ System Architecture

Below is the interactive data-flow diagram showing how the platform operates:

```mermaid
graph TD
    A[User Browser] -->|HTTP Request / Login| B(Flask App Engine)
    B -->|SQL Queries| C[(MySQL placement_db)]
    C -->|Return Validated Data| B
    B -->|Jinja2 Rendering| D[Dynamic HTML Dashboards]
    D -->|Display UI| A
