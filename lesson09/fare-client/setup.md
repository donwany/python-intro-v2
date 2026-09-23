
### Setup env
```bash
uv init --package fare-client  --python=3.12
uv venv
source .venv/bin/activate

uv add requests

```
### build and publish
```bash
# build the application
uv build

# install 
uv sync
uv pip install -e .

# friends can install the wheel file
uv pip install dist/fare_client-0.1.0-py3-none-any.whl


uv pip install twine

export TWINE_USERNAME="__token__"
export TWINE_PASSWORD="YOUR_PYPI_API_TOKEN"

twine upload dist/*

```