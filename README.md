### Install 
```bash
uv init --name sendwave --python 3.13
uv init --name sendwave --python 3.13 --description "sendwave app" --package

uv venv

source .venv/bin/active # macOs

.\.venv\Scripts\activate # windows
.\.venv\Scripts\Activate.ps1


touch .env .gitignore Dockerfile Makefile LICENCE main.py

make install
make install && make greet
```