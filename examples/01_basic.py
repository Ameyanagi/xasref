import matplotlib.pyplot as plt
from xasref import get_ref_dict


ref = get_ref_dict()
fe_k_group = ref["Fe K"]["group"]
plt.plot(fe_k_group.energy, fe_k_group.mu)
plt.show()
