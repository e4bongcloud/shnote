# linux standard mode
| D |               Name              |                                   Description                                   |
|:-:|:-------------------------------:|:-------------------------------------------------------------------------------:|
| 0 | Off                             | Turns off the device.                                                           |
| 1 | Single-user mode                | Mode for administrative tasks.[2][b]                                            |
| 2 | Multi-user mode                 | Does not configure network interfaces and does not export networks services.[c] |
| 3 | Multi-user mode with networking | Starts the system normally.[1]                                                  |
| 4 | Not used/user-definable         | For special purposes.                                                           |
| 5 | Full mode                       | Same as runlevel 3 + display manager.                                           |
| 6 | Reboot                          | Reboots the device.                                                             |

# UNIX 
|  ID  |                                               Description                                               |
|:----:|:-------------------------------------------------------------------------------------------------------:|
| 0    | Off                                                                                                     |
| 1    | Single-user mode, all filesystems unmounted but not root, all processes except console processes killed |
| 2    | Multi-user mode                                                                                         |
| 3    | Multi-user mode with RFS (and NFS in Release 4) filesystems exported                                    |
| 4    | Multi-user, User-definable                                                                              |
| 5    | Go to firmware                                                                                          |
| 6    | Reboot                                                                                                  |
| s, S | Identical to 1, except current terminal acts as the system console                                      |