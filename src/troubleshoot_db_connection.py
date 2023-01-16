from app.context import get_context
from dotenv import load_dotenv
from rich import print
from app.business_objects.repositories._sc_repository import SecurityCenterRepositories


def main():
    sc_repos = SecurityCenterRepositories()
    for item in sc_repos.get({}):
        print(item)


if __name__ == "__main__":
    load_dotenv()
    main()
