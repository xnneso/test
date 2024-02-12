def main(input: str):
    arr = input.split(' ')
    if len(arr) != 3:
        return Exception('Неверный формат данных')
    try:
        a = int(arr[0])
        b = int(arr[2])
    except:
        return Exception('Данные должны быть числами')
    if 0 < a < 11 and 0 < b < 11:
        operation = {
            '+': a+b,
            '-': a-b,
            '*': a*b,
            '/': a//b
        }
        return operation[arr[1]]
    else:
        return Exception('Неверный диапазон')
    
    
print(main(input()))
