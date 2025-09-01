# VS Code Snippets for Python Development

This directory can contain custom code snippets for your Python development.

## Adding Custom Snippets

1. Create a `.json` file in this directory (e.g., `python.json`)
2. Add your snippets following VS Code snippet syntax

Example snippet for a Python function:

```json
{
    "Python Function": {
        "prefix": "pyfunc",
        "body": ["def ${1:function_name}(${2:args}) -> ${3:return_type}:", "    \"\"\"${4:Description}.", "    ", "    Args:", "        ${2:args}: ${5:Description}", "    ", "    Returns:", "        ${3:return_type}: ${6:Description}", "    \"\"\"", "    ${0:pass}"],
        "description": "Create a Python function with docstring"
    }
}
```
