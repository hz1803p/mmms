import time
print("_____正在创建User模型类")
time.sleep(2)
with open('models.py','a+',encoding='utf-8') as f:
	code ='''
	class UserModel:
		def __init__(self,name,age):
			self.name=name
			self.age=age
	'''
	f.write(code)
print("保存成功")
