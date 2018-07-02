import pexpect


class CiscoSfConnect:

    def __init__(self, ip_device, login, password, enable=None):
        self._ip_device = ip_device
        self._login = login
        self._password = password
        self._t = None
        self._enable = enable
        self._connect_cisco_sf()

    def _connect_cisco_sf(self):
        self._t = pexpect.spawn('ssh {}@{}'.format(self._login, self._ip_device), timeout=120)
        i = self._t.expect([pexpect.TIMEOUT, pexpect.EOF, 'User Name:', '[Pp]assword:', '\(yes\/no\)'])
        if i == 0:
            print("* {} - not available".format(self._ip_device))
            return False
        elif i == 1:
            print("* {} - You need to clean the ssh key".format(self._ip_device))
            return False
        if i == 4:
            self._t.sendline("yes")
            i = self._t.expect(['User Name:', '[Pp]assword'])

        if i == 0 or i == 2:
            self._t.sendline(self._login)
            i = self._t.expect(['[Pp]assword:', '>', '#'])
            self._t.sendline(self._password)
        i = self._t.expect(['[Pp]assword', '>', '#', pexpect.exceptions.EOF])
        if i == 3:
            print("Exception")
            return False
        if i == 0:
            print("Incorrect password!")
            if i == 0:
                print("I unknown password")
                return False
        if i == 1:
            self._t.sendline("enable")
            if self._t.expect(['[Pp]assword', '#']) == 0:
                self._t.sendline(self._enable)
                if self._t.expect(['[Pp]assword', '#']) == 0:
                    print("I do not know ebnale password")
                    return False
        self._t.sendline('terminal datadump')
        self._t.expect('#')

    def send_cisco_sf(self, command, show=False):
        out = self._command_send_expect(command)
        if show is True:
            print(out)
        return out

    def _command_send_expect(self, command):
        self._t.sendline(command)
        i = self._t.expect(['#', '\(Y\/N\)', '<.+>'])
        if i == 1:
            self._t.sendline('y')
            self._t.expect('#')
        lines = str(self._t.before)
        lines = lines.replace('\\r\\n\\r\\n', '\\r\\n').replace('\\r\\n', '\n').replace('\\r', '')
        arr = lines.split('\n')
        arr[0] = command
        arr.pop(-1)
        lines = '\n'.join(arr)
        return lines



