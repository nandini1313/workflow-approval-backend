# Workflow Approval System

A full-stack Workflow Approval System built using FastAPI, React, PostgreSQL, and Google OAuth.

## Features

### Authentication
- Google OAuth Login
- JWT Authentication
- Role-Based Access Control

### Request Management
- Create Approval Requests
- View Requests
- Update Requests
- Delete Requests
- Request Details
- Request History Tracking

### Reviewer Workflow
- View Assigned Requests
- Approve Requests
- Reject Requests
- Add Review Comments
- Track Approval History

### Dashboard
- User Dashboard
- Reviewer Dashboard
- Admin Dashboard
- Request Statistics

---

## Tech Stack

### Frontend
- React
- React Router
- Axios
- Vite

### Backend
- FastAPI
- SQLAlchemy
- Pydantic
- JWT Authentication

### Database
- PostgreSQL

### Authentication
- Google OAuth 2.0

---

## Project Structure

```text
workflow-approval-system
│
├── backend
│   ├── app
│   │   ├── routes
│   │   ├── services
│   │   ├── repositories
│   │   ├── models
│   │   ├── schemas
│   │   ├── dependencies
│   │   └── core
│
├── frontend
│   ├── src
│   │   ├── pages
│   │   ├── services
│   │   ├── routes
│   │   ├── components
│   │   └── context
│
└── tests
```

## Installation

### Backend

Create virtual environment:

```bash
python -m venv venv
```

Activate virtual environment:

```bash
venv\Scripts\activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Run backend:

```bash
uvicorn app.main:app --reload
```

---

### Frontend

Install dependencies:

```bash
npm install
```

Run frontend:

```bash
npm run dev
```

---

## Environment Variables

### Backend

Create `.env`

```env
DATABASE_URL=postgresql://username:password@localhost/workflow_db

SECRET_KEY=your_secret_key

GOOGLE_CLIENT_ID=your_google_client_id

GOOGLE_CLIENT_SECRET=your_google_client_secret
```

---

## API Endpoints

### Authentication

```http
GET /auth/google/login
GET /auth/callback
GET /auth/me
```

### Requests

```http
POST /requests
GET /requests
GET /requests/my
GET /requests/{id}
PUT /requests/{id}
DELETE /requests/{id}
GET /requests/{id}/history
```

### Reviewer

```http
GET /reviewer/requests
POST /requests/{id}/approve
POST /requests/{id}/reject
```

### Dashboard

```http
GET /dashboard/stats
```

---

## User Roles

### Requester

Can:

- Create Requests
- Update Requests
- Delete Requests
- View Request History

### Reviewer

Can:

- View Assigned Requests
- Approve Requests
- Reject Requests
- Add Review Comments

### Admin

Can:

- View System Statistics
- View Users
- View All Requests

---

## Future Improvements

- Automatic Role-Based Redirect
- Email Notifications
- Request Search & Filtering
- Reviewer Assignment Dropdown
- Audit Logs
- Dark Mode
- Dashboard Analytics Charts

---

## Author

Nandini Bandari

Workflow Approval System Assessment Submission