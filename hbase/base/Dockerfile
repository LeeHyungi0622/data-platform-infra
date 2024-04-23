FROM openjdk:8
RUN apt-get update && DEBIAN_FRONTEND=noninteractive apt-get install -y --no-install-recommends net-tools curl netcat

ENV HBASE_VERSION 2.0.0

# Updated endpoint as it changes for 2.0.0 version
# See http://www.apache.org/dist/hbase/
ENV HBASE_URL https://archive.apache.org/dist/hbase/$HBASE_VERSION/hbase-$HBASE_VERSION-bin.tar.gz
RUN set -x \
    && apt-get install wget \
    && curl -fSL "$HBASE_URL" -o /tmp/hbase.tar.gz \
    && curl -fSL "$HBASE_URL.asc" -o /tmp/hbase.tar.gz.asc \
    && tar -xvf /tmp/hbase.tar.gz -C /opt/ \
    && rm /tmp/hbase.tar.gz*

RUN ln -s /opt/hbase-$HBASE_VERSION/conf /etc/hbase
RUN mkdir /opt/hbase-$HBASE_VERSION/logs

RUN mkdir /hadoop-data

ENV HBASE_PREFIX=/opt/hbase-$HBASE_VERSION
ENV HBASE_CONF_DIR=/etc/hbase

ENV PHOENIX_VERSION=5.0.0

ENV PHOENIX_SERVER=phoenix-server-hbase-$HBASE_VERSION-$PHOENIX_VERSION.jar

ENV MIRROR_URL        "https://archive.apache.org/dist"
ENV PHOENIX_HOME      /usr/local/phoenix-${PHOENIX_VERSION}

RUN mirror_url=$MIRROR_URL \
    && package_name="apache-phoenix-${PHOENIX_VERSION}-HBase-2.0" \
    && wget -q -O - ${mirror_url}/phoenix/${package_name}/bin/apache-phoenix-${PHOENIX_VERSION}-HBase-2.0-bin.tar.gz \
        | tar -xzf - -C /usr/local \
    && mv /usr/local/apache-phoenix-${PHOENIX_VERSION}-HBase-2.0-bin ${PHOENIX_HOME} \
    && cd ${PHOENIX_HOME} \
    && mv *server*.jar $HBASE_PREFIX/lib

ENV USER=root
ENV PATH $HBASE_PREFIX/bin/:$PATH

ADD entrypoint.sh /entrypoint.sh
RUN chmod a+x /entrypoint.sh

ENTRYPOINT ["/entrypoint.sh"]
