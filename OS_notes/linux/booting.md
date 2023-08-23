부팅과정을 크게 5가지로 분류하면 아래와 같다.
0 단계 : 시스템 전원 공급

1. BIOS(Basic Input/Output System) 단계(Firmware 단계)
2. 부트 로드(Boot Loader) 단계
3. 커널(Kernel) 단계
4. Init 단계

# 0단계 : 시스템 전원 공급

메인보드의 ROM-BIOS에 있는 BIOS프로그램을 자동실행 한다.
BIOS 프로그램은 전원공급과 함께 메모리의 특정번지(예:FFFF0H)에 자동 로드된다.
CPU는 전원공급과 함께 특정번지(예:FFFF0H)의 BIOS프로그램(명령들)을 자동실행 한다.
 

# 1단계 : BIOS 단계

자체진단기능(POST(Power On Self Test))
CMOS검사, CPU, MEMORY, 그래픽카드, 키보드, 마우스등 각종 장치들의 이상 유무를 검사하고 이들 장치(하드웨어들)을 초기화시킨다.
부팅매체검색과 부트로더 실행
POST과정이 이상 없이 진행 완료되면 검색된 부팅매체(하드디스크, CD-ROM, 플로피 디스크등)에서 부트로더(예:GRUB, LILO)를 불러들인다.
즉, 예를들어 하드디스크가 부팅매체로 선택되었다면 하드디스크의 부팅파티션에 있는 0번섹터 (대부분 MBR이라고도 함)에 있는 부트로더(Boot Loader, 즉, GRUB)을 읽어 들이게 된다.
부트로더(GRUB)가 메모리에 적재되면 BIOS는 종료되고, 시스템 제어권은 부트로더(GRUB)이 갖게 된다.
 
# 2단계 : 부트로드 단계

부트로더 설명
리눅스에서 사용하는 부트로더는 LILO(Linux Loader)나 GRUB가 있다.

GRUB은 커널(kernel)이미지를 불러들이고 시스템 제어권을 커널에게 넘겨준다.

GRUB(GRand Unified Bootloader)

환경 설정 파일 : /boot/grub/grub.conf(/etc/grub.conf) 

실행 파일 : /sbin/grub

설정 옵션 : /boot/grub/grub.conf 
 

    timeout=5 5초 후 부팅                             /* 부팅시 타임아웃 설정    */ 

    default=0 첫 번째로 부팅                          /* 기본 부팅 레이블(예: 0) */ 

    hiddenmenu                                       /* GRUB 메뉴 숨김         */ 

    splashimage=(hd0,0)/bot/grub/splash.xpm.gz       /* splashimage 위치       */ 

    title CentOS (2.6.18-164.11.1.el5)-->            /* 타이틀                 */ 

    root (hd0,0) 하드디스크 0번에 존재함               /* root 파티션 위치       */ 

    kernel /boot/vmlinuz-2.6.18-164.11.1.el5 ro root=LABEL=/ rhgb quiet 

    -> 부트 밑에 내용으로 부팅하겠다 initrd /boot/initrd-2.6.18-164.11.1.el5.img 

    
    (RHEL 7 or CentOS 7 이상일 경우) 
    /etc/default/grub
    
    GRUB_TIMEOUT=5

    GRUB_DISTRIBUTOR="$(sed 's, release .*$,,g' /etc/system-release)"

    GRUB_DEFAULT=saved

    GRUB_DISABLE_SUBMENU=true

    GRUB_TERMINAL_OUTPUT="console"

    GRUB_CMDLINE_LINUX="crashkernel=auto rd.lvm.lv=centos/root rhgb quiet"

    수정 후 # grub2-mkconfig -o /boot/grub2/grub.cfg 명령어로 설정 적용

 

# 3단계 : 커널 단계

/etc/grub/grub.conf 파일에 의해서 커널이 메모리상에서 실행되면, 하드웨어를 점검하고 /var/log/dmesg 파일에 기록을 한다.
루트 파일시스템(/)을 읽기 전용으로 마운트 한다. 만약 마운트 실패시 “커널 패닉” 메세지를 출력한다.
커널은 swapper프로세스(PID 0번)를 호출한다.
swapper(PID 0번)는 커널이 사용할 각 장치드라이브들을 초기화하고 init프로세스(PID 1번)가 실행하게 된다.
/sbin/init프로세스가 실행되면서 /etc/inittab파일을 읽어들여서 그 내용들을 차례대로 실행한다.
 
# 4단계 : Init 프로세스 단계
init프로세스 호출 후
/sbin/init 프로세스가 실행이 되면 /etc/inittab 파일에 정의된 순서에 따라서 시스템을 초기화하기 시작한다. 즉, 로그인프롬프트가 나오는 부팅완료화면까지 init프로세스에 의해서 실행되는 내용들인 것이다