# 💊 Prescription Management System (Serverless on AWS)

A secure, scalable prescription and medication tracking system built using **AWS Lambda**, **API Gateway**, **Python**, and **PostgreSQL**. Designed for clinics or pharmacies, this backend API manages patients, prescriptions, and items with strict role-based access control via API Gateway and a custom Lambda authorizer.

## 🧰 Tech Stack

- **Runtime**: Python (AWS Lambda)
- **API Layer**: API Gateway + Lambda Integrations
- **Authorization**: Custom Lambda Authorizer (email + password)
- **Access Control**:
  - 🔐 **Admin**: Full access to prescriptions and items (GET, POST, PUT)
  - 👤 **User**: Read-only access (GET only)
- **Database**: PostgreSQL (via SQLAlchemy ORM)
- **Infrastructure as Code**: Terraform

## 🏗️ Features

- 🧑‍⚕️ View, create, and update **prescriptions**
- 💊 Manage **prescription items** linked to each prescription
- 🔐 Role-based access control (admin vs normal user)
- 🔄 API Gateway authorizer returns dynamic IAM policies
- 📦 Modular backend architecture with clear separation of concerns

## 🔐 Access Control Summary

| Role         | Permissions                                      |
|--------------|--------------------------------------------------|
| **Admin**    | View, create, and update prescriptions & items   |
| **User**     | View prescriptions & items only (read-only)      |

- Access is enforced by **API Gateway** using IAM policies returned by a **Lambda authorizer**
- Auth is handled with **email and password** in the Authorizer
