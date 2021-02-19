import socket

if __name__ == '__main__':
    # 내부 Host
    internal_host = socket.gethostname()
    print(f'socket.gethostname() :  {internal_host}')
    internal_ip = socket.gethostbyname(internal_host)
    print(f' 내부 IP : {internal_ip}')

    # 외부 Host
    external_host = socket.getfqdn()
    print(f'socket.getfqdn() : {external_host}')
    external_ip = socket.gethostbyname(external_host)
    print(f' 외부 IP : {external_ip}')

    # 서버 Host
    external_host_dalock = socket.getfqdn("www.dalock.kr")
    print(f' dalcok 외부 Host : {external_host_dalock}')
    external_Ip_dalock = socket.gethostbyname(external_host_dalock)
    print(f' dalcok 외부 Host : {external_Ip_dalock}')

    if external_Ip_dalock == external_ip:
        print('IP 같음')
    else:
        print('IP 다름')
