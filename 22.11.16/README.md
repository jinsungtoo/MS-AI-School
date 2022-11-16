### DP 900
총 4개의 섹션
#### 1단원
데이터란 무엇인가요? 

    구조화 : 데이터베이스
    반구조화 : documentDB
    아무런 구조도 없고 그냥 때려넣는 것 : 텍스트 메시지, 보이스 레코딩 파일 등

트랜잭션 

    OLTP : 온라인 거래 처리(데이터는 한번에 한 트랜잭션으로 저장)
    OLAP : 온라인 분석 처리(데이터는 큐브에 주기적으로 로드,집계, 저장됨)
    트랜잭션의 속성 : 원자성,일관성, 격리, 영속성
    
* 분석 워크로드 : 요약(summary), 추세(trend), 비즈니스 정보

데이터 처리 기법

    일괄 처리 :모아서 한번에
	스트림 처리 : 각 새 데이터가 도착하면 처리
---
#### 2단원
데이터의 역할

    데이터베이스 관리자 : 데이터베이스 관리, 보안구현,백업,사용자 액세스, 성능 모니터링
	데이터 엔지니어 : 파이프라인 및 프로세스, 데이터 수집 스토리지, 분성용 데이터 준비 ,분석 처리를 위한 데이터 준비
	데이터 분석자 : 데이터에 대한 인사이트 제공, 시각적 개체 보고, 분석을 위한 데이터  모델링, 시각화 및 분석을 위해 데이터 결합
    
* 공통 도구 
	* 애저 데이터 스튜디오 : 온-프레미스 및 클라우드 기반 데이터 서비스 관리를 위한 그래픽 인터페이스(윈도우,맥,리눅스 사용)
	* Sql 서버 management studio : 온-프레미스 및 클라우드 기반 데이터 서비스 관리를 위한 그래픽 인터페이스(윈도우에서 실행)
	* 애저 포탈/CLI : 애저 데이터 서비스의 관리 및 프로비전용 도구
---
#### 3단원
관계형 데이터베이스 사용 사례 식별

    - iot
    - 온라인 트랜잭션 처리
    - 데이터 웨어하우징
* 엔티티란 : 실제 항목 또는 가상 항목
* Azrure virtual 머신의 Sql server : Iaas
* Azure DB – 복제본 읽기

SQL문 유형

    DML : 데이터 조작 언어 select,insert, update, delete
    DDL : 데이터 정의 언어 create, alter, drop, rename
    DCL : 데이터 컨트롤 언어 grant, revoke,deny

쿼리 도구 

    -애저포탈(web broser)
    -sql매니지먼트 스튜디오(window)
    -sql 서버 데이터 툴즈(window)
    -애저 데이터 스튜디오(window, mac, linux)
    -sqlCMD, azure CLI/Cloud Shell(terminal,web browser)
Azure table storage 

    key와 value로 저장이 되어있음
	Key는 일정하나(고정), value는 일정하지 않음(비정형, 비관계형 데이터)

* Azure blob storage : azure storage account를 먼저 만들어야함.(blob(container) 혹은 files or table or queue)
* Azure file storage : network disk 역할, 파일 공유에 서버 메시지 블록 3.0(SMB) 사용
	
* Azure cosmos DB란? (cosmos를 사용하려면 container를 추가 후 사용)
	* 다중 모델 NoSQL DBMS. 
	
	  - cosmos DB는 분할된 문서 집합으로 데이터를 관리
	  - 실시간 액세스로 읽기 및 쓰기 대기 시간이 짧음
	  - azure 스케일링과 스토리지 기능을 활용
* Cosmos DB API : SQL API, MongoDB API(NoSQL), Cassandra API, Gremlin API, Table API
	
* Cosmos DB 사용 사례 :
    웹 및 소매, 게임, IOT 시나리오
---
#### 4단원 
데이터 웨어하우스용 azure 서비스

    -azure data factory
    -azure data lake
    -azure databricks 
    -azure HDinsight
    -azure synapse analytics
* Azure Data factory : 컨베이어벨트처럼 여러 군데에서 들어오는 데이터를 모아서 처리, 파이프라인 작업으로 정의
* Azure data lake storage : POSIX(linux, unix) 및 RBAC 권한을 지원한다
	* Hadoop 분산 파일 시스템과 호환
* Azure databricks : 빅 데이터 처리 및 스트리밍 기능 제공하는 Apache Spark 기반 플랫폼
* Azure Analysis services : OLAP(온라인 분석 처리) 쿼리를 지원하기 위해 테이블 형식 모델을 빌드
* Azure HDinsight : azure 환경의 한 플랫폼에서 오픈 소스 라이브러리 사용을 지원하는 빅 데이터 처리 서비스
* Power BI :

Power BI를 사용할 수 있는 방법 

    power BI desktop, power bi 서비스, power bi mobile

Power BI 앱의 구성 요소 

    시각화, 데이터 셋, 보고서, 대시보드, 타일
