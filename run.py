import argparse
import pinboard
import sys
import yaml

_base_dir = sys.path[0]

cfg = yaml.load(open(_base_dir+"/config.yaml", "r"), Loader=yaml.FullLoader)

parser = argparse.ArgumentParser(description='Capitalize Pinboard tags.')
parser.add_argument('old_name')
parser.add_argument('new_name', nargs="?")
parser.add_argument('--dry-run', action='store_true',
                    help="Perform a dry run, doesn't change anything.")
parser.add_argument('-U', '--upper', action='store_true',
                    help="Renames the tag to an UPPERCASE string.")
args = parser.parse_args()

old_name = args.old_name
if args.new_name is not None:
    new_name = args.new_name
elif args.upper:
    new_name = args.old_name.upper()
else:
    new_name = args.old_name.capitalize()

# Check if dry run
if args.dry_run:
    print("DRY RUN? "+str(args.dry_run))

# Set up Pinboard client
pb = pinboard.Pinboard(cfg['api_token'])
print("Old tag name: "+old_name)
print("New tag name: "+new_name)

# Change the tag name
if not args.dry_run:
    pb.tags.rename(old=old_name, new=new_name)
