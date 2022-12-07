# Some kind of web application

A web application as part of Chulalongkorn University Introduction to Information System course.

## Getting Started

The following instructions will help you get the project up and running on
your local machine for development and testing purposes. For publishing sites to webhosts, see Deployment.

### Prerequisites

- Visual Studio Code. [Visual Studio Code](https://code.visualstudio.com/)
- Git [Installing Git](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git)
- Python >=3.10 [Python 3.10.9](https://www.python.org/downloads/release/python-3109/)
- Pip >=22.2.1

### Installing

Clone the remote repository onto your machine.

    git clone https://github.com/Slyt4il/project-webapp.git

Navigate to the project folder with Visual Studio Code terminal or your machine's command prompt.

If venv is not already present, create a virtual environment.

    python -m venv .venv

If venv is present, activate it.

    .venv\Scripts\activate

Requirements should be automatically installed. If not,

Install Django

    pip install Django==4.1.4
  
Install NodeJS

    pip install nodejs==0.1.1

Start the web application.

    ./manage.py runserver

Head over to your localhost on port 8000 (http://localhost:8000/) (http://127.0.0.1:8000/)

## Deployment

**Heroku**

We'll look for a new home for the project as Heroku ends its free tier service.

## Contributing

For contribution guidelines, see TODO.

## Authors

  - **Group 88**
  
  [Contributors](https://github.com/Slyt4il/project-webapp/contributors) who participated in this project.

## License

This project is licensed under the [MIT](LICENSE.md) license.