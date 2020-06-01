import argparse
import coloredlogs
import logging

from challenge.challenge import GitExtractor


def main(args):
    ge = GitExtractor(repo=args.input_repo,
                      folder=args.input_name,
                      props=args.input_props)
    for file, result in ge.files():
        logging.info(f"For the file {file} extracted:")
        logging.info(result)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Compares 2 perf summary')
    parser.add_argument('-r', '--repo', dest='input_repo',
                        help='url to the repo  ie: https://github.com/mitre/cti', required=True)
    parser.add_argument('-f', '--folder', dest='input_name',
                        help='folder inside the repo, where the jsons are located, ie:enterprise-attack/attack-pattern',
                        required=True)
    parser.add_argument('-p', '--props', nargs='+', dest="input_props",
                        help='List of arguments to extract from the jsons'
                             ' ie:  "id", "objects[0].name", "objects[0].kill_chain_phases""',
                        required=True)
    input_args = parser.parse_args()
    coloredlogs.install()
    main(input_args)
