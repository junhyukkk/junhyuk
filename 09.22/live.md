# SWEA 문제풀이
### 문제풀이 tip!
1. 문제해석
   - 문제에서 원하는 목표
    -> 명확하게 문제를 파악
============예시문제=================
1486. 장훈이의 높은선반(문제해석)
- 서점
    - 높이가 B인 선반
    - 선반
        - 키가 큰 장훈이는 물건을 자유롭게 이용할 수 있다.
    - 점원(키 =Hj)
        - 선반의 물건을 사용하기 위해 탑을 쌓는다.
        - 탑을 쌓는 방법
            - 1명 : 점원의 키 == 탑의 높이
            - 2명 이상 : 점원 키의 합 == 탑의 높이
              
            = 선반보다 높거나 같을 경우 물건을 쓸 수 있다.
    * 높이가 B이상인 탑 중에서, 높이가 가장 낮은 탑을 구해라.
- 재귀,완전탐색,백트레킹 풀면서
1. 기저조건
2. 가지치기조건
3. 다음재귀함수호출
4. 돌아왔을때 순서 외우기

----문제해석(완)----
2. 무슨 알고리즘을 쓸까?
   - 시뮬레이션 결과, 미리 무언가를 구할 수 없음.
     - 모든 경우의 수를 구해야함
        1) 완전탐색문제임을 가정하고 접근(N이 11 이상인경우 완전탐색 시간초과)
        2) N > 11 = backtracking 사용(문제의 조건을 보고 가지치기)
    

tip!
0. IDE 를 적극적으로 활용
- 디버깅 툴 >> 적극적으로 써라
