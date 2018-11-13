test:
	python2.7 -m pytest tests
	python3.7 -m pytest tests

pkgtest:
	python2.7 setup.py sdist bdist_wheel
	python2.7 -m twine check dist/*
	python3.7 -m twine check dist/*
