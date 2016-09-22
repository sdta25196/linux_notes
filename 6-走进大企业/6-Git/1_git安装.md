##git安装
```
yum install -y epel-release
yum install -y git
```

##git配置
```
git config --global user.name "your_name"
git config --global user.email "example@example.com"
```
上面的命令执行成功后，会在自己当前用户的家目录生成一个.gitconfig的文件
```
cat $HOME/.gitconfig
[user]
	name = xxxxxx
	email = xxxxxx@xxx.xxx
```
