import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

s.bind(("localhost",1234))

s.listen(1)

con,addr = s.accept()
print("Baglanti Aktif.")


while True:
	data = con.recv(2048).decode("utf-8")
	print(data)
