"""Console script for xasref."""
import os
import sys

import click

from .xasref import check_foil_dat, generate_foil_dat, root_directory


@click.command()
@click.option("-h", "--help", is_flag=True)
@click.option("-g", "--generate", is_flag=True)
@click.option("-c", "--check", is_flag=True)
def main(help, generate, check):
    if help:
        click.echo("This is a command line interface for the xasref package.")
        click.echo("The options are:")
        click.echo("-h, --help: print this help message")
        click.echo(
            "-g, --generate: generate the foil.dat file from the original source"
        )
        click.echo(
            "-c, --check: check the foil.dat file, print the e0, and plot the spectra"
        )
        return 0

    if generate:
        generate_foil_dat()

    if check:
        check_foil_dat()
        print(f"The plots are saved in {os.path.join(root_directory, './foil/img/')}")

    return 0


if __name__ == "__main__":
    sys.exit(main())  # pragma: no cover
