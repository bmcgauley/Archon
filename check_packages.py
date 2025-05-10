import importlib
import sys

# List of required packages
required_packages = [
    "mcp",
    "fastapi",
    "uvicorn",
    "python-dotenv",
    "requests"
]

# Check if packages are installed
print(f"Python version: {sys.version}")
print("\nChecking required packages:")

for package in required_packages:
    package_name = package.replace("-", "_")
    try:
        module = importlib.import_module(package_name)
        version = getattr(module, "__version__", "unknown")
        print(f"✓ {package} is installed (version: {version})")
    except ImportError:
        print(f"✗ {package} is not installed")

print("\nCheck complete!")
