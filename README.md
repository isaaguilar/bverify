# bverify

**bverify** is a minimal command-line utility for verifying bcrypt hashes. It accepts a bcrypt hash and a plaintext password, and returns whether they match.

## Features

- Verifies bcrypt hashes from the command line
- Fast and lightweight
- Installable via `uv` or `pip`

## Installation

### Option 1: Local install with `uv`

1. Clone the repository:

   bash

   ```
   git clone https://github.com/YOUR_USERNAME/bverify.git
   cd bverify
   ```

2. Create and activate a virtual environment:

   bash

   ```
   uv venv
   source .venv/bin/activate
   ```

3. Install the CLI tool:

   bash

   ```
   uv pip install .
   ```

4. Run the tool:

   bash

   ```
   bverify '$2b$12$...' 'yourPassword'
   ```

### Option 2: Make it globally available

If you want to use `bverify` outside the virtual environment:

bash

```
cp .venv/bin/bverify /usr/local/bin/
```

Or use a symlink:

bash

```
ln -s "$(pwd)/.venv/bin/bverify" /usr/local/bin/bverify
```

## Usage

bash

```
bverify <bcrypt_hash> <plaintext_password>
```

Example:

bash

```
bverify '$2b$12$eW5k7W9vYzZzY2xvZy5jb20uLi5uY2FzZQ9zZ2VjcmV0' 'mySecretPassword'
```

Output:

- `✅ Password matches`
- `❌ Password does not match`

## Development

### Project layout

Code

```
bverify/
├── bverify.py
├── pyproject.toml
├── README.md
```

### `pyproject.toml`

toml

```
[project]
name = "bverify"
version = "0.1.0"
description = "CLI tool to verify bcrypt hashes"
readme = "README.md"
requires-python = ">=3.7"
dependencies = ["bcrypt>=5.0.0"]
authors = [{ name = "Isa Aguilar" }]

[project.scripts]
bverify = "bverify:main"
```

## License

MIT License. See `LICENSE` file for details.