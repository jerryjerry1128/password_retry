password = 'a123456'
n = 3
while n > 0:
    if input('請輸入密碼: ') == password:
        print('登入成功')
        break
    else:
        n-=1
        if n != 0:
            print('密碼錯誤! 還有',n,'次機會')
        