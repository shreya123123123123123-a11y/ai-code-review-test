import ast


def analyze_python_code(file_path):

    issues = []

    try:
        with open(file_path, "r") as file:
            code = file.read()

        tree = ast.parse(code)

        for node in ast.walk(tree):

            if isinstance(node, ast.FunctionDef):

                if len(node.body) > 20:
                    issues.append(
                        {
                            "type": "complexity",
                            "line": node.lineno,
                            "message": "Function is too long"
                        }
                    )


            if isinstance(node, ast.Import):

                for name in node.names:

                    if name.name == "os":
                        issues.append(
                            {
                                "type": "security",
                                "line": node.lineno,
                                "message": "Check usage of os module"
                            }
                        )


    except Exception as e:

        issues.append(
            {
                "type": "error",
                "message": str(e)
            }
        )


    return issues