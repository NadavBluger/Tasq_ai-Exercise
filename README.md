Tasq.ai Exercise

A Simple python script joining two ro more JSON files into one.
The script is called from the cli and takes the following arguments:

help:

      -h, --help            shows help message and exits

directory:

      -d "path", --directory "path"
                        A path to a directory containing the JSON files to be joined.
                        Mutually exclusive with path. Can not be the working directory of the script

path:

      -p "path1" "path2" ..., --paths "path1" "path2" ...
                        A list of paths to the JSON files to be joined. Mutually exclusive with directory

mode

      -m {Tagged,CommaSeparated}, --mode {Tagged,CommaSeparated}
                        Whether to join the JSON files with commas or as keys of values (tags).
                        Whether the output file will be on the top level a dict or a list

output

      -o "path", --output "path"
                        The location for the output file


For example with a file containing {"what is this?": "a dict"} and another containing ["what is this?", "a list"]

and the script called like so:

python main.py -p "C:\Users\nblug\PycharmProjects\Tasq_ai Exercise\files\file_one.json" "C:\Users\nblug\PycharmProjects\Tasq_ai Exercise\files\file_two.txt"  -m "Tagged"

will result in a file containing {"file_one.json": {"what is this?": "a dict"}, "file_two.txt": ["what is this?", "a list"]}

With a directory in thw working dir of the script containing the files and the script called like so:
python main.py -d "./files" -m "CommaSeparated"

will result in a file containing [{"what is this?": "a dict"}, ["what is this?", "a list"]]

Important Note all file names must end with .txt or .json