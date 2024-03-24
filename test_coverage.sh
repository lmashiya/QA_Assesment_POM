coverage erase
coverage run --source=./QA_Assesment_POM -m unittest discover ./tests
coverage report -m
coverage html
open ./htmlcov/index.html