##前言
	软件开发过程中，肯定会遇到bug，有了问题肯定就要修复，所以bug可以通过一个临时的分支来修复，然后再把这个临时的分支给删除就可以了
	当你接到一个代号为101的bug任务时，非常自然的你就想要创建一个名为bug_fix_branch来解决它，但是问题来了，你在dev上的项目还没有提交，这个时候你工作只进行到一半，预计需要一天的时间，但是这个bug又需要在2个小时内必须搞定，怎么办？？？
	git提供了一个stash的功能，可以暂时的把你当前的工作现场“储存”起来，等以后恢复现场再来使用。

##把当前的工作现场保存起来
		# git stash
		Saved working directory and index state WIP on dev: 73d0d15 merge with no-ff
		HEAD is now at 73d0d15 merge with no-ff
		[root@unexpress learn_git]# git checkout master
		Switched to branch 'master'
	
###创建一个新的分支
		# git checkout -b bug_fix_branch
		Switched to a new branch 'bug_fix_branch'

		# vim readme.md 
		# git add readme.md 
		# git commit -m "fixed bug 101"
		[bug_fix_branch 250adce] fixed bug 101
		 1 files changed, 3 insertions(+), 0 deletions(-)

###切换到master分支上
		# git checkout master
 		Switched to branch 'master'
		
###合并分支的时候创建一个新的提交
		# git merge --no-ff -m "merged bug fix 101" bug_fix_branch
 		Merge made by recursive.
 		 readme.md |    3 +++
 		  1 files changed, 3 insertions(+), 0 deletions(-)

		# cat readme.md 
 		  Git is a distributed version control system.
 		  Git is free software distributed under the GPL.
 		  last version
	
 		  2016-09-02 20:26
 	  	Creating a new branch is so quick.
	
 		  2016-09-05 22:21
 	  	git branch management policement

   		2016-09-05 22:50
   		create a new branch named by bug_fix_branch
   
###解决完bug后，删除临时分支
		# git branch -d bug_fix_branch
   		Deleted branch bug_fix_branch (was 250adce).

###切换到dev分支上
	# git checkout dev
   Switched to branch 'dev'
	
	# git status
   # On branch dev
   nothing to commit (working directory clean)

###查看保存起来的分支列表
	# git stash list
   stash@{0}: WIP on dev: 73d0d15 merge with no-ff

###把存储起来的分支恢复现场
####这里有两种方式来恢复
* 1. git stash pop //内存恢复后，stash内容也一并删除了
* 2. git stash apply //这种方式，stash内容并不会删除
	# git stash pop
   Removing common_usages.md
   # On branch dev
   # Changed but not updated:
   #   (use "git add/rm <file>..." to update what will be committed)
   #   (use "git checkout -- <file>..." to discard changes in working directory)
   #
   #	deleted:    common_usages.md
   #
   no changes added to commit (use "git add" and/or "git commit -a")
   Dropped refs/stash@{0} (ee77d30792ef6e38cbad1ff89405be84e4db839a)

###可以进行多次stash操作，但是恢复的时候一定要先用 git stash list查看，然后恢复指定的stash，用下面的命令
	git stash apply stash@{0} //猜测，这里的0类似于数组的下标，如果要恢复第2个stash，那么就使用git stash apply stash@{1}

##好了，你现在可以正常工作了
