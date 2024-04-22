FROM smizy/hbase:1.3-alpine

ARG BUILD_DATE="2024-04-21"
ARG VERSION="5.2.0"

LABEL \
    maintainer="milnomada" \
    org.label-schema.build-date=$BUILD_DATE \
    org.label-schema.docker.dockerfile="/Dockerfile" \
    org.label-schema.license="Apache License 2.0" \
    org.label-schema.name="milnomada/hbase-phoenix" \
    org.label-schema.url="https://github.com/milnomada" \
    org.label-schema.vcs-type="Git" \
    org.label-schema.vcs-url="https://github.com/milnomada/docker-hbase-phoenix"

ENV PHOENIX_VERSION   5.2.0
# Updated
ENV HBASE_VER         2.5.0

ENV PHOENIX_HOME      /usr/local/phoenix-${PHOENIX_VERSION}
ENV MIRROR_URL        "https://archive.apache.org/dist"

ENV PATH $PATH:${PHOENIX_HOME}/bin

RUN set -x \
    && apk update \
    && apk --no-cache add \
        bash \
        su-exec \
        python \
        wget \
    && mirror_url=$MIRROR_URL \
    && package_name="phoenix-${PHOENIX_VERSION}" \
    && wget -q -O - ${mirror_url}/phoenix/${package_name}/phoenix-hbase-2.5.0-$PHOENIX_VERSION-bin.tar.gz \
        | tar -xzf - -C /usr/local \
    && mv /usr/local/phoenix-hbase-2.5.0-$PHOENIX_VERSION-bin ${PHOENIX_HOME} \
    && cd ${PHOENIX_HOME} \
    && mkdir -p server \
    && mv *-server-*.jar server/
    ## cleanup    
    ## && rm *-tests.jar *-sources.jar 

## Add user-specified CLASSPATH
ENV HBASE_CLASSPATH ${PHOENIX_HOME}/server/*

WORKDIR ${PHOENIX_HOME}
