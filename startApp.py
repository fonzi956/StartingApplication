import webbrowser, subprocess
 
vscode = "/usr/bin/code"
subprocess.Popen("%s" % (vscode))

webbrowser.open('http://google.co.kr', new=2)
quit()