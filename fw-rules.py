def chkeckAdmin():
    try:
        isAdmin = ctypes.windll.shell32.IsUserAnAdmin()
    except AttributeError:
        isAdmin = False
    if not isAdmin:
        ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, __file__, None, 1)

#def addRule(ruleName, filePath):
#    # Add new rule to Windows Firewall
#    subprocess.run("netsh advfirewall firewall add rule name="+ ruleName +" dir=out action=block enable=no program=" + filePath, shell=True, stdout=DEVNULL, stderr=DEVNULL)
#    print("Rule", ruleName, "for", filePath, "added")

#def modifyRule(ruleName, state):
#    # Edit specific rule, Disable = 0 | Enable = 1
#    if state:
#        subprocess.run("netsh advfirewall firewall set rule name="+ ruleName +" dir=out new enable=yes", shell=True, stdout=DEVNULL, stderr=DEVNULL)
#        print("Rule", ruleName, "Enabled")
#    else:
#        subprocess.run("netsh advfirewall firewall set rule name="+ ruleName +" dir=out new enable=no", shell=True, stdout=DEVNULL, stderr=DEVNULL)
#        print("Rule", ruleName, "Disabled")

# This way allows to enter rules names with spaces
def editRule(ruleName, enabled=True):
    # Edit specific rule, Disable = 0 | Enable = 1
    subprocess.run(
        [
            'netsh', 'advfirewall', 'firewall',
            'set', 'rule', f'name={ruleName}',
            'dir=out', # choose inbound or ourbound, comment out for both
            'new', f'enable={"yes" if enabled else "no"}',
        ],
        check=True,
        stdout=DEVNULL,
        stderr=DEVNULL
    )

chkeckAdmin()
#addRule("ruleName", "filePath")
editRule("443 - Dell Open Manage", 1)
