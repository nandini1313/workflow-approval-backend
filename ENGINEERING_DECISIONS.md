# Engineering Decisions

## Architecture

The application follows a layered architecture:

Frontend (React)
↓
API Layer (FastAPI Routes)
↓
Service Layer
↓
Repository Layer
↓
PostgreSQL Database

This structure was chosen to maintain separation of concerns and improve maintainability.

---

## Frontend Decisions

### React

React was selected because it provides:

- Component-based architecture
- Efficient state management
- Easy routing using React Router
- Strong community support

### Axios

Axios was used for API communication because it simplifies:

- HTTP requests
- Authorization headers
- Error handling

### React Router

React Router was used to manage:

- Login page
- Dashboard page
- Reviewer dashboard
- Admin dashboard
- Request history page

---

## Backend Decisions

### FastAPI

FastAPI was chosen because:

- High performance
- Automatic Swagger documentation
- Strong typing support
- Easy JWT integration

### SQLAlchemy

SQLAlchemy was selected as the ORM because:

- Database abstraction
- Relationship management
- Query optimization
- Maintainability

### Pydantic

Pydantic was used for:

- Request validation
- Response validation
- Type safety

---

## Authentication

### Google OAuth

Google OAuth was implemented to:

- Avoid password storage
- Improve security
- Provide simple user onboarding

### JWT Authentication

JWT tokens were selected because:

- Stateless authentication
- Easy frontend integration
- Scalable architecture

---

## Database Design

### Users

Stores:

- User information
- Email
- Role

### Approval Requests

Stores:

- Request details
- Status
- Request creator
- Assigned reviewer

### Review Actions

Stores:

- Approval actions
- Rejection actions
- Comments
- Review timestamps

This design enables complete audit tracking.

---

## Design Trade-Offs

### Reviewer Assignment

Current implementation uses Reviewer ID.

Pros:

- Simple implementation
- Easy testing

Cons:

- Not user friendly

Future improvement:

- Reviewer dropdown selection

---

### Role Based Routing

Current implementation supports separate dashboards.

Future improvement:

- Automatic role-based redirection after login

---

## Future Enhancements

### Functional

- Email notifications
- Advanced filtering
- Search functionality
- Dashboard analytics
- Reviewer selection dropdown

### Technical

- Docker deployment
- CI/CD pipeline
- Redis caching
- WebSocket notifications

---

## Conclusion

The chosen architecture prioritizes maintainability, scalability, and clear separation of responsibilities while keeping implementation complexity manageable for the assessment.