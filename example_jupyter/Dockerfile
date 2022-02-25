FROM python:3.7
ENV PYTHONUNBUFFERED 1

LABEL   maintainer="Dylan Fossl <dylan.t.fossl@gmail.com>" \
        description="Example of setting up jupyter data science environment"

WORKDIR /code

COPY . /code

RUN pip install -r requirements.txt

EXPOSE 8889

CMD ["jupyter", "notebook", "--ip=0.0.0.0", "--no-browser", "--allow-root", "--port", "8889"]

