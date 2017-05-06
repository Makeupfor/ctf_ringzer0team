# I lost my password - Challenge 51

The groups.xml contains the encrypted password: `"PCXrmCkYWyRRx3bf+zqEydW9/trbFToMDx6fAvmeCDw"`

``` xml
<?xml version="1.0" encoding="utf-8"?>
<Groups clsid="{3125E937-EB16-4b4c-9934-544FC6D24D26}">
  <User clsid="{DF5F1855-51E5-4d24-8B1A-D9BDE98BA1D1}" name="Administrator (built-in)" image="1" changed="2014-02-06 19:33:28" uid="{C73C0939-38FB-4287-AC48-478F614F5EF7}" userContext="0" removePolicy="0">
    <Properties action="R" fullName="Administrator" description="Administrator" cpassword="PCXrmCkYWyRRx3bf+zqEydW9/trbFToMDx6fAvmeCDw" changeLogon="0" noChange="0" neverExpires="1" acctDisabled="0" subAuthority="" userName="Administrator (built-in)"/>
  </User>
</Groups>
```

Let's use gpp-decrypt to decrypt the password, easy!

```
root@kali:~# gpp-decrypt PCXrmCkYWyRRx3bf+zqEydW9/trbFToMDx6fAvmeCDw
LocalRoot!
```
