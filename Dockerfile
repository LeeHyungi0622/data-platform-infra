# Base Image
#
# Date: 2022.04.18
# Author: 이현기(Lee Hyungi)
#

FROM centos:7

#
# CentOS Default Install
#
RUN yum update -y
RUN yum install  -y \
    initscripts \
    vim \
    openssh-server \
    openssh-clients \
    openssh-askpass \
    java-1.8.0-openjdk \
    java-1.8.0-openjdk-devel.x86_64

#
# set ssh
#
RUN ssh-keygen -t rsa -P '' -f ~/.ssh/id_dsa \
    && cat ~/.ssh/id_dsa.pub >> ~/.ssh/authorized_keys \
    && ssh-keygen -f /etc/ssh/ssh_host_rsa_key -t rsa -N "" \
    && ssh-keygen -f /etc/ssh/ssh_host_ecdsa_key -t ecdsa -N "" \
    && ssh-keygen -f /etc/ssh/ssh_host_ed25519_key -t ed25519 -N "" \
    && /sbin/sshd

ADD ./config/ssh_config /etc/ssh/
ADD ./config/sshd_config /etc/ssh/

#
# Hadoop Install
# 2023/06/23 Release 3.3.6
#
ENV HADOOP_VERSION=3.3.6
ENV HADOOP_URL=http://archive.apache.org/dist/hadoop/common/hadoop-$HADOOP_VERSION/hadoop-$HADOOP_VERSION.tar.gz

# Hadoop 3.3.6 버전을 내려받고 /opt/hadoop에 압축 해제
RUN curl -fSL "$HADOOP_URL" -o /tmp/hadoop.tar.gz \
    && tar -xvf /tmp/hadoop.tar.gz -C /opt/ \
    && rm /tmp/hadoop.tar.gz

# 데이터 디렉토리 생성 및 설정 폴더의 심볼릭 링크 생성
RUN ln -s /opt/hadoop-$HADOOP_VERSION /opt/hadoop \
    && mkdir /opt/hadoop/dfs \
    && ln -s /opt/hadoop-$HADOOP_VERSION/etc/hadoop /etc/hadoop \
    && rm -rf /opt/hadoop/share/doc
#
# 실행 환경에 필요한 환경 변수 등록
#
ENV HADOOP_PREFIX /opt/hadoop
ENV HADOOP_HOME $HADOOP_PREFIX
ENV HADOOP_CONF_DIR /etc/hadoop
ENV HADOOP_COMMON_LIB_NATIVE_DIR $HADOOP_HOME/lib/native
ENV HADOOP_OPTS "-Djava.library.path=$HADOOP_COMMON_LIB_NATIVE_DIR"
ENV HADOOP_PID_DIR $HADOOP_HOME/pids
ENV PATH $HADOOP_PREFIX/bin/:$PATH
ENV JAVA_HOME /usr/lib/jvm/java-1.8.0-openjdk-1.8.0.402.b06-1.el7_9.aarch64/jre
ENV YARN_HOME $HADOOP_HOME


# 각 데몬 홈 디렉토리 경로 생성
RUN mkdir /opt/hadoop/dfs/temp \
    && mkdir /opt/hadoop/dfs/namenode \
    && mkdir /opt/hadoop/dfs/datanode \
    && mkdir /opt/hadoop/dfs/namesecondary \
    && mkdir /opt/hadoop/dfs/journalnode \
    && mkdir /opt/hadoop/yarn \
    && mkdir /opt/hadoop/yarn/nm-local-dir \
    && mkdir /opt/hadoop/yarn/system \
    && mkdir /opt/hadoop/yarn/system/rmstore

ADD ./config/core-site.xml $HADOOP_CONF_DIR/
ADD ./config/hdfs-site.xml $HADOOP_CONF_DIR/
ADD ./config/mapred-site.xml $HADOOP_CONF_DIR/

ADD ./config/hadoop-env.sh $HADOOP_CONF_DIR/
ADD ./config/slaves $HADOOP_CONF_DIR/

ADD ./config/yarn-site.xml $HADOOP_CONF_DIR/

# 8020 : dfs.namenode.rpc-address.hadoop-cluster.nn1/nn2

# 8485 : dfs.namenode.shared.edits.dir (공유 편집 로그 저장을 위한 디렉토리 설정)
# qjournal://: QJM (Quorum Journal Manager)을 사용하여 공유 편집 로그를 저장함

# 8088, 8089 : RM HA 구성시 Web UI 접속 포트 

EXPOSE 8020 8485 8089 8088

ADD entrypoint.sh /entrypoint.sh
RUN chmod a+x /entrypoint.sh
