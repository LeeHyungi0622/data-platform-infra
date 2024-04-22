# /*******************************************************************
# *
# * Copyright         : 2024/04/18 이현기(Lee Hyungi)
# * File Name         : install.py
# * Description       : 해당 파일은 Hadoop EcoSystem을 설치시 이미지 빌드 및 컨테이너 생성
#                       과정을 좀 더 편리하게 하기 위해 작성한 JavaScript 기반 파일입니다.
# *                    
# * Revision History  :
# * Date		      Author 			Comments
#   2024/04/18  이현기 (Lee Hyungi)     초기 작업 착수
# * ------------------------------------------------------------------
# * 2024/04/18          	        hdfs base 이미지 빌드 스크립트 작성
# *                      	        metastore 이미지 빌드 스크립트 작성
# * ------------------------------------------------------------------
# * 2024/04/19          	        hive 이미지 빌드 스크립트 작성
# *                      	        
# * ------------------------------------------------------------------
# * 
# /******************************************************************/
import os
import sys
import time

hbase_version = '2.5.0'
phoenix_version = '5.2.0'

if sys.argv[1] == "all":
    if sys.argv[2] == "start":
        time.sleep(2)
        print("Hadoop 자체 이미지 생성이 시작되었습니다.")
        os.system("docker build -t hadoop_base:latest .")
        print("Hadoop 자체 이미지 생성이 완료되었습니다.")
        time.sleep(2)
        print("PostgreSQL 15.6 공식 이미지 Pull이 시작되었습니다.")
        os.system("docker pull postgres:15.6")
        print("PostgreSQL 15.6 공식 이미지 Pull이 완료되었습니다.")
        time.sleep(2)
        print("Hive 자체 이미지 생성이 시작되었습니다.")
        os.system("cd ./hive && docker build -t hive_base:latest .")
        print("Hive 자체 이미지 생성이 완료되었습니다.")
        time.sleep(2)
        print("confluentinc/cp-kafka 7.4.4 공식 이미지 Pull이 시작되었습니다.")
        os.system("docker pull confluentinc/cp-kafka:7.4.4")
        print("confluentinc/cp-kafka 7.4.4 공식 이미지 Pull이 완료되었습니다.")
        time.sleep(2)
        print("zookeeper:latest 공식 이미지 Pull이 시작되었습니다.")     
        os.system("docker pull zookeeper:latest")
        print("zookeeper:latest 공식 이미지 Pull이 완료되었습니다.")     
        time.sleep(2)
        print("HBase 자체 base 이미지 빌드가 시작되었습니다.")
        os.system(f"docker build -t hbase-{hbase_version} ./hbase/base")
        print("HBase base 이미지 빌드가 완료되었습니다.")
        time.sleep(2)
        print("HBase 자체 HMaster 이미지 빌드가 시작되었습니다.")
        os.system(f"docker build -t hbase-master-{hbase_version} ./hbase/hmaster")
        print("HBase 자체 HMaster 이미지 빌드가 완료되었습니다.")
        time.sleep(2)
        print("HBase 자체 HMaster 이미지 빌드가 시작되었습니다.")
        os.system(f"docker build -t hbase-regionserver-{hbase_version} ./hbase/hregionserver")
        print("HBase 자체 HMaster 이미지 빌드가 완료되었습니다.")
        time.sleep(2)
        print("HBase 자체 Phoenix 이미지 빌드가 시작되었습니다.")
        os.system(f"docker build --platform linux/amd64 -t phoenix-{phoenix_version} ./phoenix")
        print("HBase 자체 Phoenix 이미지 빌드가 시작되었습니다.")
        time.sleep(3)
        os.system("docker-compose up -d")
