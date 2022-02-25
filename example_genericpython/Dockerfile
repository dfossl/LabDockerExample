FROM python:3.7
ENV PYTHONUNBUFFERED 1

LABEL   maintainer="Dylan Fossl <dylan.t.fossl@gmail.com>" \
        description="Example of setting up jupyter data science environment"

WORKDIR /code

COPY requirements.txt /code/

RUN pip install -r requirements.txt

CMD ["/bin/bash"]



