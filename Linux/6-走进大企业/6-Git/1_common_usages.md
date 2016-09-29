# git的常用语句

## 1. git配置用户名和邮箱
	git config --global user.name "Your Name"
	git config --global user.email "email address"

## 2. 在本地创建一个仓库
	mkdir learn_git
	cd learn_git
	git init

## 3. 添加文件到仓库
	touch common_usage.md //一定要放在当前的仓库目录下面
	git add common_usage.md
	git commit -m "create a file that named common_usage"

## 4. 查看当前的状态
	git status
	git diff //如果想查看文件具体修改了那些地方，可以使用这个命令也可以在后面添加具体的文件名, 如下
	diff --git a/readme.md b/readme.md
	index 46d49bf..9247db6 100644
	--- a/readme.md
	+++ b/readme.md
	@@ -1,2 +1,2 @@
	-Git is a version control system.
	+Git is a distributed version control system.
	 Git is free software.

	* a、要随时掌握工作区状态，使用git status命令
	* b、如果git status告诉你是有文件被修改了，那么可以使用git diff file_name查看具体修改的内容

## 5. 查看最近的提交日志
	git log
	e.g.
	# git log 
	commit 3ee85e93eca255a060cbe8ef4a28d15375bf6658
	Author: hienha <hienha@163.com>
	Date:   Tue Aug 2 22:38:47 2016 +0800

	append GPL

	commit 06e4b54afcc98aa7099d31d15360014ba4cf5f74
	Author: hienha <hienha@163.com>
	Date:   Tue Aug 2 22:37:32 2016 +0800

	modified the first line.

	commit 2ee012e5e9adc12187fce89a9a65fc928cffbae1
	Author: hienha <hienha@163.com>
	Date:   Tue Aug 2 22:35:23 2016 +0800

	create a readme.md file and commit it

## 6. 回退到之前的版本
	git reset --hard HEAD^ 		//回退到上一个版本
	e.g.
		 git reset --hard HEAD^
		 HEAD is now at 06e4b54 modified the first line. //这里的06e4b54就是上个版本的开头的前几个字符，表示提交的版本号e.g.
	git reset --hard HEAD^^		//回退到倒数第二个版本
	git reset --hard HEAD~100	//回退到倒数第100个版本
	git reset --hard commit_number //回退到指定的版本号，前提是这个版本号是真实存在的，并且有记录的
	e.g.
		git reset --hard 3ee85e93eca255a060cbe8ef4a28d15375bf6658
		HEAD is now at 3ee85e9 append GPL
		cat readme.md
		Git is a distributed version control system.
		Git is free software distributed under the GPL.
	git reflog					//查看之前的命令历史，当然也可以回到之前操作的状态，因为这里的commit number记录的
	e.g. 
		3ee85e9 HEAD@{0}: reset: moving to 3ee85e93eca255a060cbe8ef4a28d15375bf6658
		2ee012e HEAD@{1}: reset: moving to 2ee012e5e9adc12187fce89a9a65fc928cffbae1
		06e4b54 HEAD@{2}: reset: moving to HEAD^
		3ee85e9 HEAD@{3}: commit: append GPL
		06e4b54 HEAD@{4}: commit: modified the first line.
		2ee012e HEAD@{5}: commit (initial): create a readme.md file and commit it

## git checkout -- file_name的用法，其实git checkout就是用版本库里的版本来替换工作区中的版本的，无论是修改还是删除都可以一键恢复
	### checkout会把你工作区的文件内容恢复到最后一迟提交的状态，比如你晚上提交了一次，第二天早上修改了文件，但是发现还是昨天的文件是最完美的状态，你现在想恢复到昨天的状态，这个时候你就可以使用git checkout 来恢复到昨天的文件内容了
	不过前提是你没有推到远程的版本库中，不然你真的惨了
	适合运用在以下的场景
	1、当你改乱了工作区的某个内容，想直接德育工作区的修改，可以直接使用git checkout -- file_name
	2、当你不但乱改了整个工作区的文件内容，还添加到了暂存区(git commit -m "commit comment")，想丢弃修改，这个时候就需要分两步进行了
		a、git reset HEAD file，这个时候就又回到了场景一
		b、参考场景1来修改
	3、已经提交了不合适的修改到版本库时,想要撤销本次提交,参考版本回退一节,不过前提是没有推送到远程库。

	### 假如新创建一个文件test.txt文件，但是一不小心把这个文件删除了，这个时候有两种选择
		a、git rm test.txt; git commit -m "I really remove the test file." //这个时候就真的删除了
		b、git checkout -- test.txt //这样又可以把文件恢复到工作区里

# git远程仓库
	## 把本地和远程仓库关联起来(先有本地，和远程的仓库关联起来)
	mkdir git_repo_name; cd !$
	git init
	echo "# This file is the readme." > README.md
	git add README.md
	git commit -m "first commit" 
	git remote add origin git@git_server:path/repo-name.git //与远程仓库关联
	git push -u origin master //第一次推送master分支的所有内容
	git push origin master //后续就不需要再加-u参数了

	## 先创建远程仓库，然后克隆到本地仓库，(这个我最在行了 ，一般也是这么干的
	
# git冲突解决

git log --graph --pretty=oneline --abbrev-commit
*   27ecd92 fixed conflict
|\  
| * 903ef98 AND simple
* | e0e575b & simple by master
|/  
* 5a3fdf1 create a new branch named dev
* 79e1383 2016-08-04 first commit and push to the remote repositories.
