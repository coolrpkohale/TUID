    '\\': lambda c: c,  # FOR "\ no newline at end of file
                if (
                    line.startswith("new file mode") or
                    line.startswith("deleted file mode") or
                    line.startswith("index ") or
                    line.startswith("diff --git")
                ):