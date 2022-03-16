import time
import os

# Список с неопределенной вложенностью для проверки:
nested_list = [
		['a', ['g','b',['ssss']], 'c'],
		['d', 'e', 'f', 'h', False],
		[1, 2, None]
	]

# Итератор
class FlatIterator:
	def __init__(self, data_list):
		self.list = data_list

	def __iter__(self):
		self.cursor = -1
		
		@decorator(path)
		def flatlist(data):
			lst = []
			for values in data:
				if type(values) == list:
					lst.extend(flatlist(values))
				else:
					lst.append(values)
			return lst
		self.flat_list = flatlist(self.list)
		return self

	def __next__(self):
		self.cursor += 1
		if self.cursor == len(self.flat_list):
			raise StopIteration
		return self.flat_list[self.cursor]

# Декоратор
path = '/Users/boksha/PycharmProjects/decorator/log/'
def decorator(path):
	def _decorator(old_function):
		def new_function(*args,**kwargs):
			os.makedirs(path,  exist_ok=True)
			with open(path+'log.txt', 'at') as f:
				f.write(f'{time.ctime()}: Вызвана функция {old_function.__name__} с аргументами {args} {kwargs} \n')
			result = old_function(*args,**kwargs)
			return result
		return new_function
	return _decorator

if __name__ == "__main__":
	flat_list = [item for item in FlatIterator(nested_list)]
	print(flat_list)
