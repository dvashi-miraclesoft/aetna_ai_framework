# **AI-Integrated Test Automation Ecosystem**

### **Overview**
This framework is a high-level automation solution designed to validate **Conversational AI** and **Healthcare Backend Services**. It combines traditional QA methodologies with **AI Model Evaluation** to provide a 360-degree view of system health, focusing on natural language understanding and data integrity.

---

### **Core Modules**
* **Behavior Driven Development (BDD)**: Utilizes **Cucumber/Behave** to define and execute business-readable test scenarios for chatbots via Gherkin syntax.
* **AI/ML Model Evaluation**: Features a custom engine built with **Scikit-Learn** to calculate **Precision, Recall, and F1-scores** for intent classification auditing.
* **Full-Stack Automation**: 
    * **UI Testing**: **Selenium WebDriver** for live browser-based portal validation.
    * **API Testing**: Automated RESTful service checks for member and healthcare provider data.
    * **Database Validation**: Direct SQL integrity checks for backend data persistence.
* **Security & Compliance**: Integrated **GenAI Data Builder** for generating synthetic, HIPAA-compliant member data for non-production testing.
* **Performance Simulation**: Includes IVR signal simulation to test telephony-based virtual assistant paths.



---

### **Technology Stack**
* **Language**: Python 3.12
* **Test Runners**: Pytest & Behave
* **Browser Automation**: Selenium
* **Machine Learning**: Scikit-Learn
* **Version Control**: Git

---

### **Project Structure**
```text
aetna_ai_framework/
├── features/           # Cucumber/BDD feature files
├── src/                # Core logic: ML evaluators and data builders
├── tests/              # Functional, API, UI, and Database test scripts
├── venv/               # Python Virtual Environment
├── report.html         # Auto-generated test execution report
└── requirements.txt    # Project dependencies
