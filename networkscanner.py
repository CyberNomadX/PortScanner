from socket import *
import time
startTime = time.time()

#TODO Debug code for user input. 
if __name__ == '__main__':
    target = input('Enter the host to be scanned:')
    t_IP = gethostbyname(target)
    print ('Starting scan on host ', t_IP)

    for i in range(50,500):
        s = socket(AF_INET, SOCK_STREAM)

        conn = s.connect_ex((t_IP, i))
        if(conn == 0) :
            print('Port %d: Open' % (i,))
        s.close()
print('Time taken: ', time.time() - startTime)