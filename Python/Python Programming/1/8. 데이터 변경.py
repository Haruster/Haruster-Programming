# 데이터 변경
# var1과 var2는 전혀 다른 방이며 서로 영향을 끼치지 않는다.
# var2에 var1의 데이터를 복사한 후 var1의 데이터를 변경하면 var1은 변경되지만 var2는 변경되지 않는 것을 확인할 수 있다.
var1 = 123
var2 = var1

var1 = 321

print(var1)

print(var2)