cd /d "%~dp0"
python setup.py bdist_wheel
pip install --no-index .\dist\wrapped_json-1.0.0-py3-none-any.whl --force-reinstall