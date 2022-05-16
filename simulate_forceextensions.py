import numpy as np
import os
import pandas as pd

# SPECIFY E2E VALUES (note that this is not the same as extension)
# Unbound extensions
#e2e_vals =  [6.0  , 6.2 , 6.4 , 6.6]
#e2e_names = ['6p0','6p2','6p4','6p6']
#probe_state = "unbound"

# Bound extensions
#e2e_vals =  [ 6.4 , 6.5 , 6.6 , 6.7]
#e2e_names = ['6p4','6p5','6p6','6p7']
#probe_state = "bound"

# Middle 1 bp extensions
#e2e_vals =  [6.5,6.75,7,7.25,7.5]
#e2e_names = ['6p5','6p75','7','7p25','7p5']
#probe_state = "middle"

# End 1 bp extension
#e2e_vals =  [6.5,6.625, 6.75, 6.875,7]
#e2e_names = ['6p5','6p625','6p75','6p875','7']
#probe_state = "end"

for idx,e2e_val in enumerate(e2e_vals):
	# MODIFY INPUT FILE FOR GIVEN E2E VAL
	f = open('inputMD_'+probe_state,'r')
	lines = f.readlines()
	f.close()
	lines[28] = "topology = "+probe_state+".top\n" #LOAD PRE- GENERATED UNBOUND CONF
	lines[29] = "conf_file = "+probe_state+".conf\n" #LOAD PRE- GENERATED UNBOUND CONF
	lines[30] = "lastconf_file = "+probe_state+"_"+e2e_names[idx]+"_last.conf\n"
	lines[31] = "trajectory_file = "+probe_state+"_trajectory_"+e2e_names[idx]+".dat\n"
	lines[47] = "name = "+probe_state+"_distance_"+e2e_names[idx]+".dat\n"
	lines[56] = "name = "+probe_state+"_distance2_"+e2e_names[idx]+".dat\n"
	#lines[60] = "name = forces_"+e2e_names[idx]+".dat\n"
	f = open('inputMD_'+probe_state,'w')
	f.writelines(lines)
	f.close()
	
	# MODIFY FORCE FILE FOR GIVEN E2E VAL
	f = open('force_'+probe_state+'.conf','r')
	lines = f.readlines()
	f.close()
	lines[5]  = 'r0 = '+str(e2e_val)+'\n'
	lines[13] = 'r0 = '+str(e2e_val)+'\n'
	f = open('force_'+probe_state+'.conf','w')
	f.writelines(lines)
	f.close()
	
	# SIMULATE E2E_VAL
	os.system('~/oxDNA_2.4_RJUNE2019/oxDNA/build/bin/oxDNA inputMD_'+probe_state)
	os.system('~/oxDNA_2.4_RJUNE2019/oxDNA/build/bin/DNAnalysis inputMD_'+probe_state)
