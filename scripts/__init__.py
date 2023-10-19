import os


def list_files_and_paths(src_path, test_path, prefix="test_"):
    for root, dirs, files in os.walk(src_path):
        if "__pycache__" in dirs:
            dirs.remove("__pycache__")
        dirs[:] = [d for d in dirs if not d.startswith(prefix)]

        for file in files:
            if file.endswith(".py") and file != "__init__.py":
                file_path = os.path.join(root, file)

                # Strip out the base directory from the file path
                file_path = file_path.replace(src_path, "", 1)

                # Replace directory separators with underscores
                file_path_modified = file_path.replace(os.sep, "_")

                # If file_path_modified starts with an underscore, remove it
                if file_path_modified.startswith("_"):
                    file_path_modified = file_path_modified[1:]

                test_file_path = os.path.join(test_path, prefix + file_path_modified)

                # Check if the test file already exists. If not, create it
                if not os.path.exists(test_file_path):
                    with open(test_file_path, "w") as f:
                        f.write("")  # Create an empty file


if __name__ == "__main__":
    src_folder_path = "../src"
    tests_folder_path = "../tests"
    list_files_and_paths(src_folder_path, tests_folder_path)
