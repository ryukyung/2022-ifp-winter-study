# 💻 IFP 2022년 겨울방학 스터디


- 활동 기간 : 2022.01.03(월) ~ 2022.02.27(일)

- 동아리 회장 

  - 이하람 <[HalamLee](https://github.com/HalamLee)>

- 참여 동아리원

  - [부회장]  정채은 <[chaeeunj](https://github.com/chaeeunj)>
  - 경준현 <[hyeon0697](https://github.com/hyeon0697)>
  - 곽혜린 <[hr111322](https://github.com/hr111322)>
  - 김성환 <[PotatoMeme](https://github.com/PotatoMeme)>
  - 김태영 <[overtae](https://github.com/overtae)>
  - 라효은 <[hyoeunla](https://github.com/hyoeunla)>
  - 류경혜 <[ryukyung](https://github.com/ryukyung)>
  - 박종민 <[jongmung](https://github.com/jongmung)>
  - 안동섭 <[tjqehd23](https://github.com/tjqehd23)>
  - 유경덕 <[N0Rib](https://github.com/N0Rib)>
  - 유재우 <[blooper20](https://github.com/blooper20)>
  - 이지희 <[ji1210h](https://github.com/ji1210h)>
  - 채희진 <[coowooc](https://github.com/coowooc)>

## ❓ 무엇을 하는가?

- 파이썬 코딩 도장 Unit 20까지 + 코드업 기초 100문제

## 🔍 어떻게 하는가?

1. 주어진 과제를 수행

2. 작성한 코드를 관련 폴더에 저장

3. 저장한 파일을 개인별 Fork한 Repo의 Branch(각자 이름)로 PUSH

4. 개인별 깃허브 Repo에 PUSH된 Branch를 IFP의 겨울방학 스터디 저장소의 개인 Branch(각자 이름)로 PR을 보냄

5. 해당 과정을 반복

   ```
   1. IFP의 겨울방학 스터디 저장소 Fork
   2. 본인의 겨울방학 스터디 저장소를 Clone (로컬의 저장소 폴더가 생성됨)
   3. IFP의 겨울방학 스터디 저장소와 동기화 (변경된 내역을 나의 저장소에도 일치시켜주는 작업)
   
   # 먼저 로컬부터 동기화해줘야 한다. (Fork 하기 전의 레포. 즉, IFP 레포의 remote 이름을 "upstream"이라고 해준다.)
   # upstream 추가 -> 통상적으로 upstream이라고 해주는게 원칙이다.
   $ git remote add upstream https://github.com/HalamLee/ifp-2022-winter-vacation-study
   # upstream 레포의 변경 내역을 로컬의 저장소와 병합
   $ git pull upstream main
   
   # 본인이 작업할 브랜치 생성 (ex: git branch 브랜치명)
   $ git branch leehalam
   # 해당 브랜치로 이동 (ex: git checkout 브랜치명)
   $ git checkout leehalam
   # 로컬의 main과 이동한 브랜치를 병합 (이로써 로컬의 leehalam 브랜치와 upstream의 main 브랜치가 동기화되었다.)
   $ git merge main
   
   4. 관련 폴더(ex: codeup) 생성
   $ mkdir codeup
   
   5. codeup 폴더로 이동
   $ cd codeup
   
   6. 풀이한 코드 업로드 (파일명 : 코드업-기초-100제-34번.py)
   
   7. 깃 Staging Area에 저장 (ex: git add 파일명)
   # 파일명에 "."을 하면 현재 폴더의 전체 파일을 tracked함.
   # 파일명에 "-a"(all의 약자)을 하면 ".git" 폴더가 위치한 루트 경로부터 전체 파일을 tracked 함.
   $ git add -a 
   
   8. ".git" 폴더에 저장 (ex: git commit -m "브랜치명(이름): 메세지") -> "-m"은 message의 약자
   $ git commit -m "leehalam: 코드업-기초-100제-34번-풀이"
   
   9. 본인이 Fork한 깃헙 저장소에 업로드 (ex: git push <Remote> <Branch>)
   $ git push origin leehalam
   
   10. 본인이 Fork한 깃헙 저장소로 이동하여 Pull Request(PR)를 보낸다.
    ❗ 이때, IFP 저장소의 main 브랜치가 아닌 "본인 이름의 브랜치"로 보내야함
    이후 회장이 확인한 후 IFP 저장소의 본인 브랜치로 병합시켜주는 작업을 하게 된다.
   ```

   

