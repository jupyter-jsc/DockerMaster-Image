import subprocess, sys 
import argparse

hostname = "DockerMaster"
user = 'tunnel'
host = 'zam10183.zam.kfa-juelich.de'
key = '~/.jupyter@jsc/j4j_docker'
port = 25488
hubport = 8000
hubname = 'j4j_proxy'
debug = True

def start():
    ret, pid = status()
    if ret == 1:
        cmd_start = ['ssh', '-p', '2222', '-i', key, '-oUserKnownHostsFile=/dev/null', '-oServerAliveInterval=60', '-oServerAliveInterval=5', '-oExitOnForwardFailure=yes', '-oStrictHostKeyChecking=no', '-L{}:{}:{}:{}'.format(hostname, port, hubname, hubport), '{}@{}'.format(user, host), '-f', '-N']
        p_start = subprocess.Popen(cmd_start)
        return True
    else:
        return False
 
def status():
    cmd_status1 = ['ps', 'aux']
    cmd_status2 = ['grep', '[L]{}:{}:{}:{}'.format(hostname, port, hubname, hubport)]
    p_status1 = subprocess.Popen(cmd_status1, stdout=subprocess.PIPE)
    p_status2 = subprocess.Popen(cmd_status2, stdin=p_status1.stdout, stdout=subprocess.PIPE)
    p_status1.stdout.close()
    out, err = p_status2.communicate()
    ret = p_status2.returncode
    if ret == 0:
        return ret, out.split()[1]
    else:
        return ret, ''

def stop():
    ret, pid = status()
    if ret == 0:
        cmd_stop1 = ['kill', '{}'.format(pid)]
        p_stop1 = subprocess.Popen(cmd_stop1, stdout=subprocess.PIPE)
        out, err = p_stop1.communicate()
        return True
    else:
        return False

def ret():
    if status()[0] == 0:
        return True
    else:
        return False

# Main
if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='BuildUp Tunnel')
    parser.add_argument('action', type=str, nargs=1, help='...')
    args = parser.parse_args()
    if args.action[0] == '0aca3fdbc4023500b5e2bb254f95f55932785e6dc33c4f12011f25f3d47403875343a985c07de18e6a568c9fcc04ef8a1400cf2e3118dfb28ace4b58ead3c962':
        start()
    elif args.action[0] == 'deb7ef7b249b1df1352525c37b8bbe3d1f6c8f36c6993e4dd6a7f87de38b8ac3dec37ee87d53024fdfa0aeeea7fc43a6147cb6df42431cc1ee66028838bfac39':
        stop()
    elif args.action[0] == '2eca457db671091b7ac46ba48bea07d541f379523a0bdf232bc2261198bbe9289774a9ba7d0d1cf69a3c235762e266927158e8a23f0f1a3e50acc529948df01d':
        pass
    else:
        sys.exit(255)
    if ret():
        sys.exit(217)
    else:
        sys.exit(218)
