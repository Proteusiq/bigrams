# if commit messages contain feat: --> minor, if ! --> major, everything else --> patch

import subprocess
from typing import Literal


def next_version() -> Literal["patch", "minor", "major"]:

    cmd = "git describe --tags --abbrev=0 | xargs -I'{}'  git log {}...HEAD --pretty=format:%s"  # noqa: E501
    with subprocess.Popen(cmd, stdout=subprocess.PIPE, shell=True) as p:
        res = p.communicate()

    commit_messages = res[0].decode("utf-8").split("\n")

    MAJOR = 3
    MINOR = 2
    PATCH = 1
    BREAKING_CHANGE_MARKER = "!"
    COMMIT_TYPE_SCORES = {"feat": MINOR, "!": MAJOR}
    VERSION_BUMP_TYPES = {PATCH: "patch", MINOR: "minor", MAJOR: "major"}

    def extract_commit_type(message):
        conventional_commit_type = message.split(":")[0]
        if conventional_commit_type.endswith(BREAKING_CHANGE_MARKER):
            return BREAKING_CHANGE_MARKER
        return conventional_commit_type

    normalized_commit_types = [
        extract_commit_type(message) for message in commit_messages
    ]

    max_score = max(
        [COMMIT_TYPE_SCORES.get(commit, 1) for commit in normalized_commit_types]
    )

    return VERSION_BUMP_TYPES.get(max_score)


if __name__ == "__main__":
    print(next_version())  # noqa T201
