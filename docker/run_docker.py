import subprocess


def run_code():

    result = subprocess.run(
        [
            "docker",
            "run",
            "code-runner"
        ],
        capture_output=True,
        text=True
    )

    return {
        "output": result.stdout,
        "error": result.stderr
    }


if __name__ == "__main__":

    result = run_code()

    print(result)