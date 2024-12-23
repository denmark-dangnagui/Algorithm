# Q. 정수를 입력 했을 때, 그 정수 이하의 소수를 모두 반환하시오.
#
# 소수는 자신보다 작은 두 개의 자연수를 곱하여 만들 수 없는 1보다 큰 자연수이다.
# 소수는 자기 자신과 1외 에는 아무것도 나눌 수 없다.
# 소수는 N의 제곱근보다 크지 않은 어떤 소수로도 나누어 떨어지지 않는다.

for x in [1,2,3,4]:
    print(x)
    if x == 4:
        break
else:
    print("for else 문은 for문이 다 끝까지 다 돌았을 때 else 부분에 있는 코드가 작동된다.")
# for else 문은 우리가 입력된 배열에 특정 값이 존재하느냐 아니냐에 따라서 행동을 하고 싶은
# 경우에 사용하면된다. 이런 소수문제처럼.

input = 20
def find_prime_list_under_number(number):
    prime_list = []

    for n in range(2,number + 1):
        for i in prime_list:
            if i * i <= n and n % i == 0:
                break
        else:
            prime_list.append(n)

    return prime_list

def find_prime_list_under_number_ltm_1st(number):
    array = []
    for num1 in range(2,number):
        cnt = 0
        if num1 != 1:
            temp = num1 - 1
            for num2 in range(temp):
                if temp != 1:
                    temp2 = temp - 1
                    for num3 in range(temp2):
                        if num2 * num3 == num1:
                            cnt += 1
        if cnt == 0:
            array.append(num1)


    return array


# 소수는 자기 자신과 1외 에는 아무것도 나눌 수 없다.
def find_prime_list_under_number_ltm_2nd(number):
    array = []
    for num in range(2,number+1):
        for num2 in range(2,num):
            if num % num2 == 0:
                break
        else:
            array.append(num)


    return array

result = find_prime_list_under_number(input)
# result = find_prime_list_under_number_ltm_2nd(input)
print(result)