class PATranslator:
    """
    Class responsible for handling subtitle text extraction, chunking, and preparation
    of request bodies for translation.
    """

    @staticmethod
    def read_file(file_path):
        """
        Reads a file and returns its content as a list of strings.

        Args:
            file_path (str): The path to the file to read.

        Returns:
            list: A list of lines in the file if successful, None if an error occurs.
        """
        try:
            with open(file_path, "r", encoding="utf-8") as file:
                content = file.readlines()
                return content # Returns a list of strings
        except FileNotFoundError:
            print(f"File not found: {file_path}")
        except PermissionError:
            print(f"You do not have permission to access: {file_path}")
        except Exception as e:
            print(f"An unexpected error occurred: {e}")

    @staticmethod
    def extract_text_lines(subs):
        """
        Extracts text lines from a subtitle file, skipping empty lines or lines that
        start with digits.

        Args:
            subs (list): A list of lines from the subtitle file.

        Returns:
            list: A list of lines containing only the text to translate.
        """
        lines_to_translate = []
        for line in subs:
            if line == "\n":
                continue
            if not line[0].isdigit():
                line = line.strip()
                lines_to_translate.append(line)

        return lines_to_translate #Returns list of strings

    @staticmethod
    def split_into_chunks(text, max_chars=5000):
        """
        Splits text into chunks with a maximum character length, ensuring no chunk
        splits words in the middle.

        Args:
            text (str): The text to split into chunks.
            max_chars (int): The maximum number of characters per chunk. Defaults to 5000.

        Returns:
            list: A list of text chunks.
        """
        text = text.strip()
        chunks = []
        chunk = text[:max_chars]
        while len(text) >= max_chars:
            # check if the last char is in the middle of a word
            if not text[max_chars] == " ":
                chunk = chunk[:chunk.rfind(" ")].strip()

            chunks.append(chunk)
            start_index = len(chunk)
            text = text[start_index:]
            chunk = text[:max_chars]
        # append last chunk
        chunks.append(chunk)

        return chunks

    @staticmethod
    def group_lines_into_chunks(lines, max_chars=5000):
        """
        Groups lines of text into chunks with a specified maximum character length.

        Args:
            lines (list): A list of lines of text.
            max_chars (int): The maximum number of characters per chunk. Defaults to 5000.

        Returns:
            list: A list of chunks formed from the lines.
        """

        chunks = []
        chunk = ""

        for line in lines:
            potential_chunk = chunk + line
            if len(potential_chunk) >= max_chars:
                split, remainder = potential_chunk.rsplit(" ", 1)
                chunks.append(split)
                chunk = remainder
            else:
                chunk = potential_chunk

        if chunk:
            chunks.append(chunk)

        return chunks

    @staticmethod
    def prepare_request_body(chunks):
        """
        Prepares a request body by formatting chunks into a list of dictionaries, because
        that is what Azure's API is expecting

        Args:
            chunks (list): A list of text chunks.

        Returns:
            list: A list of dictionaries, each containing a chunk of text.
        """
        request_body = [{"Text": chunk} for chunk in chunks]
        return request_body