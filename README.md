# SchoolProject

Introductie:
Dit project was gemaakt voor de marine, de marine vroeg aan ons of wij via een website een drone konden besturen, en zien wat de drone ziet en wat allemaal wel niet mogelijk is met een drone.
De drone is alleen te besturen met de app van deze drone, of via Python, dus hebben wij een website gemaakt met combinatie van HTML en Python.

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

```$ pip install -r requirements.txt```

start de webserver:

```$ flask --app main run```

Zet de websever op DEBUG:

```$ set FLASK_ENV=development ```

```$ set FLASK_DEBUG=1```

op linux moet je set met export vervangen:

```$ export FLASK_ENV=development ```


```$ export FLASK_DEBUG=1```


Let er dan op dat alle andere libaries zoals imageai en djitellopy ook geinstaleerd moeten worden in de virtual enviroment (. venv/bin/activate en dan pip install)
