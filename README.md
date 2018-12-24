# mjolnir

로컬 네크워크 상에서 간단하게 API를 테스트하기 위해 만든 도구입니다.
API의 실제 response 값과 원하는 response값 간의 type을 비교합니다.
구체적인 값을 assertion 하는 일반 테스터에 비해 추상화 된 비교를 수행하기 때문에 엄밀한 테스트보다는 가볍게 response type check를 하도록 만들어져 있습니다.

### 사용법

인덱스 페이지의 구성입니다.
![index](https://github.com/jamanvo/jamanvo.github.io/blob/master/assets/img/post/mjolnir_index.png)

헤더 부분은 테스트할 API의 URL 입력창, 메소드 선택버튼, 전송 버튼이 있습니다.
하단의 바디 부분은 API로 전송할 arguments, 기대하는 response, 실제 API의 response, API respone 결과와 기대값의 비교 결과를 보여주는 부분입니다.

#### 필수 입력 필드
* URL
* Control Group
* API Arguments(POST 메소드 선택시)

#### 헤더

**URL 입력창**
테스트 할 API의 URL을 입력합니다.
http~ 부터 전체의 root가 입력되어야 합니다.

**메소드 선택**
현재는 GET와 POST 메소드만이 선택 가능합니다.
향후 나머지 REST 메소드(PUT/DELETE)를 추가할 계획입니다. 

**전송**
필요한 값을 전부 입력한 뒤 API 테스트를 실행합니다.

#### 바디

**API Arguments**
API에 전송할 arguments를 JSON string 형태로 입력합니다.
GET 메소드를 선택한 경우에는 비어있어도 상관없으며, POST 메소드를 선택한 경우에는 필수입력필드입니다.

**Control Group**
기대되는 API의 결과값 입니다.
이 값을 기준으로 response 비교를 하게되며, 테스트의 핵심이기 때문에 반드시 입력되어야 합니다.
JSON string으로 입력이 되어야하며, 전송시 값이 비어있거나 JSON으로 파싱이 불가능한 값이 들어있는 경우에는 에러가 발생합니다.

** API Response**
테스트를 실행했을 때의 API의 response입니다.
아무런 가공이 되어있지 않은 상태이며, JSON string으로 보여지게 됩니다.

**Response Compare Result**
Control Group과 API Response를 비교한 결과입니다.
Control Group을 기준으로 하기때문에, API Response에 Control Group에 없는 아이템이 있는 경우 해당 아이템은 무시됩니다.
JSON string으로 표현되어 있으며, {key: bool} 형태로 표현이 됩니다.
true인 경우에는 동일한 데이터타입을 나타내며, false인 경우에는 API response에 키가 없거나 다른 데이터타입이 들어있는 경우입니다.
