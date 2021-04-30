FROM python:3

# Tells pipenv to create virtualenvs in /root rather than $HOME/.local/share.
# We do this because GitHub modifies the HOME variable between `docker build` and
# `docker run`
ENV WORKON_HOME /root

# Tells pipenv to use this specific Pipfile rather than the Pipfile in the 
# current working directory (the working directory changes between `docker build` 
# and `docker run`, this ensures we always use the same Pipfile)
ENV PIPENV_PIPFILE /Pipfile

# Install chrome
RUN apt-get install chrome

COPY rockband.py /
COPY Pipfile /
COPY Pipfile.lock /
COPY config.yaml /

# https://github.com/pypa/pipenv/issues/4273
RUN pip install 'pipenv==2018.11.26'
RUN pipenv install --deploy --ignore-pipfile

ENTRYPOINT ["pipenv", "run", "python", "./rockband.py"