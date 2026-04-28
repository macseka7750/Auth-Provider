# Modular Django Identity & Content API

[![Django CI/CD Pipeline](https://github.com/YOUR_USERNAME/YOUR_REPO_NAME/actions/workflows/django.yml/badge.svg)](https://github.com/YOUR_USERNAME/YOUR_REPO_NAME/actions)
![Python Version](https://img.shields.io/badge/python-3.11-blue)
![Django Version](https://img.shields.io/badge/django-4.2+-green)

A professional-grade, scalable backend architecture built with **Django Rest Framework (DRF)**. This project demonstrates industry-standard practices for **Identity Management**, **Role-Based Access Control (RBAC)**, and **Containerization**.

## 🚀 Key Features

-   **Secure Identity Management**: Implementation of JWT (JSON Web Tokens) using `simplejwt` and OAuth2 support via `dj-rest-auth`.
-   **Modular Architecture**: A clean `apps/` directory structure to separate concerns (Users, Blog, Core).
-   **RBAC (Role-Based Access Control)**: Custom User model supporting roles (Admin, Moderator, User) with enforced permissions.
-   **Interactive API Documentation**: Auto-generated **Swagger UI** and **Redoc** using `drf-spectacular`.
-   **Dockerized Environment**: Fully containerized setup with PostgreSQL and optimized Python slim images.
-   **CI/CD Integration**: Automated testing pipeline via GitHub Actions.

## 🛠️ Tech Stack

-   **Backend**: Python, Django, Django Rest Framework
-   **Database**: PostgreSQL
-   **Auth**: JWT, OAuth2 (Google/GitHub)
-   **DevOps**: Docker, Docker Compose, GitHub Actions
-   **Documentation**: OpenAPI 3.0 (Swagger)

## 📁 Project Structure

```text
├── config/               # Project settings and main URL dispatcher
├── apps/                 # Modular business logic
│   ├── users/            # Custom User model & Identity logic
│   └── blog/             # Content management with RBAC permissions
├── .github/workflows/    # CI/CD Pipeline definitions
├── docker-compose.yml    # Orchestration for App & DB
└── Dockerfile            # Optimized production-ready image
