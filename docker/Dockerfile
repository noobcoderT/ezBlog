FROM alpine:latest
ADD ./requirements.txt /root/requirements.txt
RUN apk add py-pip
RUN pip install -r /root/requirements.txt
VOLUME /root/ezBlog
EXPOSE 8888
ENTRYPOINT python /root/ezBlog/ezBlog.py > /root/ezBlog/run.log 2>&1
