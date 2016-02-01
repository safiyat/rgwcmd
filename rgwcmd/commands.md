# commands.py structure

```
command_list                                                           [dict, 2]
  |
  |----dest                                                            [unicode]
  ∟----commands                                                        [list, 3]
         |
	 ∟----[user, keys, caps]                                       [dict, 3]
	        |
		|----function                                          [unicode]
		|----dest                                              [unicode]
		∟----subcommands                                   [list, 2 4 4]
		     |
		     ∟--[(create,update,rm,info), (add,rm), (add,rm)]  [dict, 1]
		           |
			   ∟----arguments          [list, (9 9 2 1) (4 2) (2 2)]
			          |
				  |
				  ∟----[uid, display-name, ...]           [dict]
```
