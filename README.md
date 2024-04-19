<link rel="stylesheet" href="./styles.css" />

```
/*****************************************************************************/
*
* Copyright         : 2024/04/18 이현기(Lee Hyungi)
* File Name         : README.md
* Description       : 해당 파일은 Hadoop EcoSystem 설치 및 구성에 있어 실행에 
                      필요한 전반적인 내용을 포함하고 있습니다.
*                    
* Revision History  :
* Date		      Author 			Comments
  2024/04/18  이현기 (Lee Hyungi)     초안 작성
* ------------------------------------------------------------------
* 2024/04/17  README.md	            (초안 작성) Hadoop EcoSystem 구성 및 설정내용 작성
                                              설치 순서 상세내용 작성
* ------------------------------------------------------------------
* 
/****************************************************************************/
```

# 데이터 플랫폼 구성

## <u>시스템 구성도</u>

<img src="./hadoop_ecosystem_infra.png" alt="" />

## <u>Hadoop EcoSystem Docker container 구성</u>

### <u>Hadoop EcoSystem version 구성</u>

`yellow : 작성완료` `pink : 진행중`
<table>
    <tr>
        <th style="text-align: center">index</th>
        <th style="text-align: center">component</th>
        <th style="text-align: center">image</th>
        <th style="text-align: center">version</th>
    </tr>
    <tr style="text-align: center">
        <td class="complete">1</td>
        <td class="complete">Zookeeper</td>
        <td class="complete">Docker official image</td>
        <td class="complete">3.9.2</td>
    </tr>
    <tr style="text-align: center">
        <td class="complete">2</td>
        <td class="complete">Kafka</td>
        <td class="complete">Official Confluent Docker Image <br/>(Community)</td>
        <td class="complete">7.4.4</td>
    </tr>
    <tr style="text-align: center">
        <td class="complete">3</td>
        <td class="complete">Hadoop</td>
        <td class="complete">자체 제작 이미지 사용</td>
        <td class="complete">3.3.6</td>
    </tr>
    <tr style="text-align: center">
        <td class="complete">4</td>
        <td class="complete">Hive</td>
        <td class="complete">자체 제작 이미지 사용</td>
        <td class="complete">4.0.0</td>
    </tr>
    <tr style="text-align: center">
        <td class="complete">5</td>
        <td class="complete">Tez</td>
        <td class="complete">Hive 이미지 생성시 내부에 Engine 설치 및 환경설정</td>
        <td class="complete">0.10.3</td>
    </tr>
    <tr style="text-align: center">
        <td>6</td>
        <td>HBase</td>
        <td>자체 제작 이미지 사용</td>
        <td>2.5.8</td>
    </tr>
    <tr style="text-align: center">
        <td>7</td>
        <td>Phoenix</td>
        <td>자체 제작 이미지 사용</td>
        <td>5.1.3</td>
    </tr>
    <tr style="text-align: center">
        <td class="complete">8</td>
        <td class="complete">PostgreSQL</td>
        <td class="complete">Docker official image</td>
        <td class="complete">15.6</td>
    </tr>
</table>


### <u>Docker container Port 구성 및 설정</u>

<table>
    <tr>
        <th style="text-align: center">index</th>
        <th style="text-align: center">component</th>
        <th style="text-align: center">port</th>
        <th style="text-align: center">dependencies</th>
        <th style="text-align: center">Configuration</th>
    </tr>
    <tr style="text-align: center">
        <td class="complete">1</td>
        <td class="complete">Zookeeper</td>
        <td class="complete">
            <div class="align-center">
                - zoo-1(2181)<br/>
                - zoo-2(2182)<br/>
                - zoo-3(2183)
            </div>
        </td>
        <td class="complete">none</td>
        <td class="complete"></td>
    </tr>
    <tr style="text-align: center">
        <td class="complete">2</td>
        <td class="complete">Kafka</td>
        <td class="complete">
            <div class="align-center">
                - kafka-1(29092)<br/>
                - kafka-2(39092)<br/> 
                - kafka-3(49092)
            </div>
        </td>
        <td class="complete">
            <div class="align-center">
                [Zookeeper] <br/>- zoo-1<br/>- zoo-2<br/>- zoo-3
            </div>
        </td>
    </tr>
    <tr style="text-align: center">
        <td class="complete">3</td>
        <td class="complete">Hadoop</td>
        <td class="complete align-center">
            <div class="align-center">
                [NameNode 01] <br/> - 50070 (NameNode Web UI)<br/>- 8088 (YARN RM Web UI)<br/>
            </div>
            <br/>
            <div class="align-center">
                [NameNode 02] <br/> - 50080 (NameNoe Web UI)<br/>- 8089 (YARN RM Web UI)<br/>
            </div>
        </td>
        <td class="complete">
            <div class="align-center">
                [Zookeeper] <br/>- zoo-1<br/>- zoo-2<br/>- zoo-3
            </div>
        </td>
    </tr>
    <tr style="text-align: center">
        <td class="complete">4</td>
        <td class="complete">Hive</td>
        <td class="complete">
            <div class="align-center">
                [HiveServer 01] <br/> - 10000
            </div>
            <br/>
            <div class="align-center">
                [HiveServer 02] <br/> - 10002
            </div>
        </td>
        <td class="complete">
            <div class="align-center">
                [Zookeeper] <br/> - zoo-1<br/>- zoo-2<br/>- zoo-3
            </div>
            <br/>
            <div class="align-center">
                [Hadoop] <br/> - nn01<br/>- nn02<br/>- dn01<br/>- dn02<br/>- dn03
            </div>
            <br/>
            <div class="align-center">
                [Metastore] <br/> - metastore
            </div>
        </td>
    </tr>
    <tr style="text-align: center">
        <td class="complete">5</td>
        <td class="complete">Tez</td>
        <td class="complete">(Hive Execution Engine)</td>
        <td class="complete">Hive 내부에 구성</td>
    </tr>
    <tr style="text-align: center">
        <td>6</td>
        <td>HBase</td>
        <td>
            <div class="align-center">
                [HMaster 01 / 02] <br/> - 16000 / TBD
            </div>
            <br/>
            <div class="align-center">
                [HRegionServer 01 / 02 / 03] <br/> - 16020 / TBD / TBD
            </div>
        </td>
        <td></td>
    </tr>
    <tr style="text-align: center">
        <td>7</td>
        <td>Phoenix</td>
        <td>8765</td>
        <td></td>
    </tr>
    <tr style="text-align: center">
        <td class="complete">8</td>
        <td class="complete">PostgreSQL</td>
        <td class="complete">15432</td>
        <td class="complete">none</td>
    </tr>
</table>

### <u>설치 순서</u>

(1) Hadoop 설치하기

- hadoop_base 이미지 빌드하기
    ```zsh   
    $ python installer.py hdfs build
    ```

- postgreSQL 이미지 빌드하기
    ```zsh
    $ python installer.py 
    ```

(1) Zookeeper가 설치된다.

(2) Kafka broker 컨테이너는 Zookeepeer 컨테이너들이 올라간 후에 설치를 진행한다.

(3) 
