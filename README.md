<!--
https://readme42.com
-->


[![](https://img.shields.io/pypi/v/django-postgres-matviews.svg?maxAge=3600)](https://pypi.org/project/django-postgres-matviews/)
[![](https://img.shields.io/badge/License-Unlicense-blue.svg?longCache=True)](https://unlicense.org/)
[![](https://github.com/andrewp-as-is/django-postgres-matviews.py/workflows/tests42/badge.svg)](https://github.com/andrewp-as-is/django-postgres-matviews.py/actions)

### Installation
```bash
$ [sudo] pip install django-postgres-matviews
```

##### `settings.py`
```python
INSTALLED_APPS+=['django_postgres_matviews']
```

#### Examples
```bash
$ python manage.py refresh_matviews
$ python manage.py drop_matviews
```

```bash
$ python manage.py refresh_matview "matview1" "matview2"
$ python manage.py drop_matviews "matview1" "matview2"
```

```python
from django_postgres_matviews.utils import drop_matview, drop_matviews, get_matviews, refresh_matview, refresh_matviews

refresh_matviews()
drop_matviews()

refresh_matview('matview1')
drop_matview('matview1')

for m in get_matviews():
    m.schemaname,m.matviewname
```

<p align="center">
    <a href="https://readme42.com/">readme42.com</a>
</p>
