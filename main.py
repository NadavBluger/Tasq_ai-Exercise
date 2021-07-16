import argparse
import json
import pathlib
from os import listdir


def fetch_file(path):
    """Retrieve to contents of a JSON file and validating it"""
    try:
        with open(path, mode="r") as file:
            return json.loads(file.read())
    except json.decoder.JSONDecodeError:
        print(f"Failed to process {path} because it is not a valid JSON file")
    except FileNotFoundError:
        print(f"Failed to process {path} because it does not exists")
    except Exception as err:
        print(f"Failed to process {path} due to {err}")


def fetch_files_dir(dir_path):
    """Gather the contents and names of all JSON file in a given Directory"""
    return [(fetch_file(f"{dir_path}/{file}"), file.split(".")[0]) for file in listdir(dir_path)
            if file[-3:] == "txt" or file[-4:] == "json"]


def fetch_files_path_list(path_list):
    """Gather the contents and names of all JSON file in a given list of paths"""
    return [(fetch_file(str(path)), str(path).split("\\")[-1]) for path in path_list
            if str(path)[-3:] == "txt" or str(path)[-4:] == "json"]


def output_list(output_path, json_list):
    """Join a list of JSONs into a list and write to file"""
    with open(str(output_path)+"/output.json", mode="w") as output:
        print(json_list)
        output.write(json.dumps([file[0] for file in json_list]))


def output_dict(output_path, json_list):
    """Join a list of JSONs into a dict and write to file"""
    with open(str(output_path)+"/output.json", mode="w") as output:
        output.write(json.dumps({tag: file for file, tag in json_list}))


def parser_setup():
    """Setup an command line arguments parser"""
    parser = argparse.ArgumentParser()
    files_source_group = parser.add_mutually_exclusive_group(required=True)
    files_source_group.add_argument("-d",
                                    "--directory",
                                    type=pathlib.Path,
                                    help="A path to a directory containing the JSON files to be joined."
                                         " Mutually exclusive with path."
                                         " Can not be the working directory of the script")
    files_source_group.add_argument("-p",
                                    "--paths",
                                    type=pathlib.Path,
                                    nargs="+",
                                    help="A list of paths to the JSON files to be joined."
                                         " Mutually exclusive with directory")
    parser.add_argument("-m",
                        "--mode",
                        type=str,
                        choices=["Tagged", "CommaSeparated"],
                        help="Whether to join the JSON files with commas or as keys of values (tags)."
                             " Whether the output file will be on the top level a dict or a list",
                        default="CommaSeparated",
                        required=False)
    parser.add_argument("-o",
                        "--output",
                        type=pathlib.Path,
                        help="The location for the output file",
                        default="./")
    return parser


def main():
    argument_parser = parser_setup()
    arguments = argument_parser.parse_args().__dict__
    if arguments["directory"]:
        files = fetch_files_dir(arguments["directory"])
    else:
        files = fetch_files_path_list(arguments["paths"])
    if arguments["mode"] == "Tagged":
        output_dict(arguments["output"], files)
    else:
        output_list(arguments["output"], files)
    print(f"Your unified file is ready at {arguments['output']}")


if __name__ == '__main__':
    main()
