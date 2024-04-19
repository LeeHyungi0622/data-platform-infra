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
# * 
# /******************************************************************/
import os
import sys

if sys.argv[1] == "hdfs":
    if sys.argv[2] == "build":
        os.system("docker build -t hadoop_base:latest .")
elif sys.argv[1] == "metastore":
    if sys.argv[2] == "build":
        os.system("docker pull postgres:15.6")