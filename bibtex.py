#!/usr/bin/env python
import os
import argparse
import re

def arguments():
    parser = argparse.ArgumentParser(
        description='Grab a bibtex file, strip some fields out of it and write the result to a directory.')
    parser.add_argument(type=str, nargs=1,
                   help='Input file.',
                   dest="infile")
    parser.add_argument(type=str, nargs=1,
                   help='Output directory.',
                   dest="outdir")
    parser.add_argument(type=str, nargs="*",
    			   default=[],
                   help='Fields to strip.',
                   dest="fields")
    args = parser.parse_args()
    return args

def strip_field(field_name, bibtex):
	"""
	Strip a field out of a bibtex file string.
	"""
	reg = "%s.*,\n" % field_name
	return re.sub(reg, "", bibtex)

def do_sync(in_file, out_dir, strip_fields):
	path, fname = os.path.split(in_file)
	with open(in_file, "r") as f:
		bibtex = f.read()
	for field in strip_fields:
		bibtex = strip_field(field, bibtex)
	target = os.path.join(out_dir, fname)
	with open(target, "w") as f:
		f.write(bibtex)

if __name__ == "__main__":
	args = arguments()
	print "Copying %s to %s." % (args.infile[0], args.outdir[0])
	print "Removing fields: " + " ".join(args.fields)
	do_sync(args.infile[0], args.outdir[0], args.fields)
	print 'Done.'

