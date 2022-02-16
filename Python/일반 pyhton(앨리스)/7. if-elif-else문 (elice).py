#변수 answer에 수 1-50을 넣어봅시다.
answer = 40

#input를 통해 숫자형으로 입력을 받아서 변수 submit에 저장해봅시다.
submit = int(input())

#만약 answer보다 submit이 더 크면 "정답보다 더 큰 수를 입력했습니다."를 출력하게 한다
if answer < submit:
    print("정답보다 더 큰 수를 입력했습니다.")

#만약 answer보다 submit이 더 작으면 "정답보다 더 작은 수를 출력했습니다."를 출력하게 한다.
elif answer > submit:
    print("정답보다 더 작은 수를 입력했습니다.")

#만약 answer와 submit이 같으면 "정답!"을 출력하게 한다.
elif answer == submit:
    print("정답!")