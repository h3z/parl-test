# 环境准备

```
conda activate parl

export LC_ALL=C.UTF-8
export LANG=C.UTF-8
export PWD=`pwd`
export LD_LIBRARY_PATH=$LD_LIBRARY_PATH:./lib64
python yml_creator.py --dataset_path $PWD/data
```

# 单进程

```
python train.py
```

# 200 个进程

```
xparl start --port 8010 --cpu_num 200
python train_parl.py --actor_num 200
```

# 其他问题

* too many open file
    * `ulimit -n 204800`

# 图构造
* `test.py` 中有所有搜集的信息和构造的图。
* 图的构造过程在 `parl_baseline/graph/graph.py` 里边可以修改边的方向。