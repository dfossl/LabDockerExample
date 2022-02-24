FROM python:3.7
ENV PYTHONUNBUFFERED 1

LABEL   maintainer="Dylan Fossl <dylan.t.fossl@gmail.com>" \
        description="Example of setting up jupyter data science environment"

WORKDIR /code

COPY requirements.txt /code/

RUN pip install -r requirements.txt

# Setup SSH with secure root login
RUN apt-get update \
 && apt-get install -y openssh-server netcat \
 && mkdir /var/run/sshd \
 && echo 'root:password' | chpasswd \
 && sed -i 's/\#PermitRootLogin prohibit-password/PermitRootLogin yes/' /etc/ssh/sshd_config

EXPOSE 22
CMD ["/usr/sbin/sshd", "-D"]