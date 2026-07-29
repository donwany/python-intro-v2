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

### File Modes
```
'r'	open for reading (default)
'w'	open for writing, truncating the file first
'x'	create a new file and open it for writing
'a'	open for writing, appending to the end of the file if it exists
'b'	binary mode
't'	text mode (default)
'+'	open a disk file for updating (reading and writing)
```

### HomeWork
```
Scenario

A company receives customer support requests. Each request belongs to one of the following departments:

Technical Support
Sales
Billing
Human Resources (HR)
Customer Success

Your program should determine which department should handle the request.
```