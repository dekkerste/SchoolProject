# SchoolProject

Instructies:
We hebben flask nodig om de python met een webserver te verbinden:
https://flask.palletsprojects.com/en/2.2.x/installation/

```$ cd SchoolProject```

Use a virtual environment to manage the dependencies for your project, both in
development and in production.
What problem does a virtual environment solve? The more Python projects you
have, the more likely it is that you need to work with different versions of
Python libraries, or even Python itself. Newer versions of libraries for one
project can break compatibility in another project.
Virtual environments are independent groups of Python libraries, one for each
project. Packages installed for one project will not affect other projects or
the operating system’s packages.
Python comes bundled with the venv module to create virtual
environments.


```$ python3 -m venv venv```

Activate the environment

```$ . venv/bin/activate```

```$ pip install Flask```

start de webserver:

```$ flask --app main run```

Let er dan op dat alle andere libaries zoals imageai en djitellopy ook geinstaleerd moeten worden in de virtual enviroment (. venv/bin/activate en dan pip install)
