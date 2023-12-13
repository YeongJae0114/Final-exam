# <오픈소스프로그래밍 기말 프로젝트>
#
# ● 아래의 코드를 수정 혹은 프로그래밍하여 문제를 해결하시오.
# ● 문제의 점수는 각각 표시되며, 부분점수가 존재합니다.
#
# 학번 : 20191914 이름 : 이영재

import os
import time

# Q.1 10점
#
# 문자열 my_string과 target이 매개변수로 주어질 때,
# target이 문자열 my_string의 부분 문자열이라면 1을,
# 아니라면 0을 return 하는 solution 함수를 작성하시오.
#
# 제한사항
# 1 ≤ my_string 의 길이 ≤ 100
# my_string 은 영소문자로만 이루어져 있습니다. 
# 1 ≤ target 의 길이 ≤ 100
# target 은 영소문자로만 이루어져 있습니다.


def solution(my_string, target):
    # target 문자열이 my_strung에 포함되지 않는다면 다음 문장 실행
    if target not in my_string:
       # 부분문자열이 아니라면 answer = 0
        answer = 0
    else:  # 반대의 경우 다음 문장 실행
        # 부분문자열이라면 answer = 1
        answer = 1

    return answer


#print(solution('I love python', 'python'))
#print(solution('I love python', 'Java'))


# Q.2 10점
#
# 모스부호 해독 프로그램 만들기
# 문자열 letter 가 매개변수로 주어질 때,
# letter 영어 소문자로 바꾼 문자열을 return 하는
# solution 함수를 완성하시오.
#
# 제한사항
# 1 ≤ letter 의 길이 ≤ 1,000
# letter 의 모스부호는 공백으로 나누어져 있습니다.
# letter 에 공백은 연속으로 두 개 이상 존재하지 않습니다.
#
# letter = 여러분의 좌우명 또는 인상 깊었던 말을 쓰시오.


def solution(letter):
    ## 모스부호 딕셔너리
    morse = { 
    '.-':'a','-...':'b','-.-.':'c','-..':'d','.':'e','..-.':'f',
    '--.':'g','....':'h','..':'i','.---':'j','-.-':'k','.-..':'l',
    '--':'m','-.':'n','---':'o','.--.':'p','--.-':'q','.-.':'r',
    '...':'s','-':'t','..-':'u','...-':'v','.--':'w','-..-':'x',
    '-.--':'y','--..':'z'
    }

    # 공백을 기준으로 문자열을 나누기
    letter = letter.split()
    # 정답을 저장할 문자열
    answer = ""

    for mos in letter:  # 입력 받은 문자열(나눈상태)을 반복해서 모스부호 딕셔너리와 비교
        # 딕셔너리의 key값 value값에 접근한다.
        for key, value in morse.items():   
            # 입력한 letter를 하나씩 key와 비교
            if mos == key:
                answer += value  # 문자열에 알파벳 추가
    return answer # 정답을 리턴

# 내 좌우명 lovemyself
print(solution('.-.. --- ...- . -- -.-- ... . .-.. ..-.'))


# Q.3 10점
#
# 행성의 나이를 알파벳으로 표현할 때,
# a는 0, b는 1, ..., j는 9
# 예를 들어 cd는 23살, fb는 51살입니다.
# age가 매개변수로 주어질 때
# PROGEAMMER-857식 나이를 return 하도록
# solution 함수를 완성하시오.
#
# 제한사항
# age는 자연수입니다.
# age ≤ 1,000
# PROGRAMMERS-857 행성은 알파벳 소문자만 사용합니다.


def solution(age):
    # 자릿수 별로 나눠 list 형식으로 저장  ex)[1,2,3]
    age = list(map(int, str(age)))
    # 아스키코드 10진수 : a ~ j -> 97 ~ 106
    
    answer = "" # 변환한 행성의 나이를 저장할 문자열
    for i in age:
        # 변환할 숫자에 아스키 코드 값을 더해서 다시 문자로 변환
        answer += chr(i + 97)
    return answer

# print(solution(100))


# Q.4 10점
#
# x축과 y축으로 이루어진 2차원 직교 좌표계에 중심이 원점인
# 서로 다른 크기의 원이 두 개 주어집니다.
# 반지름을 나타내는 두 정수 r1, r2가 매개변수로 주어질 때,
# 두 원 사이의 공간에 x좌표와 y좌표가 모두 정수인 점의 개수를
# return하도록 solution 함수를 완성해주세요.
# ※ 각 원 위의 점도 포함하여 셉니다.
#
# 제한사항
# 1 ≤ r1 < r2 ≤ 1,000,000


import math

def solution(r1, r2):
    answer = 0
    # 바깥쪽 원의 x좌표를 나타내는 i
    for i in range(1, r2 + 1):
        # 원의 방정식을 이용해 y값을 찾음
        y_r2 = math.sqrt(r2**2 - i**2) # y_r2 = (r2**2 - i**2)**(0.5)

        if i <= r1: # r1보다 큰 범위만 계산
             # 원의 방정식을 이용해 y값을 찾음
            y_r1 = math.sqrt(r1**2 - i**2) # y_r1 = (r1**2 - i**2)**(0.5)
        else:
            y_r1 = 0
        # 큰 원인 y_r2를 내림, 작은 원 y_r1 올림 (길이로 정수형 좌표 개수를 구하기 위해)
        answer += math.floor(y_r2) - math.ceil(y_r1) + 1 # floor : 내림, ceil : 올림
    return answer * 4

#print(solution(2,3))

#
# Q.5 10점
#
# 0 또는 양의 정수가 주어졌을 때,
# 정수를 이어 붙여 만들 수 있는 가장 큰 수를 알아내 주세요.
#
# 예를 들어, 주어진 정수가 [6, 10, 2]라면
# [6102, 6210, 1062, 1026, 2610, 2106]를 만들 수 있고,
# 이중 가장 큰 수는 6210입니다.
#
# 0 또는 양의 정수가 담긴 배열 numbers가 매개변수로 주어질 때,
# 순서를 재배치하여 만들 수 있는 가장 큰 수를 문자열로 바꾸어
# return 하도록 solution 함수를 작성해주세요.
#
# 제한사항
# numbers의 길이는 1 이상 100,000 이하입니다.
# numbers의 원소는 0 이상 1,000 이하입니다.
# 정답이 너무 클 수 있으니 문자열로 바꾸어 return 합니다.
#
# numbers = [8, 30, 17, 2, 23]


def solution(numbers):
    # 정수형 numbers를 문자열로 바꾸고 list형태로 저장
    list_num = list(map(str,numbers)) 
    # key 를 통하여 정렬할 기준을 정할 수 있다.
    # reverse 가 True이면 내림차순
    # 익명함수를 지칭한다. 함수 선언
    list_num.sort(key = lambda x : x*3,reverse = True) # x를 3번 반복한 문자열을 기준으로 정렬
    
    answer = ''
    for i in list_num:     
        answer += i
    
    # return answer으로 바로 반환 했을 떄 numbers = [0,0]일 때 가장 큰수는 00을 반환한다.(오류)    
    # return answer
    return str(int(answer))

#print(solution([0,0]))
#print(solution([3, 30, 34, 5, 9]))
