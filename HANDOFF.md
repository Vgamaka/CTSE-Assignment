# Event Service Handoff Notes

Owner: Peiris P G V
Student ID: IT22364388

## Ready-to-move files
- app/
- Dockerfile
- requirements.txt
- .env.example
- .gitignore
- README.md
- .github/workflows/ci.yml

## Current service responsibilities
- Create event (Admin only)
- View all events
- View single event
- Update event (Admin only)
- Delete event (Admin only)
- Health check

## Required environment variables
- DATABASE_URL
- JWT_SECRET
- JWT_ALGORITHM

## Before pushing to personal repo
1. Copy all Event Service files into the new repository root.
2. Ensure `.github/workflows/ci.yml` stays under the repo root.
3. Update SonarCloud project key if needed.
4. Configure GitHub Secrets:
   - SONAR_TOKEN
   - ACR_LOGIN_SERVER
   - ACR_USERNAME
   - ACR_PASSWORD
5. Add deployment URL and Swagger URL to README after deployment.

## Integration note
Registration Service depends on Event Service for event existence validation.

## Recommended post-migration checks
- Swagger docs load
- GET /health works
- GET /events works
- Admin create/update/delete works with JWT
