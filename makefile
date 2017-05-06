
test:
	py.test-3 tests

watcher:
	find . -name *.py | entr py.test-3 tests
