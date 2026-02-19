# 🛡️ Cyber Security Course Portfolio
### Threat Intelligence • Machine Learning • Phishing Detection • MITRE ATT&CK

> A hands-on cyber security repository combining real-world threat intelligence,  
> machine learning techniques, and AI-assisted malware & phishing analysis.

---

## 📌 Repository Overview

This repository contains all **labs** and the **final project** developed as part of the Cyber Security course.

The work focuses on:
- Real-world attack scenarios  
- Practical threat analysis  
- Mapping adversary behavior to **MITRE ATT&CK**  
- Applying **AI & ML** to modern cyber threats  

The learning path progresses from **Cyber Threat Intelligence (CTI)** to **ML-based detection**,  
and culminates in an **AI-assisted phishing analysis project**.

---

## 🧪 Labs Overview

| Lab | Topic | Focus |
|----|------|------|
| **Lab 1** | 🧩 Cyber Threat Intelligence Mapping | Mapping real CTI reports to MITRE ATT&CK |
| **Lab 2** | 🚨 Network Anomaly Detection | ML-based anomaly detection on network traffic |
| **Lab 3** | Accelerated AI|Exploring advanced AI applications
| **Lab 4** | 🤖 LLM Tools & Agents | Using LLMs to explain and analyze security data |
| **Lab 5** | LLM Agent Workflow|Building workflows with LLM agents



## Project Overview

This project presents an **image-based phishing detection system** that identifies malicious websites using screenshot images rather than textual analysis. Modern phishing attacks increasingly rely on visual imitation of legitimate interfaces, making visual classification an important complementary defense approach.

The system uses a **ResNet18 convolutional neural network** with transfer learning to efficiently detect phishing pages under CPU-only constraints. The dataset was carefully prepared with labeled screenshots, stratified data splits, and exploratory data analysis to ensure reliable evaluation.

A modular detection pipeline inspired by real-world cybersecurity workflows was implemented, including preprocessing, inference, decision logic, and reporting stages. The model was evaluated using security-focused metrics such as accuracy, precision, recall, and F1-score, along with robustness testing under visual perturbations.

Overall, the project demonstrates a practical baseline solution for phishing screenshot detection that combines efficient deep learning, structured pipeline design, and realistic cybersecurity evaluation.

