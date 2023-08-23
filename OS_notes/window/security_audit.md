
# Get-EventLog 
시스템 로그, 보안 로그 등 다양한 이벤트 로그를 조회할 수 있는 명령어입니다.
``` powershell
PS C:\Users\dbstj> Get-EventLog -LogName Security

   Index Time          EntryType   Source                 InstanceID Message
   ----- ----          ---------   ------                 ---------- -------
  517450 2월 19 03:02  SuccessAud… Microsoft-Windows-S…         4672 특수 권한을 새 로그온에 할당했…
  517449 2월 19 03:02  SuccessAud… Microsoft-Windows-S…         4624 계정이 성공적으로 로그온되었습…
  517448 2월 19 02:33  SuccessAud… Microsoft-Windows-S…         4672 특수 권한을 새 로그온에 할당했…
  517447 2월 19 02:33  SuccessAud… Microsoft-Windows-S…         4624 계정이 성공적으로 로그온되었습…
  517446 2월 19 02:25  SuccessAud… Microsoft-Windows-S…         4672 특수 권한을 새 로그온에 할당했…
  517445 2월 19 02:25  SuccessAud… Microsoft-Windows-S…         4624 계정이 성공적으로 로그온되었습…
  517444 2월 19 02:15  SuccessAud… Microsoft-Windows-S…         4672 특수 권한을 새 로그온에 할당했…
  517443 2월 19 02:15  SuccessAud… Microsoft-Windows-S…         4624 계정이 성공적으로 로그온되었습…
  517442 2월 19 02:04  SuccessAud… Microsoft-Windows-S…         4672 특수 권한을 새 로그온에 할당했…
  517441 2월 19 02:04  SuccessAud… Microsoft-Windows-S…         4624 계정이 성공적으로 로그온되었습…
  517440 2월 19 01:57  SuccessAud… Microsoft-Windows-S…         4672 특수 권한을 새 로그온에 할당했…
  517439 2월 19 01:57  SuccessAud… Microsoft-Windows-S…         4624 계정이 성공적으로 로그온되었습…
  517438 2월 19 01:57  SuccessAud… Microsoft-Windows-S…         4634 계정이 로그오프되었습니다.…
  517437 2월 19 01:55  SuccessAud… Microsoft-Windows-S…         4672 특수 권한을 새 로그온에 할당했…
  517436 2월 19 01:55  SuccessAud… Microsoft-Windows-S…         4624 계정이 성공적으로 로그온되었습…
  517435 2월 19 01:55  SuccessAud… Microsoft-Windows-S…         4672 특수 권한을 새 로그온에 할당했…
  517434 2월 19 01:55  SuccessAud… Microsoft-Windows-S…         4624 계정이 성공적으로 로그온되었습…
  517433 2월 19 01:55  SuccessAud… Microsoft-Windows-S…         4799 보안 기능이 설정된 로컬 구성원…
  517432 2월 19 01:55  SuccessAud… Microsoft-Windows-S…         4799 보안 기능이 설정된 로컬 구성원…
  517431 2월 19 01:55  SuccessAud… Microsoft-Windows-S…         4672 특수 권한을 새 로그온에 할당했…
  517430 2월 19 01:55  SuccessAud… Microsoft-Windows-S…         4624 계정이 성공적으로 로그온되었습…
``` 

# Get-Process 
현재 실행 중인 프로세스를 조회할 수 있는 명령어입니다.  
명령어를 사용하면, 프로세스 이름, 경로, 명령줄 인수 등의 정보를 조회할 수 있습니다.
``` powershell 
PS C:\Users\dbstj> Get-Process | Select-Object Name, Path, CommandLine

Name                 Path
----                 ----
AdobeIPCBroker       C:\Program Files (x86)\Common Files\Adobe\Adobe Desktop Common\IPCBox\AdobeIPCB…
AggregatorHost       C:\WINDOWS\System32\AggregatorHost.exe
ApplicationFrameHost C:\WINDOWS\system32\ApplicationFrameHost.exe
audiodg              C:\WINDOWS\system32\AUDIODG.EXE
CCXProcess           C:\Program Files\Adobe\Adobe Creative Cloud Experience\CCXProcess.exe
CExecSvc             C:\WINDOWS\system32\cexecsvc.exe
chrome               C:\Program Files\Google\Chrome\Application\chrome.exe
chrome               C:\Program Files\Google\Chrome\Application\chrome.exe
``` 

# Get-Service
현재 실행 중인 서비스를 조회할 수 있는 명령어입니다.   
명령어를 사용하면, 현재 중지된 서비스 목록을 조회할 수 있습니다.

``` powershell
PS C:\Users\dbstj> Get-Service | Where-Object {$_.Status -eq 'Stopped'}

Status   Name               DisplayName
------   ----               -----------
Stopped  AJRouter           AllJoyn Router Service
Stopped  ALG                Application Layer Gateway Service
Stopped  AppIDSvc           Application Identity
```

# Get-NetFirewallRule 
방화벽 규칙을 조회할 수 있는 명령어입니다.   
``` powershell 
PS C:\Users\dbstj> Get-NetFirewallProfile -Name Public

Name                            : Public
Enabled                         : True
DefaultInboundAction            : NotConfigured
DefaultOutboundAction           : NotConfigured
AllowInboundRules               : NotConfigured
AllowLocalFirewallRules         : NotConfigured
AllowLocalIPsecRules            : NotConfigured
AllowUserApps                   : NotConfigured
AllowUserPorts                  : NotConfigured
AllowUnicastResponseToMulticast : NotConfigured
NotifyOnListen                  : True
EnableStealthModeForIPsec       : NotConfigured
LogFileName                     : %systemroot%\system32\LogFiles\Firewall\pfirewall.log
LogMaxSizeKilobytes             : 4096
LogAllowed                      : NotConfigured
LogBlocked                      : NotConfigured
LogIgnored                      : NotConfigured
DisabledInterfaceAliases        : {NotConfigured}
```

# Get-Acl 
파일이나 폴더의 액세스 권한 정보를 조회할 수 있는 명령어입니다.   
명령어를 사용하면, cmd.exe 파일의 액세스 권한 정보를 조회할 수 있습니다.

``` powershell 
Get-Acl C:\Windows\System32\cmd.exe

    Directory: C:\Windows\System32

Path    Owner                       Access
----    -----                       ------
cmd.exe NT SERVICE\TrustedInstaller NT AUTHORITY\SYSTEM Allow  ReadAndExecute, Synchronize…
```