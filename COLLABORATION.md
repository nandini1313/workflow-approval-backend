# Collaboration Report

## Team Information

This project was completed individually as part of the Workflow Approval System assessment.

Author:
- Nandini Bandari

---

## Development Approach

The project was developed incrementally using the following phases:

### Phase 1 – Project Setup

- Setup FastAPI backend
- Setup React frontend using Vite
- Configure PostgreSQL database
- Configure project structure

---

### Phase 2 – Authentication

Implemented:

- Google OAuth Login
- JWT Authentication
- User session management

---

### Phase 3 – Request Management

Implemented:

- Create Request
- View Requests
- Update Request
- Delete Request
- Request Details

---

### Phase 4 – Reviewer Workflow

Implemented:

- Reviewer Dashboard
- Approve Requests
- Reject Requests
- Review Comments
- Request History

---

### Phase 5 – Dashboard & Admin Features

Implemented:

- Dashboard Statistics
- Admin Dashboard
- User Management
- Request Tracking

---

## Challenges Faced

### Google OAuth Integration

Challenge:
- Managing OAuth callback flow and token handling.

Solution:
- Implemented FastAPI OAuth callback endpoint and JWT generation.

---

### Role-Based Access

Challenge:
- Managing permissions for Admin, Reviewer, and Requester.

Solution:
- Created dependency-based authorization checks and role validation.

---

### Request History Tracking

Challenge:
- Maintaining an audit trail for approval actions.

Solution:
- Introduced ReviewAction entity to store approval/rejection history and reviewer comments.

---

## Lessons Learned

- FastAPI dependency injection
- JWT authentication workflows
- Repository-Service architecture
- React state management
- API integration using Axios
- Role-based authorization patterns

---

## Future Improvements

- Automatic role-based redirection
- Email notifications
- Search and filtering
- Reviewer dropdown assignment
- Advanced dashboard analytics

---

## Summary

The Workflow Approval System successfully implements an end-to-end approval workflow using modern full-stack technologies. The project demonstrates authentication, authorization, CRUD operations, workflow management, and audit tracking.