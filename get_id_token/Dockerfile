FROM python:alpine

COPY . /get_id_token/

RUN apk add --no-cache gcc g++ make libffi-dev openssl-dev
RUN pip install -r /get_id_token/requirements.txt

ENTRYPOINT ["/get_id_token/get_id_token.py"]
