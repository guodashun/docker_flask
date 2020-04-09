import os, sys

def pic_list():
	path = "./static/data/ch"
	file_list = []

	for root, directions, files in os.walk(path):
		for filename in files:
			if filename.endswith(".png"):
				file_list.append(filename)

	return file_list

def song_list():
	path = "./static/data/ch"
	file_list = []

	for root, directions, files in os.walk(path):
		for filename in files:
			if filename.endswith(".mp3"):
				file_list.append(filename)

	return file_list

def text_list():
	path = "./static/data/ch"
	file_list = []

	for root, directions, files in os.walk(path):
		for filename in files:
			if filename.endswith(".txt"):
				filepath = os.path.join(root, filename)
				f = open(filepath, "r", encoding='gbk')
				file_list.append(f.readline())
	return file_list

#just for test
if __name__ == '__main__':
	a = text_list()
	for b in a:
		print(b)