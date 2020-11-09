clean:
    rm -rf venv
    find . -type f -name ‘*.pyc’ -delete

clean-build:
    rm --force --recursive build/
    rm --force --recursive dist/
    rm --force --recursive *.egg-info

clean-pyc:
    find . -name '*.pyc' -exec rm --force {} +
    find . -name '*.pyo' -exec rm --force {} +
    name '*~' -exec rm --force  {}

help:
    @echo "~~~~~~Skribbl.io Auto Draw~~~~~~"
    # Explanations

install:
    @echo "Installing dependencies..."
    python3 -m pip install -r requirements.txt

lint:
    flake8 --exclude=.tox

.PHONY: clean clean-build clean-pyc help install lint