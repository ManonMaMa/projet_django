FROM python:3

RUN pip install django mysqlclient django_bootstrap5 django-debug-toolbar django-extensions ipython

COPY entrypoint /entrypoint

ENTRYPOINT ["/bin/bash", "/entrypoint"]