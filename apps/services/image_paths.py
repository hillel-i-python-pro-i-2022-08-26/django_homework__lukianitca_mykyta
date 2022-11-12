import base64
import uuid


def _generate_pseudo_id(amount_of_iterations: int = 3) -> str:
    if amount_of_iterations <= 0:
        raise ValueError(f'Please provide positive amount of iterations. Current: "{amount_of_iterations}"')

    return (
        base64.urlsafe_b64encode(b"".join(uuid.uuid4().bytes for _ in range(amount_of_iterations)))
        .decode()
        .replace("=", "")
    )


def get_avatar_path_user(instance, avatar: str):
    _, extension = avatar.rsplit(".", maxsplit=1)
    return (
        f"users/user/avatar/"
        f"{_generate_pseudo_id(amount_of_iterations=4)}/"
        f"{_generate_pseudo_id(amount_of_iterations=1)}/"
        f"avatar.{extension}"
    )
