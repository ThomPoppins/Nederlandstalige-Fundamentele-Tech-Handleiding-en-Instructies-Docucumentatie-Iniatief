### Install Chocolatey for Individual Use:

1. First, ensure that you are using an **_[administrative shell](https://www.howtogeek.com/194041/how-to-open-the-command-prompt-as-administrator-in-windows-10/)_** - you can also install as a non-admin, check out [Non-Administrative Installation](https://docs.chocolatey.org/en-us/choco/setup#non-administrative-install).
2. Install with powershell.exe
    
    **NOTE**
    
    Please inspect [https://community.chocolatey.org/install.ps1](https://community.chocolatey.org/install.ps1) prior to running any of these scripts to ensure safety. We already know it's safe, but you should verify the security and contents of **_any_** script from the internet you are not familiar with. All of these scripts download a remote PowerShell script and execute it on your machine. We take security very seriously. [Learn more about our security protocols](https://docs.chocolatey.org/en-us/information/security).
    
    With PowerShell, you must ensure [Get-ExecutionPolicy](https://go.microsoft.com/fwlink/?LinkID=135170) is not Restricted. We suggest using `Bypass` to bypass the policy to get things installed or `AllSigned` for quite a bit more security.
    
    - Run `Get-ExecutionPolicy`. If it returns `Restricted`, then run `Set-ExecutionPolicy AllSigned` or `Set-ExecutionPolicy Bypass -Scope Process`.
    
    Now run the following command:
    
    >
    
3. Paste the copied text into your shell and press Enter.
4. Wait a few seconds for the command to complete.
5. If you don't see any errors, you are ready to use Chocolatey! Type `choco` or `choco -?` now, or see [Getting Started](https://docs.chocolatey.org/en-us/getting-started) for usage instructions.