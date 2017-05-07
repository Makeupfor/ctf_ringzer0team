# Admin panel - Challenge 104

The HTTP redirection on this page is insecure

Let's use Burp Suite to manipulate the HTTP response codes and change that 302 to a 200

Enable interception on the proxy in Burp Suite then set up your browser to use the local proxy

![burp1](burp1.png)

Send your POST request to the challenge form, then enable interception of the response

![burp2](burp2.png)

Change the 302 to a 200, then forward the request back

![burp3](burp3.png)

![burp4](burp4.png)

We now get a new page with an hidden field in the form

![burp5](burp5.png)

We'll do the same thing, swap the 302 for 200 and get the flag

![flag](flag.png)
