# Sysadmin part 7 - Challenge 91

There's a bunch of /bin/monitor processes running as user root and neo. Unfortunately we can't spawn a new process ourselves to check out what it's doing.

```
neo@forensics:~$ /bin/monitor
-bash: /bin/monitor: Permission denied
```

However, because some of the processes are already running as user neo, we could read the calls that it's doing using the strace program. We can see calls to write() and we find the flag.

```
neo@forensics:~$ strace -p 31997
Process 31997 attached - interrupt to quit
restart_syscall(<... resuming interrupted call ...>


) = 0
write(4294967295, "telnet 127.0.0.1 23\n", 20) = -1 EBADF (Bad file descriptor)
write(4294967295, "user\n", 5)          = -1 EBADF (Bad file descriptor)
write(4294967295, "FLAG-a4UV***************\n", 31) = -1 EBADF (Bad file descriptor)
write(4294967295, "get-cpuinfo\n", 12)  = -1 EBADF (Bad file descriptor)
rt_sigprocmask(SIG_BLOCK, [CHLD], [], 8) = 0
rt_sigaction(SIGCHLD, NULL, {SIG_DFL, [], 0}, 8) = 0
rt_sigprocmask(SIG_SETMASK, [], NULL, 8) = 0
nanosleep({10, 0}, 0x7fffffffec20)      = 0
write(4294967295, "telnet 127.0.0.1 23\n", 20) = -1 EBADF (Bad file descriptor)
write(4294967295, "user\n", 5)          = -1 EBADF (Bad file descriptor)
write(4294967295, "FLAG-a4UV***************\n", 31) = -1 EBADF (Bad file descriptor)
write(4294967295, "get-cpuinfo\n", 12)  = -1 EBADF (Bad file descriptor)
rt_sigprocmask(SIG_BLOCK, [CHLD], [], 8) = 0
rt_sigaction(SIGCHLD, NULL, {SIG_DFL, [], 0}, 8) = 0
rt_sigprocmask(SIG_SETMASK, [], NULL, 8) = 0
nanosleep({10, 0}, 0x7fffffffec20)      = 0
write(4294967295, "telnet 127.0.0.1 23\n", 20) = -1 EBADF (Bad file descriptor)
write(4294967295, "user\n", 5)          = -1 EBADF (Bad file descriptor)
write(4294967295, "FLAG-a4UV***************\n", 31) = -1 EBADF (Bad file descriptor)
write(4294967295, "get-cpuinfo\n", 12)  = -1 EBADF (Bad file descriptor)
rt_sigprocmask(SIG_BLOCK, [CHLD], [], 8) = 0
rt_sigaction(SIGCHLD, NULL, {SIG_DFL, [], 0}, 8) = 0
rt_sigprocmask(SIG_SETMASK, [], NULL, 8) = 0
nanosleep({10, 0}, ^C <unfinished ...>
Process 31997 detached
neo@forensics:~$
```
