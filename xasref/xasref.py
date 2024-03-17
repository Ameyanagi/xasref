import os

import matplotlib.pyplot as plt
import numpy as np

from larch import Group
from larch.io import read_athena
from larch.xafs import pre_edge

root_directory = os.path.join(os.path.dirname(__file__), "../")

# The refenences collected and stored as a athena files.
# This dictionary is used to generate the dat files including the energy, mu, and reference.
#
# The e0 is determined by the first derivative of the mu and caliberated to the tabulated value.
# This energy alignment must be done in athena file.
foil_dict_athena = [
    {
        "element": "Ag",
        "path": "foil/Agfoil.prj",
        "dat_path": "foil/Ag foil Ag K.dat",
        "group": "Agfoil_x18b",
        "edge": "K",
        "e0": 25514,
    },
    {
        "element": "Au",
        "path": "foil/Aufoil_QAS.prj",
        "dat_path": "foil/Au foil Au L3.dat",
        "group": "Au_foil",
        "edge": "L3",
        "e0": 11919,
    },
    {
        "element": "Cd",
        "path": "foil/Cdfoil_QAS.prj",
        "dat_path": "foil/Cd foil Cd K.dat",
        "group": "Cd_foil",
        "edge": "K",
        "e0": 26711,
    },
    {
        "element": "Co",
        "path": "foil/Cofoil_QAS.prj",
        "dat_path": "foil/Co foil Co K.dat",
        "group": "Co_foil",
        "edge": "K",
        "e0": 7709,
    },
    {
        "element": "Cr",
        "path": "foil/Crfoil_QAS.prj",
        "dat_path": "foil/Cr foil Cr K.dat",
        "group": "Cr_foil",
        "edge": "K",
        "e0": 5989,
    },
    {
        "element": "Cu",
        "path": "foil/Cufoil_QAS.prj",
        "dat_path": "foil/Cu foil Cu K.dat",
        "group": "Cu_foil",
        "edge": "K",
        "e0": 8979,
    },
    {
        "element": "Fe",
        "path": "foil/Fefoil_QAS.prj",
        "dat_path": "foil/Fe foil Fe K.dat",
        "group": "Fe_foil",
        "edge": "K",
        "e0": 7112,
    },
    {
        "element": "In",
        "path": "foil/Infoil.prj",
        "dat_path": "foil/In foil In K.dat",
        "group": "InFoil",
        "edge": "K",
        "e0": 27940,
    },
    {
        "element": "Mn",
        "path": "foil/Mnfoil.prj",
        "dat_path": "foil/Mn foil Mn K.dat",
        "group": "Mnfoil_x18b",
        "edge": "K",
        "e0": 6539,
    },
    {
        "element": "Mo",
        "path": "foil/Mofoil_QAS.prj",
        "dat_path": "foil/Mo foil Mo K.dat",
        "group": "Mo_foil",
        "edge": "K",
        "e0": 20000,
    },
    {
        "element": "Ni",
        "path": "foil/Nifoil_QAS.prj",
        "dat_path": "foil/Ni foil Ni K.dat",
        "group": "Ni_foil",
        "edge": "K",
        "e0": 8333,
    },
    {
        "element": "Pd",
        "path": "foil/Pdfoil_QAS.prj",
        "dat_path": "foil/Pd foil Pd K.dat",
        "group": "Pd_foil",
        "edge": "K",
        "e0": 24350,
    },
    {
        "element": "Pt",
        "path": "foil/Ptfoil.prj",
        "dat_path": "foil/Pt foil Pt L3.dat",
        "group": "Ptfoil",
        "edge": "L3",
        "e0": 11564,
    },
    {
        "element": "Re",
        "path": "foil/Refoil.prj",
        "dat_path": "foil/Re foil Re L3.dat",
        "group": "Re_Foil__001",
        "edge": "L3",
        "e0": 10535,
    },
    {
        "element": "Rh",
        "path": "foil/Rhfoil_QAS.prj",
        "dat_path": "foil/Rh foil Rh K.dat",
        "group": "Rh_foil",
        "edge": "K",
        "e0": 23220,
    },
    {
        "element": "Ru",
        "path": "foil/Rufoil_QAS.prj",
        "dat_path": "foil/Ru foil Ru K.dat",
        "group": "Ru_foil",
        "edge": "K",
        "e0": 22117,
    },
    {
        "element": "Sn",
        "path": "foil/Snfoil.prj",
        "dat_path": "foil/Sn foil Sn K.dat",
        "group": "Snfoil_x18b",
        "edge": "K",
        "e0": 29200,
    },
    {
        "element": "V",
        "path": "foil/Vfoil_QAS.prj",
        "dat_path": "foil/V foil V K.dat",
        "group": "V_foil",
        "edge": "K",
        "e0": 5465,
    },
    {
        "element": "W",
        "path": "foil/Wfoil.prj",
        "dat_path": "foil/W foil W K.dat",
        "group": "wfoil_x19a",
        "edge": "K",
        "e0": 10207,
    },
    {
        "element": "Zn",
        "path": "foil/Znfoil.prj",
        "dat_path": "foil/Zn foil Zn K.dat",
        "group": "Znfoil_x18b",
        "edge": "K",
        "e0": 9659,
    },
    {
        "element": "Zr",
        "path": "foil/Zrfoil_QAS.prj",
        "dat_path": "foil/Zr foil Zn K.dat",
        "group": "Zr_foil",
        "edge": "K",
        "e0": 17998,
    },
]


# A function to plot the foil data and the reference data.
#
# The references and the tabulated e0 values are plotted and saved as a png file in order to check the alignment of the e0.
def plot_foil(
    group: Group, ref_e0: float, label: str | None = None, save_path: str | None = None
):
    group.e0 = ref_e0
    pre_edge(group)
    fig, ax = plt.subplots()
    ax.plot(group.energy, group.mu, label=group.label)

    # use the second axis
    ax2 = ax.twinx()
    ax2.plot(group.energy, group.dmude, label="first derivative", color="r")
    ax.axvline(group.e0, color="r", linestyle="--", label="e0")
    ax.axvline(ref_e0, color="g", linestyle="--", label="ref_e0")
    ax.set_xlabel("Energy (eV)")
    ax.set_ylabel("$\mu")
    ax2.set_ylabel("First derivative")
    ax.legend()
    ax.set_xlim(group.e0 - 20, group.e0 + 80)

    if save_path:
        os.makedirs(os.path.dirname(save_path), exist_ok=True)
        fig.tight_layout()

        fig.savefig(save_path, dpi=300)

    else:
        plt.show()


# A function to print the e0 and the reference e0.
# This is used to check the e0 alignment.
def print_e0(group: Group, ref_e0: float, label: str | None = None):
    pre_edge(group)

    if label:
        print(f"{label}:\t{group.e0}\tref:{ref_e0}")
    else:
        print(f"{group.label}: {group.e0}")


# A function to save the group data as a dat file.
def save_group_dat(group: Group, ref_e0: float, filename: str | None = None):
    group.e0 = ref_e0
    pre_edge(group)

    if filename is None:
        filename = f"{group.label}.dat"

    np.savetxt(
        filename,
        np.vstack(
            (
                group.energy,
                group.mu,
                group.dmude,
            )
        ).T,
        header="energy mu dmude",
    )


# A function to generate the dat files from the reference athena files.
def generate_foil_dat():
    for foil in foil_dict_athena:
        foil_path = os.path.join(root_directory, foil["path"])
        group = read_athena(foil_path)[foil["group"]]
        save_group_dat(
            group,
            foil["e0"],
            filename=foil["dat_path"],
        )


# A function to read the reference dat files and store them as a dictionary.
#
# Arguments:
#   None
#
# Returns:
#   ref_dict (dict[dict]): A dictionary containing the reference data.
#       keys: "element edge"
#       child_keys:
#           "element": Element of interest
#           "group": Larch group of the spectra
#           "edge": Edge (K, L3, L2, L1, and ...)
#           "e0": Edge energy
#           "path": The path of the original file
#           "label": Label of the spectrum
#           "dat_path": The path of the dat file
def get_ref_dict() -> dict[str, dict]:
    ref_dict = {}

    for ref in foil_dict_athena:
        data = np.loadtxt(os.path.join(root_directory, ref["dat_path"]))
        group = Group(energy=data[:, 0], mu=data[:, 1])
        group.label = f"{ref['element']} foil {ref['element']}  {ref['edge']}"

        ref_dict[f"{ref['element']} {ref['edge']}"] = {
            "element": ref["element"],
            "group": group,
            "edge": ref["edge"],
            "e0": ref["e0"],
            "path": ref["path"],
            "label": f"{ref['element']} foil {ref['element']}  {ref['edge']}",
            "dat_path": ref["dat_path"],
        }

    return ref_dict


# A function to read the reference dat files for validation
def check_foil_dat():
    ref_dict = get_ref_dict()

    for key, foil in ref_dict.items():
        save_dir = os.path.dirname(os.path.join(root_directory, foil["path"]))

        save_plot_path = os.path.join(
            save_dir,
            "./img/",
            f"{foil['element']} foil {foil['element']}  {foil['edge']}.png",
        )

        print(f"{key}:\te0:{foil['e0']}")
        print(f"Plotting {key}")

        plot_foil(
            foil["group"],
            foil["e0"],
            label=f"{foil['element']} {foil['edge']}",
            save_path=save_plot_path,
        )


def main():
    # for foil in foil_dict:
    #     group = read_athena(foil["path"])[foil["group"]]
    #
    #     # plot_foil(group, foil["e0"], label=f"{foil['element']} {foil['edge']}")
    #     print_e0(group, foil["e0"], label=f"{foil['element']} {foil['edge']}")

    pass


if __name__ == "__main__":
    generate_foil_dat()
    check_foil_dat()
