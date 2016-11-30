## Preface
假如只有一个主分支的时候，即master，HEAD严格来讲并不是指向提交，而是指向master，master才是指向提交的，
so，HEAD指向的就是当前分支
一开始的时候，master分支是一条线，git用master指向最新的提交，HEAD再指向master，就能确定当前分支，以及当前分支的提交点

##创建分支
	git checkout -b dev
		
	git checkout -b表示创建分支的同时切换到分支上，也就相当于下面的两条命令
	git branch dev //创建一个分支
	git checkout dev //切换到新的分支上
					
##查看分支
列出所有的分支
	git branch
当我们创建新的分支，例如dev时，git就创建了一个指针dev，指向master相同的提交，再把HEAD指向dev，这样就表示当前的分支在dev上，其实，要判断当前在那个分支上，就看HEAD指向谁
这样，创建分支就是HEAD指针改变指向，工作区没有变化，当我们再提交新的内容时，master分支保持不变，而dev则向前移动一个步长，就在提交的进时候发生的


##切换分支
	git checkout master //git checkout branch_name
	当再切换到master分支上时，再来查看我们刚刚在dev分支上修改过的readme.md文件，咦，怎么刚刚修改的内容不见了？
	其实也很好理解，因为刚才我们在dev分支上的时候HEAD指针指向的是dev，而不是master，所以提交的是dev分支，而我们现在切换到master分支后，则还是上次创建dev时的状态。
	##分支合并
	假如我们在dev上的工作完成了，就可以把dev和master分支进行合并了，
		git merge dev //这个一定是其它的分支 git merge other_branch
