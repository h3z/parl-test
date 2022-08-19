<!-- TOC -->
* [一，节点分分类](#)
* [二，观测空间](#)
* [三，静态空间](#)
<!-- TOC -->

# 一，节点分分类
1. 发电机组: gen, 54 个  
   1. 新能源 18 个，特有属性   
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