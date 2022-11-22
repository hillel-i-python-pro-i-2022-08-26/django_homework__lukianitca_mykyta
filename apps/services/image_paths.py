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


def _split_file_name(filename: str) -> list:
    return filename.rsplit(".", maxsplit=1)


def get_avatar_path_user(instance, avatar: str):
    _, extension = _split_file_name(avatar)
    return (
        f"users/user/avatar/"
        f"{_generate_pseudo_id(amount_of_iterations=4)}/"
        f"{_generate_pseudo_id(amount_of_iterations=1)}/"
        f"avatar.{extension}"
    )


def get_contact_photo_path(instance, contact_photo: str):
    _, extension = _split_file_name(contact_photo)
    return (
        f"contacts/contact/photo/"
        f"{_generate_pseudo_id(amount_of_iterations=4)}/"
        f"{_generate_pseudo_id(amount_of_iterations=1)}/"
        f"photo.{extension}"
    )
