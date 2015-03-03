import socket
import sha, itertools

host='127.0.0.1'
port=80

size=4096

letters = [' ', '!', '"', '#', '$', '%', '&', '\'', '(', ')',
        '*', '+', ',', '-', '.', '/', '0', '1', '2', '3', '4', '5',
        '6', '7', '8', '9', ':', ';', '<', '=', '>', '?', '@', 'A',
        'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M',
        'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y',
        'Z', '[', '\\', ']', '^', '_', '`', 'a', 'b', 'c', 'd', 'e',
        'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q',
        'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', '{', '|', '}',
        '~']

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((host,port))
prefix = s.recv(size)
print "prefix received: "+prefix

for c in itertools.combinations_with_replacement(letters, 5):
    end = "".join(c)
    if sha.new(prefix+end).digest().endswith("\xFF\xFF\xFF"):
        response = prefix+end
        break

s.sendall(response)
print "sent prefix response: "+response

s.sendall('therealmessage')

data = s.recv(size)
print "received: "+data

s.close()
