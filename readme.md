# 💊 Prescription Management System (Serverless on AWS)

A secure, scalable prescription and medication tracking system built using **AWS Lambda**, **API Gateway**, **Cognito**, **Python**, and **PostgreSQL**. Designed for clinics or pharmacies, this backend API manages prescriptions and prescription items with strict role-based access control via API Gateway and a custom Lambda authorizer.

## 🧰 Tech Stack

- **Runtime**: Python (AWS Lambda)
- **API Layer**: API Gateway + Lambda Integrations
- **Authorization**: Custom Lambda Authorizer (Cognito JWT)
- **Access Control**:
  - 🔐 **Doctors**: Full access to prescriptions and items (GET, POST, PUT)
  - 👤 **Staffs**: Read-only access (GET only)
- **Database**: PostgreSQL (via SQLAlchemy ORM)
- **Infrastructure as Code**: Terraform

## 🏗️ Features

- 🧑‍⚕️ View, create, and update **prescriptions**
- 💊 Manage **prescription items** linked to each prescription
- 🔐 Role-based access control (doctors vs staff)
- 🔄 API Gateway authorizer returns dynamic IAM policies
- 📦 Modular backend architecture with clear separation of concerns

## 🔐 Access Control Summary

| Role         | Permissions                                      |
|--------------|--------------------------------------------------|
| **doctors**  | View, create, and update prescriptions & items   |
| **staff**   | View prescriptions & items only (read-only)      |

- Access is enforced by **API Gateway** using IAM policies returned by a **Lambda authorizer**
- Auth is handled with **Cognito JWT** in the Authorizer
