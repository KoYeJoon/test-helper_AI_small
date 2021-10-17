# 1. unit test

모듈 단위, api 전송 시, api 응답 시에 대한 unit test를 작성해보았다.

### test code 작성 시 만났던 크고 작은 이슈들 

1. UnitTest의 test case에 해당하는 함수는 "test_" 라는 이름으로 시작해야 한다.  
  
<br />
<br />
2. boto3는 aws api에 함수로써 연결할 수 있도록 하는 것으로 auto connection close가 된다. 하지만 unit test 진행 시에는 resource 관련 warning이 뜬다. 
urllib를 활용하여 api 접근 시에는 close를 해주면 되지만, boto3 의 warning은 unit test에서 불가피한 것으로 보인다.  
출처 : github issue, stack overflow
  
<br />
  
다음 github issue를 참고하여 warning이 뜨지 않도록 임의로 차단하였다.  
[Click! boto3 github issue](https://github.com/boto/boto3/issues/454)

unit test 시 초기 시, 종료 시 발생되는 코드는 다음과 같이 작성한다.

```python
import warnings 

def setUp(self):
        # 시작 시 활성화되는 코드 
        warnings.filterwarnings("ignore", category=ResourceWarning, message="unclosed.*<ssl.SSLSocket.*>") 

    def tearDown(self):
        # 테스트 종료 후 활성화되는 코드 
        pass
```
   
cf ) Capstone 수업에서 배웠던 JUnit과 비교하였을 때, JUnit의 @before == setUp, @after ==tearDown 같은 느낌이다. 


### 1. 본인인증 테스트

### 2. 두 손 인식 테스트


# 2. API test with no server 

### 1. 본인인증 테스트
### 2. 두 손 인식 테스트 


# 3. API test with server 

### 1. 본인인증 테스트 
### 2. 두 손 인식 테스트 


# 4. view-test
간단한 html을 만들어, 실제 본인인증, 두손 인식 결과를 시각화할 수 있도록 하였다. 

## How to uses?

1. view_test 를 실행하면 된다 !

```bash
$ python view_test.py
```
```
cf ) hand_detection/yolo3/src model 구분
yolo3.py : yolo3 원래 본 모델 --> PIL.image 사용하여야 하므로 font가 필요하다. 이 모델은 사용하지 않았다.
yolo3_cv.py : view_test를 위해 PIL이 아닌 cv2로 그림을 그리도록 수정하였다. cv2는 PIL보다 이미지 처리 속도가 훨씬 빠르기 때문에 view_test에서는 cv2로 바꾸었다. 이는 view_test에서 손 위치를 그림으로 보여줄 때 사용된다.
yolo3_simple.py : 몇 개의 손이 인식되었는지에 대해서만 반환한다. 이는 app.py에서 실제로 사용되는 모델이다.
```