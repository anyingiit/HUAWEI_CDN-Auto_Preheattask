import executeCommand
a = "s\n"
b = "s\n"
c = executeCommand.websitelocaGitlCommandDef("git rev-parse master")[1]
d = executeCommand.websitelocaGitlCommandDef("git rev-parse origin/master")[1]
e = '8ec500d60307ac5f3bd227e95158eabf29fe44a2'
f = '8ec500d60307ac5f3bd227e95158eabf29fe44a2'
print(a is b)
print(c is d)
print(e is f)