x = 0
while x < 3 :
	p = input('請輸入密碼:')
	if p == '123' :
		print('登入成功')
		break
	else :
		x = x + 1 
		y = 3 - x
		print('登入失敗，剩下', y, '次機會')
