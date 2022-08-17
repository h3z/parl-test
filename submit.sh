cp parl_baseline/agent.py submission
cp parl_baseline/grid_agent.py submission
cp parl_baseline/grid_model.py submission
cp parl_baseline/model submission

sed -i '_bak' 's/parl_baseline.//g' submission/agent.py
rm submission/agent.py_bak
