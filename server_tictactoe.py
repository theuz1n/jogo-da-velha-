import socket
import time
MAXBYTES = 65535
def main():

    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.bind(('127.0.0.1', 55000))

    s = socket.socket()
    host,port  = (("127.0.0.1",55000))
    matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]

    jogador1 = 1
    jogador2= 2

    jogaConn = list()
    jogaAddr = list()
    jogaName = list()         


    def validar_entrada(x, y, conn):
        if x > 3 or y > 3:
            print("\ntente novamente...")
            conn.send("Error".encode())
            return False
        elif matriz[x][y] != 0:
            print("\njoga ja existe tente novamente...\n")
            conn.send("Error".encode())
            return False
        return True

    def entrada(esperar_jogada):
        if esperar_jogada == jogador1:
            joga = "joga 1 turno"
            conn = jogaConn[0]
        else:
            joga = "joga segundo turno"
            conn = jogaConn[1]
        print(joga)
        envia_msg(joga)
        falhou = 1
        while falhou:
            try:
                conn.send("entrada".encode())
                data = conn.recv(2048 * 10)
                conn.settimeout(20)
                dataDecoded = data.decode().split(",")
                x = int(dataDecoded[0])
                y = int(dataDecoded[1])
                if validar_entrada(x, y, conn):
                    matriz[x][y] = esperar_jogada
                    falhou = 0  
                    envia_msg("matriz")
                    envia_msg(str(matriz))
            except:
                conn.send("Error".encode())
                print("tente novamente..")

            

    def checar_linhas():
        resultado = 0
        for i in range(3):
            if matriz[i][0] == matriz[i][1] and matriz[i][1] == matriz[i][2]:
                resultado = matriz[i][0]
                if resultado != 0:
                    break
        return resultado

    def checar_colunas():
        resultado = 0
        for i in range(3):
            if matriz[0][i] == matriz[1][i] and matriz[1][i] == matriz[2][i]:
                resultado = matriz[0][i]
                if resultado != 0:
                    break
        return resultado

    def checar_diagonal():
        resultado = 0
        if matriz[0][0] == matriz[1][1] and matriz[1][1] == matriz[2][2]:
            resultado = matriz[0][0]
        elif matriz[0][2] == matriz[1][1] and matriz[1][1] == matriz[2][0]:
            resultado = matriz[0][2]
        return resultado

    def checar_ganhador():
        resultado = 0
        resultado = checar_linhas()
        if resultado == 0:
            resultado = checar_colunas()
        if resultado == 0:
            resultado = checar_diagonal()
        return resultado

    def inicar_servidor():

        try:
            s.bind((host, port))
            print("Tic Tac Toe iniciando servidor \nbuscando portas", port)
            s.listen(2) 
            aceitarjogadas()
        except socket.error as e:
            print("Server binding error:", e)
        


    def aceitarjogadas():
        try:
            welcome = "bem vindo"
            for i in range(2):
                conn, addr = s.accept()
                conn.send(welcome.encode())
                name = conn.recv(2048 * 10).decode()

                jogaConn.append(conn)
                jogaAddr.append(addr)
                jogaName.append(name)
                print("jogar {} - {} [{}:{}]".format(i+1, name, addr[0], str(addr[1])))
                conn.send(" {}, sua vez de jogar {}".format(name, str(i+1)).encode())
            
            inicar()
            s.close()
        except socket.error as e:
            print("joga conexão recusada", e)   
        except:
            print("Error ocorrido")

    def inicar():
        resultado = 0
        i = 0
        while resultado == 0 and i < 9 :
            if (i%2 == 0):
                entrada(jogador1)
            else:
                entrada(jogador2)
            resultado = checar_ganhador()
            i = i + 1
        
        if resultado == 1:
            ultmsg = "jogador1- {} é o vencendor".format(jogaName[0])
        elif resultado == 2:
            ultmsg = "jogador2 - {}  é o vencendor".format(jogaName[1])
        else:
            ultmsg = "empate"

        envia_msg(ultmsg.encode())
        time.sleep(10)
        for conn in jogaConn:
            conn.close()
        

    def envia_msg(text):
        jogaConn[0].send(text.encode())
        jogaConn[1].send(text.encode())
        time.sleep(1)

    inicar_servidor()
if __name__ == '__main__':
    main()