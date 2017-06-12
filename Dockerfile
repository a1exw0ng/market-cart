FROM ubuntu:16.04
MAINTAINER Josh Granberry <jdgranberry@gmail.com>

RUN apt-get update -y && \
    apt-get install -y python-pip python-dev build-essential

COPY . /market-cart/

WORKDIR /market-cart

RUN pip install --upgrade pip
RUN pip install -r /market-cart/requirements.txt
ENV PYTHONPATH $PYTHONPATH:/market-cart/

EXPOSE 5000

ENTRYPOINT ["python"]
CMD ["./market-cart/app.py"]
