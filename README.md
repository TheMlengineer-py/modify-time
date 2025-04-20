# Time Parser
Parses time expressions like `now()+1d+3h` and returns a UTC datetime.

## Features
- user friendly ui for testing
- Supports relative time modifiers: seconds, minutes, hours, days, months, years.
- Accurate UTC handling.
- Fully tested with pytest.
- Clean and consistent codebase with pre-commit linting.
- Github actions for ci
- workflow automation script

## run commands via 'bash'

## to lunch web app in local and copy corresponding url to browser ##
-  cd src
-  python web.py
## to test the parser application in local##
- cd src
- python app.py
## to run test on the parser function in local machine ## 
- cd src
- pytest -s test_time_parser.py
## to automate workflow in local machine ## 
- cd modify-time
- ./run_all.sh 



