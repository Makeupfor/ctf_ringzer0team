# Who I am? - Challenge 160

The hint is 'website'.

Let's do a lookup on the domainf or TXT records:

```
; <<>> DiG 9.8.3-P1 <<>> txt ringzer0team.com
;; global options: +cmd
;; Got answer:
;; ->>HEADER<<- opcode: QUERY, status: NOERROR, id: 61254
;; flags: qr rd ra; QUERY: 1, ANSWER: 2, AUTHORITY: 0, ADDITIONAL: 0

;; QUESTION SECTION:
;ringzer0team.com.		IN	TXT

;; ANSWER SECTION:
ringzer0team.com.	3600	IN	TXT	"FLAG-305l9RR202HG695t6Y8ZU77xyq"
ringzer0team.com.	3600	IN	TXT	"uid=0(root) gid=0(root) groups=0(root)"

;; Query time: 58 msec
;; SERVER: 198.235.69.156#53(198.235.69.156)
;; WHEN: Thu May 11 15:14:49 2017
;; MSG SIZE  rcvd: 129
```
