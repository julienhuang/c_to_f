#溫度轉換
temp_unit = input('請選擇溫度單位(攝氏=C / 華氏=F)')
if temp_unit == 'C':
	print('您希望將攝氏溫度轉為華氏溫度')
	temp_c = float(input('請輸入攝氏溫度=___度'))
	temp_w = (temp_c * 9) / 5 + 32
	print('換算成華氏溫度為：', temp_w, '度')
if temp_unit == 'F':
	print('您希望將華氏溫度轉為攝氏溫度')
	temp_w = float(input('請輸入華氏溫度=___度'))
	temp_c = ((temp_w - 32) * 5) / 9
	print('換算成攝氏溫度為：', temp_c, '度')
