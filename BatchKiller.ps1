Disable-ScheduledTask -TaskName BatchRestarter
get-wmiobject win32_process | where commandline -match PGPLM| where commandline -match CheckInService.bat | remove-wmiobject
get-wmiobject win32_process | where commandline -match GTCC| where commandline -match CheckInService.bat | remove-wmiobject
