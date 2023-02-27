# Maintainer's build notes

```
git clean -fdx --dry-run
tox
git commit 
bumpver update --patch
poetry publish --build --username $PYPI_USERNAME --password $PYPI_PASSWORD
```

gpg sign soon!

## test:
```
pip uninstall -y bfasta 
python -m pip cache purge

pip install bfasta 

pip install --force-reinstall dist/*.whl
```
