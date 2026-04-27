# RAG_mlops25

## Notes on overall structure

- want one .venv for the whole project
- one pyproject.toml for whole project
- one pyproject.toml for backend
- one pyproject.toml for frontend


Reason for this:
- we will dockorize into 2 services (backend, frontend)
- inside each service/container want to do 'uv sync'
- some packages are only used in one service and not the other 