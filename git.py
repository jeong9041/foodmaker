def avg(data, start=0, end=None) :
    if not end :
        end = len(data)
    return sum(data[start:end])/float(end-start)

d = (3, 4, 5, 6, 7)
d2 = d[1:3]
print(d2)
avg(d, 0, 5)
print(avg(d, 0, 5))
avg(d)
print(avg(d))
avg(d, end=3)
print(avg(d, end=3))   
# git 사용법

"""
git 다운후 환경설정

1. git config --global user.name "your_name"
2. git config --global user.email "your_email" (github가입email)
3. git config --list (환경설정이 잘됬는지 확인 user name 이랑 user email 확인 )
끝

프로젝트 올리기

1. vs code에서 터미널 클릭 --> 새터미널 클릭
2. git init (맨처음 프로젝트를 올릴때 무조건 해야됨)
3. git add . (점은 프로젝트에 있는 파일 전부다 올리겠다) 만약에 하나의 파일만 올리려면 git add 4_test_emtry.py 이렇게
4. git status (확인)
5. git commit -m "first commit" (히스토리 만들기)
6. git remote add origin git@github.com:legobitna/first-foodmaker.git(여기 repo에 내소스코드를 보낸다 즉 git과 내컴터 연결)
7. git remote -v 로 연결고리 확인(선택사항)
8. git push origin master로 보내기
"""

#코드 수정후 git에 올리는 순서(추가 하는 작업에는 git init이 필요없다)
#1. git add .
#2. git status 로 확인
#3. git commit -m "second commit" (히스토리만들기)
#4. git push oringin master (git repo로 보내기)