$password = '76492d1116743f0423413b16050a5345MgB8AEEAYQBNAHgAZQAxAFEAVABIAEEAcABtAE4ATgBVAFoAMwBOAFIAagBIAGcAPQA9AHwAZAAyADYAMgA2ADgAMwBlADcANAA3ADIAOQA1ADIAMwA0ADMAMwBlADIAOABmADIAZABlAGMAMQBiAGMANgBjADYANAA4ADQAZgAwADAANwA1AGUAMgBlADYAMwA4AGEAZgA1AGQAYgA5ADIAMgBkAGIAYgA5AGEAMQAyADYAOAA='
$key = (3,4,2,3,56,34,254,222,205,34,2,23,42,64,33,223,1,34,2,7,6,5,35,12)

$marshal = [System.Runtime.InteropServices.Marshal]

# Take our encrypted string and convert it to a SecureString
$sstr = ConvertTo-SecureString -String $password -Key $key

# Convert our SecureString to a Binary String
# Return a pointer to memory where string is located
$ptr = $marshal::SecureStringToBSTR( $sstr )

# Allocates a new String and copies content of memory where that Binary String is
# Returns a plain String object we can output to the screen
$bstr = $marshal::PtrToStringBSTR( $ptr )

echo $bstr
