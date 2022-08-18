cp ../parl_baseline/agent.py .
cp ../parl_baseline/grid_agent.py .
cp ../parl_baseline/grid_model.py .
cp ../parl_baseline/model .

sed -i '_bak' 's/parl_baseline.//g' agent.py
rm agent.py_bak
