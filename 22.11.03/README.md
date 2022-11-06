## :books: Linux

### 계정 연결 (명령 프롬프트)
    
    ssh (자기아이디)@공용 IP 주소


###  패키지 설치

    sudo apt-get install \
	apt-transport-https \
	ca-certificates \
	curl \
	gnupg \
	lsb-release
    
### 도커 인증 키 다운로드

    curl -fsSL http://download.docker.com/linux/ubuntu/gpg
    

### 도커 설치

    sudo apt-get install docker-ce docker-ce-cli containerd.io
    

### 권한 변경

    sudo usermod -a -G docker $USER
    

---
### 명령어
* 접속을 끊고 나가기 : exit
* 이미지 가져오기 : pull


### :bulb: TIP
* 잘못 입력하여 실행 취소하고 싶을 때 : Ctrl + c
* 복사본을 붙여넣고 싶을 때 : 마우스 우클릭
* 가상머신 접속 비밀번호를 잊거나 헷갈릴 때 : 
	*	애저 - 리소스 그룹 - 자신의 가상 머신 - '암호' 검색  - 암호 다시 설정
