# Template repo for Django with Docker and Postgres

This repo contains ready to use setup for Django with the following:
- Django
- Postgres db image in docker
- GitHub Actions: Lint and Test

For using GitHub Actions, you need to set the following in github secrets:
- DOCKERHUB_USER
- DOCKERHUB_TOKEN

### Docker commands
- To build the image: `docker-compose build`
- To start the container:`docker-compose up`
- To stop the container:`docker-compose down`, you can also use `--volumes` flag with this command to remove the volumes created with the container.
- To run a command inside the container:`docker-compose run --rm app sh -c "<Your command>"`
