$a = get-wmiobject win32_process | where commandline -match GTCC| where commandline -match CheckInService.bat | select ProcessId
$b = get-wmiobject win32_process | where commandline -match PGPLM| where commandline -match CheckInService.bat | select ProcessId

if (!$a){ Write-Host "CheckInService-GTCC is Not-Running"} else { Write-Host "CheckInService-GTCC is Running"}
if (!$b){ Write-Host "CheckInService-PG is Not-Running"} else { Write-Host "CheckInService-PG is Running" }
