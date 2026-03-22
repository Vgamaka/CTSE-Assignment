# Event Service

Owner: Peiris P G V  
Student ID: IT22364388

## Responsibility
This microservice manages event CRUD operations and admin event control for the Cloud-Based Event Management System.

## Features
- Create event (Admin only)
- View all events
- View single event
- Update event (Admin only)
- Delete event (Admin only)
- Health check endpoint

## Endpoints
- GET /health
- POST /events
- GET /events
- GET /events/{event_id}
- PUT /events/{event_id}
- DELETE /events/{event_id}

## Environment Variables
See `.env.example`

## Notes
- Admin-only endpoints require a valid JWT with role = admin.
- Public users can view events without authentication.
