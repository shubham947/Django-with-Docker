# Template repo for Django with Docker and Postgres

This repo contains ready to use setup for Django with the following:
- Django
- `djangorestframework`
- Postgres db image in docker using `psycopg2`
- GitHub Actions: Lint and Test
- API Documentation using `drf-spetacular`

For using GitHub Actions, you need to set the following in github secrets:
- DOCKERHUB_USER
- DOCKERHUB_TOKEN

### Docker commands
- To build the image: `docker-compose build`
- To start the container: `docker-compose up`
- To stop the container: `docker-compose down`, you can also use `--volumes` flag with this command to remove the volumes created with the container.
- To run a command inside the container: `docker-compose run --rm app sh -c "<Your command>"`

### Additional Features
- **Email and phone auth backend added:** User can signup/login using both email and phone.
- **Added custom password validator:** Password should contain at least one character form each of the following: digit, Uppercase, lowercase characters, symbol, and should be of at least 6 characters.
- Phone number is handled using `django-phonenumber-field` package.
