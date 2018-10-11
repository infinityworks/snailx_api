[![CircleCI](https://circleci.com/gh/infinityworks/snailx_api/tree/develop.svg?style=svg)](https://circleci.com/gh/infinityworks/snailx_api/tree/develop)

# SnailX API

External team API for the SnailX project. (The best team.)

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. See deployment for notes on how to deploy the project on a live system.

### Setting up Dev Environment

- Run ```make build```
- Run ```make up```
- Navigate to ```0.0.0.0:5000```

### Tearing Down the Dev Environment

- Run ```make destroy-all```

## Running the Tests

- Run ```make test```
- Run ```make test-coverage``` to generate html report of test coverage.

JUnit style XML reports for testing are generated/uploaded to CircleCI when the tests are executed by `make test`.

## Deployment

CircleCI + Heroku
UAT: <https://dev-snailx-api.herokuapp.com/>

## Built With

* flask
* flask_api
* flask-sqlalchemy
* flask-migrate
* pyjwt
* coverage
* unittest-xml-reporting
* gunicorn

## Versioning

We use [SemVer](http://semver.org/) for versioning. For the versions available, see the [tags on this repository](https://github.com/your/project/tags). 

## Authors

* **Junaid Zafar** - [junaid-iw](https://github.com/junaid-iw)
* **Malik Glossop** - [glossopm](https://github.com/glossopm)
* **Matthew Sorsby** - [Sorsby](https://github.com/Sorsby)
* **Mike Silverstone** - [MikeSilverstone](https://github.com/MikeSilverstone)
* **Sandeep Sharda** - [infinitydeep](https://github.com/infinitydeep)

See also the list of [contributors](https://github.com/Sorsby/snailx_api/graphs/contributors) who participated in this project.

## License

This project is licensed under the GNU General Public License v3.0 - see the [LICENSE.md](LICENSE.md) file for details

