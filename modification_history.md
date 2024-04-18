- HDFS 구성시 수정해야 될 부분

    기존 HDFS 구성시, resource manager와 연동되어있던 zookeeper 설정을 내부 zookeeper가 아닌, 외부 Zookeeper로 연동되도록 수정 `(완료)`
    - Dockerfile 내 /opt/zookeeper 하위에 디렉토리 생성 command 제거 `(완료)`
    - HDFS image (root 경로)파일에서 Zookeeper 설치 및 cfg file 복사 부분 cmd 제거 `(완료)`
    - Docker file 내 cmd 실행에서 읽히고 있는 entrypoint.sh 파일 수정 (zookeeper 실행 부분 수정하기)

    - 2181 포트 검색 결과 내용 수정
        - config/core-site.xml (zookeeper.quorum value 수정) `(완료)`
        - config/yarn-site.xml (yarn.resourcemanager.zk-address value 수정) `(완료)`
        - config/zoo.cfg 파일 삭제 (외부 zookeeper 연동) `(완료)`

    - entrypoint.sh 내용 수정
        - zookeeper 서버 시작 스크립트 실행부분 제거 `(완료)`

- Hive 구성시 수정해야 될 부분
    - entrypoint.sh 파일 사용되고 있는 부분 찾아서 경로 수정하기
    - 2181 포트 검색 결과 내용 수정
       - hive/hive-site.xml 파일 (hive.zookeeper.quorum value 수정)

- HBase 구성시 수정해야 될 부분
    - entrypoint.sh 파일 사용되고 있는 부분 찾아서 경로 수정하기

- docker-compose.yml 구성시 수정해야 될 부분
    - entrypoint.sh 파일 사용되고 있는 부분 찾아서 경로 수정하기

