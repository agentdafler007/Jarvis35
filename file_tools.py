import os
import json
import shutil
import csv

class FileTools:
    @staticmethod
    def read_file(file_path):
        try:
            with open(file_path, 'r') as file:
                return file.read()
        except FileNotFoundError:
            return f"Error: File {file_path} not found."
        except Exception as e:
            return f"Error reading file: {str(e)}"

    @staticmethod
    def write_file(file_path, content):
        try:
            with open(file_path, 'w') as file:
                file.write(content)
            return f"Content successfully written to {file_path}"
        except Exception as e:
            return f"Error writing to file: {str(e)}"

    @staticmethod
    def append_to_file(file_path, content):
        try:
            with open(file_path, 'a') as file:
                file.write(content)
            return f"Content successfully appended to {file_path}"
        except Exception as e:
            return f"Error appending to file: {str(e)}"

    @staticmethod
    def read_json(file_path):
        try:
            with open(file_path, 'r') as file:
                return json.load(file)
        except json.JSONDecodeError:
            return f"Error: {file_path} is not a valid JSON file."
        except FileNotFoundError:
            return f"Error: File {file_path} not found."
        except Exception as e:
            return f"Error reading JSON file: {str(e)}"

    @staticmethod
    def write_json(file_path, data):
        try:
            with open(file_path, 'w') as file:
                json.dump(data, file, indent=4)
            return f"JSON data successfully written to {file_path}"
        except Exception as e:
            return f"Error writing JSON to file: {str(e)}"

    @staticmethod
    def list_files(directory):
        try:
            return os.listdir(directory)
        except FileNotFoundError:
            return f"Error: Directory {directory} not found."
        except Exception as e:
            return f"Error listing files: {str(e)}"

    @staticmethod
    def create_directory(directory):
        try:
            os.makedirs(directory, exist_ok=True)
            return f"Directory {directory} created successfully."
        except Exception as e:
            return f"Error creating directory: {str(e)}"

    @staticmethod
    def delete_file(file_path):
        try:
            os.remove(file_path)
            return f"File {file_path} deleted successfully."
        except FileNotFoundError:
            return f"Error: File {file_path} not found."
        except Exception as e:
            return f"Error deleting file: {str(e)}"

    @staticmethod
    def move_file(source, destination):
        try:
            shutil.move(source, destination)
            return f"File moved from {source} to {destination} successfully."
        except FileNotFoundError:
            return f"Error: Source file {source} not found."
        except Exception as e:
            return f"Error moving file: {str(e)}"

    @staticmethod
    def copy_file(source, destination):
        try:
            shutil.copy2(source, destination)
            return f"File copied from {source} to {destination} successfully."
        except FileNotFoundError:
            return f"Error: Source file {source} not found."
        except Exception as e:
            return f"Error copying file: {str(e)}"

    @staticmethod
    def get_file_size(file_path):
        try:
            size = os.path.getsize(file_path)
            return f"The size of {file_path} is {size} bytes."
        except FileNotFoundError:
            return f"Error: File {file_path} not found."
        except Exception as e:
            return f"Error getting file size: {str(e)}"

    @staticmethod
    def file_exists(file_path):
        return os.path.exists(file_path)

    @staticmethod
    def read_csv(file_path):
        try:
            with open(file_path, 'r', newline='') as file:
                reader = csv.reader(file)
                return list(reader)
        except FileNotFoundError:
            return f"Error: File {file_path} not found."
        except Exception as e:
            return f"Error reading CSV file: {str(e)}"

    @staticmethod
    def write_csv(file_path, data):
        try:
            with open(file_path, 'w', newline='') as file:
                writer = csv.writer(file)
                writer.writerows(data)
            return f"Data successfully written to CSV file {file_path}"
        except Exception as e:
            return f"Error writing to CSV file: {str(e)}"

    @staticmethod
    def get_file_extension(file_path):
        return os.path.splitext(file_path)[1]

    @staticmethod
    def rename_file(old_name, new_name):
        try:
            os.rename(old_name, new_name)
            return f"File renamed from {old_name} to {new_name} successfully."
        except FileNotFoundError:
            return f"Error: File {old_name} not found."
        except Exception as e:
            return f"Error renaming file: {str(e)}"