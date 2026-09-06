# Flask Practice Path

Complete these in order. Each task builds on the demos without providing a copy-paste final answer.

## Beginner

1. Add `/contact` to `main.py` and render a new template.
2. Add `/hello/<name>` and display the name through Jinja, not an HTML f-string.
3. Read `?color=blue` with `request.args` and show a default when missing.
4. Add a navigation link using `url_for()`.
5. Create a custom 404 template and test it with the test client.

## Intermediate

6. Add modulo and exponent operations to the calculator.
7. Preserve submitted form values when validation fails.
8. Add `PATCH /items/<id>` to the JSON API.
9. Add filtering and pagination query parameters to `GET /items`.
10. Add a completion filter to the SQLite task project.
11. Add flash messages after create/update/delete.
12. Add a JSON 405 error handler for API routes.

## Practical

13. Move the CRUD routes into a Blueprint.
14. Add a `users` table and connect tasks to an owner using a foreign key.
15. Require login for create/edit/delete and verify ownership.
16. Add CSRF protection to every state-changing browser form.
17. Write test-client tests for valid input, invalid input, missing records, and authentication.
18. Add environment-specific configuration classes.
19. Add request logging with method, path, status, and duration—without sensitive data.
20. Deploy the Blueprint demo with a production WSGI server and verify a health endpoint.

## Review questions

- Why should a successful POST often redirect?
- Why is client-side validation insufficient?
- What is the difference between authentication and authorization?
- Why does global in-memory data break with multiple production workers?
- When should an API return 400, 404, 409, or 415?
- What jobs belong in a route, service function, template, and database layer?

