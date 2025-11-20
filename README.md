# PyMcp
A sample  MCP Server using the Python FastMCP library.



## Repository Structure

```
McpDocs/
├── src/                          # Source code
│   └── sample_mcp_server/       # Sample MCP server
│       ├── server.py            # Main server implementation
│       ├── Dockerfile           # Docker configuration
│       ├── tests/               # Unit tests
│       └── README.md            # Server documentation
├── .github/                     # GitHub workflows
│   └── workflows/
│       └── ci.yml               # CI/CD pipeline
├── pyproject.toml               # Project configuration
└── README.md                    # This file
```



## Using UV

The `uv` package manager is a powerful alternative to `pip`. I strongly suggest it to better manage the dependencies and virtual environments.

### Installation

https://docs.astral.sh/uv/getting-started/installation/

```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```

This may require to log off and back on.

Updating:

```bash
uv self update
```

### Package management

Install a package:

```bash
uv pip install ruff
```

Alternatively, you can edit the `pyproject.toml` file, add the dependencies in the appropriate section and then install them using:

```bash
uv sync
```

The `sync` command is also useful when cloning the project elsewhere (after creating the virtual  environment on the new machine).



### Virtual Environment

Creating the default Virtual Environment (`.venv` subdirectory):

```bash
uv venv
```

Creating a Virtual Environment with a different name:

```bash
uv venv some_name
```

Activate the Virtual Environment on Linux:

```bash
source .venv/bin/activate
```

Activate the Virtual Environment on Windows:

```cmd
.venv\Scripts\activate
```

To deactivate the environment:

```bash
deactivate
```

Activating the environment from **Visual Studio Code**:

* Ensure the virtual environment exists
* Open the folder with the Python Project
* Press F1
* Type  `Python: Select Interpreter`
* Pick the entry mentioning the project name. The path should be something like `.venv/bin/python`

Docker image with pre-installed `uv`: https://github.com/astral-sh/uv/pkgs/container/uv

## Ruff Syntax checker

In addition to the  standard Python Visual studio Code extensions, I strongly suggest to install Ruff because it processes the source code extremely fast.

Anyway, there may be some collision between the two. I adjusted the `.vscode/settings.json` to minimize these problems.

Manual check the rules with `ruff`:

```bash
ruff check src/
```

Auto-fix  the issues with ruff:

```bash
ruff check src/ --fix
```

Manual check the rules  with `mypy`:

```bash
mypy src/
```

## Running the project

### Running the Sample Server

```bash
# from the project root folder
python -m src.sample_mcp_server.server
```

### Running Tests

```bash
# from the project root folder
pytest src/sample_mcp_server/tests/ -v
```

### Building with Docker

```bash
# from the project root folder
docker build -f src/sample_mcp_server/Dockerfile -t sample-mcp-server .
docker run -i sample-mcp-server
```













