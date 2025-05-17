FROM cgr.dev/chainguard/python:latest-dev

USER root

RUN <<EOT

    apk update && apk add posix-libc-utils && ldconfig

    mkdir /server
    chown -R nonroot:nonroot /server

EOT

USER nonroot

COPY --chown=nonroot *.py /server/
COPY --chown=nonroot requirements.txt /server/

RUN <<EOT

    pip install --upgrade pip
    pip install --no-cache-dir -r /server/requirements.txt

EOT

RUN ls -al /server

ENTRYPOINT ["python","/server/weather_server.py"]
