# 자동 주문 시스템 만들기

print('Good morning. Nice to meet you.')
print('Where are you from?')
print('Please select a number : ')

choiceNumber = int(input('1. 대한민국 2.USA 3.中国'))

if choiceNumber == 1:
    print('주문하시겠어요?')

elif choiceNumber == 2:
    print('Would you like to order?')

elif choiceNumber == 3:
    print('您要点菜吗？')

else:
    print('Would you like to order?')