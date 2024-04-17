<link rel="stylesheet" href="./styles.css" />

# 데이터 플랫폼 구성

## Hadoop EcoSystem Docker container 구성

### Hadoop EcoSystem version 구성 

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
        <td class="progress">3</td>
        <td class="progress">Hadoop</td>
        <td class="progress">자체 제작 이미지 사용</td>
        <td class="progress">3.3.6</td>
    </tr>
    <tr style="text-align: center">
        <td>4</td>
        <td>Hive</td>
        <td>자체 제작 이미지 사용</td>
        <td>4.0.0</td>
    </tr>
    <tr style="text-align: center">
        <td>5</td>
        <td>Tez</td>
        <td>Hive 이미지 생성시 내부에 Engine 설치 및 환경설정</td>
        <td>0.10.3</td>
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
</table>


### Docker container Port 구성 및 설정

<table>
    <tr>
        <th style="text-align: center">index</th>
        <th style="text-align: center">component</th>
        <th style="text-align: center">port</th>
        <th style="text-align: center">Configuration</th>
    </tr>
    <tr style="text-align: center">
        <td class="complete">1</td>
        <td class="complete">Zookeeper</td>
        <td class="complete">2181, 2182, 2183</td>
    </tr>
    <tr style="text-align: center">
        <td class="complete">2</td>
        <td class="complete">Kafka</td>
        <td class="complete">29092, 39092, 49092</td>
    </tr>
    <tr style="text-align: center">
        <td class="progress">3</td>
        <td class="progress">Hadoop</td>
        <td class="progress align-center">
            <div class="align-center">
                [NameNode 01] <br/> - 50070 (NameNode Web UI)<br/>- 8088 (YARN RM Web UI)<br/>
            </div>
            <br/>
            <div class="align-center">
                [NameNode 02] <br/> - 50070 (NameNoe Web UI)<br/>- 8089 (YARN RM Web UI)<br/>
            </div>
        </td>
    </tr>
    <tr style="text-align: center">
        <td>4</td>
        <td>Hive</td>
        <td></td>
    </tr>
    <tr style="text-align: center">
        <td>5</td>
        <td>Tez</td>
        <td></td>
    </tr>
    <tr style="text-align: center">
        <td>6</td>
        <td>HBase</td>
        <td></td>
    </tr>
    <tr style="text-align: center">
        <td>7</td>
        <td>Phoenix</td>
        <td></td>
    </tr>
</table>
