"""Local structural/syntax preflight for brozen AI; no secrets or network needed."""
import ast
import pathlib
import tomllib

root = pathlib.Path(__file__).resolve().parent
required = ["bot.py", "requirements.txt", "Procfile", "railway.toml", ".python-version", "README.md"]
missing = [name for name in required if not (root / name).is_file()]
if missing:
    raise SystemExit(f"FAIL missing root files: {missing}")
ast.parse((root / "bot.py").read_text(encoding="utf-8"))
config = tomllib.loads((root / "railway.toml").read_text(encoding="utf-8"))
assert config["build"]["builder"] == "RAILPACK"
assert config["deploy"]["startCommand"] == "python bot.py"
reqs = (root / "requirements.txt").read_text(encoding="utf-8")
for package in ("python-telegram-bot", "openai", "aiohttp", "python-dotenv"):
    assert package in reqs, f"Missing dependency: {package}"
print("PASS: required root files exist")
print("PASS: bot.py parses as valid Python syntax")
print("PASS: railway.toml parses and start command is configured")
print("PASS: required runtime dependencies are listed")
