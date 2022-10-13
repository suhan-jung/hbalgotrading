# hbalgotrading
# 알고리즘 트레이딩 시스템 개발


## 딜러 개입이 필요없는 최소기능의 자동매매시스템 구현

<p style="text-align: right">
2022.10.11. DT x 퀀트</p>



### 1. 개발목표 : 단일자산/단일전략/분봉데이터 기반 백테스트/실제매매 가능 시스템


### 2. 추진사유



* 작동되는 트레이딩 전략을 찾기 위해서는 백테스트와 실제(가상)매매의 많은 반복이 필요


* 자산/전략/데이터주기 등을 다양하게 변경할 수 있는 자체 구축 시스템이 필요

### 3. 개발내용
![algo-small](https://user-images.githubusercontent.com/19812675/195486362-45e69ffc-f9af-4d5c-88ed-b9b8c0ddc660.jpg)

### 4. 개발계획



* 개발환경 : 은행 외부망 PC (우분투 리눅스) - 개발 및 이후 제어 편의성 고려


* 데이터 수집 : 증권사(한국투자증권) api 활용 - 접근성 높은 기초적 방법


* 개발언어 : 파이썬(python), github, jira 등 활용 - 자체 개발방식 확립


* 인력 : 김정래 차장(개발), 정수한 차장(기획, 개발 일부, 프로젝트 관리 등)


* 일정 : 프로토타입(최소기능버전) 연말 완성 목표

### 5. 필요사항



* 개발인력 안정적 확보 : 김정래 차장 지속적 지원 및 필요시 개발가능인력 채용 등 보강


* 실제 매매 관련 : 추후 자동매매 실거래 관련 유관부서 협의, 서버/네트워크 등 운영 시스템 구축
