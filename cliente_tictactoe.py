import socket
import time
MAXBYTES = 65535
host,port = ("127.0.0.1", 55000)
def main ():
    
    sock = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

    while True:

        def print_matriz(matriz):
            for i in range(3):
                for j in range(3):
                    current = "_"
                    if matriz[i][j] == 1:
                        current = "X"
                    elif matriz[i][j] == 2:
                        current = "O"
                    print(current, end = "\t")
                print("")

        def iniciar_jogada():
            try:
                sock.connect((host, port))
                print("Connected to :", host, ":", port)
                inicar_jogo()
                sock.close()
            except socket.error as e:
                print("Socket conexão recusada:", e) 

        def inicar_jogo():
            receber = sock.recv(2048 * 10)
            print(receber.decode())

            while True:
                try: 
                    recvData = sock.recv(2048 * 10)
                    recvDataDecode = recvData.decode()

                    if recvDataDecode == "Input":
                        failed = 1
                        while failed:
                            try:
                                x = int(input("Enter the x coordinate:"))
                                y = int(input("Enter the y coordinate:"))
                                coordinates = str(x)+"," + str(y)
                                sock.send(coordinates.encode())
                                failed = 0
                            except:
                                print("tente novamente")
                        

                    elif recvDataDecode == "Error":
                        print("tente novamente")
                    
                    elif  recvDataDecode == "matriz":
                        print(recvDataDecode)
                        matrizRecv = sock.recv(2048 * 100)
                        matrizRecvDecoded = matrizRecv.decode("utf-8")
                        print_matriz(eval(matrizRecvDecoded))

                    elif recvDataDecode == "":
                        time.sleep(10)
                        break

                    else:
                        print(recvDataDecode)
                except KeyboardInterrupt:
                    print("\nKeyboard Interrupt")
                    time.sleep(1)
                    break

        iniciar_jogada()




    sock.close()

    return 0

if __name__ == '__main__':
    main()