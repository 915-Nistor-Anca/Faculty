#include <stdlib.h>
#include <stdio.h>
#include <netinet/ip.h>
#include <sys/socket.h>
#include <arpa/inet.h>
#include <sys/types.h>
#include <unistd.h>

int main(){
        uint16_t port = 1234;
        char address[256] = "0.0.0.0";
        int sock_fd = socket(AF_INET, SOCK_STREAM, 0);
        int backlog = 7;

        if(sock_fd == -1){
                perror("Socket error");
                return -1;
        }
        printf("Socket created successfully\n");
        struct sockaddr_in socket_address;
        socket_address.sin_family = AF_INET;
        socket_address.sin_port = htons(port);
        inet_aton(address, &socket_address.sin_addr);
        socklen_t socket_address_len = sizeof(socket_address);

        int res = bind(sock_fd, (const struct sockaddr*)&socket_address,
socket_address_len);
        if(res == -1){
                perror("Bind error");
                return -1;
        }

        printf("Binded to ip %s on port %hu\n", address, port);
        res = listen(sock_fd, backlog);
        if(res == -1){
                perror("Listen error");
                return -1;
        }
        printf("Listen succeeded\n");


        int a[11][11] ={{0, 0, 0, 2, 0, 0, 0, 0, 0, 0},
                        {0, 0, 1, 1, 1, 0, 0, 0, 0, 0},
                        {0, 0, 0, 1, 0, 0, 2, 0, 0, 0},
                        {0, 0, 0, 1, 0, 1, 1, 1, 0, 0},
                        {0, 0, 0, 0, 0, 0, 1, 0, 0, 0},
                        {0, 0, 0, 0, 0, 0, 1, 0, 0, 0},
                        {0, 2, 0, 0, 0, 0, 0, 0, 0, 0},
                        {1, 1, 1, 0, 0, 0, 0, 0, 0, 0},
                        {0, 1, 0, 0, 0, 0, 0, 0, 0, 0},
                        {0, 1, 0, 0, 0, 0, 0, 0, 0, 0}};



        int i = 0, j = 0, cont = 0;

        int ok = 1;

        char s = '0';

        while(ok) {

                struct sockaddr_in client_address;
                socklen_t client_address_len;


                int client_fd = accept(sock_fd, (struct sockaddr*)&client_address, &client_address_len);

                if(fork() == 0){

                        for(int k = 0; k<=7; k++){


                                if(client_fd == -1){
                                        perror("Accept error");
                                        continue;
                                }

                                printf("Client with ip %s and port %d connected successfully\n", inet_ntoa(client_address.sin_addr), ntohs(client_address.sin_port));

                                read(client_fd, &i, sizeof(int));
                                read(client_fd, &j, sizeof(int));

                                i = ntohl(i);
                                j = ntohl(j);

                                if(a[i][j] == 1)
                                        s = 'X';
                                else if(a[i][j] == 2) {
                                        cont++;
                                        s = 'H';
                                        a[i][j] = 0;
                                        a[i+1][j] = 0;
                                        a[i+2][j] = 0;
                                        a[i+3][j] = 0;
                                        a[i+1][j-1] = 0;
                                        a[i+1][j+1] = 0;
                                }

                                if(cont == 3)
                                        s = 'W';

                                write(client_fd, &s, sizeof(char));


                                printf("Client with ip:%s hit %d, %d\n", inet_ntoa(client_address.sin_addr), i, j);

                                if(cont == 3){
                                        ok = 0;
                                        break;
                                }


                        }
                        exit(0);

                }
                close(client_fd);

        }

        close(sock_fd);


        return 0;
}
