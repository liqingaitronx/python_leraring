src = open("1.jpg","rb")#把图片变成0101的二进制
tar = open("2.jpg", "wb")
tar.write(src.read())
src.close()
tar.close()