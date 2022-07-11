# CanFindCan | 시각장애인을 위한 캔음료 인식 애플리케이션
<br/>

### 💡 프로젝트 소개
- PORT-MIS에 지속해서 등록되는 매뉴얼에 대한 학습을 적용한 기계 독해를 활용한다. 어떤 업무? 이런 업무의 정답이 뭐지? 일일이 외우고 암기할 필요 없이 질문하면 최적화된 정답이 무엇인지 알아서 찾아준다.
- PORT-MIS에 실시간으로 등록되는 민원이나 업무 문의로 업무 피로도가 증가하고, 정말 중요한 업무처리의 우선순위가 늦춰지는 경우가 발생한다. 또한, 업무 숙련가가 되기 위해서는 큰 노력과 비용 및 시간이 필요하다. 이런 부분을 기계 독해를 통해 정확하고 빠르게 응대할 수 있도록 도와줄 수 있다.
<br/>

### 💡 작품의 개발 배경 및 필요성
<img width="800" alt="image" src="https://user-images.githubusercontent.com/66028419/178177905-d3b9a360-277f-41d5-88c5-371f320c74eb.png">  
<img width="800" alt="image" src="https://user-images.githubusercontent.com/66028419/178178011-ee484d6d-87e7-4534-85eb-6384307ca08f.png">
<br/>

### 💡 작품 기능
1. 캔 종류 인식 (코카콜라, 펩시, 스프라이트, 칠성사이다, 밀키스, 웰치스 포도, 포카리스웨트, 환타 오렌지)
2. 캔의 유통기한 인식 
<br/>

### 💡 작품 구성도
<img width="600" alt="image" src="https://user-images.githubusercontent.com/66028419/178178521-5ebdd0e0-04b2-47c8-89bc-8b86cecdfa30.png">  
<img width="416" alt="image" src="https://user-images.githubusercontent.com/66028419/178178892-d28897d6-ee9d-4c20-b70f-6f380cfebc10.png">
<br/>


### 💡 관련 기술
**1. 객체 탐지**  
  - 웹 크롤링
  - labelImg 툴을 이용하여 이미지의 클래스와 경계박스 지정
  - YOLOv5를 통한 학습
  - 학습된 pt 파일을 tfjs 모델로 변환  

**2. 글자 인식**
  - Amazon AWS IoT Core, AWS Rule, AWS IAM, AWS S3, AWS Cognito
  - Amazon Rekognition 
<br/>


### 💡 애플리케이션 구조 
<img width="600" alt="image" src="https://user-images.githubusercontent.com/66028419/178180128-2db8aa7c-6c85-4a0d-b866-1dacffc7b4c0.png">  
1. 캔음료 구분  
<img width="800" alt="image" src="https://user-images.githubusercontent.com/66028419/178180308-55dcafad-1a8f-4b13-96b3-df30b2a69964.png">
2. 유통기한 인식 
<img width="800" alt="image" src="https://user-images.githubusercontent.com/66028419/178180414-9740bf48-9a24-41e4-b9d9-45398e5b5741.png">
<img width="800" alt="image" src="https://user-images.githubusercontent.com/66028419/178180439-4b0574ea-4d89-4f71-a080-bdf444acf44c.png">
<br/>


### 💡 기대효과 및 발전 방향
1. 캔 음료 구분에 대한 시각장애인들의 불편함 해소
2. 일반 음료, 과자, 의약품 등과 같이 다양한 분야에서 활용
3. 캔 상세정보 검출, 캔 위치 찾기 등 추가적인 기능으로 애플리케이션 확장
<br/>


### 🔗 유튜브 링크
https://youtu.be/_G1CdMcqkwQ
<br/>

