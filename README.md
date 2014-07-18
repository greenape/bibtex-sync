Very simple python script to copy a bibtex file and strip out some fields.

I use this in combination with https://github.com/alandipert/fswatch to make working between Mendeley and LaTeX less painful -

	#!/bin/bash
	bibtex.py /path/to/your/library.bib /path/to/copy/to fields to strip

And call like so:

	fswatch-run /path/to/your/library.bib bibsync.sh