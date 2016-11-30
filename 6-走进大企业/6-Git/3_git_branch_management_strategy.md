##创建一个分支 
	git branch -d dev
	git checkout -b dev

##修改内容并提交
	git add readme.md
	git commit -m "add merge with dev"

##切换到master分支
	git checkout master

##使用--no-ff参数来进行合并，表示禁用fast forward，默认就是使用这种快进模式
	git merge --no-ff -m "merge with --no-ff option, This option will be generate a new commit" dev

##使用git log来查看分支历史
	git log --graph --pretty=oneline --abbrev-commit
	[root@unexpress learn_git]# git log --graph --pretty=oneline --abbrev-commit
	*   0f5d094 merge with no-ff option
	|\  
	| * 73d0d15 merge with no-ff
	|/  
	*   ff283ad conflict fixed
	|\  
	| * 90391ed only see first line and changed and to AND
	* | 85e5c2b changed laster line by master
	* |   346f288 Merge branch 'feature1'
	|\ \  
	| |/  
	| * 1a458a1 feature1 delete some lines.
	* | c199b85 add some lines.
	|/  
	* 2c3e1ac & simple
	* 12412c9 AND simple
	*   77fec30 conflict fixed
	|\  
	| * 3b521d1 dev branch changed this file too.
	* | a3d7b28 delete some network interface.
	|/  
	* 3393a30 This file is created by dev branch.
	* 7861b3f add some file 2_create_merge_branch.md
	* ccafc5f create a new branch name is dev
	* ad3131b commit remark as a backup
	* 79e1383 2016-08-04 first commit and push to the remote repositories.
