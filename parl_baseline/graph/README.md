<!-- TOC -->
* [一，节点分类和数量](#)
* [二，观测空间](#)
* [三，静态空间](#)
* [四，图特征构造](#)
<!-- TOC -->

# 一，节点分类和数量
1. 发电机组: gen, 54 个  
   1. 新能源 18 个
   2. 火电 35 个  
   3. 平衡机 1 个  
2. 负载: load，91 个  
   1. 可调 10 个  
   2. 储能 5 个  
   3. 普通 76 个  
3. bus，126 个  
4. branch_or & branch_ex, 194 个 (其中 9 个没有值)

# 二，观测空间
1. gen
	1. 共有
		* gen_p
		* gen_q
		* gen_v
		* gen_status
		* actual_dispatch
		* steps_to_close_gen
		* steps_to_recover_gen
		* target_dispatch
	2. 新能源
		* nextstep_renewable_gen_p_max
		* curstep_renewable_gen_p_max
2. load
	1. 共有
		* curstep_ld_p
		* ld_p
		* ld_q
		* ld_v
		* nextstep_ld_p
	2. 可调
		* adjld_p
		* total_adjld
	3. 储电
		* stoenergy_p
		* total_stoenergy
3. bus
	1. 共有
		* bus_v
4. branch
	1. 共有
		* a_ex
		* a_or
		* p_ex
		* p_or
		* q_ex
		* q_or
		* rho
		* steps_to_reconnect_line
		* v_ex
		* v_or
		* count_soft_overflow_steps
		* line_status

# 三，静态空间
1. gen
	1. 共有
		* gen_p_a
		* gen_p_b
		* gen_p_c
		* gen_p_d
		* gen_type
		* gen_p_max
		* gen_p_min
		* gen_q_max
		* gen_q_min
		* gen_v_max
		* gen_v_min
2. load
	1. 共有
		* ld_type
	1. 可调
		* adjld_a
		* adjld_b
		* adjld_c
		* adjld_capacity
		* adjld_uprate
		* adjld_dnrate
	2. 储电
		* stoenergy_k
		* stoenergy_b
		* stoenergy_name
		* stoenergy_capacity
		* stoenergy_chargerate_max
		* stoenergy_dischargerate_max
3. bus
	1. 共有
		* bus_v_max
		* bus_v_min
4. branch
	1. 共有
		* ln_thermal_limit
		* white_list_random_disconnection

# 四，图特征构造
特种数量统计：
* 发电机组, 共 **10** 个不同观测特征
	* 火电和平衡节点: **8** 个观测特征
	* 新能源节点: **8+2** 个观测特征
* 负载节点, 共 **9** 个不同观测特征
	* 普通节点: **5** 个观测特征
	* 可调节点: **5+2** 个观测特征
	* 储电节点: **5+2** 个观测特征
* bus, 共 **1** 个观测特征
* branch, 共 **12** 个观测特征


由于图中每个节点类别不同，对应特征数量也不同。需要通过填零来对其特征向量。
暂定使用这些特征，按这个顺序拼接
* 0~9 存储发电机组信息
* 10~18 存储负载信息
* 19 存 bus 信息
* 20~31 branch 信息

具体的
```python
[
# gen
'gen_p',
'gen_q',
'gen_v',
'gen_status',
'actual_dispatch',
'steps_to_close_gen',
'steps_to_recover_gen',
'target_dispatch',
'nextstep_renewable_gen_p_max',
'curstep_renewable_gen_p_max',

# load
'curstep_ld_p',
'ld_p',
'ld_q',
'ld_v',
'nextstep_ld_p',
'adjld_p',
'total_adjld',
'stoenergy_p',
'total_stoenergy',

# bus
'bus_v',

# branch
'a_ex',
'a_or',
'p_ex',
'p_or',
'q_ex',
'q_or',
'rho',
'steps_to_reconnect_line',
'v_ex',
'v_or',
'count_soft_overflow_steps',
'line_status',
]
```

