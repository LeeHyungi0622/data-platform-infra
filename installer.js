/*******************************************************************
*
* Copyright         : 2024/04/18 이현기(Lee Hyungi)
* File Name         : install.js
* Description       : 해당 파일은 Hadoop EcoSystem을 설치시 이미지 빌드 및 컨테이너 생성
                      과정을 좀 더 편리하게 하기 위해 작성한 JavaScript 기반 파일입니다.
*                    
* Revision History  :
* Date		      Author 			Comments
  2024/04/18  이현기 (Lee Hyungi)     초기 작업 착수
* ------------------------------------------------------------------
* 2024/04/18  install.js	        hdfs base 이미지 빌드 스크립트 작성
* ------------------------------------------------------------------
* 
/******************************************************************/

const { execSync } = require('child_process');

/**
 * 
 * 기본 실행 command : node [파일이름].js hdfs build
 * 
 */
if (process.argv[2] === "hdfs") {
    if (process.argv[3] === "build") {
        execSync("docker build -t hadoop_base:latest .")
    }
}

if (process.argv[2] === "metastore") {
    if (process.argv[3] === "build") {
        execSync("docker pull postgres:15.6")
    }
} 
