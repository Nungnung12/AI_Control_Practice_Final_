# AI_Control_Practice_Final_


#### AI 제어실습(python) 가위 바위보
https://www.youtube.com/watch?v=l-hCgD5ig2o



https://user-images.githubusercontent.com/112921153/204450415-cf8ed640-6fdd-43cd-9a96-e88da5e2612d.mp4

AI의 구조가 단순해짐에 따라 가위바위보로 승리를 매겨주는 AI를 제작

midiapipe_hands 오픈소스 알고리즘 주소

https://google.github.io/mediapipe/
![image](https://user-images.githubusercontent.com/112457426/207075173-0a9991be-561d-4feb-9026-8c79f8ed99dc.png)

손 추적을 위한 MediaPipe 그래프는 아래와 같다. 그래프는 2개의 하위 그래프로 구성된다. 하나는 손 감지용이고 다른 하나는 손 키포인트 계산용이다. MediaPipe가 제공하는 핵심 최적화 중 하나는 손바닥 감지기가 필요한 경우에만 실행되어 상당한 계산 시간을 절약한다는 것이다. 현재 프레임의 계산된 손 키 포인트에서 후속 비디오 프레임의 손 위치를 추론하여 각 프레임에 대해 손바닥 감지기를 실행할 필요가 없다. 견고성을 위해 손 추적기 모델은 손이 있고 투입 데이터가 합리적으로 정렬되어 있다는 확신을 포착하는 추가 스칼라를 출력한다. 신뢰도가 특정 임계 값 아래로 떨어질 때만 손 감지 모델이 전체 프레임에 다시 적용된다.



![image](https://user-images.githubusercontent.com/112457426/207077908-e8df644e-01ac-44b8-aa92-a2089d67a2cb.png)

![image](https://user-images.githubusercontent.com/112457426/207075775-42aa7577-6747-4acb-98f3-18126e374196.png)
