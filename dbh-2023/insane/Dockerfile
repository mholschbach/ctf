FROM alpine:latest

RUN apk add gcc libc-dev python3 py3-pip sudo

RUN mkdir -p /ctf/app
RUN mkdir /ctf/app/compiles
RUN mkdir /ctf/secureenv
RUN addgroup -S ctf && adduser --disabled-password --home /ctf --no-create-home ctf -G ctf

COPY --chown=ctf flag.txt /ctf/app/flag.txt
COPY --chown=ctf requirements.txt /ctf/app/requirements.txt
RUN pip3 install -r /ctf/app/requirements.txt

RUN chown -R ctf:ctf /ctf && \
	chmod -R 600 /ctf && \
	chmod a+x /ctf && \
	chmod u+x /ctf/app && \
	chmod u+x /ctf/app/compiles && \
	chmod a+xw /ctf/secureenv # ctf can write binary there


RUN echo "ctf ALL=(nobody) NOPASSWD: /ctf/secureenv/prog" >> /etc/sudoers

COPY --chown=ctf app.py /ctf/app/app.py
WORKDIR /ctf/app
USER ctf

EXPOSE 5000

CMD [ "python3", "-m" , "flask", "run", "--debug", "--host=0.0.0.0" ]
